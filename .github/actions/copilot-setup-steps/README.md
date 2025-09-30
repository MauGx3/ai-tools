# Copilot Setup Steps Action

A reusable composite action that encapsulates common setup steps for GitHub Copilot workflows with Jekyll and GitHub Pages.

## Features

- ✅ Checks out the repository code
- ✅ Sets up Ruby with configurable version
- ✅ Enables automatic bundler caching
- ✅ Configures GitHub Pages (with graceful fallback if not enabled)
- ✅ Provides helpful status messages

## Usage

### Basic Usage

```yaml
- name: Setup Copilot Environment
  uses: ./.github/actions/copilot-setup-steps
```

### Advanced Usage

```yaml
- name: Setup Copilot Environment
  uses: ./.github/actions/copilot-setup-steps
  with:
    ruby-version: '3.2'
    bundler-cache: 'true'
    cache-version: '1'
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `ruby-version` | Ruby version to use | No | `3.1` |
| `bundler-cache` | Enable bundler caching | No | `true` |
| `cache-version` | Cache version (increment to invalidate) | No | `0` |

## Outputs

| Output | Description |
|--------|-------------|
| `pages-enabled` | Whether GitHub Pages is enabled (`true` or `false`) |
| `base-path` | Base path for the site (if Pages is enabled) |

## Example Workflow

```yaml
name: Build Jekyll Site

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Setup Environment
        id: setup
        uses: ./.github/actions/copilot-setup-steps
        with:
          ruby-version: '3.1'

      - name: Build with Jekyll
        run: |
          if [[ "${{ steps.setup.outputs.pages-enabled }}" == "true" ]]; then
            bundle exec jekyll build --baseurl "${{ steps.setup.outputs.base-path }}"
          else
            bundle exec jekyll build
          fi
        env:
          JEKYLL_ENV: production
```

## What It Does

1. **Checkout**: Clones your repository code
2. **Ruby Setup**: Installs specified Ruby version with automatic gem caching
3. **Pages Configuration**: Attempts to configure GitHub Pages (continues on failure)
4. **Status Check**: Provides helpful instructions if Pages is not enabled

## Benefits

- 🎯 **Consistency**: Same setup steps across all workflows
- 🔄 **Reusability**: DRY principle for workflow configuration
- 🚀 **Easy Updates**: Change setup in one place, affects all workflows
- 📝 **Clear Documentation**: Self-documenting action with helpful messages

## Troubleshooting

### GitHub Pages Not Enabled

If you see the warning about Pages not being enabled:

1. Go to your repository Settings
2. Navigate to "Pages" in the sidebar
3. Under "Source", select "GitHub Actions"
4. Save the settings
5. Re-run the workflow

### Cache Issues

If you encounter caching issues, increment the `cache-version` input:

```yaml
- uses: ./.github/actions/copilot-setup-steps
  with:
    cache-version: '1'  # Increment this number
```

## License

This action is part of the ai-tools repository and follows the same license (Mozilla Public License 2.0).
