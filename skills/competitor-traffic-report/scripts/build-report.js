#!/usr/bin/env node
// Turn fetch-traffic.js output into one self-contained HTML report.
//   node build-report.js data.json "Report title" [--out report.html]
// Logos are downloaded and inlined as data: URIs — the page must work with no
// network at all (a published artifact's CSP blocks every external host).
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process')

const [dataPath, title] = process.argv.slice(2).filter(a => !a.startsWith('--'))
if (!dataPath) { console.error('usage: build-report.js <data.json> ["title"] [--out report.html]'); process.exit(1) }
const oi = process.argv.indexOf('--out')
const OUT = oi >= 0 ? process.argv[oi + 1] : 'report.html'

const D = JSON.parse(fs.readFileSync(dataPath, 'utf8'))
const TITLE = title || `${D.focus} vs competitors — traffic and authority`

// ponytail: shells out to curl + magick rather than pulling image libs. Both are
// already required elsewhere in this workflow; a missing logo just degrades to a swatch.
const logos = {}
for (const [d, url] of Object.entries(D.logo_urls || {})) {
  const tmp = path.join('/tmp', `lg_${d}`)
  try {
    execFileSync('curl', ['-sL', '--noproxy', '*', '--max-time', '30', '-o', tmp + '.src',
      '-H', 'User-Agent: Mozilla/5.0', url])
    execFileSync('magick', ['-background', 'none', tmp + '.src[0]', '-resize', '48x48',
      '-gravity', 'center', '-extent', '48x48', '-strip', tmp + '.png'])
    logos[d] = 'data:image/png;base64,' + fs.readFileSync(tmp + '.png').toString('base64')
  } catch { /* no logo for this one */ }
}

const tpl = fs.readFileSync(path.join(__dirname, '..', 'templates', 'report.html'), 'utf8')
const blob = `const DATA=${JSON.stringify(D)};const LOGOS=${JSON.stringify(logos)};`
fs.writeFileSync(OUT, tpl.replace(/__TITLE__/g, TITLE).replace('__DATA__', blob))
console.log(`${OUT} — ${Object.keys(D.sw).length} products, ${Object.keys(logos).length} logos, ${Math.round(fs.statSync(OUT).size / 1024)} KB`)
