# S4　Chroma〈Context Rot: How Increasing Input Tokens Impacts LLM Performance〉

- 作者：Kelly Hong、Anton Troynikov、Jeff Huber（Chroma 技術報告）
- 日期：2025-07-14
- 原文網址：https://www.trychroma.com/research/context-rot
- raw 檔案：[S4-chroma.md](../../raw/S4-chroma.md)
- 讀到的範圍：**只讀到部分**。前言、實驗設計、前幾個實驗與 LongMemEval 的主要結果有讀到；「重複字詞」實驗的結果、限制與結論沒有讀到，本 wiki 不引用那些部分。

## 這篇在講什麼

用實驗測量「只把輸入變長、任務難度不變」時，模型表現會怎麼變。結論是輸入越長，表現越不可靠。

## 重點

- 一般假設模型會平均地使用整段上下文，但實驗顯示不是：輸入越長，表現越不可靠。
- 共測試 18 個模型，包含 GPT-4.1、Claude 4、Gemini 2.5、Qwen3 系列。
- 每個任務都刻意設計得很簡單，只改變輸入長度，藉此單獨量出長度的影響。
- 問題和答案句的語意越不像，表現隨長度下降得越快。
- 只要加入一個干擾句（和問題相關但不是答案），表現就比沒有干擾時差；加到四個更差。
- 文章順序正常的長文，反而比句子被打亂的長文更難找到答案。
- 在對話記憶測驗中，只給相關片段（約 300 token）的表現，明顯高於給完整歷史（約 113k token）。
- 作者認為真實應用更複雜，長度的影響只會更明顯。

## 相關概念頁

- [Context Rot（上下文腐化）](../concepts/context-rot.md)
