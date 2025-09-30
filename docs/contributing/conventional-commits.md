---
layout: default
title: Conventional Commits Guide
---

# Conventional Commits Guide

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification to ensure a readable git history and enable automatic changelog generation.

## Commit Message Format

Every commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Type

The type must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Scope

The scope is optional and provides additional contextual information:

- `prompts`: Changes to AI prompts
- `instructions`: Changes to instruction files
- `modes`: Changes to mode configurations
- `docs`: Changes to documentation
- `ci`: Changes to CI/CD workflows
- `config`: Changes to configuration files

### Description

The description is a short summary of the code changes:

- Use the imperative, present tense: "change" not "changed" nor "changes"
- Don't capitalize the first letter
- No dot (.) at the end
- Keep it under 72 characters

### Examples

#### Feature Addition
```
feat(prompts): add code review prompt for Python
```

#### Bug Fix
```
fix(ci): correct workflow syntax error
```

#### Documentation
```
docs: update installation instructions
```

#### Breaking Change
```
feat(config)!: change Jekyll version to 4.0

BREAKING CHANGE: Jekyll 4.0 requires Ruby 2.5 or higher
```

## Automatic Changelog Generation

The changelog is automatically generated from conventional commits using [git-cliff](https://git-cliff.org/).

### On Release

When you create a new version tag (e.g., `v1.0.0`), the release workflow will:

1. Generate a changelog entry for the new version
2. Update `CHANGELOG.md`
3. Create a GitHub release with the changelog
4. Commit the updated changelog back to the main branch

### Manual Generation

To manually trigger changelog generation:

1. Go to Actions → Generate Changelog
2. Click "Run workflow"
3. Select the branch
4. Optionally specify a tag

This will create a pull request with the updated changelog.

## Configuration

The changelog generation is configured in `.cliff.toml`. This file controls:

- Changelog format and templates
- Commit grouping and categorization
- Filters for what gets included
- Sort order

## Best Practices

1. **One Commit = One Logical Change**: Keep commits focused and atomic
2. **Write Clear Descriptions**: Make it easy to understand what changed and why
3. **Use Scopes Consistently**: Help readers quickly identify which part of the project changed
4. **Document Breaking Changes**: Always use `!` and add a footer for breaking changes
5. **Link Issues**: Reference issue numbers in the footer (e.g., `Closes #123`)

## Resources

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [git-cliff Documentation](https://git-cliff.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
