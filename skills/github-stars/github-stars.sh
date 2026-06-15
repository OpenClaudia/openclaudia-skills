#!/usr/bin/env bash
# github-stars.sh — fetch a repo's stargazer timestamps and render
# by-day + by-hour star charts in the CLI.
#
# Usage:
#   github-stars.sh <owner/repo | search-term> [--tz <IANA tz>] [--days N] [--hours-days N]
#
# Examples:
#   github-stars.sh melandlabs/openloomi
#   github-stars.sh openloomi --tz America/Los_Angeles --days 14 --hours-days 2
#
# Notes:
#   - Needs `gh` authenticated (gh auth status).
#   - GitHub only returns starred_at for the first 40,000 stargazers (API cap).
#   - Default timezone is America/Los_Angeles (PT). Pass --tz for another.
set -euo pipefail

REPO=""; TZ_ARG="America/Los_Angeles"; DAYS=14; HOURS_DAYS=2
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tz) TZ_ARG="$2"; shift 2;;
    --days) DAYS="$2"; shift 2;;
    --hours-days) HOURS_DAYS="$2"; shift 2;;
    *) REPO="$1"; shift;;
  esac
done

if [[ -z "$REPO" ]]; then
  echo "usage: github-stars.sh <owner/repo | search-term> [--tz TZ] [--days N] [--hours-days N]" >&2
  exit 1
fi

# Resolve a search term to a full owner/repo (top result by stars).
if [[ "$REPO" != */* ]]; then
  echo "Searching GitHub for '$REPO'..." >&2
  RESOLVED=$(gh api "search/repositories?q=$REPO&sort=stars&order=desc" \
    --jq '.items[0].full_name' 2>/dev/null || true)
  if [[ -z "$RESOLVED" || "$RESOLVED" == "null" ]]; then
    echo "No repo found for '$REPO'." >&2; exit 1
  fi
  echo "Resolved to: $RESOLVED" >&2
  REPO="$RESOLVED"
fi

CNT=$(gh api "repos/$REPO" --jq '.stargazers_count')
echo "Repo: $REPO   total stars: $CNT" >&2
PAGES=$(( (CNT + 99) / 100 ))
if (( CNT > 40000 )); then
  echo "WARNING: $CNT stars exceeds the 40,000 timestamp cap; only the earliest 40k have starred_at." >&2
  PAGES=400
fi

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
echo "Fetching $PAGES page(s) of stargazer timestamps..." >&2
for p in $(seq 1 "$PAGES"); do
  gh api -H "Accept: application/vnd.github.star+json" \
    "repos/$REPO/stargazers?per_page=100&page=$p" --jq '.[].starred_at'
done > "$TMP"

REPO="$REPO" TZ_NAME="$TZ_ARG" DAYS="$DAYS" HOURS_DAYS="$HOURS_DAYS" python3 - "$TMP" << 'PYEOF'
import os, sys
from datetime import datetime, timezone
from collections import Counter
from zoneinfo import ZoneInfo

tz = ZoneInfo(os.environ["TZ_NAME"])
days_n = int(os.environ["DAYS"]); hours_days = int(os.environ["HOURS_DAYS"])
rows = [l.strip() for l in open(sys.argv[1]) if l.strip()]
dts = sorted(datetime.strptime(r, "%Y-%m-%dT%H:%M:%SZ")
             .replace(tzinfo=timezone.utc).astimezone(tz) for r in rows)
if not dts:
    print("No timestamped stars found."); sys.exit(0)

tzabbr = dts[-1].strftime("%Z") or os.environ["TZ_NAME"]
now = datetime.now(tz)
print(f"\n{os.environ['REPO']} — {len(dts)} stars (with timestamps)")
print(f"newest: {dts[-1]:%Y-%m-%d %I:%M %p} {tzabbr}   |   now: {now:%Y-%m-%d %I:%M %p} {tzabbr}\n")

def bar(n, mx, w=40):
    return "█" * round(n / mx * w) if mx else ""

days = Counter(d.strftime("%Y-%m-%d") for d in dts)
recent = sorted(days)[-days_n:]
mx = max(days[d] for d in recent)
peak = max(recent, key=lambda d: days[d])
print(f"STARS BY DAY ({tzabbr})")
for d in recent:
    tag = "  ← peak" if d == peak else ""
    print(f"  {d}  {days[d]:>4}  {bar(days[d], mx)}{tag}")

for day in sorted({d.strftime('%Y-%m-%d') for d in dts})[-hours_days:]:
    hrs = Counter(d.hour for d in dts if d.strftime('%Y-%m-%d') == day)
    mx = max(hrs.values())
    print(f"\nSTARS BY HOUR — {day} ({tzabbr})   total {sum(hrs.values())}")
    for h in range(24):
        if hrs[h]:
            print(f"  {h:02d}:00  {hrs[h]:>3}  {bar(hrs[h], mx, 30)}")
PYEOF
