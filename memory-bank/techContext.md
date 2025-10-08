# Tech Context

## Languages & Tooling
- Markdown + Jekyll (site publishing, GitHub Pages)
- Python 3.10+ scripts (automation & examples)
- Shell (fish) helper scripts

## Key Dependencies
| Area | Tool | Purpose |
|------|------|---------|
| Site | Jekyll (Gemfile) | Static docs site generation |
| Python | Standard library + listed in `scripts/requirements.txt` | Script execution |
| Testing | Playwright (E2E) | Site / workflow validation |

## Environment Assumptions
- Local dev: macOS/Linux with Ruby & Bundler installed for site
- Python virtualenv recommended for scripts
- Secrets provided via environment variables (never committed)

## Repository Conventions
- `applyTo` instruction metadata guides agent file targeting
- Conventional Commits regulate semantic history
- Memory Bank updated upon significant conceptual or structural change

## Performance Considerations
Minimal—static generation + lightweight scripts. Optimize clarity over micro-optimizations at this stage.

## Security Practices
- Follow `security-and-owasp.instructions.md`
- Deny-by-default approach to secret usage
- Avoid hardcoding tokens; use `.env` (gitignored) or environment

## Tooling Roadmap (Planned)
- Add markdown lint / link check CI
- Script unit tests (pytest) scaffolding
- Automated validation of instruction front matter
