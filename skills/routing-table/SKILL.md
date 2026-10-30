---
name: routing-table
description: "意图分流表。根据用户输入判断该走哪个技能、哪条生产路径。请求模糊、跨多个技能、或不知道该用哪个技能时先过这里。"
version: "1.1.0"
---

# routing-table — 意图分流

分流只解决一件事：这个请求进哪条门。根 SKILL.md 的门控流程（Fast Lane / Intake / Director / 各 Gate）和 Authority Order 是上位规则，本表是它们的查表版，冲突时以根 SKILL.md 为准。

## 何时读 references

分流规则在 `references/data.yaml` 的 `routing_rules` 与 `skill_routing`，意图识别读 `intent_identification`，决策树读 `routing_decision_tree`。先看 `references/sections.md` 定位，只读命中的分支。

## Workflow

1. 先认意图：是要写剧本、做分镜、写 prompt、生成帧、重拍、评分、还是查资料。认不出就问一句，不要猜着往下走。
2. 按 routing_rules 对到技能和路径。跨技能的请求拆成串行步骤，先上游后下游：剧本 → 分镜 → 关键帧 → prompt → 生成 → 重拍。
3. 模型选择不在本表拍板，走 Model Gate 并查 `adapters/model_facts.yaml`；本表只负责把请求送到对的门。
4. Fast Lane 情形（单镜、需求完整、无角色一致性要求）直接跳过分流，按根 SKILL.md 的快速通道走。

## Gotchas

分流错比执行差更贵：把叙事请求分到模板库，后面每一步都合格，合起来不是用户要的东西。意图拿不准时宁可多问一句。

不要因为用户提了某个词就直达对应技能。用户说「关键帧」可能实际要的是首帧定妆，听完整需求再分流。

新技能上线要同步更新本表，不然分流永远分不到它——本表刚补齐全部 20 个技能的去向，改动技能清单时记得回这里对账。

## 规则

- 一次分流只给一条主路径，备选路径最多给一条并写明触发条件。
- 分流结果要能复述：为什么进这条门，一句话说清，说不清说明意图还没认准。
