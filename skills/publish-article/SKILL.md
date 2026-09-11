---
name: publish-article
description: Publish an article to a site you own — with a searched-for title, a real author, a licensed cover image, linked sources, and (optionally) one planned backlink. Use when the user says "publish an article", "put this on our blog", "publish this draft", "add a backlink", or hands over finished copy to ship. Covers the pre-publish gates that decide whether a published page earns anything.
allowed-tools: Bash, Read, Write, Edit, WebFetch, WebSearch
---

# Publish Article

Writing the article is the easy half. This skill covers the half that decides whether the
published page earns traffic, citations, or link value: what it is titled for, who it is
attributed to, what image it carries, what it links out to, and whether the thing you intended
actually rendered.

Every rule below has a check you can run before publishing. A rule without a check gets skipped,
so run the checks.

## Modes

- **Content mode (default)** — publish an original article. No backlink involved.
- **Backlink mode** — the same, plus one planned keyword link to a target page.
- **Supplied-copy mode** — the user hands you finished text to publish. See "Supplied copy is
  immutable" below; it overrides the writing guidance, never the verification.

## Gate 1 — measure the title keyword BEFORE writing

This is the decision that most determines whether the page is worth publishing, and it is the one
usually made by instinct while drafting. Print this table before the first word:

| Candidate head phrase | Monthly volume | Difficulty | In the target topic's family? |
|---|---:|---:|---|

**Volume is measured, never assumed.** A phrase invented from the article's own finding ("the
1.3% narration gap", "the delivery problem") has zero volume by construction — nobody searches a
coinage they have never read. Clever titles are the default failure mode here, not an occasional
slip.

**The winning phrase must belong to the topic family you are actually competing in.** This is the
subtler failure and it survives the volume check cleanly. Linking to a slide-deck product,
`ai training video generator` (250/mo) beats `ai training slides` (0/mo) on volume and is still
the wrong answer: it ranks the article for a video need while the target sells slides, weakening
the topical signal at exactly the moment the choice looks optimised. Take the best-supported
phrase from the right family over a bigger number in a neighbouring one.

**Keyword tools badly understate AI and long-tail volume — do not read a 0 as "no demand".** A
tool can report 0 for a phrase your own Search Console shows taking clicks at position 1. Where
search-console data and a keyword tool disagree, the console wins; the tool is only there to rank
candidates against each other.

Fixing this after publishing is cheap on any CMS that keeps a redirect from the old slug — do it
rather than living with it. The window closes once the URL is indexed or cited.

## Gate 2 — plan the anchor and the topic (backlink mode, before writing)

A backlink's value is carried by its anchor text and by whether the surrounding article is about
the same thing as the target page. Both are decided up front and stated, never improvised while
drafting:

| Site | Article angle | Anchor | Anchor type |
|---|---|---|---|

**Read the anchors already pointing at that target page first.** New anchors are chosen against
the existing distribution, not in isolation.

- **Every anchor contains the target keyword or an obvious variant.** A branded or generic anchor
  (`here`, `this tool`, the bare brand name) passes almost nothing for the keyword being fought
  for. Spend one only after the keyword-bearing anchors are in place.
- **Vary the surface form** — exact, plural, branded+exact, partial. One identical anchor repeated
  across every placement is the clearest possible footprint of bought links.
- **The article's topic must match the target page's topic.** A link to an educational-video page
  from an e-bike article is worth close to nothing however good the anchor is.
- **One link per article to the target.** A second adds no value and looks manufactured.
- Apply Gate 1's two rules to the anchor as well. `AI training presentation maker` reads like a
  keyword and is one nobody types; `AI training presentation` is the phrase with real demand.

## Original research (original copy only)

A press release, company blog post, or wire story is a lead, not an article. Add something a
reader cannot get by opening the source:

- Read the originating source plus at least two independent primary sources contributing
  different facts. Reprints and syndicated copies count as one source.
- Produce at least one original finding by calculating, comparing, ranking, or tracing change
  over time. State the denominator, period, and method beside the result so it can be reproduced.
- For a data-bearing story include **one table and one chart**: the table carries exact values,
  the chart reveals the pattern. Bar chart for comparable categories, line chart only for a real
  time series. Never stretch two data points into a decorative chart or invent numbers to satisfy
  this rule. Where a topic genuinely has no comparable data, ship a structured comparison table
  and say why a chart would mislead.
- Charts are supplemental editorial media, embedded in the body with descriptive alt text and a
  visible source/method line — never the cover image.

Before publishing, print: sources used, the original finding, table row count, chart type, word
count. If the draft is mainly a rephrased announcement, research further instead of publishing.

## Supplied copy is immutable by default

When the user provides an article, draft, title, or passage and asks to publish it, that text is
approved copy, not a brief. **Never rewrite it without explicit permission.**

- Preserve the supplied title, thesis, framing, examples, conclusions, tone, ordering, and level
  of certainty. Do not replace the user's argument with a safer or more conventional one.
- An editing instruction authorises only the direction requested. "Make it more affirmative" means
  strengthen the supplied thesis; it does not authorise changing that thesis.
- Factual verification still applies. If verification finds a problem whose correction would
  materially change a supplied claim, show the exact issue and the proposed change and get
  permission **before publishing**. Never silently substitute a different claim.
- Without rewrite permission, limit changes to publication mechanics that preserve the words:
  Markdown formatting, escaping, platform syntax, placement of requested images.
- Before publishing, diff the final copy against the supplied copy. Every substantive change must
  map to an explicit instruction in the current request. If it does not, stop and ask.

## The quality bar — every published article MUST have

### 1. Title

- **~60 characters max** so it fits a SERP `<title>`. No multi-clause headline with an em-dash
  subtitle; trim to the single core hook.
- **Put the searched entity in it — proper nouns beat clever framing.** People search names,
  products, and companies, not concepts. `Demis Hassabis steps down, Jeff Dean leaves Google`
  outranks `Who runs Google AI now?` because both names and the company are literal query terms.
- **The test is "would someone type this", not "does it contain a proper noun".** The *wrong*
  proper noun is as dead as none. Write out the 2-3 searches a reader would actually run, then
  check the title contains those words. Two ways this fails in practice:
  - **Naming your source instead of the subject.** `The Information Drew Dario Amodei as a
    Prophet` has two proper nouns and misses the query, which is `Anthropic IPO`. Who reported it
    belongs in the byline, never the title.
  - **Spending the character budget on tone.** A wry kicker that costs you the word `statue`,
    `cast`, `review`, `price`, or `specs` costs you the highest-volume word available. Cut the
    kicker, keep the noun.
- Exactly one H1. The title is the page H1, so the body must not open with its own `# ` heading or
  repeat the title (demote body headings to H2+).

### 2. Author

A real author is attributed — never the CMS default, "Staff", or a null fallback. The author
record has a name and a bio, avatar preferred. Create one if needed rather than shipping the
fallback. Never fabricate credentials or expertise.

### 3. Images

- **Source order: public-domain photo first, AI-generated second.** Search Wikimedia Commons for
  the actual subject before generating anything, and take the file **only** if its licence is
  `Public domain` or `CC0` — never CC BY, CC BY-SA, or anything else carrying someone's terms,
  even though attribution would technically satisfy them. Use the Commons API
  (`list=search&srnamespace=6`, then `prop=imageinfo&iiprop=extmetadata`, filter on
  `LicenseShortName`) and send a real `User-Agent` or it 403s. Credit a public-domain cover in an
  italic line at the foot of the article.
- **Prefer a real photo when the subject is a real, specific object or place.** An AI render of a
  thing that exists invents its appearance, which is a fabrication with a picture around it. When
  no free photo of the subject exists, a public-domain photo of the *setting* beats an invented
  photo of the subject.
- **Landscape, and no text baked in** — roughly 1200x630 for OG. The title lives in the page, not
  the picture. Crop or regenerate if the ratio is wrong.
- **Realistic, not "AI-looking".** Editorial photographic look; avoid the glossy over-rendered
  aesthetic and metaphor-soup (one object morphing into another). Reserve conceptual imagery for
  pure-science topics; business, policy, and product stories get realistic scenes.
- The OG image URL resolves — `curl -I` returns 200, absolute `https://`, not a placeholder.
- **Distinct per article.** In a batch, assert `distinct(images) == count(articles)`. Omitting the
  field and letting the platform generate one beats shipping a duplicate.

### 4. Outbound source links — at least two, in the body

- **Naming a source in prose does not count. Link it.** A reader checking the claim has to get
  there in one click, and an unlinked source earns nothing.
- Link the primary document where one exists (filing, dataset, release, docket, court order) and
  the report that carried it otherwise. Descriptive anchor, never "here".
- Assert before publishing: `grep -c '](http' <body>` is ≥ 2. On one audit of ten freshly
  published articles, six cited their sources in prose and linked none of them — the crawler
  correctly reported zero external links.

### 5. Length — measured in words, before publishing

- **~1,000 words minimum for a service or explainer piece**, and check the live SERP for the
  target query: if the top results run 1,500+, match them. A 500-word page competing against
  1,500-word pages does not place, however well written.
- **Assert on `len(body.split())`, never `len(body)`.** A character count does not enforce a word
  threshold.
- Length must come from substance — sections answering a real question, specifics, numbers, named
  entities, failure modes. Padding is worse than being short.
- Print per-article word counts so a thin one is visible rather than averaged away.

## Embedding an X post

When the story's source or imagery is an X post, embed the post instead of copying its image: the
image is served under the author's platform licence, credit is built in, and there is no copyright
exposure.

All four must be true before embedding:

1. The post is public.
2. The poster is the actual rights holder — never embed someone's repost of another person's
   image. That is the one pattern that gets publishers sued.
3. Use the official embed markup — never a screenshot or a downloaded copy.
4. The post is the story's source or subject, not decoration.

```html
<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">FULL TWEET TEXT
HERE</p>&mdash; Author Name (@handle) <a
href="https://twitter.com/handle/status/TWEET_ID">Month D, YYYY</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
```

- **Always include the real tweet text** — if the post is deleted, the fallback is a readable
  quote with a link instead of an empty box.
- **Add `data-theme="dark"` on dark-background sites.** The default embed renders as a white card
  that glares on a dark page.
- Place it right after the paragraph discussing the post. It is never the cover/OG image.

**Read the replies too, and use their theories as commentary.** Mine the replies for
*interpretations* — theories about what the post means, skeptical counter-reads, domain experts
adding context — not engagement counts. Work two or three into a reaction section, attribute the
read to the repliers, quote a short phrase where it is vivid, and weigh the theory against the
post's own claims. Joke replies are usable once as colour, never as the analysis. If the replies
contain only jokes, say so in one line — that emptiness is itself a finding.

## Write to be cited

Earned citations are the only backlinks that compound. Derived from a full-network backlink audit
across a dozen publications: every organic link earned went to a page that was the most convenient
place to source **one specific checkable claim**. Homepages and roundups earned nothing.

1. **Write the explainer the week a concept gets a name**, before a canonical page exists.
   News-of-the-day earns nothing; the definitional page earns for months.
2. **Title = the literal question someone types.** The highest-referrer page in that audit was
   `what-does-yann-lecuns-world-model-mean-explained` — and the name in it does half the work. A
   question with no proper noun is not a query anyone types.
3. **One original number per article, stated once, in a liftable sentence.** Not spread across a
   paragraph. A writer scanning for a citable stat needs to grab a single clause.
4. **One quotable judgment per article.** Give the category verdict in a sentence a journalist can
   quote whole with attribution. A DR 82 outlet lifted *"an evolution for the robotic pool skimmer
   category, according to the review"* — one sentence supplying both their framing and their
   attribution.
5. **Publish where it compounds.** Sites publishing specific, quantified work earn citations;
   sites publishing generic regional filler earn zero. Hold every destination to the same bar.
6. **Never break a URL.** A path change without a redirect silently kills every earned link. One
   `/posts/` → `/articles/` migration stranded five DR 49 dofollow citations on 404s until a
   redirect was added. Changing a slug means shipping the redirect in the same change.
7. **Patience is structural.** A May article was picked up in July, unprompted, ten weeks later.
   Pages earn by staying indexed and findable, so URL stability and index health beat any
   launch-day push.

## Publishing mechanics (whatever the CMS)

Read the destination's own API docs or repo conventions rather than assuming. Two failure modes
are near-universal and worth checking explicitly:

- **A create call may ignore the status field and leave a draft.** Verify with a read-back rather
  than trusting the 201 — a draft renders as a 404 on the live site, and on an ISR site that 404
  then caches for the page's revalidate window even after you publish.
- **An "allow missing metadata" escape hatch fails the bar above.** It typically falls back to the
  default author and an auto-generated cover image. Never take it on a placement that matters.

For a code-based destination, read the repo's instructions, make the smallest edit matching the
existing pattern, and ship through that repo's own workflow. Do not add a content system for one
page.

## Verification — the published page, not the payload

1. The published URL returns 200.
2. Fetch the rendered HTML and confirm: the title is the page H1 and is not duplicated in the
   body, the real author byline shows, and the cover image filename is actually present. A missing
   cover collapses silently at 200.
3. **Re-read the rendered title against Gate 1.** This pass is mechanical by nature — does it
   render, is there one H1 — and will happily wave through a title that ranks for nothing. State
   the queries it targets. A title fix is free on any CMS that redirects the old slug.
4. In backlink mode, confirm the target URL and anchor are present **and dofollow**.
   **Check the rendered `rel`, never the markdown.** Many CMSs and site templates add
   `rel="nofollow"` to external links by default; a placement that ships nofollow passes no
   ranking value, which was the entire deliverable, and nothing in the publish flow warns you.
   Source citations stay nofollow — only the intended target gets the exception.
5. **ISR-cached pages do not update immediately.** A `rel` check straight after an edit reads the
   old content and looks like the change failed. Trigger revalidation or wait out the window, then
   re-check.
6. Layout-affecting changes get a headless-browser screenshot. Confirm every table and chart is
   readable at desktop and mobile widths, with legible labels and no horizontal overflow.
7. Report: destination URL, author, cover, anchor + target (backlink mode), publication method,
   and the resource ID or commit.

Only call it done when the title, author, and image bar passes **on the rendered page**.

## API requirements

None mandatory. Optional, depending on what the destination and the gates need:

| Purpose | Typical source |
|---|---|
| Keyword volume and difficulty (Gate 1) | Ahrefs, Semrush, or DataForSEO — see `ahrefs-research`, `semrush-research` |
| Real query data for the target page | Google Search Console — see `search-console` |
| Cover image generation | any image model — see `ai-image-gen` |
| Public-domain imagery | Wikimedia Commons API, no key required |
| Publishing | your own CMS or repo credentials |
