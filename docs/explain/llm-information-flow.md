---
title: "LLM Information Flow"
type: "explanation"
layout: "default"
description: "Comprehensive flowchart explaining how information is shared between prompts, instructions, agents, modes, and the Memory Bank in the ai-tools repository"
---

# LLM Information Flow and Architecture

This document provides a comprehensive visual guide to understanding how information flows between different LLM-related components in the ai-tools repository: prompts, instructions, agents, modes, and the Memory Bank.

## Overview

The ai-tools repository uses a layered architecture where different types of files serve specific purposes in guiding AI behavior:

- **Prompts** (`_prompts/`): Reusable interaction templates for specific tasks
- **Instructions** (`_instructions/`): Machine-oriented guidance with scoping rules
- **Agents** (`_agents/`): Interactive personas with specific tool access
- **Modes** (`_modes/`): Interaction configurations and system prompts
- **Memory Bank** (`memory-bank/`): Persistent project context and state

## Complete Information Flow Architecture

```mermaid
flowchart TB
    subgraph UserInput["👤 User Interaction"]
        UserRequest[User Request/Task]
        UserFeedback[User Feedback]
    end

    subgraph Discovery["🔍 Discovery & Context Loading"]
        LoadMemoryBank[Read Memory Bank Files]
        LoadInstructions[Load Applicable Instructions]
        LoadPrompts[Identify Relevant Prompts]
        ConfidenceCheck{Confidence >= 97%?}
    end

    subgraph MemoryBank["💾 Memory Bank (State & Context)"]
        ProjectBrief[projectbrief.md<br/>Core Requirements]
        ProductContext[productContext.md<br/>Why & How]
        SystemPatterns[systemPatterns.md<br/>Architecture]
        TechContext[techContext.md<br/>Tech Stack]
        
        ActiveContext[activeContext.md<br/>Current Work]
        Progress[progress.md<br/>Status]
        Tasks[tasks/ folder<br/>Task Files]
        
        ProjectBrief --> ActiveContext
        ProductContext --> ActiveContext
        SystemPatterns --> ActiveContext
        TechContext --> ActiveContext
        
        ActiveContext --> Progress
        ActiveContext --> Tasks
    end

    subgraph Instructions["📋 Instructions Layer"]
        GlobalInstructions[Global Instructions<br/>applyTo: '**']
        DomainInstructions[Domain Instructions<br/>applyTo: specific patterns]
        LanguageInstructions[Language Instructions<br/>applyTo: '**/*.py, **/*.js']
        
        ApplyToMatch{Match applyTo<br/>patterns?}
        
        GlobalInstructions --> ApplyToMatch
        DomainInstructions --> ApplyToMatch
        LanguageInstructions --> ApplyToMatch
    end

    subgraph Prompts["💬 Prompts Library"]
        PromptTemplates[Prompt Templates<br/>_prompts/]
        PromptMetadata[Metadata:<br/>title, type, audience]
        PromptExamples[Usage Examples]
        
        PromptTemplates --> PromptMetadata
        PromptTemplates --> PromptExamples
    end

    subgraph Agents["🤖 Agents"]
        AgentDef[Agent Definition<br/>.AGENTS.md]
        AgentPersona[Persona & Role]
        AgentTools[Tool Access]
        AgentHandoffs[Handoff Rules]
        
        AgentDef --> AgentPersona
        AgentDef --> AgentTools
        AgentDef --> AgentHandoffs
    end

    subgraph Modes["⚙️ Modes"]
        ModeConfig[Mode Configuration<br/>_modes/]
        SystemPrompt[System Prompt]
        Settings[Temperature, Tokens, etc.]
        
        ModeConfig --> SystemPrompt
        ModeConfig --> Settings
    end

    subgraph Processing["🔄 Agent Processing"]
        AnalyzeContext[Analyze Combined Context]
        SelectStrategy[Select Strategy/Approach]
        ValidateRules[Validate Against Rules]
        ExecuteTask[Execute Task]
    end

    subgraph Output["📤 Output & Documentation"]
        GenerateResponse[Generate Response]
        UpdateMemoryBank[Update Memory Bank]
        UpdateTasks[Update Task Status]
        CommitChanges[Commit Changes]
        DocumentDecisions[Document Decisions]
    end

    %% Main Flow
    UserRequest --> LoadMemoryBank
    UserRequest --> LoadInstructions
    UserRequest --> LoadPrompts
    
    LoadMemoryBank --> MemoryBank
    LoadInstructions --> Instructions
    LoadPrompts --> Prompts
    
    MemoryBank --> ConfidenceCheck
    Instructions --> ConfidenceCheck
    Prompts --> ConfidenceCheck
    
    ConfidenceCheck -->|No| UserFeedback
    UserFeedback --> UserRequest
    ConfidenceCheck -->|Yes| ApplyToMatch
    
    ApplyToMatch -->|Matched| AnalyzeContext
    ApplyToMatch -->|Not Matched| AnalyzeContext
    
    Agents -.->|Optional| AnalyzeContext
    Modes -.->|Optional| AnalyzeContext
    
    AnalyzeContext --> SelectStrategy
    SelectStrategy --> ValidateRules
    ValidateRules --> ExecuteTask
    
    ExecuteTask --> GenerateResponse
    GenerateResponse --> UpdateMemoryBank
    UpdateMemoryBank --> UpdateTasks
    UpdateTasks --> CommitChanges
    CommitChanges --> DocumentDecisions
    
    DocumentDecisions --> MemoryBank
    DocumentDecisions --> UserFeedback

    style MemoryBank fill:#e1f5ff
    style Instructions fill:#fff4e1
    style Prompts fill:#f0e1ff
    style Agents fill:#e1ffe1
    style Modes fill:#ffe1e1
    style ConfidenceCheck fill:#ffcccc
```

## Detailed Component Breakdown

### 1. Memory Bank Architecture

The Memory Bank maintains project state across sessions:

```mermaid
flowchart LR
    subgraph Foundation["Foundation Layer"]
        PB[projectbrief.md]
    end
    
    subgraph Context["Context Layer"]
        PC[productContext.md]
        SP[systemPatterns.md]
        TC[techContext.md]
    end
    
    subgraph Active["Active State"]
        AC[activeContext.md]
    end
    
    subgraph Tracking["Progress Tracking"]
        PR[progress.md]
        TF[tasks/]
    end
    
    PB --> PC
    PB --> SP
    PB --> TC
    
    PC --> AC
    SP --> AC
    TC --> AC
    
    AC --> PR
    AC --> TF

    style PB fill:#4a90e2
    style AC fill:#e94c4c
    style PR fill:#50c878
    style TF fill:#ffa500
```

### 2. Instruction File Scoping

How agents select applicable instructions:

```mermaid
flowchart TD
    Start[File Being Modified]
    
    CheckGlobal{Matches<br/>applyTo: '**'?}
    CheckDomain{Matches<br/>domain pattern?}
    CheckLanguage{Matches<br/>language pattern?}
    
    GlobalRules[Apply Global Instructions]
    DomainRules[Apply Domain Instructions]
    LanguageRules[Apply Language Instructions]
    
    Combine[Combine All Applicable Rules]
    Priority[Higher Specificity = Higher Priority]
    ApplyRules[Apply Final Rule Set]
    
    Start --> CheckGlobal
    CheckGlobal -->|Yes| GlobalRules
    CheckGlobal -->|No| CheckDomain
    
    CheckDomain -->|Yes| DomainRules
    CheckDomain -->|No| CheckLanguage
    
    CheckLanguage -->|Yes| LanguageRules
    CheckLanguage -->|No| Combine
    
    GlobalRules --> Combine
    DomainRules --> Combine
    LanguageRules --> Combine
    
    Combine --> Priority
    Priority --> ApplyRules

    style Start fill:#e1f5ff
    style Combine fill:#fff4e1
    style ApplyRules fill:#e1ffe1
```

### 3. Task Management Workflow

How tasks are created, tracked, and completed:

```mermaid
flowchart TD
    NewTask[New Task Request]
    CreateFile[Create TASKID-name.md]
    
    subgraph TaskFile["Task File Contents"]
        Status[Status: Pending/In Progress/Completed]
        Request[Original Request]
        Thought[Thought Process]
        Plan[Implementation Plan]
        Subtasks[Subtasks Table]
        ProgressLog[Progress Log]
    end
    
    UpdateIndex[Update _index.md]
    
    Execute[Execute Task]
    LogProgress[Add Progress Log Entry]
    UpdateSubtask[Update Subtask Status]
    UpdateStatus[Update Task Status]
    
    Complete{Task<br/>Complete?}
    MarkComplete[Mark as Completed]
    Continue[Continue Work]
    
    NewTask --> CreateFile
    CreateFile --> TaskFile
    TaskFile --> UpdateIndex
    
    UpdateIndex --> Execute
    Execute --> LogProgress
    LogProgress --> UpdateSubtask
    UpdateSubtask --> UpdateStatus
    UpdateStatus --> Complete
    
    Complete -->|Yes| MarkComplete
    Complete -->|No| Continue
    Continue --> Execute
    
    MarkComplete --> UpdateIndex

    style NewTask fill:#4a90e2
    style TaskFile fill:#fff4e1
    style Complete fill:#ffcccc
    style MarkComplete fill:#50c878
```

### 4. Agent Decision-Making Process

How agents process requests and decide actions:

```mermaid
flowchart TD
    AgentStart[Agent Receives Request]
    
    ReadMB[Read Memory Bank]
    ReadInst[Read Instructions]
    ReadPrompts[Read Relevant Prompts]
    
    CheckConf{Confidence<br/>>= 97%?}
    
    AskClarify[Ask Clarifying Question]
    
    AnalyzeTask[Analyze Task Requirements]
    CheckCustomAgent{Custom Agent<br/>Available?}
    
    DelegateAgent[Delegate to Custom Agent]
    ProcessSelf[Process Task Directly]
    
    SelectPrompt[Select Prompt Template]
    ApplyInstructions[Apply Instructions]
    ApplyMode[Apply Mode Settings]
    
    ValidateSecurity[Validate Security Rules]
    ValidateFormat[Validate Output Format]
    
    Execute[Execute Task]
    
    UpdateMB[Update Memory Bank]
    UpdateProgress[Update Progress]
    Commit[Commit Changes]
    
    AgentStart --> ReadMB
    ReadMB --> ReadInst
    ReadInst --> ReadPrompts
    
    ReadPrompts --> CheckConf
    CheckConf -->|No| AskClarify
    AskClarify --> AgentStart
    
    CheckConf -->|Yes| AnalyzeTask
    AnalyzeTask --> CheckCustomAgent
    
    CheckCustomAgent -->|Yes| DelegateAgent
    CheckCustomAgent -->|No| ProcessSelf
    
    DelegateAgent --> UpdateMB
    
    ProcessSelf --> SelectPrompt
    SelectPrompt --> ApplyInstructions
    ApplyInstructions --> ApplyMode
    
    ApplyMode --> ValidateSecurity
    ValidateSecurity --> ValidateFormat
    ValidateFormat --> Execute
    
    Execute --> UpdateMB
    UpdateMB --> UpdateProgress
    UpdateProgress --> Commit

    style CheckConf fill:#ffcccc
    style CheckCustomAgent fill:#fff4e1
    style Execute fill:#e1ffe1
    style UpdateMB fill:#e1f5ff
```

### 5. Information Priority Hierarchy

When conflicts arise, information sources have this priority:

```mermaid
flowchart TD
    Conflict[Information Conflict Detected]
    
    Check1{Memory Bank<br/>activeContext?}
    Check2{Specific<br/>Instruction?}
    Check3{General<br/>Instruction?}
    Check4{Prompt<br/>Template?}
    Check5{Mode<br/>Setting?}
    
    Use1[Use Memory Bank Decision]
    Use2[Use Specific Instruction]
    Use3[Use General Instruction]
    Use4[Use Prompt Template]
    Use5[Use Mode Default]
    
    AskUser[Ask User for Clarification]
    
    Conflict --> Check1
    Check1 -->|Found| Use1
    Check1 -->|Not Found| Check2
    
    Check2 -->|Found| Use2
    Check2 -->|Not Found| Check3
    
    Check3 -->|Found| Use3
    Check3 -->|Not Found| Check4
    
    Check4 -->|Found| Use4
    Check4 -->|Not Found| Check5
    
    Check5 -->|Found| Use5
    Check5 -->|Not Found| AskUser

    style Use1 fill:#4a90e2
    style Use2 fill:#50c878
    style Use3 fill:#ffa500
    style AskUser fill:#ffcccc
```

## Key Principles

### 1. **Memory Bank is Source of Truth**
The Memory Bank files (`memory-bank/`) contain the canonical project state and should be consulted at the start of every session.

### 2. **Instructions Use applyTo Scoping**
Instruction files include `applyTo` patterns (glob syntax) to define which files they apply to:
- `applyTo: '**'` - applies globally
- `applyTo: '**/*.py'` - applies to Python files
- `applyTo: 'scripts/*.py'` - applies only to Python files in scripts/

### 3. **Confidence Gate Enforcement**
Agents must express confidence percentage and ask clarifying questions if confidence < 97% before proceeding.

### 4. **Layered Guidance System**
- **Global Instructions**: Apply everywhere (security, memory bank, git)
- **Domain Instructions**: Apply to specific areas (python/, kubernetes/)
- **Language Instructions**: Apply to file types (\*.py, \*.js)

### 5. **Task-Driven Documentation**
Non-trivial work should be documented in `memory-bank/tasks/` with:
- Task ID and name
- Original request
- Thought process
- Implementation plan
- Progress tracking
- Progress log

## Usage Patterns

### When to Use Each Component

| Component | Use When | Example |
|-----------|----------|---------|
| **Prompt** | Quick prototyping, ad-hoc generation, interactive refinement | Code review template, documentation writer |
| **Instruction** | Consistent automated behavior, CI/CD rules, contributor guidance | Python coding standards, security checklist |
| **Agent** | Interactive persona with specific tools, complex workflows | Custom code reviewer, specialized analyzer |
| **Mode** | Setting interaction context, system behavior configuration | Advanced coding assistant, research mode |
| **Memory Bank** | Maintaining project state, tracking decisions, documenting context | Current focus, completed work, task history |

## Best Practices

### For Contributors

1. **Read Memory Bank First**: Always start by reading `projectbrief.md`, `activeContext.md`, and `progress.md`
2. **Follow applyTo Patterns**: When creating instructions, use specific patterns to avoid conflicts
3. **Update Documentation**: Document decisions and changes in Memory Bank files
4. **Use Conventional Commits**: Follow the commit message format specified in instructions
5. **No Hardcoded Secrets**: Use environment variables for all sensitive data

### For Agents

1. **Express Confidence**: Always state confidence percentage in responses
2. **Ask When Uncertain**: If confidence < 97%, ask clarifying questions
3. **Combine Context**: Use Memory Bank + Instructions + Prompts together
4. **Delegate When Possible**: Use custom agents for specialized tasks
5. **Document Changes**: Update Memory Bank files after significant changes

## Examples

### Example 1: Adding a New Python Script

**Information Flow:**
1. Agent reads Memory Bank → understands project structure
2. Agent loads `python.instructions.md` (matches `applyTo: '**/*.py'`)
3. Agent loads `security-and-owasp.instructions.md` (global security rules)
4. Agent checks confidence → 98% confident, proceeds
5. Agent creates script following Python conventions
6. Agent updates `activeContext.md` with decision
7. Agent commits with conventional commit message

### Example 2: Reviewing Code

**Information Flow:**
1. Agent reads task from `memory-bank/tasks/`
2. Agent loads relevant prompt: `code-review-assistant.md`
3. Agent loads instructions for file types being reviewed
4. Agent applies mode settings: `advanced-coding-assistant.md`
5. Agent performs review following combined guidance
6. Agent updates task progress log
7. Agent updates `progress.md` with review completion

## Related Documentation

- [Design and Memory Bank](./design-and-memory-bank.md) - Overview of Memory Bank concept
- [Add a Prompt or Instruction](../how-to/add-a-prompt-or-instruction.md) - How-to guide for adding new content
- [Prompt Engineering Best Practices](../guides/prompt-engineering-best-practices.md) - Best practices for prompts
- [Authoring Guidelines](../../memory-bank/authoring-guidelines.md) - Comprehensive authoring standards

## Maintenance

This document should be updated when:
- New component types are added to the repository
- Information flow patterns change significantly
- New best practices are established
- User feedback indicates confusion about information sharing

---

**Last Updated**: 2025-11-20  
**Status**: Active Documentation
