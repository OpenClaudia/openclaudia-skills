---
name: i18n
description: >
  Add full internationalization (i18n) to a Next.js project using next-intl.
  Supports 14+ languages, SEO-friendly locale routing, hreflang sitemaps, and bulk
  translation. Use when asked to "internationalize", "add i18n", "add translations",
  "multi-language", "localize", "add language support", or "translate my site".
---

# Internationalize a Next.js Project

Add complete internationalization to a Next.js (App Router) project using **next-intl v4**. Handles routing, translation files, sitemap hreflang, and bulk translation across all locales.

## Step 1: Assess the Project

1. Check Next.js version (`package.json`) — must be 13+ with App Router
2. Check if i18n is already partially set up (look for `next-intl`, `next-i18next`, `[locale]` routes)
3. Identify all pages/routes that need translation
4. Identify all user-facing strings (hardcoded text in components)
5. Ask the user which locales to support (default: en, es, fr, de, pt, ja, ar, zh, zh-tw, id, vi, ms, ru, hi)

## Step 2: Install Dependencies

```bash
npm install next-intl
```

## Step 3: Create i18n Configuration Files

Create 4 files under `src/i18n/`:

### `src/i18n/config.ts`
```typescript
export const locales = ['en', 'es', 'fr', 'de', 'pt', 'ja', 'ar', 'zh', 'zh-tw', 'id', 'vi', 'ms', 'ru', 'hi'] as const

export type Locale = (typeof locales)[number]
export const defaultLocale: Locale = 'en'

export const localeNames: Record<Locale, string> = {
  en: 'English',
  es: 'Espanol',
  fr: 'Francais',
  de: 'Deutsch',
  pt: 'Portugues',
  ja: '日本語',
  ar: 'العربية',
  zh: '简体中文',
  'zh-tw': '繁體中文',
  id: 'Bahasa Indonesia',
  vi: 'Tieng Viet',
  ms: 'Bahasa Melayu',
  ru: 'Русский',
  hi: 'हिन्दी',
}

export const rtlLocales: Locale[] = ['ar']
```

### `src/i18n/routing.ts`
```typescript
import { defineRouting } from 'next-intl/routing'
import { defaultLocale, locales } from './config'

export const routing = defineRouting({
  locales,
  defaultLocale,
  localePrefix: 'as-needed', // English URLs stay clean, other locales get /es/, /fr/, etc.
})
```

### `src/i18n/navigation.ts`
```typescript
import { createNavigation } from 'next-intl/navigation'
import { routing } from './routing'

export const { Link, redirect, usePathname, useRouter } = createNavigation(routing)
```

### `src/i18n/request.ts`
```typescript
import { getRequestConfig } from 'next-intl/server'
import { routing } from './routing'

export default getRequestConfig(async ({ requestLocale }) => {
  let locale = await requestLocale
  if (!locale || !routing.locales.includes(locale as any)) {
    locale = routing.defaultLocale
  }
  return {
    locale,
    messages: (await import(`../messages/${locale}.json`)).default,
  }
})
```

## Step 4: Create Middleware

Create `src/middleware.ts`:
```typescript
import createMiddleware from 'next-intl/middleware'
import { routing } from '@/i18n/routing'

export default createMiddleware({
  ...routing,
  localeDetection: false, // Don't auto-redirect based on Accept-Language
})

export const config = {
  matcher: ['/((?!_next|api|images|fonts|favicon|sitemap|robots).*)'],
}
```

**Key decision**: `localeDetection: false` prevents auto-redirecting users based on browser language. This keeps English URLs stable for SEO.

## Step 5: Update next.config

```typescript
import createNextIntlPlugin from 'next-intl/plugin'
const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts')

export default withNextIntl(nextConfig)
```

## Step 6: Add `[locale]` Dynamic Route

Move all page content under `src/app/[locale]/`:

1. Create `src/app/[locale]/layout.tsx` with:
   - `generateStaticParams()` returning all locales
   - `setRequestLocale(locale)` call
   - `<NextIntlClientProvider>` wrapping children
   - `<html lang={locale} dir={rtlLocales.includes(locale) ? 'rtl' : 'ltr'}>`
   - Hreflang `<link>` tags in `<head>` for all locales + `x-default`

2. Move existing pages into `src/app/[locale]/`
3. Each page should call `setRequestLocale(locale)` for static generation

## Step 7: Extract Strings into Translation Files

1. Create `src/messages/en.json` with all user-facing strings organized by section:
   ```json
   {
     "common": { "signIn": "Sign In" },
     "tools": { "tool-slug": { "title": "...", "description": "..." } },
     "faq": { "tool-slug": [{ "question": "...", "answer": "..." }] }
   }
   ```

2. Replace hardcoded strings with `useTranslations()`:
   ```typescript
   const t = useTranslations('common')
   return <button>{t('signIn')}</button>
   ```

3. For server components, use `getTranslations()`:
   ```typescript
   const t = await getTranslations('common')
   ```

## Step 8: Translate to All Locales

For each non-English locale, create `src/messages/{locale}.json` with the same structure as `en.json`.

### Translation Tips

- Translate naturally, not literally
- Keep technical terms in English (PowerPoint, PDF, API, etc.)
- Preserve JSON structure exactly (same keys, same nesting)
- Preserve interpolation variables like `{count}`, `{name}` unchanged

### Verification Script

After translation, verify quality:

```python
import json

locales = ['es', 'fr', 'de', 'pt', 'ja', 'ar', 'zh', 'zh-tw', 'id', 'vi', 'ms', 'ru', 'hi']
english_words = ['the ', 'and ', 'you ', 'your ', 'our ', 'this ', 'that ', 'with ', 'from ', 'will ']

with open('src/messages/en.json') as f:
    en = json.load(f)

for loc in locales:
    with open(f'src/messages/{loc}.json') as f:
        data = json.load(f)

    missing = [s for s in en if s not in data]

    eng_count = 0
    def check(d):
        nonlocal eng_count
        if isinstance(d, dict):
            for v in d.values(): check(v)
        elif isinstance(d, str):
            if sum(1 for w in english_words if w in d.lower()) >= 3:
                eng_count += 1
    check(data)

    status = 'OK' if not missing and eng_count == 0 else 'ISSUES'
    print(f'{loc}: {status} (missing={len(missing)}, english={eng_count})')
```

## Step 9: Update Sitemap with Hreflang

Update `src/app/sitemap.ts`:

```typescript
import { MetadataRoute } from 'next'
import { locales } from '@/i18n/config'

const baseUrl = 'https://www.example.com'

function buildAlternates(path: string): Record<string, string> {
  const alternates: Record<string, string> = {}
  for (const locale of locales) {
    const prefix = locale === 'en' ? '' : `/${locale}`
    alternates[locale] = `${baseUrl}${prefix}${path}`
  }
  return alternates
}

export default function sitemap(): MetadataRoute.Sitemap {
  return pages.map((path) => ({
    url: `${baseUrl}${path}`,
    lastModified: new Date(),
    alternates: { languages: buildAlternates(path) },
  }))
}
```

Generate one canonical URL per page with hreflang alternates, NOT one URL per locale.

## Step 10: Add Language Selector (Optional)

Add a language switcher using `useRouter` and `usePathname` from `@/i18n/navigation` to switch locales while preserving the current path.

## Step 11: Verify

1. `npm run build` — check all static pages generate correctly
2. English URLs have no prefix: `/tools`
3. Locale URLs have prefix: `/es/tools`
4. Sitemap has hreflang alternates
5. RTL rendering works for Arabic
6. Run the translation verification script

## Common Pitfalls

- **`public/sitemap.xml`** conflicts with dynamic `src/app/sitemap.ts` in dev — delete the static one
- **Middleware matcher** must exclude `_next`, `api`, `sitemap`, `robots`, and static assets
- **`localePrefix: 'as-needed'`** is critical — keeps default locale URLs clean for SEO continuity
- **`localeDetection: false`** prevents unwanted redirects that break SEO
- **Large translation files** (5000+ lines) can make git pushes fail — use `git config http.postBuffer 524288000`
- **Verify translations** — automated translation often produces mixed-language output
