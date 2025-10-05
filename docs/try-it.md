# Try it — quick smoke tests
---
title: "Try it"
type: "tutorial"
layout: "default"
---

Run these brief commands (fish shell) to verify basic setup.

```fish
# create and activate a venv (fish)
python -m venv .venv
source .venv/bin/activate.fish

# install script deps
pip install -r scripts/requirements.txt

# run a quick help check
python scripts/repo_recommender.py --help
```

If the help output appears, the basic environment is configured correctly.
