---
name: github-stars
description: Show a GitHub repo's star growth as CLI charts — by day and by hour, in any timezone. Use when the user asks to "check GitHub stars", "stars by hour/day for <repo>", "star growth", "how many stars did <repo> get today", or shares a repo name and wants its starring activity over time.
---

# github-stars

Fetch a repo's per-star timestamps from the GitHub API and render two ASCII charts in the terminal: **stars by day** and **stars by hour** (for the most recent day(s)). Useful for tracking a launch, a Show HN / Product Hunt spike, or DevRel growth.

## Requirements

- The [`gh` CLI](https://cli.github.com/) installed and authenticated (`gh auth status`). Unauthenticated calls hit a low rate limit and large repos fail mid-pagination.
- Python 3.9+ (uses the stdlib `zoneinfo` for correct DST handling).

## How it works

The script calls `gh api` with the `application/vnd.github.star+json` Accept header, which adds a `starred_at` timestamp to each stargazer. It paginates through all stargazers, converts each timestamp to the target timezone, and buckets them by day and by hour.

## Usage

The script lives next to this file. From the skill directory:

```bash
bash github-stars.sh <owner/repo | search-term> [--tz <IANA tz>] [--days N] [--hours-days N]
```

- **`<owner/repo>`** — exact repo (e.g. `facebook/react`). Skips the search.
- **`<search-term>`** — a bare word (no `/`) is resolved to the top repo by stars.
- **`--tz`** — IANA timezone for all buckets. Default `America/Los_Angeles`. Use e.g. `UTC`, `America/New_York`, `Asia/Shanghai`, `Europe/Berlin`.
- **`--days N`** — how many recent days to show in the daily chart (default 14).
- **`--hours-days N`** — how many recent days to break out hourly (default 2).

## Examples

```bash
# default: last 14 days daily + last 2 days hourly
bash github-stars.sh vercel/next.js

# resolve a search term, show UTC
bash github-stars.sh next.js --tz UTC

# zoom in: only today hourly, 7-day daily window
bash github-stars.sh facebook/react --days 7 --hours-days 1
```

## Sample output

```
owner/repo — 284 stars (with timestamps)
newest: 2026-06-15 02:03 PM PDT   |   now: 2026-06-15 02:11 PM PDT

STARS BY DAY (PDT)
  2026-06-13    16  █████████
  2026-06-14    69  ████████████████████████████████████████  ← peak
  2026-06-15    22  █████████████

STARS BY HOUR — 2026-06-15 (PDT)   total 22
  06:00     5  ██████████████████████████████
  07:00     2  ████████████
  14:00     2  ████████████
```

## Caveats — surface these to the user when relevant

- **40,000-star cap:** GitHub only returns `starred_at` for the first 40k stargazers. Past that, the hourly/daily breakdown is incomplete (the script warns). The plain total stays accurate.
- **Net, not gross:** the stargazer list reflects stars currently in place. Un-stars don't appear, so a flat total between two checks can hide +1/−1 churn. If the live `stargazers_count` disagrees with the timestamp count, an un-star happened.
- **DST is handled** automatically via `zoneinfo` — don't hardcode UTC offsets.

## Re-checking / live polling

Just run the script again — it re-fetches live each time. To watch a launch, re-run on an interval and report the delta; don't poll faster than every ~15 minutes (rate limits + politeness).
