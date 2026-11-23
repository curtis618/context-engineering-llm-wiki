# 證據卡：什麼是 Context Engineering
wiki: concepts/what-is-context-engineering.md

- **DEF-1** Karpathy 的定義：把「剛好對的資訊」填進上下文視窗，供下一步使用的精細藝術與科學。 [S1]
- **DEF-2** Lütke 的定義：提供所有必要的上下文，讓任務有可能被 LLM 解決的藝術。 [S1]
- **DEF-3** Anthropic 的定義：在模型推論時，挑選並維護「最佳的一組 token」的各種策略，範圍包含 prompt 以外所有會進到上下文的資訊。 [S5]
- **DEF-4** 學術綜述的定義：一門超越單純提示設計的正式學科，有系統地最佳化提供給 LLM 的資訊。 [S7]
- **DEF-5** Karpathy 認為，「prompt」讓人想到的是一小段任務描述；而在正式的 LLM 應用裡，context engineering 是把對的資訊填進上下文視窗，供下一步使用。 [S1]
- **DEF-6** 寫 prompt 是單一、獨立的工作（寫出一份提示）；context engineering 是反覆進行的，每次要傳東西給模型時都要重新挑選。 [S5]
- **DEF-7** 管理的範圍從一段提示擴大到整個上下文狀態：系統指令、工具、外部資料、對話歷史。 [S5]
- **DEF-8** 問題從「怎麼找到對的字句」變成「什麼樣的上下文配置，最可能讓模型做出想要的行為」。 [S5]
- **DEF-9** Lütke 的說法：提供讓任務可解所需的所有上下文；Anthropic 的說法：找出最小的一組高訊號 token。這兩個說法出自不同文章，這裡只並列。 [S1][S5]
- **DEF-10** Prompt engineering 的重點是怎麼寫好指令，尤其是系統提示；Anthropic 把 context engineering 視為它的自然延伸。 [S5]
- **DEF-11** Willison 指出，多數人把「prompt engineering」理解成「在聊天機器人裡打字」。 [S1]
