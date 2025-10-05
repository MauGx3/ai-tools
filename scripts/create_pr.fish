#!/usr/bin/env fish
# Helper: create branch, commit docs changes, push and open PR (fish shell)

set BRANCH "feat/docs/diataxis-docs"
set COMMIT_MSG "feat(docs): add Diátaxis documentation (tutorial/how-to/reference/explanation) and CONTRIBUTING guide"

echo "Creating branch $BRANCH"
git checkout -b $BRANCH

echo "Staging docs and contributing files"
git add docs/ CONTRIBUTING.md README.md PULL_REQUEST.md

echo "Committing with message: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo "Pushing branch to origin"
git push -u origin $BRANCH

if type -q gh
    echo "Opening PR with GitHub CLI (gh)"
    gh pr create --fill --title "$COMMIT_MSG" --body "Adds tutorial, how-to, reference, explanation, try-it pages and CONTRIBUTING.md. See docs/ for details."
else
    echo "gh CLI not found. Install https://cli.github.com/ or create a PR in the GitHub web UI for branch: $BRANCH"
end
