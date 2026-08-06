# 可灵提示词工程 — 给拍视频的人写的手册

> 别向模型要"电影感"。回答一个问题：这个镜头对观众做了什么？

这是一个给 AI 视频生成写的提示词手册，以快手可灵（Kling）为主。不是论文，不是术语词典——是实战中总结出来的"怎么写 prompt 才能出片"。

25 个文件，从"我从来没写过"到"我要精确控制第 3 秒的音效对齐"，全覆盖。

**兼容模型：** Kling v3 / v2.5-turbo / v2-1-master / video-o1
**支持模式：** 文生视频 · 图生视频 · 多图参考 · 视频续写 · 动作迁移 · 口型同步

---

## 从哪里开始？

**先做这件事：** 打开 [17-user-journey.md](17-user-journey.md)，5 道题判断你在哪层。这个文件编号是 17，但你第一个该读它——知道自己在哪，才不会把时间浪费在不需要看的东西上。

然后按你的情况选路线：

**写过但总翻车？** → [09-anti-slop.md](09-anti-slop.md)（90% 的问题出在这），再查 [18-troubleshooting-gallery.md](18-troubleshooting-gallery.md) 的快速诊断表。

**想系统学？** → 按这个顺序：01 → 02 → 13 → 08 → 15 → 16。

**就想抄作业？** → 直接去 [13-templates.md](13-templates.md) 拿模板，或者看 [examples/](examples/) 里的 5 个完整案例。

---

## 核心思路（30 秒版）

写 prompt 之前先回答五个问题（导演五问）：

1. **这场戏干嘛的？** 引入 / 深化 / 转折 / 收束
2. **价值怎么变的？** 安全→威胁 / 陌生→盟友 / 掌控→无力
3. **观众站在谁那边？** 和主角一起紧张？还是在远处看？
4. **谁有权力？** 谁占空间、谁被挤到边缘
5. **没说出来的是什么？** 角色说的和角色要的之间的差距

答案决定后面一切——景别、角度、光线、运动、声音，全部服务于这五个答案。

**黄金公式：**
```
[谁 + 在哪 + 做什么] + [景别 + 角度 + 运动] + [光源 + 方向] + [声音] + [约束]
```

**一个完整例子：**
```
雨夜，快递员穿过湿滑的天桥，一扇铁门正在缓缓关闭。
镜头：低角度侧面跟拍，从左到右，停在快递员的手抓住铁门的瞬间。
光线：薄雾中的琥珀色工作灯，月光在湿金属上勾出冷色轮廓。
声音：雨打钢架、呼吸声、铁门电机嗡鸣。
约束：无文字、无 logo、无多余人物。
```

注意：没有"电影感""史诗感""8K"。每个词都能被摄影机或麦克风检测到。

---

## 反空话规则（最重要的事）

> 如果一个词不能被摄影机、麦克风、测光表或秒表检测到，改写它。

| 别写这个 | 改成这个 |
|---------|---------|
| 电影感 | 景别 + 运动 + 光线 + 色调 |
| 史诗感 | 物理规模 + 人群 + 镜头距离 |
| 8K / 杰作 / 高质量 | 删掉。一个字都别写 |
| 氛围感 / 高级感 | 光源 + 色温 + 材质 |
| 雨夜,霓虹,赛博朋克,4K | 写成一句话：谁在哪做什么 |

更多替换 → [09-anti-slop.md](09-anti-slop.md)

---

## 文件索引

### 基础层（入门必读）

| 文件 | 干什么用的 |
|------|-----------|
| [01-directing-engine.md](01-directing-engine.md) | 导演引擎：五问 → 三个补充字段 → 一致性原则 → 节拍编排 → 魔法前缀 |
| [02-shot-language.md](02-shot-language.md) | 镜头语言：景别、角度、运动、支撑方式、FPV |
| [03-t2v-guide.md](03-t2v-guide.md) | 文生视频：prompt 结构、多镜头语法、时长控制 |
| [04-i2v-guide.md](04-i2v-guide.md) | 图生视频：源素材承载规则、保持模式 vs 变化模式、人物/产品保护 |
| [09-anti-slop.md](09-anti-slop.md) | 反空话词典：6 类空话 + 替换表 + 中文空话陷阱 |
| [13-templates.md](13-templates.md) | 即用模板：每种模式的骨架 + Recipe Cards + 5 种组合模式库 |
| [17-user-journey.md](17-user-journey.md) | 用户分层路径：入门/进阶/专业三层 + 自测 + 推荐路线 |

### 进阶层（理解"为什么"）

| 文件 | 干什么用的 |
|------|-----------|
| [05-multi-image-omni.md](05-multi-image-omni.md) | 多图参考：角色锁定、运动参考、镜头参考 |
| [06-video-extension.md](06-video-extension.md) | 视频续写：续接、漂移修复、序列状态 |
| [07-motion-transfer.md](07-motion-transfer.md) | 动作迁移：参考视频 → 角色图 → 动作嫁接 |
| [08-audio-guide.md](08-audio-guide.md) | 音频指南：原生音频、对话、口型同步、10 场景音画配对示例 |
| [10-allocation-model.md](10-allocation-model.md) | 算力分配：身份保真 vs 动作幅度 vs 场景密度 |
| [11-genre-guides.md](11-genre-guides.md) | 类型片指南：叙事/非叙事分道 + 15 种类型（产品/短剧/动作/动画/美食/风景/VFX/科幻/恐怖/MV…） |
| [12-kling-capability-map.md](12-kling-capability-map.md) | 可灵能力地图：能做什么、不能做什么、怎么绕 |
| [16-language-strategy.md](16-language-strategy.md) | 中英文混合策略：什么用中文、什么用英文、速查表 |

### 专业层（精确控制）

| 文件 | 干什么用的 |
|------|-----------|
| [14-model-mechanics.md](14-model-mechanics.md) | 模型机制：理解生成器为什么这么工作 |
| [15-timeline-syntax.md](15-timeline-syntax.md) | 时间轴语法：状态层 + 运动层 + 节奏层，5 个完整示例 |
| [18-troubleshooting-gallery.md](18-troubleshooting-gallery.md) | 故障深度拆解：5 类 23 条，每条有完整 ❌→✅ 对比和原理分析 |
| [19-cinematography-dictionary.md](19-cinematography-dictionary.md) | 摄影术语词典：100+ 项（景别/角度/运动/光线/色彩/音频/VFX/构图） |
| [20-style-tags.md](20-style-tags.md) | 风格标签：8 导演风格 + 8 视觉风格 + 6 情绪风格 + 组合公式 |
| [21-retake-protocol.md](21-retake-protocol.md) | 重试协议：5 个判定、单变量规则、重试预算、拍摄日志、诚实退出 |
| [22-text-to-image.md](22-text-to-image.md) | 文生图完整指南：多模型适配（Kolors/Qwen/Seedream）、相机锚定、景深控制（光圈-视觉对照+虚化形状）、曝光控制（剪影/双重曝光/漏光/HDR）、色彩与影调（色温/互补色/7种电影调色）、完整布光体系（25种布光+光质+决策树）、光线词汇、情绪外化、类型专项指南（8种：人文街拍/广告/海报6模板/编辑杂志/建筑/角色概念艺术/中国风）、景观专项（9要素+6类型）、32种风格体系（12核心+20+扩展）、负面提示词策略、角色一致性、反塑料感、效果提升 |
| [23-first-last-frame.md](23-first-last-frame.md) | 首帧/尾帧完整指南：状态插值逻辑、好首帧5标准、好尾帧4标准、配对原则、T2I生成首帧6步流程、多镜头帧链式串联、常见翻车修复、3个实战案例（角色转身/产品变化/场景过渡） |

### 工作流

| 文件 | 干什么用的 |
|------|-----------|
| [workflows/storyboard-to-prompt.md](workflows/storyboard-to-prompt.md) | 分镜转 Prompt 工作流：Beat Board 输入格式、逐字段翻译规则、角色卡复用、风格 token 统一、3镜头翻译示例、质量检查清单 |

### 参考资料

| 文件 | 内容 |
|------|------|
| [references/anti_slop_lexicon.md](references/anti_slop_lexicon.md) | Anti-Slop 完整词库 |
| [references/failure_atlas.md](references/failure_atlas.md) | 失败诊断图谱速查表（一行一个问题，快速定位改哪句） |
| [references/negative_prompt_library.md](references/negative_prompt_library.md) | 反向检查清单（生成后对照排查，不是 prompt 模板） |
| [QUICK-REF.md](QUICK-REF.md) | 一页纸速查（贴在显示器边上那张） |
| [CHECKLIST.md](CHECKLIST.md) | 提交前检查清单 |
| [examples/](examples/) | 5 个完整实战案例 |
| [CHALLENGES.md](CHALLENGES.md) | 10 个提示词挑战（从 ⭐ 到 ⭐⭐⭐，练手用） |

---

## 5 种组合模式（速览）

你的场景该用哪种结构？选一个骨架，填入具体内容：

| 模式 | 公式 | 什么时候用 | 默认镜头 |
|------|------|-----------|---------|
| **定锚式** | 主体不动 + 单一动作 + 固定机位 | 产品、肖像、建筑 | 锁定 |
| **递进式** | 远景 → 中景 → 特写 | 故事、品牌、旅行 | 推 → 跟 → 锁定 |
| **对比式** | A 状态 —过渡→ B 状态 | 变身、季节、改造 | 锁定远景 |
| **揭示式** | 遮挡/模糊 → 清晰/全貌 | 悬念、揭幕、出场 | 缓推 |
| **跟随式** | 主体运动 + 镜头同速跟随 | 奔跑、骑行、追逐 | 稳定器跟拍 |

完整结构公式 + 实战 prompt + 常见误用 → [13-templates.md](13-templates.md)「Prompt 组合模式库」

---

## 常见翻车 & 修复

| 翻车 | 为什么 | 怎么修 |
|------|--------|--------|
| 面部变形 | 近景 + 快速运动 | 拉远镜头或减速 |
| 产品/logo 变了 | 没在 prompt 里显式保护 | 开头写"保持[特征]完全不变" |
| 动作和声音错位 | 没写时间锚点 | 用 `[Xs]` 标记对齐 |
| 画面像壁纸 | 没有运动也没有变化 | 加一个缓慢镜头运动 + 一个自然变化 |
| 文字乱码 | 模型不擅长渲染文字 | 加"无文字"约束，后期加 |
| 续写跳变 | 没重复身份约束 | 每次续写重复身份 + 光线 + 镜头 |

完整诊断矩阵（5 类 23 条）→ [18-troubleshooting-gallery.md](18-troubleshooting-gallery.md)

---

## 项目结构

```
kling-prompt-engineering/
├── README.md                          # 你正在看的这个
├── QUICK-REF.md                       # 一页纸速查
├── CHECKLIST.md                       # 提交前检查清单
├── CHALLENGES.md                      # 10 个提示词挑战
├── 01-directing-engine.md             # 导演引擎
├── 02-shot-language.md                # 镜头语言
├── 03-t2v-guide.md                    # 文生视频
├── 04-i2v-guide.md                    # 图生视频
├── 05-multi-image-omni.md             # 多图参考
├── 06-video-extension.md              # 视频续写
├── 07-motion-transfer.md              # 动作迁移
├── 08-audio-guide.md                  # 音频指南
├── 09-anti-slop.md                    # 反空话词典
├── 10-allocation-model.md             # 算力分配
├── 11-genre-guides.md                 # 类型片指南
├── 12-kling-capability-map.md         # 可灵能力地图
├── 13-templates.md                    # 即用模板 + 组合模式库
├── 14-model-mechanics.md              # 模型机制
├── 15-timeline-syntax.md              # 时间轴语法
├── 16-language-strategy.md            # 中英文混合策略
├── 17-user-journey.md                 # 用户分层路径
├── 18-troubleshooting-gallery.md      # 故障诊断
├── 19-cinematography-dictionary.md    # 摄影术语词典
├── 20-style-tags.md                   # 风格标签
├── 21-retake-protocol.md              # 重试协议
├── 22-text-to-image.md                # 文生图
├── 23-first-last-frame.md             # 首帧/尾帧指南
├── references/                        # 参考资料
│   ├── anti_slop_lexicon.md
│   ├── failure_atlas.md
│   └── negative_prompt_library.md
├── examples/                          # 实战案例
│   ├── 01-emotion-closeup.md
│   ├── 02-product-showcase.md
│   ├── 03-city-nightscape.md
│   ├── 04-food-closeup.md
│   └── 05-action-scene.md
├── adapters/                          # 模型适配器
│   ├── kling_adapter.yaml
│   ├── seedance_adapter.yaml
│   ├── t2i_adapter.yaml               # 文生图多模型适配
│   ├── prompt_translator.yaml
│   └── model_router.yaml
├── workflows/                         # 工作流
│   └── storyboard-to-prompt.md        # 分镜转 Prompt
├── skills/                            # Skill 文件
│   └── *.skill
└── scripts/                           # 验证脚本
    └── *.py
```

---

## 原创内容与致谢

说清楚哪些是搬来的，哪些是自己写的。

**移植自 [seedance-2.0 Skill OS](https://github.com/Emily2040/seedance-2.0)：** 导演引擎的基础框架（导演五问 + 三个补充字段 + 一致性原则 + 节拍编排）、魔法前缀的思路、"描述可检测的物理现象"这条核心原则、源素材承载状态规则（I2V）、叙事/非叙事分道、重试协议、Prompt 压缩优先级。这些是整个项目的地基。

**本项目原创的：**
- 预算分配模型（身份保真 / 动作幅度 / 场景密度的三角交易）
- 音画三层模型（环境音层 / 动作音效层 / 情绪音乐层）
- 时间轴语法（状态层 + 运动层 + 节奏层）
- 5 种组合模式（定锚式 / 递进式 / 对比式 / 揭示式 / 跟随式）
- Anti-Slop 中文适配（中文空话陷阱、中文替换表）
- 故障诊断矩阵（5 类 23 条）
- 用户分层路径（入门 / 进阶 / 专业三层）
- 中英文混合策略
- 10 个音画场景示例
- 多模型适配器（adapters/）——把同一套方法论翻译给不同模型消费

**致谢：** 感谢 seedance-2.0 Skill OS 的作者提供了扎实的方法论基础。没有那个项目，这个项目不会存在。

MIT License — 随便用，注明出处就行。

---

<p align="center">
  <i>导演模型，而非微调画面。</i>
</p>
