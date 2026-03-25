---
name: brand-research
description: >
  Fetch brand info (name, description, logos, colors, industry) from the brand.dev API.
  Use when asked to look up a brand, fetch a company logo, get brand details, research
  a company's visual identity, or find brand assets for a project.
---

# Brand Research

Look up brand information using the [brand.dev](https://brand.dev) API and save logos locally.

## Prerequisites

- **brand.dev API key** in `BRANDDEV_API_KEY` environment variable (sign up at brand.dev)

## Step 1: Get the Domain

Extract the target domain from the user's input. Strip protocol and trailing slashes (e.g., `https://example.com/` -> `example.com`).

## Step 2: Fetch Brand Info

```bash
curl -s "https://api.brand.dev/v1/brand/retrieve?domain=${DOMAIN}" \
  -H "Authorization: Bearer ${BRANDDEV_API_KEY}" \
  -H "Content-Type: application/json"
```

Extract from the response:
- **Brand name** (`.brand.title` or `.brand.name`)
- **Description** (`.brand.description`)
- **Logo URLs** (from `.brand.logos[]`) — prefer icon/square logos for card layouts, full logos for headers
- **Industry/category** if available

## Step 3: Download Logos Locally

Always download logos locally for serving. External `media.brand.dev` URLs can change or go down.

### Where to save

Match the project's existing asset conventions:
- **Next.js / static sites**: `public/logos/<context>/` (served as `/logos/<context>/`)
- **Other web projects**: check for existing `static/`, `assets/`, `images/`, or `public/` directories
- **If no convention exists**: create a `logos/` directory under the project's static asset root

### Naming Convention
- `<brand-slug>.<ext>` — lowercase brand name, spaces replaced by hyphens
- Optionally group by context subdirectory (e.g., `partners/`, `customers/`)

### Download Command
```bash
mkdir -p <logo-dir>
curl -sL "<logo-url>" -o "<logo-dir>/<brand-slug>.<ext>"
```

## Step 4: Return Results

Provide the user with:
- Brand name
- Description
- Industry
- **Local logo path** — the path to use in code
- Original source URL (for reference only)

## Important Rules

1. **Always save images locally** — never use `media.brand.dev` URLs directly in production code.
2. **Use local paths in code** — reference relative to the project's static asset serving root.
3. **Prefer square/icon logos** for card layouts (they fit better in grid cards).
4. **Prefer full/horizontal logos** for headers and hero sections.
5. If the brand has no logos in the API response, note this and suggest using a fallback icon.
