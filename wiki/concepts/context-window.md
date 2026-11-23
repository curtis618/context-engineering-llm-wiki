# 上下文視窗（Context Window）

> 一句話：模型在回答的那一刻「看得到」的所有文字，就是它的工作記憶。

## 用電腦來比喻

- Karpathy 的比喻：LLM 像一種新的作業系統，模型是 CPU，上下文視窗是 RAM，也就是模型的工作記憶。 [S2]
- 作業系統要決定哪些東西放進 RAM；context engineering 做的是類似的事，決定哪些資訊放進上下文視窗。 [S2]

## 視窗裡裝了什麼

- 指令（instructions）：提示詞、記憶、少量範例、工具的說明。 [S2]
- 知識（knowledge）：事實與記憶。 [S2]
- 工具（tools）：呼叫工具後回傳的結果。 [S2]

## 為什麼需要管理

- 任務一長，工具回傳的內容不斷累積，agent 會用掉大量 token。 [S2]
- 後果有三種：超出上下文視窗、成本與延遲暴增、表現變差。 [S2]
- Anthropic 提到 agent 的對話常常長達數百輪，所以需要仔細管理上下文。 [S2]

## 相關頁面

- [什麼是 Context Engineering](what-is-context-engineering.md)
- [上下文的四種失敗模式](context-failure-modes.md)
- [Context Rot（上下文腐化）](context-rot.md)
- [四種策略總覽](four-strategies.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)
