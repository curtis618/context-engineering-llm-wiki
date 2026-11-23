# 策略二：選取（Select）

> 一句話：需要的時候，才把相關資訊拉進上下文視窗。

## 做法

- 定義：把上下文拉進視窗，幫助 agent 完成任務。 [S2]
- 選記憶：可以選範例、指令或事實。寫程式的 agent 會固定載入規則檔，例如 Claude Code 的 CLAUDE.md。 [S2]
- 選工具：對工具說明做 RAG，只取出相關的工具；研究顯示這能讓選對工具的準確率提升到 3 倍。 [S2]
- 選知識：寫程式的 agent 會結合檔案搜尋、知識圖譜檢索與重新排序。 [S2]

## 相關頁面

- [四種策略總覽](four-strategies.md)
- [寫入](write-context.md)
- [壓縮](compress-context.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)
