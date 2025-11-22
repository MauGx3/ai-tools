# Custom Agents

This directory contains custom agent definitions for GitHub Copilot in VS Code. Custom agents allow you to create specialized AI assistants tailored to specific development roles and tasks.

## What are Custom Agents?

Custom agents are specialized configurations that define:
- Specific instructions and expertise areas
- Available tools and capabilities
- Handoff workflows to other agents
- Preferred AI models

## Available Agents

### Cloud Infrastructure Expert (`cloud.agent.md`)

**Purpose**: Specialized assistant for cloud infrastructure, containerization, and orchestration tasks.

**Expertise Areas**:
- Docker containerization and multi-stage builds
- Kubernetes orchestration and deployments
- Cloud platforms (AWS, Azure, GCP)
- CI/CD pipelines with GitHub Actions
- Infrastructure as Code (Terraform, CloudFormation)
- Security hardening and best practices

**When to Use**:
- Creating or optimizing Dockerfiles
- Writing Kubernetes manifests
- Designing cloud infrastructure
- Setting up CI/CD pipelines
- Troubleshooting deployment issues
- Implementing security best practices

**Available Tools**: `search`, `fetch`, `githubRepo`, `bash`, `view`, `edit`, `create`

**Handoffs**:
- **Code Review**: Transition to default agent for reviewing infrastructure code
- **Implement Changes**: Hand off to default agent for implementing planned changes

## How to Use Custom Agents

### In VS Code

1. Open the GitHub Copilot chat
2. Click the agents dropdown (default is usually `@workspace`)
3. Select "Cloud Infrastructure Expert" from the list
4. Ask your cloud/infrastructure-related questions

### Example Usage

```
# Switch to Cloud Infrastructure Expert agent
@cloud-infrastructure-expert

# Then ask questions like:
- Create a production-ready Kubernetes deployment for a Node.js API
- Optimize this Dockerfile for size and security
- Design an AWS infrastructure for a microservices application
- Set up a GitHub Actions workflow for building and deploying containers
```

## Creating New Agents

To create a new custom agent:

1. Create a new `.agent.md` file in this directory
2. Add YAML frontmatter with configuration:
   ```yaml
   ---
   description: Brief description shown in chat input
   name: Display name for the agent
   tools: ['search', 'fetch', 'githubRepo', 'bash']
   model: Claude Sonnet 4  # Optional, defaults to selected model
   handoffs:
     - label: Button text
       agent: target-agent-name
       prompt: Message to send
       send: false  # Auto-send or pre-fill
   ---
   ```
3. Write detailed instructions in the markdown body
4. Reference relevant instruction files from `_instructions/`
5. Include example use cases and limitations

## Agent Design Principles

When creating custom agents:

1. **Clear Boundaries**: Define specific expertise areas and limitations
2. **Tool Selection**: Include only relevant tools for the agent's purpose
3. **Reference Instructions**: Link to existing instruction files for detailed guidance
4. **Handoff Workflows**: Define logical transitions to other agents
5. **Production Ready**: Focus on real-world, production-quality guidance
6. **Security First**: Always prioritize security best practices

## Resources

- [VS Code Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- Repository instruction files in `_instructions/` directory
- Agent design guide in `_instructions/agent-expert.md`

## Related Files

- `_instructions/containerization-docker-best-practices.instructions.md`
- `_instructions/kubernetes-deployment-best-practices.instructions.md`
- `.github/instructions/github-actions-ci-cd-best-practices.instructions.md`
- `.github/copilot-instructions.md` - Global Copilot configuration

---

For questions or suggestions about custom agents, please open an issue or discussion in the repository.
