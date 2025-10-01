---
name: feat(integrate): Integrate `repository-analyzer` prompt into repo_recommender
about: Integrate the repository-analyzer prompt so the recommender can use an AI agent to interpret each starred repository
labels: feat, enhancement, ai
---

## Summary

Integrate the existing `repository-analyzer` prompt (see `_prompts/repository-analyzer.md`) into `scripts/repo_recommender.py` so the recommender can invoke an AI agent to interpret each starred repository. The goal is to augment recommendations with structured insights derived from the prompt (purpose, likely use-cases, risk notes, suggested integration points) and include that reasoning in the recommendation report.

## Motivation

We already have a descriptive prompt for analyzing repositories. Embedding that prompt into the recommender enables richer, human-friendly explanations and categorization for recommended repos. This boosts the usefulness of the tool when suggesting repositories for a given project.

## Acceptance Criteria

- [ ] `repo_recommender.py` can optionally run an AI analysis step for each repository using the `repository-analyzer` prompt.
- [ ] Analysis results are stored in each `RepositoryRecommendation.metadata['analysis']` entry and included in the generated report.
- [ ] The feature is opt-in via a CLI flag (`--analyze-repos`) or programmatic parameter.
- [ ] The implementation supports both local LLM/embedding-based agents and a pluggable API-based agent (e.g., OpenAI) with a clear adapter interface.
- [ ] Unit tests cover the analysis step with a mocked agent.
- [ ] Documentation (docs/guides) describes how to enable and configure the analysis step and how to add custom prompts.

## Implementation Notes

- Add a small `agent` abstraction in `scripts/repo_recommender.py` (or a new module `scripts/ai_agent.py`) exposing a simple interface:
  ```py
  class Agent:
      def analyze(self, prompt: str, context: dict) -> dict:
          """Return structured analysis (dict) from prompt + context"""
  ```

- Provide two adapters:
  - `LocalEmbeddingAgent` (uses sentence-transformers embeddings + simple prompt templates or a local LLM if available)
  - `APIAgent` (wrapper for remote LLM APIs; expects API key via env or config)

- The `_prompts/repository-analyzer.md` file should be loaded, formatted with repo metadata (name, description, topics, README preview), and passed to the agent.

- Add `--analyze-repos` and `--analyze-agent` CLI flags to `repo_recommender.py` and `scan_starred_repos.py` recommendation flow. Default: off.

- Augment `RepositoryRecommendation.metadata['analysis']` with fields like `summary`, `use_cases`, `integration_advice`, `risks`, `confidence`.

- Persist analysis in recommendation report. For markdown output, include an "Analysis" subsection per repository.

- Add unit test using pytest that injects a `MockAgent` returning a deterministic analysis to validate wiring.

## Files to change (suggested)

- `scripts/repo_recommender.py` — add agent interface and wiring for analysis, CLI flags, report augmentation
- `scripts/ai_agent.py` — optional new module with adapters
- `scripts/scan_starred_repos.py` — ensure recommendation flow can pass analyze flags and agent config
- `_prompts/repository-analyzer.md` — ensure placeholders documented
- `scripts/requirements.txt` — add optional deps (openai, local LLM libs) to an extras group
- `tests/test_recommender_analysis.py` — new unit tests
- `docs/guides/automatic-output-results-folder.md` — document new flag and usage

## Testing

- Add a `MockAgent` test ensuring analysis appears in `RepositoryRecommendation.metadata['analysis']` and is included in markdown output.
- Integration test: run `scan_starred_repos.py --recommend --analyze-repos --recommend-format markdown --recommend-output results/test.md` using a `MockAgent` to ensure the CLI flow produces analysis in the results file.

## Security & Cost

- Analysis may require external API keys (OpenAI). Document environment variables and rate/cost considerations.
- Provide clear opt-in default to avoid accidental API usage.

## Suggested branch / commit message

Branch: `feat/ai-integrate-repository-analyzer`

Commit message (Conventional Commits):
```
feat(recommender): integrate repository-analyzer prompt via pluggable AI agent

- Add agent abstraction and adapters for local and API agents
- Add CLI flag --analyze-repos and include analysis in reports
- Add tests and documentation
```

---

If you'd like, I can also prepare the initial skeleton code (agent interface, mock adapter, CLI wiring, and tests) and open a PR. Want me to create those scaffold files now?