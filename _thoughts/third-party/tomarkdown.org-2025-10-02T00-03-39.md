# Effective context engineering for AI agents

Published Sep 29, 2025

Context is a critical but finite resource for AI agents. In this post, we explore strategies for effectively curating and managing the context that powers them.

After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: **context engineering**. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?"

**Context** refers to the set of tokens included when sampling from a large-language model (LLM). The **engineering** problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome. Effectively wrangling LLMs often requires _thinking in context_ — in other words: considering the holistic state available to the LLM at any given time and what potential behaviors that state might yield.

In this post, we’ll explore the emerging art of context engineering and offer a refined mental model for building steerable, effective agents.

#### Context engineering vs. prompt engineering

At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes (see [our docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) for an overview and useful prompt engineering strategies). **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

In the early days of engineering with LLMs, prompting was the biggest component of AI engineering work, as the majority of use cases outside of everyday chat interactions required prompts optimized for one-shot classification or text generation tasks. As the term implies, the primary focus of prompt engineering is how to write effective prompts, particularly system prompts. However, as we move towards engineering more capable agents that operate over multiple turns of inference and longer time horizons, we need strategies for managing the entire context state (system instructions, tools, [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP), external data, message history, etc).

An agent running in a loop generates more and more data that _could_ be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the [art and science](https://x.com/karpathy/status/1937902205765607626?lang=en) of curating what will go into the limited context window from that constantly evolving universe of possible information.

![Image 2: Prompt engineering vs. context engineering](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffaa261102e46c7f090a2402a49000ffae18c5dd6-2292x1290.png&w=3840&q=75)

_In contrast to the discrete task of writing a prompt, context engineering is iterative and the curation phase happens each time we decide what to pass to the model._

#### Why context engineering is important to building capable agents

Despite their speed and ability to manage larger and larger volumes of data, we’ve observed that LLMs, like humans, lose focus or experience confusion at a certain point. Studies on needle-in-a-haystack style benchmarking have uncovered the concept of [context rot](https://research.trychroma.com/context-rot): as the number of tokens in the context window increases, the model’s ability to accurately recall information from that context decreases.

While some models exhibit more gentle degradation than others, this characteristic emerges across all models. Context, therefore, must be treated as a finite resource with diminishing marginal returns. Like humans, who have [limited working memory capacity](https://journals.sagepub.com/doi/abs/10.1177/0963721409359277), LLMs have an “attention budget” that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM.

This attention scarcity stems from architectural constraints of LLMs. LLMs are based on the [transformer architecture](https://arxiv.org/abs/1706.03762), which enables every token to [attend to every other token](https://huggingface.co/blog/Esmail-AGumaan/attention-is-all-you-need) across the entire context. This results in n² pairwise relationships for n tokens.

As its context length increases, a model's ability to capture these pairwise relationships gets stretched thin, creating a natural tension between context size and attention focus. Additionally, models develop their attention patterns from training data distributions where shorter sequences are typically more common than longer ones. This means models have less experience with, and fewer specialized parameters for, context-wide dependencies.

Techniques like [position encoding interpolation](https://arxiv.org/pdf/2306.15595) allow models to handle longer sequences by adapting them to the originally trained smaller context, though with some degradation in token position understanding. These factors create a performance gradient rather than a hard cliff: models remain highly capable at longer contexts but may show reduced precision for information retrieval and long-range reasoning compared to their performance on shorter contexts.

These realities mean that thoughtful context engineering is essential for building capable agents.

#### The anatomy of effective context

Given that LLMs are constrained by a finite attention budget, _good_ context engineering means finding the _smallest_ _possible_ set of high-signal tokens that maximize the likelihood of some desired outcome. Implementing this practice is much easier said than done, but in the following section, we outline what this guiding principle means in practice across the different components of context.

**System prompts** should be extremely clear and use simple, direct language that presents ideas at the _right altitude_ for the agent. The right altitude is the Goldilocks zone between two common failure modes. At one extreme, we see engineers hardcoding complex, brittle logic in their prompts to elicit exact agentic behavior. This approach creates fragility and increases maintenance complexity over time. At the other extreme, engineers sometimes provide vague, high-level guidance that fails to give the LLM concrete signals for desired outputs or falsely assumes shared context. The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide strong heuristics for guiding behavior.

![Image 3: Calibrating the system prompt in the process of context engineering.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0442fe138158e84ffce92bed1624dd09f37ac46f-2292x1288.png&w=3840&q=75)

_At one end of the spectrum, we see brittle if-else hardcoded prompts; at the other end we see prompts that are overly general or falsely assume shared context._

We recommend organizing prompts into distinct sections (like `<background_information>`, `<instructions>`, `## Tool guidance`, `## Output description`, etc) and using techniques like XML tagging or Markdown headers to delineate these sections; however，the exact formatting of prompts is likely becoming less important as models become more capable.

Regardless of how you decide to structure your system prompt，you should be striving for\_the\_minimal\_set\_of\_information\_that\_fully\_outlines\_your\_expected\_behavior\_.(Note that minimal does not necessarily mean short; you still need to give th.e\_agent\_sufficient\_information\_up\_front\_to\_ensure\_it\_adheres\_to\_the\_desired\_behavior.\_It’s best to start by testing\_a\_minimal\_prompt\_with\_the\_best\_model\_available\_to\_see\_how\_it\_performs\_on\_your\_task,_and\_then\_add\_clear\_instructions\_and\_examples\_to\_improve\_performance\_based\_on\_failure\_modes\_found\_during\_initial\_testing._

**Tools** allow agents to operate with their environment and pull in new information as they work; because tools define th.e\_contract\_between\_agents\_and\_there\_environmental\_space\_as\_an\_agent\_works\_(see [writing tools for ai agents – with ai agents](https://www.anthropic.com/engineering/writing-tools-for-agents)), it’s extremely important that tools promote efficiency; both by returning information that is token efficient and by encouraging efficient agent behaviors.

In [Writing tools for AI agents – with AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents), we discussed building tools that are well understood by LLMs and have minimal overlap in functionality; similarto th.e\_functions\_of\_a\_well-designed\_codebase\_tools\_should\_be\_self-contained,\_robust\_to\_error,\_and\_extremely\_clear\_with\_respect\_to\_their\_intended\_use.\_Input\_parameters\_should\_similarity\_unambiguous,\_play\_to\_the\_inherent\_strengthsinthesemodel.\_One\_of\_the\_most\_common\_failure\_modes\_we\_see\_is\_bloated\_tool\_sets\_that\_cover too much functionality\_or\_lead tobumbound\_decision\_points\_about\_whireshouldbeused\_foradetaughttask.We do not recommendthis.\_Instead,_werecommendworking\_tocurate\_and\_keep\_your\_context\_informative,_yettight.Having examples,_otherwise\_known\_as\_few-shotprompting,_is awellknownbestpracticethatweseektobuildag.setofdiverse,canonicedemostratiofnetworksthateffectivelyoutpreferresthedefinedbehavior.oftheagent.ForandalLLM,fewshotexamplessaretheworthaplotofwords.Thefollowingoverallguidanceacrossthedifferentcomponentsofcontext(systemprompts_,tools_,few-shotexamples__,messagemessagehistory,e.t.c)_istobethoughtfulandeasytounveared,henceforthettingaminimumviablesetoftoolsfortheagentcanalsolenderto\_more\_reliablemaintenanceandpruningofcontextoverlonginteractions._

Providing examples,\_otherwise known assomehowassumesharingcontext.\_Our overall guidance across th.e\_componentsofcontext(_systemprompts_,`tools`,`examples`,`messages`)istobetactiveandkeepyourcontextinformative,andyettight.Nowletssinkintodynamicallyretrievingcontextatruntime.

#### Context engineering for long-horizon tasks

Long-horizon tasks require agents to maintain coherence, context, and goal-directed behavior over sequences of actions where the token count exceeds the LLM’s context window. For tasks that span tens of minutes to multiple hours of continuous work, like large codebase migrations or comprehensive research projects, agents require specialized techniques to work around the context window size limitation.

Waiting for larger context windows might seem like an obvious tactic. But it's likely that for the foreseeable future, context windows of all sizes will be subject to context pollution and information relevance concerns—at least for situations where the strongest agent performance is desired. To enable agents to work effectively across extended time horizons, we've developed a few techniques that address these context pollution constraints directly: compaction, structured note-taking, and multi-agent architectures.

#### Compaction

Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary. Compaction typically serves as the first lever in context engineering to drive better long-term coherence. At its core, compaction distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation.

In Claude Code, for example, we implement this by passing the message history to the model to summarize and compress the most critical details. The model preserves architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs or messages. The agent can then continue with this compressed context plus the five most recently accessed files. Users get continuity without worrying about context window limitations.

The art of compaction lies in the selection of what to keep versus what to discard, as overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later. For engineers implementing compaction systems, we recommend carefully tuning your prompt on complex agent traces. Start by maximizing recall to ensure your compaction prompt captures every relevant piece of information from the trace, then iterate to improve precision by eliminating superfluous content.

An example of low-hanging superfluous content is clearing tool calls and results – once a tool has been called deep in the message history, why would the agent need to see the raw result again? One of the safest lightest touch forms of compaction is tool result clearing, most recently launched as a feature on the Claude Developer Platform.

#### Structured note-taking

Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times.

This strategy provides persistent memory with minimal overhead. Like Claude Code creating a to-do list, or your custom agent maintaining a NOTES.md file, this simple pattern allows the agent to track progress across complex tasks, maintaining critical context and dependencies that would otherwise be lost across dozens of tool calls.

Claude playing Pokémon demonstrates how memory transforms agent capabilities in non-coding domains. The agent maintains precise tallies across thousands of game steps—tracking objectives like "for the last 1,234 steps I've been training my Pokémon in Route 1, Pikachu has gained 8 levels toward the target of 10." Without any prompting about memory structure, it develops maps of explored regions, remembers which key achievements it has unlocked, and maintains strategic notes of combat strategies that help it learn which attacks work best against different opponents.

After context resets, the agent reads its own notes and continues multi-hour training sequences or dungeon explorations. This coherence across summarization steps enables long-horizon strategies that would be impossible when keeping all the information in the LLM’s context window alone.

As part of our Sonnet 4.5 launch, we released a memory tool in public beta on the Claude Developer Platform that makes it easier to store and consult information outside the context window through a file-based system. This allows agents to build up knowledge bases over time, maintain project state across sessions, and reference previous work without keeping everything in context.

Sub-agent architectures

Sub-agent architectures provide another way around context limitations. Rather than one agent attempting to maintain state across an entire project, specialized sub-agents can handle focused tasks with clean context windows. The main agent coordinates with a high-level plan while subagents perform deep technical work or use tools to find relevant information. Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens).

This approach achieves a clear separation of concerns—the detailed search context remains isolated within sub-agents, while the lead agent focuses on synthesizing and analyzing the results. This pattern, discussed in How we built our multi-agent research system, showed a substantial improvement over single-agent systems on complex research tasks.

The choice between these approaches depends on task characteristics. For example:

    Compaction maintains conversational flow for tasks requiring extensive back-and-forth;
    Note-taking excels for iterative development with clear milestones;
    Multi-agent architectures handle complex research and analysis where parallel exploration pays dividends.

Even as models continue to improve, the challenge of maintaining coherence across extended interactions will remain central to building more effective agents.
Conclusion

Context engineering represents a fundamental shift in how we build with LLMs. As models become more capable, the challenge isn't just crafting the perfect prompt—it's thoughtfully curating what information enters the model's limited attention budget at each step. Whether you're implementing compaction for long-horizon tasks, designing token-efficient tools, or enabling agents to explore their environment just-in-time, the guiding principle remains the same: find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome.

The techniques we've outlined will continue evolving as models improve. We're already seeing that smarter models require less prescriptive engineering, allowing agents to operate with more autonomy. But even as capabilities scale, treating context as a precious, finite resource will remain central to building reliable, effective agents.

Get started with context engineering in the Claude Developer Platform today, and access helpful tips and best practices via our memory and context management cookbook.
Acknowledgements

Written by Anthropic's Applied AI team: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, and Jeremy Hadfield, with contributions from team members Rafi Ayub, Hannah Moran, Cal Rueb, and Connor Jennings. Special thanks to Molly Vorwerck, Stuart Ritchie, and Maggie Vo for their support.
