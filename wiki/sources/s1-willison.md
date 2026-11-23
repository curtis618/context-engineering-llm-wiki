# S1　Simon Willison〈Context engineering〉

- 作者：Simon Willison（個人部落格）
- 日期：2025-06-27
- 原文網址：https://simonwillison.net/2025/Jun/27/context-engineering/
- raw 檔案：[S1-willison.md](../../raw/S1-willison.md)
- 讀到的範圍：全文。文中引用的兩則推文只讀到這篇文章轉述的部分。

## 這篇在講什麼

一篇短文，說明為什麼「context engineering」這個詞比「prompt engineering」更好，並引用 Tobi Lütke 與 Andrej Karpathy 對這個詞的定義。

## 重點

- Willison 認為「context engineering」正在取代「prompt engineering」，而且這個詞可能會留下來。
- 他以前替「prompt engineering」辯護過，但發現多數人把它理解成「在聊天機器人裡打字」。大家自己推測出來的意思，才是會留下來的意思。
- 他認為「context engineering」讓人直覺想到的意思，比較接近它真正的意思。
- Tobi Lütke（Shopify 執行長）的定義：提供所有必要的上下文，讓任務有可能被 LLM 解決的藝術。
- Andrej Karpathy 的定義：把「剛好對的資訊」填進上下文視窗，供下一步使用的精細藝術與科學。
- Karpathy 說它同時是科學也是藝術。科學的部分包括任務說明、少量範例（few-shot examples）、RAG、相關資料、工具、狀態與歷史、壓縮；藝術的部分是對 LLM「心理」的直覺。
- 文章沒有說這個詞是誰發明的。

## 相關概念頁

- [什麼是 Context Engineering](../concepts/what-is-context-engineering.md)
