---
applyTo: '**/*.instructions.md'
---
## Purpose

This instructions file teaches an LLM agent how to refactor an existing `.instructions.md` file so it follows the guidance in "5 tips for writing better custom instructions for Copilot" and the repository's conventions.

Confidence requirement: before making edits, ensure you can state an explicit confidence percentage. If your confidence is <97%, ask targeted clarifying questions and do not mutate files.

## Contract (inputs / outputs / error modes)

- Inputs: path to a single `.instructions.md` file (absolute or repo-relative). The file may be empty, outdated, or partially structured.
- Output: a refactored `.instructions.md` file that:
  - contains a YAML front matter with at least `applyTo` and optional metadata
  - includes the five recommended sections: Overview, Tech Stack, Coding Guidelines, Project Structure, Resources
  - follows repo markdown rules (H2/H3 headings, short lines, Sphinx/docstring notes where relevant)
- Error modes:
  - Missing file: report and abort
  - Ambiguous intent or missing info: pause and ask user
  - Conflicting rules across instruction files: surface conflict and propose resolution

## High-level steps (what the agent will do)

1. Read the target file fully and compute a summary of its current sections and rules.
2. Run a quick repository context check (locate `README.md`, `_instructions/`, `docs/`, `scripts/`) to gather hints about tech stack and structure.
3. Produce an edit plan (in plain text) that lists proposed additions/changes and the rationale. Include a confidence percentage and any clarifying questions.
4. After approval (or if confidence >=97% and no questions remain), apply the refactor in a single atomic edit:
   - Add or normalize YAML front matter
   - Reorder or add the five sections
   - Preserve any project-specific rules; rewrite them where they belong (e.g., Python rules -> Coding Guidelines)
   - Add cross-references to other instruction files and `general.instructions.md` policy about confidence and commits
5. Run validation checks (local markdown linting guidelines, simple front-matter presence, heading levels).

## Detailed rewrite recipe (per-section guidance)

Use these heuristics and templates to rewrite or add content.

1) YAML front matter

- Required: `applyTo: "**/*.instructions.md"` (or more specific pattern where appropriate).
- Optional: `title`, `description`, `tags`, `applyTo` pattern.
- Place it at the top of the file enclosed by `---` lines.

2) Overview (H2)

- 2–4 short sentences explaining the purpose and audience of the instructions file.
- If the repository context is known, include one sentence about where the file applies (e.g., "applies to Python files in `scripts/`").

3) Tech Stack & Environment (H2)

- List primary languages, runtimes, and major tools used by the code that these instructions affect.
- If unsure, point to likely files (e.g., `scripts/README.md`, `Gemfile`, `requirements.txt`) and ask clarifying question.

4) Coding Guidelines (H2)

- Consolidate language-agnostic rules here (naming, docstrings, testing expectations, security bullet points).
- Move language-specific rules into dedicated subsections or point to existing language instructions (e.g., `python/python.instructions.md`).
- Keep rules prescriptive and short; include examples only for non-obvious rules.

5) Project Structure (H2)

- Add a short tree or bullet list showing where relevant code lives (e.g., `scripts/`, `docs/`, `_instructions/`).
- If the repo contains special folders (Memory Bank, MCP servers), mention them and link.

6) Resources (H2)

- Point to scripts, templates, CI jobs, and docs that help developers follow the instructions (`scripts/README.md`, `docs/guides/`, `.github/` workflows).
- Add a short validation checklist (see Validation below).

7) Preservation rules

- Preserve any policy statements that are legally or operationally critical (security rules, commit policies, test requirements).
- Do not remove author attributions or historical notes; move them to a `History` subsection if necessary.

## Edge cases and clarifying questions

- Empty file: create a minimal template containing the YAML front matter and the five sections with TODO placeholders and ask the user to fill domain-specific details if confidence <97%.
- Multiple instruction files with overlapping `applyTo`: surface conflict and recommend disambiguation (narrower globs or file-scoped instructions).
- Very long instruction files: break into logical files (e.g., `python.instructions.md`, `review/*.instructions.md`) and propose the split in the edit plan.

## Validation checks (post-edit)

Run these simple validations locally and report failures:

- YAML front matter exists and `applyTo` is present.
- Top-level headings use `##` (no H1); only `###` for subsections.
- Lines are reasonably short (soft limit 400 chars; prefer ~120 chars for readability).
- The five sections are present (Overview, Tech Stack, Coding Guidelines, Project Structure, Resources). If any is intentionally omitted, document why.
- No secrets are added to the file (API keys, tokens, passwords).
- Cross-links to other instruction files are correct (relative paths).

Optional automated checks (if tooling available):

- Run a Markdown linter and surface issues.
- Check repository for referenced files (`scripts/README.md`, `docs/`) and warn if missing.

## Example flow (agent run)

1. Read `_instructions/old.instructions.md` and summarize existing sections.
2. Generate edit plan and show: "Confidence: 95% — please confirm the tech stack is Python 3.8+ or grant permission to infer from `scripts/README.md`."
3. After confirmation, rewrite file following the recipe above.
4. Run validation checks.

## When to escalate to a human

- If confidence <97% after inspecting repo context and asking reasonable questions.
- If you detect legal/security text whose change might have policy implications.
- If multiple instruction files appear to conflict in scope and the correct resolution is unclear.

## Minimal refactor template (copy-paste)

---

applyTo: "`<glob pattern>`"
-----------

## Overview

- Short elevator pitch about purpose and audience.

## Tech Stack & Environment

- Languages and major tools.

## Coding Guidelines

- Key rules and where to find language-specific guidance.

## Project Structure

- Short tree of where code and docs live.

## Resources

- Useful scripts, CI jobs, and docs.

---

## Final notes

- Always include your confidence percentage at the top of the edit plan and final message.
- Avoid changing unrelated files and keep edits minimal and reviewable.
