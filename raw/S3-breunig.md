# S3 raw: "How Long Contexts Fail"

- Title: How Long Contexts Fail
- Author: no byline on the page; published on dbreunig.com
- Published: 2025-06-22
- URL: https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
- Fetched: 2026-11-23. Read in full. The studies it links (Gemini 2.5 report, Databricks, BFCL, GeoEngine, Microsoft/Salesforce paper) were not fetched; they are described only as this page reports them.

## Extract (paraphrased notes)

### Main argument
- Context windows have grown (up to 1M tokens in Gemini 2.5 and GPT-4.1), but longer contexts do not generate better responses. Overloaded contexts can make agents fail in surprising ways.
- Agents are the most exposed, because they gather information, synthesize findings and coordinate actions through context.
- The main value of very large windows is summarization and fact retrieval. For other uses, respect the model's "distraction ceiling".

### Context Poisoning
- Definition: a hallucination or other error makes it into the context, where it is repeatedly referenced.
- Evidence: Google DeepMind's Gemini 2.5 technical report, describing a Gemini agent playing Pokémon. When the goals section of its context was poisoned with misinformation about the game state, the agent developed nonsensical strategies and repeated behaviour, and it could take a very long time to undo.

### Context Distraction
- Definition: a context grows so long that the model over-focuses on the context, neglecting what it learned during training.
- Evidence (same Gemini Pokémon agent, described as anecdotal): as the context grew significantly beyond 100k tokens, the agent favoured repeating actions from its history rather than synthesizing novel plans.
- Evidence: a Databricks study found correctness began to fall around 32k tokens for Llama 3.1 405b, and sooner for smaller models.

### Context Confusion
- Definition: superfluous content in the context is used by the model to generate a low-quality response.
- Evidence: Berkeley Function-Calling Leaderboard; every model performs worse when provided with more than one tool, and models sometimes call tools that are not relevant.
- Evidence: GeoEngine benchmark with 46 tools. A quantized Llama 3.1 8b failed when given all 46 tools, even though the context was well within the 16k context window; it succeeded when given only 19 tools.

### Context Clash
- Definition: new information and tools accrue in the context that conflict with other information in the context.
- Evidence: a Microsoft and Salesforce paper took benchmark prompts and "sharded" them across multiple chat turns. Result: an average drop of 39%. OpenAI's o3 dropped from 98.1 to 64.1.
- Explanation given: early wrong attempts stay in the context; when LLMs take a wrong turn in a conversation, they get lost and do not recover.
- Third-party MCP tool descriptions can also clash with the rest of the prompt.

### Fixes
- This page does not detail fixes; it points to a follow-up article ("How to Fix Your Context", not fetched) and mentions dynamically loading tools and context quarantines.

## Short quotes

- "Contexts can become poisoned, distracting, confusing, or conflicting."
- "But in reality, longer contexts do not generate better responses."
- "It may be irrelevant information or needless tool definitions, but the model will take it into account."
- "we discover that when LLMs take a wrong turn in a conversation, they get lost and do not recover."
