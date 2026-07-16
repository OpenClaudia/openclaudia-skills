#!/usr/bin/env bash
# GEO Difficulty — call the enception.ai API and print a table.
# Usage: score.sh "keyword one" "keyword two" ... [--client domain]
# Endpoint override: GEO_DIFFICULTY_URL (default prod).
set -euo pipefail

URL="${GEO_DIFFICULTY_URL:-https://www.enception.ai/api/tools/geo-difficulty}"
CLIENT=""
KEYWORDS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --client) CLIENT="$2"; shift 2 ;;
    --client=*) CLIENT="${1#*=}"; shift ;;
    *) KEYWORDS+=("$1"); shift ;;
  esac
done

if [ ${#KEYWORDS[@]} -eq 0 ]; then
  echo "usage: score.sh \"keyword\" [\"keyword2\" ...] [--client domain]" >&2
  exit 1
fi

# Build JSON body with python (safe quoting).
BODY=$(KW="$(printf '%s\n' "${KEYWORDS[@]}")" CLIENT="$CLIENT" python3 -c '
import json,os
kw=[k for k in os.environ["KW"].split("\n") if k.strip()]
b={"keywords":kw}
if os.environ.get("CLIENT"): b["client"]=os.environ["CLIENT"]
print(json.dumps(b))')

curl -s -X POST "$URL" -H 'content-type: application/json' -d "$BODY" --max-time 150 \
| python3 -c '
import json,sys
d=json.load(sys.stdin)
if "results" not in d:
    print(json.dumps(d,indent=2)); sys.exit(0)
hasc=bool(d.get("client"))
hdr=["keyword","absolute"]+(["client_verdict","client_diff"] if hasc else [])+["KD","demand","UR","tgt%","AIO","competitors"]
print("\t".join(hdr))
for r in sorted(d["results"],key=lambda x:-(x["absolute_difficulty"] or 0)):
    nsrc=len(r["aio_sources"])
    aio="cited" if r.get("aio_cited") else ("n/a" if not r["aio_available"] else (str(nsrc)+"src" if nsrc else "none"))
    dem=r.get("demand_score")
    row=[r["keyword"],str(r["absolute_difficulty"])]
    if hasc: row+=[str(r.get("verdict")),str(r.get("client_difficulty"))]
    row+=[("-" if r["kd"] is None else str(r["kd"])),("-" if dem is None else str(dem)),str(r["competition_ur_median"]),str(r["targeting_pct"]),aio,", ".join(r["real_competitors"][:4])]
    print("\t".join(row))
'
