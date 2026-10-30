---
name: validation-scripts
description: "验证体系说明。KPE 的技能、prompt、分镜、模型事实各由什么脚本验证、验证什么。改完技能或文档要自检、CI 挂了要定位时用。"
version: "1.1.0"
---

# validation-scripts — 验证体系

先说清分工：本技能是验证体系的说明书，真正跑的是 `scripts/` 里的脚本和 CI（`.github/workflows/validate.yml`）。改说明书不等于改验证，验证口径变了要改脚本，并在这里同步记录。

现行验证清单：

- `scripts/validate_all.py` — 技能与文档的结构校验（frontmatter、引用、计数口径）
- `scripts/prompt_lint.py` — prompt 空话与硬项门禁
- `scripts/check_model_facts.py` — 模型事实口径漂移（适配器、capability-map、translator 与 model_facts 对齐）
- `scripts/validate_storyboard.py` — 分镜 JSON 校验与 manifest/OTIO 导出
- `scripts/build_style_index.py --check` — 风格索引与 24 号文档同步
- `evals/score_video.py` — 成片评分聚合与基线回归

## 何时读 references

验证类型与报告模板在 `references/data.yaml` 的 `validation_types`、`validation_report_template`，先看 `references/sections.md` 定位。data.yaml 里的脚本清单是旧版，与现行 scripts/ 对不上时以 scripts/ 和 CI 为准，并回头修正 data.yaml 的记录。

## Workflow

1. 改了什么就跑对应脚本，不要只跑 validate_all 蒙混：改模型数据跑 check_model_facts，改分镜跑 validate_storyboard，改 24 号文档跑 build_style_index --check。
2. 提交前本地跑一遍 CI 的全套步骤，红了先定位是哪一层：结构、口径、还是内容。
3. 新增一类产物就给它配一个验证：能机器查的不要靠人眼清单，这是这个仓库一路过来的规矩。
4. 验证失败先看脚本报的具体项，不要为了过检去改脚本的检查项；确属检查项过期，改完在 CHANGELOG 里写明。

## Gotchas

validate_all 全绿不等于内容对。它查结构和口径，不查事实；模型规格这类事实靠 model_facts 的 verified_at 纪律和人工复核。

本地绿、CI 红通常是依赖差异（pyyaml 之类）或路径问题，先对环境再怀疑内容。

## 规则

- 验证脚本只许依赖标准库加 pyyaml，新依赖先进 CI 验证再落地。
- 每个脚本的退出码要有意义：0 通过、非 0 失败，CI 靠这个判断，不许只打印不返回。
