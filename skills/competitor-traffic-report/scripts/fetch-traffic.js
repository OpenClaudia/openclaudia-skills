#!/usr/bin/env node
// Pull traffic + authority metrics for one focus domain and its competitors.
//   node fetch-traffic.js <focus.com> <comp1.com,comp2.com,...> [--out data.json]
//
// Three metrics, three sources, deliberately not interchangeable:
//   total visits   SimilarWeb  all traffic, any channel, 3 months
//   organic        Ahrefs      search-only estimate, ~30 months of history
//   DR             Ahrefs      0-100 backlink authority, a single current value
//
// Needs AHREFS_API_KEY. Logos need BRANDDEV_API_KEY (optional; omit and the report
// falls back to a colour swatch).
const fs = require('fs'), { execFileSync } = require('child_process')

const [focus, listArg] = process.argv.slice(2).filter(a => !a.startsWith('--'))
if (!focus || !listArg) { console.error('usage: fetch-traffic.js <focus.com> <comp1,comp2,...> [--out data.json]'); process.exit(1) }
const oi = process.argv.indexOf('--out')
const OUT = oi >= 0 ? process.argv[oi + 1] : 'data.json'
const DOMAINS = [...new Set([focus, ...listArg.split(',').map(s => s.trim()).filter(Boolean)])]

const AH = process.env.AHREFS_API_KEY
if (!AH) { console.error('AHREFS_API_KEY not set'); process.exit(1) }
const BD = process.env.BRANDDEV_API_KEY
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
const today = new Date().toISOString().slice(0, 10)

// curl, not fetch: a proxy in the environment turns these into 403s and 405s that
// look like auth failures. --noproxy sidesteps it.
const curl = (url, ...h) => execFileSync('curl',
  ['-sL', '--noproxy', '*', '--max-time', '45', ...h.flatMap(x => ['-H', x]), url], { maxBuffer: 1 << 26 })

// --- SimilarWeb: total visits, last 3 months -------------------------------
// The X-Extension-Version header is what gets past CloudFront; a browser User-Agent
// alone 403s. The endpoint also rate-limits BY IP at roughly 15 calls per window, so
// this paces at 15s and still expects misses on a long list — rerun to fill them.
async function similarweb(domain) {
  const h = ['Content-Type: application/json', 'X-Extension-Version: 6.12.21', `User-Agent: ${UA}`]
  const raw = curl(`https://data.similarweb.com/api/v1/data?domain=${encodeURIComponent(domain)}`, ...h)
  const j = JSON.parse(raw)
  const v = j.EstimatedMonthlyVisits || {}
  if (!Object.keys(v).length) throw new Error('no EstimatedMonthlyVisits')
  return Object.fromEntries(Object.entries(v).map(([d, n]) => [d.slice(0, 7), Math.round(n / 10) / 100]))
}

// --- Ahrefs -----------------------------------------------------------------
const ahrefs = (path, qs) => JSON.parse(curl(`https://api.ahrefs.com/v3/${path}?${qs}`, `Authorization: Bearer ${AH}`))

// The free public DR endpoint does not consume API units. Its licence permits
// publishing the value provided the report shows "Domain Rating by Ahrefs" with a
// live link next to it — the template already does.
const domainRating = (d) =>
  ahrefs('public/domain-rating-free', `date=${today}&target=${encodeURIComponent(d)}`).domain_rating.domain_rating

// Organic history. This one DOES spend Ahrefs units, one row per month requested.
function organic(domain, months = 30) {
  const end = new Date(), start = new Date(end.getFullYear(), end.getMonth() - months, 1)
  const j = ahrefs('site-explorer/metrics-history',
    `target=${encodeURIComponent(domain)}&date_from=${start.toISOString().slice(0, 10)}` +
    `&history_grouping=monthly&volume_mode=monthly&mode=subdomains&select=date,org_traffic`)
  // mode=subdomains, not domain: domain-mode silently excludes the www. host, which
  // reads as a near-empty site for anyone whose canonical is www.
  return Object.fromEntries((j.metrics || []).map(m => [m.date.slice(0, 7), Math.round(m.org_traffic / 10) / 100]))
}

// --- logos (optional) -------------------------------------------------------
function logo(domain) {
  if (!BD) return null
  try {
    const j = JSON.parse(curl(`https://api.brand.dev/v1/brand/retrieve?domain=${domain}`, `Authorization: Bearer ${BD}`))
    const ls = (j.brand || {}).logos || []
    const pick = ls.find(l => l.type === 'icon') || ls.find(l => l.type === 'symbol') || ls[0]
    return pick ? pick.url : null
  } catch { return null }
}

;(async () => {
  const out = { focus, generated_at: new Date().toISOString(), sw: {}, ah: {}, dr: {}, logo_urls: {}, misses: [] }
  for (const d of DOMAINS) {
    const row = []
    try { out.sw[d] = await similarweb(d); row.push('visits') }
    catch (e) { out.misses.push(`${d} visits: ${e.message}`) }
    try { out.dr[d] = domainRating(d); row.push('DR') } catch (e) { out.misses.push(`${d} DR: ${e.message}`) }
    try { out.ah[d] = organic(d); row.push('organic') } catch (e) { out.misses.push(`${d} organic: ${e.message}`) }
    const l = logo(d); if (l) out.logo_urls[d] = l
    console.log(`  ${d.padEnd(24)} ${row.join(' ') || 'nothing'}`)
    await sleep(15000)  // SimilarWeb's per-IP window; everything else is far cheaper
  }
  fs.writeFileSync(OUT, JSON.stringify(out))
  console.log(`\n${Object.keys(out.sw).length}/${DOMAINS.length} with visits, ${Object.keys(out.dr).length} with DR -> ${OUT}`)
  if (out.misses.length) console.log('misses:\n  ' + out.misses.join('\n  '))
})()
