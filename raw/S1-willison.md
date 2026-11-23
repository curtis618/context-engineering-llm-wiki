# S1 raw: Simon Willison, "Context engineering"

- Title: Context engineering
- Author: Simon Willison (Simon Willison's Weblog)
- Published: 2025-06-27
- URL: https://simonwillison.net/2025/Jun/27/context-engineering/
- Fetched: 2026-11-23. Read in full. The two tweets it embeds were read only as quoted on this page.

## Extract (paraphrased notes)

- The term "context engineering" has recently started to gain traction as a better alternative to "prompt engineering"; Willison likes it and thinks it may have sticking power.
- He had earlier defended the term "prompt engineering" (his post of 2023-02-21), hoping it could capture the complexity of building reliable prompts.
- His problem with "prompt engineering": most people infer that it just means typing things into a chatbot. Inferred definitions are the ones that stick.
- He thinks the inferred meaning of "context engineering" will be much closer to the intended meaning.
- Tobi Lütke (Shopify CEO) says he prefers "context engineering" over prompt engineering and defines it as the art of providing all the context for the task to be plausibly solvable by the LLM.
- Andrej Karpathy says "+1". He argues prompts suggest short task descriptions, whereas in industrial-strength LLM apps context engineering means filling the context window with the right information for the next step.
- Karpathy calls it both a science and an art. Science: task descriptions and explanations, few-shot examples, RAG, related (possibly multimodal) data, tools, state and history, compacting. Art: intuition about LLM "psychology". He says doing this well is highly non-trivial.
- The page names no coiner or origin of the term; it only says it has recently gained traction.

## Short quotes

- Lütke: "the art of providing all the context for the task to be plausibly solvable by the LLM."
- Karpathy: "the delicate art and science of filling the context window with just the right information for the next step."
- Willison: "most people's inferred definition is that it's a laughably pretentious term for typing things into a chatbot!"
- Willison: "I think the inferred definition of "context engineering" is likely to be much closer to the intended meaning."
