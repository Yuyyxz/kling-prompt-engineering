#!/usr/bin/env python3
"""成片评分聚合与基线回归检查。维度定义见 evals/video-rubric.md。

用法:
    python3 evals/score_video.py scores.jsonl
    python3 evals/score_video.py scores.jsonl --save-baseline evals/video-baseline.json
    python3 evals/score_video.py scores.jsonl --baseline evals/video-baseline.json

基线对比: 同一 (model, prompt_version) 组合在基线里不存在时按新组合处理；
要查「新版本比旧版本退步没有」，把旧版本聚合存基线后，新版本数据里
用 --compare-version <旧版本> 显式指定对比对象。
任一维度回退 > 阈值（默认 0.3）退出码 1。
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

DIMS = ["visual_quality", "temporal_consistency", "dynamic_degree",
        "text_alignment", "factual_consistency", "character_consistency",
        "audio_sync"]


def load_scores(path):
    rows, errors = [], []
    for i, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"第 {i} 行 JSON 解析失败: {e}")
            continue
        sc = r.get("scores") or {}
        for d in DIMS:
            v = sc.get(d)
            if v is not None and not (isinstance(v, (int, float)) and 1 <= v <= 4):
                errors.append(f"第 {i} 行 {d}={v} 不在 1-4 范围")
        missing = [d for d in DIMS if d not in sc]
        if missing:
            errors.append(f"第 {i} 行缺维度 {missing}（无声镜头 audio_sync 填 null，不要省略）")
        rows.append(r)
    return rows, errors


def aggregate(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[(r.get("model"), r.get("prompt_version"))].append(r)
    out = {}
    for key, rs in groups.items():
        agg = {"n": len(rs)}
        for d in DIMS:
            vals = [r["scores"][d] for r in rs if r.get("scores", {}).get(d) is not None]
            agg[d] = round(sum(vals) / len(vals), 3) if vals else None
        dims_present = [agg[d] for d in DIMS if agg[d] is not None]
        agg["overall"] = round(sum(dims_present) / len(dims_present), 3) if dims_present else None
        out[f"{key[0]} @ {key[1]}"] = agg
    return out


def fmt(agg):
    lines = []
    for name, a in agg.items():
        cells = "  ".join(f"{d.split('_')[0]}={a[d]}" for d in DIMS if a[d] is not None)
        lines.append(f"{name}  n={a['n']}  overall={a['overall']}\n    {cells}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="成片评分聚合 + 基线回归")
    ap.add_argument("scores")
    ap.add_argument("--baseline", help="基线 JSON 路径（存在则自动对比）")
    ap.add_argument("--save-baseline", help="把本次聚合写为基线到这个路径")
    ap.add_argument("--compare-version", help="基线里要对比的 prompt_version（跨版本回归检查）")
    ap.add_argument("--threshold", type=float, default=0.3)
    args = ap.parse_args()

    rows, errors = load_scores(args.scores)
    for e in errors:
        print(f"[error] {e}")
    if errors:
        return 1
    agg = aggregate(rows)
    print(fmt(agg))

    if args.save_baseline:
        Path(args.save_baseline).write_text(
            json.dumps(agg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"[ok] 基线已写入 {args.save_baseline}")

    rc = 0
    baseline_path = args.baseline
    if baseline_path and Path(baseline_path).exists():
        base = json.loads(Path(baseline_path).read_text(encoding="utf-8"))
        for name, a in agg.items():
            bname = name
            if args.compare_version:
                model = name.split(" @ ")[0]
                bname = f"{model} @ {args.compare_version}"
            b = base.get(bname)
            if not b:
                print(f"[note] 基线里没有 {bname}，跳过对比（新组合）")
                continue
            for d in DIMS + ["overall"]:
                if a.get(d) is not None and b.get(d) is not None and b[d] - a[d] > args.threshold:
                    print(f"[REGRESSION] {name} 的 {d} 回退 {b[d]} -> {a[d]}（阈值 {args.threshold}）")
                    rc = 1
        if rc == 0:
            print("[ok] 与基线对比无回退")
    return rc


if __name__ == "__main__":
    sys.exit(main())
