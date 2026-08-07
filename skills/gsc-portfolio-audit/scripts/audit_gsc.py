#!/usr/bin/env python3
"""Portfolio-wide Google Search Console audit.

  portfolio  every property ranked by clicks, with period-over-period deltas
  queries    per-site new / rising / dropping / lost / low-CTR keywords

Needs GOOGLE_GSC_CLIENT_ID, GOOGLE_GSC_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN in the
environment (or GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET). The refresh token must have
been issued for the SAME OAuth client you pair it with, or the token endpoint returns
`unauthorized_client` — the most common setup failure when an account has more than one
Google OAuth client.

Scope required: https://www.googleapis.com/auth/webmasters.readonly
"""
import argparse, os, sys, datetime as dt
from concurrent.futures import ThreadPoolExecutor

import requests

SITES_URL = "https://www.googleapis.com/webmasters/v3/sites"
# Properties to leave out of reports, e.g. domains you no longer control, so their
# decay isn't misread as a ranking problem. Set GSC_EXCLUDE="a.com,b.com" to populate.
EXCLUDE = {s.strip() for s in os.environ.get("GSC_EXCLUDE", "").split(",") if s.strip()}


def creds():
    cid = os.environ.get("GOOGLE_GSC_CLIENT_ID") or os.environ.get("GOOGLE_CLIENT_ID")
    sec = os.environ.get("GOOGLE_GSC_CLIENT_SECRET") or os.environ.get("GOOGLE_CLIENT_SECRET")
    tok = os.environ.get("GOOGLE_REFRESH_TOKEN")
    if not all((cid, sec, tok)):
        sys.exit("ERROR: set GOOGLE_GSC_CLIENT_ID, GOOGLE_GSC_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN")
    return cid, sec, tok


def auth_header():
    cid, sec, tok = creds()
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": cid, "client_secret": sec,
        "refresh_token": tok, "grant_type": "refresh_token"}, timeout=30)
    if not r.ok:
        sys.exit(f"ERROR: token refresh failed ({r.status_code}): {r.text[:200]}\n"
                 "If this is `unauthorized_client`, the refresh token belongs to a different "
                 "OAuth client than the id/secret you supplied.")
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def periods(days):
    end = dt.date.today() - dt.timedelta(days=3)  # GSC lags ~3 days
    return ((end - dt.timedelta(days=days - 1), end),
            (end - dt.timedelta(days=days * 2 - 1), end - dt.timedelta(days=days)))


def query(h, site, rng, dimensions=(), limit=1):
    url = f"{SITES_URL}/{requests.utils.quote(site, safe='')}/searchAnalytics/query"
    r = requests.post(url, headers=h, json={
        "startDate": str(rng[0]), "endDate": str(rng[1]),
        "dimensions": list(dimensions), "rowLimit": limit}, timeout=60)
    r.raise_for_status()
    return r.json().get("rows") or []


def all_sites(h):
    r = requests.get(SITES_URL, headers=h, timeout=30)
    r.raise_for_status()
    return [s["siteUrl"] for s in r.json().get("siteEntry", [])
            if s["siteUrl"] not in EXCLUDE and short(s["siteUrl"]) not in EXCLUDE]


def short(site):
    return site.replace("sc-domain:", "").replace("https://", "").replace("http://", "").rstrip("/")


def pct(now, prev):
    if prev == 0:
        return "  new" if now else "    -"
    return "   0%" if now == prev else f"{(now - prev) / prev * 100:+.0f}%"


def cmd_portfolio(args, h):
    p1, p0 = periods(args.days)

    def one(site):
        try:
            def tot(rng):
                rows = query(h, site, rng) or [{}]
                return rows[0].get("clicks", 0), rows[0].get("impressions", 0)
            c1, i1 = tot(p1)
            c0, i0 = tot(p0)
            return {"site": site, "c1": c1, "i1": i1, "c0": c0, "i0": i0}
        except Exception as exc:
            return {"site": site, "err": str(exc)[:70]}

    with ThreadPoolExecutor(10) as ex:
        res = list(ex.map(one, all_sites(h)))
    bad = [r for r in res if "err" in r]
    res = [r for r in res if "err" not in r]
    res.sort(key=lambda r: (-r["c1"], -r["i1"]))

    print(f"last {args.days}d: {p1[0]} .. {p1[1]}   vs prior: {p0[0]} .. {p0[1]}\n")
    print(f"{'#':>3}  {'property':34} {'clicks':>9} {'Δ':>7}   {'impressions':>13} {'Δ':>7}")
    print("-" * 82)
    for n, x in enumerate(res, 1):
        print(f"{n:>3}  {short(x['site']):34} {x['c1']:>9,} {pct(x['c1'], x['c0']):>7}"
              f"   {x['i1']:>13,} {pct(x['i1'], x['i0']):>7}")
    t = lambda k: sum(x[k] for x in res)
    print("-" * 82)
    print(f"{'':3}  {'TOTAL':34} {t('c1'):>9,} {pct(t('c1'), t('c0')):>7}"
          f"   {t('i1'):>13,} {pct(t('i1'), t('i0')):>7}")
    if EXCLUDE:
        print(f"\nexcluded: {', '.join(sorted(EXCLUDE))}")
    if bad:
        print("\nerrors:")
        for b in bad:
            print(f"  {short(b['site'])}: {b['err']}")
    return res


def cmd_queries(args, h, sites=None):
    p1, p0 = periods(args.days)
    sites = sites or all_sites(h)

    def one(site):
        a = {r["keys"][0]: r for r in query(h, site, p1, ["query"], 25000)}
        b = {r["keys"][0]: r for r in query(h, site, p0, ["query"], 25000)}
        f = args.min_clicks
        new = [(k, v["clicks"], v["impressions"], v["position"]) for k, v in a.items()
               if v["clicks"] >= f and b.get(k, {}).get("clicks", 0) == 0]
        rise = [(k, v["clicks"], b[k]["clicks"], v["position"], b[k]["position"]) for k, v in a.items()
                if k in b and b[k]["clicks"] >= f
                and v["clicks"] >= b[k]["clicks"] * 1.5 and v["clicks"] - b[k]["clicks"] >= f * 4]
        drop = [(k, v["clicks"], b[k]["clicks"], v["position"], b[k]["position"]) for k, v in a.items()
                if k in b and b[k]["clicks"] >= f * 10 and v["clicks"] <= b[k]["clicks"] * 0.6]
        gone = [(k, v["clicks"], v["position"]) for k, v in b.items()
                if k not in a and v["clicks"] >= f * 6]
        ctr = [(k, v["clicks"], v["impressions"], v["position"]) for k, v in a.items()
               if v["impressions"] >= 1500 and v["position"] <= 10
               and v["clicks"] / v["impressions"] < 0.02]
        new.sort(key=lambda x: -x[1])
        rise.sort(key=lambda x: -(x[1] - x[2]))
        drop.sort(key=lambda x: -(x[2] - x[1]))
        gone.sort(key=lambda x: -x[1])
        ctr.sort(key=lambda x: -x[2])
        n = args.limit
        return site, new[:n], rise[:n], drop[:n], gone[:n], ctr[:n]

    with ThreadPoolExecutor(6) as ex:
        for site, new, rise, drop, gone, ctr in ex.map(one, sites):
            print(f"\n{'=' * 78}\n{short(site)}")
            if not any((new, rise, drop, gone, ctr)):
                print("  (no query clears the thresholds - traffic is fragmented long tail"
                      " or anonymized by Google)")
            for title, rows, fmt in (
                ("NEW (no clicks in prior period)", new,
                 lambda r: f"    {r[1]:>6,} clicks {r[2]:>8,} impr  pos {r[3]:5.1f}   {r[0][:58]}"),
                ("RISING", rise,
                 lambda r: f"    {r[2]:>6,} -> {r[1]:>6,}  pos {r[4]:5.1f}->{r[3]:5.1f}   {r[0][:58]}"),
                ("DROPPING", drop,
                 lambda r: f"    {r[2]:>6,} -> {r[1]:>6,}  pos {r[4]:5.1f}->{r[3]:5.1f}   {r[0][:58]}"),
                ("LOST (no data now)", gone,
                 lambda r: f"    was {r[1]:>6,} clicks pos {r[2]:5.1f}   {r[0][:58]}"),
                ("CTR GAP (ranks well, few clicks -> rewrite title/description)", ctr,
                 lambda r: f"    {r[1]:>6,} clicks {r[2]:>8,} impr  pos {r[3]:5.1f}   {r[0][:58]}"),
            ):
                if rows:
                    print(f"  {title}:")
                    for r in rows:
                        print(fmt(r))


def main():
    ap = argparse.ArgumentParser(description="Audit all Google Search Console properties")
    ap.add_argument("command", choices=["portfolio", "queries", "full"], nargs="?", default="full")
    ap.add_argument("--days", type=int, default=28, help="window; compared against the window before it")
    ap.add_argument("--site", action="append", help="restrict to these properties (repeatable)")
    ap.add_argument("--limit", type=int, default=12, help="rows per section")
    ap.add_argument("--min-clicks", type=int, default=5, help="ignore queries below this many clicks")
    ap.add_argument("--top", type=int, default=12, help="full: how many properties get a query breakdown")
    args = ap.parse_args()

    h = auth_header()
    if args.command == "portfolio":
        cmd_portfolio(args, h)
    elif args.command == "queries":
        cmd_queries(args, h, args.site)
    else:
        ranked = cmd_portfolio(args, h)
        cmd_queries(args, h, args.site or [r["site"] for r in ranked[:args.top]])


if __name__ == "__main__":
    main()
