---
name: autom-rank-check
description: Check where a domain and its competitors rank in live Google and Bing results for a list of keywords, per country and language, with the Autom SERP API, and optionally whether Google AI Mode cites them. Use when the user asks "where do we rank for", "rank check", "check our Google and Bing positions", "are we on page one for", "who outranks us for these keywords", or "rankings in France vs the US". For a content brief from one SERP use serp-analyzer; for rank history from an Ahrefs project use ahrefs-research; for your own site's average position use search-console.
allowed-tools: Bash, Read, Write
---

# Autom Rank Check

Run each keyword through live Google and Bing searches from a chosen country and language. Find the rank of the brand domain and of each competitor domain in the organic results, and report who holds the top spots. Optionally, ask Google AI Mode the same keywords and check whether its answer cites the brand.

This is a point-in-time check: one live search per keyword, engine and page. It is not a tracked history.

**Disclosure:** This skill was contributed by Autom and calls Autom's paid API. New accounts get 1,000 free requests with no card (https://autom.dev/pricing). A Google or Bing page costs 1 credit; a Google AI Mode answer costs 3.

API reference (for humans): https://docs.autom.dev/google-search, https://docs.autom.dev/bing-search, https://docs.autom.dev/google-search-ai, https://docs.autom.dev/credits

## Requirements

- `AUTOM_API_KEY`: create a key at https://app.autom.dev/register?utm_source=openclaudia-skills&utm_medium=byok
- `curl` and `jq`

If `AUTOM_API_KEY` is not set, do not stop. Tell the user the key is not set, then do a manual check: use the WebSearch tool for each keyword, find the brand and competitor domains in the results, and fill in the same table. Label those rows "manual (WebSearch)", and say that WebSearch results are not localized to the chosen country and do not cover Bing.

Never write the key to a file, a report, or the chat.

## Inputs

Ask for what is missing:

1. **Brand domain**, for example `acme.com`. Strip `https://`, paths and a leading `www.`. A subdomain such as `blog.acme.com` counts as the brand.
2. **Keywords**: 1 to 50. If the user gives none, suggest up to 10 from the brand's site or category and show them for approval.
3. **Country**: two-letter code, default `us`. Used as `gl` on Google and `cc` on Bing.
4. **Language**: default `en`. Used as `hl` on Google.
5. **Engines**: any of `google`, `bing`, `aimode`. Default: `google` and `bing`. `aimode` is opt-in.
6. **Depth**: how many result pages to read per keyword on Google and Bing, 1 to 3. Default 1 (the first page). Each page is one call.
7. **Competitors** (optional): up to 5 domains to rank beside the brand.
8. **City** (optional, Google and AI Mode only): a place name such as `Paris, France`, sent as `location`.

## Cost and approval

| Engine | Endpoint | Credits |
|--------|----------|--------:|
| Google Search | `GET /v1/google/search` | 1 per page |
| Bing Search | `GET /v1/bing/search` | 1 per page |
| Google AI Mode | `GET /v1/google/search/ai` | 3 per keyword |

Only successful (`200`) calls are billed. Before the first call, show the number of calls and the credit total, for example 20 keywords x (Google 2 pages + Bing 2 pages) = 80 credits. Get approval before you spend more than 50 credits, unless the user already approved a budget.

## Step 1: Write the keyword list

Write the keywords to `/tmp/autom-keywords.txt` with the Write tool, one per line, so that user text never goes into a shell command line. Number them in the order of the file; `N` below is the line number.

## Step 2: Run the calls

Google, page `P` of keyword `N`:

```bash
N=0
while IFS= read -r KEYWORD; do
  N=$((N + 1))
  for P in 1; do   # use "1 2" or "1 2 3" for a depth of 2 or 3
    curl -sS -G "https://api.autom.dev/v1/google/search" \
      -H "x-api-key: ${AUTOM_API_KEY}" \
      --data-urlencode "query=${KEYWORD}" \
      --data-urlencode "gl=us" \
      --data-urlencode "hl=en" \
      --data-urlencode "page=${P}" \
      --max-time 70 \
      -o "/tmp/autom-google-${N}-p${P}.json" -w "google ${N} p${P}: %{http_code}\n"
  done
done < /tmp/autom-keywords.txt
```

Add `--data-urlencode "location=Paris, France"` for a city. Do not send `location` and `uule` together.

For Bing, run the same loop with this `curl` in place of the Google one. The country goes in `cc`:

```bash
    curl -sS -G "https://api.autom.dev/v1/bing/search" \
      -H "x-api-key: ${AUTOM_API_KEY}" \
      --data-urlencode "query=${KEYWORD}" \
      --data-urlencode "cc=us" \
      --data-urlencode "page=${P}" \
      --max-time 70 \
      -o "/tmp/autom-bing-${N}-p${P}.json" -w "bing ${N} p${P}: %{http_code}\n"
```

On Bing, send either `cc` (country) or `mkt` (market such as `en-US`), not both.

For Google AI Mode, run the same loop without the page loop, one call per keyword, only if the user chose `aimode`:

```bash
    curl -sS -G "https://api.autom.dev/v1/google/search/ai" \
      -H "x-api-key: ${AUTOM_API_KEY}" \
      --data-urlencode "query=${KEYWORD}" \
      --data-urlencode "gl=us" \
      --data-urlencode "hl=en" \
      --max-time 70 \
      -o "/tmp/autom-aimode-${N}.json" -w "aimode ${N}: %{http_code}\n"
```

Run the calls one after another. The server answers within 60 seconds. Stop reading further pages of a keyword once `.pagination.has_next_page` is `false`.

## Step 3: Read the responses

Google and Bing both return `organic_results[]` with `position`, `title`, `link`, `domain` and `snippet`, plus `pagination` and `search_parameters`. Google can also return `knowledge_graph`, `related_searches[]` and `search_information`. A query with no organic results can come back without the `organic_results` array, so always use `.organic_results[]?`.

Rank is the order of the organic result across the pages you read, starting at 1. Pass the page files in page order:

```bash
# Rank and URL of every brand result for keyword 1 on Google
jq -rs --arg d "acme.com" '
  [.[] | .organic_results[]?] | to_entries[]
  | ((.value.link // "") | (capture("^https?://(www\\.)?(?<h>[^/:?#]+)")? | .h) // "") as $h
  | select($h == $d or ($h | endswith("." + $d)))
  | [.key + 1, .value.link] | @tsv' \
  /tmp/autom-google-1-p1.json /tmp/autom-google-1-p2.json

# Top 10 for keyword 1: rank, host, title
jq -rs '
  [.[] | .organic_results[]?] | to_entries[:10][]
  | [.key + 1, ((.value.link // "") | (capture("^https?://(www\\.)?(?<h>[^/:?#]+)")? | .h) // ""), .value.title]
  | @tsv' /tmp/autom-google-1-p1.json

# Related searches Google showed (ideas for more keywords)
jq -r '.related_searches[]?.query' /tmp/autom-google-1-p1.json
```

Run the same filters on the Bing files. Run the first filter once per domain (brand and each competitor). The brand's rank for a keyword is the lowest number it returns; if it returns nothing, write "not in top X", where X is the number of organic results you read.

Google AI Mode returns `text_blocks[]` (`type`, `snippet`), `references[]` (`index`, `title`, `link`, `source`), `shopping_results[]` and `reconstructed_markdown`. When Google shows no AI Mode answer, the response has an `error` field such as "Google hasn't returned an AI Mode answer for this query." and empty arrays; record "no AI Mode answer".

```bash
# Did Google show an AI Mode answer?
jq -r '.error // "answer shown"' /tmp/autom-aimode-1.json

# Brand references in the answer
jq -r --arg d "acme.com" '
  .references[]?
  | ((.link // "") | (capture("^https?://(www\\.)?(?<h>[^/:?#]+)")? | .h) // "") as $h
  | select($h == $d or ($h | endswith("." + $d)))
  | .link' /tmp/autom-aimode-1.json

# Is the brand name in the answer text? Pass the name in lowercase.
jq -r --arg b "acme" '[.text_blocks[]?.snippet // empty] | join(" ") | ascii_downcase | contains($b)' /tmp/autom-aimode-1.json
```

## Output

Write `rank-check-<domain>-<country>-<YYYY-MM-DD>.md` with:

1. A header: brand domain, competitors, country, language, city if any, date, engines, depth, number of calls, credits used.
2. One table, one row per keyword:

| Keyword | Google rank | Google URL | Bing rank | Bing URL | Best competitor (Google) | AI Mode cites brand |
|---------|------------:|------------|----------:|----------|--------------------------|---------------------|

   Leave out the AI Mode column if it was not run. Put "not in top X" where the brand was not found.
3. A competitor table: for each domain, the number of keywords where it is in the top 3, top 10, and found at all, on each engine.
4. A short summary with counts, not percentages: for example "Google: top 10 for 7 of 20 keywords; Bing: top 10 for 11 of 20". Name the keywords where Google and Bing differ by 5 or more places, and the domains that hold rank 1 most often.
5. Next steps that come from the data, for example keywords ranked 4 to 15 (closest to a gain), and keywords where a competitor ranks and the brand has no page.

## How to read the results

- Each row is one live search from one country at one moment. Results vary by city, device, time and personalization. Do not present a single check as a trend; run the same list on a schedule to compare.
- "Not in top X" means not found in the results you read. It does not mean the page is not indexed.
- A brand can appear more than once (for example a page and its sitelink). Report the best rank and list the other URLs.

## Errors

Errors return `{"error": "..."}`.

| HTTP | What to do |
|------|------------|
| 400 | A parameter is missing or invalid. Check `query`, the country code, and that `location`/`uule` or `cc`/`mkt` are not sent together. |
| 401 | The key is missing, invalid, inactive or expired, or a rate limit was hit (the message starts with "Rate limit exceeded"). For a key error, ask the user to check `AUTOM_API_KEY`. For a rate limit, wait 30 seconds and retry once. |
| 402 | Out of credits. Stop and tell the user. |
| 500 | Retry once, then skip that call and note it in the report. Failed calls are not billed. |

Do not loop on errors. After one failed retry, report the error and continue with the other calls.

## MCP alternative

If the host already has the Autom MCP server connected (`https://mcp.autom.dev/`), you can use its `google_search`, `bing_search` and `google_search_ai` tools with the same parameters instead of curl. The cost and approval rules above stay the same.
