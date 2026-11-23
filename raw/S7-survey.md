# S7 raw: "A Survey of Context Engineering for Large Language Models"

- Title: A Survey of Context Engineering for Large Language Models
- Authors: Lingrui Mei, Jiayu Yao, Yuyao Ge, Yiwei Wang, Baolong Bi, Yujun Cai, Jiazhi Liu, Mingyu Li, Zhong-Zhi Li, Duzhen Zhang, Chenlin Zhou, Jiayi Mao, Tianze Xia, Jiafeng Guo, Shenghua Liu (15 authors)
- Submitted: 2025-07-17 (arXiv 2507.13334)
- URL: https://arxiv.org/abs/2507.13334
- Fetched: 2026-11-23. PARTIAL READ: only the abstract page was read. The 166-page body was NOT read, so nothing below goes beyond the abstract.

## Extract (paraphrased notes, abstract only)

- The survey introduces context engineering as a formal discipline that goes beyond simple prompt design, covering the systematic optimization of the information payloads given to LLMs.
- It is based on a systematic analysis of over 1400 research papers.
- Taxonomy, part one, foundational components:
  - Context retrieval and generation: prompt-based generation and external knowledge acquisition.
  - Context processing: long-sequence processing, self-refinement, and structured information integration.
  - Context management: memory hierarchies, compression, and optimization.
- Taxonomy, part two, system implementations that combine those components:
  - Retrieval-augmented generation (RAG): modular, agentic and graph-enhanced architectures.
  - Memory systems: enabling persistent interactions.
  - Tool-integrated reasoning: function calling and environmental interaction.
  - Multi-agent systems: coordinating communication and orchestration.
- Key finding: a fundamental asymmetry exists between model capabilities. With advanced context engineering, current models are remarkably proficient at understanding complex contexts, but show pronounced limitations in generating equally sophisticated, long-form outputs.
- The authors call addressing this gap a defining priority for future research, and describe the survey as a technical roadmap and a unified framework for researchers and engineers.

## Short quotes

- "a formal discipline that transcends simple prompt design"
- "systematic optimization of information payloads for LLMs"
- "a fundamental asymmetry exists between model capabilities."
- "Addressing this gap is a defining priority for future research."
