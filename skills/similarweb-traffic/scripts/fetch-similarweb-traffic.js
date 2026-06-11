#!/usr/bin/env node
// Fetch traffic overview for a domain from SimilarWeb's public data endpoint.
// No dependencies, no API key. Same endpoint PageGun's fetchSimilarwebTraffic() uses.
//
// Usage:
//   node fetch-similarweb-traffic.js <domain> [--json]
//   node fetch-similarweb-traffic.js chatslide.ai
//   node fetch-similarweb-traffic.js chatslide.ai --json   # raw normalized JSON only

const DATA_URL = 'https://data.similarweb.com/api/v1/data'
const USER_AGENT =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

function normalizeDomain(domain) {
  return String(domain || '')
    .trim()
    .replace(/^https?:\/\//i, '')
    .replace(/^www\./i, '')
    .replace(/\/.*$/, '')
    .toLowerCase()
}

function num(v) {
  if (v === null || v === undefined || v === '') return null
  const n = Number(v)
  return Number.isFinite(n) ? n : null
}

function fmt(n) {
  return n === null ? 'n/a' : n.toLocaleString('en-US')
}

function pct(v) {
  const n = num(v)
  return n === null ? 'n/a' : `${(n * 100).toFixed(1)}%`
}

async function main() {
  const args = process.argv.slice(2)
  const jsonOnly = args.includes('--json')
  const domain = normalizeDomain(args.find((a) => !a.startsWith('--')))

  if (!domain) {
    console.error('Usage: node fetch-similarweb-traffic.js <domain> [--json]')
    process.exit(1)
  }

  const url = new URL(DATA_URL)
  url.searchParams.set('domain', domain)

  let res
  try {
    res = await fetch(url, {
      headers: {
        accept: 'application/json,text/plain,*/*',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': USER_AGENT,
      },
    })
  } catch (err) {
    console.error(`Network error fetching ${domain}: ${err.message}`)
    process.exit(2)
  }

  if (!res.ok) {
    console.error(`SimilarWeb request failed for ${domain}: HTTP ${res.status}`)
    if (res.status === 404) console.error('(404 usually means SimilarWeb has no data for this domain.)')
    process.exit(3)
  }

  const d = await res.json()
  const e = d.Engagments || {}
  const ts = d.TrafficSources || {}

  const overview = {
    domain,
    siteName: d.SiteName ?? null,
    title: d.Title ?? null,
    description: d.Description ?? null,
    globalRank: num(d.GlobalRank && d.GlobalRank.Rank),
    categoryRank: num(d.CategoryRank && d.CategoryRank.Rank),
    category: (d.CategoryRank && d.CategoryRank.Category) ?? null,
    snapshotMonth:
      e.Year && e.Month ? `${e.Year}-${String(e.Month).padStart(2, '0')}` : null,
    visits: num(e.Visits),
    bounceRate: num(e.BounceRate),
    pagesPerVisit: num(e.PagePerVisit),
    timeOnSite: num(e.TimeOnSite),
    estimatedMonthlyVisits: Object.entries(d.EstimatedMonthlyVisits || {})
      .map(([date, v]) => ({ date, visits: num(v) }))
      .sort((a, b) => a.date.localeCompare(b.date)),
    trafficSources: {
      searchOrganic: num(ts.SearchOrganic),
      searchPaid: num(ts.SearchPaid),
      direct: num(ts.Direct),
      referrals: num(ts.Referrals),
      socialOrganic: num(ts.SocialOrganic),
      socialPaid: num(ts.SocialPaid),
      mail: num(ts.Mail),
      displayAds: num(ts['Display Ads'] ?? ts.DisplayAds),
      genAi: num(ts.GenAi),
      affiliate: num(ts.Affiliate),
    },
    topCountries: (d.TopCountryShares || []).map((c) => ({
      countryCode: c.CountryCode ?? null,
      value: num(c.Value),
    })),
    topKeywords: (d.TopKeywords || []).map((k) => k.Name).filter(Boolean),
  }

  if (jsonOnly) {
    console.log(JSON.stringify(overview, null, 2))
    return
  }

  const lines = []
  lines.push(`# SimilarWeb traffic — ${domain}`)
  if (overview.snapshotMonth) lines.push(`Snapshot month: ${overview.snapshotMonth}`)
  lines.push('')
  lines.push('| Metric | Value |')
  lines.push('|---|---|')
  lines.push(`| Monthly visits | ${fmt(overview.visits)} |`)
  lines.push(`| Global rank | ${overview.globalRank ? '#' + fmt(overview.globalRank) : 'n/a'} |`)
  lines.push(`| Category rank | ${overview.categoryRank ? '#' + fmt(overview.categoryRank) : 'n/a'} |`)
  lines.push(`| Category | ${overview.category ?? 'n/a'} |`)
  lines.push(`| Bounce rate | ${pct(overview.bounceRate)} |`)
  lines.push(`| Pages / visit | ${overview.pagesPerVisit === null ? 'n/a' : overview.pagesPerVisit.toFixed(2)} |`)
  lines.push(`| Avg. time on site | ${overview.timeOnSite === null ? 'n/a' : Math.round(overview.timeOnSite) + 's'} |`)

  if (overview.estimatedMonthlyVisits.length) {
    lines.push('')
    lines.push('**Monthly visits trend:**')
    lines.push(
      overview.estimatedMonthlyVisits
        .map((p) => `${p.date.slice(0, 7)}: ${fmt(p.visits)}`)
        .join('  →  '),
    )
  }

  const srcEntries = Object.entries(overview.trafficSources)
    .filter(([, v]) => v !== null && v > 0)
    .sort((a, b) => b[1] - a[1])
  if (srcEntries.length) {
    lines.push('')
    lines.push('**Traffic sources:**')
    for (const [k, v] of srcEntries) lines.push(`- ${k}: ${pct(v)}`)
  }

  if (overview.topCountries.length) {
    lines.push('')
    lines.push('**Top countries:** ' + overview.topCountries
      .map((c) => `${c.countryCode} ${pct(c.value)}`)
      .join(', '))
  }

  if (overview.topKeywords.length) {
    lines.push('')
    lines.push('**Top keywords:** ' + overview.topKeywords.slice(0, 8).join(', '))
  }

  console.log(lines.join('\n'))
}

main().catch((err) => {
  console.error(err.message)
  process.exit(1)
})
