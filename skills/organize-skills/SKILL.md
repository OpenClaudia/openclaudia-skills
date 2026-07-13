---
name: organize-skills
description: Audit and reorganize a Claude Code / Codex skill library — enforce a naming convention (prefix each skill by which backend or product it touches), rename skills consistently, fix the symlinks and cross-references a rename breaks, and report broken symlinks and stale name references. Use when the user says "organize my skills", "rename these skills", "clean up the skill library", "enforce a skill naming convention", or "fix broken skill symlinks".
user_invocable: true
argument-hint: "[optional: the prefix rule, e.g. 'acme-* if it calls the Acme API, local-* otherwise']"
---

# Organize Skills

Reorganize a skill library so names encode what each skill actually touches, and keep symlinks and
cross-references consistent when you rename.

Many setups keep ONE canonical skill library in a shared dir and symlink it into each tool's hub
(e.g. `~/.claude/skills/`, `~/.codex/skills/`). Some skills live inside a project repo and are
symlinked into the hub. A single rename can therefore touch several symlinks plus every doc that
references the old name — that fan-out is what this skill manages.

## Step 1 — Inventory

List every skill and where it really lives. A hub entry is usually a symlink to the canonical dir:

```bash
for hub in <hub-1> <hub-2>; do
  echo "== $hub =="; ls -la "$hub"
done
```

Resolve each name to its real directory with `readlink -f`. Note which skills live in a project repo
versus the shared library — repo-resident renames must be `git mv` in that repo.

## Step 2 — Classify by backend (the naming rule)

The convention: **the prefix names the backend the skill depends on**, decided by what it actually
calls, not by its topic. Grep each skill dir for the tell-tale dependency:

```bash
grep -rlE "<api-host>/api|/api/<x>|<db-client>|<AUTH_TOKEN_NAME>" "$skill_dir"
```

- Calls a specific product's API / database → that product's prefix (e.g. `acme-*`).
- Pure-local (browser automation, offline SOP, file processing, no backend) → a generic/local prefix.
- Keep a topical infix when a family is large (e.g. `acme-seo-*` vs `acme-reddit-*`) so related skills sort together.

State the classification back to the user before renaming. A skill that *feels* product-specific but
makes zero backend calls belongs in the local bucket, and vice versa — go by the dependency.

## Step 3 — Rename (and fix everything a rename breaks)

For each rename `OLD → NEW`:

1. **Move the canonical dir.**
   - Shared-library-resident: `mv <lib>/OLD <lib>/NEW`
   - Repo-resident: `cd <repo> && git mv <skills-path>/OLD <skills-path>/NEW && git commit`
   - Misplaced in the wrong repo? Move it to the shared library rather than just renaming in place.
2. **Rewire symlinks in every hub.** Remove the stale link, create the new one pointing at the
   canonical dir. Do this for each tool hub that mirrors the library.
3. **Update the `name:` frontmatter** inside `NEW/SKILL.md` to match the directory — the loader keys
   on it, not on the folder name.
4. **Fix cross-references.** Other skills and any long-term memory/notes files may mention `OLD` by
   name or by old path:
   ```bash
   grep -rln "OLD" <lib> <memory-dirs> 2>/dev/null
   ```
   Replace the most-specific string first (full old *path* before the bare *name*) so a skill that
   also moved gets its path updated cleanly.

## Step 4 — Verify

```bash
# broken symlinks in any hub
for hub in <hub-1> <hub-2>; do
  find -L "$hub" -maxdepth 1 -type l ! -exec test -e {} \; -print
done
# no lingering old names
grep -rn "OLD" <lib> 2>/dev/null
# each renamed skill's name: matches its dir
grep -m1 "^name:" <lib>/NEW/SKILL.md
```

Confirm the loader re-registers each renamed skill under its new name. Remove any pre-existing dead
symlinks you find while sweeping — cheap to fix, confusing to leave.

## Notes
- Never drop a skill you didn't rename. Only touch what the convention requires.
- Renames are cheap and reversible; broken cross-references are the real cost — Steps 3.4 and 4 are the
  point of this skill, not the `mv`.
- Commit repo-resident renames one logical rename per commit so they bisect and revert independently.
