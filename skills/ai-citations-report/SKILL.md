---
name: ai-citations-report
description: "Generate an AI Citations Report (GEO) for a domain — which AI-search prompts cite the site across Google AI Overview and ChatGPT, plus organic-traffic context and per-article citation coverage. Use when the user asks for an 'AI citations report', 'GEO citations report', or 'which AI prompts cite <domain>'."
---

# AI Citations Report

Generate a styled, client-ready GEO report showing which AI-search prompts cite a domain across Google AI Overview and ChatGPT.

This skill is a thin client over the **Enception AI Citations API** (`POST https://www.enception.ai/api/external/ai-citations`). Do not re-implement the data pull or report HTML locally — all logic (LLM Mentions pull, cited-vs-retrieved classification, traffic trend, content coverage, HTML→PDF) runs server-side.

**Disclosure:** This skill was contributed by Enception AI and calls Enception's **paid** API. Citation data comes from DataForSEO LLM Mentions; traffic figures are modelled estimates.

API docs: https://www.enception.ai/doc/api-ai-citations

## Requirements

- `ENCEPTION_API_KEY` — access key for the Enception API. Self-serve: sign up at https://www.enception.ai, then generate a free-tier key under Account → API Key (10 reports/month free; contact the team for higher limits).

## What it produces

A styled PDF (or HTML/JSON) with:

- Summary table of every prompt that **cited** or **retrieved** the domain
- Organic traffic, 12-month month-over-month trend, and position distribution
- Full cited-prompt answer cards with the domain's source highlighted
- Retrieved-but-not-cited gap cards (content opportunities)
- Optional per-article citation coverage for URLs you pass in

## How to run

```bash
curl -X POST https://www.enception.ai/api/external/ai-citations \
  -H 'Content-Type: application/json' \
  -d '{
    "domain": "example.com",
    "brandName": "Example Inc",
    "locationCode": 2840,
    "articles": ["my-article-slug", "https://example.com/articles/another-post"],
    "passcode": "'"$ENCEPTION_API_KEY"'"
  }' \
  -o ai-citations-example.com.pdf
```

Then open the PDF and visually verify (traffic cards, trend deltas, source highlights) before presenting it.

### Options

- `domain` (required) — the site to analyze.
- `brandName`, `locationCode`, `languageCode`, `genDate` (optional) — default to the domain, `2840` (US), `en`, and today. Common location codes: `2840` = US, `2826` = UK, `2124` = Canada.
- `articles[]` (optional) — article slugs or full URLs for the content-coverage section. Omit to skip that section.
- `format` (optional) — `pdf` (default), `html`, or `json` (`json` returns `{citedCount, retrievedCount, promptCount, html}`; useful for debugging or piping counts elsewhere).

## Honesty guardrails (enforced in the report template)

- Says **"not yet cited in AI answers"**, never "not indexed" — LLM Mentions verifies AI citations, not Google indexation.
- Traffic is labelled **modelled estimates** (DataForSEO), not measured analytics.
- Never promise future AI citations in client-facing docs — citations are an emergent outcome of content quality, not a deliverable you can guarantee.

## Notes

- Rate limit: 20 requests/hour.
- A domain with zero AI citations still gets a valid report — the gap cards and traffic context are the value in that case.
