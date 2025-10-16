# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### ⛰️  Features

- *(ci)* Add copilot-setup-steps composite action
- *(ci)* Add codeql action
- *(instructions)* Add copilot-instructions.md for automated code review
- *(instructions)* Add new copilot-instructions file
- *(instructions)* Add new copilot-instructions file
- *(ci)* Add copilot-setup-steps composite action
- *(changelog)* Add automatic changelog generation
- *(changelog)* Add automatic changelog generation following Conventional Commits
- *(prompts)* Add personal-finance prompt
- *(prompts)* Add personal-finance prompt (#3)
- Add dotenv loading and task for installing python-dotenv
- Added starred repos information
- Add alpha GitHub Copilot instructions for the repo
- Implement AI-powered repository recommendation system and enhance starred repo scanner
- *(scripts)* Add automatic timestamped output to results/ folder
- *(actions)* Add Copilot setup steps workflow for automated environment setup
- Comprehensive testing and coding guidelines for Python projects
- Enhance starred repos file handling and output reporting
- Restore comprehensive code review best practices and guidelines
- Add gitkeep
- Add initial links to smithery.md
- Add performance improvement instructions for Python code
- Add refactoring guidelines for Python code
- Add comprehensive context engineering strategies for AI agents
- Add initial content for &INGEST.md with explanations and boilerplate prompts
- Add Copilot setup steps workflow for Python environment
- Add comprehensive MCP tools instructions and usage patterns
- Add Starred Repository Scanner guide for automated repository analysis
- Add initial draft of Python Agents documentation
- Add mcp_servers documentation file
- Add guidelines for writing effective Copilot instructions
- *(instructions)* Update Python coding guidelines and conventions for clarity and modern practices
- *(instructions)* Add global collaboration rules and coding guidelines
- *(instructions)* Enhance Copilot collaboration guidelines and structure
- *(instructions)* Add accessibility specialist guidelines for WCAG compliance
- *(instructions)* Add agent-expert guidelines for creating and optimizing Claude Code agents
- *(instructions)* Add api-documenter guidelines for creating OpenAPI specifications and SDKs
- *(instructions)* Add api-security-audit guidelines for conducting security audits on REST APIs
- *(instructions)* Add guidelines for refactoring `.instructions.md` files
- *(instructions)* Add structured code review playbook for enhanced review processes
- Add comprehensive guides and techniques for GitHub Copilot usage
- Add ccpm files
- *(tests)* Add Playwright configuration and initial site tests
- *(instructions)* Add comprehensive secure coding guidelines based on OWASP Top 10
- *(workflow)* Enhance dependency installation logic in Jekyll GitHub Pages workflow
- *(docs)* Add getting-started tutorial
- *(docs)* Add how-to for prompts/instructions
- *(docs)* Add reference for repo structure
- *(docs)* Add design explanation and memory bank overview
- *(docs)* Add try-it quick tests
- *(docs)* Add docs index/landing page
- *(docs)* Add Diátaxis documentation (tutorial/how-to/reference/explanation) and CONTRIBUTING guide
- *(docs)* Add Diátaxis documentation and CONTRIBUTING guide (#27)
- Create personal-finance.prompt.yml
- Add Contributor Covenant Code of Conduct
- Create SECURITY.md for security policy and reporting
- Update issue templates
- Add comprehensive documentation for AI Tools Collection and Memory Bank
- *(tests)* Add WIP test runner prompts for Playwright integration
- *(instructions)* Add brainstorming facilitator guide with structured ideation techniques
- *(prompts)* Add instruction generation guide for AI coding agents
- Add comprehensive guidelines for Specification-Driven Workflow v1, SQL development, task implementation, TaskSync V4, and TypeScript 5 ES2022 standards
- Add comprehensive guidelines for Specification-Driven Workflow v1, SQL development, task implementation, TaskSync V4, and TypeScript 5/ES2022 standards
- Add GitHub Actions workflows for AutoPR and triggers configuration

### 🐛 Bug Fixes

- *(instructions)* Change filename and paths
- *(docs)* Move docs.md to docs/index.md and fix broken links
- *(ci)* Use default branch instead of main
- *(docs)* Change number of pages
- *(config)* Use dynamic year for footer
- *(dependabot)* Dependabot.yml formatting issues
- Typo
- *(ci)* Update git-cliff-action from v3 to v4
- Improve import error messages for numpy, sentence-transformers, and scikit-learn
- Add .venv to .gitignore to prevent tracking of virtual environment files
- Refine Python coding style guidelines for clarity and consistency
- Improve clarity and consistency in refactoring guidelines
- *(ci)* Make npm install resilient when package-lock.json is absent
- Remove references to confidence
- Add index.md to resolve GitHub Pages 404 error
- Add index.md to resolve GitHub Pages 404 error (#29)
- Update applyTo syntax for consistency in AI prompt engineering guidelines
- Correct typo in instruction source path and improve formatting in instruction generation guidelines
- Correct formatting issues and ensure consistent markdown compliance across documentation files
- Improve formatting and structure in workflow files; ensure proper installation command for jq and add validation job in triggers
- Update collaborator check logic and improve error handling; upgrade actions/checkout and AutoPR versions
- Add check for OPENAI_API_KEY in AutoPR workflow to ensure it is set before execution

### 📚 Documentation

- Enhance contributing documentation
- *(changelog)* Update changelog
- *(changelog)* Update changelog (#20)
- Clarify .gitignore entry for environment variables
- *(changelog)* Update changelog
- *(changelog)* Update changelog (#21)
- *(changelog)* Update changelog
- *(changelog)* Update changelog (#25)
- Add CONTRIBUTING guide
- Add PULL_REQUEST helper
- Update README with docs links
- *(changelog)* Update changelog
- *(changelog)* Update changelog (#30)
- *(memory-bank)* Add consolidated authoring guidelines and task record (TASK002)
- *(copilot)* Concise repo-specific Copilot instructions (read Memory Bank first)
- Fix markdown compliance issues in core files
- Add initial Awesome AI Tools documentation with curated resources
- Update README and example workflow for Copilot setup steps; add workflow file for GitHub Actions

### 🚜 Refactor

- Update copilot-instructions.md based on review feedback
- Enhance code review instructions with industry research and MCP tools reference
- Make instructions server-agnostic and add comprehensive code review guide
- Delete repos directory
- Clean up code formatting and improve readability in repo_recommender.py
- Remove `repos` folder

### 🎨 Styling

- Format code for better readability and consistency

### ⚙️ Miscellaneous Tasks

- *(issues)* Publish feature issue for repository-analyzer integration
- Remove outdated GitHub Actions Copilot setup guide
- Remove GitHub MCP Server Tools reference document
- Remove unused files
- Change file structure
- Change file structure
- *(ci)* Trigger workflow run to validate Playwright tests (no functional changes)
- *(scripts)* Add create_pr helper script
- Delete scripts/create_pr.fish
- Update documentation files with frontmatter and improve formatting
- Remove outdated PULL_REQUEST and personal-finance.prompt.yml files to streamline project structure

### ◀️ Revert

- V2 instructions to v1

<!-- generated by git-cliff -->
