---
title: "MCP Tools Reference for Code Review"
type: "usage"
difficulty: "intermediate"
time_required: "10 minutes"
prerequisites: "Understanding of MCP (Model Context Protocol) and GitHub API"
description: "Comprehensive reference for MCP tools available for automated code review tasks"
tags: ["MCP", "tools", "GitHub", "automation"]
categories: ["reference"]
---

This reference guide lists all available MCP tools for conducting automated code reviews, with usage examples and best practices.

## GitHub Pull Request Tools

### Get Pull Request Details
**Tool**: `github-mcp-server-get_pull_request`

**Purpose**: Retrieve comprehensive PR information including title, description, author, labels, and status.

**Parameters**:
- `owner` (required): Repository owner username or organization
- `repo` (required): Repository name
- `pullNumber` (required): Pull request number

**Usage**:
```json
{
  "tool": "github-mcp-server-get_pull_request",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "pullNumber": 123
  }
}
```

**Use Cases**:
- Initial review setup: Get PR context, linked issues, and labels
- Check review status and approvals
- Understand the scope and purpose of changes

### Get Pull Request Diff
**Tool**: `github-mcp-server-get_pull_request_diff`

**Purpose**: Retrieve the complete diff of all changes in the pull request.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `pullNumber` (required): Pull request number

**Usage**:
```json
{
  "tool": "github-mcp-server-get_pull_request_diff",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "pullNumber": 123
  }
}
```

**Use Cases**:
- Analyze line-by-line changes
- Identify added, removed, and modified code
- Review context around changes

### Get Pull Request Files
**Tool**: `github-mcp-server-get_pull_request_files`

**Purpose**: List all files modified in the pull request with change statistics.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `pullNumber` (required): Pull request number
- `page` (optional): Page number for pagination
- `perPage` (optional): Results per page (max 100)

**Usage**:
```json
{
  "tool": "github-mcp-server-get_pull_request_files",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "pullNumber": 123,
    "perPage": 100
  }
}
```

**Use Cases**:
- Get overview of changed files
- Identify file types and change magnitude
- Prioritize review order (e.g., security-sensitive files first)

### Get Pull Request Reviews
**Tool**: `github-mcp-server-get_pull_request_reviews`

**Purpose**: Retrieve all reviews submitted for the pull request.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `pullNumber` (required): Pull request number

**Usage**:
```json
{
  "tool": "github-mcp-server-get_pull_request_reviews",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "pullNumber": 123
  }
}
```

**Use Cases**:
- Check existing review feedback
- Avoid duplicate comments
- Build on previous reviewer suggestions

### Get Pull Request Review Comments
**Tool**: `github-mcp-server-get_pull_request_review_comments`

**Purpose**: Retrieve detailed review comments on specific code lines.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `pullNumber` (required): Pull request number

**Usage**:
```json
{
  "tool": "github-mcp-server-get_pull_request_review_comments",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "pullNumber": 123
  }
}
```

**Use Cases**:
- Review existing inline comments
- Identify discussed issues
- Continue conversations on specific code sections

## File Content Tools

### Get File Contents
**Tool**: `github-mcp-server-get_file_contents`

**Purpose**: Retrieve the full content of a file from the repository.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `path` (required): Path to the file
- `ref` (optional): Branch, tag, or commit SHA

**Usage**:
```json
{
  "tool": "github-mcp-server-get_file_contents",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "path": "src/components/Button.tsx",
    "ref": "feature-branch"
  }
}
```

**Use Cases**:
- Get complete file context for better understanding
- Review imports and dependencies
- Understand how changed code fits in the file structure

### Get Commit Details
**Tool**: `github-mcp-server-get_commit`

**Purpose**: Retrieve detailed information about a specific commit.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `sha` (required): Commit SHA
- `include_diff` (optional): Include diff in response (default: true)

**Usage**:
```json
{
  "tool": "github-mcp-server-get_commit",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "sha": "abc123def456",
    "include_diff": true
  }
}
```

**Use Cases**:
- Review individual commits in the PR
- Understand commit history and evolution
- Check commit messages and authorship

## Search Tools

### Search Code
**Tool**: `github-mcp-server-search_code`

**Purpose**: Search for code patterns across the repository or all of GitHub.

**Parameters**:
- `query` (required): Search query with GitHub code search syntax
- `sort` (optional): Sort field
- `order` (optional): Sort order (asc/desc)
- `page` (optional): Page number
- `perPage` (optional): Results per page (max 100)

**Usage**:
```json
{
  "tool": "github-mcp-server-search_code",
  "parameters": {
    "query": "repo:organization/repository-name language:python def process_payment",
    "perPage": 10
  }
}
```

**Use Cases**:
- Find similar implementations in the codebase
- Identify patterns for consistency
- Locate related functions or utilities

### Search Issues
**Tool**: `github-mcp-server-search_issues`

**Purpose**: Search for related issues in the repository.

**Parameters**:
- `query` (required): Search query
- `sort` (optional): Sort field
- `order` (optional): Sort order
- `page` (optional): Page number
- `perPage` (optional): Results per page (max 100)

**Usage**:
```json
{
  "tool": "github-mcp-server-search_issues",
  "parameters": {
    "query": "repo:organization/repository-name is:issue authentication bug",
    "perPage": 10
  }
}
```

**Use Cases**:
- Find related issues or bug reports
- Check if reported problems are known
- Understand context for changes

## Workflow Tools

### List Workflow Runs
**Tool**: `github-mcp-server-list_workflow_runs`

**Purpose**: List CI/CD workflow runs for the repository.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `workflow_id` (required): Workflow ID or filename
- `branch` (optional): Filter by branch
- `status` (optional): Filter by status (queued, in_progress, completed)

**Usage**:
```json
{
  "tool": "github-mcp-server-list_workflow_runs",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "workflow_id": "ci.yml",
    "status": "completed"
  }
}
```

**Use Cases**:
- Check CI/CD test results
- Verify build status
- Review automated checks

### Get Job Logs
**Tool**: `github-mcp-server-get_job_logs`

**Purpose**: Retrieve logs from workflow jobs.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `job_id` (optional): Specific job ID
- `run_id` (optional): Workflow run ID
- `failed_only` (optional): Get only failed job logs
- `tail_lines` (optional): Number of lines from end (default: 500)

**Usage**:
```json
{
  "tool": "github-mcp-server-get_job_logs",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "run_id": 12345,
    "failed_only": true,
    "tail_lines": 100
  }
}
```

**Use Cases**:
- Investigate test failures
- Review linting errors
- Check build errors

## Security Tools

### List Code Scanning Alerts
**Tool**: `github-mcp-server-list_code_scanning_alerts`

**Purpose**: Retrieve code scanning alerts (e.g., from CodeQL).

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `state` (optional): Alert state (open, closed, dismissed, fixed)
- `severity` (optional): Filter by severity

**Usage**:
```json
{
  "tool": "github-mcp-server-list_code_scanning_alerts",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "state": "open",
    "severity": "high"
  }
}
```

**Use Cases**:
- Check for security vulnerabilities
- Review SAST findings
- Identify potential security issues

### List Secret Scanning Alerts
**Tool**: `github-mcp-server-list_secret_scanning_alerts`

**Purpose**: Retrieve secret scanning alerts for exposed credentials.

**Parameters**:
- `owner` (required): Repository owner
- `repo` (required): Repository name
- `state` (optional): Alert state
- `secret_type` (optional): Filter by secret type

**Usage**:
```json
{
  "tool": "github-mcp-server-list_secret_scanning_alerts",
  "parameters": {
    "owner": "organization",
    "repo": "repository-name",
    "state": "open"
  }
}
```

**Use Cases**:
- Detect exposed API keys or credentials
- Verify no secrets in the PR
- Check for leaked sensitive data

## Best Practices for Tool Usage

### Efficient Review Workflow

1. **Initial Context Gathering**:
   ```
   get_pull_request → get_pull_request_files → get_pull_request_diff
   ```

2. **Deep File Analysis** (when needed):
   ```
   get_file_contents → search_code (for similar patterns)
   ```

3. **Security Check**:
   ```
   list_code_scanning_alerts → list_secret_scanning_alerts
   ```

4. **CI/CD Validation**:
   ```
   list_workflow_runs → get_job_logs (if failures)
   ```

5. **Context from History**:
   ```
   get_pull_request_reviews → get_pull_request_review_comments
   ```

### Tool Selection Guidelines

**For Small PRs (< 10 files)**:
- Use `get_pull_request_diff` for complete context
- Minimal need for individual file retrieval

**For Large PRs (> 20 files)**:
- Use `get_pull_request_files` to prioritize
- Selectively use `get_file_contents` for critical files
- Consider requesting PR to be split

**For Security-Sensitive Changes**:
- Always run `list_code_scanning_alerts`
- Check `list_secret_scanning_alerts`
- Review authentication/authorization code manually

**For Complex Logic Changes**:
- Use `search_code` to find similar patterns
- Use `get_file_contents` for full context
- Review related test files

### Rate Limiting and Performance

- Batch related requests when possible
- Cache file contents for repeated access
- Use pagination efficiently for large result sets
- Respect GitHub API rate limits (5000/hour for authenticated users)
- Use conditional requests (ETags) to save quota

### Error Handling

- Handle 404 errors gracefully (file might be deleted)
- Retry on 5xx errors with exponential backoff
- Check permissions before attempting operations
- Validate parameters before making requests

## Common Patterns

### Pattern: Comprehensive PR Review
```javascript
// 1. Get PR overview
const pr = await get_pull_request(owner, repo, pullNumber);

// 2. Get all changed files
const files = await get_pull_request_files(owner, repo, pullNumber);

// 3. Get the diff
const diff = await get_pull_request_diff(owner, repo, pullNumber);

// 4. Check security alerts
const securityAlerts = await list_code_scanning_alerts(owner, repo, 'open');

// 5. Check CI/CD status
const workflows = await list_workflow_runs(owner, repo, workflowId);

// 6. For critical files, get full context
for (const file of criticalFiles) {
  const content = await get_file_contents(owner, repo, file.path);
  // Analyze content...
}
```

### Pattern: Security-Focused Review
```javascript
// 1. Check for exposed secrets
const secrets = await list_secret_scanning_alerts(owner, repo, 'open');

// 2. Check code scanning results
const codeAlerts = await list_code_scanning_alerts(owner, repo, 'open', 'high');

// 3. Search for security-sensitive patterns
const sqlQueries = await search_code(`repo:${owner}/${repo} "execute(" OR "query("`);

// 4. Review authentication changes
const authFiles = files.filter(f => f.filename.includes('auth'));
```

### Pattern: Performance Review
```javascript
// 1. Identify database-related changes
const dbFiles = files.filter(f => 
  f.filename.includes('model') || 
  f.filename.includes('query') ||
  f.filename.includes('repository')
);

// 2. Get full context for DB changes
for (const file of dbFiles) {
  const content = await get_file_contents(owner, repo, file.filename);
  // Check for N+1 queries, missing indexes, etc.
}

// 3. Check if tests verify performance
const testFiles = files.filter(f => f.filename.includes('test'));
```

## Integration with Review Instructions

This MCP tools reference complements the main `copilot-instructions.md` file. When conducting a review:

1. Use tools from this reference in the "Review Analysis Process"
2. Apply the checklists from the main instructions
3. Format output according to the main instructions' guidelines
4. Follow severity classifications from the main instructions

## Additional Resources

- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [GitHub GraphQL API Documentation](https://docs.github.com/en/graphql)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [GitHub Code Search Syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)
