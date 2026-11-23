# 策略三：壓縮（Compress）

> 一句話：把長長的歷史縮成重點，只留下完成任務需要的部分。

## 做法

- 定義：只保留完成任務所需的 token。 [S2]
- 摘要（summarisation）：Claude Code 的「auto-compact」會在上下文視窗用掉 95% 之後，把整段過程摘要起來。 [S2]
- 也可以只摘要特別佔空間的工具輸出（例如搜尋結果），或在 agent 之間交接時摘要。 [S2]
- 修剪（trimming）：用固定規則刪掉內容，例如移除較舊的訊息。 [S2]

## 相關頁面

- [四種策略總覽](four-strategies.md)
- [選取](select-context.md)
- [隔離](isolate-context.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)
