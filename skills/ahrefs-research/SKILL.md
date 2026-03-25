---
name: ahrefs-research
description: >
  Use the Ahrefs Python SDK to pull SEO data — backlinks, keywords, domain ratings,
  organic traffic, site audits, rank tracking, and brand monitoring. Use when asked
  to research competitors, find backlink opportunities, analyze organic keywords,
  check domain authority, or do any Ahrefs-powered SEO research.
---

# Ahrefs SEO Research

Use the official Ahrefs Python SDK (`ahrefs-python`) to pull SEO data programmatically.

## Prerequisites

- **Python 3.11+**
- **Ahrefs API key** in `AHREFS_API_KEY` environment variable (requires an Ahrefs subscription with API access)

## Installation

```sh
pip3 install git+https://github.com/ahrefs/ahrefs-python.git
```

Dependencies: `httpx`, `pydantic`.

## Capabilities

- **Site Explorer** — Backlinks, organic keywords, domain rating, traffic, referring domains
- **Keywords Explorer** — Keyword research, volumes, difficulty, related terms
- **Rank Tracker** — SERP monitoring, competitor tracking
- **Site Audit** — Technical SEO issues, page content, page explorer
- **Brand Radar** — AI brand mentions, share of voice, impressions
- **SERP Overview** — Search result analysis
- **Batch Analysis** — Bulk domain/URL metrics via POST

## API Method Discovery

The SDK has 52 methods across 7 API sections. Use the built-in search to find the right method:

**Python:**
```python
from ahrefs.search import search_api_methods

print(search_api_methods("domain rating"))
print(search_api_methods("backlinks", section="site-explorer", limit=3))
```

**CLI:**
```sh
python3 -m ahrefs.api_search "domain rating"
python3 -m ahrefs.api_search "backlinks" --section site-explorer --limit 3
python3 -m ahrefs.api_search "batch" --json
python3 -m ahrefs.api_search --sections  # list all API sections
```

## Important Rules

- ALWAYS use the `ahrefs-python` SDK. DO NOT make raw `httpx`/`requests` calls to the Ahrefs API.
- ALWAYS pass dates as strings in `YYYY-MM-DD` format (e.g. `"2025-01-15"`).
- ALWAYS use `select` on list endpoints to request only the columns you need — saves API units.
- USE context managers (`with` / `async with`) for client lifecycle management.
- NEVER hardcode API keys. Use `AHREFS_API_KEY` env var.
- The client handles retries (429, 5xx, connection errors) automatically. DO NOT add retry logic.

## Quick Start

```python
import os
from ahrefs import AhrefsClient

with AhrefsClient(api_key=os.environ["AHREFS_API_KEY"]) as client:
    data = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")
    print(data.domain_rating)  # 91.0
    print(data.ahrefs_rank)    # 3
```

## SDK Patterns

### Client Setup

```python
import os, ahrefs

with ahrefs.AhrefsClient(
    api_key=os.environ["AHREFS_API_KEY"],
    timeout=30.0,      # request timeout in seconds (default: 60)
    max_retries=3,      # retries on transient errors (default: 2)
) as client:
    ...
```

### Async Client

```python
import asyncio
from ahrefs import AsyncAhrefsClient

async with AsyncAhrefsClient(api_key=os.environ["AHREFS_API_KEY"]) as client:
    dr_ahrefs, dr_moz = await asyncio.gather(
        client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15"),
        client.site_explorer_domain_rating(target="moz.com", date="2025-01-15"),
    )
```

### Calling Methods

```python
# Keyword arguments (recommended)
data = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")

# Request objects (full type safety)
from ahrefs.types import SiteExplorerDomainRatingRequest
request = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
data = client.site_explorer_domain_rating(request)
```

Method names follow `{api_section}_{endpoint}`, e.g. `site_explorer_organic_keywords`, `keywords_explorer_overview`.

### List Endpoints

```python
items = client.site_explorer_organic_keywords(
    target="ahrefs.com",
    date="2025-01-15",
    select="keyword,volume,best_position",
    order_by="volume:desc",
    limit=10,
)
for item in items:
    print(item.keyword, item.volume, item.best_position)
```

### Error Handling

```python
import ahrefs

try:
    data = client.site_explorer_domain_rating(target="example.com", date="2025-01-15")
except ahrefs.AuthenticationError:    # 401
    ...
except ahrefs.RateLimitError as e:    # 429 — e.retry_after has the delay
    ...
except ahrefs.NotFoundError:          # 404
    ...
except ahrefs.APIError as e:          # other 4xx/5xx
    ...
except ahrefs.APIConnectionError:     # network / timeout
    ...
```

### Common Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `target` | `str` | Domain, URL, or path to analyze |
| `date` | `str` | Date in YYYY-MM-DD format |
| `date_from` / `date_to` | `str` | Date range for history endpoints |
| `country` | `str` | Two-letter country code (ISO 3166-1 alpha-2) |
| `select` | `str` | Comma-separated columns to return |
| `where` | `str` | Filter expression (JSON string) |
| `order_by` | `str` | Column and direction, e.g. `"volume:desc"` |
| `limit` | `int` | Max results to return |

### Filtering with `where`

```python
import json
where = json.dumps({"field": "volume", "is": ["gte", 1000]})
items = client.site_explorer_organic_keywords(
    target="ahrefs.com", date="2025-01-15",
    select="keyword,volume", where=where,
)
```
