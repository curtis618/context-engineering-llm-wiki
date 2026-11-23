# 四種策略總覽：寫入、選取、壓縮、隔離

> 一句話：管理上下文的方法可以分成四類，分別處理「存、取、縮、分」。

## 四類各是什麼

- 寫入（Write）：把資訊存到上下文視窗外面，之後需要時再用。詳見[寫入](write-context.md)。 [S2]
- 選取（Select）：把需要的資訊拉進上下文視窗。詳見[選取](select-context.md)。 [S2]
- 壓縮（Compress）：只保留完成任務所需的 token。詳見[壓縮](compress-context.md)。 [S2]
- 隔離（Isolate）：把上下文拆開，分給不同的地方處理。詳見[隔離](isolate-context.md)。 [S2]

## 相關頁面

- [上下文視窗](context-window.md)
- [上下文的四種失敗模式](context-failure-modes.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)
