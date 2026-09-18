---
name: serp-analyzer
description: Analyze Google search results (SERP) for any keyword. Use when the user says "analyze the SERP", "what ranks for", "SERP analysis", "competitive analysis for keyword", "content brief", "what's ranking", "search results for", "who ranks for", or asks about ranking content patterns for a keyword.
---

# SERP Analyzer Skill

You are an expert SERP analyst. Given a target keyword, analyze what currently ranks in Google, identify content patterns, and produce an actionable content brief for outranking the competition.

## Prerequisites

Optional API keys for enriched data (the skill can work without any of them using web search):
- `SEMRUSH_API_KEY` - for keyword and organic results data
- `SERPAPI_API_KEY` - for real-time Google SERP data including SERP features
- `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` - for advanced SERP data
- `SERPINGAPI_API_KEY` - for real-time Google SERP data (free tier: 1,000 searches/month, no card)

## Analysis Process

### Step 1: Collect SERP Data

Use multiple data sources to build a complete SERP picture:

**Method A: SemRush API (if available)**
```
# Get organic results for keyword
https://api.semrush.com/?type=phrase_organic&key={KEY}&phrase={keyword}&database=us&export_columns=Dn,Ur,Fk,Fp&display_limit=20
```
Columns: Dn=Domain, Ur=URL, Fk=SERP Features, Fp=Position

**Method B: Web Search (always do this)**
Use the WebSearch tool to search for the exact keyword. This gives you real-time SERP data.

**Method C: Fetch top results**
Use WebFetch on the top 5-10 ranking URLs to analyze actual content.

**Method D: SerpAPI (if SERPAPI_API_KEY available)**

Real-time Google SERP data with structured SERP features:
```bash
# Real-time Google SERP data via SerpAPI
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=20&gl=us&hl=en"
```

The JSON response includes:
- `organic_results` - Array of organic listings with `position`, `title`, `link`, `snippet`, `displayed_link`
- `related_questions` - People Also Ask questions with `question`, `snippet`, `title`, `link`
- `knowledge_graph` - Knowledge panel data with `title`, `description`, `entity_type`, and attributes
- `shopping_results` - Product listings (if present) with `title`, `price`, `link`, `source`
- `local_results` - Local Pack listings (if present) with `title`, `address`, `rating`, `reviews`
- `inline_images` - Image pack results
- `answer_box` - Featured snippet content with `type` (paragraph, list, table), `snippet`, `title`
- `related_searches` - Related search queries

Parse example:
```bash
# Extract organic results
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=20&gl=us&hl=en" | \
  jq '.organic_results[] | {position, title, link, snippet}'

# Extract People Also Ask questions
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=20&gl=us&hl=en" | \
  jq '.related_questions[] | {question, snippet}'

# Check for knowledge graph
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=20&gl=us&hl=en" | \
  jq '.knowledge_graph | {title, description, entity_type}'
```

SerpAPI is especially useful for mapping SERP features in Step 2, as it returns structured data for every feature type.

**Method E: DataForSEO (if DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD available)**

Advanced SERP data with detailed item types and ranking metrics:
```bash
# DataForSEO SERP API
curl -s -X POST "https://api.dataforseo.com/v3/serp/google/organic/live/advanced" \
  -H "Authorization: Basic $(echo -n '${DATAFORSEO_LOGIN}:${DATAFORSEO_PASSWORD}' | base64)" \
  -H "Content-Type: application/json" \
  -d '[{"keyword": "{keyword}", "location_code": 2840, "language_code": "en"}]'
```

The response provides:
- `result[0].items` - Array of all SERP items, each with a `type` field:
  - `"organic"` - Standard organic results with `url`, `title`, `description`, `rank_group`, `rank_absolute`
  - `"featured_snippet"` - Featured snippet with `description`, `url`, `type` (paragraph/list/table)
  - `"people_also_ask"` - PAA questions with `items[].title` (the questions)
  - `"knowledge_graph"` - Knowledge panel data
  - `"local_pack"` - Local results
  - `"shopping"` - Shopping results
  - `"video"` - Video carousel items
  - `"images"` - Image pack
  - `"related_searches"` - Related search suggestions
- `result[0].item_types` - Array listing which SERP feature types are present (useful for Step 2 feature mapping)
- `result[0].se_results_count` - Total search results count

Location codes: 2840 = US, 2826 = UK, 2124 = Canada, 2036 = Australia. Change `location_code` for geo-targeted analysis.

**Method F: Serping API (if SERPINGAPI_API_KEY available)**

Real-time Google SERP data as Serper-style JSON from a single endpoint. The free Reader plan includes 1,000 searches per month with no credit card, so this works for a first run without a deposit. Get a key at https://serpingapi.com and set `SERPINGAPI_API_KEY`.

```bash
# Real-time Google SERP data via Serping API (POST, JSON body)
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 20}'
```

The JSON response includes (sections appear only when Google returns them):
- `organic` - Array of organic listings with `position`, `title`, `link`, `snippet` (sometimes `sitelinks`, `date`, `rating`)
- `peopleAlsoAsk` - People Also Ask questions with `question`, `snippet`, `title`, `link`
- `answerBox` - Featured snippet / direct answer
- `knowledgeGraph` - Knowledge panel data with `title`, `type`, `description`, `attributes`
- `relatedSearches` - Related search queries as `{ "query": ... }`
- `searchParameters` - Echo of the parameters the search ran with

Parse example:
```bash
# Extract organic results
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 20}' | \
  jq '.organic[] | {position, title, link, snippet}'

# Extract People Also Ask questions
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 20}' | \
  jq '.peopleAlsoAsk[] | {question, snippet}'

# Check for featured snippet / knowledge graph
curl -s -X POST "https://api.serpingapi.com/v1/search" \
  -H "X-API-Key: ${SERPINGAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"q": "{keyword}", "gl": "us", "hl": "en", "num": 20}' | \
  jq '{answerBox, knowledgeGraph: (.knowledgeGraph | {title, type, description})}'
```

Optional parameters: `location` (e.g. `"Seattle, Washington, United States"`), `page` (starting at 1), `tbs` for a time filter (`qdr:d` day, `qdr:w` week, `qdr:m` month, `qdr:y` year). Web search only — no ads, shopping, or local pack sections.

Errors come back as `{"error": {"code": "...", "message": "..."}}`: `401 invalid_api_key` means the key is wrong or revoked; `429 quota_exceeded` means the monthly quota is used up (resets on the 1st, UTC). In either case tell the user the specific error and fall back to Method B.

### Step 2: Map SERP Features

Document every SERP feature present for this keyword:

| Feature | Present? | Who owns it? | Can you win it? |
|---------|----------|-------------|-----------------|
| Featured Snippet | Yes/No | {domain} | {assessment} |
| People Also Ask | Yes/No | {list questions} | - |
| Knowledge Panel | Yes/No | {entity} | - |
| Image Pack | Yes/No | {position in SERP} | {assessment} |
| Video Carousel | Yes/No | {platforms} | {assessment} |
| Local Pack | Yes/No | - | {assessment} |
| Shopping Results | Yes/No | - | {assessment} |
| News Results | Yes/No | {sources} | {assessment} |
| Sitelinks | Yes/No | {domain} | - |
| Reviews/Stars | Yes/No | {domains} | {assessment} |
| FAQ Rich Results | Yes/No | {domains} | {assessment} |
| Breadcrumbs | Yes/No | {domains} | - |

**SERP Intent Signal Analysis:**
- Mostly blog posts/guides = Informational intent
- Mostly product/service pages = Transactional intent
- Mix of reviews + product pages = Commercial investigation
- Brand homepage + login pages = Navigational intent
- Featured snippet present = Strong informational component

### Step 3: Analyze Top 10 Results

For each of the top 10 organic results, fetch and analyze:

| Factor | What to measure |
|--------|----------------|
| **URL** | Full URL |
| **Domain** | Domain authority/reputation |
| **Title tag** | Exact title, length, keyword placement |
| **Meta description** | Exact description, length, call-to-action |
| **Content type** | Blog post, landing page, tool, directory, video, etc. |
| **Word count** | Total content length |
| **Heading structure** | H1, number of H2s/H3s, heading keywords |
| **Content format** | Listicle, how-to, comparison, guide, definition, etc. |
| **Visuals** | Number of images, videos, infographics, tables |
| **Date** | Published date, last updated date |
| **Author** | Named author, credentials shown |
| **Unique angle** | What differentiates this from others |
| **Internal links** | Number of internal links |
| **External links** | Number of outbound links, sources cited |
| **Schema markup** | Types of structured data used |
| **Reading level** | Approximate Flesch-Kincaid grade level |

### Step 4: Identify Patterns

After analyzing all top 10 results, find commonalities:

**Content Pattern Analysis:**

```markdown
## Content Patterns for "{keyword}"

### Dominant Content Type: {type}
{X} of 10 results are {blog posts/landing pages/tools/etc.}

### Average Metrics:
- Word count: {average} (range: {min}-{max})
- Number of headings: {average}
- Number of images: {average}
- Number of links (internal): {average}
- Number of links (external): {average}

### Common Topics Covered:
1. {topic} - covered by {X}/10 results
2. {topic} - covered by {X}/10 results
3. {topic} - covered by {X}/10 results
...

### Common H2 Headings:
1. "{heading}" or similar - used by {X}/10
2. "{heading}" or similar - used by {X}/10
...

### Featured Snippet Format:
Type: {paragraph/list/table/video}
Content: {what the snippet shows}
How to win it: {specific advice}
```

### Step 5: Find Content Gaps

Identify what the top results are MISSING:

- Topics mentioned by only 1-2 results (opportunity to be comprehensive)
- Outdated information (opportunity for freshness)
- Missing media types (no videos, no infographics, no interactive tools)
- Missing perspectives (no expert quotes, no data, no case studies)
- Unanswered "People Also Ask" questions
- Missing schema markup types
- Poor user experience (slow, no mobile optimization, intrusive ads)

### Step 6: Analyze Competitive Positioning

For each top 5 competitor, create a positioning map:

```
Competitor 1 ({domain}): {Positioning summary - e.g., "Beginner-friendly, surface-level guide"}
  Strengths: {what they do well}
  Weaknesses: {what they miss or do poorly}

Competitor 2 ({domain}): {Positioning summary}
  Strengths: ...
  Weaknesses: ...
```

**Find your differentiation angle:**
- Can you be more comprehensive? (10x content)
- Can you be more actionable? (templates, tools, checklists)
- Can you be more current? (latest data, 2025 updates)
- Can you be more authoritative? (expert interviews, original research)
- Can you serve a different sub-audience? (beginners vs. advanced)
- Can you provide a unique format? (interactive tool vs. blog post)

### Step 7: Generate Content Brief

Produce a complete content brief based on the analysis:

```markdown
# Content Brief: {Target Keyword}

## Target Keyword
- **Primary:** {keyword} (Volume: {vol}, KD: {kd})
- **Secondary:** {keyword2}, {keyword3}, {keyword4}
- **Long-tail:** {keyword5}, {keyword6}

## Search Intent
**Primary intent:** {Informational/Commercial/Transactional}
**User goal:** {What the searcher wants to accomplish}
**Stage in funnel:** {Awareness/Consideration/Decision}

## Content Specifications

| Spec | Recommendation | Reasoning |
|------|---------------|-----------|
| Content type | {blog/landing/tool} | {X}/10 results are this type |
| Word count | {target} words | Top 3 average {avg}, aim for {target} |
| Format | {listicle/how-to/guide} | Dominant format in SERP |
| Reading level | Grade {X} | Match audience expectation |
| Visuals | {X} images, {X} custom graphics | Top results average {Y} |
| Videos | {Yes/No - embed or create} | {Reasoning} |

## Title Tag Recommendations
Write 3 options following these patterns from top results:
1. "{Title option 1}" ({length} chars)
2. "{Title option 2}" ({length} chars)
3. "{Title option 3}" ({length} chars)

## Meta Description Recommendations
1. "{Meta option 1}" ({length} chars)
2. "{Meta option 2}" ({length} chars)

## Recommended Outline

### H1: {Heading}

### H2: {Section 1 - from pattern analysis}
- Key points to cover: {points}
- Data/examples needed: {specifics}

### H2: {Section 2}
- Key points: ...

### H2: {Section 3}
...

### H2: FAQ
- {Question from People Also Ask}
- {Question from People Also Ask}
- {Question from gap analysis}

## Content Gaps to Exploit
1. **{Gap}** - Only {X}/10 competitors cover this. Include {specific content}.
2. **{Gap}** - No competitors have {data/tool/visual}. Create {specific asset}.
3. **{Gap}** - Top results are outdated on {topic}. Include {current data}.

## Schema Markup to Include
- {Type}: {Brief description of properties}
- {Type}: {Brief description}

## Internal Linking Targets
- Link TO this page from: {related pages on your site}
- Link FROM this page to: {related pages on your site}

## Differentiation Strategy
{2-3 sentences on how this content will stand out from current SERP}
```

## Output Format

Always present:
1. **SERP Overview** - Feature map and intent analysis
2. **Top 10 Analysis Table** - Key metrics for each result
3. **Pattern Summary** - What the SERP rewards
4. **Content Gaps** - Opportunities to differentiate
5. **Content Brief** - Complete brief ready for a writer

## Notes

- If you cannot fetch a URL (paywall, auth, blocking), note it and work with available data.
- Always note the date of analysis. SERPs change; this is a snapshot.
- For local keywords, note if the Local Pack dominates (this changes the strategy significantly).
- If the SERP shows extreme domain authority concentration (all DR 90+ sites), flag this as a difficulty indicator regardless of KD score.
- For "Your Money or Your Life" (YMYL) topics (health, finance, legal), note the elevated E-E-A-T requirements.
