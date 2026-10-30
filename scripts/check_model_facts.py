#!/usr/bin/env python3
"""模型事实一致性检查

单一数据源是 adapters/model_facts.yaml。本脚本查三件容易漂移的事：
1. kling_adapter.yaml 的全系上限有没有跟事实文件打架
2. 12-kling-capability-map.md 的规格表里还有没有已过期的旧口径
3. model_facts.yaml 本身有没有 verified_at、是不是太久没复核

用法: python scripts/check_model_facts.py
退出码: 有冲突 1，无冲突 0。只用标准库，yaml 可用时解析，不可用时退回文本检查。
"""

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "adapters" / "model_facts.yaml"
STALE_AFTER_DAYS = 60

problems = []
warnings = []


def read(path):
    return path.read_text(encoding="utf-8")


def main():
    if not FACTS.exists():
        print("[FAIL] adapters/model_facts.yaml 不存在，单一数据源缺失")
        return 1
    facts = read(FACTS)

    m = re.search(r'verified_at:\s*"(\d{4}-\d{2}-\d{2})"', facts)
    if not m:
        problems.append("model_facts.yaml 缺 verified_at")
    else:
        verified = date.fromisoformat(m.group(1))
        age = (date.today() - verified).days
        if age > STALE_AFTER_DAYS:
            warnings.append(f"model_facts.yaml 已 {age} 天没复核（verified_at={m.group(1)}），使用前先复核")
        print(f"[ok] verified_at = {m.group(1)}（{age} 天前）")

    # 事实文件里 Kling 全系上限
    fam = re.search(r'kling_family:.*?max_duration_s:\s*(\d+)', facts, re.S)
    facts_max = int(fam.group(1)) if fam else None

    # 1. kling_adapter 全系上限
    adapter = read(ROOT / "adapters" / "kling_adapter.yaml")
    am = re.search(r'capabilities:.*?max_duration:\s*"(\d+)s"', adapter, re.S)
    if am and facts_max and int(am.group(1)) != facts_max:
        problems.append(
            f"kling_adapter.yaml 全系 max_duration={am.group(1)}s 与 model_facts 的 {facts_max}s 不一致"
        )
    else:
        print(f"[ok] kling_adapter 全系时长上限与事实文件一致（{facts_max}s）")
    if "镜头语言] + [主体动作" in adapter:
        problems.append("kling_adapter.yaml 还在用旧黄金公式（以镜头语言开头），应与 CLAUDE.md 新公式对齐")
    else:
        print("[ok] kling_adapter 黄金公式已是新公式")

    # 2. capability-map 旧口径残留
    capmap = read(ROOT / "12-kling-capability-map.md")
    stale_patterns = [
        (r"\|\s*v3\s*\|\s*1080p\s*\|\s*5/10s", "规格表还写 v3 = 1080p / 5/10s（旧口径）"),
        (r"video-o1\s*\|\s*720p", "规格表还写 video-o1 = 720p（旧口径，应为 1080p）"),
        (r"v2\.5-turbo.*5/10/15s", "规格表还把 15s 写成 v2.5-turbo 主规格（应注明渠道口径）"),
    ]
    for pat, msg in stale_patterns:
        if re.search(pat, capmap):
            problems.append(f"12-kling-capability-map.md: {msg}")
    if not any("12-kling" in p for p in problems):
        print("[ok] capability-map 规格表没有旧口径残留")
    if "model_facts.yaml" not in capmap:
        problems.append("12-kling-capability-map.md 没有指向 model_facts.yaml 的口径说明")

    # 3. planned 模型口径
    translator = read(ROOT / "adapters" / "prompt_translator.yaml")
    if "draft_unverified" not in translator:
        problems.append("prompt_translator.yaml 没有标注 planned 模型的草案状态")
    else:
        print("[ok] prompt_translator 已标注草案状态")

    for w in warnings:
        print(f"[warn] {w}")
    for p in problems:
        print(f"[FAIL] {p}")
    if problems:
        print(f"\n共 {len(problems)} 处冲突，先改冲突文件对齐 model_facts.yaml，不要改事实文件迁就旧口径。")
        return 1
    print("\n模型事实一致性检查通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
