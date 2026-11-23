# 好的上下文長什麼樣子

> 一句話：資訊要充足，但要精簡；目標是「最小的一組高訊號內容」。

## 核心原則

- 找出最小的一組高訊號 token，讓想要的結果最可能發生。 [S5]
- 整體要求是：資訊充足，但保持精簡。 [S5]
- 建議做法是從最簡單可行的方式開始。 [S5]

## 系統提示（system prompt）

- 要寫在「剛好的高度」：不要寫成死板的 if-else 規則，也不要寫成假設對方都懂的空泛指示。 [S5]
- 用分段來組織，例如 XML 標籤或 Markdown 標題。 [S5]
- 精簡不代表短。先用最少的提示測試，再根據實際出錯的地方補上指令與範例。 [S5]

## 工具

- 工具回傳的內容要節省 token。 [S5]
- 避免工具太多、功能重疊。如果人類工程師都說不出某個情況該用哪個工具，agent 也做不到。 [S5]

## 範例

- 仍然強烈建議提供範例，但不要塞一長串特殊情況，而是挑少量、多樣、有代表性的例子。 [S5]

## 不同觀點

- 範例有幫助：Anthropic 仍強烈建議提供少量、多樣、有代表性的範例。 [S5]
- 範例可能帶偏：Manus 提醒，agent 會模仿上下文裡重複的模式，範例太一致時會讓它陷入固定做法，所以要加入變化。 [S6]

## 相關頁面

- [實戰經驗：Manus 的六條心得](production-lessons.md)
- [什麼是 Context Engineering](what-is-context-engineering.md)
- [上下文視窗](context-window.md)
- [選取](select-context.md)
- 來源：[S5 Anthropic](../sources/s5-anthropic.md)、[S6 Manus](../sources/s6-manus.md)
