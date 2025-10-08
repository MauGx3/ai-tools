# System Patterns

## Architectural Overview
A content- and instruction-centric repository published via Jekyll (GitHub Pages) + Markdown assets. Python scripts provide automation examples; no central runtime service.

## Core Components
- Documentation (Diátaxis) under `docs/`
- Instruction sets `_instructions/` with `applyTo` selectors
- Prompts `_prompts/`
- Modes `_modes/`
- Automation scripts `scripts/`
- Memory Bank `memory-bank/` (this directory)

## Patterns in Use
| Pattern | Description | Rationale |
|---------|-------------|-----------|
| Diátaxis Docs | Tutorial/How-to/Reference/Explanation segmentation | Cognitive clarity & onboarding efficiency |
| Conventional Commits | Structured commit messages | Automated changelogs & review clarity |
| Memory Bank Files | Persistent context across sessions | Overcome stateless AI limitations |
| Security Instructions Overlay | OWASP-aligned enforcement | Reduce risk of insecure code suggestions |

## Data & State
- No database: Markdown is the primary state medium.
- Generated artifacts (results/) are ephemeral and excluded from versioned knowledge unless curated.

## Extensibility Strategy
Add new instruction sets via `_instructions/` and update Navigation / docs index as needed. Introduce new automation scripts under `scripts/` with isolated dependency footprints.

## Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Instruction drift vs code reality | Enforce updates via PR review checklists |
| Security regression | Central OWASP instruction file referenced in changes |
| Knowledge fragmentation | Mandatory Memory Bank update policy |

## Open Questions
- Should we add automated linting for instruction front matter? (Pending)
- Standard test harness for scripts? (Planned expansion)
