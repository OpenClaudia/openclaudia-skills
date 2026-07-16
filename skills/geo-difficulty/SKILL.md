---
name: geo-difficulty
description: "Score how hard a keyword is to rank for in the AI-search era — page-level URL Rating of real competitors (not just domain DR), Ahrefs keyword difficulty, and whether a given site already ranks or is cited in Google's AI Overview. Use when the user asks 'how hard is <keyword> to rank', 'geo difficulty for <keyword>', or 'keyword difficulty for <domain>'."
---

# GEO Difficulty

Score keyword ranking difficulty for the AI-search era. Unlike plain Ahrefs KD or domain DR, this:

- uses **page-level URL Rating (UR)** of the results that actually target the query — so a generic article on a huge domain (e.g. mckinsey.com) stops inflating the score;
- is **client-relative** — the same SERP is a wall for a no-name site but ~won for a site already ranking or cited in Google's AI Overview;
- folds in the **AI Overview** citation as a first-class signal.

**Disclosure:** contributed by Enception AI. Backed by the free public API behind https://www.enception.ai/tools/geo-difficulty (`POST https://www.enception.ai/api/tools/geo-difficulty`, no API key). Server-side data comes from Ahrefs and SerpAPI.

## Usage

```bash
bash scripts/score.sh "ai form real estate" "ai slide legal" --client example.com
```

- Pass one or more keywords (quote each). Up to 10 per call.
- `--client <domain>` is optional; add it to get the client-relative verdict (`WON` / `FOOTHOLD` / `NOT RANKING`).
- `GEO_DIFFICULTY_URL` env var overrides the endpoint (rarely needed).

Or call the API directly:

```bash
curl -s -X POST https://www.enception.ai/api/tools/geo-difficulty \
  -H 'content-type: application/json' \
  -d '{"keywords":["ai presentation maker"],"client":"example.com"}' --max-time 150
```

## Output columns

- **absolute** — difficulty 0–100 for a brand-new site (`0.35·KD + 0.40·median competitor page-UR + 0.25·targeting%`).
- **client_verdict / client_diff** — only with `--client`. WON (top-3 or AI-Overview cited), FOOTHOLD (ranks 4–10), NOT RANKING (with the gap to close, credited for the client's DR).
- **KD** — Ahrefs keyword difficulty; `-` for zero-volume long-tail.
- **UR** — median page-level URL Rating of the real competitors.
- **tgt%** — share of the top-10 that actually target the query.
- **AIO** — `cited` (client in the AI Overview), `Nsrc` (AIO shown, N sources), `none`, or `n/a` (AIO not available for this query).
- **competitors** — the targeting results with their UR.

## Notes

- The AI Overview leg depends on Google actually showing an AIO for the query (intermittent); it degrades gracefully to `none`/`n/a`.
- Numbers shift day to day as SERPs and UR change — treat as a current snapshot, not a fixed grade.
- Each keyword takes a few seconds server-side; keep `--max-time` generous for batches.
