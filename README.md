# 🎬 Kling AI Prompt Engineering — Director-Grade Video Generation Guide

> **可灵 AI 提示词工程 — 导演式视频生成指南**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Kling AI](https://img.shields.io/badge/AI%20Video-Kling%20v3-purple)](https://klingai.com)

**Core Idea: Direct the model, don't tweak pixels.**

Don't ask the model for "cinematic feel" — answer: *what does this shot do to the audience?*

核心理念：导演模型，而非微调画面。不要向模型要"电影感"，要回答：这个镜头对观众做了什么？

**Compatible Models:** Kling v3 / v2.5-turbo / v2-1-master / video-o1
**Modes:** Text-to-Video · Image-to-Video · Multi-Image Omni · Video Extension · Motion Transfer · Lip Sync

---

## 🚀 Quick Start — 30 秒入门

```
1. What does this shot do to the audience? (one intention)
2. Shot size + angle + camera movement = shot setup
3. Lighting + sound + constraints = atmosphere
4. One sentence = one beat, one clip = one change
```

### Prompt Formula

```
[Subject + Action] + [Shot Setup] + [Lighting Change] + [Sound] + [Constraints]
```

**Example:**

```
On a rainy night, a courier crosses a slippery overpass as a metal gate slowly closes.
Camera: Low-angle side tracking shot, left to right, stopping on the courier's hand grabbing the gate.
Lighting: Amber work lights in thin mist, moonlight tracing cold outlines on wet metal.
Sound: Rain on steel, breathing, gate motor hum.
Constraints: No text, no logos, no extra people.
```

---

## 📚 Documentation Index

### 🆕 v1.1 — New Additions

| Feature | Source | Added to |
|---------|--------|----------|
| Beat Direction (节拍编排) | HyperFrames | 01-directing-engine.md § Step 7 |
| Composition Density (构图密度) | HyperFrames | 09-anti-slop.md § 构图密度规则 |
| Multi-Modal Reference Formula | Seedance 2.0 | 05-multi-image-omni.md § 多模态引用公式 |
| Video Editing Operations | Seedance 2.0 | 06-video-extension.md § 视频编辑操作 |
| Video Extension Formulas | Seedance 2.0 | 06-video-extension.md § 视频续写公式 |
| Portrait Consistency Strategy | Seedance Studio | 04-i2v-guide.md § 人物一致性策略 |

| Doc | Content |
|-----|---------|
| [01-directing-engine](01-directing-engine.md) | Director Engine: 5-step reading → consistency principles → scene types |
| [02-shot-language](02-shot-language.md) | Shot Language: sizes, angles, camera movements, support modes |
| [03-t2v-guide](03-t2v-guide.md) | Text-to-Video: prompt structure, multi-shot syntax, duration control |
| [04-i2v-guide](04-i2v-guide.md) | Image-to-Video: hold vs change mode, character/product protection |
| [05-multi-image-omni](05-multi-image-omni.md) | Multi-Image Reference: character lock, motion ref, camera ref |
| [06-video-extension](06-video-extension.md) | Video Extension: continuation, drift repair, sequence state |
| [07-motion-transfer](07-motion-transfer.md) | Motion Transfer: reference video → character image → action graft |
| [08-audio-guide](08-audio-guide.md) | Audio: native audio, dialogue, lip sync, audio-visual relationship |
| [09-anti-slop](09-anti-slop.md) | Anti-Slop Lexicon: 6 categories of empty words + replacement table |
| [10-allocation-model](10-allocation-model.md) | Budget Allocation: identity fidelity vs action amplitude vs scene density |
| [11-genre-guides](11-genre-guides.md) | Genre Guides: product ads, short drama, action, animation, food, scenery |
| [12-kling-capability-map](12-kling-capability-map.md) | Kling Capability Map: what it can do, how to use it, workarounds |
| [13-templates](13-templates.md) | Ready-to-Use Templates: prompt skeletons for every mode and scenario |
| [14-model-mechanics](14-model-mechanics.md) | Model Mechanics: understanding why the generator works this way |

### 🔧 Advanced References (for Hermes Agent integration)

| Doc | Content |
|-----|---------|
| [15-kling-rest-api](15-kling-rest-api.md) | REST API calls: domain, auth, params, multi-shot, voice, Python templates |
| [16-ai-short-drama-workflow](16-ai-short-drama-workflow.md) | AI Short Drama workflow: script → storyboard → video → editing |
| [17-prompt-package-template](17-prompt-package-template.md) | Prompt Package template: standard output format, character cards, first-frame rules |

---

## 🎯 Cross-Reference: "I want to..."

| Goal | Go to |
|------|-------|
| Don't know how to analyze a scene | 01-directing-engine · Step 1 |
| Prompt is too vague, no specific shots | 02-shot-language |
| All my words are "cinematic" / "epic" | 09-anti-slop |
| One image → video, don't know what to write | 04-i2v-guide |
| Multi-image reference, character assignment unclear | 05-multi-image-omni |
| Video extension won't connect | 06-video-extension |
| Character motion transfer | 07-motion-transfer |
| Add dialogue / lip sync | 08-audio-guide |
| Character face melting / product logo warped | 10-allocation-model |
| Don't know what Kling can do | 12-kling-capability-map |
| Want ready-made templates to edit | 13-templates |

---

## ⚡ Core Methodology: Director Engine

### Step 1 — Five Director Questions

Before writing a prompt, answer:

1. **Function:** What does this scene do in the story? (introduce / deepen / turn / close)
2. **Turn:** What's the value reversal? (safe→threat / stranger→ally / control→powerless)
3. **Perspective:** Whose experience are we in?
4. **Power:** Who holds power, and how does it move?
5. **Subtext:** What's true but unsaid?

### Step 2 — Consistency Principle

**One intention — all technical elements play the same note.**

| Technical Element | How to Express Intention |
|-------------------|------------------------|
| Shot Size | Close-up = inner world; Wide = scale / isolation |
| Angle | Low = empowerment; High = weakening; Eye-level = equality |
| Camera Move | Push = discovery; Pull = reveal; Static = held breath |
| Lighting | Soft = safe; Side = mystery; Backlight = drama |
| Sound | Intimate = thinner; Threat = thicker |

### Step 3 — Budget Allocation

Each generation has a finite budget. Pick ONE as primary spend:

| Primary Spend | Secondary | Save |
|---------------|-----------|------|
| Product identity (ref anchor) | Material motion | Scene density |
| Action amplitude (motion ref) | Identity (character image) | Face close-ups |
| Scene density / atmosphere | Camera movement | Character identity |

---

## 🚫 Anti-Slop Rules

> If a word can't be detected by a camera, microphone, light meter, or stopwatch — rewrite it.

| Empty Word | Replace With |
|-----------|-------------|
| Cinematic | Shot size + movement + lighting + color grade |
| Epic | Physical scale + crowd + camera distance |
| Breathtaking | Visible contrast / reveal / motion |
| 8K / Masterpiece | DELETE |
| Moody / Atmospheric | Light source + color temp + ambient sound |
| Premium / Luxurious | Material + whitespace + controlled lighting |

**Negation Rule:** "No blur" → "Hands resting still on the table." Only use negation in the constraints slot.

---

## 🏗️ Project Structure

```
kling-prompt-engineering/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── 01-directing-engine.md             # Director methodology
├── 02-shot-language.md                # Camera grammar reference
├── 03-t2v-guide.md                    # Text-to-Video guide
├── 04-i2v-guide.md                    # Image-to-Video guide
├── 05-multi-image-omni.md             # Multi-image reference
├── 06-video-extension.md              # Video continuation
├── 07-motion-transfer.md              # Motion transfer
├── 08-audio-guide.md                  # Audio & lip sync
├── 09-anti-slop.md                    # Anti-slop dictionary
├── 10-allocation-model.md             # Budget allocation model
├── 11-genre-guides.md                 # Genre-specific guides
├── 12-kling-capability-map.md         # Kling capabilities & limits
├── 13-templates.md                    # Ready-to-use prompt templates
├── 14-model-mechanics.md              # Model mechanics theory
├── 15-kling-rest-api.md               # REST API reference
├── 16-ai-short-drama-workflow.md      # Short drama production workflow
└── 17-prompt-package-template.md      # Prompt package format
```

---

## ⚠️ Common Pitfalls

1. **Writing "cinematic" etc.** The model can't process abstract evaluations. Use physical descriptions.
2. **Too many actions in one shot.** One shot = one beat = one change. Split multi-action into segments.
3. **Negation as quality insurance.** "No blur, no distortion" actually summons those concepts. Describe what IS there.
4. **Re-describing reference image info.** For I2V, only write what the image CAN'T show: motion, light change, sound. First line: "Keep X unchanged."
5. **Dialogue sentences too long.** 15-second lip sync budget: Chinese = one short clause, English = 5-10 words.
6. **Using output as reference for continuation.** Always re-anchor with the original reference image.
7. **Not declaring exclusions for reference characters.** Motion reference carries appearance. Must write: "Do not copy performer's appearance."
8. **Expecting text/logo rendering.** Put text in post-production. Logo: lock camera + light motion.

---

## 🤝 Contributing

Issues and PRs welcome. If you have Kling prompt tips that work consistently, share them!

## 📄 License

MIT — use freely, credit appreciated.

---

## 🙏 Credits

Methodology ported from [seedance-2.0 Skill OS](https://github.com/Emily2040/seedance-2.0) director engine, adapted and expanded for Kling AI's specific capabilities and constraints.

---

<p align="center">
  <i>导演模型，而非微调画面。</i><br>
  <i>Direct the model. Don't tweak pixels.</i>
</p>
