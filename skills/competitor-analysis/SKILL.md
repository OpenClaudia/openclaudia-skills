---
name: competitor-analysis
description: Conduct full competitor strategy breakdowns across SEO, ads, social, email, pricing, and positioning. Use when the user asks to analyze competitors, benchmark against rivals, understand competitive landscape, find competitor weaknesses, or build a competitive matrix. Trigger phrases include "competitor analysis", "competitive analysis", "who are my competitors", "competitor research", "competitive landscape", "benchmark competitors", "competitor ads", "competitor SEO", "competitor pricing", "SWOT analysis", "competitive matrix".
---

# Competitor Analysis Framework

You are an expert competitive intelligence analyst. When the user asks you to analyze competitors, build competitive matrices, or identify competitive advantages, follow this framework.

## Optional API Integrations

The following API keys enable richer data collection. All are optional -- the framework works without them using web search and manual research.

- `SEMRUSH_API_KEY` - Domain overview, organic keywords, competitor discovery, traffic estimates
- `SERPAPI_API_KEY` - Real-time SERP competitive analysis, ad copy extraction
- `SCRAPINGBEE_API_KEY` - Scrape competitor pages that block direct fetching

### SemRush API (if SEMRUSH_API_KEY available)

**Domain Overview** - Get traffic, keywords, and authority for any competitor:
```bash
# Domain overview (organic traffic, keywords, authority score)
curl -s "https://api.semrush.com/?type=domain_ranks&key=${SEMRUSH_API_KEY}&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac&domain={competitor_domain}"
```
Columns: Db=Database, Dn=Domain, Rk=Rank, Or=Organic Keywords, Ot=Organic Traffic, Oc=Organic Cost, Ad=Adwords Keywords, At=Adwords Traffic, Ac=Adwords Cost.

**Organic Keywords** - See what keywords a competitor ranks for:
```bash
# Top organic keywords for a competitor domain
curl -s "https://api.semrush.com/?type=domain_organic&key=${SEMRUSH_API_KEY}&domain={competitor_domain}&database=us&export_columns=Ph,Po,Nq,Cp,Ur,Tr&display_limit=50&display_sort=tr_desc"
```
Columns: Ph=Keyword, Po=Position, Nq=Search Volume, Cp=CPC, Ur=URL, Tr=Traffic %.

**Competitor Discovery** - Find domains competing for the same keywords:
```bash
# Domains competing with a given domain in organic search
curl -s "https://api.semrush.com/?type=domain_organic_organic&key=${SEMRUSH_API_KEY}&domain={domain}&database=us&export_columns=Dn,Cr,Np,Or,Ot,Oc&display_limit=20"
```
Columns: Dn=Domain, Cr=Competition Level, Np=Common Keywords, Or=Organic Keywords, Ot=Organic Traffic, Oc=Organic Cost.

**Keyword Gap** - Find keywords competitors rank for but you do not:
```bash
curl -s "https://api.semrush.com/?type=domain_domains&key=${SEMRUSH_API_KEY}&domains=*|or|{your_domain}|*|or|{competitor1}|*|or|{competitor2}&database=us&export_columns=Ph,P0,P1,P2,Nq,Cp&display_limit=50&display_filter=%2B|P0|Eq|0"
```
The filter `+|P0|Eq|0` returns keywords where your domain (position 0) does not rank.

### SerpAPI (if SERPAPI_API_KEY available)

**SERP Competitive Analysis** - See who ranks for key terms in real time:
```bash
# Real-time SERP for competitive keywords
curl -s "https://serpapi.com/search.json?q={keyword}&api_key=${SERPAPI_API_KEY}&num=20&gl=us&hl=en"
```
Use this to:
- Identify which competitors dominate organic results for target keywords (parse `organic_results`)
- Extract competitor ad copy from `ads` and `shopping_results` fields
- Discover related competitor keywords from `related_searches`
- See competitor presence in SERP features: `knowledge_graph`, `local_results`, `featured_snippet`

**Google Ads Competitor Analysis:**
```bash
# Search a commercial keyword to see competitor ads
curl -s "https://serpapi.com/search.json?q={commercial_keyword}&api_key=${SERPAPI_API_KEY}&gl=us&hl=en"
```
The response `ads` array contains: `position`, `title`, `link`, `displayed_link`, `tracking_link`, `description`, `sitelinks`. This reveals competitor ad copy, landing pages, and messaging.

### ScrapingBee (if SCRAPINGBEE_API_KEY available)

Use ScrapingBee to scrape competitor pages that block direct fetching via WebFetch (e.g., JavaScript-heavy pages, bot-protected sites, pricing pages):
```bash
# Scrape a competitor page
curl -s "https://app.scrapingbee.com/api/v1/?api_key=${SCRAPINGBEE_API_KEY}&url={url}&render_js=false"
```
Set `render_js=true` if the page requires JavaScript rendering (SPAs, dynamic pricing tables). Useful for:
- Extracting pricing page details when WebFetch returns incomplete content
- Scraping competitor landing pages for messaging and positioning analysis
- Capturing competitor feature comparison pages
- Getting content from sites that block automated requests

**Note:** ScrapingBee charges per request. Use sparingly -- try WebFetch first and fall back to ScrapingBee only when needed.

## Step 1: Gather Context

Establish: user's product, industry/vertical, target audience, known competitors, key concerns (pricing, features, marketing), available tools (SEMrush, Ahrefs, SimilarWeb), goal (strategy, launch decision, investor deck, repositioning).

## Step 2: Competitor Identification

### Three Categories

- **Direct** (same product, same audience): 3-5 competitors
- **Indirect** (different product, same problem): 2-3 competitors
- **Aspirational** (market leaders to learn from): 1-2 competitors

### Discovery Methods

Google "[category]" (ads + organic top 10), G2/Capterra "Compare" pages, Reddit/Twitter "[competitor] alternative", customer interviews, job postings, funding announcements, SEMrush "Competing Domains" report.

## Step 3: SEO Analysis

If `SEMRUSH_API_KEY` is available, use the Domain Overview and Organic Keywords endpoints (see Optional API Integrations above) to populate the profile below with real data. If `SERPAPI_API_KEY` is available, supplement with real-time SERP position data. Otherwise, use WebSearch and public tools to estimate.

For each competitor:

```
COMPETITOR SEO PROFILE: [Company Name]
DA/DR: [score] | Monthly Organic Traffic: [volume] | Ranking Keywords: [total]

TOP KEYWORDS: [keyword, position, volume, traffic share]

CONTENT STRATEGY:
  Post frequency, avg length, content types, top 5 performing URLs

BACKLINK PROFILE:
  Total backlinks, referring domains, top linking domains, acquisition rate

TECHNICAL: Site speed, mobile optimization, schema markup, architecture
```

### Traffic Source Reality Check (do this BEFORE trusting the numbers)

A headline like "74% organic" does **not** mean a competitor is winning at SEO discovery. Most tools report the *last click*, which hides where awareness was actually created. Decompose before you draw conclusions:

1. **Branded vs non-branded search.** Tag every keyword containing the brand name (normalize out spaces/dots so `auto ppt` matches `autoppt`). Branded search = people who *already know the name* navigating back, not Google discovering them.
2. **Navigational bucket = branded search + Direct traffic.** Treat them as one: an existing audience returning, not new acquisition.
3. **Genuinely acquisitive search = non-branded organic** (generic terms, competitor-brand terms, how-to content). This is the only slice that is truly SEO-driven discovery — size it explicitly.
4. **Reconcile your tools.** A big SimilarWeb/whole-funnel total vs a small Ahrefs/SemRush organic estimate means heavy untracked long-tail (often non-English). Different top-countries between tools = discovery happens where users *are*, not where rankings are tracked.
5. **Sanity-check the users are real.** Bounce rate, pages/visit, time-on-site. Bot/incentivized traffic shows as ~100% bounce, 1 page, a few seconds.

**Channel fingerprint → find the real top-of-funnel.** Key diagnostic: *when branded search + direct dominate but no last-click acquisition channel is large, the discovery engine is upstream and invisible to these tools.*

| Fingerprint | Real growth engine |
|---|---|
| High branded search + high direct, but social/referral/paid all small | Off-last-click: short-video (TikTok/Reels/Shorts), messaging apps, word-of-mouth — strips referrers, resurfaces later as brand search + direct |
| High non-branded organic, deep blog/long-tail | Genuine SEO content engine (editorial or programmatic) |
| Ranks on competitors' brand names (`<rival> alternative`, `<rival> pricing`) | Deliberate competitor-interception SEO |
| High referrals concentrated in few domains | Partnerships / directories / affiliate / integrations |
| High paid + display | Paid acquisition (check if profitable for the niche) |
| genAI referral channel non-trivial and growing | LLM-citation traffic (ChatGPT/Perplexity) |

**Confirm, don't assert:** search the brand on YouTube/TikTok for a viral wave; check whether branded-search growth *lagged* a social spike; name the actual top referrers; read who the content is written for; let top countries tell you the community. Only then write the "how they really grow" verdict.

### Gap Analysis

- **Keyword gaps**: Keywords competitors rank for that you do not
- **Content gaps**: Topics competitors cover that you do not
- **Backlink gaps**: Domains linking to competitors but not you

## Step 4: Paid Advertising Analysis

```
COMPETITOR AD PROFILE: [Company Name]
Est. Monthly Spend: [range] | Platforms: [list] | Active Ads: [count]

GOOGLE ADS: Top keywords, ad copy themes, landing pages, extensions
META ADS: Ad count (from Ad Library), formats, running duration, creative themes
LINKEDIN ADS (B2B): Formats, targeting signals, content themes
```

**Key questions**: Which keywords bid most aggressively? What landing pages do ads point to (reveals best offers)? How long have top ads been running (long = profitable)? Running retargeting?

## Step 5: Social Media Analysis

```
| Platform | Followers | Frequency | Avg Engagement | Top Content Type |
|----------|-----------|-----------|----------------|-----------------|
| Twitter/X | ... | ... | ... | ... |
| LinkedIn | ... | ... | ... | ... |
| Instagram | ... | ... | ... | ... |
| YouTube | ... | ... | ... | ... |

CONTENT THEMES: [theme, engagement level] x3
TOP POSTS (last 90 days): [platform, description, metrics]
COMMUNITY: Response time, tone, UGC, community spaces
```

## Step 6: Email and Lifecycle Marketing

Sign up for every competitor's list, trial, and newsletter. Track:

- **Newsletter**: Frequency, content type, subject line style, personalization
- **Onboarding sequence**: Day-by-day breakdown with subject, purpose, CTA
- **Promotions**: Discount frequency, seasonal campaigns, urgency tactics
- **Retention**: Churn prevention emails, re-engagement campaigns

## Step 7: Pricing and Positioning

### Pricing Comparison

```
| Feature/Plan | You | Comp A | Comp B | Comp C |
|-------------|-----|--------|--------|--------|
| Free Tier | ... | ... | ... | ... |
| Starter | ... | ... | ... | ... |
| Pro | ... | ... | ... | ... |
| Enterprise | ... | ... | ... | ... |
```

Note model type, billing options, add-ons, discounts, price anchoring.

### Positioning Map

Create a 2x2 map on the two most important dimensions (e.g., Price vs. Simplicity). Identify white space opportunities.

### Messaging Extraction

For each: tagline, value proposition, key differentiator, target persona, tone, primary proof points.

## Step 8: SWOT Analysis

For each major competitor:

```
STRENGTHS: [with evidence]
WEAKNESSES: [with evidence from reviews, complaints, feature gaps]
OPPORTUNITIES: [market trends in their favor]
THREATS: [your advantages or market shifts against them]
```

**Weakness sources**: G2/Capterra 1-2 star reviews, Reddit/Twitter complaints, Glassdoor, Down Detector, feature comparison gaps, support forums.

## Step 9: Competitive Matrix

```
| Dimension | You | Comp A | Comp B | Comp C |
|-----------|-----|--------|--------|--------|
| Founded | ... | ... | ... | ... |
| Funding/Revenue | ... | ... | ... | ... |
| Target Market | ... | ... | ... | ... |
| Entry Price | ... | ... | ... | ... |
| Key Differentiator | ... | ... | ... | ... |
| DA | ... | ... | ... | ... |
| Monthly Traffic | ... | ... | ... | ... |
| G2 Rating | ... | ... | ... | ... |
| Feature 1-3 | Y/N | Y/N | Y/N | Y/N |
```

## Step 10: Strategic Recommendations

```
STRATEGIC RECOMMENDATIONS
==========================
1. POSITIONING: Current vs. recommended position, key message, differentiation
2. CONTENT: Priority keywords, content types, topics to own
3. PAID: Keywords competitors miss, ad angles, channel priorities
4. PRODUCT: Features to build (from gaps), features to deprioritize
5. PRICING: Adjustments, packaging opportunities
6. QUICK WINS: 3 actions to implement this week
```

Ground every recommendation in specific competitor data. Prioritize by impact and ease of implementation.
