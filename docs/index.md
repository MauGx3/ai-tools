---
layout: default
title: Documentation
---

## Documentation

Comprehensive guides, references, and examples for using AI tools effectively.

## 📚 Guides
Detailed tutorials and walkthroughs for various AI tool workflows.

- [Getting Started Guide](guides/getting-started.md) - New to AI tools? Start here
- [Starred Repository Scanner](guides/starred-repository-scanner.md) - Scan and analyze your GitHub starred repositories
- [Prompt Engineering Guide](guides/prompt-engineering.md) - Learn to write effective prompts
- [Workflow Optimization Guide](guides/workflow-optimization.md) - Maximize your productivity
- [Integration Guide](guides/integration.md) - Integrate AI tools into your existing workflow

## 📖 References
Quick reference materials and cheat sheets.

- [Prompt Templates](references/prompt-templates.md) - Ready-to-use prompt templates
- [Model Comparison](references/model-comparison.md) - Compare different AI models
- [Best Practices Checklist](references/best-practices.md) - Quick reference for best practices
- [Troubleshooting Guide](references/troubleshooting.md) - Common issues and solutions

## 💡 Examples
Sample implementations and real-world use cases.

- [Code Review Examples](examples/code-review.md) - AI-assisted code review workflows
- [Documentation Examples](examples/documentation.md) - AI-generated documentation samples
- [Analysis Examples](examples/analysis.md) - Data analysis and research examples
- [Creative Writing Examples](examples/creative-writing.md) - Creative AI applications
- [Starred Repository Analysis](../data/example-starred-repos-analysis.md) - Complete workflow for analyzing GitHub stars

## 🤖 Automation Tools
AI-powered scripts and workflows.

- [Repository Analyzer Prompt](../prompts/repository-analyzer/) - AI prompt for repository analysis
- [Scanner Script Documentation](../scripts/) - Technical details for automation scripts

## Repository Documentation

### Structure Overview
```
ai-tools/
├── prompts/          # Categorized AI prompts
│   ├── coding/       # Development-related prompts
│   ├── writing/      # Content creation prompts
│   ├── analysis/     # Data analysis prompts
│   ├── creative/     # Creative and brainstorming prompts
│   └── productivity/ # Efficiency and planning prompts
├── instructions/     # Step-by-step guides
│   ├── setup/        # Installation and configuration
│   ├── usage/        # How-to guides
│   └── best-practices/ # Recommended approaches
├── modes/           # AI interaction modes
│   ├── development/  # Coding configurations
│   ├── research/     # Research configurations
│   ├── documentation/ # Writing configurations
│   └── troubleshooting/ # Problem-solving configurations
├── docs/            # Documentation and guides
│   ├── guides/       # Detailed tutorials
│   ├── references/   # Quick references
│   └── examples/     # Sample implementations
└── thoughts/        # Personal insights and experiments
    ├── reflections/  # Learning insights
    ├── experiments/  # Testing results
    └── ideas/        # Future projects
```

### Contributing Guidelines

#### Adding New Content

1. **Choose the Right Category**: Determine whether your content is a prompt, instruction, mode, or thought
2. **Use Consistent Naming**: Follow the naming convention `category-specific-name.md`
3. **Include Complete Metadata**: Fill out all relevant front matter fields
4. **Provide Examples**: Include usage examples where applicable
5. **Test Your Content**: Ensure prompts and instructions work as expected

#### Commit Conventions

This project follows [Conventional Commits](contributing/conventional-commits.md) specification:
- Use structured commit messages (e.g., `feat:`, `fix:`, `docs:`)
- Enable automatic changelog generation
- Maintain a readable git history

See the [Conventional Commits Guide](contributing/conventional-commits.md) for details.

#### Content Standards

- **Clear Titles**: Use descriptive, searchable titles
- **Detailed Descriptions**: Explain what the content does and when to use it
- **Proper Categorization**: Use the correct categories and tags
- **Example Usage**: Include practical examples and variations
- **Maintenance**: Keep content updated and relevant

#### File Templates

Each content type has a specific template with required front matter:

- **Prompts**: Include category, description, tags, use_case
- **Instructions**: Include type, difficulty, time_required, prerequisites
- **Modes**: Include mode_type, ai_model, context_length, best_for
- **Thoughts**: Include thought_type, date, status, related_tools

### GitHub Pages Deployment

This repository is configured for automatic GitHub Pages deployment:

1. **Automatic Building**: GitHub Actions builds the site on every push to main
2. **Custom Domain**: Configure in repository settings if desired
3. **SSL/HTTPS**: Automatically enabled for github.io domains
4. **Branch Protection**: Main branch is protected to ensure quality

### Local Development

To work on this repository locally:

```bash
# Clone the repository
git clone https://github.com/MauGx3/ai-tools.git
cd ai-tools

# Install dependencies
bundle install

# Start the development server
bundle exec jekyll serve

# Visit http://localhost:4000 to view the site
```

### Maintenance

- **Regular Updates**: Keep content current and relevant
- **Link Checking**: Ensure internal and external links work
- **Performance**: Monitor site speed and optimize as needed
- **SEO**: Update metadata and descriptions for better discoverability
