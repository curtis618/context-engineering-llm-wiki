# 策略一：寫入（Write）

> 一句話：把資訊存到上下文視窗外面，像是讓 AI 做筆記。

## 做法

- 定義：把上下文存到視窗之外，幫助 agent 完成任務。 [S2]
- 草稿區（scratchpad）：任務進行中做的筆記，可以是寫進檔案，也可以是存在程式執行狀態的一個欄位。 [S2]
- 例子：Anthropic 的多代理研究系統會把計畫存進記憶，因為上下文超過 200,000 token 時會被截斷。 [S2]
- 長期記憶：跨對話保存的記憶，ChatGPT、Cursor、Windsurf 都會自動產生這類記憶。 [S2]
- 結構化筆記（structured note-taking）：agent 定期把筆記寫到視窗外的記憶，之後再讀回來，例如待辦清單或 NOTES.md 檔。 [S5]
- 例子：玩寶可夢的 Claude 會記錄數量與地圖，上下文被重置後靠讀自己的筆記繼續。 [S5]
- 適合的情境：有明確階段、反覆推進的工作。 [S5]

## 相關頁面

- [四種策略總覽](four-strategies.md)
- [選取](select-context.md)
- 來源：[S2 LangChain](../sources/s2-langchain.md)、[S5 Anthropic](../sources/s5-anthropic.md)
