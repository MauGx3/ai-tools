# Authoring Guidelines: Prompts, Instructions, and Agent Instructions

> Consolidated standards derived from existing instruction files, experimental workflow notes (`_thoughts/ai-documentation-workflow-experiment.md`), and external best-practice reference (`_thoughts/Prompt Templates Instructions for LLMs  Labelvisor.md`). This serves as a single authoritative Memory Bank entry for content creation consistency.

## 1. Scope & Purpose
Provide uniform rules for creating and maintaining:
- Prompts (`_prompts/`)
- Instruction files (`_instructions/` & nested language/domain sets)
- Agent-oriented instruction overlays (files containing `applyTo:` directives or operational policies)

## 2. Placement & File Types
| Content Type | Location | Purpose | Example |
|--------------|----------|---------|---------|
| Prompt | `_prompts/` | Reusable interaction template | `code-review-assistant.md` |
| General Instruction | `_instructions/` | Cross-cutting rules (security, memory bank) | `security-and-owasp.instructions.md` |
| Domain/Language Instruction | `_instructions/<domain>/` | Language-specific practices | `python/python.instructions.md` |
| Mode Definition | `_modes/` | Interaction configuration/persona | `advanced-coding-assistant.md` |
| Thought / Rationale | `_thoughts/` | Experiments & design reasoning | `ai-documentation-workflow-experiment.md` |
| Memory Bank Entry | `memory-bank/` | Persistent canonical context | This file |

## 3. Naming Conventions
- Kebab-case for filenames (lowercase, hyphen separated).
- Suffix with `.instructions.md` for instruction governance files.
- Use concise verbs/nouns: `refactoring-python.instructions.md` not `python-refactoring-guide-v1.md`.
- Avoid dates in filenames—use front matter or internal metadata.

## 4. Metadata & Front Matter
When applicable include (YAML or pseudo-front matter):
```
---
title: "Clear Title"
type: "prompt|how-to|policy|best-practices|reference|explanation"
difficulty: "beginner|intermediate|advanced" (if relevant)
audience: "maintainers|contributors|agents"
applyTo: ["glob or path patterns"]   # only for agent-scope instructions
updated: 2025-10-08
---
```
Required minimal fields per type:
| Type | Required | Optional |
|------|----------|----------|
| Prompt | title, purpose | examples, tags |
| Instruction | title, type | applyTo, rationale, risks |
| Agent Policy | title, applyTo | escalation_path, safety, validation |

## 5. `applyTo` Best Practices
- Keep patterns specific (e.g., `scripts/*.py` not `**/*.py` unless intentionally global).
- Group related patterns; avoid duplicating across files—prefer one source of truth per scope.
- Document exclusions if non-obvious ("Not applied to generated test fixtures").
- Periodically audit for dead patterns after restructures.

## 6. Prompt Authoring Principles
Derived from experimental workflow + external template guidance:
| Principle | Description | Example |
|-----------|-------------|---------|
| Clear Objective | State the task in one decisive sentence | "Summarize repository architecture..." |
| Structured Sections | Use headings: Context, Task, Constraints, Output | Improves scanability |
| Explicit Constraints | Token, style, format specs reduce ambiguity | "Limit to 200 words" |
| Provide Examples | Few-shot guidance clarifies expectations | Example input/output blocks |
| Role / Persona | Align model behavior | "You are a senior security reviewer" |
| Deterministic Format | Enforce JSON/schema when machine-parsed | JSON schema snippet |
| Progressive Refinement | Encourage iterative improvement loops | Step-by-step refinement prompt |
| Avoid Ambiguity | Eliminate vague adjectives | Replace "optimize" with measurable target |

Anti-patterns:
- Overloaded instructions (too many unrelated tasks)
- Hidden assumptions
- Underspecified output format

## 7. Instruction File Authoring Principles
- One conceptual domain per instruction file (separation of concerns).
- Lead with intent & scope boundaries.
- Provide decision criteria (when to apply vs when not to).
- Include risk table for security- or performance-sensitive domains.
- Cross-link related instructions ("See also: refactoring-python.instructions.md").
- Maintain changelog snippet if file drives critical process.

## 8. Agent Instruction Guidelines
- Be explicit about REQUIRED vs OPTIONAL behaviors.
- Define escalation triggers (e.g., "Ask user if confidence < 97%")—reinforces current repo policy.
- Provide validation checkpoints (build, lint, tests, security scan).
- Include safeguarding rules (no secrets, no network exfiltration, confirm destructive ops).
- Specify output formatting requirements (e.g., heading levels, fenced code rules) to ensure predictability.

Checklist for agent-facing instruction files:
- [ ] Scope & intent
- [ ] applyTo patterns
- [ ] Required success criteria
- [ ] Error / fallback strategies
- [ ] Security constraints
- [ ] Update policy (when file must be revised)

## 9. Security & Compliance Highlights
From `security-and-owasp.instructions.md` principles (summarized):
- Never commit secrets / API keys.
- Use parameterization (avoid injection risks) in code examples.
- Validate & sanitize untrusted input paths.
- Reference OWASP Top 10 where relevant (e.g., for auth, injection, sensitive data).
- Encourage least privilege in examples (scoped tokens, minimal permissions).

## 10. Review & PR Checklist (Content-Specific)
| Item | Prompts | Instructions | Agent Instructions |
|------|---------|-------------|--------------------|
| Clear objective | ✓ | ✓ | ✓ |
| Proper metadata | ✓ | ✓ | ✓ |
| Examples (if needed) | ✓ | Optional | Optional |
| applyTo patterns valid | N/A | If scoped | ✓ |
| Security considerations | ✓ | ✓ | ✓ |
| Links to related docs | Optional | Recommended | Recommended |
| Formatting/style passes | ✓ | ✓ | ✓ |
| No secrets or PII | ✓ | ✓ | ✓ |

## 11. Quality Metrics (Initial Baselines)
- Acceptance rate of new prompts without revision > 70%.
- Instruction drift incidents per quarter: target 0 (tracked via PR review notes).
- Time-to-onboard (from clone to first successful script run): < 10 minutes.
- Review turnaround for instruction changes: < 24h.

## 12. Common Failure Modes & Remedies
| Failure | Symptom | Remedy |
|---------|---------|--------|
| Ambiguous prompt | Inconsistent model outputs | Add explicit format & constraints |
| Bloated instruction file | Hard to apply selectively | Split by domain / concern |
| Stale applyTo patterns | Instructions not triggered | Audit after structural changes |
| Untracked rationale changes | Confusion in future PRs | Log in Memory Bank (activeContext) |

## 13. Future Enhancements
Planned improvements:
- Lint tool to validate front matter & applyTo existence in repo.
- Automated dead pattern detector (flags unmatched applyTo globs).
- CI job: markdown link + schema validation for structured prompt JSON examples.
- Semantic diff annotator for instruction changes (summarize added/removed rules).

## 14. Maintenance Policy
- Update this file whenever new content types or validation tooling is introduced.
- Reference it from CONTRIBUTING and PR templates for visibility.
- Log major revisions in `progress.md` and `activeContext.md`.

## 15. Source References
- `_thoughts/ai-documentation-workflow-experiment.md` (workflow, iterative prompting)
- `_thoughts/Prompt Templates Instructions for LLMs  Labelvisor.md` (template structuring & clarity principles)
- Existing instruction files in `_instructions/` & `.github/instructions/`

---
**Status:** Authoritative baseline established (2025-10-08). Future updates must preserve section numbering for stable referencing.
