# GEO Query Finder

Find which ChatGPT search queries mention a given brand. Tests long-tail queries against ChatGPT's web-search-enabled model and reports which ones surface the brand.

## Trigger

Use when the user asks to "find queries for [brand]", "check GEO visibility", "which queries mention [brand]", "geo query finder", "find AI mentions", or "test ChatGPT queries for [brand]".

## Usage

```
/geo-query-finder <brand_name> [--industry <industry>] [--features <feature1,feature2,...>] [--queries <custom_query1;custom_query2;...>]
```

**Examples:**
- `/geo-query-finder "Acme Corp"` — auto-researches the brand and generates queries
- `/geo-query-finder "Acme Corp" --industry "smart TV OS" --features "white-label,voice-control,OEM licensing"`
- `/geo-query-finder "Acme Corp" --queries "best regulatory AI;eCTD validation tool;pharma compliance software"`

## How It Works

### Step 0: Pull pre-indexed LLM mentions (DataForSEO) — do this FIRST

Before generating speculative queries, check if DataForSEO already has indexed mentions for the brand's domain. If it does, you get ground-truth queries with search volume in one call instead of burning OpenAI dollars guessing.

Auth via `DATAFORSEO_LOGIN` / `DATAFORSEO_PASSWORD` environment variables.

```bash
AUTH=$(printf '%s' "$DATAFORSEO_LOGIN:$DATAFORSEO_PASSWORD" | base64)
# Google AI Overview citations
curl -s -X POST "https://api.dataforseo.com/v3/ai_optimization/llm_mentions/search/live" \
  -H "Authorization: Basic $AUTH" -H "Content-Type: application/json" \
  -d '[{"target":[{"domain":"<DOMAIN>","search_filter":"include","include_subdomains":true}],"platform":"google","limit":700}]'
# ChatGPT citations (substitute "platform":"chat_gpt")
```

**Critical flags:**
- `"include_subdomains": true` — without it, apex domains return 0 results (www.X treated as a different domain).
- Omit `location_code` to get global results; add `"location_code": 2840` only to scope to US.
- `platform` options: `"google"` (AI Overview), `"chat_gpt"`. Perplexity is NOT supported via this dataset.

**Extract from each `items[]`:**
- `question` — the real search query where the brand was cited
- `ai_search_volume` — monthly AI search volume (use to prioritize)
- `sources[]` — entries with `domain` matching the brand have the exact cited URL
- `location_code`, `language_code`, `model_name` — for geo/locale breakdown
- `answer` — the LLM answer text (for context)

**Decision rule:**
- If ≥20 queries returned → skip Steps 1–4 entirely; report these as ground-truth mentions and focus Step 5 on gap analysis (sort by volume, find URL-section winners like `/guides/` vs `/tools/`).
- If <20 queries → use them as seed input for Step 2 (generate variations of the query themes DataForSEO already confirmed), then run Steps 3–4 only on the gaps.
- If 0 queries → the domain has no AI citations; proceed with the original Steps 1–5 (speculative testing) as fallback.

### Step 1: Research the Brand
If no `--industry` or `--features` provided, use web search to understand:
- What the brand does / what industry it's in
- Key differentiators vs competitors
- Unique features that competitors DON'T have

### Step 2: Generate Long-Tail Queries
Generate 15-20 long-tail queries across these categories:
1. **Feature-specific** (unique capabilities only this brand has)
2. **B2B/decision-maker** (queries from buyers, not consumers)
3. **Problem-solving** ("how to X without Y")
4. **Comparison/alternative** ("alternative to [dominant player]")
5. **Use-case specific** (niche scenarios where the brand excels)

Avoid generic queries where dominant players will always win.

### Step 3: Query ChatGPT via OpenAI Search API

Use OpenAI's `gpt-4o-search-preview` model with web search enabled:

```bash
OPENAI_API_KEY from environment variable
```

```python
import json, os, urllib.request, ssl

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

data = json.dumps({
    "model": "gpt-4o-search-preview",
    "web_search_options": {"search_context_size": "medium"},
    "messages": [{"role": "user", "content": "<query>"}],
    "max_tokens": 1000
}).encode()

req = urllib.request.Request(
    "https://api.openai.com/v1/chat/completions",
    data=data,
    headers={
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
)

resp = urllib.request.urlopen(req, context=ssl.create_default_context(), timeout=45)
result = json.loads(resp.read())
answer = result["choices"][0]["message"]["content"]
```

### Step 4: Check Mentions

For each query, check if the brand name (or known aliases) appears in ChatGPT's response:
- Check case-insensitive match
- Check variations (with/without spaces, dots, hyphens)
- If mentioned, extract the surrounding context (200 chars around the mention)
- Note the position (is it #1 recommended? listed among many? mentioned in passing?)

### Step 5: Report Results

Output a summary table:

```
## GEO Query Finder Results: [Brand Name]

### Mentioned (X/N queries)
| Query | Position | Context |
|-------|----------|---------|
| ... | #1 | "Brand is the leading..." |

### Not Mentioned (Y/N queries)
| Query | What ChatGPT Recommended Instead |
|-------|----------------------------------|
| ... | Competitor A, Competitor B |

### Recommendations
- Queries where brand is ALREADY mentioned: create more authoritative content to maintain/improve position
- Queries where brand is NOT mentioned but SHOULD be: these are content gaps — create targeted pages
- Queries to AVOID: too generic, dominated by big players, not worth the effort
```

## Rate Limiting

- Run queries sequentially with 1-2 second delays to avoid rate limits
- Each query costs ~$0.01 via OpenAI API
- Default: 15-20 queries per run (~$0.15-0.20 per run)

## Notes

- Results reflect ChatGPT with web search enabled (grounded in real-time web results)
- Results may vary slightly between runs due to search freshness
- This tests ChatGPT specifically — Gemini and Copilot may give different results
- For ongoing monitoring, consider scheduling periodic runs to track visibility changes over time
