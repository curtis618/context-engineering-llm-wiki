# S6 raw: Manus, "Context Engineering for AI Agents: Lessons from Building Manus"

- Title: Context Engineering for AI Agents: Lessons from Building Manus
- Author: Yichao 'Peak' Ji (Manus)
- Published: 2025-07-18
- URL: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- Fetched: 2026-11-23. Read in full.

## Extract (paraphrased notes)

### Why context engineering instead of training models
- In the BERT era each fine-tuning iteration could take weeks; for a fast-moving product that feedback loop is a deal-breaker.
- At a previous startup the author's in-house trained models became irrelevant overnight when GPT-3 and Flan-T5 arrived.
- Context engineering lets the team ship improvements in hours instead of weeks, and keeps the product independent of the underlying model. Image: if model progress is the rising tide, Manus wants to be the boat, not the pillar stuck to the seabed.
- The team has rebuilt its agent framework four times. The author states that none of the lessons is universal truth.

### Lesson: design around the KV-cache
- Claim: the KV-cache hit rate is the single most important metric for a production-stage AI agent, because it drives latency and cost.
- Reason: an agent's context grows every step while outputs stay short. In Manus the average input-to-output token ratio is about 100:1.
- Price example given (Claude Sonnet): cached input costs 0.30 USD per million tokens versus 3 USD uncached, a 10x difference.
- Practices: keep the prompt prefix stable (a single-token change invalidates the cache from that point; do not put a second-precision timestamp at the top of the system prompt); make the context append-only and never modify earlier actions or observations.

### Lesson: mask, don't remove
- Claim: avoid dynamically adding or removing tools mid-iteration unless absolutely necessary.
- Reasons: tool definitions sit near the front of the context, so changing them invalidates the cache for everything after; and earlier actions that refer to tools no longer defined confuse the model.
- Practice: keep all tools defined, and instead block or allow tool choices at decoding time (masking) according to the current state.

### Lesson: use the file system as context
- Claim: treat the file system as the ultimate context: unlimited in size, persistent, and directly operable by the agent.
- Reasons: even context windows of 128K tokens or more fall short; observations such as web pages and PDFs can be huge; performance degrades at long lengths; long inputs are expensive even with caching.
- Irreversible compression is risky because you cannot know which observation will become critical later.
- Practice: make compression restorable. Drop a web page's content from the context as long as its URL is kept; drop a document's content if its file path remains.

### Lesson: manipulate attention through recitation
- A typical Manus task takes around 50 tool calls, so the agent can drift or forget its goals.
- Practice: the agent creates a todo.md file and rewrites it step by step, checking off completed items. Rewriting the plan pushes the global goal into the recent end of the context, countering "lost-in-the-middle" problems.

### Lesson: keep the wrong stuff in
- Claim: leave failed actions, error messages and stack traces in the context instead of cleaning them up.
- Reason: erasing failure removes evidence; when the model sees a failed action and the resulting observation, it updates its beliefs and is less likely to repeat the mistake.
- The author considers error recovery one of the clearest signs of real agentic behaviour.

### Lesson: don't get few-shotted
- Claim: few-shot prompting can backfire in agents, because the model imitates the pattern of action-observation pairs in its context.
- Example: reviewing a batch of 20 resumes, the agent falls into a rhythm and repeats similar actions even when they are no longer the best choice.
- Practice: introduce small amounts of structured variation in serialization templates, phrasing and ordering.

## Short quotes

- "the KV-cache hit rate is the single most important metric for a production-stage AI agent"
- "unless absolutely necessary, avoid dynamically adding or removing tools mid-iteration"
- "Erasing failure removes evidence. And without evidence, the model can't adapt."
- "In other words, don't few-shot yourself into a rut."
- "If model progress is the rising tide, we want Manus to be the boat, not the pillar stuck to the seabed."
