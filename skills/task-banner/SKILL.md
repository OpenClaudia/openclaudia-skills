---
name: task-banner
description: Set up (or toggle) a macOS desktop banner that appears whenever Claude Code finishes a task, showing a one-line summary of what was done. Use when the user says "notify me when Claude is done", "desktop notification on completion", "set up the task banner", "mute the banner", or "unmute the banner".
---

# task-banner

Show a large, always-on-top desktop banner when Claude Code finishes a turn — with a one-line summary of what was actually completed. Works even when macOS Notification Center silently drops `osascript display notification` calls (a common problem: the CLI has no Notification Center registration, so the command exits 0 but nothing shows).

The banner is a borderless Cocoa overlay window drawn by `mac-overlay.js` (a JXA script adapted from [peon-ping](https://github.com/PeonPing/peon-ping)), so no notification permissions are needed.

## Requirements

- macOS (the overlay uses Cocoa via JXA / `osascript -l JavaScript`)
- Claude Code with hooks support

## Setup

1. Copy `mac-overlay.js` from this skill directory to `~/.claude/scripts/mac-overlay.js`.

2. Merge a `Stop` hook into `~/.claude/settings.json` (read the file first and preserve existing hooks):

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "m=$(cat /tmp/claude-banner-msg 2>/dev/null); rm -f /tmp/claude-banner-msg; [ -f ~/.claude/banner.off ] || osascript -l JavaScript ~/.claude/scripts/mac-overlay.js \"${m:-Task done}\" blue \"\" 0 4 2>/dev/null || true",
            "async": true
          }
        ]
      }
    ]
  }
}
```

3. To make the banner show *what* was finished (instead of the generic "Task done"), add this to your global agent instructions file (`~/.claude/CLAUDE.md` or `AGENTS.md`):

> After finishing each task, write a short summary of what was completed to `/tmp/claude-banner-msg` (e.g. `printf 'Typecheck fixed and committed' > /tmp/claude-banner-msg`). Identify the actual task; never use a generic "task done".

The Stop hook displays the message and deletes the file. If the file is absent, it falls back to "Task done".

## Toggle (mute / unmute)

The hook checks a sentinel file — no config editing needed:

```bash
touch ~/.claude/banner.off   # mute the banner
rm -f ~/.claude/banner.off   # unmute
```

When the user asks to mute/unmute the banner, run the matching command and report the resulting state.

## How it works / notes

- `mac-overlay.js <message> <color> <icon> <slot> <dismiss_seconds>` — color is `blue`/`yellow`/`red`, dismiss `0` means persistent-until-click.
- The hook consumes `/tmp/claude-banner-msg` even while muted, so no stale summary pops up later when unmuted.
- On recent macOS the JXA bridge constant `NSTextAlignmentCenter` evaluates to the legacy AppKit value (2), which the unified runtime treats as right-aligned — the bundled script hardcodes alignment `1` (center) to compensate.
- `/tmp/claude-banner-msg` is shared across parallel Claude sessions; if two finish in the same instant one banner may show the other's summary. Use a per-session file path if that ever matters.
