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
