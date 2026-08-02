# 贡献指南 / Contributing Guide

欢迎加入可灵提示词工程项目！我们相信优秀的提示词是"导演思维 + 工程结构"的结合——每一条提示词都应像分镜脚本一样精确、可复现、可迭代。我们期待你分享经过验证的模板与技巧，让社区共同构建最完整的可灵 AI 创作知识库。

Welcome to the Kling Prompt Engineering project! We believe great prompts combine "director thinking + engineering structure" — every prompt should be as precise, reproducible, and iterable as a storyboard. We look forward to your verified templates and techniques.

---

## 如何贡献 / How to Contribute

### 提交新的提示词模板 / Submitting a New Prompt Template

1. **Fork** 本仓库到你的 GitHub 账号
2. 将模板添加到 `templates/` 目录（通用模板）或 `skills/` 目录（领域技能）
3. 运行验证脚本确保格式正确：
   ```bash
   python scripts/validate_all.py skills/
   ```
4. 运行提示词检查确保无 slop 词汇：
   ```bash
   python scripts/prompt_lint.py "your prompt text here"
   ```
5. 提交 **Pull Request**，填写 PR 模板中的验证清单

### 提交 Bug 修复或改进 / Submitting a Bug Fix or Improvement

1. Fork → 创建分支（如 `fix/typo-in-t2v-guide`）
2. 修改相关文件
3. 确保改动不破坏现有验证：`python scripts/validate_all.py skills/`
4. 提交 PR，说明改动原因与影响范围

### 添加新的领域技能 / Adding a New Genre/Domain Skill

1. 在 `skills/` 下创建目录：`skills/your-skill-name/`
2. 编写 `SKILL.md` 文件（格式见下方）
3. 运行验证：`python scripts/validate_all.py skills/`
4. 如有配套示例，放入 `examples/` 目录
5. 提交 PR

---

## 技能文件格式 / Skill File Format

### 标准格式（推荐）/ Standard Format (Preferred)

路径：`skills/skill-name/SKILL.md`

文件必须包含 YAML frontmatter：

```markdown
---
name: skill-name
description: 一句话描述该技能的用途与触发场景
version: 1.0.0
---

# 技能标题

## Steps
1. ...

## Pitfalls
- ...

## Verification
...
```

**必填 frontmatter 字段 / Required frontmatter fields:**

| 字段 | 说明 |
|------|------|
| `name` | 技能名称，与目录名一致（小写 + 连字符） |
| `description` | 一句话描述，说明做什么、何时使用 |
| `version` | 语义化版本号（semver），如 `1.0.0` |

### 旧版格式 / Legacy Format

`.skill` YAML 文件仍然被接受，但新贡献请优先使用 `SKILL.md` 格式。旧格式文件将在后续版本中逐步迁移。

Legacy `.skill` YAML files are still accepted, but new contributions should prefer the `SKILL.md` format. Legacy files will be migrated in future versions.

---

## 验证 / Validation

所有 PR 必须通过以下检查：

```bash
# 技能文件结构验证
python scripts/validate_all.py skills/

# 提示词质量检查（不应有 error 级别问题）
python scripts/prompt_lint.py "your prompt"
```

---

## 提交信息规范 / Commit Message Convention

使用以下前缀：

| 前缀 | 用途 |
|------|------|
| `feat:` | 新增模板、技能或功能 |
| `fix:` | 修复错误、修正提示词 |
| `docs:` | 文档更新（README、指南等） |
| `refactor:` | 重构、格式调整（不改变功能） |

示例：
```
feat: add cyberpunk cityscape T2V template
fix: correct camera movement syntax in i2v guide
docs: update README with new skill index
refactor: reorganize genre guides into subdirectories
```

---

## 行为准则 / Code of Conduct

- **友善交流**：尊重每一位贡献者，建设性地讨论问题
- **注明出处**：引用他人提示词或创意时，标注原始来源
- **Be kind**: Respect every contributor; discuss issues constructively
- **Credit sources**: Always attribute original authors when referencing others' prompts or ideas

---

感谢你的贡献！/ Thank you for contributing!
