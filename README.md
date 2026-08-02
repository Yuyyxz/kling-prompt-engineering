# 🎬 Kling AI Prompt Engineering — Director-Grade Video Generation

> **可灵 AI 提示词工程 — 导演式视频生成指南**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Kling AI](https://img.shields.io/badge/AI%20Video-Kling%20v3-purple)](https://klingai.com)

**Core Idea: Direct the model, don't tweak pixels.**

不要向模型要"电影感"——回答：*这个镜头对观众做了什么？*

**Compatible Models:** Kling v3 / v2.5-turbo / v2-1-master / video-o1
**Modes:** Text-to-Video · Image-to-Video · Multi-Image Omni · Video Extension · Motion Transfer · Lip Sync

---

## 🚀 Quick Start — 30 秒入门

**方式一：装 Skill（推荐）**

```bash
# Claude Code
curl -sL https://raw.githubusercontent.com/Yuyyxz/kling-prompt-engineering/main/install.sh | bash -s claude

# Cursor
curl -sL https://raw.githubusercontent.com/Yuyyxz/kling-prompt-engineering/main/install.sh | bash -s cursor

# 自定义目录
curl -sL https://raw.githubusercontent.com/Yuyyxz/kling-prompt-engineering/main/install.sh | bash -s generic -d ~/.custom/skills/
```

装完后直接对 AI 说："帮我拍一个产品视频"——它会自动引导你完成提示词生成。

**方式二：读文档（进阶）**

```
1. 这个镜头对观众做了什么？（一个意图）
2. 景别 + 角度 + 运镜 = 镜头设置
3. 光源 + 声音 + 约束 = 氛围
4. 一句话 = 一个节拍，一个片段 = 一个变化
```

**方式三：一页纸速查**

直接看 [cheatsheet.md](cheatsheet.md)——公式、五问、替换表、示例全在一页。

---

## 🧠 Root SKILL.md — 导演引擎入口

项目根目录的 [`SKILL.md`](SKILL.md) 是标准 Claude Code / Cursor skill 入口，实现了：

- **Fast Lane**：简单请求直接出提示词，不跑完整流程
- **Operating Loop**：复杂请求走 9 个 Gate（导演五问 → 模式选择 → 能力检查 → 素材权威 → 构建 → 质量检查 → 诊断 → 安全）
- **Authority Order**：规则冲突时的 9 级优先级裁决

标准格式子 Skill 位于 `skills/*/SKILL.md` 目录（兼容 Claude Code 原生加载）。

---

## 🔧 Tools

```bash
# 提示词质量检查（Anti-Slop 可执行版）
python scripts/prompt_lint.py "你的提示词"

# 自动化评测（LLM-judge 打分）
python evals/run_evals.py

# 格式验证
python scripts/validate_all.py skills/
```

---

## 📦 Available Skills

| Skill | 用途 | 触发词 |
|-------|------|--------|
| `director-engine.skill` | 导演引擎：意图→技术执行 | "帮我拍"、"AI视频"、"可灵" |
| `kling-screenwriting.skill` | 编剧助手 | "编剧"、"写剧本"、"故事" |
| `kling-templates.skill` | 即用模板库（30+类型） | "模板"、"给我一个提示词" |
| `kling-style-tags.skill` | 风格标签系统 | "风格"、"宫崎骏"、"赛博朋克" |
| `kling-storyboard.skill` | 分镜表输出 | "分镜"、"storyboard" |
| `timeline-format.skill` | 时间轴格式提示词 | "时间轴"、"timeline" |
| `domain-skills.skill` | 15个行业垂直模板 | "电商"、"美食"、"房地产" |
| `failure-atlas.skill` | 失败诊断与修复 | "生成失败"、"效果不好" |
| `anti-slop.skill` | 弱词替换 | "提示词太虚"、"不具体" |

完整列表见 [`skills/`](skills/) 目录。

---

## ⚡ Prompt Formula

```
[主体 + 动作] + [镜头设置] + [光线变化] + [声音] + [约束]
```

**Example:**

```
On a rainy night, a courier crosses a slippery overpass as a metal gate slowly closes.
Camera: Low-angle side tracking shot, left to right, stopping on the courier's hand grabbing the gate.
Lighting: Amber work lights in thin mist, moonlight tracing cold outlines on wet metal.
Sound: Rain on steel, breathing, gate motor hum.
Constraints: No text, no logos, no extra people.
```

**导演五问（写提示词前先回答）：**

1. **功能** — 这个场景在故事中做什么？（引入/深化/转折/收束）
2. **转折** — 价值反转是什么？（安全→威胁 / 陌生人→盟友）
3. **视角** — 我们在谁的体验里？
4. **权力** — 谁持有权力，如何流动？
5. **潜台词** — 什么是真实但未说出的？

详见 [01-directing-engine.md](01-directing-engine.md)。

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

**Negation Rule:** "No blur" → "Hands resting still on the table." 否定句只放在约束槽。

详见 [09-anti-slop.md](09-anti-slop.md)。

---

## 📚 Documentation Index

| Doc | Content |
|-----|---------|
| [01-directing-engine](01-directing-engine.md) | 导演引擎：导演五问 → 一致性原则 → 节拍编排 → 引导式构建 → 魔法前缀 |
| [02-shot-language](02-shot-language.md) | 镜头语言：景别、角度、运动、支撑、FPV/无人机 |
| [03-t2v-guide](03-t2v-guide.md) | 文生视频：提示词结构、多镜头语法、时长控制 |
| [04-i2v-guide](04-i2v-guide.md) | 图生视频：保持 vs 变化模式、角色/产品保护 |
| [05-multi-image-omni](05-multi-image-omni.md) | 多图参考：角色锁定、运动参考、相机参考 |
| [06-video-extension](06-video-extension.md) | 视频延长：续写、漂移修复、序列状态 |
| [07-motion-transfer](07-motion-transfer.md) | 运动迁移：参考视频 → 角色图 → 动作嫁接 |
| [08-audio-guide](08-audio-guide.md) | 音频：原生音频、对白、口型同步、视听关系 |
| [09-anti-slop](09-anti-slop.md) | Anti-Slop 词典：6 类空话 + 替换表 |
| [10-allocation-model](10-allocation-model.md) | 预算分配：身份保真 vs 动作幅度 vs 场景密度 |
| [11-genre-guides](11-genre-guides.md) | 类型指南：15 种类型（产品/短剧/动作/动画/美食/风景/VFX/科幻/恐怖/纪录片/MV/时尚/教育/体育/旅行） |
| [12-kling-capability-map](12-kling-capability-map.md) | 可灵能力图：能做什么、怎么用、绕过限制 |
| [13-templates](13-templates.md) | 即用模板：每种模式和场景的提示词骨架 |
| [14-model-mechanics](14-model-mechanics.md) | 模型机制：理解生成器为什么这样工作 |
| [18-troubleshooting-gallery](18-troubleshooting-gallery.md) | 故障排除：10 种常见失败模式 + 修复方法 |
| [19-cinematography-dictionary](19-cinematography-dictionary.md) | 电影摄影词典：100+ 项术语速查 |
| [20-style-tags](20-style-tags.md) | 风格标签：8 导演风格 + 8 视觉风格 + 6 情绪风格 + 组合公式 |

### Advanced References

| Doc | Content |
|-----|---------|
| [adapters/model_router.yaml](adapters/model_router.yaml) | 模型路由层配置（Kling / Seedance 已实现，Runway / Sora / Pika 规划中） |
| [adapters/kling_adapter.yaml](adapters/kling_adapter.yaml) | Kling 模型专属配置 |
| [adapters/seedance_adapter.yaml](adapters/seedance_adapter.yaml) | Seedance 模型专属配置 |
| [adapters/prompt_translator.yaml](adapters/prompt_translator.yaml) | 多语言提示词翻译器 |
| [examples/model_routing_examples.yaml](examples/model_routing_examples.yaml) | 5 个完整路由使用示例 |
| [workflows/video_pipeline.yaml](workflows/video_pipeline.yaml) | 条件触发确认制 6 步生产流水线 |

---

## 🎯 Cross-Reference: "I want to..."

| Goal | Go to |
|------|-------|
| 不知道怎么分析场景 | [01-directing-engine](01-directing-engine.md) · Step 1 |
| 提示词太虚，没有具体镜头 | [02-shot-language](02-shot-language.md) |
| 全是 "cinematic" / "epic" | [09-anti-slop](09-anti-slop.md) |
| 一张图 → 视频，不知道写什么 | [04-i2v-guide](04-i2v-guide.md) |
| 多图参考，角色分配不清 | [05-multi-image-omni](05-multi-image-omni.md) |
| 视频延长接不上 | [06-video-extension](06-video-extension.md) |
| 角色动作迁移 | [07-motion-transfer](07-motion-transfer.md) |
| 加对白 / 口型同步 | [08-audio-guide](08-audio-guide.md) |
| 角色脸融了 / 产品 logo 变形 | [10-allocation-model](10-allocation-model.md) |
| 不知道可灵能做什么 | [12-kling-capability-map](12-kling-capability-map.md) |
| 想要现成模板改一改 | [13-templates](13-templates.md) |
| 生成失败了怎么修 | [18-troubleshooting-gallery](18-troubleshooting-gallery.md) |

---

## ⚠️ Common Pitfalls

1. **写 "cinematic" 等抽象词。** 模型无法处理抽象评价，用物理描述替代。
2. **一个镜头塞太多动作。** 一镜 = 一拍 = 一变。多动作拆成多段。
3. **用否定句当质量保险。** "No blur, no distortion" 反而会召唤这些概念。描述你要的。
4. **重复描述参考图已有的信息。** I2V 只写图片无法展示的：运动、光变、声音。首行写 "Keep X unchanged"。
5. **对白太长。** 15 秒口型预算：中文 = 一个短分句，英文 = 5-10 词。
6. **用输出当续写参考。** 永远用原始参考图重新锚定。
7. **不声明排除参考角色外貌。** 运动参考会携带外貌，必须写 "Do not copy performer's appearance"。
8. **期望文字/logo 渲染。** 文字放后期。Logo：锁相机 + 微光动。

---

## 🏗️ Project Structure

```
kling-prompt-engineering/
├── README.md                          # 本文件
├── CHANGELOG.md                       # 版本历史
├── CLAUDE.md                          # 项目规范（AI 消费）
├── LICENSE                            # MIT License
├── install.sh                         # 一键安装脚本
├── requirements.txt                   # Python 依赖
├── 01-directing-engine.md             # 导演方法论
├── 02-shot-language.md                # 镜头语法参考
├── 03-t2v-guide.md                    # 文生视频指南
├── 04-i2v-guide.md                    # 图生视频指南
├── 05-multi-image-omni.md             # 多图参考
├── 06-video-extension.md              # 视频延长
├── 07-motion-transfer.md              # 运动迁移
├── 08-audio-guide.md                  # 音频与口型同步
├── 09-anti-slop.md                    # Anti-Slop 词典
├── 10-allocation-model.md             # 预算分配模型
├── 11-genre-guides.md                 # 类型指南
├── 12-kling-capability-map.md         # 可灵能力与限制
├── 13-templates.md                    # 即用提示词模板
├── 14-model-mechanics.md              # 模型机制理论
├── 18-troubleshooting-gallery.md      # 故障排除案例库
├── 19-cinematography-dictionary.md    # 电影摄影词典
├── 20-style-tags.md                   # 风格标签系统
├── adapters/                          # 模型适配器
│   ├── model_router.yaml              # 模型路由配置
│   ├── base_adapter.yaml              # 基础适配器接口
│   ├── kling_adapter.yaml             # Kling 适配器
│   ├── seedance_adapter.yaml          # Seedance 适配器
│   └── prompt_translator.yaml         # 提示词翻译器
├── skills/                            # Skill 文件（AI 工具消费）
│   ├── director-engine.skill          # 导演引擎 (P0)
│   ├── timeline-format.skill          # 时间轴格式 (P0)
│   ├── domain-skills.skill            # 领域垂直 (P1)
│   ├── multi-episode-narrative.skill  # 多集叙事 (P1)
│   ├── anti-slop.skill                # Anti-Slop (P1)
│   ├── routing-table.skill            # 路由表 (P2)
│   ├── failure-atlas.skill            # 失败诊断 (P2)
│   ├── material-numbering.skill       # 素材编号 (P2)
│   ├── multilingual-vocabulary.skill  # 多语言词汇 (P3)
│   ├── validation-scripts.skill       # 验证脚本 (P3)
│   ├── multi-platform.skill           # 多平台兼容 (P3)
│   └── ...                            # 更多 Skill
├── scripts/                           # 工具脚本
│   ├── validate_all.py                # 综合验证
│   ├── validate_yaml.py               # YAML 格式验证
│   ├── validate_required_fields.py    # 必需字段验证
│   ├── validate_vocab_coverage.py     # 词汇覆盖验证
│   ├── validate_naming_convention.py  # 命名规范验证
│   ├── validate_version.py            # 版本号验证
│   └── generate_docx.py              # 文档导出（一次性工具）
├── examples/                          # 使用示例
│   └── model_routing_examples.yaml    # 模型路由示例
├── workflows/                         # 生产流水线
│   └── video_pipeline.yaml            # 6 步条件触发流水线
├── references/                        # 参考资料
│   ├── anti_slop_lexicon.md           # 弱词词典
│   ├── failure_atlas.md               # 失败图谱
│   └── negative_prompt_library.md     # 负面提示词库
└── research/                          # 调研文档
    └── GitHub竞品调研报告.md           # 竞品分析
```

---

## 🔧 Validation

```bash
# 安装依赖
pip install -r requirements.txt

# 验证所有 Skill 文件
python scripts/validate_all.py skills/

# 验证单个文件
python scripts/validate_all.py skills/director-engine.skill
```

---

## 🤝 Contributing

Issues and PRs welcome. 如果你有经过验证的可灵提示词技巧，欢迎分享。

提交前请运行 `python scripts/validate_all.py skills/` 确保验证通过。

## 📄 License

MIT — use freely, credit appreciated.

## 🙏 Credits

Methodology ported from [seedance-2.0 Skill OS](https://github.com/Emily2040/seedance-2.0) director engine, adapted and expanded for Kling AI's specific capabilities and constraints.

---

<p align="center">
  <i>导演模型，而非微调画面。</i><br>
  <i>Direct the model. Don't tweak pixels.</i>
</p>
