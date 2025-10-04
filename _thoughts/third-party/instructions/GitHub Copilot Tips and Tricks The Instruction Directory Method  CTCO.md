![feature image](https://www.ctco.blog/_astro/github-copilot-tips.CCD9XbAa_bzQms.webp)

## Table of contents[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#table-of-contents)

Open Table of contents

-   [The instruction directory revelation](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#the-instruction-directory-revelation)
-   [Why this approach actually works](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#why-this-approach-actually-works)
-   [Setting up your instruction directory](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#setting-up-your-instruction-directory)
    -   [The core files you need](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#the-core-files-you-need)
    -   [File structure and naming conventions](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#file-structure-and-naming-conventions)
-   [Essential instruction files explained](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#essential-instruction-files-explained)
    -   [AGENT\_INSTRUCTIONS.md - Your development codex](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#agent_instructionsmd---your-development-codex)
    -   [AGENT\_SESSION\_MEMORY.md - Persistent context](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#agent_session_memorymd---persistent-context)
    -   [Domain-specific documentation](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#domain-specific-documentation)
    -   [BUILD\_AND\_DEPLOYMENT\_NOTES.md - Operational knowledge](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#build_and_deployment_notesmd---operational-knowledge)
-   [Real-world example: The SaaS project](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#real-world-example-the-saas-project)
-   [How to integrate this with your workflow](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#how-to-integrate-this-with-your-workflow)
-   [Common mistakes and how to avoid them](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#common-mistakes-and-how-to-avoid-them)
-   [Advanced tips for maximum effectiveness](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#advanced-tips-for-maximum-effectiveness)
-   [The results speak for themselves](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#the-results-speak-for-themselves)

## The instruction directory revelation[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#the-instruction-directory-revelation)

I’ve been working with Github copilot agents for a number of weeks now and I’ve learned a few things that helped me focus the way in which these agents performed their work. AI agents periodically seemed to forget context between sessions or struggled to understand the bigger picture of complex projects, I took a step back and decided to think about how I’d set up a Junior developer for success, in fact how do I properly delegate tasks now as a technical leader. The answer that I came up with is what I call ‘the instruction directory method’.

From what I’ve seen most developers use AI agents reactively. They fire up Copilot, ask a question, get an answer, and wonder why the AI doesn’t seem to understand their project’s nuances or remember important decisions from previous sessions. I was doing the same thing until I realised that GitHub Copilot agents are only as good as the context you provide them the same as any other living breathing person.

The instruction directory method changes everything. Instead of starting each conversation from scratch, you create a dedicated folder structure that gives AI agents persistent, comprehensive context about your project. It’s like having a shared knowledge base that carries over between sessions, and the results are genuinely impressive.

## Why this approach actually works[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#why-this-approach-actually-works)

GitHub Copilot agents excel when they have rich context to work with. The problem is that traditional project documentation is often scattered, outdated, or written for humans rather than AI consumption. The instruction directory approach solves this by creating purpose-built documentation that serves both human developers and AI agents.

Think about it this way: when a new developer joins your team, you don’t just point them at the codebase and say “figure it out.” You provide context about the project goals, architectural decisions, coding standards, and operational procedures. AI agents need exactly the same kind of onboarding, but they need it in a structured, consistent format.

The beauty of this approach is that it creates a feedback loop. As you work with agents and they help solve problems or implement features, you can capture that knowledge back into your instruction files. This builds up a comprehensive knowledge base that makes each subsequent interaction more effective.

## Setting up your instruction directory[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#setting-up-your-instruction-directory)

### The core files you need[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#the-core-files-you-need)

Here’s the essential structure I use for every project. Don’t worry about getting this perfect from the start - you can evolve it as you learn what works best for your specific context:

```
your-project/
├── instructions/
│   ├── AGENT_INSTRUCTIONS.md          # Main development guidelines
│   ├── AGENT_SESSION_MEMORY.md        # Session notes and context
│   ├── BUILD_AND_DEPLOYMENT_NOTES.md  # Operational procedures
│   └── agent_reports/                 # AI-generated documentation
│       ├── FEATURE_IMPLEMENTATION_SUMMARY.md
│       ├── ARCHITECTURE_DECISIONS.md
│       └── TESTING_REPORTS.md
├── src/
└── ...
```

### File structure and naming conventions[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#file-structure-and-naming-conventions)

I use uppercase filenames with underscores for a reason - they stand out clearly when you’re browsing files, and they’re easy for AI agents to identify and reference. The `instructions/` folder name is intentionally generic because you’ll be referencing it constantly in prompts.

The key is consistency. Once you establish a naming pattern, stick with it. AI agents work better when they can predict where to find information.

## Essential instruction files explained[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#essential-instruction-files-explained)

### AGENT\_INSTRUCTIONS.md - Your development codex[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#agent_instructionsmd---your-development-codex)

This is your main context file. It should contain everything an AI agent needs to understand your project from a development perspective. Here’s what I include:

**Project vision and goals**: What you’re building and why. This helps agents understand the broader context when making suggestions.

**Technical architecture**: Your stack, project structure, and key architectural decisions. Be specific about which frameworks, patterns, and tools you’re using.

**Development standards**: Coding conventions, naming patterns, and quality requirements. If you have specific ways of doing things, document them here.

**Current priorities**: What you’re working on right now and what’s coming next. This helps agents focus their suggestions on relevant areas.

Here’s a condensed example from one of my SaaS projects:

```
# SaaS Development Agent Instructions

## Project Vision
SiteCentral is a premium content management platform competing with PlatformX and PlatformY, targeting global enterprises with an emphasis on outstanding user experience and performance.

## Technical Architecture
- Three-project Blazor Server + WebAssembly solution (.NET 9)
- **SiteCentral.App**: Core user-facing application  
- **SiteCentral.AdminConsole**: Administrative portal with Azure Entra ID integration  
- **SiteCentral.Core**: Shared business logic and data-access layer  

## Development Standards
- Bootstrap 5.3.3 with custom CSS variables for flexible theming  
- Entity Framework Core, with migrations applied only via the main application  
- Role-based authorization using ASP.NET Core Identity  
- Component-driven architecture ensuring clear separation of concerns  
```

### AGENT\_SESSION\_MEMORY.md - Persistent context[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#agent_session_memorymd---persistent-context)

This file bridges the gap between sessions. When an AI agent helps you solve a problem or implement a feature, you can capture the key decisions and learnings here. It’s like leaving notes for your future self and future AI interactions.

I structure this file chronologically with clear headings:

```
# Agent Session Memory

## June 2025 - Authentication Enhancement
- Implemented Azure Entra ID integration for admin portal
- Key decision: Separate authentication contexts for main app vs admin
- Learning: PowerShell scripts for validation work better than manual testing

## May 2025 - Waitlist Management System
- Completed full waitlist functionality with enhanced UX
- Generated 8-digit numeric invite codes instead of random strings
- Created comprehensive admin interface with real-time statistics
```

### Domain-specific documentation[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#domain-specific-documentation)

For complex projects, I create additional files that capture domain-specific knowledge. In my SaaS project, I have files like `TOKEN_GENERATION_SUMMARY.md` that document how specific features work:

```
# Token Generation Implementation Summary

## Overview
Token generation uses JWT with custom claims for API access and admin privileges.

## Implementation Details
- Service: `TokenService` in SaaS.Shared.Core
- Configuration: appsettings.json with environment-specific keys
- Validation: Custom middleware for token validation and refresh

## Usage Patterns
- Admin tokens: 24-hour expiry with elevated claims
- User tokens: 7-day expiry with collection access claims
```

### BUILD\_AND\_DEPLOYMENT\_NOTES.md - Operational knowledge[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#build_and_deployment_notesmd---operational-knowledge)

Don’t forget the operational side. This file contains the practical information agents need to help with builds, deployments, and troubleshooting:

```
# Build and Deployment Notes

## Local Development
- Run migrations: `dotnet ef database update` from SaaS.Application
- Start main app: `dotnet run --project src/SaaS.Application`
- Start admin portal: `dotnet run --project src/SaaS.AdminPortal`

## Common Issues
- Connection string conflicts: Check appsettings.Development.json
- Migration errors: Ensure running from correct project directory
- Authentication failures: Verify Azure Entra ID configuration
```

## Real-world example: The SaaS project[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#real-world-example-the-saas-project)

Let me show you how this works in practice with my SaaS project. It’s a Blazor-based collection management platform with a three-project architecture. The instruction directory has been absolutely crucial for maintaining context across development sessions.

When I start a new session with GitHub Copilot, I begin with something like:

```
@workspace I'm working on the SaaS project. Please read the
instructions/AGENT_INSTRUCTIONS.md file first to understand the project 
context and development guidelines. I need help implementing a new feature 
for bulk card imports.
```

The agent immediately understands:

-   The project architecture (three Blazor projects with shared core)
-   Which project to put new features in (main app vs admin portal)
-   The coding standards and patterns we follow
-   The current development priorities and constraints

Instead of starting with generic suggestions, the agent gives contextually appropriate recommendations that fit the existing architecture and patterns.

## How to integrate this with your workflow[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#how-to-integrate-this-with-your-workflow)

Start small and build up. Here’s the approach I recommend:

**Week 1**: Create the basic structure with just `AGENT_INSTRUCTIONS.md`. Include your project overview, tech stack, and any immediate context an agent would need.

**Week 2**: Add `AGENT_SESSION_MEMORY.md` and start capturing key decisions and learnings from your AI interactions.

**Week 3**: Create domain-specific files for complex areas of your codebase. Build and deployment notes if you have specific procedures.

**Week 4**: Start asking agents to generate reports and documentation that you can store in the `agent_reports/` subfolder.

The key is to make this part of your natural workflow. When an AI agent helps you solve a problem, spend 30 seconds updating your session memory. When you make an architectural decision, capture it in the instructions file.

## Common mistakes and how to avoid them[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#common-mistakes-and-how-to-avoid-them)

**Mistake 1: Writing for humans, not AI agents** Your instruction files should be clear and structured, but optimised for AI consumption. Use headings, bullet points, and clear categories rather than prose.

**Mistake 2: Not updating files as the project evolves** Stale documentation is worse than no documentation. Make updating your instruction files part of your definition of done for features.

**Mistake 3: Being too generic** Don’t just copy-paste generic project information. Include the specific decisions, patterns, and constraints that make your project unique.

**Mistake 4: Ignoring the feedback loop** When agents give you good suggestions, capture the reasoning in your instruction files. This improves future interactions.

## Advanced tips for maximum effectiveness[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#advanced-tips-for-maximum-effectiveness)

**Reference files explicitly in prompts**: Don’t assume agents will read your instruction files automatically. Reference them directly: “Please review instructions/AGENT\_INSTRUCTIONS.md before suggesting changes.”

**Use consistent terminology**: If you call something a “binder” in your codebase, use “binder” in your instruction files. Consistency helps agents understand your domain language.

**Include negative examples**: Document what NOT to do as well as what to do. “Don’t create new database contexts - use the shared ApplicationDbContext.”

**Version your instruction files**: Keep your instruction files in source control and update them as your project evolves. They’re as important as your code.

**Create templates for common requests**: I have standard prompts that reference my instruction files for common tasks like “implementing a new feature” or “refactoring existing code.”

## The results speak for themselves[](https://www.ctco.blog/posts/github-copilot-tips-and-tricks#the-results-speak-for-themselves)

Since implementing this approach with one SaaS projects, I’ve seen dramatic improvements in AI agent effectiveness:

-   **Context retention**: Agents remember architectural decisions and patterns between sessions
-   **Relevant suggestions**: Recommendations fit the existing codebase rather than being generic
-   **Faster onboarding**: New features get implemented following established patterns automatically
-   **Better documentation**: The instruction files serve as living documentation for human developers too

The time investment upfront pays dividends quickly. Instead of spending time explaining context in every interaction, agents immediately understand your project and provide contextually appropriate help.

Most importantly, this approach scales. As your project grows in complexity, your instruction directory grows with it, maintaining that crucial context that makes AI agents genuinely useful rather than just clever.

If you’re serious about using GitHub Copilot agents effectively, stop treating each interaction as a one-off conversation. Build the context structure, maintain it as part of your workflow, and watch how much more effective your AI-assisted development becomes.

The instruction directory method isn’t just a productivity hack - it’s a fundamental shift in how you structure knowledge for human-AI collaboration. Give it a try, and I guarantee you’ll wonder how you ever worked without it.