# Contributing to OpenClaudia

Thanks for your interest in contributing! OpenClaudia is an open-source marketing toolkit for AI coding agents, and we welcome contributions of all kinds.

## Ways to Contribute

- **New skills** — add a marketing skill that solves a real problem
- **Bug fixes** — fix issues in existing skills
- **Documentation** — improve README, skill descriptions, or examples
- **API integrations** — connect skills to new marketing APIs
- **Translations** — help make skills work in more languages

Contributions of all of the above are free to submit and free to merge. The one
case with its own rules is a vendor adding its own product — see below.

## Vendor Integrations (adding your own product)

If you work on the product being added, say so in the PR. We welcome these, and
the terms depend on one thing: whether an agent can run the documented calls
without paying.

- **Free to use** — no paid plan, credits, or card needed for the calls the PR
  documents. Merged free, same review as any other contribution.
- **Paid product** — any paid tier, credit pack, or subscription is needed to
  actually use it. The listing is sponsored. Open the PR as usual, note it in the
  description, and we will reply with sponsorship terms before merging.

This applies to a vendor documenting its own product, not to skills that happen
to call a paid API. Anyone may add an integration for a product they do not work
on, free, at any time.

Every vendor integration, free or sponsored, still has to pass:

- **Opt-in** — gated behind its own environment variable, with the skill fully
  working when the variable is unset.
- **Self-contained instructions** — the agent's instructions live in this repo.
  Link vendor docs for humans to read; never tell the agent to fetch its
  instructions from a URL the vendor can change.
- **Verified claims** — every endpoint, field, and error code in the PR has to
  match the live API.
- **Attribution** — signup links carry OpenClaudia's referral code where the
  vendor runs a referral program.

## Creating a New Skill

### 1. Pick a skill idea

Check [open issues](https://github.com/OpenClaudia/openclaudia-skills/issues) for requested skills, or propose your own. If you're unsure whether your idea fits, open an issue to discuss first.

### 2. Create the skill directory

```
skills/
  your-skill-name/
    SKILL.md          # Required — the skill definition
```

Skill names should be lowercase, hyphenated, and descriptive: `seo-audit`, `write-blog`, `email-sequence`.

### 3. Write the SKILL.md

Every skill is a single `SKILL.md` file with YAML frontmatter and detailed instructions:

```markdown
---
name: your-skill-name
description: One-line description of what this skill does (shown in skill list)
allowed-tools: Bash
---

# Your Skill Name

Detailed instructions that the AI agent will follow when this skill is invoked.

## When to use this skill

Describe the trigger phrases and use cases.

## What this skill does

Step-by-step instructions for the agent:
1. Gather input from the user
2. Call APIs or read files
3. Generate output
4. Write results to disk or take action

## API Requirements (if any)

List any API keys needed and how to configure them.
```

### Frontmatter fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Skill name (lowercase, hyphenated). Becomes the slash command: `/your-skill-name` |
| `description` | Yes | One-line description shown in `npx openclaudia list` |
| `allowed-tools` | No | Comma-separated list of tools the skill needs access to (e.g., `Bash`, `Read`, `Write`). Use this when your skill needs to run shell commands (curl, API calls) or perform file operations. If omitted, the skill can only generate text responses. |

**When to use `allowed-tools`:**
- `Bash` — skill makes API calls via curl, runs CLI tools, or executes shell commands
- `Read` — skill needs to read files from the user's project
- `Write` — skill creates or modifies files

Example: a skill that sends emails via the Resend API needs `allowed-tools: Bash` to execute curl commands.

### 4. Skill authoring guidelines

- **Be specific** — the more precise your instructions, the better the agent performs
- **Include examples** — show the agent what good output looks like
- **Handle errors** — tell the agent what to do when an API key is missing or a request fails
- **Keep it focused** — one skill should do one thing well
- **Test it** — run your skill in Claude Code before submitting

### 5. Submit a pull request

1. Fork the repo
2. Create a branch: `git checkout -b skill/your-skill-name`
3. Add your skill directory under `skills/`
4. Update the README if your skill adds a new category
5. Open a PR with:
   - What the skill does
   - How you tested it
   - Any API keys required

## Code Review Standards

We review PRs for:

- **Correctness** — does the skill do what it claims?
- **Clarity** — are the instructions clear and unambiguous?
- **Safety** — does the skill avoid destructive actions without user confirmation?
- **Privacy** — does the skill avoid sending user data to unexpected third parties?

## Reporting Issues

Found a bug or have a feature request? [Open an issue](https://github.com/OpenClaudia/openclaudia-skills/issues/new) with:

- Skill name (if applicable)
- What you expected to happen
- What actually happened
- Your environment (OS, Claude Code version)

## Community

- **GitHub Issues** — bug reports and feature requests
- **GitHub Discussions** — questions and ideas
- **Twitter/X** — [@Claudia1569302](https://x.com/Claudia1569302)

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
