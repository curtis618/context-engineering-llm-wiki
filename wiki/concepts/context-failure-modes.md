# 上下文的四種失敗模式

> 一句話：上下文不是越多越好，塞錯東西會讓模型以四種方式出錯。

## 四種模式

- 上下文污染（Context Poisoning）：幻覺（模型編出來的錯誤內容）跑進了上下文。 [S2]
- 上下文分心（Context Distraction）：上下文太長，蓋過了模型訓練時學到的東西。 [S2]
- 上下文混淆（Context Confusion）：多餘的內容影響了回答。 [S2]
- 上下文衝突（Context Clash）：上下文裡不同部分互相矛盾。 [S2]
- 這四種分類是 Drew Breunig 提出的，LangChain 的文章引用了它。 [S2]

## 相關頁面

- [上下文視窗](context-window.md)
- [四種策略總覽](four-strategies.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)
