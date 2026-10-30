#!/usr/bin/env python3
"""重拍日志聚合：把 JSONL 重拍记录汇总成 failure-atlas 的供稿候选。

字段约定见 workflows/retake-log-template.md。聚合口径:
- 按失败归类计数，同类失败 >= 3 次 -> atlas 候选（带症状样本）；
- 同一「失败归类 + 改动的变量字段」组合被验证有效（改完即 accepted）
  >= 2 次 -> 已验证修法候选；
- 输出 markdown 草稿到 stdout 或 --out 文件，**只是草稿**，
  进 failure-atlas 前必须人工过（模板里的既定纪律）。

用法: python3 scripts/retake_report.py logs/project-a.jsonl [更多日志...]
"""
import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="重拍日志聚合 -> failure-atlas 候选草稿")
    ap.add_argument("logs", nargs="+")
    ap.add_argument("--out")
    args = ap.parse_args()

    rows = []
    for p in args.logs:
        for i, line in enumerate(Path(p).read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"[error] {p} 第 {i} 行解析失败: {e}", file=sys.stderr)
                return 1
    total = len(rows)
    verdicts = Counter((r.get("result") or {}).get("verdict") for r in rows)
    cats = Counter()
    symptoms = defaultdict(list)
    fix_verified = Counter()
    per_shot = Counter()
    credits = 0
    for r in rows:
        res = r.get("result") or {}
        per_shot[(r.get("project"), r.get("shot_id"))] += 1
        c = (r.get("cost") or {}).get("credits")
        if isinstance(c, (int, float)):
            credits += c
        if res.get("verdict") in ("retake", "rejected") and res.get("failure_category"):
            cats[res["failure_category"]] += 1
            if res.get("symptom"):
                symptoms[res["failure_category"]].append(
                    f"{r.get('shot_id')} attempt {r.get('attempt')}: {res['symptom']}")
        if res.get("verdict") == "accepted":
            cv = r.get("changed_variable") or {}
            # 找到同 shot 前一条失败记录的归类，归功于这次改动
            prev = [x for x in rows if x.get("shot_id") == r.get("shot_id")
                    and x.get("project") == r.get("project")
                    and (x.get("attempt") or 0) < (r.get("attempt") or 0)
                    and (x.get("result") or {}).get("failure_category")]
            if prev and cv.get("field"):
                cat = prev[-1]["result"]["failure_category"]
                fix_verified[(cat, cv["field"], str(cv.get("to")))] += 1

    accepted = verdicts.get("accepted", 0)
    lines = ["# 重拍日志聚合（failure-atlas 供稿草稿，需人工过）", ""]
    lines.append(f"- 记录总数 {total}，accepted {accepted}，retake {verdicts.get('retake', 0)}，"
                 f"rejected {verdicts.get('rejected', 0)}，一次通过率 "
                 f"{(accepted / total * 100 if total else 0):.0f}%（按记录计，含重拍后续记录）")
    lines.append(f"- 已知成本合计 {credits} credits（只统计填了 credits 的记录）")
    lines.append("")
    lines.append("## 失败归类计数")
    for cat, n in cats.most_common():
        lines.append(f"- {cat}: {n} 次")
    lines.append("")
    lines.append("## atlas 候选（同类失败 >= 3 次）")
    cand = [(c, n) for c, n in cats.most_common() if n >= 3]
    if not cand:
        lines.append("- 暂无（样本不足 3 次的类别不提炼，避免把偶发当规律）")
    for cat, n in cand:
        lines.append(f"### {cat}（{n} 次）")
        for s in symptoms[cat][:5]:
            lines.append(f"- 症状样本：{s}")
    lines.append("")
    lines.append("## 已验证修法候选（同归类+同改动 accepted >= 2 次）")
    fixes = [(k, n) for k, n in fix_verified.most_common() if n >= 2]
    if not fixes:
        lines.append("- 暂无")
    for (cat, field, to), n in fixes:
        lines.append(f"- {cat} -> 改 {field} 为「{to}」：验证 {n} 次")
    lines.append("")
    lines.append("## 重拍最多的镜头")
    for (proj, shot), n in per_shot.most_common(5):
        if n > 1:
            lines.append(f"- {proj} / {shot}: {n} 条记录")
    text = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"[ok] 已写到 {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
