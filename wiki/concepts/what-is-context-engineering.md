# 什麼是 Context Engineering（上下文工程）

> 一句話：決定「要把哪些資訊放到 AI 眼前」的工作。

## 定義

- Tobi Lütke 的定義：提供所有必要的上下文，讓任務有可能被 LLM 解決的藝術。 [S1]
- Andrej Karpathy 的定義：把「剛好對的資訊」填進上下文視窗（context window），供下一步使用的精細藝術與科學。 [S1]
- Karpathy 列出要放進去的東西：任務說明、少量範例（few-shot examples）、RAG 查到的資料、工具、狀態與歷史，以及壓縮過的內容。 [S1]
- LangChain 的定義：在 agent 執行的每一步，把剛好對的資訊填進上下文視窗的藝術與科學。 [S2]
- Anthropic 的定義：在模型推論時，挑選並維護「最佳的一組 token」的各種策略，範圍包含 prompt 以外所有會進到上下文的資訊。 [S5]
- 學術綜述的定義：一門超越單純提示設計的正式學科，有系統地最佳化提供給 LLM 的資訊。 [S7]
- Cognition 公司認為，context engineering 實際上是打造 AI agent 的工程師的首要工作。 [S2]

## 和 Prompt Engineering 的差別

- 「prompt」讓人想到的是一小段任務描述；但在正式的 LLM 應用裡，真正的工作是安排整個上下文視窗的內容。 [S1]
- Willison 指出，多數人把「prompt engineering」理解成「在聊天機器人裡打字」，所以這個詞無法表達背後的複雜度。 [S1]
- Prompt engineering 的重點是怎麼寫好指令，尤其是系統提示；Anthropic 把 context engineering 視為它的自然延伸。 [S5]
- 寫 prompt 是單一、獨立的工作（寫出一份提示）；context engineering 是反覆進行的，每次要傳東西給模型時都要重新挑選。 [S5]
- 管理的範圍從一段提示擴大到整個上下文狀態：系統指令、工具、外部資料、對話歷史。 [S5]
- 問題從「怎麼找到對的字句」變成「什麼樣的上下文配置，最可能讓模型做出想要的行為」。 [S5]

## 各家強調的重點

- Lütke 強調「要夠」：提供讓任務可解所需的所有上下文。 [S1]
- Anthropic 強調「不要多」：找出最小的一組高訊號 token，因為上下文是有限資源。 [S5]
- 這兩個說法出自不同文章，原文沒有互相反駁。 [S1][S5]

## 相關頁面

- [上下文視窗](context-window.md)
- [好的上下文長什麼樣子](designing-good-context.md)
- [四種策略總覽](four-strategies.md)
- [研究全景：學術界怎麼分類](research-landscape.md)
- 來源：[S1 Willison](../sources/s1-willison.md)、[S2 LangChain](../sources/s2-langchain.md)、[S5 Anthropic](../sources/s5-anthropic.md)、[S7 Survey](../sources/s7-survey.md)
