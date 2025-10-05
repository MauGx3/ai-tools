# How to add a prompt or instruction
---
title: "Add a prompt or instruction"
type: "how-to"
layout: "default"
---

This how-to recipe explains how to add a new prompt, instruction, or Diátaxis-style instruction file and prepare a PR.

Goal
- Add a new prompt or instruction file that will be picked up by contributors and automated agents.

Where to add files
- Prompts live in `_prompts/` (top-level). Use a clear filename and a short header describing its intent.
- Instruction files live in `_instructions/` and often include YAML front-matter or a short header describing applyTo patterns.

Naming and conventions
- Use kebab-case for filenames, e.g. `my-new-prompt.md`.
- Include metadata at the top: purpose, audience, and any `applyTo` lines (see existing files in `_instructions/` for examples).

Steps

1. Create the new file in the appropriate folder

2. Add a brief header with intent and target audience

```markdown
# My New Prompt

Purpose: Assist with X
Audience: novice developers

...prompt content...
```

3. Run a quick lint or manual check
- Ensure there are no trailing tabs, and that the prompt follows the project's style.

4. Add tests or a smoke-check (optional)
- If your prompt relies on a script or example, add a small example under `scripts/` or `data/` that demonstrates it.

5. Open a PR
- Use a descriptive Conventional Commit message, e.g. `feat(prompts): add my-new-prompt.md`.
- In the PR description, include: purpose, example usage, and any security considerations.

Security checklist
- Never include secrets or credentials in prompt files.
- If a prompt requires external API keys, document expected environment variables and mark them in the instructions (see `security-and-owasp.instructions.md`).

PR checklist (suggested)
- [ ] File added to the correct folder
- [ ] Short purpose and audience described
- [ ] No credentials or secrets
- [ ] Follows naming conventions
- [ ] Proposed commit message follows Conventional Commits
