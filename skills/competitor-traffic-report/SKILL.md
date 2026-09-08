---
name: competitor-traffic-report
description: Build an interactive competitive-traffic report for any company and its rivals — monthly visits (SimilarWeb), organic search traffic and Domain Rating (Ahrefs) — as one self-contained HTML page with ranked charts, a three-month trend, a multi-year overlay and a data table. Use when asked to benchmark a product against competitors, size up a market, answer "how much traffic does X get compared to Y", build a competitive landscape, or produce a traffic/authority comparison deck or page.
---

# competitor-traffic-report

Three metrics, three different questions. Do not average them or treat one as a proxy for another:

| Metric | Source | Answers |
|---|---|---|
| Monthly visits | SimilarWeb | total demand, every channel |
| Organic traffic | Ahrefs | how much of it search is producing |
| Domain Rating | Ahrefs | backlink authority — the structural position |

Visits and organic move on a single viral page. **DR does not**, which is why a gap in DR says
more about where a company actually sits than a good traffic month does.

## Run

```bash
export AHREFS_API_KEY=...   # required
export BRANDDEV_API_KEY=...  # optional, for logos
S=skills/competitor-traffic-report/scripts

node $S/fetch-traffic.js acme.com rival1.com,rival2.com,rival3.com --out /tmp/data.json
node $S/build-report.js /tmp/data.json "AI presentation tools, ranked" --out /tmp/report.html
```

Open the HTML, or publish it with the **Artifact** tool. It is self-contained — logos inlined as
data URIs, no external requests — so it survives a strict CSP.

The focus domain is coloured orange and ranked in every chart; competitors take a five-step blue
ramp ordered by rank, so colour carries magnitude instead of being decoration.

## Choosing the competitor set

Whoever asked usually names three or four. Fill the set out to **20–40** before running: a
five-company chart cannot show where anyone sits, and the interesting findings (how much of the
market one player holds, how many are shrinking) need the tail. Sources for names, cheapest first:

- the client's own "alternatives to X" and comparison pages;
- an `X alternatives` / `best X tools` SERP, read deep enough to reach the top 100;
- Ahrefs `competitors_overview` for domains ranking on the same keywords.

Drop anything that is not a real peer: a general-purpose giant (Adobe, Google) dominates every
chart while competing for none of the same buyers, and its presence compresses everyone else into
the bottom decile. Same for a friendly company the requester does not consider a rival — ask.

**Subdomains are already counted.** SimilarWeb's root-domain figure includes them, so listing both
`acme.com` and `app.acme.com` double-counts and buries the real number. (Verified: wikipedia.org
3.53B vs en.wikipedia.org 0.88B.) List the root only.

## Constraints worth knowing before the first run

- **SimilarWeb rate-limits by IP**, roughly 15 calls per window, and the block lasts hours. The
  script paces at 15s and still misses on a long list — rerun to fill gaps, or spread a 40-domain
  set across two sessions. The `X-Extension-Version` header is mandatory; a browser User-Agent
  alone returns 403.
- **A returned `0` means "below SimilarWeb's detection floor", not "no traffic".** The template
  drops those from the charts rather than ranking a live site last. For a domain you own, read
  Search Console instead.
- **Ahrefs organic uses `mode=subdomains`.** Domain mode silently excludes the `www.` host, which
  reads as an empty site for anyone whose canonical is `www.`.
- **The free DR endpoint costs no API units.** Organic history does — one row per month per domain.

## Publishing the report

The Ahrefs licence (`ahrefs.com/legal/domain-rating-license`) grants a royalty-free right to
display and publish DR data **provided** the attribution *Domain Rating by [Ahrefs](https://ahrefs.com/)*
appears next to it with a live link. The template ships that line; do not remove it. The same
licence prohibits reselling the data or using it to build something that competes with Ahrefs.

## Reading the result

The report shows position. The story is usually in a gap between two of the three metrics:

- **Organic rank far above visits rank** — search is carrying more than its share; paid, social or
  direct is the thin part.
- **DR far above organic** — the authority is there and the content is not converting it. This is
  the most actionable gap, because it is a content problem, not a link-building one.
- **DR far below peers at similar traffic** — the traffic is bought or borrowed, and it stops the
  moment spend stops.
- **A near-identical name at a fraction of the DR** (`brand.app` at DR 87 vs `brand.com.ai` at 38)
  is a copycat domain, not a competitor.

State the denominator and the window beside any figure taken from this report. Both sources are
modelled estimates, least reliable exactly where it matters most — the small end.
