# Active Context

## Current Focus
Creating custom agent infrastructure for GitHub Copilot to support specialized workflows. Currently implementing a Cloud Infrastructure Expert agent.

## Recently Completed
- Added structured documentation pages under `docs/`
- Added CONTRIBUTING guide and PR helper script
- Began branch integration for documentation changes (rebasing & conflict resolution in progress previously)
- Memory Bank scaffolding created (this session)
- Created `.github/agents/` directory structure
- Implemented Cloud Infrastructure Expert custom agent (`cloud.agent.md`)

## In Progress
- Finalizing branch rebase & PR (if not already completed externally)
- Planning automation around markdown linting & front matter validation

## Next Steps (Planned)
1. Confirm PR merged for documentation branch.
2. Add markdown link check CI workflow.
3. Introduce pytest scaffold for future script tests.
4. Add Memory Bank update checklist to PR template (future enhancement).

## Decisions (Recent)
- Chose to prioritize explicit Diátaxis segmentation for initial docs set.
- Accepted "theirs" versions of doc files during rebase to unify content (pending rebase completion if not already pushed).
- Established initial Memory Bank file schema exactly per instruction guidelines.
- Created custom agent following VS Code `.agent.md` pattern with YAML frontmatter
- Included comprehensive tools list (search, fetch, githubRepo, bash, view, edit, create) for cloud agent
- Referenced existing instruction files for containerization and Kubernetes best practices

## Pending Questions
- Should we version scripts dependencies with a lock file? (Open)
- Add automated security scanning (e.g., `pip-audit`)? (Planned)

## Collaboration Signals
Contributors should update `progress.md` and this file (Active Context) when shifting focus areas or completing roadmap steps.
