# Copilot Setup Steps Action

This folder contains a reusable composite action that encapsulates common setup steps used by workflows and by the GitHub Copilot coding agent.

Important: To customize the Copilot coding agent's ephemeral development environment you must also include a top-level workflow at `.github/workflows/copilot-setup-steps.yml` in your default branch. That workflow must declare a single job named `copilot-setup-steps`. See GitHub Docs:

- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

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

## Inputs (action)

This composite action exposes inputs to control the included setup steps. These are convenience inputs for reuse in workflows; the Copilot-specific `copilot-setup-steps.yml` workflow may include its own steps instead.

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `ruby-version` | Ruby version to use (for projects using Ruby/Jekyll) | No | `3.1` |
| `bundler-cache` | Enable bundler caching | No | `true` |
| `cache-version` | Cache version (increment to invalidate) | No | `0` |

## Outputs

| Output | Description |
|--------|-------------|
| `pages-enabled` | Whether GitHub Pages is enabled (`true` or `false`) |
| `base-path` | Base path for the site (if Pages is enabled) |

## Example Workflow (using action)

See `example-workflow.yml` in this folder for a full example that uses this action within a normal multi-job GitHub Actions workflow. If your goal is to customize Copilot's environment for agent sessions, create and validate the required workflow file at `.github/workflows/copilot-setup-steps.yml` (this repository already contains one example).

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

## Troubleshooting & notes

- If a Copilot setup step fails (non-zero exit) the remaining steps are skipped and Copilot will continue with the current environment state. Use the Actions UI to iterate and validate your setup steps manually.
- Keep the `copilot-setup-steps.yml` workflow minimal: Copilot only respects `steps`, `permissions`, `runs-on`, `services`, `snapshot`, and `timeout-minutes` on the single job named `copilot-setup-steps`.
- Use repository Environments (Settings → Environments → copilot) to add environment variables or secrets that Copilot will have access to. Prefer secrets for sensitive values.

## License

This action is part of the ai-tools repository and follows the same license (Mozilla Public License 2.0).
