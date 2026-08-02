# .skill 文件格式规范

本文档定义了 `skills/` 目录下 `.skill` 文件的标准格式。

## 格式要求

每个 `.skill` 文件是一个 **YAML 文档**，以 `#` 注释开头作为人类可读标题，后跟 YAML 键值对。

### 必需字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | Skill 名称，kebab-case，与文件名一致（不含扩展名） |
| `version` | string | 语义化版本号，格式 `x.y.z`（如 `1.0.0`） |
| `description` | string | 一行描述：做什么 + 何时触发 |
| `philosophy` | string (multiline) | 核心理念，解释为什么这样设计 |

### 可选字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `deprecated` | boolean | 是否已废弃 |
| `replaced_by` | string | 替代文件名 |
| `constraints` | list[string] | 使用约束 |
| `workflow` | map | 使用流程步骤 |

### 命名规范

- 文件名：`^[a-z0-9]+(-[a-z0-9]+)*\.skill$`
- 示例：`director-engine.skill`、`anti-slop.skill`

## 文件结构示例

```yaml
# 人类可读标题
# 补充说明（可选）

name: "my-skill"
version: "1.0.0"
description: "一句话说明做什么、何时用"

philosophy: |
  核心理念的多行描述。
  解释为什么这样设计，而不是那样。

# 以下为 Skill 特定内容，结构自由
my_custom_section:
  key: "value"

constraints:
  - "约束条件 1"
  - "约束条件 2"

workflow:
  step_1: "第一步"
  step_2: "第二步"
```

## 注意事项

- **不要使用 `---` frontmatter 分隔符。** 文件以 `#` 注释开头，直接跟 YAML 内容。
- **不要在提示词内容中使用 JSON。** Skill 的 Schema 定义可以用 YAML 嵌套结构，但面向视频模型的 prompt 必须是自然语言。
- **版本号必须是三段式 semver。** `1.0` 不合规，`1.0.0` 合规。
- **废弃文件必须标注 `deprecated: true` 和 `replaced_by`。**

## 验证

```bash
python scripts/validate_all.py skills/
```

验证项目：YAML 格式 → 必需字段 → 命名规范 → 版本号格式。
