# 策略四：隔離（Isolate）

> 一句話：把工作拆給不同的「房間」做，每個房間有自己乾淨的上下文。

## 做法

- 定義：把上下文拆開，幫助 agent 完成任務。 [S2]
- 多代理（multi-agent）：把上下文分給多個子代理（sub-agent），每個都有自己的工具、指令與上下文視窗。 [S2]
- 例子：Anthropic 的多代理研究系統讓多個子代理平行工作，表現比單一代理好。 [S2]
- 代價：Anthropic 提到多代理用掉的 token 最多可達一般聊天的 15 倍。 [S2]
- 沙盒（sandbox）：讓程式在隔離環境執行，只把挑選過的結果傳回給模型，佔空間的資料留在外面。 [S2]

## 相關頁面

- [四種策略總覽](four-strategies.md)
- [壓縮](compress-context.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)
