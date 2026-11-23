# Wiki 變更紀錄

只往下加，不改舊紀錄。

## 2026-11-23 建立

- 完成訪談與需求摘要（見 `interview.md`），生成 `AGENTS.md`、資料夾與 lint 腳本。

## 2026-11-23 ingest S1 Willison

- 新增 `raw/S1-willison.md`、`sources/s1-willison.md`。
- 新增概念頁 `what-is-context-engineering.md`（定義、與 prompt engineering 的差別）。

## 2026-11-23 ingest S2 LangChain

- 新增 `raw/S2-langchain.md`、`sources/s2-langchain.md`。
- 新增概念頁：`context-window.md`、`context-failure-modes.md`、`four-strategies.md`、`write-context.md`、`select-context.md`、`compress-context.md`、`isolate-context.md`。
- 更新 `what-is-context-engineering.md`：加入 LangChain 的定義與相關頁面連結。

## 2026-11-23 ingest S3 How Long Contexts Fail

- 新增 `raw/S3-breunig.md`、`sources/s3-breunig.md`。
- 改寫 `context-failure-modes.md`：四種模式各自成節，補上 S3 的定義、研究與實例。

## 2026-11-23 ingest S4 Chroma Context Rot

- 新增 `raw/S4-chroma.md`、`sources/s4-chroma.md`。來源只讀到約前三分之二，已在來源頁註明，未讀到的部分不引用。
- 新增概念頁 `context-rot.md`；`context-window.md` 加上連結。

## 2026-11-23 ingest S5 Anthropic

- 新增 `raw/S5-anthropic.md`、`sources/s5-anthropic.md`。
- 新增概念頁 `designing-good-context.md`。
- 更新 `what-is-context-engineering.md`（Anthropic 的定義、與 prompt engineering 的差別、新增「不同觀點」：給全部 vs 給最少）。
- 更新 `context-window.md`（有限資源、注意力預算）、`context-rot.md`（成因解釋）。
- 更新四個策略頁：寫入（結構化筆記）、選取（即時取用）、壓縮（compaction 與風險）、隔離（子代理回傳摘要）。

## 2026-11-23 ingest S6 Manus

- 新增 `raw/S6-manus.md`、`sources/s6-manus.md`。
- 新增概念頁 `production-lessons.md`，含「不同觀點」：錯誤該不該留在上下文（S6 vs S3）。
- 更新 `write-context.md`（檔案系統、todo.md）、`compress-context.md`（新增「不同觀點」：摘要 vs 可還原壓縮）、`designing-good-context.md`（新增「不同觀點」：範例有幫助 vs 可能帶偏）。

## 2026-11-23 ingest S7 Survey

- 新增 `raw/S7-survey.md`、`sources/s7-survey.md`。來源只讀到摘要，已在來源頁註明。
- 新增概念頁 `research-landscape.md`；`what-is-context-engineering.md` 加入綜述的定義。

## 2026-11-23 依 AI 忠實度審查修正（簡報流程的關卡 5 退回到 wiki）

- 問題：ingest 時把幾組「強調重點不同」的說法寫成互相對立的「不同觀點」，但原文並沒有互相反駁。
- 修正 `what-is-context-engineering.md`、`designing-good-context.md`、`compress-context.md`、`production-lessons.md`：「不同觀點」改為「各家強調的重點」或「相關提醒」，並寫明兩邊談的對象。
- 其他修正：「一次性的工作」改為「單一、獨立的工作」；工具「功能重疊」改為「選擇模糊不清」；價格補上「以 Claude Sonnet 為例」；「等幾週」補上 BERT 年代的前提。

## 2026-11-23 第一次執行「關卡 0」（wiki 對 raw 的 AI 審查）後修正

- 審查了 134 條有出處的條目，找到 12 個問題（中 4、低 8，沒有高）。
- `context-failure-modes.md`：六條研究與例子補上「據該文轉述」，因為原始研究沒有讀；補回「軼事性質」「有時」。
- `designing-good-context.md`、`production-lessons.md`、`what-is-context-engineering.md`、`compress-context.md`：上一輪把「對立」改成「其實不衝突」，但那也是 wiki 自己下的結論。改成只並列、註明出自不同文章。
- 補回被拿掉的限定詞與前提：「除非絕對必要」「典型任務」（原寫成平均）「比較不容易重犯」「在最好的模型上」「一項關鍵優先事項」（原寫成首要任務）；一句 Karpathy 的論點補上歸屬。

## 2026-11-23 第 3 次審查後修正（5 項，全部低嚴重度）

- `compress-context.md`：刪掉「也」（等於判定兩個來源一致）；「Anthropic 稱這個做法為 compaction」改成「Anthropic 介紹 compaction」（原句把兩篇文章的概念畫上等號）。
- `what-is-context-engineering.md`：刪掉 wiki 自己加的「因為上下文是有限資源」；Karpathy 的論點改回貼近原文的說法；Karpathy 的清單補回「相關資料（可能是多模態）」。
