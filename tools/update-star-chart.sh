#!/bin/sh
# Regenerate assets/star-history.png from the repo's own star data.
# Needs a gh login with admin/collab access to the repo (GitHub restricted
# the stargazers API to admins/collaborators in June 2026), plus matplotlib.
set -e
cd "$(dirname "$0")/.."

gh api -H "Accept: application/vnd.github.star+json" --paginate \
  "repos/OpenClaudia/openclaudia-skills/stargazers?per_page=100" \
  --jq '.[].starred_at' > /tmp/openclaudia-stars.txt

python3 - <<'EOF'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime

dates = sorted(datetime.strptime(l.strip(), '%Y-%m-%dT%H:%M:%SZ')
               for l in open('/tmp/openclaudia-stars.txt'))
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
ax.plot(dates, range(1, len(dates) + 1), color='#2f81f7', linewidth=2)
ax.fill_between(dates, range(1, len(dates) + 1), alpha=0.1, color='#2f81f7')
ax.set_title('OpenClaudia/openclaudia-skills — Star History', fontsize=12)
ax.set_ylabel('GitHub Stars')
ax.grid(alpha=0.3)
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig('assets/star-history.png')
print(f'{len(dates)} stars')
EOF

sed -i '' -E "s/<sub>Updated [0-9]{4}-[0-9]{2}-[0-9]{2}\./<sub>Updated $(date +%F)./" README.md
rm -f /tmp/openclaudia-stars.txt
