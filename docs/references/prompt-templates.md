---
layout: default
title: Prompt Templates Reference
---

# Prompt Templates Reference

Quick reference for creating effective AI prompts with consistent structure and metadata.

## Basic Prompt Template

```yaml
---
title: "Descriptive Prompt Name"
category: "coding|writing|analysis|creative|productivity"
description: "Brief description of what this prompt does"
tags: ["tag1", "tag2", "tag3"]
use_case: "When to use this prompt"
---

Your prompt content goes here...

Include clear instructions, context, and format specifications.
```

## Category Guidelines

### Coding Prompts
- **Focus**: Development, debugging, code review, architecture
- **Tags**: programming languages, frameworks, specific techniques
- **Examples**: "code-review", "debugging", "optimization", "testing"

### Writing Prompts  
- **Focus**: Content creation, documentation, editing, communication
- **Tags**: content types, audiences, specific formats
- **Examples**: "documentation", "technical-writing", "user-guides", "api-docs"

### Analysis Prompts
- **Focus**: Research, data analysis, evaluation, decision-making
- **Tags**: analysis types, domains, methodologies
- **Examples**: "data-analysis", "research", "evaluation", "comparison"

### Creative Prompts
- **Focus**: Brainstorming, ideation, problem-solving, innovation
- **Tags**: techniques, contexts, creative processes
- **Examples**: "brainstorming", "ideation", "problem-solving", "innovation"

### Productivity Prompts
- **Focus**: Planning, organization, optimization, workflow improvement
- **Tags**: productivity areas, tools, methodologies
- **Examples**: "planning", "organization", "optimization", "workflow"

## Advanced Prompt Structure

```yaml
---
title: "Advanced Prompt Name"
category: "primary-category"
description: "Detailed description with specific outcomes"
tags: ["specific", "searchable", "keywords"]
use_case: "Specific scenarios when this is most effective"
ai_model: "Recommended AI model (optional)"
context_length: "Suggested context window size (optional)"
difficulty: "beginner|intermediate|advanced (optional)"
---

## Context Setting
Brief explanation of the AI's role and expertise.

## Task Instructions
Clear, specific instructions for the AI.

## Output Format
Detailed specification of desired response structure.

## Examples (Optional)
Sample inputs and expected outputs.

## Variations (Optional)
Alternative versions or customizations.
```

## Effective Prompt Patterns

### Role-Based Prompts
```
You are a [specific role] with expertise in [domain].
Your task is to [specific action] focusing on [key aspects].
```

### Structured Output Prompts
```
Please provide your response in the following format:
1. Section One: [description]
2. Section Two: [description]
3. Section Three: [description]
```

### Iterative Prompts
```
Let's work through this step by step:
1. First, analyze [aspect one]
2. Then, consider [aspect two]  
3. Finally, synthesize [final output]
```

### Context-Rich Prompts
```
Given the following context:
- [Background information]
- [Constraints and requirements]
- [Success criteria]

Please [specific task request].
```

## Metadata Best Practices

### Titles
- Use descriptive, searchable names
- Include the main function or purpose
- Avoid generic terms like "helper" or "assistant"
- Examples: "Code Review Assistant", "Technical Documentation Generator"

### Descriptions
- Explain what the prompt does
- Mention key features or capabilities
- Keep under 150 characters for readability
- Focus on outcomes and benefits

### Tags
- Use 3-5 relevant, searchable tags
- Include technical terms users might search for
- Add domain-specific keywords
- Examples: ["api", "documentation", "openapi", "technical-writing"]

### Use Cases
- Specify when this prompt is most effective
- Mention prerequisites or ideal conditions
- Include context about problem types
- Examples: "When you need to create comprehensive API documentation from code"

## Common Patterns

### Code-Related Prompts
```yaml
category: "coding"
tags: ["programming-language", "task-type", "complexity-level"]
use_case: "When working with [specific technology] for [specific purpose]"
```

### Documentation Prompts
```yaml
category: "writing"
tags: ["documentation-type", "audience", "format"]
use_case: "When creating [doc-type] for [audience] using [format]"
```

### Analysis Prompts
```yaml
category: "analysis"
tags: ["analysis-type", "domain", "methodology"]
use_case: "When you need to [analyze-what] for [purpose]"
```

## Quality Checklist

Before adding a new prompt, verify:

- [ ] Clear, specific title that indicates purpose
- [ ] Appropriate category assignment
- [ ] Complete description under 150 characters
- [ ] 3-5 relevant, searchable tags
- [ ] Specific use case explanation
- [ ] Well-structured prompt content
- [ ] Clear instructions for the AI
- [ ] Specified output format when needed
- [ ] Examples included where helpful
- [ ] Tested and validated functionality

## Examples Repository

For complete examples of each prompt type, see:
- [Coding Examples](../examples/coding-prompts.md)
- [Writing Examples](../examples/writing-prompts.md)
- [Analysis Examples](../examples/analysis-prompts.md)
- [Creative Examples](../examples/creative-prompts.md)
- [Productivity Examples](../examples/productivity-prompts.md)