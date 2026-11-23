# 證據卡：壓縮
wiki: concepts/compress-context.md

- **COM-1** 摘要：Claude Code 的「auto-compact」會在上下文視窗用掉 95% 之後，把整段過程摘要起來。 [S2]
- **COM-2** Compaction：對話快到視窗上限時，把它摘要起來，用摘要開一個新的視窗繼續。 [S5]
- **COM-3** 風險：壓縮得太兇可能丟掉細節，而那些細節要到後面才看得出重要。 [S5]
- **COM-4** 不同觀點：Anthropic 與 LangChain 把「摘要後繼續」當成主要做法；Manus 主張壓縮要能還原，例如丟掉網頁內容但留下網址。 [S2][S5][S6]
- **COM-5** 修剪：用固定規則刪掉內容，例如移除較舊的訊息。 [S2]
