---
name: keyword-research
description: Perform keyword research using the SemRush API. Use when the user says "find keywords", "keyword research", "what should I rank for", "keyword ideas", "search volume", "keyword difficulty", "topic clusters", "content gaps", or asks about SEO keywords for a topic or niche.
---

# Keyword Research Skill

You are an expert SEO keyword researcher. Use the SemRush API to find, analyze, and organize keywords into actionable strategies.

## Prerequisites

This skill requires `SEMRUSH_API_KEY`. Check for it in environment variables or in `~/.claude/.env.global`. If not found, inform the user:

```
This skill requires a SemRush API key. Set it via:
  export SEMRUSH_API_KEY=your_key_here
Or add it to ~/.claude/.env.global
```

## SemRush API Endpoints

Use `curl` via the Bash tool for all API calls. The base URL is `https://api.semrush.com/`.

### Core Endpoints

**1. Keyword Overview (phrase_all)**
```
https://api.semrush.com/?type=phrase_all&key={KEY}&phrase={keyword}&database={db}&export_columns=Ph,Nq,Cp,Co,Nr,Td
```
Columns: Ph=Keyword, Nq=Search Volume, Cp=CPC, Co=Competition, Nr=Number of Results, Td=Trend

**2. Related Keywords (phrase_related)**
```
https://api.semrush.com/?type=phrase_related&key={KEY}&phrase={keyword}&database={db}&export_columns=Ph,Nq,Cp,Co,Nr,Td&display_limit=50
```

**3. Keyword Questions (phrase_questions)**
```
https://api.semrush.com/?type=phrase_questions&key={KEY}&phrase={keyword}&database={db}&export_columns=Ph,Nq,Cp,Co,Nr,Td&display_limit=50
```

**4. Domain Organic Keywords (domain_organic)**
```
https://api.semrush.com/?type=domain_organic&key={KEY}&domain={domain}&database={db}&export_columns=Ph,Po,Nq,Cp,Co,Tr,Tc,Nr,Td&display_limit=100
```
Additional columns: Po=Position, Tr=Traffic, Tc=Traffic Cost

**5. Keyword Difficulty (phrase_kdi)**
```
https://api.semrush.com/?type=phrase_kdi&key={KEY}&phrase={keyword}&database={db}&export_columns=Ph,Kd
```
Columns: Kd=Keyword Difficulty (0-100)

### Database Codes
- `us` (United States - default)
- `uk` (United Kingdom)
- `ca` (Canada)
- `au` (Australia)
- `de`, `fr`, `es`, `it`, `br`, `in`, `jp`

Ask the user for target market if not specified. Default to `us`.

## Research Process

### Step 1: Understand the Brief

Ask or infer:
- **Niche/Topic:** What is the site about?
- **Target audience:** Who are they trying to reach?
- **Business model:** How do they monetize? (SaaS, ecommerce, ads, affiliate)
- **Current domain:** If they have one, pull existing rankings
- **Target market:** Which country/language?
- **Competitors:** Known competitors to analyze

### Step 2: Seed Keyword Discovery

Generate 10-20 seed keywords based on the brief. Use three methods:

**Method A: Brainstorm seeds** from the topic
- Core product/service terms
- Problem terms ("how to fix...", "why is...")
- Audience terms (job titles, demographics)
- Alternative terms and synonyms

**Method B: Pull competitor keywords** using `domain_organic` for 2-3 competitor domains

**Method C: Expand seeds** using `phrase_related` and `phrase_questions` for each seed

### Step 3: Analyze Each Keyword

For every keyword candidate, collect via API:

| Metric | Source | What it tells you |
|--------|--------|-------------------|
| Search Volume (Nq) | phrase_all | Monthly searches |
| Keyword Difficulty (Kd) | phrase_kdi | How hard to rank (0-100) |
| CPC (Cp) | phrase_all | Commercial value indicator |
| Competition (Co) | phrase_all | PPC competition (0-1) |
| Trend (Td) | phrase_all | 12-month trend data |
| SERP Results (Nr) | phrase_all | Total competing pages |

### Step 4: Classify by Search Intent

Categorize every keyword into one of four intents:

| Intent | Signals | Examples | Content Type |
|--------|---------|----------|--------------|
| **Informational** | how, what, why, guide, tutorial, tips | "how to start a blog" | Blog post, guide, video |
| **Navigational** | brand names, specific product names, login | "semrush login" | Homepage, product page |
| **Commercial** | best, review, comparison, vs, top, alternatives | "best SEO tools 2025" | Comparison, review, listicle |
| **Transactional** | buy, price, discount, coupon, free trial, sign up | "semrush pricing" | Landing page, product page |

**Intent classification rules:**
- "how to" / "what is" / "why" = Informational
- "{brand} + {feature}" = Navigational
- "best" / "top" / "vs" / "alternative" / "review" = Commercial Investigation
- "buy" / "price" / "discount" / "free" / "download" / "sign up" = Transactional
- If ambiguous, check the SERP: majority blog posts = informational, majority product pages = transactional

### Step 5: Build Topic Clusters

Organize keywords into pillar-cluster structure:

```
Pillar Page: [Broad topic keyword - high volume, high difficulty]
  |
  +-- Cluster 1: [Subtopic keyword group]
  |     +-- Supporting keyword 1
  |     +-- Supporting keyword 2
  |     +-- Question keyword 1
  |
  +-- Cluster 2: [Subtopic keyword group]
  |     +-- Supporting keyword 1
  |     +-- Supporting keyword 2
  |
  +-- Cluster 3: ...
```

**Clustering rules:**
- Pillar: Volume > 5,000, KD 40-80, broad topic
- Cluster head: Volume 1,000-5,000, KD 20-50, specific subtopic
- Supporting: Volume 100-1,000, KD < 30, long-tail variations
- Each cluster should have 3-8 supporting keywords
- Every supporting page links back to the pillar page

### Step 6: Prioritize with the KOB Score

Calculate the Keyword Opposition to Benefit (KOB) score for prioritization:

```
KOB Score = (Search Volume * CTR Estimate * Business Value) / Keyword Difficulty

Where:
- CTR Estimate: Position 1 = 0.30, Pos 2 = 0.15, Pos 3 = 0.10 (use 0.15 as default)
- Business Value: 3 = direct revenue keyword, 2 = consideration keyword, 1 = awareness keyword
- Keyword Difficulty: 1-100 from SemRush (use max(KD, 1) to avoid division by zero)
```

**Priority tiers:**
- KOB > 50: High priority - target first
- KOB 20-50: Medium priority - target in months 2-3
- KOB 5-20: Low priority - target later
- KOB < 5: Deprioritize unless strategically important

### Step 7: Find Content Gaps

Compare the user's domain against competitors:

1. Pull top 100 keywords for each competitor via `domain_organic`
2. Identify keywords where competitors rank but user does not
3. Filter for keywords with KOB > 20
4. These are content gap opportunities

## Output Format

Present results in this structure:

```markdown
# Keyword Research Report: {Topic/Niche}
**Date:** {date}
**Target Market:** {country}
**Total Keywords Found:** {count}
**Total Monthly Search Volume:** {sum}

## Top 20 Keywords by KOB Score

| # | Keyword | Volume | KD | CPC | Intent | KOB Score |
|---|---------|--------|-----|-----|--------|-----------|
| 1 | {keyword} | {vol} | {kd} | ${cpc} | {intent} | {kob} |
| ... | ... | ... | ... | ... | ... | ... |

## Topic Clusters

### Pillar: {Pillar keyword} (Volume: {vol}, KD: {kd})

| Cluster | Head Keyword | Volume | KD | Supporting Keywords |
|---------|-------------|--------|-----|---------------------|
| {name} | {keyword} | {vol} | {kd} | kw1, kw2, kw3 |

### Content Plan

| Priority | Keyword | Intent | Content Type | Est. Monthly Traffic |
|----------|---------|--------|-------------|---------------------|
| 1 | {keyword} | {intent} | {type} | {vol * 0.15} |
| ... | ... | ... | ... | ... |

## Question Keywords (FAQ Opportunities)

| Question | Volume | KD | Suggested Content |
|----------|--------|-----|-------------------|
| {question} | {vol} | {kd} | {content type} |

## Content Gaps vs. Competitors

| Keyword | Volume | KD | Competitor Ranking | Opportunity |
|---------|--------|-----|--------------------|-------------|
| {keyword} | {vol} | {kd} | {competitor}: #{pos} | {content type} |

## Recommended Next Steps

1. {Specific action item with keyword target}
2. ...
```

## Tips for Better Results

- **Batch API calls** to conserve API credits. Query related keywords in groups.
- **Always check trends.** A keyword with declining volume may not be worth targeting.
- **CPC indicates money intent.** High CPC keywords ($5+) usually have strong commercial intent even if not obvious.
- **Low KD is not always easy.** If all top results are from DR 80+ sites, a KD of 20 may still be hard for a new site.
- **Local vs. national.** For local businesses, append city/state to seed keywords.
- **Seasonal keywords.** Note if trends show seasonality; plan content 2-3 months before peak.
- If the API returns an error or no data, inform the user of the specific issue rather than guessing.

## Supplementary API Integrations

These APIs complement SemRush and can be used as alternatives or for additional data points. They are not required if SemRush is available.

### DataForSEO (Alternative/Complement to SemRush)

If `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` are available, use DataForSEO for keyword search volume and related data. This is especially useful as a fallback when SemRush credits are limited or for cross-referencing data.

**Search Volume Endpoint:**

```bash
# Get keyword search volume data from DataForSEO
curl -s -X POST "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live" \
  -H "Authorization: Basic $(echo -n "${DATAFORSEO_LOGIN}:${DATAFORSEO_PASSWORD}" | base64)" \
  -H "Content-Type: application/json" \
  -d '[{"keywords": ["keyword1", "keyword2", "keyword3"], "location_code": 2840, "language_code": "en"}]'
```

**Parsing the response:**

```bash
# Extract keyword metrics from DataForSEO response
curl -s -X POST "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live" \
  -H "Authorization: Basic $(echo -n "${DATAFORSEO_LOGIN}:${DATAFORSEO_PASSWORD}" | base64)" \
  -H "Content-Type: application/json" \
  -d '[{"keywords": ["keyword1", "keyword2"], "location_code": 2840, "language_code": "en"}]' | \
  jq '.tasks[0].result[] | {
    keyword: .keyword,
    search_volume: .search_volume,
    competition: .competition,
    competition_index: .competition_index,
    cpc: .cpc,
    monthly_searches: .monthly_searches
  }'
```

Key fields:
- **`search_volume`** - Average monthly search volume
- **`competition`** - Competition level: "LOW", "MEDIUM", or "HIGH"
- **`competition_index`** - Numeric competition score (0-100)
- **`cpc`** - Cost per click in USD
- **`monthly_searches`** - Array of 12 monthly volume data points (useful for identifying seasonal trends)

**Common location codes:**
- `2840` - United States
- `2826` - United Kingdom
- `2124` - Canada
- `2036` - Australia
- `2250` - France
- `2158` - Germany

**Keyword Suggestions Endpoint:**

```bash
# Get keyword suggestions (similar to SemRush phrase_related)
curl -s -X POST "https://api.dataforseo.com/v3/keywords_data/google_ads/keywords_for_keywords/live" \
  -H "Authorization: Basic $(echo -n "${DATAFORSEO_LOGIN}:${DATAFORSEO_PASSWORD}" | base64)" \
  -H "Content-Type: application/json" \
  -d '[{"keywords": ["seed keyword"], "location_code": 2840, "language_code": "en", "sort_by": "search_volume"}]'
```

**When to use DataForSEO vs SemRush:**
- Use **SemRush** as the primary source for keyword difficulty, competitor analysis, and domain organic keywords
- Use **DataForSEO** for bulk search volume lookups (supports up to 700 keywords per request, more cost-effective for large batches)
- Use **DataForSEO** when you need Google Ads-aligned data (their data comes directly from Google Keyword Planner)
- Cross-reference both sources when search volume numbers differ significantly

### SerpAPI (People Also Ask & Related Searches)

If `SERPAPI_API_KEY` is available, use SerpAPI to extract "People Also Ask" questions and related searches directly from Google SERPs. This data is not available from SemRush and is valuable for FAQ sections and content ideation.

**Search Endpoint:**

```bash
# Get SERP data including People Also Ask and related searches
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=10"
```

**Parsing People Also Ask:**

```bash
# Extract People Also Ask questions
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=10" | \
  jq -r '.related_questions[] | {
    question: .question,
    snippet: .snippet,
    link: .link,
    title: .title
  }'
```

Key response sections:
- **`related_questions`** - Array of "People Also Ask" questions with snippets and source URLs
- **`related_searches`** - Array of related search queries that Google suggests
- **`organic_results`** - Top 10 organic results (useful for SERP analysis)

**Parsing Related Searches:**

```bash
# Extract related searches for content ideation
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=10" | \
  jq -r '.related_searches[] | .query'
```

**How to use SerpAPI data in keyword research:**

1. **FAQ content:** Use "People Also Ask" questions directly as H2/H3 headings in blog posts or as FAQ schema entries. These are questions Google already associates with the keyword.
2. **Content gap discovery:** If a PAA question has a weak snippet answer (short, vague, or from a low-authority site), that is an opportunity to write a better answer and win the featured snippet.
3. **Keyword expansion:** Related searches are Google's own suggestions for related topics. Add these to your keyword list and check their volume via SemRush or DataForSEO.
4. **Search intent validation:** The organic results show what content types Google ranks for this keyword. If all top 10 are blog posts, write a blog post. If they are product pages, a blog post will not rank.
5. **Cluster building:** Group PAA questions and related searches by subtopic to identify natural content clusters.

**Additional SerpAPI parameters:**
- `location=United+States` - Geo-target the search
- `gl=us` - Country code for Google domain
- `hl=en` - Interface language
- `device=desktop` or `device=mobile` - Desktop vs mobile SERPs (mobile may show different PAA questions)

**Note:** SerpAPI charges per search. Use it strategically for your highest-priority keywords rather than for bulk research. Pair it with SemRush for volume data and DataForSEO for bulk lookups.

### Serping API (People Also Ask & Related Searches — free tier)

If `SERPINGAPI_API_KEY` is available, use Serping API (https://serpingapi.com) for the same "People Also Ask" and related-searches data from live Google SERPs. The free Reader plan includes 1,000 searches per month with no credit card, so it is a good default when no SerpAPI key is set. Paid plans are flat monthly (from $49 for 20,000 searches).

**Search Endpoint:**

```bash
# Get SERP data including People Also Ask and related searches
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 10}'
```

**Parsing People Also Ask:**

```bash
# Extract People Also Ask questions
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 10}' | \
  jq -r '.peopleAlsoAsk[] | {question, snippet, link, title}'
```

Key response sections (present only when Google shows them):
- **`peopleAlsoAsk`** - Array of "People Also Ask" questions with snippets and source URLs
- **`relatedSearches`** - Array of `{ "query": ... }` objects that Google suggests
- **`organic`** - Organic results with `position`, `title`, `link`, `snippet`
- **`answerBox`** / **`knowledgeGraph`** - Featured snippet and knowledge panel, when present

**Parsing Related Searches:**

```bash
# Extract related searches for content ideation
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 10}' | \
  jq -r '.relatedSearches[] | .query'
```

Use the data exactly as described for SerpAPI above (FAQ headings, gap discovery, keyword expansion, intent validation, clustering).

**Additional Serping API parameters:** `location` (e.g. `"Seattle, Washington, United States"`), `page` (starting at 1), `tbs` time filter (`qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`). Every response carries `X-Quota-Remaining`, so you can tell the user how much of the monthly quota is left. Errors are `{"error": {"code", "message"}}` — `429 quota_exceeded` means the month's quota is spent; report it rather than retrying.
