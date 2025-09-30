---
title: "Copilot Code Review Instructions"
type: "best-practices"
difficulty: "intermediate"
time_required: "15-30 minutes per review"
prerequisites: "GitHub Copilot access, basic understanding of code review principles"
description: "Comprehensive agentic instructions for automated code review using GitHub Copilot and AI agents"
tags: ["code review", "copilot", "AI", "best practices"]
categories: ["automation"]
applyTo: ["**"]
---

This guide provides actionable instructions for conducting effective automated code reviews using GitHub Copilot and other AI agents. These instructions are designed for both human reviewers leveraging AI tools and autonomous AI agents performing reviews.

## Core Review Principles

Based on industry best practices from Google's Engineering Practices, Microsoft's Code Review guidelines, and research from publications like "Best Kept Secrets of Peer Code Review" (SmartBear):

### 1. Review Intent, Not Just Implementation
- Understand the problem being solved before critiquing the solution
- Verify that the change aligns with the stated requirements
- Check if the approach is appropriate for the problem scope
- Consider alternative solutions that might be simpler or more maintainable

### 2. Focus on Impact and Correctness
- Prioritize correctness, security, and performance over style
- Identify bugs, logic errors, and edge cases
- Review error handling and failure scenarios
- Verify that the code does what it claims to do

### 3. Be Objective and Specific
- Provide concrete examples and suggest specific improvements
- Reference documentation, standards, or similar code in the codebase
- Distinguish between "must fix" issues and optional suggestions
- Use facts and reasoning rather than personal preference

## Automated Review Checklist

### 🔒 Security Review
- [ ] **Input Validation**: All user inputs are validated and sanitized
- [ ] **Authentication**: Proper authentication mechanisms are implemented
- [ ] **Authorization**: Access controls are correctly enforced
- [ ] **Data Exposure**: No sensitive data is logged or exposed
- [ ] **Injection Prevention**: SQL, XSS, and command injection risks are mitigated
- [ ] **Cryptography**: Secure algorithms and proper key management used
- [ ] **Dependencies**: No known vulnerabilities in dependencies
- [ ] **Error Handling**: Errors don't leak sensitive information

### ⚡ Performance Review
- [ ] **Algorithm Efficiency**: Optimal time and space complexity
- [ ] **Database Queries**: Efficient queries with proper indexing
- [ ] **Caching**: Appropriate use of caching strategies
- [ ] **Resource Management**: Proper cleanup of connections, files, memory
- [ ] **Async Operations**: Non-blocking operations where beneficial
- [ ] **Pagination**: Large datasets are paginated appropriately
- [ ] **N+1 Queries**: No N+1 query patterns detected
- [ ] **Load Testing**: Performance considerations for scale

### 🏗️ Code Quality Review
- [ ] **Readability**: Code is clear and self-documenting
- [ ] **Naming**: Variables, functions, and classes have descriptive names
- [ ] **Complexity**: Functions and methods are reasonably sized
- [ ] **DRY Principle**: No unnecessary code duplication
- [ ] **SOLID Principles**: Good separation of concerns
- [ ] **Error Handling**: Comprehensive and appropriate error handling
- [ ] **Comments**: Complex logic is well-documented
- [ ] **Formatting**: Consistent code style and formatting

### 🧪 Testing & Quality Assurance
- [ ] **Test Coverage**: Critical paths have test coverage
- [ ] **Test Quality**: Tests are meaningful and maintainable
- [ ] **Edge Cases**: Boundary conditions are tested
- [ ] **Error Scenarios**: Failure cases are tested
- [ ] **Test Isolation**: Tests are independent and reproducible
- [ ] **Mocking**: External dependencies are properly mocked
- [ ] **Integration Tests**: Key workflows have integration coverage
- [ ] **Documentation**: Tests serve as documentation

### 📝 Documentation Review
- [ ] **API Documentation**: Public APIs are documented
- [ ] **Code Comments**: Complex logic is explained
- [ ] **README Updates**: Documentation reflects changes
- [ ] **Change Documentation**: Breaking changes are documented
- [ ] **Examples**: Usage examples are provided where helpful
- [ ] **Type Definitions**: Types/interfaces are well-defined
- [ ] **Deprecation**: Deprecated features are marked clearly
- [ ] **Migration Guides**: Major changes include migration instructions

## AI Agent Instructions

> **Note**: For comprehensive MCP tools reference, see `mcp-tools-reference.md` which provides detailed documentation on all available tools for code review automation.

### Review Analysis Process

1. **Initial Assessment**
   - Use `github-mcp-server-get_pull_request` to retrieve PR details
   - Use `github-mcp-server-get_pull_request_diff` to get the full diff
   - Use `github-mcp-server-get_pull_request_files` to list all changed files
   - Read commit messages and PR description for context

2. **Systematic Evaluation**
   - Apply the automated review checklist systematically
   - Use `github-mcp-server-get_file_contents` to view full file context when needed
   - Use `github-mcp-server-list_code_scanning_alerts` for security vulnerabilities
   - Use `github-mcp-server-list_secret_scanning_alerts` for exposed credentials
   - Use `github-mcp-server-search_code` to find similar patterns in codebase
   - Categorize findings by severity (Critical, Major, Minor)
   - Document specific line numbers and file locations
   - Prepare actionable recommendations

3. **Generate Review Output**
   - Start with an overall assessment summary
   - List findings organized by category and severity
   - Highlight positive aspects of the implementation
   - Provide specific, actionable recommendations
   - Include code examples for suggested improvements

### Review Output Format

Use this concise format:

**Summary**: [1-2 sentence overview]

**Critical Issues** 🚨
- `file.ext:line` - [Issue] → [Solution]

**Major Issues** ⚠️
- `file.ext:line` - [Issue] → [Solution]

**Minor Issues** 💡
- `file.ext:line` - [Issue] → [Solution]

**Positive Aspects** ✅
- [What's done well]

**Recommendations** 📋
1. [Priority actions]

### Severity Guidelines

**Critical (🚨)**: Must be fixed before merge
- Security vulnerabilities (including known CVEs in dependencies)
- Data corruption risks
- Breaking changes without migration path
- Resource leaks that impact stability
- Logic errors causing incorrect behavior

**Dependency Vulnerability Check**:
- Use `npm audit`, `pip check`, `bundle audit`, or equivalent to identify CVEs
- Check NIST NVD, GitHub Security Advisories, and Snyk databases
- Report CVSS score and severity (Critical: 9.0-10.0, High: 7.0-8.9)
- Verify if patches or updated versions are available
- Recommend immediate action for exploitable vulnerabilities

**Major (⚠️)**: Should be fixed before merge
- Performance issues affecting user experience
- Significant technical debt introduction
- Missing error handling in critical paths
- Poor scalability patterns
- Inconsistent architecture

**Minor (💡)**: Nice to have improvements
- Code style inconsistencies
- Minor performance optimizations
- Documentation improvements
- Refactoring opportunities
- Better naming suggestions

> **Note**: Language-specific code review instructions are available in separate files. This guide focuses on universal code review principles applicable to all programming languages.

## Integration with CI/CD

> **Note**: Prepare your CI/CD pipeline to support language-specific review instructions. Create separate instruction files for each language (e.g., `copilot-instructions-python.md`, `copilot-instructions-javascript.md`) and configure your pipeline to load the appropriate instructions based on the file type being reviewed.

### Automated Review Triggers
- **Pull Request Creation**: Initial automated review
- **Push to PR**: Incremental review of changes
- **Review Request**: Deep dive analysis
- **Pre-merge**: Final validation check

### Review Comments

Follow GitHub's code review best practices:

**Comment Placement**:
- Use inline comments for specific line issues
- Use general comments for overall architectural feedback
- Start review threads at the appropriate line, not at random locations
- Use "suggestion" blocks for simple fixes that can be applied directly

**Comment Structure** (based on Conventional Comments):
- `suggestion:` For proposed code changes
- `issue:` For problems that need to be addressed
- `question:` For clarifications needed
- `nitpick:` For minor, optional improvements
- `praise:` (use sparingly) For particularly good solutions

**Comment Quality**:
- Be specific: Reference exact lines, variables, or functions
- Provide rationale: Explain why something is an issue
- Offer solutions: Don't just point out problems
- Link to resources: Standards, docs, or similar code examples
- Keep it brief: One issue per comment when possible

**Example Format**:
```
issue: This SQL query is vulnerable to injection attacks.

The user input on line 45 is directly concatenated into the query string.
Use parameterized queries instead:
`cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))`

Reference: OWASP SQL Injection Prevention
```

### False Positive Handling
- Allow developers to mark false positives
- Learn from corrections over time
- Provide explanation for flagged issues
- Offer option to suppress specific rules

## AI Collaboration with Humans

### When Working with Human Reviewers
1. **Complement, Don't Replace**: Focus on routine checks while humans handle architectural decisions
2. **Ask for Clarification**: When uncertain about intent or requirements, ask questions instead of making assumptions
3. **Learn from Feedback**: When humans override or modify your suggestions, note the pattern for future reviews
4. **Provide Context**: Explain why you flagged an issue, including relevant documentation or best practices
5. **Escalate Appropriately**: Flag complex issues that require human judgment (e.g., architectural decisions, business logic)

### Effective Communication
- Use clear, concise language without jargon
- Frame suggestions as questions when uncertain: "Could X improve Y?"
- Acknowledge uncertainty explicitly: "This may be an issue, please verify"
- Reference existing patterns: "Line 50 uses pattern X; is there a reason for the difference here?"
- State facts objectively without unnecessary praise or criticism

### Collaboration Protocol
- **Initial Review**: Provide automated feedback on common issues
- **Human Review**: Wait for human reviewer to assess architectural and business logic
- **Iterative Refinement**: Respond to new changes quickly with focused feedback
- **Learning**: Track which suggestions are accepted/rejected to improve future reviews

## Common Pitfalls to Avoid

### AI-Specific Pitfalls
❌ **Hallucinating Issues**: Don't report problems that don't exist in the actual code
✅ **Verify Before Flagging**: Ensure issues are real and reproducible

❌ **Over-Explaining**: Don't provide verbose explanations for simple issues
✅ **Be Concise**: State the issue and solution clearly and briefly

❌ **Ignoring Context**: Don't apply generic rules without considering project context
✅ **Contextual Review**: Adapt feedback to the project's patterns and requirements

❌ **Repeating Feedback**: Don't flag the same issue multiple times across similar code
✅ **Consolidate**: Group similar issues and suggest a comprehensive solution

❌ **Missing Obvious Issues**: Don't get distracted by minor issues while missing critical bugs
✅ **Prioritize**: Always check security and correctness first

### Over-Automation
❌ Blindly accepting all AI suggestions
✅ Review and validate automated findings

### Scope Creep
❌ Suggesting unrelated refactoring
✅ Focus on changes in the current PR

### Style Over Substance
❌ Nitpicking formatting issues individually
✅ Consolidate all formatting issues into a single, actionable comment

**For Multiple Formatting Issues**:
Instead of commenting on each formatting violation, consolidate them:

```
suggestion: Multiple formatting inconsistencies detected. Run the project's formatter:

npm run format           # For JavaScript/TypeScript projects
black .                  # For Python projects
gofmt -w .              # For Go projects
dotnet format           # For .NET projects

Or configure your editor to format on save.

Issues found:
- Lines 15, 23, 45: Inconsistent indentation
- Lines 30-35: Missing trailing commas
- Lines 50, 67: Inconsistent quote style
```

This approach:
- Saves reviewer time
- Provides actionable solution
- Avoids cluttering the review with minor style comments
- Delegates formatting to automated tools

### Missing Context
❌ Reviewing code in isolation
✅ Understanding business requirements and constraints

## Success Metrics

Track these indicators to measure review effectiveness:

**Quality Metrics**:
- **Issue Detection Rate**: Target 70-85% of bugs caught in review (industry benchmark)
- **False Positive Rate**: Keep below 15% (< 15 incorrect suggestions per 100 comments)
- **Defect Density**: Track post-merge defects per 1000 lines of code (target: < 1.0)
- **Critical Issues Found**: Number of security/correctness issues caught before merge

**Efficiency Metrics**:
- **Review Turnaround Time**: Target < 24 hours from PR creation to review
- **Review Thoroughness**: Comments per 100 lines of code changed (typical: 3-7)
- **Fix Cycle Time**: Time from comment to resolution (target: < 4 hours)
- **Review Size**: Lines of code per review (optimal: 200-400 LOC)

**Collaboration Metrics**:
- **Developer Satisfaction**: Survey score 4.0+ / 5.0
- **Suggestion Acceptance Rate**: 60-80% of suggestions implemented
- **Review Iterations**: Number of review cycles per PR (target: 1-2)
- **Discussion Quality**: Resolved vs. dismissed threads ratio (target: > 80% resolved)

**References**:
- Cisco study: Best reviews are 200-400 LOC, taking 60-90 minutes
- SmartBear research: Optimal review rate is < 500 LOC/hour
- Microsoft study: Reviews with < 24h turnaround have 15% fewer defects

## Continuous Improvement

### Learning from Past Reviews
1. **Track Patterns**: Identify common issues and false positives
2. **Analyze Feedback**: Review which suggestions were accepted/rejected
3. **Update Knowledge**: Incorporate new patterns and project-specific rules
4. **Refine Approach**: Adjust severity thresholds based on team preferences
5. **Share Insights**: Document lessons learned for future reviews

### Self-Improvement for AI Agents
- **After Each Review**: Note which findings were validated by humans
- **Weekly**: Analyze acceptance rate of different types of suggestions
- **Monthly**: Identify categories where accuracy can improve
- **Quarterly**: Evaluate if new types of issues should be added to checklist
- **Continuously**: Learn project-specific patterns and conventions

### Adaptation Strategies
- If false positive rate is high: Be more conservative, require stronger evidence
- If missing issues: Expand checklist, review context more thoroughly
- If feedback is unclear: Ask more clarifying questions, provide better examples
- If overloading reviewers: Consolidate similar issues, reduce noise

## Future Review Instructions

When conducting subsequent code reviews for the same repository or team:

1. **Reference Previous Reviews**: Check history for similar patterns or issues
2. **Apply Learned Patterns**: Use project-specific knowledge from past interactions
3. **Respect Established Norms**: Follow team conventions identified in previous reviews
4. **Build on Feedback**: Incorporate human reviewer preferences from past PRs
5. **Track Recurring Issues**: Identify and flag systemic problems across multiple PRs
6. **Suggest Process Improvements**: When patterns emerge, recommend preventive measures
7. **Maintain Consistency**: Apply the same standards across similar code changes
8. **Evolve with Codebase**: Adapt as the project grows and patterns change

### Context Retention
- Remember coding style preferences from previous reviews
- Track architectural decisions and their rationale
- Note which suggestions were rejected and why
- Build understanding of project-specific constraints
- Recognize team priorities (e.g., security-first vs. speed-first)

### Progressive Assistance
- Start with fundamental issues in first reviews
- Gradually introduce more advanced suggestions as trust builds
- Adjust verbosity based on feedback (more/less explanation)
- Focus on areas where past suggestions were most valuable
- Reduce focus on areas where suggestions were consistently rejected
