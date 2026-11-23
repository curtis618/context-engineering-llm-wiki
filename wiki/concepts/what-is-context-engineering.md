# 什麼是 Context Engineering（上下文工程）

> 一句話：決定「要把哪些資訊放到 AI 眼前」的工作。

## 定義

- Tobi Lütke 的定義：提供所有必要的上下文，讓任務有可能被 LLM 解決的藝術。 [S1]
- Andrej Karpathy 的定義：把「剛好對的資訊」填進上下文視窗（context window），供下一步使用的精細藝術與科學。 [S1]
- Karpathy 列出要放進去的東西：任務說明、少量範例（few-shot examples）、RAG 查到的資料、工具、狀態與歷史，以及壓縮過的內容。 [S1]

- LangChain 的定義：在 agent 執行的每一步，把剛好對的資訊填進上下文視窗的藝術與科學。 [S2]
- Cognition 公司認為，context engineering 實際上是打造 AI agent 的工程師的首要工作。 [S2]

## 和 Prompt Engineering 的差別

- 「prompt」讓人想到的是一小段任務描述；但在正式的 LLM 應用裡，真正的工作是安排整個上下文視窗的內容。 [S1]
- Willison 指出，多數人把「prompt engineering」理解成「在聊天機器人裡打字」，所以這個詞無法表達背後的複雜度。 [S1]

## 相關頁面

- [上下文視窗](context-window.md)
- [四種策略總覽](four-strategies.md)
- 來源：[S1 Willison](../sources/s1-willison.md)、[S2 LangChain](../sources/s2-langchain.md)
