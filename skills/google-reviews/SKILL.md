---
name: google-reviews
description: >
  Fetch Google Maps ratings, review counts, and rating distributions for any business
  using the DataForSEO API. Use when asked to check Google reviews, compare business
  ratings, audit Google Maps presence, or analyze competitor reviews.
---

# Google Reviews

Fetch Google Maps review data for any business using the [DataForSEO](https://dataforseo.com) API.

## Prerequisites

- **DataForSEO account** with `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` environment variables

## Usage

### Single Business

```bash
curl -s -X POST "https://api.dataforseo.com/v3/business_data/google/my_business_info/live" \
  -u "${DATAFORSEO_LOGIN}:${DATAFORSEO_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '[{
    "keyword": "Business Name",
    "location_name": "City,State,Country",
    "language_code": "en"
  }]'
```

### Extract Key Data

From the API response, extract:
- **Business name** (`title`)
- **Rating** (`rating.value`) — e.g., 4.2
- **Review count** (`rating.votes_count`) — e.g., 677
- **Rating distribution** (`rating.rating_distribution`) — breakdown by 1-5 stars
- **Address** — full street address
- **Category** — business type (e.g., "Car dealer", "Restaurant")
- **Website URL**

### Batch Mode

For comparing multiple businesses, loop through a list and collect results into a markdown comparison table:

| Business | Rating | Reviews | Category |
|----------|--------|---------|----------|
| Business A | 4.5 | 1,234 | Restaurant |
| Business B | 3.8 | 567 | Restaurant |

Add a 200ms delay between requests to avoid rate limits.

## Output Format

Return results as structured JSON for single lookups, or as a markdown table for batch comparisons. Always include:
- Business name
- Star rating
- Total review count
- Rating distribution (1-5 star breakdown)
- Address and category

## Location Format

Use the DataForSEO location format: `City,State/Province,Country`

Examples:
- `Vancouver,British Columbia,Canada`
- `Toronto,Ontario,Canada`
- `New York,New York,United States`
- `London,England,United Kingdom`

## Use Cases

- **Reputation audit** — check a client's Google rating before a proposal
- **Competitor analysis** — compare ratings across competing businesses
- **Local SEO** — monitor Google Maps presence and review velocity
- **Due diligence** — research businesses before partnerships

## Important Notes

- DataForSEO charges per API call — be mindful with large batches
- The API returns the first matching business for the keyword + location
- Results are synchronous (returned immediately)
