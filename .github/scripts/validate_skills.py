#!/usr/bin/env python3
"""Validate skill frontmatter and README skill table.

Checks:
1. Every skills/*/SKILL.md has a YAML frontmatter block (delimited by ---).
2. The frontmatter parses as valid YAML and has non-empty `name` and `description`.
3. The README skill table lists exactly the skills present in skills/ (count + names).

Exits non-zero with a report if any check fails.
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

# Matches README table rows like: | `skill-name` | description | ... |
TABLE_ROW = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|")


def parse_frontmatter(text: str):
    """Return the parsed frontmatter dict, or raise ValueError."""
    if not text.startswith("---"):
        raise ValueError("missing YAML frontmatter (file must start with '---')")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("frontmatter block is not closed with a second '---'")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a YAML mapping")
    return data


def main() -> int:
    errors = []

    skill_dirs = sorted(p.name for p in SKILLS_DIR.iterdir() if p.is_dir())

    for name in skill_dirs:
        skill_md = SKILLS_DIR / name / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{name}: missing SKILL.md")
            continue
        try:
            data = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{name}/SKILL.md: {exc}")
            continue
        for field in ("name", "description"):
            value = data.get(field)
            if not (isinstance(value, str) and value.strip()):
                errors.append(f"{name}/SKILL.md: missing or empty `{field}` field")

    # Reconcile the README skill table against the skills/ directory.
    documented = {m.group(1) for line in README.read_text(encoding="utf-8").splitlines()
                  if (m := TABLE_ROW.match(line))}
    actual = set(skill_dirs)

    undocumented = sorted(actual - documented)
    phantom = sorted(documented - actual)
    if undocumented:
        errors.append("README skill table is missing rows for: " + ", ".join(undocumented))
    if phantom:
        errors.append("README skill table has rows with no skills/ dir: " + ", ".join(phantom))
    if len(documented) != len(actual):
        errors.append(f"README skill count ({len(documented)}) != skills/ dir count ({len(actual)})")

    if errors:
        print("Skill validation FAILED:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All {len(actual)} skills valid; README table matches skills/ directory.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
