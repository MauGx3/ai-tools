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

## Custom agents & instruction files

If you plan to reuse guidance across the repo or need deterministic, automated behavior (for example, standardized code-review checks), prefer creating a short instruction file rather than relying on ad-hoc prompts.

- Instruction files: put reusable, machine-oriented guidance in `_instructions/`. Keep them short, focused, and include frontmatter with at least `title` and `applyTo` globs so they are discoverable and targetable.
- VS Code custom agents: when you need an interactive persona (planner, implementer, reviewer) with specific tool access or handoffs, consider adding a `.agent.md` that references instruction files instead of embedding long prompts in the agent body.
- Examples & determinism: include a tiny example of expected input and expected output/feedback in the instruction file — this helps automated workflows and reviewers understand the intended behavior.

References:

- `_thoughts/third-party/agents/Custom agents in VS Code.md`
- `_thoughts/third-party/instructions/Unlocking the full power of Copilot code review Master your instructions files - The GitHub Blog.md`
