---
name: cloro-ai-visibility
description: Check if ChatGPT, Google AI Mode and Gemini mention or cite a brand for a set of prompts, and if Google shows an AI Overview that cites it, per country, with the cloro API. Use when the user asks "does ChatGPT mention us", "AI visibility check", "which sources does AI Mode cite", "are we in the AI Overview for", "AI answer citations for [brand]", or "compare AI answers across engines". For organic SERP analysis use serp-analyzer; for a hosted GEO report use ai-citations-report.
allowed-tools: Bash, Read, Write
---

# cloro AI Visibility

Send buyer prompts to ChatGPT, Google AI Mode and Gemini, and queries to Google with the AI Overview, from a chosen country. Read back the answer text and the sources each answer cites. Report where the brand is mentioned, where its domain is cited, and which other domains are cited.

**Disclosure:** This skill was contributed by cloro and calls cloro's paid API. The free plan includes 500 credits a month, which is about 70 to 80 calls with this skill.

API reference (for humans): https://cloro.dev/docs/api-reference/introduction?utm_source=openclaudia-skills&utm_medium=byok

## Requirements

- `CLORO_API_KEY`: get a key at https://dashboard.cloro.dev/api-keys?utm_source=openclaudia-skills&utm_medium=byok
- `curl` and `jq`

If `CLORO_API_KEY` is not set, do not stop. Tell the user that the key is not set, then do the manual check: give the user the prompt list to run in each engine, or use the WebSearch tool for the Google queries, and fill in the same output table from what the user pastes back. Label those rows "manual".

Never write the key to a file, a report, or the chat.

## Inputs

Ask for what is missing:

1. **Brand name** and **domain** (for example `Acme` and `acme.com`). Accept more than one domain.
2. **Prompts**: 1 to 10 buyer questions, for example "best CRM for small agencies". If the user gives none, write 5 from the brand's category and show them for approval.
3. **Country**: ISO 3166-1 alpha-2 code, default `US`.
4. **Engines**: any of `chatgpt`, `aimode`, `gemini`, `google`. Default: all four.
5. **Competitors** (optional): names or domains to count beside the brand.

## Cost and approval

Each sync call costs credits:

| Engine | Endpoint | Credits |
|--------|----------|--------:|
| ChatGPT | `POST /v1/monitor/chatgpt` | 7 |
| Google AI Mode | `POST /v1/monitor/aimode` | 6 |
| Gemini | `POST /v1/monitor/gemini` | 6 |
| Google Search with AI Overview | `POST /v1/monitor/google` | 7 |

Before the first call, show the number of calls and the credit total (for example 5 prompts x 4 engines = 130 credits). Get approval before you spend more than 30 credits, unless the user already approved a budget. Use only the four engines in this table. If the user asks for another engine, say that this skill does not cover it.

## Step 1: Run the calls

Build each request body with `jq` so that user text is never put into the shell command:

```bash
# AI engines: chatgpt, aimode, gemini
ENGINE=chatgpt
jq -n --arg prompt "best CRM for small agencies" --arg country "US" \
  '{prompt: $prompt, country: $country, include: {markdown: true}}' > /tmp/cloro-body.json

curl -sS -X POST "https://api.cloro.dev/v1/monitor/${ENGINE}" \
  -H "Authorization: Bearer ${CLORO_API_KEY}" \
  -H "Content-Type: application/json" \
  --data @/tmp/cloro-body.json \
  --max-time 180 \
  -o "/tmp/cloro-${ENGINE}-1.json" -w '%{http_code}\n'
```

```bash
# Google Search with the AI Overview
jq -n --arg query "best crm for small agencies" --arg country "US" \
  '{query: $query, country: $country, include: {aioverview: true}}' > /tmp/cloro-body.json

curl -sS -X POST "https://api.cloro.dev/v1/monitor/google" \
  -H "Authorization: Bearer ${CLORO_API_KEY}" \
  -H "Content-Type: application/json" \
  --data @/tmp/cloro-body.json \
  --max-time 120 \
  -o /tmp/cloro-google-1.json -w '%{http_code}\n'
```

An AI answer can take up to about a minute. Run the calls one after another, and save each response to its own file.

## Step 2: Read the responses

AI engines return `{success, result: {text, markdown, sources[], citationPills[], model}}`:

```bash
# Answer text
jq -r '.result.text' /tmp/cloro-chatgpt-1.json

# Every source the answer used: position, label, URL
jq -r '.result.sources[] | [.position, .label, .url] | @tsv' /tmp/cloro-chatgpt-1.json

# Cited domains, most frequent first
jq -r '.result.sources[].url | capture("^https?://(www\\.)?(?<h>[^/]+)").h' /tmp/cloro-chatgpt-1.json | sort | uniq -c | sort -rn
```

- Count every entry in `sources` as a citation. Do not use the `footnote` flag on ChatGPT sources as a citation marker; it is not reliable.
- `citationPills` can be empty. `model` can be `null` on ChatGPT.

Google returns `{success, result: {organicResults[], peopleAlsoAsk[], relatedSearches[], aioverview?}}`:

```bash
# Is there an AI Overview, and which sources does it cite?
jq -r 'if .result.aioverview then "AI Overview: yes" else "AI Overview: no" end' /tmp/cloro-google-1.json
jq -r '.result.aioverview.sources[]? | [.position, .label, .url] | @tsv' /tmp/cloro-google-1.json

# Organic results; skip rows whose link is empty or a google.com/goto URL
jq -r '.result.organicResults[] | select((.link // "") != "" and ((.link // "") | test("google\\.com/goto") | not)) | [.position, .title, .link] | @tsv' /tmp/cloro-google-1.json
```

## Step 3: Score each prompt and engine

For each prompt and engine, record:

- **Mentioned**: the brand name appears in `result.text` (case-insensitive). For Google, check `result.aioverview.text`.
- **Cited**: a source URL host equals the brand domain or ends with `.<domain>`.
- **Cited URLs**: the brand's URLs from the sources.
- **Other domains cited**: the top 5 other domains, with competitors marked.
- **Google organic position** (Google only): the best `position` of a brand URL in `organicResults`, or "not in results".

## Output

Write `ai-visibility-<brand>-<YYYY-MM-DD>.md` with:

1. A header: brand, domains, country, date, engines, number of calls, credits used.
2. One table, one row per prompt and engine:

| Prompt | Engine | Mentioned | Cited | Brand URLs cited | Other domains cited |
|--------|--------|-----------|-------|------------------|---------------------|

3. A short summary: the number of answers that mention the brand and the number that cite it, out of the total (for example "ChatGPT: mentioned in 3 of 5, cited in 1 of 5"). Name the domains that the engines cite most often for this prompt set.
4. Next steps that come from the data, for example pages that competitors get cited for and the brand has no equivalent of.

## How to read the results

- One call is one sample. AI answers change between runs and between days. Report counts with the sample size ("3 of 5"), not as a percentage or a trend.
- Do not say a page is "not indexed" when it is not cited. Say "not cited in this answer".
- For trends, run the same prompt set on a schedule and compare the counts.

## More than 10 prompts

Use the async batch API. It costs 2 credits less per task than sync. Send up to the approved number of tasks in one request:

```bash
jq -n --arg country "US" '[
  {taskType: "CHATGPT", payload: {prompt: "best crm for small agencies", country: $country}},
  {taskType: "AIMODE",  payload: {prompt: "best crm for small agencies", country: $country}},
  {taskType: "GOOGLE",  payload: {query: "best crm for small agencies", country: $country, include: {aioverview: true}}}
]' > /tmp/cloro-batch.json

curl -sS -X POST "https://api.cloro.dev/v1/async/task/batch" \
  -H "Authorization: Bearer ${CLORO_API_KEY}" \
  -H "Content-Type: application/json" \
  --data @/tmp/cloro-batch.json -o /tmp/cloro-batch-out.json

jq -r '.results[] | select(.success) | .task.id' /tmp/cloro-batch-out.json
```

`taskType` is `CHATGPT`, `AIMODE`, `GEMINI` or `GOOGLE`. Poll each task id every 15 seconds until `task.status` is `COMPLETED` or `FAILED`:

```bash
curl -sS "https://api.cloro.dev/v1/async/task/${TASK_ID}" \
  -H "Authorization: Bearer ${CLORO_API_KEY}" -o "/tmp/cloro-task-${TASK_ID}.json"
jq -r '.task.status' "/tmp/cloro-task-${TASK_ID}.json"
```

When it is `COMPLETED`, the engine result is under `.response` (same fields as `.result` in the sync calls). Items with `success: false` in the batch response were not queued; read their `error.message`.

## Errors

Errors return `{"success": false, "error": {"code": "...", "message": "..."}}`.

| HTTP | Code | What to do |
|------|------|------------|
| 401 | `INVALID_API_KEY_FORMAT` | The key is wrong. Ask the user to check `CLORO_API_KEY`. |
| 403 | `INSUFFICIENT_CREDITS` | Stop. Tell the user the balance is used up. |
| 429 | | Too many calls at the same time. Wait 30 seconds and retry once. |
| 400 | `VALIDATION_ERROR` | Read `error.details` and fix the request body. |

Do not loop on errors. After one failed retry, report the error and continue with the other calls.

## MCP alternative

If the host already has the cloro MCP server (`https://mcp.cloro.dev/mcp`) connected, you can use its tools instead of curl: `scrape_chatgpt`, `scrape_google_ai_mode`, `scrape_gemini`, `scrape_google` and `list_countries`. Use only these tools. The server lists other tools that this skill does not use. The cost and approval rules above stay the same.
