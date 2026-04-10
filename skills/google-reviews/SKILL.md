---
name: google-reviews
description: Fetch Google review ratings and review counts for businesses via DataForSEO API. Use when the user asks to check Google reviews, get review counts, compare business ratings, audit Google Maps presence, or analyze competitor reviews.
---

# Google Reviews

Fetch Google Maps ratings, review counts, and rating distributions for any business using the DataForSEO API.

## When to Use This Skill

Use this skill when the user:

- Asks to check Google reviews for a business
- Wants to compare ratings across multiple businesses
- Needs Google review counts for a report or analysis
- Asks about a business's Google Maps presence
- Wants to audit competitor reviews

## Tool Location

Global tools directory: `~/.agents/tools/`

- Script: `~/.agents/tools/fetch-google-reviews.js`
- Credentials: `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` in environment variables

## Usage

### Single Business

```bash
cd ~/.agents/tools && node fetch-google-reviews.js "Business Name" "City,Province,Country"
```

Example:
```bash
cd ~/.agents/tools && node fetch-google-reviews.js "Trust Auto Sales" "Richmond,British Columbia,Canada"
```

### Batch Mode

Create a JSON file with an array of businesses, then run:

```bash
cd ~/.agents/tools && node fetch-google-reviews.js --batch /path/to/businesses.json
```

JSON file format:
```json
[
  {"keyword": "Business One", "location": "Vancouver,British Columbia,Canada"},
  {"keyword": "Business Two"}
]
```

- `keyword` (required): Business name to search
- `location` (optional): Defaults to "Richmond,British Columbia,Canada"

## Output

### Single Business (JSON)

```json
{
  "keyword": "Trust Auto Sales",
  "title": "Trust Auto Sales",
  "rating": 4.2,
  "reviews": 677,
  "rating_distribution": {"1": 117, "2": 7, "3": 3, "4": 19, "5": 531},
  "address": "3691 Number 3 Rd, Richmond, BC V6X 2B8",
  "category": "Car dealer",
  "url": "https://trustauto.ca/"
}
```

### Batch Mode

Prints a markdown table followed by full JSON:

```
| Business | Rating | Reviews | Address |
|----------|--------|---------|---------|
| Trust Auto Sales | 4.2 | 677 | 3691 Number 3 Rd, Richmond, BC V6X 2B8 |
```

## Location Format

Use the DataForSEO location format: `City,Province/State,Country`

Examples:
- `Richmond,British Columbia,Canada`
- `Vancouver,British Columbia,Canada`
- `Toronto,Ontario,Canada`
- `New York,New York,United States`

## API Details

- Uses DataForSEO `business_data/google/my_business_info/live` endpoint
- Synchronous (returns results immediately)
- Returns first matching business for the keyword + location
- Batch mode adds 200ms delay between requests to avoid rate limits

## Important Notes

- If `npm install` hasn't been run yet: `cd ~/.agents/tools && npm install`
- The script loads credentials from both local `.env` and environment variables
- DataForSEO charges per API call -- be mindful with large batches
