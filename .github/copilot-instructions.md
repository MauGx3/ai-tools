---
applyTo: "**"
---
## Overview

- This file sets the global rules for collaborating with GitHub Copilot across the entire `ai-tools` workspace.
- Always operate transparently: surface assumptions, cite relevant instructions, and document outcomes so future sessions stay aligned.
- Treat every task as part of an ongoing knowledge base—keep the Memory Bank and repository documentation consistent with your actions.

## Collaboration Workflow

### Confidence Gate

- Do not make any changes until you have **97% confidence** that you understand the request.
- Every response must state an explicit confidence percentage. If confidence is below 97%, ask targeted follow-up questions before proceeding.
- Example of a compliant reply: “Confidence: 92%. Please clarify the target output format before I continue.”
- This rule must be echoed in all subordinate instruction files so downstream agents honour it.

### Enforcement & Runtime Behaviour

- Any proposal or code delivery without a confidence value—and, when <97%, a clarifying question—is a policy violation.
- When uncertainty arises mid-task, pause, reassess requirements, and surface new questions rather than forging ahead.
- Document confidence rationale in progress notes (e.g., task logs, Memory Bank updates) to preserve traceability.

## Tech Stack & Tooling

- Primary languages: Python (automation scripts in `scripts/`) and Markdown for documentation. The site scaffold also includes Jekyll/Ruby assets (`Gemfile`, `_config.yml`)—respect their conventions when touched.
- Preferred tooling aligns with language-specific instruction files: Python uses `uv`, `pytest`, `ruff`, `polars`, and `loguru`. Ruby/Jekyll tasks rely on Bundler workflows defined in project docs.
- Environment secrets should come from `.env` or secure key stores; never hardcode credentials.
- Follow `security-and-owasp.instructions.md` for secure coding practices across languages.

## Project Structure

- Root documentation (`README.md`, `docs/`, `instructions.md`) describes AI-assistant workflows and should remain authoritative.
- `_instructions/`: layered instruction sets (general, language-specific, review). Update the relevant file when project norms evolve.
- `_thoughts/` & `thoughts.md`: historical analyses; treat as append-only references.
- `scripts/`: Python automation utilities plus `results/` outputs. Coordinate updates with accompanying documentation and requirements files.
- `data/`: Sample datasets—avoid storing sensitive information.
- `.github/`: Copilot and workflow configuration; changes here affect automation and must be validated carefully.
- `memory-bank/` (when present): canonical state tracking. Always review and update per Memory Bank procedures before and after significant work.

## Coding & Contribution Guidelines

### Git & Commit Discipline

- Adhere to [Conventional Commits](https://www.conventionalcommits.org/) for every commit. Summaries must use the format `<type>[optional scope]: <description>` with a maximum of 72 characters.
- Valid types include: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`. Use scopes to pinpoint the affected area (e.g., `docs(instructions)`).
- End every “commit-worthy” update with a proposed commit message in the final response. Omitting this is a violation.
- Breaking changes must append `!` after the type/scope and include details in the body.
- Provide a git commit description only when the summary cannot capture the change within 72 characters.

### Additional Collaboration Expectations

- Use English in commit summaries unless domain-specific terms make translation impractical.
- Keep commits atomic: one logical change per commit.
- Reference applicable instruction files in discussions and updates to maintain shared context.
- When adding or updating automation, surface required commands and ensure they work in the Fish shell environment (default for this workspace).

## Resources & References

- `memory-bank.instructions.md`: Workflow for maintaining project memory—consult at the start of every session.
- `python/python.instructions.md` and other language-specific files: Supersede general rules where more specific guidance exists.
- `docs/guides/`: Operational guides (e.g., starred repository scanner) that detail end-to-end processes.
- `_thoughts/third-party/5 tips for writing better custom instructions for Copilot - The GitHub Blog.md`: Source for structuring instruction files; revisit when evolving guidance.
- `.github/copilot-instructions.md`: Central Copilot configuration; keep changes aligned with this general policy.

---

Follow this convention and the associated language-specific instructions for all contributions.
