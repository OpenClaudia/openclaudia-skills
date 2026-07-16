---
name: geo-analysis
description: "Run a full GEO/SEO client analysis for a domain via the Enception external API — start the analysis, poll its status, and download the PDF report covering AI visibility, market research, and competitors. Use when the user says 'run a client analysis', 'analyze <domain> for GEO', 'GEO analysis for <domain>', or 'check analysis status'."
---

# GEO Analysis

Run a full GEO/SEO analysis for a domain and get a client-ready PDF report: AI visibility (is the brand recommended by ChatGPT / Google AI), deep market research, and competitor landscape.

Thin wrapper over the Enception client-analysis API. Three operations: **start**, **status**, **report** (plus an optional brand-name correction).

**Disclosure:** contributed by Enception AI and calls Enception's **paid** external API. Docs: https://www.enception.ai/doc/api-client-analysis

## Requirements

- `ENCEPTION_ANALYSIS_API_KEY` — sent as the `x-api-key` header. Contact the Enception team via https://www.enception.ai to obtain one. Rate limit: 10 requests/minute.

## 1. Start

`POST https://www.enception.ai/api/external/client-analysis/start`

Required: `website_url`, `primary_region`, `core_goals`. Sensible defaults: `primary_region=us`, `core_goals=traffic`, `output_language=en`, `competitors=[]`. The API normalizes URLs to a bare domain and rejects IPs. Returns `{ id, message }` — **save the `id`**.

Pick `output_language` from an explicit request first, then the user's conversation language, then the domain TLD (`.cn` → `zh`; otherwise `en`).

```bash
curl -s -X POST "https://www.enception.ai/api/external/client-analysis/start" \
  -H "x-api-key: $ENCEPTION_ANALYSIS_API_KEY" -H "Content-Type: application/json" \
  -d '{"website_url":"https://example.com/","primary_region":"us","competitors":[],"core_goals":"traffic","output_language":"en"}'
```

Only override `primary_region` / `core_goals` / `competitors` if the user specifies. `core_goals` is free text (e.g. `traffic`, `ranking`). Competitors: `[{"name":"X","domain":"x.com"}, ...]` (max 5). For multiple domains, fire one POST each and collect the ids.

## 2. Status

`POST https://www.enception.ai/api/external/client-analysis/status` with body `{ "id": "<id>" }` and the same `x-api-key` header. Returns `{ status: 'pending' | 'failed' | 'succeeded', progress_percent?, pdf_url? }`.

A full run takes **~20–45 minutes** — the bottleneck is the deep market-research step. Poll on a long interval (minutes, not seconds). `succeeded` ⇒ ready to fetch the report. If a run fails or stalls indefinitely, report that to the user rather than inventing results.

## 3. Report

`GET https://www.enception.ai/api/external/client-analysis/report/<id>` — public, no auth; shareable by id. Works once status is `succeeded` (also serves partial runs).

```bash
curl -s -o geo-analysis-example.pdf \
  "https://www.enception.ai/api/external/client-analysis/report/<id>"
```

Confirm it's a real PDF (`file geo-analysis-example.pdf`), then give the user the file and/or the public URL.

## 4. Fix "zero visibility" (brand-name correction)

`POST https://www.enception.ai/api/external/client-analysis/update-brand` with body `{ "id", "brand_name"?, "alternative_names": [...] }` and the `x-api-key` header.

When a report shows zero/low AI visibility but the brand IS recommended by ChatGPT/Google, it's almost always because the brand is only known by its fused domain label (e.g. `pudurobotics`) while AI engines say "Pudu Robotics". Supply the real name + aliases and the route recomputes visibility from the already-stored answers (no re-query — fast), then re-fetch the report.

```bash
curl -s -X POST "https://www.enception.ai/api/external/client-analysis/update-brand" \
  -H "x-api-key: $ENCEPTION_ANALYSIS_API_KEY" -H "Content-Type: application/json" \
  -d '{"id":"<id>","brand_name":"Pudu Robotics","alternative_names":["Pudu","PuduBot"]}'
```

Returns `{ success, mention_rate, overall_score, average_position, analysis_regenerated }`. New analyses resolve the brand name automatically; this is the manual correction path for existing reports.
