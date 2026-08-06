# Changelog

All notable changes to this project will be documented in this file.

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
