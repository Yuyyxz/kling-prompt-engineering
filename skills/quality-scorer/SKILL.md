---
name: quality-scorer
description: "质量评分（prompt 层）。按维度给 prompt 打分和分级，给出改进建议。交付前自评、比较两个 prompt 版本优劣时用。成片评分不在这里，去 evals/video-rubric.md。"
version: "1.1.0"
---

# quality-scorer — 质量评分（prompt 层）

先划界：这个技能评的是 prompt 文本，成片质量走 `evals/video-rubric.md` 的七维量表加 `evals/score_video.py`，两套不要混用同一张表。文本层还有机器门禁 `scripts/prompt_lint.py`，lint 管空话和硬项，本技能管维度分和改进方向。

## 何时读 references

维度定义读 `references/data.yaml` 的 `scoring_dimensions`，计算与分级读 `score_calculation`、`score_grades`，改进建议的写法读 `improvement_suggestions`。先看 `references/sections.md` 定位。

## Workflow

1. 先跑 prompt_lint，硬项不过的先回去改，不要带病评分。
2. 按维度逐项打分，每项给分必须带一句依据：扣分扣在哪一行、哪个词。
3. 汇总分级，按 score_grades 给出等级和能不能交付的结论。
4. 改进建议按影响排序：先改影响最大的维度，一次给不超过三条，建议要具体到改哪句、换成什么。

## Gotchas

打分最容易犯的是印象分：整体顺眼就全项高分。逐项打、逐项给依据，就是为了防这个。

两个版本比优劣时必须盲评顺序：先各自打分再对照总分，不要先定结论再凑分。

分数只在同一评分者、同一量表内可比。跨人、跨版本的分数直接比大小没有意义，这点和成片基线回归的纪律一样。

## 规则

- 评分结论要落到动作：交付、改后交付、还是推倒重写，三选一，不许只给分不给结论。
- 改进建议禁止写「提升电影感」这类空话，建议本身也要过 anti-slop。
