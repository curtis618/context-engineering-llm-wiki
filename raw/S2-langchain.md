# S2 raw: LangChain, "Context Engineering"

- Title: Context Engineering
- Author: The LangChain Team
- Published: 2025-07-02
- URL: https://www.langchain.com/blog/context-engineering-for-agents (redirected from https://blog.langchain.com/context-engineering-for-agents/)
- Fetched: 2026-11-23. Read in full.

## Extract (paraphrased notes)

### Definition and analogy
- Definition (TL;DR): context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory.
- Analogy credited to Andrej Karpathy: LLMs are like a new kind of operating system. The LLM is the CPU and the context window is the RAM, the model's working memory. As an operating system curates what fits into RAM, context engineering plays a similar role.
- Cognition is quoted saying context engineering is effectively the #1 job of engineers building AI agents.

### Types of context
- Instructions: prompts, memories, few-shot examples, tool descriptions.
- Knowledge: facts, memories.
- Tools: feedback from tool calls.
- The article calls context engineering an umbrella across these types.

### Why it is needed
- Long-running tasks and accumulated tool feedback make agents use many tokens. This can exceed the context window, balloon cost and latency, or degrade performance.
- Anthropic is quoted: agents often engage in conversations spanning hundreds of turns, requiring careful context management.
- It lists Drew Breunig's four ways longer context causes problems: Context Poisoning (a hallucination makes it into the context), Context Distraction (the context overwhelms the training), Context Confusion (superfluous context influences the response), Context Clash (parts of the context disagree).
- Other failures mentioned: wrong memory retrieval, and tool overload from overlapping tool descriptions.

### Strategy: Write
- Writing context means saving it outside the context window to help an agent perform a task.
- Scratchpads: note-taking that persists information during a task; can be a tool call that writes to a file, or a field in a runtime state object.
- Anthropic's multi-agent researcher saves its plan to memory, because a context window over 200,000 tokens gets truncated.
- Long-term memories across sessions: Reflexion (reflection after each turn), Generative Agents (periodically synthesised memories). ChatGPT, Cursor and Windsurf auto-generate cross-session memories.

### Strategy: Select
- Selecting context means pulling it into the context window to help an agent perform a task.
- Memory selection: few-shot examples (episodic), instructions (procedural), facts (semantic). Code agents use always-loaded files such as Claude Code's CLAUDE.md and Cursor/Windsurf rules files.
- Large memory collections use embeddings or knowledge graphs for indexing.
- Tools: apply RAG over tool descriptions to fetch only relevant tools; recent papers show this improves tool selection accuracy by 3-fold.
- Knowledge/RAG: code agents such as Windsurf combine grep/file search, knowledge-graph retrieval and re-ranking.

### Strategy: Compress
- Compressing context involves retaining only the tokens required to perform a task.
- Summarisation: Claude Code's "auto-compact" summarises the trajectory after 95% of the context window is used. Recursive and hierarchical summarisation are also mentioned.
- Summarising specific token-heavy tool outputs (e.g. search tools), and at agent-to-agent handoffs.
- Trimming: hard-coded heuristics such as removing older messages; Drew Breunig calls this "prune".

### Strategy: Isolate
- Isolating context involves splitting it up to help an agent perform a task.
- Multi-agent: split context across sub-agents, each with its own tools, instructions and context window.
- Anthropic's multi-agent researcher: parallel subagents with their own context windows outperformed single-agent setups. Cost: up to 15× more tokens than chat, as reported by Anthropic.
- Sandboxes: run code in a sandbox; only selected return values go back to the LLM, token-heavy objects stay out of the context.
- Runtime state schema: some fields are exposed to the LLM, others hold data for selective use.

## Short quotes

- "Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory."
- "Writing context means saving it outside the context window to help an agent perform a task."
- "Selecting context means pulling it into the context window to help an agent perform a task."
- "Compressing context involves retaining only the tokens required to perform a task."
- "Isolating context involves splitting it up to help an agent perform a task."
