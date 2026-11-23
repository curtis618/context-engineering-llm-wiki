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

## 上下文是有限資源

- 上下文必須被當成有限資源，而且邊際效益遞減：放越多，每一份新增內容的幫助越小。 [S5]
- 模型有「注意力預算（attention budget）」，每多一個 token 就會消耗一點。 [S5]
- 原因在模型架構：每個 token 都要和其他所有 token 建立關係，n 個 token 就有 n² 組關係，內容越多越難兼顧。 [S5]
- 表現是逐漸變差，不是到某個長度突然崩潰。 [S5]
- 等視窗變大不能解決問題，因為內容被污染、不相關的問題依然存在。 [S5]

## 相關頁面

- [什麼是 Context Engineering](what-is-context-engineering.md)
- [上下文的四種失敗模式](context-failure-modes.md)
- [Context Rot（上下文腐化）](context-rot.md)
- [四種策略總覽](four-strategies.md)
- [好的上下文長什麼樣子](designing-good-context.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)、[S5 Anthropic](../sources/s5-anthropic.md)
