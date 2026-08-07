# OpenClaudia

Open-source AI marketing skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/introducing-codex/), and other coding agents. 74 skills that turn your terminal into a full-service marketing team.

**Website:** [openclaudia.com](https://openclaudia.com)
**GitHub:** [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills)

## Install

```bash
# Install all 74 skills
npx openclaudia install --all

# Install a specific skill
npx openclaudia install seo-audit

# Install multiple skills
npx openclaudia install write-blog keyword-research email-sequence
```

## Usage

After installing, open Claude Code and use any skill as a slash command:

```
> /write-blog "10 Tips for SaaS Growth"
> /seo-audit https://mysite.com
> /email-sequence --type welcome
> /competitor-analysis acme.com
> /social-content --platform reddit
```

## Skills

### SEO & Site Audit
| Skill | Description |
|-------|-------------|
| `seo-audit` | Full technical + on-page SEO audit with actionable fixes |
| `keyword-research` | Keyword research via SemRush, DataForSEO, SerpAPI |
| `serp-analyzer` | Analyze SERP results and ranking factors |
| `backlink-audit` | Audit backlink profile via SemRush or Ahrefs |
| `schema-markup` | Generate and validate Schema.org structured data |
| `programmatic-seo` | Create SEO-optimized pages at scale |

### Content Writing
| Skill | Description |
|-------|-------------|
| `write-blog` | SEO-optimized blog posts with Unsplash images |
| `write-landing` | High-converting landing page copy |
| `copywriting` | Marketing copy for any page type |
| `copy-editing` | Line-by-line copy polish and improvement |
| `content-strategy` | Content calendars and topic clusters |

### Email Marketing
| Skill | Description |
|-------|-------------|
| `email-sequence` | Create and send drip campaigns via Resend API |
| `email-subject-lines` | Generate, A/B test, and send subject lines |

### Social Media
| Skill | Description |
|-------|-------------|
| `social-content` | Create and publish posts to Reddit, X, LinkedIn, Instagram, Facebook |
| `thread-writer` | Write and post viral threads on X and Reddit |
| `content-calendar` | Plan and schedule social media content |

### Ads & Conversion
| Skill | Description |
|-------|-------------|
| `google-ads` | Write Google Ads copy and campaigns |
| `facebook-ads` | Create Facebook/Meta ad campaigns |
| `page-cro` | Landing page conversion rate optimization |
| `ab-test-setup` | Design and implement A/B tests |

### Analytics & Research (API-Powered)
| Skill | Description | API |
|-------|-------------|-----|
| `semrush-research` | SEO & competitive intelligence | `SEMRUSH_API_KEY` |
| `brand-monitor` | Brand mention tracking & sentiment | `BRANDDEV_API_KEY` |
| `google-analytics` | GA4 reports and insights | Google OAuth |
| `search-console` | Google Search Console data | Google OAuth |
| `google-ads-report` | Google Ads performance reporting | Google OAuth |

### Strategy & Planning
| Skill | Description |
|-------|-------------|
| `marketing-ideas` | 139 proven marketing ideas by category |
| `marketing-psychology` | 70+ psychological principles for marketing |
| `competitor-analysis` | Full competitor strategy breakdown |
| `pricing-strategy` | Pricing page and strategy optimization |
| `launch-strategy` | Product launch planning and execution |
| `icp-builder` | Define ideal customer profiles |

### Growth & Automation
| Skill | Description |
|-------|-------------|
| `referral-program` | Design referral and viral loops |
| `lead-magnet` | Create lead magnets and gated content |
| `signup-flow-cro` | Optimize signup conversion funnels |
| `onboarding-cro` | Improve user onboarding flows |

## API Configuration

Skills work without API keys but provide richer results when configured. Set keys in `.env` or `~/.claude/.env.global`:

```bash
RESEND_API_KEY=           # Send emails (email-sequence, email-subject-lines)
SEMRUSH_API_KEY=          # SEO data (keyword-research, backlink-audit, competitor-analysis)
AHREFS_API_KEY=           # Backlink data (backlink-audit)
SERPAPI_API_KEY=           # SERP data (serp-analyzer, keyword-research)
BRANDDEV_API_KEY=         # Brand monitoring (brand-monitor)
UNSPLASH_CLIENT_ID=       # Stock images (write-blog, social-content)
GOOGLE_CLIENT_ID=         # Google APIs (analytics, search-console, ads)
GOOGLE_CLIENT_SECRET=     # Google APIs
REDDIT_CLIENT_ID=         # Reddit posting (social-content)
REDDIT_CLIENT_SECRET=     # Reddit posting
SCRAPINGBEE_API_KEY=      # Web scraping (competitor-analysis)
```

## Commands

```bash
npx openclaudia install --all          # Install all skills
npx openclaudia install <name>         # Install specific skill(s)
npx openclaudia list                   # List available skills
npx openclaudia remove <name>          # Remove a skill
npx openclaudia remove --all           # Remove all skills
```

## How It Works

Skills are installed to `~/.claude/skills/` as Markdown files. Each skill registers as a slash command in Claude Code. When invoked, the agent follows the skill's instructions to execute marketing tasks — reading your project files, calling APIs, and writing output directly to disk.

## Contributing

1. Fork [the repository](https://github.com/OpenClaudia/openclaudia-skills)
2. Create a skill directory under `skills/`
3. Add a `SKILL.md` with YAML frontmatter and instructions
4. Submit a pull request

## Related Projects

- [How to Win GEO](https://howtowingeo.com) — Guide to Generative Engine Optimization
- [OpenClaudia Website](https://openclaudia.com) — Official website and documentation

## License

MIT — see [LICENSE](https://github.com/OpenClaudia/openclaudia-skills/blob/main/LICENSE)

## Created by

[Quanlai Li](https://quanl.ai) and the OpenClaudia community.
