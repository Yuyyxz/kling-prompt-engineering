# CLAUDE.md — 项目规范（给 AI 助手看的）

你正在一个 AI 视频提示词工程项目里工作。方法论和 Skill 逻辑全在根目录 `SKILL.md`，别在这里重复它。这个文件只管"怎么编辑这个项目"。

## 项目是什么

给可灵和 Seedance 用户准备的导演式提示词工具集。不是词典，是工作方法。用户说一句话想法，AI 给出可以直接粘进生成器的提示词。

## 编辑规则

- 改方法论/流程 → 改 `SKILL.md`，这里是 single source of truth
- 改模型参数/能力 → 改 `12-kling-capability-map.md`，数据必须来自官方文档，别凭记忆写
- 改 Skill → 改 `skills/*/SKILL.md`（标准格式），别改 `.skill` 文件（legacy）
- 改提示词模板 → 改 `skills/kling-templates/SKILL.md` 或 `13-templates.md`
- 加新文档 → 编号递增，放根目录，更新 README 文档索引

## 写作风格

- 像一个每天用可灵出片的人在写笔记，不像产品经理在写规格书
- 不用 emoji 做标题
- 不用"核心理念"、"赋能"、"系统性"、"全方位"这类词
- 有观点就说，不确定就标"未验证"
- 中文为主，技术术语保留英文（T2V、I2V、Anti-Slop）

## 验证

改完跑：
```bash
python scripts/validate_all.py skills/
python scripts/prompt_lint.py "你写的示例提示词"
```

## 禁止

- 不要在提示词示例里用 cinematic / beautiful / 4k / epic / masterpiece
- 不要在文档里写未经验证的模型参数
- 不要新增 `.skill` 格式文件
- 不要在没有数据来源的情况下写"支持 XX 功能"

## 文件地图

| 要找什么 | 去哪 |
|---------|------|
| 方法论/流程/路由 | `SKILL.md` |
| 模型参数/能力 | `12-kling-capability-map.md` |
| Seedance 提示词写法 | `references/seedance-prompt-guide.md` |
| Anti-Slop 替换表 | `09-anti-slop.md` |
| 模板库 | `skills/kling-templates/SKILL.md` |
| 风格标签 | `skills/kling-style-tags/SKILL.md` |
| 分镜表格式 | `skills/kling-storyboard/SKILL.md` |
| 验证脚本 | `scripts/validate_all.py` |
| 提示词检查 | `scripts/prompt_lint.py` |
| 评测 | `evals/run_evals.py` |
| 版本历史 | `CHANGELOG.md` |
| 贡献指南 | `CONTRIBUTING.md` |
