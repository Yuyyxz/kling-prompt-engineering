---
name: multi-platform
description: "多平台兼容数据。KPE 在不同 AI 编程工具（Claude Code、Cursor、Codex 等）上的安装与使用差异。用户问某个平台怎么装、怎么加载技能时用。"
version: "1.1.0"
---

# multi-platform — 多平台兼容

先说清现状：真正可执行的是仓库根目录的 `install.sh`，它支持 claude / cursor / codex / windsurf / trae / qwen / generic 七种目标，装的是标准技能目录。本技能的 data.yaml 保留了早期 15+ 平台的兼容笔记和配置模板，做 install.sh 没覆盖的平台时拿来参考，但不要把笔记当成已实测的安装路径。

## 何时读 references

查某平台的记录读 `references/data.yaml` 的 `supported_platforms` 和 `config_templates`，先看 `references/sections.md` 定位。安装方法与脚本在 `installation_methods`、`installation_scripts` 两节，是历史版本，和现行 install.sh 冲突时以 install.sh 为准。

## Workflow

1. 先确认目标平台在不在 install.sh 的七种里。在，直接用 install.sh，不要手抄文件。
2. 不在，用 generic 模式装到自定义目录，再按 data.yaml 里同类平台的配置模板补加载方式。
3. 装完验证：目标工具里能列出技能、能触发一个技能、references 跟着目录一起过去了，三项都过才算装好。
4. 遇到平台特有的坑（路径、编码、frontmatter 兼容），记回 data.yaml 对应平台条目下方，不要只留在当次对话里。

## Gotchas

技能的 description 是各平台的触发依据，写得含糊哪个平台都触发不准。改 description 时按最严的平台标准写：讲清做什么、什么时候用。

frontmatter 兼容性各家不一：多余字段有的平台忽略、有的直接报错。新字段先在目标平台实测再全量铺开。

Windows 路径和编码是老问题。中文路径下个别工具读不到 references，装到纯英文路径能避开大半。

## 规则

- 平台支持状态分三档写清：install.sh 已支持、data.yaml 有笔记未实测、完全没记录。不许把第二档说成第一档。
- 新增平台先跑通最小验证（列出 + 触发 + references 可读）再写进文档。
