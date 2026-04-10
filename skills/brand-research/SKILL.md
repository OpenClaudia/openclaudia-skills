---
name: brand-dev
description: Fetch brand info (name, description, logos, industry) from brand.dev API and save logos locally. Use when the user asks to look up a brand, fetch a logo, get brand info, or add a company with its logo.
user_invocable: true
---

# Brand.dev Skill

Fetch brand data from the brand.dev API and save logos locally for serving.

## Step 1: Get the Domain

Extract the target domain from the user's input. Strip protocol and trailing slashes (e.g., "https://example.com/" -> "example.com").

## Step 2: Fetch Brand Info

```bash
BRANDDEV_API_KEY=$(grep BRANDDEV_API_KEY environment variables | cut -d= -f2)
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

ALWAYS download logos locally for serving. Never reference external `media.brand.dev` URLs in production code — they can change or go down.

### Where to save

The save location depends on the project. Look for existing patterns:
- **Next.js / static sites**: `public/logos/<context>/` (served as `/logos/<context>/`)
- **Other web projects**: check for existing `static/`, `assets/`, `images/`, or `public/` directories
- **If no convention exists**: create a `logos/` directory under the project's static asset root

### Naming Convention
- `<brand-slug>.<ext>` where:
  - `<brand-slug>` is the lowercase brand name, spaces replaced by hyphens (e.g., `miss-a` not `miss_a`)
  - `<ext>` matches the original file extension (png, webp, jpg, svg)
- Optionally group by context subdirectory (e.g., `partners/`, `customers/`) if the project has multiple logo collections

### Download Command
```bash
mkdir -p <logo-dir>
curl -sL "<logo-url>" -o "<logo-dir>/<brand-slug>.<ext>"
```

### Verify Download
```bash
ls -la <logo-dir>/<brand-slug>.<ext>
```

## Step 4: Return Results

Provide the user with:
- Brand name
- Description
- Industry
- **Local logo path** — the path to use in code (relative to the project's static root)
- Original source URL (for reference only)

## Important Rules

1. **Always save images locally** — never use `media.brand.dev` URLs directly in production code.
2. **Use local paths in code** — reference relative to the project's static asset serving root.
3. **Prefer square/icon logos** for card layouts (they fit better in grid cards).
4. **Prefer full/horizontal logos** for headers and hero sections.
5. If the brand has no logos in the API response, note this and suggest using a fallback icon.
