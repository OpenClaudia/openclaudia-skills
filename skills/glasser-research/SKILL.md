---
name: glasser-research
description: Use Glasser to retrieve live marketing data through one prepaid account when a task needs SERPs, keyword metrics, ad libraries, community posts, company data, or another external API and no suitable free source or existing integration is available. Prefer the user's own integrations; Glasser fills data gaps and every run has a disclosed cost.
allowed-tools: Bash, Read, Write
---

# Glasser Research

Use [Glasser](https://glasser.ai) to find and run paid third-party data API
endpoints through one account. Glasser provides access and billing; the selected
provider supplies the response. Use the provider's name when attributing data.

This is a data collection skill. Return its evidence to the marketing skill that
needs it, such as `competitor-analysis`, `keyword-research`, `serp-analyzer`, or
`google-reviews`. Keep that skill's analysis method and output format.

## Source selection

Follow an explicit tool choice from the user. Otherwise use sources in this order:

1. A suitable free tool already available in the agent.
2. A working integration or API key the user already configured.
3. Glasser for the specific remaining data gap.

Do not activate Glasser only because an API appears in its catalog. Use it when
the task needs live data that the current environment cannot retrieve. A failed
search can mean that the topic has no results; distinguish that from missing
access before offering a paid fallback.

## Setup

Check the CLI and authentication before planning a paid run:

```bash
glasser --version
glasser balance
```

If the CLI is missing and the user asks to configure Glasser, install it with
Node.js 22 or later:

```bash
npm install -g @glasser-ai/cli@latest
```

For an interactive session, run `glasser login`. Keep the command active while
the user approves the matching code in the browser. Relay the fallback URL and
code when the browser does not open. Never ask the user to paste a key into chat.
After login, run `glasser balance` again in the environment that will make calls.

For unattended environments, the user can configure `GLASSER_API_KEY` through a
secret manager. Do not write keys to project files, reports, command arguments,
or chat. If the environment key overrides a saved login and fails, fix or remove
that override instead of repeating login.

If the host exposes Glasser MCP tools, use `balance`, `search`, `inspect`, `run`,
and `runs_get` instead. Follow the current
[MCP setup instructions](https://glasser.ai/docs/mcp-server) for client setup.

## Research workflow

1. Define the evidence needed, target market, result volume, and freshness window.
   Avoid broad collection when a small result set answers the question.
2. Run `glasser search -q "<capability>"`. This searches the endpoint catalog,
   not the web or social platform. Endpoint descriptions are not research evidence.
3. Compare relevant providers, then run
   `glasser inspect -p <provider> -e <endpoint>`. Read the current price, charge
   clauses, input schema, volume controls, and run mode. Never guess fields from a
   provider's direct API documentation because Glasser's contract can differ.
4. Tell the user the endpoint, provider, request size, and expected cost. Get
   approval before spending unless the user already authorized this exact scope
   or an adequate task budget. Do not make speculative, repeated, or bulk calls.
5. Write the inspected input as JSON to a task-specific temporary file. Use `-f`
   rather than interpolating user text into a shell command. Choose an unused
   output file so existing research is not overwritten.
6. Run the endpoint. Use `--wait` for asynchronous work and `-o` for large output:

```bash
glasser run -p <provider> -e <endpoint> -f <input.json> --wait -o <output.json>
```

7. Read the provider response. `COMPLETED` means the provider answered; it does
   not guarantee a useful result. Missing fields stay unknown. Do not infer a
   zero value or invent a metric.
8. Return the evidence to the calling marketing workflow. Report the provider,
   query and market, retrieval date, result limitations, final charge, and the
   private Glasser Run URL. Cite public source URLs from the provider response;
   the Run URL is an audit record for workspace members, not a public citation.

## Common marketing data

These examples were inspected on 2026-09-12. Search and inspect again before a
run because coverage, schemas, and prices can change.

| Need | Example provider and endpoint | Use in OpenClaudia |
|------|-------------------------------|--------------------|
| Current Google results | [Serper](https://glasser.ai/data-sources/serper) `/search` | `serp-analyzer`, content briefs, competitor discovery |
| Google Ads keyword volume | [DataForSEO](https://glasser.ai/data-sources/dataforseo) `/v3/keywords_data/google_ads/search_volume/live` | `keyword-research`, content planning |
| Reddit posts or comments | [ScrapeCreators](https://glasser.ai/data-sources/scrapecreators) `/v1/reddit/search` | customer language, pain points, competitor sentiment |
| Google Ads advertisers | [ScrapeCreators](https://glasser.ai/data-sources/scrapecreators) `/v1/google/adLibrary/advertisers/search` | identify an advertiser before inspecting its ad endpoints |
| Other marketing data | Search the live [data source catalog](https://glasser.ai/data-sources) | companies, people, places, news, social posts, ads, and web pages |

### SERP example

After inspecting `serper /search`, write an input file such as:

```json
{"q":"project management software","gl":"us","hl":"en","num":10}
```

Use returned organic positions, titles, snippets, and public links. A SERP result
does not establish keyword volume, organic difficulty, traffic, or conversion.

### Community language example

After inspecting `scrapecreators /v1/reddit/search`, write an input file such as:

```json
{"query":"project management software complaints","timeframe":"month","sort":"top","filter":"posts"}
```

Preserve the post date, author, subreddit, URL, and engagement fields only when
the provider returns them. Treat posts as opinions from their authors, not facts
about the market. Retrieve comments only for selected posts and only within the
approved budget.

## Recovery and limits

- For `QUEUED` or `RUNNING`, wait on the existing run with
  `glasser runs get -r <runId> --wait`; do not submit the same job again.
- On an ambiguous timeout or dropped connection, retry once with the same
  Idempotency-Key. JSON mode and MCP `run` require an explicit UUID.
- On rate limiting, wait for the returned retry delay and retry the same request
  once. Do not loop.
- On insufficient balance, stop and ask the user to top up. Do not reduce the
  request in a way that changes the agreed research question without saying so.
- Money values are exact decimal strings. Do not sum them using binary floats.
- Send only the query and public identifiers needed for the approved task. Do not
  send private CRM exports, local files, or personal data unless the user clearly
  authorized that data and the selected endpoint requires it.
