---
name: wechat-read
description: "Read and search the user's own WeChat (微信) chats from a local plaintext export on macOS: recent conversations, a full thread, keyword search, contacts, chats waiting on a reply, and a one-day digest. Use when the user says 'read my WeChat', 'check my 微信', 'what did <person> say on WeChat', 'search my WeChat for X', 'who haven't I replied to', or 'summarize my WeChat today'."
---

# WeChat reader

Reads the user's own WeChat for macOS (3.x) chats from a plaintext export on
their own machine. Stdlib Python only. Nothing is uploaded or sent.

## Before you touch it

- **It does not decrypt anything and never handles keys.** It reads a plaintext
  export that a separate tool has already produced. If the user has no export
  yet, that is step one and not this skill's job. The
  [wechat-moments README](https://github.com/OpenClaudia/wechat-moments#you-need-an-exporter-first)
  lists existing exporters. Read their code before running one.
- **The export is a snapshot.** New messages appear only after the user re-runs
  their exporter. Say how old the snapshot is rather than presenting it as live.
- **Own account only.** Never post, reply, or message on the user's behalf.
  Drafting a reply for the user to send themselves is fine.

## Setup

```bash
export WECHAT_EXPORT=~/path/to/decrypted   # expects Message/, Contact/, Group/, Session/
S=<this skill>/scripts
```

## Commands

```bash
python3 $S/wechat.py list [N]               # recent conversations + who spoke last
python3 $S/wechat.py read <name|wxid> [N]   # full thread; group senders resolved
python3 $S/wechat.py search "<keyword>" [N] # text search across all chats
python3 $S/wechat.py contacts "<keyword>"   # find usernames by name/remark/nickname
python3 $S/wechat.py unreplied [days]       # 1:1 chats where THEY messaged last
python3 $S/wechat.py day YYYY-MM-DD [--all] # every thread active that day
python3 $S/wechat.py whoami                 # the user's own wxid
```

## Reading it right

- **Names are ambiguous.** Several contacts can share a display name. `read`
  shows the most recently active match and lists the others' wxids. When the
  user means a specific person, confirm with them or target `read <wxid>`.
- **Groups need their `@chatroom` id.** `read` resolves 1:1 names but not group
  display names. Take the id from the third column of `list`.
- **`unreplied` is a candidate list, not a to-do list.** Most "last from them"
  messages are closers ("好的", "哦哦"). Read each thread and judge by content.
  Before calling someone ignored, `search` their name: the conversation may have
  moved to a group chat.
- **`day` hides large groups** (15+ members) unless `--all`. To always include or
  exclude a group, or match groups by name, add one entry per line to
  `ignore_groups.txt`, `keep_groups.txt` or `relevant_keywords.txt` in
  `WECHAT_CONFIG` (default `~/.config/wechat-read`).
- **Pronouns:** `day` tags each 1:1 contact with the gender from their own
  WeChat profile when set. When it says `pronoun unknown`, use their name.
- Message types: 1 text, 3 image, 34 voice, 43 video, 47 sticker, 49 file/link,
  10000 system.
