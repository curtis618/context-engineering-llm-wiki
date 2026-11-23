# S5 raw: Anthropic, "Effective context engineering for AI agents"

- Title: Effective context engineering for AI agents
- Author: Anthropic Applied AI team (Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield, with contributors)
- Published: 2025-09-29
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Fetched: 2026-11-23. Read in full.

## Extract (paraphrased notes)

### Definitions
- "Context" is the set of tokens included when sampling from an LLM. The engineering problem is optimizing the usefulness of those tokens against the model's constraints.
- Context engineering: the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.
- Prompt engineering: methods for writing and organizing LLM instructions for optimal outcomes, focused on how to write effective prompts, particularly system prompts.
- Anthropic calls context engineering the natural progression of prompt engineering.
- Difference: prompt engineering is a discrete task (writing a prompt). Context engineering is iterative; the curation happens each time you decide what to pass to the model. It covers the whole context state: system instructions, tools, MCP, external data, message history.
- Agents run in multi-turn loops and keep generating data that could be relevant next turn, so the information must be refined cyclically.
- The question shifts from finding the right words to: what configuration of context is most likely to generate the model's desired behaviour?

### Why it matters: context rot and the attention budget
- Context rot: as the number of tokens in the window increases, the model's ability to accurately recall information from it decreases. This appears across all models, though some degrade more gently.
- Context must be treated as a finite resource with diminishing marginal returns. LLMs have an "attention budget"; every new token depletes it by some amount.
- Cause: in the transformer architecture every token attends to every other token, giving n² pairwise relationships for n tokens. Training data contains more short sequences than long ones, so models have less experience with long-range dependencies.
- The result is a performance gradient, not a hard cliff.

### The anatomy of effective context
- Core principle: find the smallest possible set of high-signal tokens that maximize the likelihood of the desired outcome.
- System prompts: aim for the "right altitude", between brittle hardcoded if-else logic and vague high-level guidance that assumes shared context. Organize into sections (XML tags or Markdown headers). Minimal does not necessarily mean short. Start with a minimal prompt on the best model, then add instructions and examples based on observed failures.
- Tools: tools are the contract between the agent and its information/action space; they should be token-efficient in what they return. Avoid bloated tool sets with ambiguous choices. If a human engineer cannot say which tool to use in a situation, the agent cannot either.
- Examples (few-shot): still strongly recommended. Do not stuff in a laundry list of edge cases; curate a small set of diverse, canonical examples.
- Overall: keep context informative, yet tight.

### Context retrieval and agentic search
- Working definition of agents: LLMs autonomously using tools in a loop.
- "Just in time" strategy: instead of loading all data up front, agents keep lightweight identifiers (file paths, stored queries, web links) and load the data at runtime with tools.
- Claude Code example: it uses commands like head and tail to analyse large data without loading full objects into context. Metadata (folder names, file names, timestamps) signals what a file is for. Progressive disclosure lets agents discover context step by step.
- Trade-off: runtime exploration is slower than retrieving pre-computed data, and agents can waste context without good tools. A hybrid is often best: Claude Code loads CLAUDE.md files up front and uses glob and grep to fetch files just in time.
- Advice: do the simplest thing that works.

### Long-horizon tasks: three techniques
- Tasks lasting tens of minutes to hours exceed the context window. Waiting for bigger windows is not enough, because pollution and relevance problems persist.
- Compaction: take a conversation nearing the context window limit, summarize it, and start a new window with the summary. Claude Code keeps architectural decisions, unresolved bugs and implementation details, and discards redundant tool outputs. Over-aggressive compaction can lose subtle details whose importance only becomes clear later; tune for recall first, then precision. The lightest form is clearing old tool results.
- Structured note-taking: the agent regularly writes notes persisted to memory outside of the context window and pulls them back later. Examples: a to-do list, or a NOTES.md file. Claude playing Pokémon keeps tallies and maps across thousands of steps and reads its own notes after context resets.
- Sub-agent architectures: specialized sub-agents handle focused tasks with clean context windows; the lead agent coordinates and synthesizes. A sub-agent may use tens of thousands of tokens exploring but returns a condensed summary, often 1,000-2,000 tokens.
- Which to choose: compaction for long back-and-forth conversations; note-taking for iterative work with clear milestones; multi-agent for complex research where parallel exploration pays off.

### Conclusion
- As models get smarter they need less prescriptive engineering and can act more autonomously, but treating context as a precious, finite resource stays central.

## Short quotes

- "Context, therefore, must be treated as a finite resource with diminishing marginal returns."
- "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."
- "Every new token introduced depletes this budget by some amount"
- "the agent regularly writes notes persisted to memory outside of the context window."
