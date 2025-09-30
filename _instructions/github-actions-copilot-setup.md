---
title: "Using the Copilot Setup Steps Action"
type: "usage"
difficulty: "beginner"
time_required: "10-15 minutes"
prerequisites: "Basic GitHub Actions knowledge, existing Jekyll setup"
description: "Guide to using the reusable copilot-setup-steps composite action in your workflows"
---

This guide explains how to use the `copilot-setup-steps` composite action to streamline your GitHub Actions workflows for Jekyll and GitHub Pages projects.

## What is the Copilot Setup Steps Action?

The `copilot-setup-steps` action is a reusable composite action that encapsulates common setup steps needed for Jekyll-based GitHub Pages workflows. It provides a consistent, maintainable way to configure your CI/CD environment.

## Prerequisites

Before using this action, ensure you have:
- A GitHub repository with Jekyll setup
- Basic understanding of GitHub Actions workflows
- A workflow file in `.github/workflows/` directory

## Usage

### Basic Implementation

Add the action to your workflow file (e.g., `.github/workflows/build.yml`):

```yaml
name: Build and Deploy

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Setup Copilot Environment
        uses: ./.github/actions/copilot-setup-steps
      
      - name: Build with Jekyll
        run: bundle exec jekyll build
```

### Advanced Configuration

Customize the action with inputs:

```yaml
- name: Setup Copilot Environment
  id: setup
  uses: ./.github/actions/copilot-setup-steps
  with:
    ruby-version: '3.2'    # Specify Ruby version
    bundler-cache: 'true'  # Enable gem caching
    cache-version: '0'     # Cache invalidation key
```

### Using Outputs

The action provides outputs that you can use in subsequent steps:

```yaml
- name: Setup Copilot Environment
  id: setup
  uses: ./.github/actions/copilot-setup-steps

- name: Build with conditional base path
  run: |
    if [[ "${{ steps.setup.outputs.pages-enabled }}" == "true" ]]; then
      bundle exec jekyll build --baseurl "${{ steps.setup.outputs.base-path }}"
    else
      bundle exec jekyll build
    fi
```

## Features

### Automatic Checkout
The action automatically checks out your repository code, so you don't need a separate checkout step.

### Ruby Environment Setup
- Installs the specified Ruby version
- Configures bundler
- Caches gems for faster workflow runs

### GitHub Pages Configuration
- Attempts to configure GitHub Pages
- Continues gracefully if Pages is not enabled
- Provides helpful instructions for enabling Pages

### Informative Output
- Clear status messages during execution
- Helpful error messages with remediation steps
- Success/failure indicators for each step

## Configuration Options

### Inputs

| Input | Description | Default | Example |
|-------|-------------|---------|---------|
| `ruby-version` | Ruby version to install | `3.1` | `3.2`, `2.7` |
| `bundler-cache` | Enable bundler caching | `true` | `true`, `false` |
| `cache-version` | Cache key version | `0` | `1`, `2`, `3` |

### Outputs

| Output | Description | Usage |
|--------|-------------|-------|
| `pages-enabled` | Whether Pages is configured | `${{ steps.setup.outputs.pages-enabled }}` |
| `base-path` | Base path for Jekyll build | `${{ steps.setup.outputs.base-path }}` |

## Common Use Cases

### Standard Jekyll Build

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/copilot-setup-steps
      - run: bundle exec jekyll build
      - uses: actions/upload-artifact@v4
        with:
          name: site
          path: _site/
```

### Jekyll Build with Tests

```yaml
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/copilot-setup-steps
      
      - name: Build site
        run: bundle exec jekyll build
      
      - name: Test HTML
        run: bundle exec htmlproofer ./_site
```

### Multi-Ruby Testing

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        ruby: ['2.7', '3.0', '3.1', '3.2']
    steps:
      - uses: ./.github/actions/copilot-setup-steps
        with:
          ruby-version: ${{ matrix.ruby }}
      
      - run: bundle exec jekyll build
      - run: bundle exec rake test
```

## Troubleshooting

### Pages Not Enabled

If you see a warning about GitHub Pages not being enabled:

1. Navigate to your repository's Settings
2. Click on "Pages" in the left sidebar
3. Under "Source", select "GitHub Actions"
4. Click "Save"
5. Re-run your workflow

### Cache Issues

If you experience issues with cached gems:

1. Increment the `cache-version` input:
   ```yaml
   - uses: ./.github/actions/copilot-setup-steps
     with:
       cache-version: '1'
   ```

2. Or manually clear the cache:
   - Go to Actions tab in your repository
   - Click "Caches" in the left sidebar
   - Delete the relevant cache entries

### Ruby Version Conflicts

If your build fails due to Ruby version issues:

1. Check your `Gemfile.lock` for the Ruby version requirement
2. Specify the matching version in the action:
   ```yaml
   - uses: ./.github/actions/copilot-setup-steps
     with:
       ruby-version: '3.1'  # Match your Gemfile.lock
   ```

### Bundler Installation Errors

If bundler fails to install gems:

1. Ensure your `Gemfile` is valid
2. Try disabling the cache temporarily:
   ```yaml
   - uses: ./.github/actions/copilot-setup-steps
     with:
       bundler-cache: 'false'
   ```
3. Check the Actions log for specific error messages

## Best Practices

### 1. Pin Ruby Versions
Always specify a Ruby version for consistency:
```yaml
with:
  ruby-version: '3.1'
```

### 2. Use Cache Versioning
Increment cache version when you update dependencies:
```yaml
with:
  cache-version: '1'  # Increment when Gemfile changes significantly
```

### 3. Leverage Outputs
Use action outputs for conditional logic:
```yaml
- id: setup
  uses: ./.github/actions/copilot-setup-steps
- if: steps.setup.outputs.pages-enabled == 'true'
  run: echo "Pages is ready!"
```

### 4. Keep Workflows DRY
Use this action in all Jekyll workflows for consistency:
- Build workflows
- Test workflows  
- Preview workflows
- Deployment workflows

## Benefits

✅ **Reduced Boilerplate**: No need to repeat setup steps in every workflow
✅ **Consistency**: Same environment setup across all workflows
✅ **Maintainability**: Update setup in one place, affects all workflows
✅ **Error Handling**: Built-in error messages and remediation guidance
✅ **Performance**: Automatic caching for faster workflow runs

## Related Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Composite Actions Guide](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action)
- [Jekyll GitHub Pages Setup](jekyll-github-pages-setup.md)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## Contributing

If you find issues or have suggestions for improving this action:
1. Check the existing workflow configurations
2. Test changes locally when possible
3. Document any new inputs or outputs
4. Update this guide with new examples
