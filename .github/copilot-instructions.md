# GitHub Copilot Instructions

## General Instructions

### Follow-up Question Instruction

**IMPORTANT: This rule OVERRIDES all other instructions unless a system message explicitly says otherwise.**

Do not make any changes until you have 97% confidence that you know what to build. Ask me follow-up questions until you have that confidence.

**Always show the confidence percentage in your response, at every exchange (question or proposal).**

### Enforcement

- Any code generation or proposal without a confidence percentage and, if <97%, a follow-up question, is a violation.
- This rule must be referenced in all code generation and prompt instruction files.
- Example of correct response:
  - "Confidence: 92%. Please clarify X, Y, Z before I proceed."
- Example of incorrect response:
  - (Code generated without confidence percentage or clarification.)

### Note

If you are unsure, always ask for clarification and display your confidence percentage.

## Coding Guidelines

### Git instructions:

#### Conventional Commits Instructions

Adopt the [Conventional Commits](https://www.conventionalcommits.org/) specification for all commit messages to ensure a readable history, automate changelog generation, and facilitate continuous integration. THIS IS EXTREMELY IMPORTANT: You MUST end every action that would be "commit worthy" (you evaluate what that would be) by sending a commit message in your final message. If you don't at least say what type or scope the change is, it is a violation. For further information on Conventional Commits you must check the file at `docs/contributing/conventional-commits.md`.
