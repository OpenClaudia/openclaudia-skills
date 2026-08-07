---
name: wechat-moments
description: "Rank and summarize the user's own WeChat Moments (朋友圈) feed so real life events and genuine information rise above promotion and small talk, weighted by how much the user actually talks to each author. Use when the user says 'summarize my Moments', 'read my 朋友圈', 'what did I miss on Moments', 'rank my Moments', or 'check my WeChat Moments'."
---

# WeChat Moments digest

Turns a WeChat Moments feed into a short ranked digest: what deserves a reply,
what is genuinely informative, and what is marketing wearing a personal voice.

The scripts live in a **separate repository**, not here, because they depend on
the WeChat desktop client rather than any marketing API:

**https://github.com/OpenClaudia/wechat-moments**

```bash
git clone https://github.com/OpenClaudia/wechat-moments.git
```

Read that repo's README before running anything. It documents the setup, the
limits, and the risks — this skill is the ranking method, not the plumbing.

## Before you touch it

- **It does not decrypt anything and never handles keys.** It reads a plaintext
  database that a separate WeChat export tool has already produced. If the user
  has no export yet, that is step one and it is not this skill's job — the repo
  lists existing tools for it.
- **Moments do not sync in the background.** WeChat fetches the timeline only
  while the Moments window is open. Without a sync the export contains only
  what the user already scrolled past, so the digest is a replay of what they
  have already seen. Say so rather than presenting stale posts as today's.
- **Tell the user the limits before setting this up on a schedule.** It needs
  WeChat running and logged in, it only stays complete while the machine is
  awake (sleep gaps are permanently unrecoverable), Tencent may break or patch
  it at any time, automating the client may be noticed and may carry account
  risk, and nothing is guaranteed.
- **Never post, like, comment, or message on the user's behalf.** Reading and
  writing files is the whole remit.

## Ranking

This is the part worth carrying to any feed, not just WeChat.

**Score = event weight × relationship weight.** Do it yourself from the
structured records; do not write a scoring script. The point is judgement —
"her mother is in hospital" outranks "went to Kyoto".

**Event weight (0-10).** Birth, death, serious illness, wedding, divorce,
emigration at the top. New job, funding, graduation, a home, a pregnancy just
below. Travel and opinions in the middle. Food, gym, weather, scenery at the
bottom. Promotion and recruiting score zero.

**Insight vs. announcement** decides most of the digest, because feeds full of
founders and creators are full of engagement bait. Real information has at
least one of: a number you could check, a mechanism (*why* it works), a cost
the author actually paid, or a changed mind. Adjectives (突破 / 颠覆 /
groundbreaking), a milestone with no mechanism, an invitation, an upvote
request, or a takeaway generic enough to predate the event are announcements.
**Prestige is not evidence** — a famous venue is still promotion when the
payload is one generic sentence. A tiny post can be real insight.

**Relationship weight — lead with how much the user SENT.** Not total volume:
a marketer who broadcasts dozens of pitches and never gets a reply scores
identically to a close friend. A reply is a choice; an inbound blast is not.
Never-messaged contacts get filtered hard whatever they posted — expect them to
be about a third of any day's feed.

**A close friend's small post usually beats a stranger's big news**, because
only one of them is a relationship the user can act on. Ranking on content
alone inverts this every time.

**Time since last contact is its own signal.** Many messages sent but silent
for a long time is a lapsed close friend, and a life event from one of those is
the most actionable thing a digest can surface.

**Promotion wears a personal voice.** A discount code, a signup link, an
invite-only pitch: the poster is selling, however casual the phrasing.

**Urgency is a modifier, never a reason.** Never open a digest with a dated
section — that structure promotes whatever has a deadline, and deadlines are
what promotions have. An expiring ad is still an ad.

## Output

Ten items is plenty; fewer is often right, and **zero worth reporting is a
legitimate result** — say so rather than padding. Keep strong ties and
weak-tie-but-useful content in separate, clearly labelled sections, so
interesting content from a stranger never looks like something to act on. Show
the relationship numbers per entry so the ranking is auditable and the user can
correct it.

Summarize Chinese posts in Chinese and English posts in English. Say what a
post *is*; never repost it verbatim.
