# Context Engineering Wiki 目錄

主題：Context Engineering（上下文工程）。規則見專案根目錄的 `AGENTS.md`，變更紀錄見 [log.md](log.md)。

## 概念頁

- [什麼是 Context Engineering](concepts/what-is-context-engineering.md)：定義，以及和 prompt engineering 的差別。
- [上下文視窗](concepts/context-window.md)：模型的工作記憶，裡面裝什麼、為什麼要管理。
- [上下文的四種失敗模式](concepts/context-failure-modes.md)：污染、分心、混淆、衝突。
- [四種策略總覽](concepts/four-strategies.md)：寫入、選取、壓縮、隔離。
- [策略一：寫入](concepts/write-context.md)：把資訊存到視窗外。
- [策略二：選取](concepts/select-context.md)：把需要的資訊拉進視窗。
- [策略三：壓縮](concepts/compress-context.md)：只留必要的 token。
- [策略四：隔離](concepts/isolate-context.md)：把上下文拆開處理。

## 來源摘要頁

- [S1 Willison〈Context engineering〉](sources/s1-willison.md)：這個詞為什麼比 prompt engineering 好。
- [S2 LangChain〈Context Engineering〉](sources/s2-langchain.md)：四種策略的分類與實例。
- [S3〈How Long Contexts Fail〉](sources/s3-breunig.md)：長上下文出錯的四種方式與證據。
