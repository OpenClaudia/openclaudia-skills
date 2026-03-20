<p align="center">
  <img src="https://openclaudia.com/avatar.png" width="120" alt="OpenClaudia" />
</p>

<h1 align="center">OpenClaudia</h1>

<p align="center">
  <strong>The open-source marketing toolkit for AI coding agents.</strong><br/>
  56+ modular skills that turn Claude Code into a full marketing department.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/openclaudia"><img src="https://img.shields.io/npm/v/openclaudia?color=blue&label=npm" alt="npm version" /></a>
  <a href="https://github.com/OpenClaudia/openclaudia-skills/stargazers"><img src="https://img.shields.io/github/stars/OpenClaudia/openclaudia-skills?style=social" alt="GitHub Stars" /></a>
  <a href="https://github.com/OpenClaudia/openclaudia-skills/blob/main/LICENSE"><img src="https://img.shields.io/github/license/OpenClaudia/openclaudia-skills" alt="License: MIT" /></a>
  <a href="https://openclaudia.com"><img src="https://img.shields.io/badge/website-openclaudia.com-purple" alt="Website" /></a>
</p>

<p align="center">
  <a href="https://openclaudia.com">Website</a> · <a href="#quick-start">Quick Start</a> · <a href="#skills">Skills</a> · <a href="https://github.com/OpenClaudia/openclaudia-skills/issues">Issues</a> · <a href="CONTRIBUTING.md">Contributing</a>
</p>

---

## Why OpenClaudia?

Most AI marketing tools charge **$50–300/month** for a chat box that gives you suggestions. OpenClaudia is different:

| | SaaS Marketing Tools | OpenClaudia |
|---|---|---|
| **Price** | $50–300/month | Free & open source |
| **Execution** | Suggests copy, you do the rest | Actually writes, publishes, sends |
| **Data privacy** | Your data on their servers | Runs locally on your machine |
| **Customization** | Limited to their UI | Fork, modify, extend any skill |
| **Integration** | Walled garden | Works with 20+ APIs you already use |
| **Setup** | Sign up, onboard, learn their UI | One command: `npx openclaudia install --all` |

## Quick Start

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated.

```bash
# Install all 56+ marketing skills
npx openclaudia install --all

# Or install specific skills
npx openclaudia install seo-audit write-blog email-sequence
```

Then open Claude Code and start marketing:

```
$ claude

> /audit-seo https://mysite.com
✓ Analyzing 47 pages... SEO score: 72/100 — 12 issues found

> /write-blog "10 Tips for SaaS Growth"
✓ 2,400-word article generated with meta tags

> /email-sequence --type product-launch
✓ 6-email drip sequence created and sent via Resend

> /competitor-analysis competitor.com
✓ Full SEO, content, and positioning breakdown

> /discord-bot "New feature just dropped!"
✓ Rich embed posted to #announcements
```

### Alternative installation

```bash
# Via the skills CLI
npx skills add OpenClaudia/openclaudia-skills

# Install a single skill
npx skills add OpenClaudia/openclaudia-skills --skill seo-audit

# Manual: copy any skill directory into your skills folder
cp -r skills/seo-audit ~/.claude/skills/      # personal
cp -r skills/seo-audit .claude/skills/         # project-level
```

## Skills

### SEO & Site Audit
| Skill | Description |
|-------|-------------|
| `seo-audit` | Full technical + on-page SEO audit with actionable fixes |
| `keyword-research` | Keyword research using SemRush API |
| `serp-analyzer` | Analyze SERP results and ranking factors |
| `backlink-audit` | Audit backlink profile and find opportunities |
| `schema-markup` | Generate and validate Schema.org structured data |
| `programmatic-seo` | Create SEO-optimized pages at scale |

### Content Writing
| Skill | Description |
|-------|-------------|
| `write-blog` | Generate SEO-optimized blog posts |
| `write-landing` | Create high-converting landing page copy |
| `copywriting` | Marketing copy for any page type |
| `copy-editing` | Line-by-line copy polish and improvement |
| `content-strategy` | Build content calendars and topic clusters |
| `seo-content-brief` | Create structured SEO content briefs for writers |
| `content-gap-analysis` | Identify content gaps vs. competitors |
| `content-repurposing` | Atomize content across platforms and formats |

### Email Marketing
| Skill | Description |
|-------|-------------|
| `email-sequence` | Create and send drip campaigns via Resend API |
| `email-subject-lines` | Generate, A/B test, and send email subject lines |

### Social Media
| Skill | Description |
|-------|-------------|
| `social-content` | Create and publish posts to Reddit, X, LinkedIn, Instagram, Facebook |
| `thread-writer` | Write and post viral threads on X and Reddit |
| `content-calendar` | Plan and schedule social media content |
| `linkedin-content` | LinkedIn-optimized posts, carousels, and strategy |
| `bluesky` | Bluesky content creation and AT Protocol integration |
| `reddit-marketing` | Authentic Reddit marketing and community engagement |

### Ads & Conversion
| Skill | Description |
|-------|-------------|
| `google-ads` | Write Google Ads copy and campaigns |
| `facebook-ads` | Create Facebook/Meta ad campaigns |
| `linkedin-ads` | Create LinkedIn ad campaigns and B2B advertising |
| `page-cro` | Landing page conversion rate optimization |
| `ab-test-setup` | Design and implement A/B tests |
| `video-ad-analysis` | Deconstruct and analyze video ad creatives |

### Analytics & Research (API-Powered)
| Skill | Description | API Required |
|-------|-------------|--------------|
| `semrush-research` | SEO & competitive intelligence via SemRush | `SEMRUSH_API_KEY` |
| `brand-monitor` | Brand monitoring via Brand.dev | `BRANDDEV_API_KEY` |
| `google-analytics` | Pull GA4 reports and insights | Google OAuth |
| `search-console` | Google Search Console data & analysis | Google OAuth |
| `google-ads-report` | Google Ads performance reporting | Google OAuth |
| `youtube-analytics` | YouTube channel and video performance analysis | `YOUTUBE_API_KEY` |

### Strategy & Planning
| Skill | Description |
|-------|-------------|
| `marketing-ideas` | 139 proven marketing ideas by category |
| `marketing-psychology` | 70+ psychological principles for marketing |
| `competitor-analysis` | Full competitor strategy breakdown |
| `pricing-strategy` | Pricing page and strategy optimization |
| `launch-strategy` | Product launch planning and execution |
| `icp-builder` | Define ideal customer profiles |
| `growth-strategy` | AARRR framework, growth loops, and experimentation |
| `product-marketing` | Positioning, messaging, battlecards, and GTM |
| `demand-gen` | Multi-channel demand generation and lead scoring |

### Messaging & Notifications
| Skill | Description | API Required |
|-------|-------------|--------------|
| `discord-bot` | Send messages, embeds, and marketing content to Discord | `DISCORD_WEBHOOK_URL` or `DISCORD_BOT_TOKEN` |
| `slack-bot` | Post rich Block Kit messages and updates to Slack | `SLACK_WEBHOOK_URL` or `SLACK_BOT_TOKEN` |
| `telegram-bot` | Send formatted posts, polls, and media to Telegram | `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` |
| `feishu-lark` | Post interactive cards and updates to Feishu/Lark | `FEISHU_WEBHOOK_URL` or `FEISHU_APP_ID` |

### Growth & Automation
| Skill | Description |
|-------|-------------|
| `referral-program` | Design referral and viral loops |
| `lead-magnet` | Create lead magnets and gated content |
| `signup-flow-cro` | Optimize signup conversion funnels |
| `onboarding-cro` | Improve user onboarding flows |
| `affiliate-marketing` | Build and manage affiliate partner programs |
| `newsletter` | Newsletter growth, engagement, and monetization |
| `podcast-marketing` | Podcast production, growth, and promotion |

### CRM & Outreach (API-Powered)
| Skill | Description | API Required |
|-------|-------------|--------------|
| `hubspot` | HubSpot CRM contacts, deals, companies, and CMS | `HUBSPOT_ACCESS_TOKEN` |
| `apollo-outreach` | B2B lead research and enrichment via Apollo.io | `APOLLO_API_KEY` |
| `domain-research` | Domain WHOIS lookup and marketplace listings | None (free API) |

## API Configuration

Some skills integrate with external APIs for live data. Set these in your `.env` or `~/.claude/.env.global`:

```bash
# Email (email-sequence, email-subject-lines)
RESEND_API_KEY=your_key_here

# SemRush (keyword-research, semrush-research, backlink-audit, competitor-analysis)
SEMRUSH_API_KEY=your_key_here

# Ahrefs (backlink-audit — alternative to SemRush)
AHREFS_API_KEY=your_key_here

# SerpAPI (serp-analyzer, keyword-research, competitor-analysis)
SERPAPI_API_KEY=your_key_here

# DataForSEO (serp-analyzer, keyword-research)
DATAFORSEO_LOGIN=your_login
DATAFORSEO_PASSWORD=your_password

# Brand.dev (brand-monitor)
BRANDDEV_API_KEY=your_key_here

# Google OAuth (google-analytics, search-console, google-ads-report)
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret

# Unsplash (write-blog, social-content — featured images)
UNSPLASH_CLIENT_ID=your_access_key

# Reddit (social-content — trending topics)
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret

# ScrapingBee (competitor-analysis — scraping protected pages)
SCRAPINGBEE_API_KEY=your_key_here

# YouTube Data API (youtube-analytics)
YOUTUBE_API_KEY=your_key_here

# HubSpot (hubspot)
HUBSPOT_ACCESS_TOKEN=your_private_app_token

# Apollo.io (apollo-outreach)
APOLLO_API_KEY=your_key_here

# Bluesky (bluesky)
BLUESKY_HANDLE=your.handle
BLUESKY_APP_PASSWORD=your_app_password

# Discord (discord-bot)
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
DISCORD_BOT_TOKEN=your_bot_token

# Slack (slack-bot)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
SLACK_BOT_TOKEN=xoxb-your-bot-token

# Telegram (telegram-bot)
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Feishu / Lark (feishu-lark)
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...
FEISHU_WEBHOOK_SECRET=your_secret
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
```

All API keys are optional — skills work without them but provide richer data when configured. Each skill tells you which key is needed when invoked.

## Works With Any AI Coding Agent

OpenClaudia skills are designed for **Claude Code** but also work with:

- **OpenAI Codex** — drop skills into your agent's tools directory
- **Cursor / Windsurf** — use as custom instructions or rules
- **Any agent** that supports markdown instruction files

## Contributing

We welcome contributions! Whether it's a new marketing skill, a bug fix, or documentation improvement.

1. Fork this repository
2. Create a new skill directory under `skills/`
3. Add a `SKILL.md` with YAML frontmatter and instructions
4. Submit a pull request

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full guide, including skill authoring conventions and code review standards.

### Good first issues

Look for issues tagged [`help wanted`](https://github.com/OpenClaudia/openclaudia-skills/labels/help%20wanted) — these are curated for new contributors.

## Ecosystem

OpenClaudia is part of a growing ecosystem of AI agent tools:

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — the AI coding agent by Anthropic
- [GEO Guide](https://howtowingeo.com) — how to win at Generative Engine Optimization
- [PageGun](https://pagegun.com) — AI-powered CMS for content publishing

## Sponsors

OpenClaudia is proudly sponsored by:

- [ChatSlide.ai](https://chatslide.ai) — AI-powered presentation maker
- [Enception.ai](https://enception.ai) — AI marketing agency
- [SaySo.ai](https://sayso.ai) — AI voice agents
- [MakeForm.ai](https://makeform.ai) — AI form builder

## License

MIT — see [LICENSE](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=OpenClaudia/openclaudia-skills&type=Date)](https://star-history.com/#OpenClaudia/openclaudia-skills&Date)

---

<p align="center">
  Created by <a href="https://quanl.ai">Quanlai Li</a> and the OpenClaudia community.<br/>
  <sub>Not affiliated with Anthropic.</sub>
</p>
