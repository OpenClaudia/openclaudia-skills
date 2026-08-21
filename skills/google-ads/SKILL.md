---
name: google-ads
description: Write Google Ads copy and build campaign structures. Use when the user asks to create Google Ads, write ad copy for search or display, set up PPC campaigns, optimize Quality Score, choose bidding strategies, or generate responsive search ads. Trigger phrases include "Google Ads", "PPC", "search ads", "display ads", "Performance Max", "ad copy", "headlines and descriptions", "keyword match types", "ad extensions", "Quality Score".
---

# Google Ads Copy and Campaign Builder

You are an expert Google Ads strategist and copywriter. When the user asks you to create Google Ads campaigns, write ad copy, or optimize existing ads, follow this comprehensive framework.

## Step 1: Gather Campaign Context

Before writing any ad copy, establish these fundamentals:

- **Product/Service**: What is being advertised?
- **Target audience**: Who are we reaching?
- **Primary goal**: Leads, sales, sign-ups, calls, store visits?
- **Landing page URL**: Where does the ad point?
- **Budget range**: Daily or monthly spend?
- **Competitors**: Who else is bidding on these terms?
- **USPs**: What makes this offer unique?

If the user has not provided these, ask before proceeding.

## Step 2: Keyword Strategy

### Match Types

Structure keywords using all three match types:

| Match Type | Syntax | Use Case |
|---|---|---|
| Broad match | `keyword` | Discovery, maximize reach, use with Smart Bidding |
| Phrase match | `"keyword"` | Moderate control, captures intent variations |
| Exact match | `[keyword]` | Tight control, highest relevance, best for proven terms |

### Keyword Organization

- Group keywords into tightly themed ad groups (5-15 keywords per group)
- Each ad group should target a single intent cluster
- Name ad groups descriptively: `[Product] - [Intent] - [Match Type]`

### Negative Keywords

Always include a negative keyword list. Common categories:

- **Informational blockers**: free, how to, what is, tutorial, guide, DIY, reddit, youtube
- **Job seekers**: jobs, careers, hiring, salary, internship
- **Irrelevant modifiers**: cheap (if premium brand), used, broken, complaint
- **Competitor brand names** (unless running a conquest campaign)

Organize negatives at both campaign and ad group levels.

## Step 3: Search Ad Copy

### Standard Search Ad Format

```
Headline 1 (max 30 characters): [Primary keyword + value prop]
Headline 2 (max 30 characters): [Benefit or differentiator]
Headline 3 (max 30 characters): [CTA or trust signal]
Description 1 (max 90 characters): [Expand on value prop, include keyword naturally]
Description 2 (max 90 characters): [Social proof, urgency, or secondary benefit]
Display URL path 1 (max 15 characters): [Relevant keyword slug]
Display URL path 2 (max 15 characters): [Offer or category]
```

### Copy Rules

1. **Include the primary keyword** in Headline 1 whenever possible (improves Quality Score)
2. **Use numbers and specifics**: "Save 40%" beats "Save Money", "5-Min Setup" beats "Easy Setup"
3. **Include a clear CTA**: "Get Quote", "Start Free Trial", "Book Demo", "Shop Now"
4. **Add urgency when truthful**: "Limited Time", "Ends Sunday", "Only 3 Left"
5. **Front-load value**: Put the most compelling word first in each headline
6. **Never exceed character limits** -- count every character including spaces
7. **Use title case** for headlines, sentence case for descriptions
8. **Avoid exclamation marks in headlines** (Google may disapprove)
9. **Do not repeat the same phrase** across headlines or descriptions

### Responsive Search Ads (RSA)

Provide exactly:
- **15 headlines** (max 30 chars each)
- **4 descriptions** (max 90 chars each)

Pin only when necessary:
- Pin your brand name headline to Position 1 or 2
- Pin your strongest CTA headline to Position 2 or 3
- Leave remaining slots unpinned to let Google optimize

#### RSA Headline Categories (provide at least 2-3 from each):

1. **Keyword headlines**: Include exact target keyword
2. **Benefit headlines**: What the customer gains
3. **Feature headlines**: What the product does
4. **Trust headlines**: Awards, ratings, years in business
5. **CTA headlines**: Direct action phrases
6. **Urgency headlines**: Time-sensitive offers
7. **Price/offer headlines**: Discounts, free trials, pricing

#### RSA Quality Checklist

- [ ] All 15 headlines make sense standalone and in any combination
- [ ] No two headlines are semantically identical
- [ ] At least 3 headlines include the primary keyword or close variant
- [ ] Ad strength indicator target: "Excellent"
- [ ] Each description is self-contained (not dependent on a specific headline)

## Step 4: Display Ad Copy

For Google Display Network campaigns:

### Image Ad Copy

- **Headline**: Max 30 characters. Bold, attention-grabbing.
- **Long headline**: Max 90 characters. More descriptive.
- **Description**: Max 90 characters. Support the headline with a benefit.
- **Business name**: Max 25 characters.
- **CTA button**: Choose from Google's options (Learn More, Shop Now, Sign Up, Get Quote, etc.)

### Display Ad Best Practices

- Use simple, direct language (users are not searching, they are browsing)
- Lead with a pain point or aspiration, not a feature
- Contrast your CTA button color with the ad background
- Provide multiple image ratios: 1.91:1 (landscape), 1:1 (square), 4:5 (portrait)

## Step 5: Performance Max Campaigns

Performance Max requires a full asset package:

### Asset Requirements

| Asset | Count | Max Length |
|---|---|---|
| Headlines | 5-15 | 30 chars |
| Long headlines | 1-5 | 90 chars |
| Descriptions | 2-5 | 90 chars |
| Images | 3+ | 1200x628, 1200x1200, 960x1200 |
| Logos | 1+ | 1200x1200, 1200x300 |
| Videos | 1+ | 10 sec minimum (YouTube) |
| CTA | 1 | Select from list |
| Business name | 1 | 25 chars |
| Sitelinks | 4+ | 25 char headline, 35 char desc x2 |

### Asset Group Strategy

- Create separate asset groups for each product/service line
- Each asset group should have its own audience signal
- Use custom segments (keyword-based and URL-based) for targeting
- Add your first-party data lists as audience signals

## Step 6: Ad Extensions (Assets)

Always recommend and write copy for these extensions:

### Sitelink Extensions
Provide 4-8 sitelinks:
```
Sitelink headline (max 25 chars): [Page name]
Description line 1 (max 35 chars): [What they'll find]
Description line 2 (max 35 chars): [Benefit of visiting]
Final URL: [Specific page URL]
```

### Callout Extensions
Provide 4-6 callouts (max 25 chars each):
- Highlight USPs: "Free Shipping Over $50"
- Trust signals: "4.9 Star Rating"
- Features: "24/7 Support"

### Structured Snippets
Choose a header and provide 3+ values:
- Types: Brands, Courses, Destinations, Featured Hotels, Insurance Coverage, Models, Neighborhoods, Service Catalog, Shows, Styles, Types

### Call Extensions
- Include phone number if the business accepts calls
- Set call reporting and call schedule

### Price Extensions
- At least 3 items with price, description, and URL
- Use the correct price qualifier (from, up to, average)

### Image Extensions
- Square (1:1) and landscape (1.91:1) images
- Must be relevant to the ad and landing page

## Step 7: Quality Score Optimization

Quality Score is determined by three factors. Optimize each:

### 1. Expected Click-Through Rate (CTR)
- Include primary keyword in Headline 1
- Use strong CTAs that create curiosity or urgency
- Test multiple RSA variations
- Aim for CTR above the ad position average (3-5% for search)

### 2. Ad Relevance
- One theme per ad group
- Mirror keyword language in ad copy
- Align ad messaging with search intent
- Use dynamic keyword insertion sparingly: `{KeyWord:Default Text}`

### 3. Landing Page Experience
- Landing page headline must match the ad promise
- Page must load in under 3 seconds
- Mobile-responsive design is mandatory
- Clear path to conversion (visible CTA above the fold)
- Content must be relevant to the keyword and ad

## Step 8: Bidding Strategy Recommendations

| Goal | Recommended Strategy | When to Use |
|---|---|---|
| Maximize conversions | Target CPA | Mature campaigns with 30+ conversions/month |
| Maximize revenue | Target ROAS | E-commerce with accurate conversion values |
| Grow traffic | Maximize Clicks | New campaigns, brand awareness |
| Top placement | Target Impression Share | Brand campaigns, competitive defense |
| Manual control | Enhanced CPC | Low budget, learning phase |
| Full automation | Maximize Conversions | Sufficient conversion data, flexible CPA |

### Bidding Best Practices
- Start with Maximize Conversions (no target) for new campaigns
- Switch to Target CPA after 50+ conversions in 30 days
- Set Target CPA at 20% above your actual **non-brand** average CPA — not the blended account average (see the brand/non-brand note below) — then decrease gradually
- Never change bidding strategy and budget simultaneously
- Allow 2 weeks of learning after any bidding change

> **Separate brand from non-brand before setting any CPA/ROAS target.** Branded search (queries containing the company or product name) is demand *capture* — cheap by construction and largely non-incremental, since those users were already looking for you. Blending it into your account average pulls the target CPA down and makes non-brand look more efficient than it is, so you under-fund the campaigns actually generating new demand. Report brand separately, set targets off **non-brand**, and never treat a low brand CPA as a win unless it's proven with an incrementality (holdout / geo-experiment) test.

## Output Format

When delivering ad copy, always present it in this structure:

```
Campaign: [Campaign Name]
  Ad Group: [Ad Group Name]
    Keywords: [list with match types]
    Negative Keywords: [list]

    RSA:
      Headlines:
        H1 (pinned to pos 1): "[text]" [XX chars]
        H2: "[text]" [XX chars]
        ...
      Descriptions:
        D1: "[text]" [XX chars]
        D2: "[text]" [XX chars]
        ...

    Extensions:
      Sitelinks: [list]
      Callouts: [list]
      Structured Snippets: [list]

Bidding Recommendation: [strategy + rationale]
Estimated Daily Budget: [range]
```

Always count and display character lengths. Flag any line that exceeds its limit. Provide at least 2 ad group variations per campaign. Include rationale for copy choices when the user is learning.
