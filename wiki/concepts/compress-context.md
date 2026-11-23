# 策略三：壓縮（Compress）

> 一句話：把長長的歷史縮成重點，只留下完成任務需要的部分。

## 做法

- 定義：只保留完成任務所需的 token。 [S2]
- 摘要（summarisation）：Claude Code 的「auto-compact」會在上下文視窗用掉 95% 之後，把整段過程摘要起來。 [S2]
- 也可以只摘要特別佔空間的工具輸出（例如搜尋結果），或在 agent 之間交接時摘要。 [S2]
- 修剪（trimming）：用固定規則刪掉內容，例如移除較舊的訊息。 [S2]
- Anthropic 稱這個做法為 compaction：對話快到視窗上限時，把它摘要起來，用摘要開一個新的視窗繼續。 [S5]
- Claude Code 壓縮時會保留架構決策、還沒解決的 bug 與實作細節，丟掉重複的工具輸出。 [S5]
- 最輕量的壓縮是清掉舊的工具回傳結果。 [S5]
- 適合的情境：來回很多輪的長對話。 [S5]

## 風險

- 壓縮得太兇可能丟掉細節，而那些細節要到後面才看得出重要。建議先確保重要的都留下，再逐步刪去多餘的。 [S5]

- Manus 也指出，不可還原的壓縮有風險，因為無法預知哪一筆資料之後會變得關鍵。 [S6]

## 各家強調的重點

- LangChain 並列兩種做法：摘要與修剪。 [S2]
- Anthropic 介紹 compaction（摘要後用新視窗繼續），並提醒壓得太兇會丟細節。 [S5]
- Manus 強調壓縮要能還原，例如丟掉網頁內容但留下網址、丟掉文件內容但留下檔案路徑，需要時再讀回來。 [S6]

## 相關頁面

- [四種策略總覽](four-strategies.md)
- [選取](select-context.md)
- [隔離](isolate-context.md)
- [實戰經驗：Manus 的六條心得](production-lessons.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)、[S5 Anthropic](../sources/s5-anthropic.md)、[S6 Manus](../sources/s6-manus.md)
