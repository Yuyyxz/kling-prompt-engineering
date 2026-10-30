---
name: timeline-format
description: "时间轴格式提示词。给 Seedance、可灵等模型写带时间戳分段的时间轴 prompt，含续写和多集衔接。模型吃时间轴语法、单次要出多段内容时用。"
version: "1.1.0"
---

# timeline-format — 时间轴格式

时间轴 prompt 是把分镜的时间结构直接写给模型的格式：哪几秒发生什么、声音怎么走、参考怎么挂。现行生产里分镜的权威中间产物是结构化 JSON（`schemas/storyboard.schema.json`），时间轴文本是从 JSON 渲染出来的一种投喂格式，不要反过来拿文本当源头改。

## 何时读 references

格式规范读 `references/data.yaml` 的 `timeline_spec`，风格与场景段写法读 `style_description`、`scene_description`、`sound_design`，续写和多集读 `video_extension`、`multi_episode`。先看 `references/sections.md` 定位。示例在 `timeline_examples`，套格式前先看一条。

## Workflow

1. 从结构化分镜出发：每个 shot 对应一个时间段，时长逐字抄 JSON，不要临场重估。
2. 按 spec 拼时间轴：风格段在前定调，逐段写画面、运镜、声音，参考素材在段内指名分工。
3. 声音段和时间轴对齐：Seedance 系以音频为时钟，对白和音乐的落点先定，画面段跟着音频长度走。
4. 总时长和模型单次上限对一遍（`adapters/model_facts.yaml`）：超限就分段生成加续写，不要把 30 秒的轴塞进 10 秒的模型。
5. 续写时上一段的尾帧状态写进下一段的起始状态，多集衔接同理，状态交接不清是跨段漂移的主因。

## Gotchas

时间段不要切太碎。一秒一段模型跟不上节拍，按戏剧节拍切段，一段一个节拍，和单镜单节拍是同一条纪律。

时间轴里写了模型不支持的东西（多主体分别计时之类）不会报错，只会默默做不到。投喂前过一遍 `scripts/adapt_prompt.py` 的目标模型警告。

文本版和 JSON 版对不上时以 JSON 为准并回改文本。两份都改只会越改越分叉。

## 规则

- 时间戳用绝对秒数段（0–4s），不用「开头、中间」这类相对说法。
- 每段必须有声音设计，哪怕是环境声或静默，留空等于让模型乱配。
