# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased - 第三批] - legacy 技能迁完 + lint 中文词表补齐 + 自动优化立项

### Added
- 剩余 13 个 legacy .skill 全部迁移为标准技能目录（anti-slop、cost-estimator、keyframe-generator、material-numbering、motion-director、multi-platform、multilingual-vocabulary、quality-scorer、retake-protocol、routing-table、timeline-format、validation-scripts、visual-pipeline）：SKILL.md 为 Workflow + Gotchas + 与现行脚本/数据的分工说明，完整旧版数据进 `references/data.yaml`，配 `references/sections.md` 章节行号索引。标准技能目录至此共 20 个，无待迁移项
- `experiments/` — DSPy 式自动优化立项：README 写明启动门槛（≥30 条同评分者的真实成片评分 + 一次有意义的基线对比 + 窄优化目标），`variant_eval.py` 变体实验脚手架（prompt_lint 排序，只对 prompt 层成立）+ 示例变体

### Fixed
- `scripts/prompt_lint.py` 中文弱词漏检：SLOP_TABLE 此前只有英文，`find_slop` 的 `\b` 边界对中文也不适用，导致中文空话词（词目见 lint 词表）整批漏检、空话 prompt 得 85 分过检。补 17 个中文弱词（依据 09-anti-slop.md 与 anti_slop_lexicon 的既有禁用表）并让 CJK 词走子串匹配；同例空话 prompt 现为 0 分，KPE 写法回归测试仍 100 分

## [Unreleased - 第二批] - adapters 可执行 + 风格库数据化 + 成片评测层

### Added
- `scripts/adapt_prompt.py` — adapters 可执行化：分镜 JSON + model_facts 硬限制 → 分模型生成计划（multi_prompt/逐镜模式、统一请求预览），不支持与超限项显式进 warnings/errors 不静默丢弃
- `adapters/model_facts.yaml` 升 1.1.0：新增 Kling 4.0 条目（2026-10-16 全球开放，3–30s、最多 10 关键帧、Omni Reference 合计 15 素材、立体声；4K/HDR 为 coming soon 已标注），Seedance 2.5 补 fal 渠道状态（480p/720p、参考上限 50 文件）
- `scripts/validate_storyboard.py --otio` — 分镜导出 OpenTimelineIO 时间线（11 维与 prompt 哈希进 metadata.kpe），接剪辑/ffmpeg 合成阶段
- `data/styles.json` + `scripts/build_style_index.py` + `scripts/search_styles.py` — 24 号风格库 156 条数据化，md 为源、JSON 为派生索引，CI 校验同步；agent 按条检索不再整篇加载
- `evals/video-rubric.md` + `evals/score_video.py` + `evals/video-scores.example.jsonl` — 成片评测层：VideoScore 五维 + 角色一致/音画同步共七维（1–4 分），聚合、存基线、回退超 0.3 报警
- `scripts/retake_report.py` — 重拍日志聚合：失败归类计数、同类 ≥3 次或修法验证 ≥2 次产出 failure-atlas 候选草稿（仍须人工过）

### Changed
- `install.sh` 随装脚本扩充（adapt_prompt / build_style_index / search_styles / retake_report）
- CI 新增适配冒烟、风格索引同步、成片评分与重拍聚合冒烟四步

## [Unreleased] - 技能渐进加载 + 模型事实单一数据源 + 分镜结构化

### Added
- `adapters/model_facts.yaml` — 模型硬事实单一数据源（分型号时长/分辨率/参考上限/多镜头，带 verified_at 和渠道口径说明）
- `scripts/check_model_facts.py` — 口径漂移检查，已接入 CI
- `schemas/storyboard.schema.json` — 分镜结构化格式（11 维 + 角色卡 + 风格 token + prompt_text 双份交付）
- `scripts/validate_storyboard.py` — 分镜校验（总时长、相邻景别、角色卡逐字一致、风格 token、引用完整性），可输出 manifest 片段
- `examples/storyboard-example.json` — 可通过校验的分镜示例
- `workflows/retake-log-template.md` + `templates/retake-log.example.jsonl` — 重拍日志字段与单变量纪律
- 4 个技能补 `references/`：各技能的完整旧版数据以 `references/data.yaml` 入内，并配速查 md（domains / formats / four-act-and-sequence-state / quick-diagnosis + diagnosis-examples）

### Changed
- 4 个新 SKILL.md（kling-screenwriting、domain-skills、multi-episode-narrative、failure-atlas）从指针式薄文件改成渐进加载结构：正文留 Workflow + Gotchas + 何时读 references，版本升到 1.1.0
- `install.sh` 重写：安装标准技能目录（整目录含 references），本地克隆优先、否则浅克隆；不再逐个下载 legacy `.skill` 文件
- `adapters/kling_adapter.yaml`：全系上限对齐 model_facts（15s），黄金公式换成 CLAUDE.md 新公式，视频输入按型号说明
- `12-kling-capability-map.md` 规格表更新到 model_facts 口径（v3 最高 4K/3-15s、补 Omni/O1/2.6 Pro 行、v2.5-turbo 15s 标注为渠道口径）
- `adapters/prompt_translator.yaml`：runway/sora/pika 三节标注 draft_unverified 草案，与 router 的 planned 状态对齐
- 根 `SKILL.md` Model Gate、`workflows/storyboard-to-prompt.md`、`skills/kling-storyboard`、`CLAUDE.md` 补单一数据源与结构化交付的指针
- CI（validate.yml）新增两步：check_model_facts、validate_storyboard 示例

### Notes
- 本批改动只在本地工作副本，未推送 GitHub（推送 403 问题未解决，见仓库外记录）。

## [Unreleased - 第一批] - kpe 第一批 skill 迁移 + 数字口径对齐

### Added
- `skills/kling-screenwriting/SKILL.md` — 从 archive 旧版迁移，分镜级剧本入口
- `skills/domain-skills/SKILL.md` — 15 个行业方向入口
- `skills/multi-episode-narrative/SKILL.md` — 尾帧衔接与多集连续叙事入口
- `skills/failure-atlas/SKILL.md` — 8 类失败诊断入口

### Fixed
- README 编号文档数 26 → 28（01–24，其中 22 章拆为 22 + 22a–22d）
- `skills/README.md` 改成全量对照表，根目录待迁移由笼统的 17 个改为可核对的 13 个
- 删除根目录重复的 `generate_docx.py`，只保留 `scripts/generate_docx.py`

### Notes
- 旧 `.skill` 文件暂保留作为数据参考，未删除，避免破坏现有引用和校验；后续迁移按 skills/README.md 的表逐个推进。
- 风格库 156 条已实测核对（106 风格 + 50 氛围），与 README 一致，不用改。


## [3.1.3] - 引擎工具链补全 + Anti-Slop 误报修复

### Added
- `scripts/t2i_generate.py` — 文生图提示词生成器：创意意图 → Kolors/Qwen/Seedream 三模型 prompt（读 adapters/t2i_adapter.yaml 翻译规则，缺要素提示不编造）

### Changed
- `scripts/prompt_lint.py` 新增 `--mode t2i` 文生图检查模式：景别/角度骨架、相机锚定（真实相机型号）、负面提示词；视频特有检查（声音/动作密度）仅 T2V 模式执行

### Fixed
- `scripts/validate_all.py` 教学豁免大幅增强——全量验证从 79.2% 提升到 100%
  - 新增豁免：引用块（`>` 开头）、❌/✅ 示例行、自检清单（`- [ ]`）
  - 否定/批评指令扩展（不能用/不能写/没写/不是/空洞/删掉…）
  - 比较句（比 X 有效）、讨论句（X 是什么?模型不知道）
  - 括号注释（含中文全角括号）、中文弯引号包裹
  - 专业术语搭配（cinematic color grading / lighting 等）
  - 教学代码块检测：块内 ❌/✅/Before 标记 + 代码块上方 `### Before` 标题
  - 引用来源（来自/引用/参考自）、加粗短语（**X**）

## [3.1.2] - 验证脚本重写

### Fixed
- `scripts/validate_all.py` 重写：新增 .md 验证 6 项检查（末尾空行/标题跳级/代码块闭合/表格格式/交叉引用断链/Anti-Slop 违规）
- 支持 `--skill-only` / `--md-only` / 单文件模式
- 修复 6 处断链（research 报告 3 处、storyboard 工作流 3 处）

## [3.1.1] - 全面细节审查

### Fixed
- QUICK-REF.md：导演五问补三个加固字段、组合模式表同步、新增首尾帧速查 + 多模型适配速查
- README.md：文件数 25→26、组合模式速览表同步、项目结构树补全
- CHECKLIST.md：新增首尾帧检查 4 项 + 文生图检查 4 项
- CHALLENGES.md / 06-video-extension.md 细节同步

## [3.1.0] - 首帧/尾帧专章

### Added
- `23-first-last-frame.md` — 首尾帧完整指南：状态插值逻辑、好首帧 5 标准、好尾帧 4 标准、配对原则、T2I 生成首帧 6 步流程、多镜头帧链式串联、5 类翻车修复、3 个实战案例
- `adapters/t2i_adapter.yaml` — 文生图多模型适配器（Kolors / Qwen Image 3 Pro / Seedream 5.0）
- `workflows/storyboard-to-prompt.md` — 分镜转 Prompt 工作流

## [3.0.0] - 10 轮迭代改进

### Added
- `22-text-to-image.md` — 文生图完整指南（相机锚定/景深/曝光/布光/风格体系/负面提示词）
- `QUICK-REF.md` — 一页纸速查
- `CHECKLIST.md` — 提交前检查清单
- `CHALLENGES.md` — 10 个提示词挑战（⭐ 到 ⭐⭐⭐）
- `examples/` — 5 个完整实战案例 + before_after 对比
- `scripts/prompt_lint.py` — 提示词质量检查 CLI
- `.github/` — CI + issue/PR 模板

## [2.5.0] - Production Ready

### Added
- `CLAUDE.md` — 项目规范文件
- `install.sh` — 一键安装脚本（支持 Claude Code / Cursor / Codex / Windsurf / Trae / Qwen Code）
- `scripts/validate_all.py` — 综合验证脚本
- `scripts/validate_yaml.py` — YAML 格式验证
- `scripts/validate_required_fields.py` — 必需字段验证
- `scripts/validate_vocab_coverage.py` — 词汇覆盖验证
- `scripts/validate_naming_convention.py` — 命名规范验证
- `scripts/validate_version.py` — 版本号验证

## [2.4.0] - Multilingual & Validation

### Added
- `skills/multilingual-vocabulary.skill` — 6 种语言的原生电影词汇（zh/en/ja/ko/es/ru）
- `skills/validation-scripts.skill` — 自动化测试和验证
- `skills/multi-platform.skill` — 支持 15+ 平台安装兼容

## [2.3.0] - Routing & Diagnostics

### Added
- `skills/routing-table.skill` — 智能分流系统
- `skills/failure-atlas.skill` — 系统性诊断和修复
- `skills/material-numbering.skill` — 标准化素材管理（C01-C99 / S01-S99 / P01-P99）

## [2.2.0] - Domain Skills & Quality Governance

### Added
- `skills/domain-skills.skill` — 15 个行业专业 Skill 模板
- `skills/multi-episode-narrative.skill` — 尾帧衔接 + 视频延长
- `skills/anti-slop.skill` — 弱词替换表

### 15 个领域覆盖
- 创意风格：电影风格、3D CGI、卡通动画、漫画转视频、打斗场景、动漫
- 商业营销：动态设计广告、电商广告、产品 360°、社交钩子、品牌故事
- 行业专项：音乐视频、时尚型录、美食饮品、房地产

## [2.1.0] - Director Engine & Timeline Format

### Added
- `skills/director-engine.skill` — 从意图推导到技术执行
- `skills/timeline-format.skill` — 用时间轴替代 JSON

### Changed
- 核心升级：从"提示词词典"升级为"Skill OS"
- 黄金公式更新：[场景意图/戏剧功能] + [一个可见节拍] + [一个镜头运动] + [真实光源] + [参考角色绑定]

## [2.0.0] - Model Router & Multi-Model Support

### Added
- `adapters/model_router.yaml` — 模型路由层配置
- `adapters/kling_adapter.yaml` — Kling 模型适配器
- `adapters/seedance_adapter.yaml` — Seedance 模型适配器
- `adapters/base_adapter.yaml` — 基础适配器接口
- `adapters/prompt_translator.yaml` — 多语言提示词翻译器
- `examples/model_routing_examples.yaml` — 5 个完整使用示例

## [1.2.0] - Deep Optimization (GitHub Research)

### Added
- Magic Prefix System (魔法前缀) — from ai-shortfilm-prompts (241⭐)
- Guided Construction Mode (引导式构建) — from seedance-skills
- FPV/Drone Scenarios — from ai9app
- Genre Expansion 8→15 类型扩展
- `18-troubleshooting-gallery.md` — 故障排除案例库
- `19-cinematography-dictionary.md` — 电影摄影术语词典

## [1.1.0] - New Additions

### Added
- Beat Direction (节拍编排) — from HyperFrames
- Composition Density (构图密度) — from HyperFrames
- Multi-Modal Reference Formula — from Seedance 2.0
- Video Editing Operations — from Seedance 2.0
- Video Extension Formulas — from Seedance 2.0
- Portrait Consistency Strategy — from Seedance Studio

## [1.0.0] - Initial Release

### Added
- Core documentation (01-14)
- Director Engine methodology
- Shot Language reference
- Anti-Slop lexicon
- Budget Allocation model
- Ready-to-use templates
