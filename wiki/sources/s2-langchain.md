# S2　LangChain〈Context Engineering〉

- 作者：The LangChain Team
- 日期：2025-07-02
- 原文網址：https://www.langchain.com/blog/context-engineering-for-agents
- raw 檔案：[S2-langchain.md](../../raw/S2-langchain.md)
- 讀到的範圍：全文。

## 這篇在講什麼

把 agent 的上下文管理方法整理成四類：寫入（write）、選取（select）、壓縮（compress）、隔離（isolate），每一類都舉了實際產品的例子。

## 重點

- 定義：在 agent 執行的每一步，把剛好對的資訊填進上下文視窗的藝術與科學。
- 比喻（引自 Karpathy）：LLM 像一種新的作業系統，模型是 CPU，上下文視窗是 RAM，也就是模型的工作記憶。
- 上下文有三類：指令、知識、工具回傳的結果。
- 任務一長，工具回傳的內容不斷累積，會超出視窗、增加成本與延遲，或讓表現變差。
- 文中引用 Drew Breunig 整理的四種上下文失敗：污染、分心、混淆、衝突。
- 四種策略：寫入是存到視窗外，選取是拉進視窗，壓縮是只留必要的 token，隔離是把上下文拆開。

## 相關概念頁

- [什麼是 Context Engineering](../concepts/what-is-context-engineering.md)
- [上下文視窗](../concepts/context-window.md)
- [上下文的四種失敗模式](../concepts/context-failure-modes.md)
- [四種策略總覽](../concepts/four-strategies.md)
- [寫入](../concepts/write-context.md)、[選取](../concepts/select-context.md)、[壓縮](../concepts/compress-context.md)、[隔離](../concepts/isolate-context.md)
