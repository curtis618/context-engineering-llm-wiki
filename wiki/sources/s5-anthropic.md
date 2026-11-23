# S5　Anthropic〈Effective context engineering for AI agents〉

- 作者：Anthropic Applied AI 團隊
- 日期：2025-09-29
- 原文網址：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- raw 檔案：[S5-anthropic.md](../../raw/S5-anthropic.md)
- 讀到的範圍：全文。

## 這篇在講什麼

Anthropic 的工程指南：把上下文當成有限資源，說明好的上下文長什麼樣子，以及任務很長時的三種處理技巧。

## 重點

- 定義：context engineering 是在模型推論時，挑選並維護「最佳的一組 token」的各種策略。
- 它是 prompt engineering 的自然延伸：寫 prompt 是一次性的工作，context engineering 則是每一輪都要重新決定給模型什麼。
- 上下文是有限資源，而且邊際效益遞減。模型有「注意力預算」，每多一個 token 就消耗一點。
- 核心原則：找出最小的一組高訊號 token，讓想要的結果最可能發生。
- 系統提示要寫在「剛好的高度」，工具要少而清楚，範例要少而有代表性。
- 即時（just in time）取用：只保留檔案路徑這類輕量的索引，需要時才用工具載入內容。
- 長任務的三種技巧：壓縮（compaction）、結構化筆記、子代理架構。

## 相關概念頁

- [什麼是 Context Engineering](../concepts/what-is-context-engineering.md)
- [上下文視窗](../concepts/context-window.md)
- [Context Rot（上下文腐化）](../concepts/context-rot.md)
- [好的上下文長什麼樣子](../concepts/designing-good-context.md)
- [寫入](../concepts/write-context.md)、[選取](../concepts/select-context.md)、[壓縮](../concepts/compress-context.md)、[隔離](../concepts/isolate-context.md)
