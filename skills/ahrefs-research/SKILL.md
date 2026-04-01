---
name: ahrefs-research
description: >
  Use the Ahrefs Python SDK to pull SEO data -- backlinks, keywords, domain ratings,
  organic traffic, site audits, rank tracking, and brand monitoring. Use when asked
  to research competitors, find backlink opportunities, analyze organic keywords,
  check domain authority, or do any Ahrefs-powered SEO research.
---

# Ahrefs SEO Research

## Overview

The Ahrefs API provides programmatic access to Ahrefs SEO data. The official Python SDK (`ahrefs-python`) provides typed request and response models for all endpoints, auto-generated from the OpenAPI spec.

Key capabilities:
- **Site Explorer** - Backlinks, organic keywords, domain rating, traffic, referring domains
- **Keywords Explorer** - Keyword research, volumes, difficulty, related terms
- **Rank Tracker** - SERP monitoring, competitor tracking
- **Site Audit** - Technical SEO issues, page content, page explorer
- **Brand Radar** - AI brand mentions, share of voice, impressions
- **SERP Overview** - Search result analysis
- **Batch Analysis** - Bulk domain/URL metrics via POST

## Installation

```sh
pip3 install git+https://github.com/ahrefs/ahrefs-python.git
```

Requires Python 3.11+. Dependencies: `httpx`, `pydantic`.

## API Method Discovery

The SDK has 52 methods across 7 API sections. The built-in search tool is the fastest way to find the right method -- it returns matching method signatures, parameters, and return types directly, so there's no need to scan through a large reference.

**Python** (preferred when already in a Python context):

```python
from ahrefs.search import search_api_methods

# Returns formatted text with method signatures, parameters, and return types
print(search_api_methods("domain rating"))

# Filter by API section and limit results
print(search_api_methods("backlinks", section="site-explorer", limit=3))
```

**CLI** (preferred when exploring from the terminal):

```sh
# Ensure python3 points to the interpreter where ahrefs-python is installed:
#   which python3
#   python3 -c "import ahrefs"
python3 -m ahrefs.api_search "domain rating"
python3 -m ahrefs.api_search "backlinks" --section site-explorer --limit 3
python3 -m ahrefs.api_search "batch" --json
python3 -m ahrefs.api_search --sections  # list all API sections
```

## IMPORTANT RULES

- ALWAYS use the `ahrefs-python` SDK. DO NOT make raw `httpx`/`requests` calls to the Ahrefs API.
- ALWAYS pass dates as strings in `YYYY-MM-DD` format (e.g. `"2025-01-15"`).
- ALWAYS use `select` on list endpoints to request only the columns you need. List endpoints return all columns by default, which wastes API units and increases response size.
- USE context managers (`with` / `async with`) for client lifecycle management.
- NEVER hardcode API keys in source code. Use the `AHREFS_API_KEY` environment variable or your preferred secrets mechanism.
- The client handles retries (429, 5xx, connection errors) automatically. DO NOT implement your own retry logic on top of the SDK.

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
import os
import ahrefs

with ahrefs.AhrefsClient(
    api_key=os.environ["AHREFS_API_KEY"],  # or any secrets source
    base_url="...",          # override API base URL (default: https://api.ahrefs.com/v3)
    timeout=30.0,            # request timeout in seconds (default: 60)
    max_retries=3,           # retries on transient errors (default: 2)
) as client:
    ...
```

Async client:

```python
import os
from ahrefs import AsyncAhrefsClient

async with AsyncAhrefsClient(api_key=os.environ["AHREFS_API_KEY"]) as client:
    data = await client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")
```

For parallel calls, use `asyncio.gather`:

```python
import asyncio

async with AsyncAhrefsClient(api_key=os.environ["AHREFS_API_KEY"]) as client:
    dr_ahrefs, dr_moz = await asyncio.gather(
        client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15"),
        client.site_explorer_domain_rating(target="moz.com", date="2025-01-15"),
    )
```

### Calling Methods

Two calling styles -- both are equivalent:

```python
# Keyword arguments (recommended)
data = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")

# Request objects (full type safety)
from ahrefs.types import SiteExplorerDomainRatingRequest
request = SiteExplorerDomainRatingRequest(target="ahrefs.com", date="2025-01-15")
data = client.site_explorer_domain_rating(request)
```

Method names follow `{api_section}_{endpoint}`, e.g. `site_explorer_organic_keywords`, `keywords_explorer_overview`.

### Responses

Methods return typed Data objects directly.

**Scalar endpoints** return a single data object (or `None`):

```python
data = client.site_explorer_domain_rating(target="ahrefs.com", date="2025-01-15")
print(data.domain_rating)
```

**List endpoints** return a list of data objects. There is no pagination -- set `limit` to the number of results you need. Use `select` to request only the columns you need:

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
except ahrefs.RateLimitError as e:    # 429 -- e.retry_after has the delay
    ...
except ahrefs.NotFoundError:          # 404
    ...
except ahrefs.APIError as e:          # other 4xx/5xx -- e.status_code, e.response_body
    ...
except ahrefs.APIConnectionError:     # network / timeout
    ...
```

All exceptions inherit from `ahrefs.AhrefsError`.

### Common Parameters

Most list endpoints share these parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `target` | `str` | Domain, URL, or path to analyze |
| `date` | `str` | Date in YYYY-MM-DD format |
| `date_from` / `date_to` | `str` | Date range for history endpoints |
| `country` | `str` | Two-letter country code (ISO 3166-1 alpha-2) |
| `select` | `str` | Comma-separated columns to return |
| `where` | `str` | Filter expression |
| `order_by` | `str` | Column and direction, e.g. `"volume:desc"` |
| `limit` | `int` | Max results to return |

Parameters typed as enums in the API reference (`CountryEnum`, `VolumeModeEnum`, etc.) accept plain strings -- pass `country="us"` not `CountryEnum("us")`.

The `where` parameter takes a JSON string. Use `json.dumps()` to build it:

```python
import json
where = json.dumps({"field": "volume", "is": ["gte", 1000]})
items = client.site_explorer_organic_keywords(
    target="ahrefs.com", date="2025-01-15",
    select="keyword,volume", where=where,
)
```

For full filter syntax (boolean combinators, operators, nested fields), see the Ahrefs API documentation.

## API Methods

Use `search_api_methods("query")` or `python3 -m ahrefs.api_search "query"` to find methods by keyword. Search covers all 52 methods across 7 API sections and returns complete signatures, parameters, and response fields.
