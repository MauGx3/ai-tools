---
title: "Copilot Code Review Instructions"
type: "best-practices"
difficulty: "intermediate"
time_required: "15-30 minutes per review"
prerequisites: "GitHub Copilot access, basic understanding of code review principles"
description: "Comprehensive agentic instructions for automated code review using GitHub Copilot and AI agents"
---

This guide provides actionable instructions for conducting effective automated code reviews using GitHub Copilot and other AI agents. These instructions are designed for both human reviewers leveraging AI tools and autonomous AI agents performing reviews.

## Core Review Principles

### 1. Focus on High-Impact Issues
- Prioritize security vulnerabilities and critical bugs
- Identify performance bottlenecks and scalability concerns
- Flag architectural issues that impact maintainability
- Balance thoroughness with actionable feedback

### 2. Provide Constructive Feedback
- Be specific about issues and proposed solutions
- Include code examples for suggested improvements
- Explain the reasoning behind recommendations
- Acknowledge positive aspects of the code

### 3. Context-Aware Analysis
- Consider the project's specific requirements and constraints
- Understand the codebase conventions and patterns
- Respect the existing architecture and design decisions
- Adapt feedback to the team's skill level and practices

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
   ```
   - Read the entire diff/changeset
   - Identify the purpose and scope of changes
   - Note the affected components and systems
   - Understand the context from commit messages and PR description
   ```

2. **Systematic Evaluation**
   ```
   - Apply the automated review checklist systematically
   - Categorize findings by severity (Critical, Major, Minor)
   - Document specific line numbers and file locations
   - Prepare actionable recommendations
   ```

3. **Generate Review Output**
   ```
   - Start with an overall assessment summary
   - List findings organized by category and severity
   - Highlight positive aspects of the implementation
   - Provide specific, actionable recommendations
   - Include code examples for suggested improvements
   ```

### Review Output Format

Use this structured format for consistency:

```markdown
## Code Review Summary

**Overall Assessment**: [Brief summary of code quality and main concerns]

**Files Reviewed**: [Number] files with [Number] additions and [Number] deletions

---

## Critical Issues 🚨
*Security vulnerabilities or major bugs that must be addressed*

1. **[Issue Title]** - `filename.ext:line`
   - **Problem**: [Description of the issue]
   - **Impact**: [Potential consequences]
   - **Solution**: [Specific recommendation]
   - **Example**:
   ```language
   // Suggested fix
   ```

## Major Issues ⚠️
*Performance problems or significant design concerns*

[Same format as Critical Issues]

## Minor Issues 💡
*Style improvements, optimizations, or suggestions*

[Same format as Critical Issues]

## Positive Aspects ✅
*Well-implemented features and good practices*

- [Specific praise with examples]
- [Recognition of good patterns]
- [Acknowledgment of improvements]

## Recommendations 📋
*Actionable next steps*

1. [Priority action items]
2. [Suggested improvements]
3. [Future considerations]
```

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

## Language-Specific Considerations

### JavaScript/TypeScript
- Check for proper TypeScript types (avoid `any`)
- Verify async/await error handling
- Review React hooks usage and dependencies
- Validate PropTypes or TypeScript interfaces
- Check for memory leaks in event listeners

### Python
- Verify PEP 8 compliance
- Check for proper exception handling
- Review type hints usage
- Validate virtual environment and dependencies
- Check for resource cleanup (context managers)

### Java
- Verify null safety
- Review exception handling patterns
- Check for resource management (try-with-resources)
- Validate thread safety in concurrent code
- Review logging practices

### Go
- Check error handling (never ignore errors)
- Review goroutine and channel usage
- Verify context propagation
- Check for resource leaks (defer statements)
- Validate error wrapping with context

### Ruby
- Review ActiveRecord query patterns
- Check for N+1 query problems
- Verify proper use of blocks and lambdas
- Review test coverage with RSpec/Minitest
- Check for security issues in Rails apps

## Integration with CI/CD

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

## Best Practices for Reviewers

### Human + AI Collaboration
1. **Use AI for Initial Triage**: Let AI catch common issues
2. **Focus Human Review**: Spend time on architecture and design
3. **Verify AI Findings**: Validate automated suggestions
4. **Provide Context**: Add domain knowledge AI might miss
5. **Continuous Improvement**: Refine AI instructions based on feedback

### Review Efficiency
- Review smaller changesets more frequently
- Focus on changes, not entire files
- Use automated tools for style and format checks
- Prioritize high-risk areas (security, data handling)
- Set reasonable time limits per review session

### Communication Tips
- Be respectful and professional
- Assume positive intent
- Ask questions to understand intent
- Offer to pair on complex issues
- Celebrate good work and improvements

## Common Pitfalls to Avoid

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

### Delayed Feedback
❌ Waiting days to provide review
✅ Review within 24 hours when possible

## Success Metrics

Track these indicators to measure review effectiveness:

- **Issue Detection Rate**: Percentage of bugs caught in review
- **Review Turnaround Time**: Time from PR creation to review
- **False Positive Rate**: Incorrect automated suggestions
- **Developer Satisfaction**: Feedback quality ratings
- **Code Quality Metrics**: Post-merge defect rates

## Continuous Improvement

### Regular Reviews
- **Weekly**: Review metrics and patterns
- **Monthly**: Update instructions based on learnings
- **Quarterly**: Evaluate new AI capabilities
- **Annually**: Complete review process audit

### Feedback Loop
1. Collect feedback from developers
2. Analyze common false positives
3. Identify missed issues in production
4. Update instructions and rules
5. Share learnings with the team

## Next Steps

1. **Start with Manual + AI**: Combine human expertise with AI assistance
2. **Build Confidence**: Gradually increase reliance on automation
3. **Customize Instructions**: Adapt to your team's specific needs
4. **Measure Impact**: Track improvements in code quality
5. **Iterate and Improve**: Continuously refine the process

---

**Remember**: The goal is to improve code quality while respecting developers' time and expertise. AI-assisted code review should enhance, not replace, human judgment and collaboration.
