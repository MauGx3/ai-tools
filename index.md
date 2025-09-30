---
layout: default
title: AI Tools Collection
---

# Welcome to AI Tools Collection

This repository contains a comprehensive collection of AI-related tools, prompts, instructions, modes, and documentation for personal use. Everything is organized by category and fully documented for easy reference and deployment.

## Quick Navigation

### 🎯 [Prompts](/prompts/)
Curated collection of AI prompts organized by purpose:
- **Coding**: Development, debugging, code review prompts
- **Writing**: Content creation, editing, documentation prompts
- **Analysis**: Data analysis, research, evaluation prompts
- **Creative**: Brainstorming, ideation, creative writing prompts
- **Productivity**: Task management, planning, optimization prompts

### 📋 [Instructions](/instructions/)
Step-by-step guides and procedures:
- **Setup**: Installation and configuration guides
- **Usage**: How-to guides for tools and workflows
- **Best Practices**: Recommended approaches and methodologies

### 🎛️ [Modes](/modes/)
AI interaction modes and configurations:
- **Development**: Coding and software development modes
- **Research**: Information gathering and analysis modes
- **Documentation**: Technical writing and documentation modes
- **Troubleshooting**: Problem-solving and debugging modes

### 📚 [Documentation](/docs/)
Comprehensive documentation and references:
- **Guides**: Detailed tutorials and walkthroughs
- **References**: Quick reference materials and cheat sheets
- **Examples**: Sample implementations and use cases

### 💭 [Thoughts](/thoughts/)
Personal reflections and experimental ideas:
- **Reflections**: Insights and learnings from AI tool usage
- **Experiments**: Testing new approaches and techniques
- **Ideas**: Future improvements and potential projects

## 🤖 Featured: Starred Repository Scanner

Automatically scan and analyze your GitHub starred repositories with AI:

- **[Getting Started Guide](/docs/guides/starred-repository-scanner/)** - 5-minute quick start
- **[Repository Analyzer Prompt](/prompts/repository-analyzer/)** - AI prompt for repository analysis
- **[Full Instructions](/instructions/starred-repository-scanner/)** - Complete setup and usage guide
- **[Example Analysis](/data/example-starred-repos-analysis.md)** - See the complete workflow in action

**Quick Start:**
```bash
pip install requests
export GITHUB_TOKEN="your_token"
python scripts/scan_starred_repos.py --output data/starred-repos.json
```

## Repository Structure

```
ai-tools/
├── prompts/          # Categorized AI prompts
├── instructions/     # Step-by-step guides
├── modes/           # AI interaction modes
├── scripts/         # Automation scripts (e.g., starred repo scanner)
├── data/            # Output from automation scripts
├── docs/            # Documentation and guides
├── thoughts/        # Personal insights and experiments
├── _layouts/        # Jekyll page layouts
├── _config.yml      # Jekyll configuration
└── Gemfile          # Ruby dependencies
```

## Features

- **GitHub Pages Ready**: Fully configured for GitHub Pages deployment
- **Modern Documentation**: Jekyll-based with responsive design
- **Organized Structure**: Clear categorization for easy navigation
- **Template System**: Consistent layouts for different content types
- **Search Friendly**: SEO optimized with proper metadata
- **Mobile Responsive**: Works well on all device sizes

## Getting Started

1. Browse the collections using the navigation above
2. Each item includes detailed metadata and usage information
3. Use the search functionality to find specific tools or techniques
4. Contribute new content by following the established patterns

## Local Development

To run this site locally:

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000` to view the site.

---

*This repository is licensed under the Mozilla Public License 2.0. See [LICENSE](LICENSE) for details.*