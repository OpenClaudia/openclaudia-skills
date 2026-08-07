---
name: gsc-portfolio-audit
description: >
  Audit EVERY Google Search Console property at once — rank all sites by clicks and
  impressions with period-over-period deltas, then diff keywords per site to surface what
  is newly ranking, rising, dropping, lost, or ranking well without earning clicks.
  Built for agencies and multi-site owners. Use when asked to compare all sites, rank
  properties by traffic, find new keywords across a portfolio, or spot which site is down.
  Trigger phrases: "audit GSC", "all my sites", "rank my properties", "portfolio search
  performance", "which sites are down", "what new keywords are we ranking for",
  "client site performance", "GSC report across accounts".
  For ONE site's queries, pages, or index coverage, use the search-console skill instead.
---

# GSC Portfolio Audit

Answers "how is everything doing?" across every property on a Search Console account, which is the question the per-site tooling can't answer without dozens of manual exports.

## Setup

Requires an OAuth refresh token with `https://www.googleapis.com/auth/webmasters.readonly`:

```bash
export GOOGLE_GSC_CLIENT_ID=...      # or GOOGLE_CLIENT_ID
export GOOGLE_GSC_CLIENT_SECRET=...  # or GOOGLE_CLIENT_SECRET
export GOOGLE_REFRESH_TOKEN=...
export GSC_EXCLUDE="olddomain.com"   # optional, comma-separated
pip install requests
```

**The most common setup failure is `unauthorized_client` on token refresh.** It means the refresh token was issued for a different OAuth client than the id/secret you paired with it. Accounts that have added Google integrations over time usually have several clients; match the pair that minted the token.

## Run it

```bash
python3 scripts/audit_gsc.py            # full: ranking + keyword diff for the top 12
python3 scripts/audit_gsc.py portfolio  # just the ranked table
python3 scripts/audit_gsc.py queries --site sc-domain:example.com
python3 scripts/audit_gsc.py --days 90  # quarter over quarter
```

Flags: `--days` (window, compared against the window immediately before it), `--site` (repeatable), `--top`, `--limit`, `--min-clicks`.

## Sections and what they mean

| Section | Read it as |
|---|---|
| NEW | queries with zero clicks last period. Where growth is actually coming from. |
| RISING | up ≥50%. Check whether position moved too — if it didn't, demand rose, not your ranking. |
| DROPPING | down ≥40% off a real base. **Position tells you which kind:** rank fell = ranking loss; rank held but clicks collapsed = something took the clicks above you (AI Overview, a new SERP feature, or the query changed shape). |
| LOST | ranked before, no data now. |
| CTR GAP | ≥1,500 impressions, top 10, under 2% CTR. Title and description rewrites, the cheapest wins available. |

## Interpreting

- **Report clicks first, impressions second.** One large property can swing portfolio impressions enough to mask that everything else grew.
- **Separate brand from non-brand.** A site whose entire keyword set is its own name (or misspellings of a competitor's) has no acquisition engine, however good the click count looks. Say so plainly in the report.
- **A whole-site collapse on its own head term is usually not SEO.** Check ownership before diagnosing rankings: `whois <domain> | grep -i "registrar\|updated date"` plus whether it still resolves. Expired, transferred, or disputed domains produce a textbook ranking cliff that no amount of SEO work will fix.
- **"new" in the portfolio table means zero clicks in the prior window**, which for a recently launched site is a launch, not a data gap.
- **Don't skip queries in languages you can't read.** On multi-market sites the growth is usually in non-English long tail; translate the interesting ones rather than filtering them out.
- A property returning 403 is verified for listing but not for search analytics. The script reports it instead of hiding it.

## Notes

- GSC data lags about 3 days; the script offsets for this automatically.
- Both periods are fetched per property in parallel, so a 40-property account takes seconds.
- Query rows are capped at 25,000 per period, well above what any single site returns for a 28-day window.
