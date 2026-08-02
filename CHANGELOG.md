# Changelog

All notable changes to this project will be documented in this file.

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
