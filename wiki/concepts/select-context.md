# 策略二：選取（Select）

> 一句話：需要的時候，才把相關資訊拉進上下文視窗。

## 做法

- 定義：把上下文拉進視窗，幫助 agent 完成任務。 [S2]
- 選記憶：可以選範例、指令或事實。寫程式的 agent 會固定載入規則檔，例如 Claude Code 的 CLAUDE.md。 [S2]
- 選工具：對工具說明做 RAG，只取出相關的工具；研究顯示這能讓選對工具的準確率提升到 3 倍。 [S2]
- 選知識：寫程式的 agent 會結合檔案搜尋、知識圖譜檢索與重新排序。 [S2]

## 即時取用（just in time）

- 不事先載入所有資料，只保留輕量的索引（檔案路徑、查詢語句、網址），需要時才用工具把內容載入。 [S5]
- 例子：Claude Code 用 head、tail 這類指令分析大型資料，不把整份資料放進上下文。 [S5]
- 檔名、資料夾名稱、時間戳記這些中繼資料，本身就能提示一個檔案的用途。 [S5]
- 代價：執行時才探索，比直接取用預先算好的資料慢；沒有好工具時，agent 也可能浪費上下文。 [S5]
- 折衷做法：一部分事先載入，一部分即時取用。Claude Code 會先載入 CLAUDE.md，再用 glob 與 grep 即時找檔案。 [S5]

## 相關頁面

- [四種策略總覽](four-strategies.md)
- [寫入](write-context.md)
- [壓縮](compress-context.md)
- [好的上下文長什麼樣子](designing-good-context.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)、[S5 Anthropic](../sources/s5-anthropic.md)
