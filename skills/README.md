# skills/ 目录说明

这个目录里有两种格式的文件，它们的关系是：

**`*/SKILL.md`（主路径）** — 标准 Claude Code / Cursor 格式。AI 工具原生加载的就是这些。每个子目录是一个独立 skill。

**`*.skill`（legacy 数据参考）** — 项目早期的自定义 YAML 格式。内容仍然有效，但格式不被任何 AI 工具原生消费。保留是因为部分文件包含 SKILL.md 尚未覆盖的详细数据（如 domain-skills 的 15 个行业参数、multilingual-vocabulary 的 6 语言词汇表）。

## 迁移状态（全量对照，2026-10-28 核查）

标准目录已有 7 个：kling-templates、kling-style-tags、kling-storyboard、kling-screenwriting、domain-skills、multi-episode-narrative、failure-atlas。

全部 20 个标准技能目录已在 2026-10-30 迁完并补完渐进加载：SKILL.md 正文是 Workflow + Gotchas，详细数据拆进各自 `references/`（`data.yaml` 是旧版完整数据，第一批四个另配速查 md，第三批十三个配 `sections.md` 章节索引），不再用正文指针指向目录外的 legacy 文件。新技能一律按这个结构做，不要再产出只有三十行的指针文件。

| .skill 文件 | 位置 | 状态 |
|---|---|---|
| kling-templates.skill | archive/ | ✅ 已迁移，见 skills/kling-templates/SKILL.md |
| kling-style-tags.skill | archive/ | ✅ 已迁移，见 skills/kling-style-tags/SKILL.md |
| kling-storyboard.skill | 根目录 | ✅ 已迁移，见 skills/kling-storyboard/SKILL.md |
| kling-screenwriting.skill | archive/ | ✅ 已迁移，见 skills/kling-screenwriting/SKILL.md |
| domain-skills.skill | 根目录 | ✅ 已迁移，见 skills/domain-skills/SKILL.md |
| multi-episode-narrative.skill | 根目录 | ✅ 已迁移，见 skills/multi-episode-narrative/SKILL.md |
| failure-atlas.skill | 根目录 | ✅ 已迁移，见 skills/failure-atlas/SKILL.md |
| director-engine.skill | 根目录 | 被根 SKILL.md 替代，不再作为独立 skill 加载 |
| kling-director.skill | archive/ | 已废弃（deprecated），不要再用 |
| anti-slop.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| cost-estimator.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| keyframe-generator.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| material-numbering.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| motion-director.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| multi-platform.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| multilingual-vocabulary.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| quality-scorer.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| retake-protocol.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| routing-table.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| timeline-format.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| validation-scripts.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |
| visual-pipeline.skill | 根目录 | ✅ 已迁移（第三批，2026-10-30） |

根目录 .skill 共 18 个：已迁移 17 个（第一批 4 个在 skills/README 上文，第二批补完渐进加载，第三批 2026-10-30 迁完剩余 13 个），director-engine 被根 SKILL.md 替代、不独立加载。至此无待迁移项；.skill 文件保留为数据参考，各技能的完整旧版数据已复制进对应技能目录的 references/data.yaml。

## 给贡献者

- 新 skill 一律用 `skills/skill-name/SKILL.md` 格式
- 不要再新增 `.skill` 文件
- 迁移旧文件时：核心逻辑写入 SKILL.md（Workflow + Gotchas），详细数据放同目录 `references/`（完整数据存 `references/data.yaml`，再配一份速查 md），并在本表更新状态；不要在 SKILL.md 里写指向目录外 legacy 文件的指针
- 格式规范见根目录 `SKILL_SCHEMA.md`（针对 .skill），SKILL.md 格式参照已迁移的 kling-templates/SKILL.md（frontmatter + Workflow + 规则）
