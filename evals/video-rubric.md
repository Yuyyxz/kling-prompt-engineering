# 成片评分量表（Video Rubric）

prompt 层评测在 `rubric.md`（评文本），这份评**成片**。维度骨架借
VideoScore（TIGER-Lab，VideoFeedback 37.6K 条人工标注训练，与人工评分的
Spearman 相关最高 0.77）的五维，再加 KPE 生产里最常翻车的两个维度。
全部 1–4 分，4 最好。打分可以是人工，也可以是 VLM 看片/抽帧，
但同一轮对比里评分者必须一致，换评分者要重打基线。

## 维度与锚点

| 维度 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| visual_quality 视觉质量 | 无伪影，质感达到 prompt 声明的设备/胶片感 | 轻微瑕疵，不细看不觉 | 明显涂抹/闪烁/塑料感 | 大面积崩坏，不可用 |
| temporal_consistency 时序一致 | 全程无变形无闪跳 | 局部轻微漂移 | 中段出现变形或跳变 | 主体形态持续不稳定 |
| dynamic_degree 动态程度 | 动作幅度与分镜要求匹配且自然 | 略欠或略过 | 明显僵止或乱动 | 基本静止/动作完全失控 |
| text_alignment 文图对齐 | 主体、动作、场景、光线全中 | 漏 1 个次要元素 | 漏关键动作或场景错位 | 画面与 prompt 基本无关 |
| factual_consistency 事实一致 | 物理与常识全对（手指数、文字、空间关系） | 1 处小错 | 多处不合理 | 物理崩坏，如穿模、物体凭空出现 |
| character_consistency 角色一致 | 与角色卡逐项对得上，全程同一人 | 服饰/发型有小漂移 | 五官或体型明显变了 | 换人 |
| audio_sync 音画同步 | 对白口型、音效落点全对齐 | 偏差 <0.3s 级别 | 对白与口型明显脱节 | 无音频或完全错位；无声镜头填 null 不计 |

## 记录格式

一行一个成片，JSON Lines，存项目自己的文件（模板见
`evals/video-scores.example.jsonl`）：

```json
{"case_id": "天台决定/SHOT-02", "model": "kling_3_0", "prompt_version": "sb-1.0.0",
 "prompt_sha256": "…", "scorer": "human|vlm:<name>", "scores":
 {"visual_quality": 3, "temporal_consistency": 3, "dynamic_degree": 2,
  "text_alignment": 4, "factual_consistency": 3, "character_consistency": 2,
  "audio_sync": null}, "note": "一句话写最主要的扣分点"}
```

## 怎么用

- `python3 evals/score_video.py <scores.jsonl>` 按（模型 × prompt 版本）
  聚合各维均分与总均分；
- `--save-baseline evals/video-baseline.json` 把当前聚合存为基线；
- 之后每次跑自动与基线对比，任一维度回退超过 0.3 标出（退出码 1），
  防止改 prompt/换模型时悄悄变差——对应 promptfoo 式基线回归的做法；
- 分数本身别跨评分者、跨项目直接比，只比同一基线体系内的变化。

维度来源：VideoScore 五维 https://tiger-ai-lab.github.io/VideoScore/ ；
分类法参照 EvalCrafter 四大类 https://github.com/evalcrafter/EvalCrafter 。
