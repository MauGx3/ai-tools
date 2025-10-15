---
title: "Create a Pull Request for the documentation changes"
---

## Create a Pull Request for the documentation changes

Recommended branch name:

feat/docs/diataxis-docs

Conventional commit message (use as-is):

```
feat(docs): add Diátaxis documentation (tutorial/how-to/reference/explanation) and CONTRIBUTING guide
```

Fish-shell commands (run from repository root):

```fish
# create and switch to a new branch
git checkout -b feat/docs/diataxis-docs

# stage the changes (adjust paths if you added/edited more files)
git add docs/ CONTRIBUTING.md README.md PULL_REQUEST.md scripts/create_pr.fish

# commit
git commit -m "feat(docs): add Diátaxis documentation (tutorial/how-to/reference/explanation) and CONTRIBUTING guide"

# push the branch to origin
git push -u origin feat/docs/diataxis-docs

# open a PR using GitHub CLI (interactive)
gh pr create --fill --title "feat(docs): add Diátaxis documentation and CONTRIBUTING guide" --body "Adds tutorial, how-to, reference, explanation, try-it pages and CONTRIBUTING.md. See docs/ for details."
```

If you don't have the GitHub CLI installed, create the PR in the GitHub UI after pushing the branch. The PR title and body above are recommended.

Notes
- Review the changes locally before pushing: `git status`, `git diff --staged`.
- If you prefer a different branch name, adjust the commands accordingly.
