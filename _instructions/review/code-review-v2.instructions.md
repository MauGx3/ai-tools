---
applyTo: "**"
excludeAgent: "coding-agent"
title: "Structured Code Review Playbook"
type: "best-practices"
difficulty: "intermediate"
time_required: "20-30 minutes"
prerequisites: "Familiarity with `general.instructions.md`, repository workflow, and GitHub PR process"
description: "Reorganized guidance for conducting thorough, high-impact code reviews in the ai-tools project"
tags: ["code review", "quality assurance", "collaboration", "best practices"]
categories: ["development"]
---

## Overview

- Purpose: provide a concise, context-aware playbook that complements `code-review.instructions.md` while following the Copilot “5 tips” structure.
- Audience: reviewers (human or AI) working on pull requests across the `ai-tools` repository.
- Prime directive: honour the 97% confidence gate from `general.instructions.md`—state your confidence before delivering review output, and pause to ask questions if it drops.
- Review objective: validate intent, correctness, security, and maintainability without blocking progress on low-priority nits.

## Tech Stack & Review Environment

- Languages & artefacts: Python automation scripts (`scripts/`), Markdown documentation (`docs/`, `_instructions/`), Jekyll templates/layouts (`_layouts/`, `_config.yml`), and workflow assets under `.github/`.
- Tooling expectations:
  - Static analysis: `ruff` for Python style, Markdown linting via CI when applicable.
  - Testing: `pytest` for Python modules; Jekyll builds via Bundler when layout changes occur.
  - Security: follow `security-and-owasp.instructions.md` and verify secrets remain in `.env` or secret stores.
- Review setup checklist:
  - Pull latest `main`, run `pytest` / `ruff` / Jekyll build locally when scope warrants.
  - Inspect PR description, linked issues, and any task files within `memory-bank/`.
  - Confirm Conventional Commit message in PR title or associated commits.

## Review Workflow & Guidelines

### 1. Prepare & Understand Intent

- Read the entire PR summary, linked tickets, and relevant instruction files before reviewing code blocks.
- Capture the author’s goal: What problem is solved? Which repo areas are touched? Reference the Memory Bank for recent context when available.

### 2. Prioritize Impact

Assess findings using a severity ladder:

| Level | Criteria | Action |
|-------|----------|--------|
| Critical | Breaks correctness, security, data integrity | Block merge; propose fix |
| High | Performance regressions, architectural drift, missing tests | Request change before merge |
| Medium | Maintainability concerns, unclear intent | Prefer fix-now; if deferred, document follow-up |
| Low | Style nits, micro-optimizations | Mark as optional; don’t block |

Focus first on functionality, security, and regression risk. Confirm that regression and unit tests cover new or changed behaviour. Cross-check with `python.instructions.md` (or language-specific equivalents) for style disagreements.

### 3. Deliver Objective, Actionable Feedback

- Anchor every comment with evidence: cite lines, standards, or existing patterns.
- Prefer structured sentences using Conventional Comments (`nit`, `suggestion`, `issue`, `praise`) to convey severity.
- Example transformation:
  - 🔴 Issue: “The SQL query interpolates `user_input` directly (line 78). Please switch to parameterized queries to avoid injection, as we do in `scan_starred_repos.py:210`.”
  - 🟢 Praise: “Nice reuse of `RepoRecommender` abstractions—mirrors the pattern from PR #142 and keeps the CLI cohesive.”
- When uncertain, ask clarifying questions instead of assuming intent.

### 4. Apply Advanced Techniques

- Scope-aware review: small fixes (<50 LOC) → edge cases; medium features (50–400 LOC) → architecture & tests; large refactors (>400 LOC) → ensure behaviour parity and consider requesting split.
- Contextual empathy: tailor explanations depending on contributor experience. Offer rationale for new contributors; focus on systemic impact for seasoned maintainers.
- Detect common pitfalls: magic numbers, deep nesting, missing error handling—recommend named constants, early returns, and defensive coding per project conventions.

### 5. Communication & Resolution

- Use the Situation–Behavior–Impact format to frame blockers.
- Distinguish between “must fix before merge” and “follow-up task”; open an issue when deferring meaningful work.
- Escalate synchronous discussions if >10 critical issues emerge or design direction remains unsettled after async feedback.

## Repository Structure & Reference Points

- `scripts/`: Python CLIs—verify changes update `scripts/README.md` and add tests under `scripts/tests/` when behaviours shift.
- `docs/` & `README.md`: documentation must reflect behaviour changes; ensure table-of-contents and cross-links stay accurate.
- `_instructions/`: layered guidance. Confirm modified instructions stay consistent across related files (e.g., general vs. language-specific).
- `.github/`: workflow automation; verify YAML syntax, action versions, and secret usage.
- `memory-bank/`: if updated, check entries echo actual state and maintain traceability.

## Resources & Checklists

- Security deep dive: validate input sanitization, authz boundaries, secret handling (see checklist in the legacy instructions).
- Performance review: watch for O(n²) patterns, redundant database calls, and memory hotspots; suggest maps/sets, batching, pagination as needed.
- Quality checklist highlights:
  - Variable and function names self-document intent.
  - Functions maintain single responsibility and acceptable cyclomatic complexity (<10 where practical).
  - Tests cover new branches and edge cases (empty data, large payloads, API failures).
  - Error handling surfaces actionable logs without leaking sensitive data.
- Positive reinforcement: acknowledge well-executed patterns to reinforce best practices.

## Additional References

- Legacy compendium: `code-review.instructions.md` (deep dives, examples, and extended checklists).
- External standards: Google Engineering Practices, Conventional Comments, OWASP Top 10.
- Repository knowledge sources: Memory Bank files, `_thoughts/` analyses, and third-party article “5 tips for writing better custom instructions for Copilot.”
- For language nuances, consult `code-review-instructions-python.md` (and future language-specific supplements) before flagging stylistic issues.

---

Apply this playbook alongside the detailed legacy guide to deliver reviews that are thorough, respectful, and aligned with the project’s quality bar.
