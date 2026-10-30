---
name: multilingual-vocabulary
description: "多语言电影词汇表。6 种语言的原生电影术语（景别、运镜、光线等），写外语 prompt 或外语对白、用模型母语术语沟通时用。"
version: "1.1.0"
---

# multilingual-vocabulary — 多语言电影词汇

给模型写 prompt，术语要用它训练语料里的原生说法。中文「推镜头」逐字译过去的外语版本，模型未必当运镜指令读；用目标语言电影工业自己的词，它才照着执行。

## 何时读 references

六种语言的词汇表在 `references/data.yaml` 的 `chinese_vocabulary`、`english_vocabulary`、`japanese_vocabulary`、`korean_vocabulary`、`spanish_vocabulary`、`russian_vocabulary` 各节，先看 `references/sections.md` 定位到目标语言那一段，只读那一段。翻译规则在 `translation_rules`。

## Workflow

1. 先定这条 prompt 的主语言。依据是目标模型的强势语言，不是用户的母语；模型与语言的对应看 `adapters/model_facts.yaml` 的对白语种与各模型条目。
2. 结构按 KPE 的公式写，术语逐项换成目标语言的原生电影词，不要整句机翻。
3. 角色名、IP 名这类专名保持原文，不要音译；Seedance 平台屏蔽 IP 名的规则照旧（见 model_facts 的 ip_note）。
4. 对白另走一遍：对白语言和 prompt 语言可以不同，写明对白语种，口型支持范围先查 model_facts。

## Gotchas

中英混写不是偷懒，是有意的策略：主体和动作中文、设备与镜头术语英文，在可灵这类双语模型上是已验证的打法。但混写要有分工，不能一句里来回跳。

俄语词汇表在库里但主流模型对俄语 prompt 的支持没验证过，用之前先小样测一条，不要整集押上去。

词汇表给的是术语，不是整句。把术语拼回句子时语法按目标语言来，术语正确但句子不通，模型照样读偏。

## 规则

- 同一集内 prompt 主语言保持一致，中途换语言会让风格 token 的执行也跟着漂。
- 新术语先验证再进表：拿一条已知 prompt 只换术语测效果，有效才收录，并注明验证模型。
