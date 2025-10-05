# Design overview and the Memory Bank
---
title: "Design and the Memory Bank"
type: "explanation"
layout: "default"
---

This explanation describes the repository design and the Memory Bank concept used for agent workflows.

Purpose
- Explain why instruction files exist, how automated agents use them, and how contributors should think about the Memory Bank.

Key ideas

- Instruction files in `_instructions/` and prompt files in `_prompts/` act as configuration and behavioral guidance for agents. They contain `applyTo` patterns and usage notes so automation can pick the right instructions.
- The Memory Bank (see `.github/instructions/memory-bank.instructions.md`) is a set of markdown files that maintain important project state across sessions: `projectbrief.md`, `productContext.md`, `activeContext.md`, etc.

How agents use these files
- Agents read instruction files with `applyTo` metadata to determine which rules apply to which parts of the repository.
- When making changes, agents are expected to update the Memory Bank files to record decisions and progress.

Design patterns and contributor expectations
- Keep instruction files explicit: state audience, intent, and any constraints.
- Follow the principle of least surprise: changes to instruction files must include a log entry in the Memory Bank where relevant.

Security notes
- Treat all inputs as untrusted. Do not hardcode API keys or secrets in prompt or instruction files. Use environment variables and document them in `docs/reference/repo-structure.md` or the specific instruction file.
