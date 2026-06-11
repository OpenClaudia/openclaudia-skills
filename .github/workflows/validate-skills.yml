name: Validate Skills

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install PyYAML
        run: pip install pyyaml
      - name: Validate SKILL.md frontmatter and README table
        run: python3 .github/scripts/validate_skills.py
