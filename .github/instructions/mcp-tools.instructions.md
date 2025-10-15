---
applyTo: "**"
---
# Available MCP Tool Categories

<!-- TODO -->

### Code Repository Tools

For interacting with version control systems and code hosting platforms.

<!-- list MCP tools for code repositories -->

**GitHub MCP Server** - See [`github-mcp-server-tools.md`](github-mcp-server-tools.md) for detailed documentation

- Pull request analysis and review
- Repository file access
- Commit history and diffs
- Issue and discussion management
- Workflow and CI/CD integration

## General Usage Patterns

### 1. Tool Discovery

Before using MCP tools, understand what's available:

- Review server documentation to identify relevant tools
- Check tool parameters and return types
- Understand authentication requirements
- Note rate limits and usage constraints

### 2. Single Tool Usage

For simple operations, invoke a single tool:

**Example** - Fetching file contents:

```json
{
  "server": "github-mcp-server",
  "tool": "get_file_contents",
  "parameters": {
    "owner": "username",
    "repo": "repository",
    "path": "src/main.py"
  }
}
```

### 3. Tool Chaining

For complex workflows, chain multiple tools:

**Pattern**: Information Gathering → Analysis → Action

1. Use search/query tools to find relevant data
2. Use retrieval tools to get detailed information
3. Use processing tools to analyze the data
4. Use action tools to implement changes

**Example Workflow with GitHub MCP Server** - Code Review:

```
1. get_pull_request() → Get PR metadata
2. get_pull_request_files() → List changed files
3. get_file_contents() → Fetch full context for key files
4. get_pull_request_diff() → Review specific changes
5. search_code() → Find similar patterns in codebase
6. [Manual review and comment generation]
```

### 4. Parallel Tool Invocation

When operations are independent, invoke tools in parallel:

- Fetch multiple files simultaneously
- Query multiple data sources at once
- Perform concurrent searches

**Best Practice**: Only parallelize when there are no dependencies between operations.

## Best Practices for Multiple Tools

### Planning Your Workflow

1. **Identify the Goal**: What do you need to accomplish?
2. **List Required Information**: What data do you need?
3. **Map to Tools**: Which tools provide that data?
4. **Determine Dependencies**: What must happen in sequence vs. parallel?
5. **Plan Error Handling**: What if a tool fails?

### Efficient Tool Usage

**Do:**

- ✅ Start with broad queries, then drill down to specifics
- ✅ Cache results when the same data is needed multiple times
- ✅ Use pagination for large result sets
- ✅ Combine related operations when possible
- ✅ Respect rate limits and implement backoff strategies

**Don't:**

- ❌ Fetch the same data multiple times
- ❌ Request more data than needed (use filters and pagination)
- ❌ Chain tools unnecessarily (simplify when possible)
- ❌ Ignore error responses and continue blindly
- ❌ Mix authentication contexts without careful consideration

### Error Handling

When working with multiple tools:

- Check response status before proceeding to next tool
- Implement graceful degradation (partial results are often useful)
- Log tool invocations for debugging
- Handle authentication and permission errors appropriately
- Consider retry logic for transient failures

### Performance Optimization

1. **Minimize Tool Calls**: Fetch complete data in fewer calls
2. **Use Appropriate Filters**: Reduce data transfer and processing
3. **Leverage Caching**: Store frequently accessed data
4. **Batch Operations**: Group similar operations when supported
5. **Monitor Usage**: Track tool call counts and response times

## Integration Patterns

### Pattern 1: Research and Analysis

**Use Case**: Gathering information to answer questions or make decisions

**Tools Sequence**:

1. Search tools → Find relevant sources
2. Retrieval tools → Get detailed content
3. Analysis tools → Process and synthesize

**Example**: Researching a technical issue

- Search codebase for error patterns
- Retrieve relevant code sections
- Search documentation for related topics
- Analyze commit history for recent changes

### Pattern 2: Validation and Review

**Use Case**: Verifying correctness and quality

**Tools Sequence**:

1. Retrieval tools → Get current state
2. Comparison tools → Check against standards/history
3. Analysis tools → Identify issues

**Example**: Code review workflow

- Get pull request changes
- Retrieve file contexts
- Search for similar code patterns
- Compare against style guidelines

### Pattern 3: Automation and Action

**Use Case**: Performing operations based on conditions

**Tools Sequence**:

1. Query tools → Check current state
2. Decision tools → Determine actions needed
3. Action tools → Execute changes
4. Verification tools → Confirm results

**Example**: Repository maintenance

- Query open issues and PRs
- Check workflow statuses
- Identify stale items
- Update labels or close items

### Pattern 4: Monitoring and Reporting

**Use Case**: Tracking state and generating insights

**Tools Sequence**:

1. Collection tools → Gather metrics
2. Aggregation tools → Summarize data
3. Comparison tools → Track trends
4. Formatting tools → Present results

**Example**: Project health dashboard

- List recent commits and PRs
- Get workflow run statistics
- Search for security alerts
- Compile and format report

## Advanced Techniques

### Context Building

Build comprehensive context by combining tools:

- Use broad tools first (list, search)
- Narrow down with specific tools (get, show)
- Enrich with related tools (history, references)

### Conditional Logic

Adapt tool usage based on results:

```
IF search_results > threshold THEN
  use_detailed_tool()
ELSE
  use_summary_tool()
```

### Iterative Refinement

Use tool results to guide subsequent calls:

1. Start with broad query
2. Analyze initial results
3. Refine parameters based on findings
4. Repeat until goal is achieved

### Cross-Domain Integration

Combine tools from different domains:

- GitHub + File System: Clone and analyze repositories
- Web + Database: Fetch and store external data
- AI/ML + Code: Analyze code semantics and patterns

## Tool-Specific Documentation

For detailed documentation on specific MCP tool servers:

- **Additional MCP Servers**:
  - Check the [MCP Server Registry](https://github.com/modelcontextprotocol/servers) for community-maintained servers
  - Review server README files for tool documentation
  - Consult API specifications for parameter details

## Common Use Cases

### Code Review Automation

**Tools Needed**: GitHub MCP Server

1. Retrieve PR information and files
2. Get file contents for context
3. Search for similar code patterns
4. Generate review comments

### Documentation Generation

**Tools Needed**: File System, Code Analysis

1. List project files
2. Read source code
3. Extract comments and structure
4. Generate formatted documentation

### Data Analysis

**Tools Needed**: Database, File System, Web

1. Query data sources
2. Retrieve datasets
3. Process and transform data
4. Generate reports and visualizations

### Testing and Validation

**Tools Needed**: GitHub, File System, Web

1. Retrieve test specifications
2. Fetch implementation code
3. Compare against requirements
4. Validate test coverage

## Troubleshooting

### Tool Not Available

- Verify the MCP server is running and accessible
- Check that the tool name is spelled correctly
- Ensure you have required permissions

### Authentication Errors

- Verify credentials are properly configured
- Check token/API key validity and scope
- Ensure authentication context matches the tool

### Rate Limiting

- Implement exponential backoff
- Cache results to reduce duplicate calls
- Consider using batch operations
- Monitor your usage against limits

### Unexpected Results

- Verify parameter types and formats
- Check for required vs. optional parameters
- Review tool documentation for caveats
- Test with minimal parameters first

### Performance Issues

- Reduce data transfer with filters
- Use pagination for large datasets
- Parallelize independent operations
- Consider caching frequently accessed data

## Security Considerations

When using MCP tools:

- **Never expose credentials** in tool parameters or responses
- **Validate permissions** before performing actions
- **Sanitize inputs** to prevent injection attacks
- **Audit tool usage** for compliance and security
- **Use least privilege** - only grant necessary permissions
- **Rotate credentials** regularly
- **Monitor for suspicious patterns** in tool usage

## Summary

Effective use of MCP tools requires:

1. **Understanding** what tools are available and what they do
2. **Planning** your workflow to use tools efficiently
3. **Chaining** tools logically to accomplish complex tasks
4. **Handling** errors and edge cases gracefully
5. **Optimizing** for performance and maintainability

By following these guidelines and patterns, you can leverage multiple MCP tools to create powerful, automated workflows that enhance productivity and code quality.
