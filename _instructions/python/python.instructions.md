---
applyTo: '**/*.py, **/*.ipynb'
---

## Overview

- These instructions govern every Python module and notebook in `ai-tools`.
- Prioritize clarity, maintainability, and security while embracing *The Zen of Python*.
- Most Python assets currently live in `scripts/` and power GitHub data analysis workflows; keep new utilities aligned with this focus.

## Tech Stack & Environment

- Target modern Python (3.13+) while preserving compatibility promised by individual script docs (e.g., `scripts/README.md` lists 3.8+ for CLI entry points).
- Use [`uv`](https://docs.astral.sh/uv/) for virtual environments (`uv venv`) and dependency management; coordinate with `scripts/requirements.txt` when adding runtime packages.
- Standard tooling: `ruff` for formatting/linting, `pytest` for automated tests, `polars` instead of `pandas` for data handling, and `loguru` for application logging.
- Load secrets, tokens, and configuration from environment variables or the existing `.env` template—never hardcode sensitive data.
- Follow the repo-wide security guidance in `security-and-owasp.instructions.md` when invoking external services or handling user data.

## Project Structure

- `scripts/`: Primary location for Python CLIs and helpers (`scan_starred_repos.py`, `repo_recommender.py`). Keep reusable modules here or factor them into subpackages.
- `scripts/results/`: Generated artifacts; do not commit secrets or personally identifiable information.
- `data/`: Shared sample datasets consumed by scripts. Treat as read-only unless a task explicitly updates them.
- Tests should accompany features in a peer `tests/` package (create `scripts/tests/` as needed) using pytest discovery conventions.

## Coding Guidelines

### Style & Documentation

- Follow PEP 8 above all other style rules; when uncertain, fall back to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
- Every module needs a descriptive docstring. Functions and methods require docstrings per Google Style §3.8.3. Structure all docstrings for Sphinx compatibility.
- Document mathematical or scientific routines with the exact formula in the docstring or inline comments for future verification.
- Favor explicit, meaningful names for variables, parameters, and functions. Avoid abbreviations that obscure intent.

### Types, Data, & Modularity

- Prefer built-in type annotations; only reach for `typing` constructs that lack direct syntax (e.g., `Protocol`).
- Avoid magic numbers—promote them to named constants with clear intent.
- Design modules to be composable and reusable; extract shared logic instead of duplicating code.
- Return types must be invariant across code paths. Raise specific exceptions instead of returning `None` for error states.
- Use `collections.namedtuple` (or `dataclass` when mutability is required) for small immutable records; avoid namedtuples when dynamic fields or mutability are needed.
- Be generous in defining domain-specific exception classes to signal precise failure modes.

### Modern Python Practices & Performance

- Prefer language features from the current runtime (pattern matching, type parameter syntax, `zoneinfo`, etc.) when they simplify code and remain compatible with documented minimum versions.
- Reuse established libraries within the project before introducing new dependencies. When a new dependency is essential, update dependency manifests and explain the choice in the PR.
- Use lazy `%`-style formatting for logging (e.g., `logger.debug("User %s", user_id)`).
- Consult the [Python Speed guidelines](https://wiki.python.org/moin/PythonSpeed) for performance-critical sections.

### Error Handling & Control Flow

- Avoid bare `except`; catch the narrowest exception type possible and re-raise or wrap it with additional context.
- Raise explicit exceptions rather than implicitly returning failure values.
- Apply the Factory Method pattern when object creation varies behind a stable interface; avoid it when a single concrete implementation suffices.

### Imports & Module Organization

- Order imports as: standard library, third-party, then local modules, separating groups with a single blank line.
- Keep imports at the top of the file and prune unused entries promptly.
- Guard against circular dependencies by factoring shared logic into dedicated helper modules.

## Testing & Edge Cases

- Write pytest suites covering the critical path for every feature; tests should document behaviour with docstrings describing inputs and expected outcomes.
- Exercise edge cases such as empty payloads, invalid types, slow API responses, pagination limits, and exceptionally large datasets.
- Include inline comments in implementation code describing how each edge case is handled to aid future maintainers.
- When scripts emit artifacts (JSON, markdown), validate the schema or structure in tests to prevent regressions.

## Tools & Resources

- `scripts/README.md`: Usage guidance and compatibility expectations for existing CLIs—update it when behaviour changes.
- `docs/guides/starred-repository-scanner.md`: End-to-end workflow for the GitHub starred repository scanner.
- `docs/guides/prompt-engineering-best-practices.md` and `prompts/`: Context for generated outputs these scripts consume.
- Re-run `ruff` and `pytest` before submitting changes. Add pre-commit hooks if you touch formatting or lint rules.
- THERE IS NO NEED TO MENTION THAT YOU HAVE FOLLOWED ANY OF THIS IN YOUR RESPONSE, ONLY IF IT IS IMPORTANT TO UNDERSTAND THE ENTIRE JOB!
