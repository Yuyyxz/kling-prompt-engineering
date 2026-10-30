#!/usr/bin/env python3
"""Prompt 变体实验脚手架：同一镜头多个变体，用 prompt_lint 打分排序。

定位见 experiments/README.md：这是 DSPy 式自动优化立项前的手动版，
指标只是 prompt 层的 lint 分（文本卫生），**不代表成片质量**。
变体之间要比成片好坏，走 evals/video-rubric.md + score_video.py。

输入 JSONL，每行: {"case_id": "...", "variant": "A", "prompt": "..."}
用法: python3 experiments/variant_eval.py experiments/variants.example.jsonl
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LINT = REPO / "scripts" / "prompt_lint.py"
SCORE_RE = re.compile(r"Score:\s*(\d+)/100")


def lint_score(prompt):
    p = subprocess.run([sys.executable, str(LINT), prompt],
                       capture_output=True, text=True)
    m = SCORE_RE.search(p.stdout)
    return int(m.group(1)) if m else None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    groups = defaultdict(list)
    for i, line in enumerate(Path(sys.argv[1]).read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        s = lint_score(row["prompt"])
        if s is None:
            print(f"[error] 第 {i} 行 lint 未返回分数，跳过")
            continue
        groups[row["case_id"]].append((row["variant"], s))
    for case, vs in groups.items():
        vs.sort(key=lambda x: -x[1])
        print(f"\n{case}")
        for rank, (v, s) in enumerate(vs, 1):
            print(f"  {rank}. {v}: {s}/100")
        if len(vs) > 1:
            print(f"  极差 {vs[0][1] - vs[-1][1]} 分（只说明文本卫生差异，不说明成片差异）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
