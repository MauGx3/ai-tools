# Scripts

This directory contains automation scripts for various AI-powered workflows.

## Available Scripts

### `scan_starred_repos.py`

Automated scanner for GitHub starred repositories. Fetches metadata and prepares data for AI-based analysis.

**Features:**
- Fetches all starred repositories via GitHub API
- Extracts comprehensive metadata (language, topics, stars, watchers, etc.)
- **NEW: Language breakdown** - Get percentage distribution of languages used
- **NEW: Enhanced description generation** - Automatically generate rich descriptions from metadata
- Optional README preview fetching
- Pagination support for large collections
- Rate limit awareness
- Flexible output formats

**Requirements:**
- Python 3.8+
- `requests` library: `pip install requests`
- GitHub Personal Access Token (optional but recommended)

**Basic Usage:**
```bash
# Set your GitHub token
export GITHUB_TOKEN="your_token_here"

# Scan your starred repositories
python scan_starred_repos.py --output data/starred-repos.json

# Scan with enhanced descriptions
python scan_starred_repos.py --enhance-description --limit 20

# Scan with language breakdown and README previews
python scan_starred_repos.py --include-languages --include-readme --limit 20

# Scan another user's public stars
python scan_starred_repos.py --username octocat --output octocat-stars.json
```

**Command-Line Options:**
- `--output`, `-o`: Output file path (default: stdout)
- `--username`, `-u`: GitHub username (default: authenticated user)
- `--token`, `-t`: GitHub token (or use GITHUB_TOKEN env var)
- `--per-page`: Results per page (default: 100)
- `--max-pages`: Maximum pages to fetch
- `--limit`, `-l`: Maximum repositories to process
- `--include-readme`: Fetch README previews
- `--include-languages`: **NEW** - Fetch language breakdown (percentage distribution)
- `--enhance-description`: **NEW** - Generate enhanced descriptions automatically

**Examples:**

```bash
# Quick test with first 10 repos
python scan_starred_repos.py --limit 10

# Full scan with enhanced descriptions
python scan_starred_repos.py --enhance-description --output enhanced-scan.json

# Comprehensive analysis with all features
python scan_starred_repos.py --include-readme --include-languages --enhance-description --limit 50

# Scan first 50 repos from specific user with language data
python scan_starred_repos.py --username torvalds --include-languages --limit 50

# Use custom token
python scan_starred_repos.py --token ghp_xxxxx --output my-stars.json
```

**Output Format:**
```json
{
  "scan_date": "2024-01-15T10:30:00Z",
  "total_repositories": 150,
  "username": "your_username",
  "repositories": [
    {
      "repository": "owner/repo-name",
      "owner": "owner",
      "name": "repo-name",
      "github_url": "https://github.com/owner/repo-name",
      "description": "Repository description",
      "enhanced_description": "Repository description | Topics: web, javascript | Built with JavaScript | Popular project with 5,234 stars | Framework",
      "language": "Python",
      "languages": {
        "Python": 75.5,
        "JavaScript": 15.2,
        "HTML": 9.3
      },
      "topics": ["tag1", "tag2"],
      "stars": 1234,
      "forks": 56,
      "watchers": 89,
      "open_issues": 12,
      "created_at": "2020-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z",
      "homepage": "https://example.com",
      "license": "MIT",
      "archived": false,
      "fork": false
    }
  ]
}
```

**Next Steps:**

After scanning, use the [Repository Analyzer prompt](../_prompts/repository-analyzer.md) to generate:
- Enhanced descriptions
- Keywords and tags
- Potential use cases
- Category classifications
- Integration opportunities

See the [Starred Repository Scanner guide](../_instructions/starred-repository-scanner.md) for complete workflow instructions.

## Adding New Scripts

When adding new scripts to this directory:

1. **Add shebang**: `#!/usr/bin/env python3` or `#!/usr/bin/env bash`
2. **Make executable**: `chmod +x script_name.py`
3. **Add docstring**: Document purpose and usage
4. **Include examples**: Provide usage examples
5. **Update this README**: Add script to the list above
6. **Handle errors**: Graceful error handling and messages
7. **Support `--help`**: Include helpful command-line help

## Related Documentation

- [Starred Repository Scanner Instructions](../_instructions/starred-repository-scanner.md)
- [Repository Analyzer Prompt](../_prompts/repository-analyzer.md)
- [GitHub MCP Server Tools](../_instructions/github-mcp-server-tools.md)
