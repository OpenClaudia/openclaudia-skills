---
name: similarweb-traffic
description: Fetch website traffic estimates (monthly visits, traffic sources, top countries, keywords, engagement, ranks) for any domain from SimilarWeb. Use when the user asks about a domain's traffic, monthly visits, traffic sources, audience countries, or wants to compare/benchmark sites against competitors.
---

# SimilarWeb Traffic

Fetch traffic-overview estimates for any domain — monthly visits, traffic-source breakdown, top countries, top keywords, engagement metrics, and global/category ranks.

## When to Use This Skill

Use this skill when the user:

- Asks how much traffic a domain gets ("what's the traffic for X")
- Wants monthly visit trends for a site
- Needs a traffic-source breakdown (organic vs direct vs paid vs GenAI, etc.)
- Wants to know a site's audience countries
- Wants to compare/benchmark several domains against each other or competitors

## Usage

No API key required. Self-contained Node script (uses built-in `fetch`, no `npm install`).

```bash
node scripts/fetch-similarweb-traffic.js <domain>
```

Examples:
```bash
# Formatted markdown summary (default)
node scripts/fetch-similarweb-traffic.js chatslide.ai

# Raw normalized JSON (for further processing / comparisons)
node scripts/fetch-similarweb-traffic.js stripe.com --json
```

The domain can be passed bare (`example.com`) or as a URL (`https://www.example.com/pricing`) — it gets normalized (strips scheme, `www.`, and path).

### Comparing multiple domains

Run the script once per domain with `--json` and combine the results into a table. Add a short delay between calls to be polite to the endpoint.

## Output

Default mode prints a markdown summary: a metrics table (monthly visits, ranks, bounce, pages/visit, time on site), a monthly-visits trend line, traffic-source breakdown, top countries, and top keywords.

`--json` mode prints a normalized object:

```json
{
  "domain": "stripe.com",
  "globalRank": 327,
  "categoryRank": 21,
  "category": "Finance",
  "snapshotMonth": "2026-05",
  "visits": 122394040,
  "bounceRate": 0.55,
  "pagesPerVisit": 3.26,
  "timeOnSite": 165.9,
  "estimatedMonthlyVisits": [{ "date": "2026-03-01", "visits": 118067753 }],
  "trafficSources": { "searchOrganic": 0.48, "direct": 0.23, "...": 0 },
  "topCountries": [{ "countryCode": "US", "value": 0.087 }],
  "topKeywords": ["..."]
}
```

`visits` is the most recent complete month. Rates (`bounceRate`, all `trafficSources`, `topCountries[].value`) are 0–1 fractions.

## API Details

- Endpoint: `https://data.similarweb.com/api/v1/data?domain=<domain>` — SimilarWeb's **undocumented public data endpoint** (the one their browser extension uses). No auth, no key, free.
- Requires a browser `user-agent` header (the script sends one) — default `curl`/bot agents are blocked.
- Synchronous, returns immediately.

## Important Notes

- **Estimates, not ground truth.** SimilarWeb models traffic; numbers can be off, especially for mid/low-traffic sites. For a domain you own, your own Google Analytics / Search Console data is authoritative — prefer those when available.
- **Unknown domains return zeros, not an error.** SimilarWeb responds HTTP 200 with all-zero/synthetic data when it has no data for a domain. If every visit count is 0, treat it as "no SimilarWeb data."
- **Unofficial endpoint.** It can be rate-limited, change shape, or require auth without notice; this is a gray-area use of SimilarWeb's data outside their paid API.
- Exit codes: `2` network error, `3` non-200 HTTP response.
