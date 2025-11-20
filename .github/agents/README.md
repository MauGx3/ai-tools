# Custom Agents

This directory contains custom agent definitions for VS Code and GitHub Copilot. Custom agents are specialized AI assistants that provide focused expertise for specific tasks.

## Available Agents

### Cloud Infrastructure (`cloud.agent.md`)

**Purpose**: Cloud infrastructure and deployment specialist

**Expertise**:
- Cloud platforms (AWS, Azure, GCP)
- Container orchestration (Kubernetes, Docker, Helm)
- Infrastructure as Code (Terraform, Ansible, CloudFormation)
- CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)

**When to use**:
- Deploying applications to cloud platforms
- Setting up Kubernetes clusters and workloads
- Creating or optimizing Dockerfiles
- Designing CI/CD pipelines
- Infrastructure as Code projects
- Cloud architecture decisions
- Security and compliance for cloud deployments

**Handoffs**:
- To Planner: For detailed infrastructure planning
- To Reviewer: For security and best practices review
- To Implementation: For executing infrastructure changes

**Tools**: fetch, githubRepo, search, usages, view, edit, bash

## How to Use Custom Agents

### In VS Code

1. Open the Chat view in VS Code
2. Click on the agent dropdown (usually shows "@workspace")
3. Select "Cloud Infrastructure" or another custom agent
4. Your prompts will be processed with that agent's specialized context

### Creating New Agents

To create a new custom agent:

1. Create a new `.agent.md` file in this directory
2. Add YAML frontmatter with configuration:
   ```yaml
   ---
   description: Brief description of the agent
   name: Agent Display Name
   tools: ['tool1', 'tool2']
   model: Claude Sonnet 4
   handoffs:
     - label: Handoff Label
       agent: target-agent
       prompt: Prompt to send
       send: false
   ---
   ```
3. Add the agent's instructions in Markdown below the frontmatter
4. Reference existing instruction files from `_instructions/` for detailed guidance

### Best Practices

- Keep agents focused on specific domains or tasks
- Reference existing instruction files instead of duplicating content
- Define clear handoff points for common workflows
- Specify appropriate tools for the agent's needs
- Include examples and common use cases

## References

- [Custom agents in VS Code](../../_thoughts/third-party/agents/Custom%20agents%20in%20VS%20Code.md)
- [Add a prompt or instruction](../../docs/how-to/add-a-prompt-or-instruction.md)
- [Prompt Engineering Best Practices](../../docs/guides/prompt-engineering-best-practices.md)
