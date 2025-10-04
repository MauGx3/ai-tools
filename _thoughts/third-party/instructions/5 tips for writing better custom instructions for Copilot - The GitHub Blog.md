If you’ve read any of my stuff or listened to one of my presentations before, you’ve likely heard my snarky joke: “Don’t be passive aggressive with Copilot.” 

My point with this joke is serious, though. Copilot works best when you give it the right context. Just like a new teammate, it can’t read your mind (even if it sometimes feels like it can).

Copilot can likely figure out what you’re doing and how you’re doing it. But spelling out the essentials – what you’re building, the stack you’re using, the rules to follow, etc., will help avoid confusion and mistakes.

This is why instructions files are so important. They’re your chance to give Copilot that background, that institutional knowledge the rest of your team has from their experience with the project.

The centerpiece for Copilot is `copilot-instructions.md`, the file which is read on every Copilot chat or agent request.

So how should one be crafted?

To help you avoid the blank-page problem, here are five things every instruction file should include (plus a bonus tip on how Copilot can even help you write the file itself).

## Before we get started

One important tip I want to share before we get into more details is to not overthink things. There isn’t a specific prescribed way to write instructions files. The nature of generative AI is probabilistic, meaning the same requests can actually render different results. Your goal is to tilt the scales, to help point Copilot to finding the answer you’re hoping for as often as possible.

The five sections (and bonus tip) below aren’t meant as requirements, but recommendations. In my experience, having these sections, or at the very least the key information indicated by these sections, in your instructions file will vastly increase the quality of suggestions from Copilot.

You should use these as a starting point, and experiment and explore based on your projects, models, and experience with Copilot.

## Give GitHub Copilot a project overview

It’s tough to write code for an app if you don’t know what the app is! The same thing is true for GitHub Copilot, and that’s where a project overview instructions file can be exceptionally helpful. 

The header for your instructions file should be the elevator pitch for your app. What’s the app? Who’s the audience? What are the key features? It doesn’t need to be long, just a few sentences to set the stage.

Here’s an example of a project overview for an instructions file:

```
# Contoso Companions

This is a website to support pet adoption agencies. Agencies are onboarded into the application, where they can manage their locations, available pets, and publicize events. Potential adoptors can search for pets available in their area, discover agencies, and submit adoption applications.
```

The above example is clear, direct, and simple. You don’t need to write the Magna Carta, but it’s important to give Copilot some context around what you’re trying to accomplish at a high level. And this example app totally isn’t a way for me to convince myself to adopt a new pet (seriously, it’s not and I’m not just telling myself that). 

## Identify the tech stack you’re using in your project 

Once you’ve identified what you’re building, the next thing to identify is what you’re using to build it. This includes the backend and frontend tech you’re using, any APIs you’re calling, and any testing suites you’re targeting. After all, the number of frameworks alone to create a website is always growing. Case in point? Three new JavaScript frameworks have probably launched since you started reading this blog post!

You don’t need to channel your inner George RR Martin when creating instructions files, crafting paragraphs upon paragraphs explaining the minutiae. Instead, think about creating a list highlighting the tech you’re using, and maybe add a note or two about how they’re being used. This will help Copilot understand the environment in which it’s creating code.  
Here’s a quick example from my own work for reference: 

```
## Tech stack in use

### Backend

- Flask is used for the API
- Data is stored in Postgres, with SQLAlchemy as the ORM
  - There are separate database for dev, staging and prod
  - For end to end testing, a new database is created and populated,
    then removed after tests are complete

### Frontend

- Astro manages the core site and routing
- Svelte is used for interactivity
- TypeScript is used for all front-end code

### Testing

- Unittest for Python
- Vitest for TypeScript
- Playwright for e2e tests
```

## Spell out your coding guidelines

Before you create your first pull request, you need to know the guidelines you should be following. Some of this is about how the code should be written. Are we using semicolons for JavaScript or TypeScript, for instance? Type hints for Python? Tabs or spaces? (The only correct answers are yes, yes, and spaces. I won’t be taking any questions.)

Depending on your project structure, you could incorporate your guidelines into your tech stack instructions file. But I generally like having a separate section for guidelines, as many of them will apply across all languages in use. I find it to be more readable, which is important for maintainability, and there’s often crossover of guidance between languages and frameworks.

You can also consider using [.instructions files](https://code.visualstudio.com/docs/copilot/copilot-customization#_use-instructionsmd-files) for guidelines for specific types of files, like all `.astro` or `.jsx` files, or unit tests which might match a pattern of `/tests/test_*.py`.

Here’s another example from some of my own work: 

```
## Project and code guidelines

- Always use type hints in any language which supports them
- JavaScript/TypeScript should use semicolons
- Unit tests are required, and are required to pass before PR
  - Unit tests should focus on core functionality
- End-to-end tests are required
  - End-to-end tests should focus on core functionality
  - End-to-end tests should validate accessibility
- Always follow good security practices
- Follow RESTful API design principles
- Use scripts to perform actions when available
```

## Explain your project structure

Just as there are countless frameworks and ways to write your code, there’s a seemingly infinite number of ways to structure a project. In a monorepo structure, for instance, your front end could be in a folder called frontend. Or front-end. Or front\_end. Or client. Or web…

I think you see where this is going. 

And while Copilot could certainly figure it out, a quick ls command can reveal the answer. But listing your project structure in a custom instructions file both saves Copilot a bit of work, and gives you an opportunity to provide a little more context about what’s in the folders.

Here’s an example:

```
## Project structure

- server/ : Flask backend code
  - models/ : SQLAlchemy ORM models
  - routes/ : API endpoints organized by resource
  - tests/ : Unit tests for the API
  - utils/ : Utility functions and helpers, including database calls
- client/ : Astro/Svelte frontend code
  - src/components/ : Reusable Svelte components
  - src/layouts/ : Astro layout templates
  - src/pages/ : Astro pages and routes
  - src/styles/ : CSS stylesheets
- scripts/ : Development, deployment and testing scripts
- docs/ : Project documentation to be kept in sync at all times
```

## Point GitHub Copilot to available resources

Almost every project has a set of scripts or resources available to aid in development. These might be scripts to streamline setup or running tests, or software factories to generate code or templates. The introduction of [MCP support in VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) and [Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp) in particular opens up even more tools for Copilot’s agents to use. 

We already established that Copilot can discover what’s available to it, but a couple of pointers in the right direction via a custom instructions file will increase accuracy and speed.

Here’s an example: 

```
## Resources

- scripts folder
  - start-app.sh : Installs all libraries and starts the app
  - setup-env.sh : Installs all libraries
  - test-project.sh : Installs all libraries, runs unit and e2e tests
- MCP servers
  - Playwright: Used for generating Playwright tests or interacting with site
  - GitHub: Used to interact with repository and backlog
```

## Bonus tip: Get GitHub Copilot to help you create your custom instructions file

There isn’t one perfect way to create instructions files, and something is always better than nothing. That said, we all want to get it right, or as close to right as possible. Hopefully the guidelines above have given you inspiration!

But there’s still the matter of actually writing them out. And that still might leave you with the blank page problem we started with.

Fortunately, Copilot can help you help Copilot!

You can prompt Copilot agent mode in your IDE (or [assign an issue to Copilot](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/assign-copilot-to-an-issue) in your GitHub repository) to ask it to create your instructions file. You could use this file as is, or edit it as you see fit. There’s even a [recommended prompt in our Docs on Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions#using-a-single-githubcopilot-instructionsmd-file-1) you can use to generate the instructions file! A streamlined version of the full recommendation could look like this:

```
Your task is to "onboard" this repository to a coding agent by adding a .github/copilot-instructions.md file. It should contain information describing how the agent, seeing the repo for the first time, can work most efficiently.

You will do this task only one time per repository, and doing a good job can SIGNIFICANTLY improve the quality of the agent's work, so take your time, think carefully, and search thoroughly before writing the instructions.

## Goals

- Document existing project structure and tech stack.
- Ensure established practices are followed. 
- Minimize bash command and build failures.

## Limitations
- Instructions must be no longer than 2 pages.
- Instructions should be broadly applicable to the entire project.

## Guidance

Ensure you include the following:

- A summary of what the app does.
- The tech stack in use
- Coding guidelines
- Project structure
- Existing tools and resources

## Steps to follow

- Perform a comprehensive inventory of the codebase. Search for and view:
  - README.md, CONTRIBUTING.md, and all other documentation files.
  - Search the codebase for indications of workarounds like 'HACK', 'TODO', etc.
- All scripts, particularly those pertaining to build and repo or environment setup.
- All project files.
- All configuration and linting files.
- Document any other steps or information that the agent can use to reduce time spent exploring or trying and failing to run bash commands.

## Validation

Use the newly created instructions file to implement a sample feature. Use the learnings from any failures or errors in building the new feature to further refine the instructions file.
```

Using the above prompt can help you save time. But more importantly, it can also help you clarify your thoughts and goals around any given project. 

## Last words on instructions files

To be clear, providing instructions doesn’t guarantee perfect code. But having a good instructions file is a great first step towards increasing the quality of code suggestions from Copilot. If you ask me, having a `copilot-instructions.md` file is a requirement for any project where you’re using Copilot.

And again – it doesn’t need to be perfect. Starting with these sections will provide a great foundation from which to build:

-   Elevator pitch of what you’re building
-   Frameworks and the tech stack you’re using to build it
-   Coding and other project guidelines
-   Project structure and where to find things
-   Resources available for automation and tasks

From there you can begin to explore [.instructions files](https://code.visualstudio.com/docs/copilot/copilot-customization#_use-instructionsmd-files) for more specific guidance for Copilot. But it all starts with [`copilot-instructions.md`](http://copilot-instructions.md/). 

[**Read the Docs**](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) to learn more about custom instructions in GitHub Copilot >

## Written by

 ![Christopher Harrison](https://avatars.githubusercontent.com/u/6109729?v=4&s=200)

Senior Developer Advocate, GitHub

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

![GitHub Universe 2025](https://github.blog/wp-content/uploads/2024/04/Universe24-North_Star.svg)

### GitHub Universe 2025

Last chance: Save $700 on your IRL pass to Universe and join us on Oct. 28-29 in San Francisco.

[Register now](https://githubuniverse.com/?utm_source=Blog&utm_medium=GitHub&utm_campaign=module)