# GitHub AI 视频提示词工程深度调研报告

> 调研时间：2026-07-21
> 目标：找到高价值改进方向，提升 kling-prompt-engineering 项目竞争力

---

## 一、高价值竞品项目

### Tier 1：已验证的方法论（100+⭐）

| 项目 | Stars | 核心价值 | 值得学的 |
|------|-------|---------|---------|
| **jnMetaCode/ai-shortfilm-prompts** | 241 | 好莱坞导演PJ Ace认证的AI短片方法论 | "单行魔法提示词"、真实摄影机+镜头语言锚定、失败→修复案例库、Claude Code Skill集成 |
| **LeoYeAI/seedance-skills** | 14 | 28个模块化Agent Skill、6语言支持 | 领域技能拆分（camera/motion/lighting/characters/style/vfx）、反废话过滤、版权安全重写 |

### Tier 2：完整工作流平台（20-50⭐）

| 项目 | Stars | 核心价值 | 值得学的 |
|------|-------|---------|---------|
| **yfge/ai-video-studio** | 32 | Timeline-first的AI短剧生产平台 | 虚拟IP管理、时间线为单一事实源(SSOT)、harness测试、资产追踪 |
| **JohnKeating1997/spark-video** | 29 | premise→screenplay→storyboard→render→mp4 | 完整的从想法到成片的流程、人物/场景/道具一致性、中英双语 |
| **kaigani/codeywood** | 28 | Claude Code技能驱动的AI影视制作 | 基于参考图的一致性（非LoRA）、模块化技能架构、质量门控 |
| **LudwigKienle/ai-video-production-editor** | 21 | 开源AI视频制作编辑器(React+Electron) | 节点式管线、连续性审查、重拍队列、时间线编辑 |
| **ai9app/AI-Cinematic-Prompt-Director** | 15 | 250项电影摄影知识库 | 逐场景提示词矩阵、专业摄影术语词典 |

### Tier 3：值得关注的工具

| 项目 | Stars | 核心价值 |
|------|-------|---------|
| **rmarji/get-shit-done** | 1 | 版本化Bible、运动优先的shotlist、联系表概念 |
| **sschepis/martin** | 1 | NPM包形式的媒体导演、适配器模式支持多引擎 |

---

## 二、关键发现

### 发现1："单行魔法提示词"比长篇大论更有效

来自 ai-shortfilm-prompts（241⭐）的核心洞察：

```
❌ 大多数人写的：
"Epic cinematic shot of a beautiful female mech warrior activating 
a stunning energy shield in the rain. Highly detailed, 4K"

✅ 方法论写的：
"Anamorphic widescreen cinematic. Simulated IMAX film camera + 
Panavision C-series lens (35mm focal, f/4 aperture). Handheld shot 
— extremely subtle, breath-like camera float throughout. 
{{your scene description}}. No score. Production audio only."
```

**为什么有效：** 真实摄影机型号 + "呼吸感微浮动" 把AI锚定到真实的电影美学，而不是模糊的"电影感"关键词。

**可灵改进：** 在01-directing-engine.md里加一个"魔法前缀"系统——用户可以直接复制的、经过验证的提示词开头模板。

### 发现2：模块化技能拆分 > 单一大文档

来自 seedance-skills 的架构：

```
核心工作流：interview → sequence → continuation → prompt
领域技能：camera / motion / lighting / characters / style / vfx / audio
安全质量：copyright / antislop / filter
多语言词汇：zh / ja / ko / es / ru / en
```

**可灵改进：** 不需要拆成28个文件（你的项目是文档不是工具），但可以在README里加一个"按场景索引"的快速查找表。

### 发现3：版本化创意决策

来自 get-shit-done 的"版本化Bible"概念：

```
bible_v001.yaml → 第一版创意约束
bible_v002.yaml → 迭代后的约束
```

每次迭代不丢失之前的工作。

**可灵改进：** 在13-templates.md里加"提示词迭代模板"——教用户如何系统性地修改和版本管理提示词。

### 发现4：失败→修复案例库是最实用的内容

来自 ai-shortfilm-prompts 的 cases.md：

```
❌ 失败的提示词 → 问题分析 → ✅ 修复后的提示词
```

**可灵改进：** 创建一个 "troubleshooting-gallery.md"，收录常见失败模式和修复方法。

### 发现5：基于参考图的一致性 > 提示词描述一致性

来自 codeywood 的关键洞察：

```
故事 → 人物/场景定义 → 参考图库 → 镜头图片 → 视频
每个阶段用前一个阶段的输出作为参考输入
```

**可灵改进：** 在04-i2v-guide.md里强化"参考图工作流"——不是单张图生视频，而是建立参考图库再逐镜头生成。

### 发现6：250项电影摄影术语词典

来自 AI-Cinematic-Prompt-Director：

```
Camera Movements: FPV Tracking, Dolly Zoom, Crane Shot...
Shot Types: Extreme Close-Up, Dutch Angle, Over-the-Shoulder...
Lighting: Volumetric Lighting, Chiaroscuro, Golden Hour...
VFX: Anamorphic lens flare, Film grain, Lens whacking...
```

**可灵改进：** 创建 "17-cinematography-dictionary.md"——可灵可用的电影摄影术语速查表。

---

## 三、改进优先级（重新排序）

| 优先级 | 改进项 | 来源 | 工作量 | 价值 | 落地位置 |
|--------|--------|------|--------|------|---------|
| **P0** | 魔法前缀系统 | ai-shortfilm-prompts | 低 | 极高 | 01-directing-engine.md 新增§ |
| **P0** | 类型模板扩展(6→15) | ai-shortfilm-prompts | 中 | 高 | 11-genre-guides.md 扩展 |
| **P0** | 引导式构建模式 | seedance-skills | 低 | 高 | 01-directing-engine.md 新增§ |
| **P1** | 失败→修复案例库 | ai-shortfilm-prompts | 中 | 极高 | 新建 troubleshooting-gallery.md |
| **P1** | 电影摄影术语词典 | AI-Cinematic-Prompt-Director | 中 | 高 | 新建 17-cinematography-dictionary.md |
| **P1** | FPV/无人机场景 | ai9app | 低 | 中 | 02-shot-language.md 新增§ |
| **P2** | 提示词迭代模板 | get-shit-done | 低 | 中 | 13-templates.md 新增§ |
| **P2** | 参考图工作流强化 | codeywood | 中 | 中 | 04-i2v-guide.md 强化 |
| **P2** | 按场景快速索引 | seedance-skills | 低 | 中 | README.md 新增 |
| ❌ | Eval评估框架 | yfge | 高 | 低 | 不做（文档项目不适合） |
| ❌ | @-mention语法 | - | 低 | 低 | 不做（可灵不支持） |
| ❌ | 企业级工作流 | cclank | 高 | 低 | 不做（scope外） |

---

## 四、已落地的改进（本次）

1. ✅ 11-genre-guides.md：6种 → 15种类型
2. ✅ 01-directing-engine.md：新增"引导式构建模式"
3. ✅ 02-shot-language.md：新增FPV/无人机场景

## 五、建议下一步

1. 创建 troubleshooting-gallery.md（失败→修复案例库）
2. 创建 17-cinematography-dictionary.md（电影摄影术语词典）
3. 在01-directing-engine.md里加"魔法前缀"系统

---

*调研数据来源：GitHub搜索、AnySearch、直接仓库访问*
