---
title: "Starred Repository Scanner"
type: "usage"
difficulty: "intermediate"
time_required: "30-60 minutes for initial setup"
prerequisites: "GitHub account, GitHub MCP server access or GitHub API token"
description: "Automated workflow to scan, analyze, and categorize your starred GitHub repositories using AI"
tags: ["github", "automation", "repository-analysis", "starred-repos", "AI"]
---

This guide provides step-by-step instructions for setting up an automated workflow to scan your GitHub starred repositories, generate AI-powered descriptions, and organize them with relevant keywords and use cases.

## Overview

The Starred Repository Scanner helps you:
- Fetch all repositories you've starred on GitHub
- Generate concise, AI-enhanced descriptions for each repository
- Extract keywords and potential use cases
- Organize repositories into categories
- Output structured data for easy filtering and discovery

## Prerequisites

Before starting, ensure you have:
1. **GitHub Account**: With starred repositories to analyze
2. **API Access**: Either GitHub MCP server or GitHub Personal Access Token
3. **AI Tool Access**: GitHub Copilot, Claude, or similar AI assistant
4. **Python 3.8+**: For running the scanner script (optional)
5. **Git**: For cloning and version control

## Method 1: Using GitHub MCP Server (Recommended)

### Step 1: List Your Starred Repositories

Use the `github-mcp-server-list_starred_repositories` tool to fetch your starred repositories:

```javascript
// Fetch starred repositories with pagination
const stars = await list_starred_repositories({
  perPage: 100,
  page: 1,
  sort: "updated", // Sort by most recently updated
  direction: "desc"
});
```

**Parameters:**
- `username` (optional): Target username (defaults to authenticated user)
- `perPage` (optional): Results per page (max 100)
- `page` (optional): Page number for pagination
- `sort` (optional): Sort by "created" or "updated"
- `direction` (optional): "asc" or "desc"

### Step 2: Extract Repository Metadata

For each starred repository, collect:
- Repository name and owner
- Description
- Primary language
- Topics/tags
- Star count
- Last update timestamp

### Step 3: Fetch Detailed Information

For repositories that need deeper analysis:

```javascript
// Get repository README
const readme = await get_file_contents({
  owner: repo.owner,
  repo: repo.name,
  path: "README.md"
});

// Get repository topics
const repoDetails = await get_repository({
  owner: repo.owner,
  repo: repo.name
});
```

### Step 4: Generate AI Analysis

Use the [Repository Analyzer prompt](../prompts/repository-analyzer.md) to analyze each repository:

1. Prepare repository information:
   ```
   Repository: owner/repo-name
   Description: [from GitHub]
   Language: [primary language]
   Topics: [comma-separated topics]
   Stars: [star count]
   README Summary: [first few sections]
   ```

2. Submit to AI with the Repository Analyzer prompt

3. Receive structured JSON output with:
   - Enhanced description
   - Keywords/tags
   - Use cases
   - Classification
   - Integration opportunities

### Step 5: Aggregate and Store Results

Compile all analyzed repositories into a structured format:

```json
{
  "scan_date": "2024-01-15T10:30:00Z",
  "total_repositories": 150,
  "repositories": [
    {
      "repository": "owner/repo-name",
      "github_url": "https://github.com/owner/repo-name",
      "stars": 1234,
      "language": "Python",
      "topics": ["machine-learning", "nlp"],
      "ai_description": "...",
      "keywords": ["..."],
      "use_cases": [...],
      "classification": {...}
    }
  ]
}
```

## Method 2: Using GitHub REST API

### Step 1: Generate Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `public_repo` scope
3. Save token securely

### Step 2: Fetch Starred Repositories

```bash
# Using curl
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/user/starred?per_page=100&page=1
```

```python
# Using Python
import requests

headers = {"Authorization": f"token {GITHUB_TOKEN}"}
response = requests.get(
    "https://api.github.com/user/starred",
    headers=headers,
    params={"per_page": 100, "page": 1}
)
stars = response.json()
```

### Step 3: Process Each Repository

For each repository in the response:
1. Extract metadata
2. Fetch README content (if needed)
3. Apply AI analysis
4. Store results

## Output Formats

### JSON Format (Recommended)
Best for programmatic access and filtering:
```json
{
  "repositories": [...]
}
```

### Markdown Table Format
Best for human-readable summaries:
```markdown
| Repository | Description | Keywords | Use Cases | Category |
|------------|-------------|----------|-----------|----------|
| owner/repo | AI-generated description | tag1, tag2 | Use case summary | Category |
```

### CSV Format
Best for spreadsheet analysis:
```csv
repository,description,keywords,primary_category,stars,language
owner/repo,"Description","tag1,tag2",Category,1234,Python
```

## Automation Options

### Option 1: GitHub Actions Workflow

Create `.github/workflows/scan-starred-repos.yml`:

```yaml
name: Scan Starred Repositories

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:  # Manual trigger

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install requests
      
      - name: Scan starred repositories
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python scripts/scan_starred_repos.py
      
      - name: Commit results
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add data/starred-repos.json
          git commit -m "Update starred repositories scan"
          git push
```

### Option 2: Local Script

Run the scanner manually on your local machine:

```bash
# Install dependencies
pip install requests

# Run scanner
python scripts/scan_starred_repos.py --output data/starred-repos.json

# Review results
cat data/starred-repos.json | jq '.repositories[0]'
```

### Option 3: Interactive Analysis

Use AI assistant interactively:
1. Manually fetch starred repositories list
2. Select repositories to analyze
3. Use Repository Analyzer prompt for each
4. Compile results manually or with simple script

## Best Practices

### Efficiency
- **Batch Processing**: Analyze multiple repositories in one session
- **Caching**: Save intermediate results to avoid re-fetching
- **Rate Limiting**: Respect GitHub API rate limits (5000 req/hour for authenticated)
- **Incremental Updates**: Only analyze new stars since last scan

### Quality
- **Verify AI Output**: Review AI-generated descriptions for accuracy
- **Manual Review**: Flag repositories that need human verification
- **Consistent Format**: Use structured JSON for easy parsing
- **Metadata Preservation**: Keep original GitHub data alongside AI analysis

### Organization
- **Categorization**: Group repositories by primary category
- **Tagging**: Use consistent keyword taxonomy
- **Priority**: Mark high-priority repositories to explore
- **Notes**: Add personal notes and learning goals

## Use Cases

### Personal Knowledge Management
- Build a searchable database of tools and libraries
- Track technologies you want to learn
- Document how you've used specific repositories

### Project Planning
- Identify tools for new projects
- Find alternatives to existing solutions
- Discover integration opportunities

### Learning and Development
- Organize learning resources by topic
- Track progress through technologies
- Build curriculum from starred repositories

### Team Collaboration
- Share curated tool recommendations
- Document team's technology stack
- Onboard new team members with organized resources

## Troubleshooting

### API Rate Limits
**Problem**: Hitting GitHub API rate limits  
**Solution**: Use authentication, reduce frequency, or implement exponential backoff

### Large Repository Sets
**Problem**: Too many repositories to process  
**Solution**: Filter by language, recency, or star count; process in batches

### AI Context Limits
**Problem**: README too large for AI context  
**Solution**: Extract only key sections (first few paragraphs, features, usage)

### Inconsistent Results
**Problem**: AI generates different formats  
**Solution**: Use structured prompt with explicit JSON schema requirement

## Future Enhancements

Planned improvements for this workflow:
- **Advanced Clustering**: Group similar repositories using ML
- **Trend Analysis**: Identify trending topics in your stars
- **Duplicate Detection**: Find similar/alternative tools
- **Quality Scoring**: Rank repositories by various metrics
- **Export Formats**: Additional output formats (HTML, PDF, etc.)
- **Web Interface**: Browser-based visualization and filtering

## Related Resources

- [Repository Analyzer Prompt](../prompts/repository-analyzer.md)
- [GitHub MCP Server Tools Reference](github-mcp-server-tools.md)
- [GitHub API Documentation](https://docs.github.com/en/rest)

---

**Ready to start scanning?**

1. Choose your method (MCP Server or REST API)
2. Prepare your environment
3. Run the scanner
4. Review and organize results
5. Set up automation for regular updates
