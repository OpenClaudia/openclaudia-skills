---
name: piloterr-ad-library
description: Pull the ads competitors run on Google (Ads Transparency Center) and LinkedIn (Ad Library), per country and date window, with the Piloterr API, and turn them into a summary of formats, messages, offers and CTAs. Use when the user asks "what ads is [competitor] running", "competitor ad research", "show me their LinkedIn ads", "Google Ads Transparency for [domain]", "ad library check", or wants ad copy examples before writing their own. For writing ad copy use google-ads or linkedin-ads; for video creative breakdowns use video-ad-analysis; for a multi-provider data marketplace use glasser-research.
allowed-tools: Bash, Read, Write
---

# Piloterr Ad Library

Search the Google Ads Transparency Center and the LinkedIn Ad Library for each competitor, from a chosen country and date window. Read back the ad cards, fetch details for a sample, and report what each competitor runs: formats, surfaces, dates, headlines and copy, offers and calls to action.

**Disclosure:** This skill was contributed by Piloterr and calls Piloterr's paid API. New accounts get 500 free credits with no card (https://www.piloterr.com/pricing). Every call in this skill costs 2 credits.

API reference (for humans): https://www.piloterr.com/library/googleadstransparency-search, https://www.piloterr.com/library/googleadstransparency-ad, https://www.piloterr.com/library/linkedinadlibrary-search, https://www.piloterr.com/library/linkedinadlibrary-ad, https://docs.piloterr.com/credits

## Requirements

- `PILOTERR_API_KEY`: create a key at https://app.piloterr.com/register?utm_source=openclaudia-skills&utm_medium=byok
- `curl` and `jq`

If `PILOTERR_API_KEY` is not set, do not stop. Tell the user the key is not set, then do the manual check: ask the user to search each competitor's domain at https://adstransparency.google.com and to open `https://www.linkedin.com/ad-library/search?accountOwner=<name>`, then fill in the same tables from what the user pastes back. Label those rows "manual".

Never write the key to a file, a report, or the chat.

## Inputs

Ask for what is missing:

1. **Competitors**: 1 to 5. For each, the **domain** (for Google, for example `acme.com`) and the **company name** as it appears on LinkedIn (for example `Acme`).
2. **Platforms**: `google`, `linkedin`, or both. Default: both.
3. **Country**: two-letter code, default `US`. Google takes one country (or `anywhere`); LinkedIn takes a comma-separated list or `ALL`.
4. **Date window**: default the last 30 days.
5. **Detail calls**: how many ads per competitor and platform to open for full details, 0 to 10. Default 5.
6. **Google filters** (optional): `format` (`text`, `image`, `video`) and `platform` (comma-separated: `search`, `youtube`, `shopping`, `maps`, `play`).

## Cost and approval

| Call | Endpoint | Credits |
|------|----------|--------:|
| Google ad search | `GET /v2/googleadstransparency/search` | 2 |
| Google ad detail | `GET /v2/googleadstransparency/ad` | 2 |
| LinkedIn ad search | `GET /v2/linkedinadlibrary/search` | 2 |
| LinkedIn ad detail | `GET /v2/linkedinadlibrary/ad` | 2 |

Only successful (`200`) calls are billed. Before the first call, show the number of calls and the credit total, for example 3 competitors x 2 platforms x (1 search + 5 details) = 36 calls = 72 credits. Get approval before you spend more than 40 credits, unless the user already approved a budget.

## Step 1: Search Google Ads Transparency

One call per competitor. `query` takes a domain, an advertiser name, an advertiser id (`AR` followed by digits) or a full Ads Transparency URL. Use the domain.

```bash
curl -sS -G "https://api.piloterr.com/v2/googleadstransparency/search" \
  -H "x-api-key: ${PILOTERR_API_KEY}" \
  --data-urlencode "query=acme.com" \
  --data-urlencode "region=US" \
  --data-urlencode "preset_date=last_30_days" \
  --data-urlencode "per_page=40" \
  --max-time 70 \
  -o /tmp/piloterr-google-1.json -w '%{http_code}\n'
```

Date window: `preset_date` is `today`, `yesterday`, `last_7_days` or `last_30_days`. For another window, send `start_date` and `end_date` (`YYYY-MM-DD`, both inclusive) instead. `per_page` goes from 1 to 100 (default 40). For more ads, send `cursor` with the value of `.pagination.next`, only within the approved budget. `topic` defaults to `commercial`.

The response is `{results[], pagination}`. Each result has `url`, `creative_id`, `advertiser_id`, `advertiser_name`, `domain`, `format`, `first_shown_at`, `last_shown_at`, `image_url`, `preview_url`, `image_width`, `image_height`. Dates, images and pagination totals can be `null`.

```bash
# Ads found, by advertiser and format
jq -r '.results[]? | [.advertiser_name, .format] | @tsv' /tmp/piloterr-google-1.json | sort | uniq -c | sort -rn

# One line per ad: format, first and last shown, creative URL
jq -r '.results[]? | [.format, (.first_shown_at // "-"), (.last_shown_at // "-"), .url] | @tsv' /tmp/piloterr-google-1.json
```

A domain can map to more than one advertiser (an agency, a reseller). Keep the advertisers that match the competitor and say which ones you dropped.

## Step 2: Search the LinkedIn Ad Library

One call per competitor. Send the company name in `account_owner`. Without `account_owner`, `query` is a keyword search on all advertisers (or a full LinkedIn Ad Library search URL).

```bash
curl -sS -G "https://api.piloterr.com/v2/linkedinadlibrary/search" \
  -H "x-api-key: ${PILOTERR_API_KEY}" \
  --data-urlencode "account_owner=Acme" \
  --data-urlencode "countries=US" \
  --data-urlencode "date_option=last-30-days" \
  --max-time 70 \
  -o /tmp/piloterr-linkedin-1.json -w '%{http_code}\n'
```

`date_option` is `last-30-days`, `current-month`, `current-year`, `last-year` or `custom-date-range` (then send `start_date` and `end_date` as `YYYY-MM-DD`). Add `keyword` to filter on ad copy. For the next page, send `cursor` with the value of `.pagination.cursor`, only within the approved budget.

The response is `{results[], pagination}`. Each result has `url`, `ad_id`, `format`, `headline`, `description`, `advertiser_name`, `image_url`, `advertiser_image_url`. `pagination` has `total_results`, `total_pages`, `per_page` and `cursor`.

```bash
# Total ads in the window and how many this page holds
jq -r '"\(.pagination.total_results // "?") ads, \(.results | length) on this page"' /tmp/piloterr-linkedin-1.json

# Advertisers returned (account_owner is a name match; drop advertisers that are not the competitor)
jq -r '.results[]?.advertiser_name' /tmp/piloterr-linkedin-1.json | sort | uniq -c | sort -rn

# Copy of each ad: format, headline, description, URL
jq -r '.results[]? | [.format, (.headline // ""), (.description // "" | gsub("\\s+"; " ")), .url] | @tsv' /tmp/piloterr-linkedin-1.json
```

## Step 3: Open a sample of ads

Pick up to the approved number of ads per competitor and platform, newest and most varied formats first. Pass the `url` from the search results.

```bash
# Google creative: text read from the preview image, surfaces, regions, impressions range
jq -j '.results[0].url' /tmp/piloterr-google-1.json > /tmp/piloterr-url.txt
curl -sS -G "https://api.piloterr.com/v2/googleadstransparency/ad" \
  -H "x-api-key: ${PILOTERR_API_KEY}" \
  --data-urlencode "query@/tmp/piloterr-url.txt" \
  --data-urlencode "region=US" \
  --max-time 70 \
  -o /tmp/piloterr-google-1-ad-1.json -w '%{http_code}\n'

jq '{advertiser_name, format, creative_text, platforms, first_shown, last_shown,
     impressions_min, impressions_max,
     regions: [.regions[]? | {region, platforms, first_shown, last_shown, impressions_min, impressions_max}]}' \
  /tmp/piloterr-google-1-ad-1.json
```

```bash
# LinkedIn ad: CTA, payer, status, dates, landing page, impressions, targeting
jq -j '.results[0].url' /tmp/piloterr-linkedin-1.json > /tmp/piloterr-url.txt
curl -sS -G "https://api.piloterr.com/v2/linkedinadlibrary/ad" \
  -H "x-api-key: ${PILOTERR_API_KEY}" \
  --data-urlencode "query@/tmp/piloterr-url.txt" \
  --max-time 70 \
  -o /tmp/piloterr-linkedin-1-ad-1.json -w '%{http_code}\n'

jq '{advertiser_name, format_label, status, headline, description, cta_text, paid_by,
     start_date, end_date, target_url, impressions, targeting}' /tmp/piloterr-linkedin-1-ad-1.json
```

`jq -j` writes the URL without a trailing newline, and `--data-urlencode "query@file"` reads the value from the file, so a URL taken from a response never goes into a shell command line. On both platforms many detail fields can be `null` (dates, impressions, targeting, `creative_text`, `target_url`). Report a `null` as "not shown", never as zero.

## Output

Write `ad-library-<YYYY-MM-DD>.md` with:

1. A header: competitors, platforms, country, date window, number of calls, credits used.
2. An overview table, one row per competitor and platform:

| Competitor | Platform | Ads found | Formats | Surfaces / CTAs | Earliest first shown | Ads opened |
|------------|----------|----------:|---------|-----------------|----------------------|-----------:|

   "Ads found" is the number of ads in the results you read; for LinkedIn also give `pagination.total_results`.
3. One section per competitor with the ad copy you read: LinkedIn headline, description and CTA; Google `creative_text` and format. Quote the copy as it appears, with the creative URL.
4. A summary of patterns across competitors: recurring messages and claims, offers (trial, demo, discount, content download), CTAs, which formats each one leans on, and ads that have run the longest.
5. Next steps for the user's own ads that come from the data, for example angles nobody uses, or a CTA every competitor uses that the user does not. Hand off to `google-ads` or `linkedin-ads` to write copy.

## How to read the results

- The ad libraries show what ran, not what worked. Long-running ads are a hint, not proof, that an ad performs.
- Impressions in Ads Transparency are ranges (`impressions_min`, `impressions_max`) and often missing. Do not turn them into spend.
- Google `creative_text` is read from the preview image, so it can be partial. Say so when you quote it.
- Zero results means no ads were found for that name, country and window. Check the domain or the LinkedIn company name before you conclude the competitor does not advertise.

## Errors

Errors return `{"error": "..."}`.

| HTTP | What to do |
|------|------------|
| 400 | A parameter is missing or invalid. Check `query` / `account_owner`, the country code, and the date format. |
| 401 | The key is missing, invalid, inactive or expired, or a rate limit was hit (the message starts with "Rate limit exceeded"). For a key error, ask the user to check `PILOTERR_API_KEY`. For a rate limit, wait 30 seconds and retry once. |
| 402 | Out of credits. Stop and tell the user. |
| 500 | Retry once, then skip that call and note it in the report. Failed calls are not billed. |

Do not loop on errors. After one failed retry, report the error and continue with the other calls.

## MCP alternative

If the host already has the Piloterr MCP server connected, you can use its `googleadstransparency_search`, `googleadstransparency_ad`, `linkedinadlibrary_search` and `linkedinadlibrary_ad` tools with the same parameters instead of curl. Use only these tools for this skill. The cost and approval rules above stay the same.
