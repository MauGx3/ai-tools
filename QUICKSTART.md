# Quick Start: Starred Repository Scanner

Get started analyzing your GitHub starred repositories with AI in under 5 minutes.

## Prerequisites

- Python 3.8 or higher
- GitHub account with starred repositories
- GitHub Personal Access Token (optional but recommended)

## Step 1: Install Dependencies

```bash
pip install requests
```

That's it! Only one dependency needed.

## Step 2: Get GitHub Token (Optional)

For scanning your own starred repositories:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scope: `public_repo` or `repo`
4. Copy the token

## Step 3: Scan Your Starred Repositories

```bash
# Set your token (recommended)
export GITHUB_TOKEN="your_token_here"

# Basic scan
python scripts/scan_starred_repos.py --output data/starred-repos.json --limit 10

# OR with enhanced descriptions (NEW!)
python scripts/scan_starred_repos.py --enhance-description --limit 10

# OR with full analysis (languages + enhanced descriptions)
python scripts/scan_starred_repos.py --include-languages --enhance-description --limit 10
```

This will scan your first 10 starred repositories and save the results.

**New Features:**
- `--enhance-description`: Automatically generates rich descriptions from metadata
- `--include-languages`: Fetches language breakdown with percentages
- `--include-readme`: Includes README previews for deeper AI analysis

## Step 4: Review the Output

```bash
# View the results
cat data/starred-repos.json | python -m json.tool | head -50

# Or open in your favorite editor
code data/starred-repos.json
```

You'll see structured data like:
```json
{
  "scan_date": "2024-01-15T10:30:00Z",
  "total_repositories": 10,
  "repositories": [
    {
      "repository": "owner/repo-name",
      "description": "Repository description",
      "enhanced_description": "Repository description | Topics: web, api | Built with Python | Popular project with 2,345 stars",
      "language": "Python",
      "languages": {
        "Python": 85.5,
        "JavaScript": 10.2,
        "CSS": 4.3
      },
      "topics": ["topic1", "topic2"],
      "stars": 1234,
      ...
    }
  ]
}
```

## Step 5: Analyze with AI

Now use the [Repository Analyzer prompt](_prompts/repository-analyzer.md) to enhance each repository:

1. Open your AI assistant (GitHub Copilot, Claude, ChatGPT, etc.)
2. Copy the Repository Analyzer prompt
3. For each repository, provide its data
4. Get enhanced descriptions, keywords, and use cases

Example input to AI:
```
Repository: facebook/react
Description: "The library for web and native user interfaces"
Language: JavaScript
Topics: javascript, react, frontend, ui
Stars: 225,000
```

Example output from AI:
- **Enhanced Description**: "React is a declarative, component-based JavaScript library..."
- **Keywords**: javascript-library, ui-framework, component-based, ...
- **Use Cases**: Building Modern Web Applications, Cross-Platform Mobile Development, ...

## Step 6: Organize Your Results

Build a searchable database:
- Group by language
- Filter by use case
- Search by keywords
- Track learning priorities

See [example-starred-repos-analysis.md](data/example-starred-repos-analysis.md) for inspiration.

## Common Commands

```bash
# Scan all your starred repos
python scripts/scan_starred_repos.py --output data/starred-repos.json

# NEW: Scan with enhanced descriptions
python scripts/scan_starred_repos.py --enhance-description --output data/starred-repos.json

# NEW: Comprehensive scan with all features
python scripts/scan_starred_repos.py --enhance-description --include-languages --include-readme --limit 50

# Scan with README previews (slower but more context)
python scripts/scan_starred_repos.py --include-readme --limit 20

# Scan another user's public stars
python scripts/scan_starred_repos.py --username torvalds --limit 50

# Quick test with first 5 repos
python scripts/scan_starred_repos.py --limit 5
```

## Next Steps

1. **Full Scan**: Remove `--limit` to scan all your stars
2. **AI Analysis**: Use the prompt to analyze repositories in batches
3. **Automation**: Set up GitHub Actions for weekly scans (see workflow example)
4. **Organization**: Build your personal repository knowledge base
5. **Sharing**: Share curated lists with your team

## Troubleshooting

### "Authentication required"
- Set `GITHUB_TOKEN` environment variable
- Or use `--token` parameter

### "API rate limit"
- Use authentication (gives 5000 req/hour vs 60)
- Add delays between requests
- Scan in smaller batches

### "Module not found: requests"
- Install: `pip install requests`
- Or: `python -m pip install requests`

## Learn More

- **Full Guide**: [_instructions/starred-repository-scanner.md](_instructions/starred-repository-scanner.md)
- **Prompt Template**: [_prompts/repository-analyzer.md](_prompts/repository-analyzer.md)
- **Example Analysis**: [data/example-starred-repos-analysis.md](data/example-starred-repos-analysis.md)
- **Script Details**: [scripts/README.md](scripts/README.md)

## Support

Questions or issues?
- Check the [full documentation](_instructions/starred-repository-scanner.md)
- Review [example output](data/example-starred-repos-analysis.md)
- Open an issue on GitHub

---

**Happy scanning! 🚀**
