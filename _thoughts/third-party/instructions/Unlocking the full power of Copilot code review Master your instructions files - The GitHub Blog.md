---
created: 2025-11-20T12:36:44 (UTC -03:00)
tags: []
source: https://github.blog/ai-and-ml/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files/
author: Ria Gopu
---

# Unlocking the full power of Copilot code review: Master your instructions files - The GitHub Blog

> ## Excerpt
> Ready to make your code reviews smarter and easier? Learn how to structure your instructions files for better results, avoid common pitfalls, and see real-world examples to get started. 🚀

---
Copilot code review (CCR) helps you automate code reviews and ensure your project meets your team’s standards. We recently added support for both `copilot-instructions.md` and path-specific `*.instructions.md` files, so now you can customize Copilot’s behavior to fit your workflow. This flexibility empowers you to guide Copilot with clear, actionable rules for effective and consistent reviews.

But with this flexibility comes some uncertainty:

-   When is Copilot code review reading your instructions?
-   Why doesn’t it always follow your instructions exactly?
-   How can you ensure Copilot code review listens to your guidance?

While you can format your instructions file however you want, Copilot code review is non-deterministic and has specific limitations that will evolve as we improve the product. Understanding how to guide Copilot within its current capabilities is key to getting the most from your reviews.

After reviewing many instructions files, common questions, and feedback, we’ve created this guide to help you write instructions that really work—and avoid some pitfalls along the way.

⚠️ Note: While these tips are designed for Copilot code review, you might find some of them useful when writing instructions files for other Copilot products.

## **General tips**

Getting started is the hardest part. Here are some things to keep in mind when starting with your instructions. 

-   **Keep it concise:** Copilot works best with focused, short instructions. Start small and iterate. Even a single line can help guide Copilot. On the flip side, long instructions files (over ~1,000 lines) can lead to inconsistent behavior.
-   **Structure matters:** Use headings and bullet points to keep information organized and easy for Copilot to process.
-   **Be direct:** Short, imperative rules are more effective than long paragraphs.
-   **Show examples:** Demonstrate concepts with sample code or explanations—just like you would with a teammate.

## **Repo-wide vs. path-specific instructions**

In addition to the centralized repo-wide `copilot-instructions.md` file, we recently expanded your customization options by enabling Copilot code review to read any `NAME.instructions.md` file with an `applyTo` frontmatter in your `.github/instructions` directory. It can be confusing to have two seemingly similar options for customization, but each provides different value! Here are some tips for how to differentiate between the two, and use them both effectively.

-   Place language-specific rules in `*.instructions.md` files and then use the `applyTo` frontmatter property to target specific languages (e.g., `applyTo: **/*.py` or `applyTo: documentation/*.md`).
-   Place rules meant specifically for only Copilot code review or only Copilot coding agent in `*.instructions.md` files, and use the `excludeAgent` frontmatter property to prevent either agent from reading your file.
-   Organize different topics (e.g., security, language-specific guidelines, etc.) into separate `*.instructions.md` files.
-   Reserve general instructions, team standards, and guidelines for the whole repository for `copilot-instructions.md` (e.g., “Flag use of deprecated libraries across the codebase”).

## **Rules of thumb**

Effective instructions files often include:

1.  Clear titles
2.  A purpose or scope statement to clarify intent
3.  Lists of guidelines/rules instead of dense paragraphs
4.  Best practice recommendations
5.  Style conventions (indentation, naming, organization)
6.  Sample code blocks for clarification
7.  Section headings for organization
8.  Task-specific instructions (e.g., for tests or endpoints)
9.  Language/tooling context
10.  Emphasis on readability and consistency
11.  Explicit directives for Copilot (“Prefer X over Y”)

## **What not to do**

Certain types of instructions aren’t supported by Copilot code review. Here are common pitfalls to avoid:

-   Trying to **change the UX or formatting of Copilot comments** (e.g., “Change the font of Copilot code review comments”).
-   Trying to **modify the “Pull Request Overview” comment** (e.g. prompting to remove it or change its purpose to be something other than provide an overview of the pull request).
-   Requesting Copilot code review **performs tasks outside of code review**. (e.g., trying to modify the product behavior like asking it to block a pull request from merging).
-   Including **external links.** Copilot won’t follow them. You should copy relevant info into your instructions files instead.
-   Adding **requests meant to generally and non-specifically improve behavior** (e.g., “Be more accurate” or “Identify all issues”). Copilot code review is already tuned to do this and adding language like this adds more noise that confuses the LLM.

## **Recommended structure for instructions files**

Starting off with a blank Markdown file can feel daunting. Here’s one structure that you can use, ready to copy-paste into your instructions file as a starting point!

````
# [Your Title Here]
*Example: ReactJS Development Guidelines*

## Purpose & Scope
Briefly describe what this file covers and when to use it.

---

## Naming Conventions
- [Add rules here, e.g., "Use camelCase for variable names."]

## Code Style
- [Add rules here, e.g., "Indent using 2 spaces."]

## Error Handling
- [Add rules here.]

## Testing
- [Add rules here.]

## Security
- [Add rules here.]

---

## Code Examples
```js
// Correct pattern
function myFunction() { ... }

// Incorrect pattern
function My_function() { ... }
```

---

## [Optional] Task-Specific or Advanced Sections

### Framework-Specific Rules
- [Add any relevant rules for frameworks, libraries, or tooling.]

### Advanced Tips & Edge Cases
- [Document exceptions, advanced patterns, or important caveats.]
````

## **Example: A `typescript.instructions.md` file**

Now let’s implement all of these guidelines in an example path-specific instruction file.

````
---
applyTo: "**/*.ts"
---
# TypeScript Coding Standards
This file defines our TypeScript coding conventions for Copilot code review.

## Naming Conventions

- Use `camelCase` for variables and functions.
- Use `PascalCase` for class and interface names.
- Prefix private variables with `_`.

## Code Style

- Prefer `const` over `let` when variables are not reassigned.
- Use arrow functions for anonymous callbacks.
- Avoid using `any` type; specify more precise types whenever possible.
- Limit line length to 100 characters.

## Error Handling

- Always handle promise rejections with `try/catch` or `.catch()`.
- Use custom error classes for application-specific errors.

## Testing

- Write unit tests for all exported functions.
- Use [Jest](https://jestjs.io/) for all testing.
- Name test files as `<filename>.test.ts`.

## Example

```typescript
// Good
interface User {
  id: number;
  name: string;
}

const fetchUser = async (id: number): Promise<User> => {
  try {
    // ...fetch logic
  } catch (error) {
    // handle error
  }
};

// Bad
interface user {
  Id: number;
  Name: string;
}

async function FetchUser(Id) {
  // ...fetch logic, no error handling
}
````

## **Get started**

### Getting started with Copilot code review

New to Copilot code review? Get started by [adding Copilot as a reviewer](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#using-copilot-code-review) to your pull requests! 

### Adding new custom instructions

Create a `copilot-instructions.md` file in the `.github` directory of your repository, or a path-specific `*.instructions.md` file within the `.github/instructions` directory in your repository, and use this post and [examples in the awesome-copilot repository](https://github.com/github/awesome-copilot/tree/main/instructions) for inspiration.

Or just [ask Copilot coding agent](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions#asking-copilot-coding-agent-to-generate-a-copilot-instructionsmd-file) to generate an instructions file for you, and iterate from there. 

### Editing existing custom instructions

Have existing custom instructions for Copilot code review that you think could use some editing after reading this post, but don’t know where to begin? Have Copilot coding agent edit your file for you!

1.  Navigate to the agents page at [github.com/copilot/agents](https://github.com/copilot/agents).
2.  Using the dropdown menu in the prompt field, select the repository and branch where you want Copilot to edit custom instructions.

Copy the following prompt, editing it for your use-case as needed. **Make sure to modify the first sentence to specify which instruction files you want it to edit.** This prompt will tailor your instructions file for Copilot code review, so it may make unwanted edits if used for instruction files meant for other agents.

````
**Prompt for Copilot Coding Agent: Revise My Instructions File**

---
Review and revise my existing `NAME-OF-INSTRUCTION-FILES` files. Preserve my file's meaning and intention—do NOT make unnecessary changes or edits. Only make improvements where needed, specifically:

- Remove unsupported or redundant content.  
  Unsupported content includes:
  - instructions to change Copilot code review comment formatting (font, font size, adding headers, etc)
  - instructions to change "PR Overview" comment content
  - instructions for product behavior changes outside of existing code review functionality (like trying to block a pull request from merging)
  - Vague, non-specific directives like “be more accurate”, "identify all issues" or similar
  - Directives to “follow links” or inclusion of any external links
- Reformat sections for clarity if they do not have any structure. 
  - If my file does not have any structure, reformat into the structure below or similar, depending on the topics covered in the file. 
  - Do not change the intent or substance of the original content unless the content is not supported.
- Organize content with section headings and bullet points or numbered lists.
- Add sample code blocks if clarification is needed and they are missing.
- When applicable, separate language-specific rules into path-specific instructions files with the format `NAME.instructions.md`, with the `applyTo` property, if not already done.
- If the file is over 4000 characters long, prioritize shortening the file by identifying redundant instructions, instructions that could be summarized, and instructions that can be removed due to being unspported. 

**Example Structure:**

# Python Coding Standards

Guidelines for Python code reviews with Copilot.

## Naming Conventions

- Use `snake_case` for functions and variables.
- Use `PascalCase` for class names.

## Code Style

- Prefer list comprehensions for simple loops.
- Limit lines to 80 characters.

## Error Handling

- Catch specific exceptions, not bare `except:`.
- Add error messages when raising exceptions.

## Testing

- Name test files as `test_*.py`.
- Use `pytest` for tests.

## Example

```python
# Good
def calculate_total(items):
    return sum(items)

# Bad
def CalculateTotal(Items):
    total = 0
    for item in Items:
        total += item
    return total
```

---

### Framework-Specific Rules
- For Django, use class-based views when possible.

### Advanced Tips & Edge Cases
- Use type hints for function signatures.
````

4.  Click **Start task** or press Return.

Copilot will start a new session, which will appear in the list below the prompt box. Copilot will create a draft pull request, modify your custom instructions, push them to the branch, then add you as a reviewer when it has finished. This will trigger a notification for you.

## **Resources to check out**

-   [Copilot code review custom instructions example in GitHub docs](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/code-reviewer)
-   [awesome-copilot repository of instructions examples](https://github.com/github/awesome-copilot/tree/main/instructions)

Customizing with Copilot instructions files makes code review work for you—give it a try and see the difference in your workflow!

## Written by

 ![Ria Gopu](https://avatars.githubusercontent.com/u/189655821?v=4&s=200)

## Explore more from GitHub

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

### Docs

Everything you need to master GitHub, all in one place.

[Go to Docs](https://docs.github.com/)

![GitHub](https://github.blog/wp-content/uploads/2024/07/Icon_95220f.svg)

### GitHub

Build what’s next on GitHub, the place for anyone from anywhere to build anything.

[Start building](https://github.com/)

![Customer stories](https://github.blog/wp-content/uploads/2024/07/Icon_da43dc.svg)

### Customer stories

Meet the companies and engineering teams that build with GitHub.

[Learn more](https://github.com/customer-stories)

![The GitHub Podcast](https://github.blog/wp-content/uploads/2023/02/galaxy23-icon.svg)

### The GitHub Podcast

Catch up on the GitHub podcast, a show dedicated to the topics, trends, stories and culture in and around the open source developer community on GitHub.

[Listen now](https://the-github-podcast.simplecast.com/)
