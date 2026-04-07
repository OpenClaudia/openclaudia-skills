# How to Use OpenClaudia

A practical guide to getting the most out of OpenClaudia's 62+ marketing skills in Claude Code.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Your First Skill](#your-first-skill)
- [Skill Categories & Workflows](#skill-categories--workflows)
  - [SEO Workflow](#seo-workflow)
  - [Content Marketing Workflow](#content-marketing-workflow)
  - [Social Media Workflow](#social-media-workflow)
  - [Email Marketing Workflow](#email-marketing-workflow)
  - [Ads & Conversion Workflow](#ads--conversion-workflow)
  - [Analytics & Reporting Workflow](#analytics--reporting-workflow)
  - [Strategy & Planning Workflow](#strategy--planning-workflow)
- [Setting Up API Keys](#setting-up-api-keys)
- [Combining Skills](#combining-skills)
- [Project-Level vs Global Skills](#project-level-vs-global-skills)
- [Tips & Best Practices](#tips--best-practices)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

1. **Claude Code** installed and authenticated. [Install guide](https://docs.anthropic.com/en/docs/claude-code)
2. A terminal (macOS, Linux, or WSL on Windows)
3. Node.js 18+ (for the installer CLI)

## Installation

### Install all skills (recommended for first-time users)

```bash
npx openclaudia install --all
```

This copies all 62+ skill files to `~/.claude/skills/`, making them available as slash commands in every Claude Code session.

### Install specific skills

```bash
# Just the ones you need
npx openclaudia install seo-audit write-blog reddit-marketing

# List available skills
npx openclaudia list
```

### Manual installation

```bash
# Clone the repo
git clone https://github.com/OpenClaudia/openclaudia-skills.git

# Copy skills to your global skills directory
cp -r openclaudia-skills/skills/seo-audit ~/.claude/skills/

# Or to a specific project
cp -r openclaudia-skills/skills/seo-audit ./your-project/.claude/skills/
```

### Verify installation

Open Claude Code and type `/` — you should see the installed skills listed as available slash commands.

---

## Your First Skill

Let's run an SEO audit to see how skills work:

```
$ claude

> /seo-audit https://yoursite.com
```

Claude will:
1. Crawl your site's key pages
2. Check meta tags, headings, schema markup, and page speed
3. Analyze keyword optimization and internal linking
4. Generate a detailed report with actionable fixes
5. Save the report as a file in your project

That's it. Every skill follows this pattern: **invoke with a slash command, provide input, get output.**

---

## Skill Categories & Workflows

### SEO Workflow

Start with an audit, then fix issues systematically.

```
# Step 1: Audit your site
> /seo-audit https://yoursite.com

# Step 2: Research keywords for your niche
> /keyword-research "AI form builder"

# Step 3: Analyze what competitors rank for
> /serp-analyzer "best AI form builder 2026"

# Step 4: Audit your backlink profile
> /backlink-audit https://yoursite.com

# Step 5: Generate schema markup for key pages
> /schema-markup https://yoursite.com/pricing

# Step 6: Create SEO pages at scale
> /programmatic-seo "Create city landing pages for 50 US metros"
```

**Skills used:** `seo-audit` → `keyword-research` → `serp-analyzer` → `backlink-audit` → `schema-markup` → `programmatic-seo`

### Content Marketing Workflow

Plan your content strategy, then produce and distribute.

```
# Step 1: Build a content strategy
> /content-strategy "B2B SaaS project management tool"

# Step 2: Find content gaps vs competitors
> /content-gap-analysis competitor1.com competitor2.com

# Step 3: Create a content brief for writers
> /seo-content-brief "best project management tools for remote teams"

# Step 4: Write the blog post
> /write-blog "Best Project Management Tools for Remote Teams in 2026"

# Step 5: Polish the copy
> /copy-editing ./blog-post.md

# Step 6: Repurpose into social content
> /content-repurposing ./blog-post.md
```

**Skills used:** `content-strategy` → `content-gap-analysis` → `seo-content-brief` → `write-blog` → `copy-editing` → `content-repurposing`

### Social Media Workflow

Create and distribute content across platforms.

```
# Step 1: Plan a content calendar
> /content-calendar "SaaS product launch, 4 weeks, focus on LinkedIn and Reddit"

# Step 2: Write a LinkedIn thought leadership post
> /linkedin-content "Lessons learned scaling to 100K users"

# Step 3: Create a Reddit marketing campaign
> /reddit-marketing "Share our AI form builder in relevant subreddits"

# Step 4: Write a viral thread for X
> /thread-writer "How we grew from 0 to 100K monthly visitors in 12 months"

# Step 5: Cross-post to Bluesky
> /bluesky "Announce our new feature launch"

# Step 6: Post to Discord and Slack
> /discord-bot "New feature: AI-powered form validation"
> /slack-bot "Weekly marketing update: traffic up 20%"
```

**Skills used:** `content-calendar` → `linkedin-content` → `reddit-marketing` → `thread-writer` → `bluesky` → `discord-bot` / `slack-bot`

### Email Marketing Workflow

Build email sequences that convert.

```
# Step 1: Create a drip campaign
> /email-sequence --type product-launch

# Step 2: A/B test subject lines
> /email-subject-lines "Product launch announcement for AI form builder"
```

**Skills used:** `email-sequence` → `email-subject-lines`

**Note:** Requires `RESEND_API_KEY` to actually send emails. Without it, skills generate the email copy for you to send manually.

### Ads & Conversion Workflow

Optimize your ad spend and landing pages.

```
# Step 1: Create Google Ads campaigns
> /google-ads "AI form builder, target: small business owners, budget: $2000/month"

# Step 2: Create Facebook/Meta ad campaigns
> /facebook-ads "Retarget website visitors with feature demo video"

# Step 3: Create LinkedIn ads for B2B
> /linkedin-ads "Target VP Engineering at companies with 50-500 employees"

# Step 4: Optimize landing page conversion
> /page-cro https://yoursite.com/pricing

# Step 5: Set up A/B tests
> /ab-test-setup "Test pricing page with annual vs monthly toggle"

# Step 6: Analyze video ad performance
> /video-ad-analysis "Review our top 3 YouTube pre-roll ads"
```

**Skills used:** `google-ads` → `facebook-ads` → `linkedin-ads` → `page-cro` → `ab-test-setup` → `video-ad-analysis`

### Analytics & Reporting Workflow

Pull data from your tools and generate insights.

```
# Step 1: Check Google Analytics
> /google-analytics "Show me traffic trends for the last 90 days"

# Step 2: Analyze Search Console performance
> /search-console "Top queries and pages for the last month"

# Step 3: Run SemRush competitive analysis
> /semrush-research "Compare our domain with competitor.com"

# Step 4: Pull Google Ads performance
> /google-ads-report "Campaign performance for March 2026"

# Step 5: Check YouTube channel stats
> /youtube-analytics "Video performance for the last 30 days"

# Step 6: Monitor brand mentions
> /brand-monitor "Track mentions of our brand across the web"
```

**Skills used:** `google-analytics` → `search-console` → `semrush-research` → `google-ads-report` → `youtube-analytics` → `brand-monitor`

### Strategy & Planning Workflow

Plan your marketing strategy from scratch.

```
# Step 1: Define your ideal customer
> /icp-builder "B2B SaaS selling to enterprise HR teams"

# Step 2: Analyze competitors
> /competitor-analysis competitor.com

# Step 3: Build a growth strategy
> /growth-strategy "Double organic traffic in 6 months"

# Step 4: Plan a product launch
> /launch-strategy "Launching v2.0 of our platform in Q2"

# Step 5: Optimize pricing
> /pricing-strategy https://yoursite.com/pricing

# Step 6: Get creative marketing ideas
> /marketing-ideas "We're a dev tools startup with $5K/month marketing budget"
```

**Skills used:** `icp-builder` → `competitor-analysis` → `growth-strategy` → `launch-strategy` → `pricing-strategy` → `marketing-ideas`

---

## Setting Up API Keys

Skills work without API keys (using web search and free data), but they're more powerful with live API access.

Create a file at `~/.claude/.env.global` or add to your project's `.env`:

```bash
# Most impactful keys to set up first:
RESEND_API_KEY=your_key        # Enables actual email sending
SEMRUSH_API_KEY=your_key       # Rich SEO & keyword data
UNSPLASH_CLIENT_ID=your_key    # Featured images for blog posts
```

See the full list of API keys in the [README](README.md#api-configuration).

**Priority order for API setup:**
1. **Resend** — if you want to send emails directly
2. **SemRush or Ahrefs** — for real keyword and backlink data
3. **Google OAuth** — for Analytics, Search Console, and Ads reporting
4. **Unsplash** — for stock images in blog posts
5. **Everything else** — add as needed for specific skills

---

## Combining Skills

The real power of OpenClaudia is chaining skills together. You can ask Claude to run multiple skills in one conversation:

### Example: Full content pipeline

```
> Research keywords for "AI form builder", write a blog post targeting the best
> keyword, then create a LinkedIn post and Reddit comment promoting it.
```

Claude will automatically use `keyword-research` → `write-blog` → `linkedin-content` → `reddit-marketing` in sequence.

### Example: Competitor teardown

```
> Do a full competitor analysis of competitor.com — SEO audit, content gap
> analysis, and backlink comparison. Then create a content strategy to beat them.
```

Claude chains: `competitor-analysis` → `seo-audit` → `content-gap-analysis` → `backlink-audit` → `content-strategy`

### Example: Launch campaign

```
> We're launching a new feature next week. Create a launch strategy, write the
> announcement blog post, email sequence, social media posts, and Discord
> announcement.
```

Claude uses: `launch-strategy` → `write-blog` → `email-sequence` → `social-content` → `discord-bot`

---

## Project-Level vs Global Skills

### Global skills (`~/.claude/skills/`)

Available in every Claude Code session, across all projects. This is where `npx openclaudia install` puts skills by default.

Best for: general marketing skills you use everywhere.

### Project-level skills (`.claude/skills/`)

Available only in that project's Claude Code sessions. Use this when you want to customize a skill for a specific project.

```bash
# Copy and customize a skill for your project
cp -r ~/.claude/skills/write-blog .claude/skills/write-blog

# Edit the SKILL.md to add project-specific instructions
# e.g., "Always mention our product name as 'FormAI'"
```

Project-level skills override global skills with the same name.

---

## Tips & Best Practices

### 1. Be specific with your prompts

```
# Vague — skill has to guess
> /write-blog "AI tools"

# Specific — better output
> /write-blog "10 AI Form Builders Compared: Features, Pricing, and Which One
> to Choose in 2026" --target-keyword "best AI form builder" --word-count 2500
```

### 2. Provide context in your project

If your project has a `CLAUDE.md` file with brand guidelines, tone of voice, or product details, skills will automatically use that context.

### 3. Review and iterate

Skills generate a first draft. Ask Claude to refine:

```
> /write-blog "Topic here"
> Make the introduction more compelling and add a comparison table
> Add internal links to our /pricing and /features pages
```

### 4. Use natural language, not just slash commands

You don't have to use slash commands. Claude recognizes when a skill is relevant:

```
> Write a blog post about AI form builders
# Claude automatically uses the write-blog skill

> Audit the SEO on my site
# Claude automatically uses seo-audit
```

### 5. Chain skills for comprehensive campaigns

Instead of running skills one at a time, describe your goal and let Claude orchestrate:

```
> I need a complete content marketing campaign for our product launch next month.
> Start with competitor analysis, then create a content calendar, write the key
> pieces, and set up the email drip campaign.
```

---

## Troubleshooting

### Skills don't appear as slash commands

```bash
# Reinstall
npx openclaudia install --all

# Check they're in the right place
ls ~/.claude/skills/
```

### API calls fail

```
# Check your env file
cat ~/.claude/.env.global

# Make sure the key is set (not empty)
echo $RESEND_API_KEY
```

### Skill output isn't what you expected

- Add more context to your prompt
- Check if the skill needs an API key for richer data
- Open an [issue](https://github.com/OpenClaudia/openclaudia-skills/issues) if the skill's instructions need improvement

### Skills conflict with project-level instructions

Project-level `.claude/skills/` takes priority over global `~/.claude/skills/`. If a skill behaves differently in one project, check for a project-level override.

---

## What's Next?

- Browse the [full skill list](README.md#skills) to see everything available
- [Contribute a skill](CONTRIBUTING.md) if you have a marketing workflow that's missing
- Star the repo on [GitHub](https://github.com/OpenClaudia/openclaudia-skills) to stay updated
- Visit [openclaudia.com](https://openclaudia.com) for tutorials and news

---

<p align="center">
  <sub>Questions? <a href="https://github.com/OpenClaudia/openclaudia-skills/issues">Open an issue</a> or reach out at <a href="https://x.com/Claudia1569302">@Claudia1569302</a></sub>
</p>
