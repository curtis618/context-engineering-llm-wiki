# S4 raw: Chroma, "Context Rot: How Increasing Input Tokens Impacts LLM Performance"

- Title: Context Rot: How Increasing Input Tokens Impacts LLM Performance (Chroma Technical Report)
- Authors: Kelly Hong, Anton Troynikov, Jeff Huber (Chroma)
- Published: 2025-07-14
- URL: https://www.trychroma.com/research/context-rot (redirected from https://research.trychroma.com/context-rot)
- Fetched: 2026-11-23. PARTIAL READ: only roughly the first two thirds of the page came back as text (intro, experimental design, needle/distractor/structure experiments, LongMemEval design and headline result). The repeated-words results, limitations and conclusion sections were NOT read. Only what was read is recorded below.

## Extract (paraphrased notes, from the part that was read)

### Main claim
- LLMs are typically presumed to process context uniformly. The report finds they do not: performance grows increasingly unreliable as input length grows.
- The visible text gives no formal one-sentence definition of the term "context rot"; it is the report's title for this effect.
- Design principle: each task is kept intentionally simple and controlled so that only input length changes, isolating the impact of context length alone.
- Because real applications are more complex than these tasks, the authors expect the effect of input length to be even more pronounced in practice.

### Setup
- 18 LLMs evaluated, including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3 models.
- Total LLM calls: 194,480.

### Experiment: needle-question similarity
- Task: find a "needle" (the sentence containing the answer) in a long "haystack" of text. Varied: how semantically similar the needle is to the question.
- Finding: performance degrades more quickly with input length when the needle and question are less similar. At short lengths models succeed even on low-similarity pairs.

### Experiment: distractors
- A distractor is text that is related to the question but does not answer it. Conditions: no distractors (baseline), one distractor, four distractors.
- Finding: even a single distractor reduces performance relative to the baseline, and four distractors compound the drop.
- Claude models had the lowest hallucination rates and tend to abstain when uncertain; GPT models hallucinated most.

### Experiment: haystack structure
- Varied: original text with coherent flow versus the same sentences randomly shuffled.
- Finding (surprising to the authors): structural coherence consistently hurts performance; models did better on shuffled haystacks, across all 18 models.

### Experiment: LongMemEval (conversational memory questions)
- Compared "focused" prompts containing only the relevant parts (about 300 tokens) with "full" prompts containing the whole history (about 113k tokens), on 306 prompts.
- Finding: across all models, performance is significantly higher on focused prompts than on full prompts.

## Short quotes

- "models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows."
- "Each task remains intentionally simple and is deliberately controlled to isolate the impact of context length alone."
- "Even a single distractor reduces performance relative to the baseline (needle only)"
- "Surprisingly, we find that structural coherence consistently hurts model performance."
- "Across all models, we see significantly higher performance on focused prompts compared to full prompts."
