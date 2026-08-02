# skills/ 目录说明

这个目录里有两种格式的文件，它们的关系是：

**`*/SKILL.md`（主路径）** — 标准 Claude Code / Cursor 格式。AI 工具原生加载的就是这些。每个子目录是一个独立 skill。

**`*.skill`（legacy 数据参考）** — 项目早期的自定义 YAML 格式。内容仍然有效，但格式不被任何 AI 工具原生消费。保留是因为部分文件包含 SKILL.md 尚未覆盖的详细数据（如 domain-skills 的 15 个行业参数、multilingual-vocabulary 的 6 语言词汇表）。

## 迁移状态

| 子目录 SKILL.md | 对应 .skill | 状态 |
|----------------|------------|------|
| `kling-templates/` | `kling-templates.skill` | ✅ 已迁移 |
| `kling-style-tags/` | `kling-style-tags.skill` | ✅ 已迁移 |
| `kling-storyboard/` | `kling-storyboard.skill` | ✅ 已迁移 |
| — | `director-engine.skill` | 被根 SKILL.md 替代 |
| — | `kling-director.skill` | 已废弃（deprecated） |
| — | 其余 17 个 .skill | 待迁移（数据仍有效） |

## 给贡献者

- 新 skill 一律用 `skills/skill-name/SKILL.md` 格式
- 不要再新增 `.skill` 文件
- 迁移旧文件时：提取核心逻辑写入 SKILL.md，详细数据可保留为同目录下的 `.yaml` 参考文件
- 格式规范见根目录 `SKILL_SCHEMA.md`
