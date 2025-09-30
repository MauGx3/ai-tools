---
title: "Copilot Code Review Instructions"
type: "best-practices"
difficulty: "intermediate"
time_required: "15-30 minutes per review"
prerequisites: "GitHub Copilot access, basic understanding of code review principles"
description: "Comprehensive agentic instructions for automated code review using GitHub Copilot and AI agents"
applyTo: ["*.md", "*.js", "*.ts", "*.py", "*.java", "*.go", "*.rb", "*.php", "*.cs", "*.cpp", "*.c", "*.h", "*.jsx", "*.tsx", "*.vue", "*.swift", "*.kt"]
---

This guide provides actionable instructions for conducting effective automated code reviews using GitHub Copilot and other AI agents. These instructions are designed for both human reviewers leveraging AI tools and autonomous AI agents performing reviews.

## Core Review Principles

### 1. Understand Before Critiquing
- Read and comprehend the entire change before commenting
- Identify the intent and context of the modifications
- Consider the business requirements driving the change
- Review related documentation and linked issues

### 2. Be Kind and Constructive
- Assume positive intent from the author
- Frame feedback as questions or suggestions, not commands
- Praise good solutions and improvements
- Focus on the code, not the person

### 3. Provide Actionable Feedback
- Be specific about issues and proposed solutions
- Include code examples for suggested improvements
- Explain the reasoning behind recommendations
- Link to relevant documentation or standards

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

### Review Analysis Process

1. **Initial Assessment**
   - Use `github-mcp-server-get_pull_request` to retrieve PR details
   - Use `github-mcp-server-get_pull_request_diff` to get the full diff
   - Use `github-mcp-server-get_pull_request_files` to list all changed files
   - Read commit messages and PR description for context

2. **Systematic Evaluation**
   - Apply the automated review checklist systematically
   - Use `github-mcp-server-get_file_contents` to view full file context when needed
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
- Security vulnerabilities
- Data corruption risks
- Breaking changes without migration path
- Resource leaks that impact stability
- Logic errors causing incorrect behavior

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
- Place inline comments at specific lines
- Link to relevant documentation
- Reference similar patterns in the codebase
- Suggest related improvements in context

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
- Frame suggestions as questions when appropriate: "Consider X because Y?"
- Acknowledge when you're uncertain: "This might be an issue, but please verify"
- Respect existing patterns: "I see this pattern elsewhere; is there a reason for the difference?"
- Celebrate improvements: "This change addresses the previous concern well"

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
❌ Nitpicking formatting issues
✅ Prioritize functional and security concerns

### Missing Context
❌ Reviewing code in isolation
✅ Understanding business requirements and constraints

## Success Metrics

Track these indicators to measure review effectiveness:

- **Issue Detection Rate**: Percentage of bugs caught in review
- **Review Turnaround Time**: Time from PR creation to review
- **False Positive Rate**: Incorrect automated suggestions
- **Developer Satisfaction**: Feedback quality ratings
- **Code Quality Metrics**: Post-merge defect rates

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
