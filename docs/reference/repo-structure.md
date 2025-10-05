# Repository structure (reference)
---
title: "Repository structure"
type: "reference"
layout: "default"
---

Quick reference for the most important files and folders in this repository.

- `README.md` — project overview and quick links
- `docs/` — user-facing documentation (this folder)
- `_prompts/` — prompt definitions used by agents
- `_instructions/` — instruction files with `applyTo` rules for automated agents
- `scripts/` — Python utilities and automation scripts
  - `requirements.txt` — Python dependencies used by the scripts
  - `repo_recommender.py`, `scan_starred_repos.py` — main example scripts
- `data/` — sample datasets and example outputs
- `results/` — example outputs and run artifacts (may be gitignored)
- `.github/` — CI workflows, GitHub Actions and project automation
  - `workflows/` — contains e.g. `jekyll-gh-pages.yml` for site publishing
- `docs/` — documentation pages for GitHub Pages / site

Commands

- Run tests (if provided): see `tests/` and `playwright.config.ts` for end-to-end checks.
- Install Python dependencies for scripts:
  ```fish
  pip install -r scripts/requirements.txt
  ```

Environment & secrets
- The repository uses environment variables for any external integrations. Never commit secrets — read `security-and-owasp.instructions.md` for guidance.
