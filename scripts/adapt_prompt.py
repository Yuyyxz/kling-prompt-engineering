#!/usr/bin/env python3
"""把结构化分镜（storyboard JSON）适配到目标模型，输出可提交的生成计划。

这是 adapters/ 从「死数据」变可执行的第一步：读 adapters/model_facts.yaml
（唯一事实源），对每镜做硬限制检查，不支持或超限的项**显式写进
warnings/errors，不静默丢弃**。输出包含统一请求预览（normalized request，
形状参考 fal 等聚合渠道的 Input Schema：prompt / multi_prompt / duration /
aspect_ratio / resolution），方便下游换任何渠道提交。

用法:
    python3 scripts/adapt_prompt.py examples/storyboard-example.json \
        --model kling_4_0 --model seedance_2_0
    python3 scripts/adapt_prompt.py sb.json --model all --out /tmp/plan
    # --out 写 <out>.<model>.json；不带 --out 时打印到 stdout（JSON）

退出码: 任一目标模型出现 errors 时为 1，否则 0。
依赖: PyYAML（仓库脚本统一依赖）。先用 validate_storyboard.py 校验分镜再适配。
"""
import argparse
import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
TEXT_HINTS = ("文字", "字幕", "招牌", "标题", "text", "signage", "logo")
DIALOGUE_HINTS = ("说", "台词", "对白", "喊", "问", "答", "：", "“", "”", '"')


def load_facts(path):
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return data["meta"], data["models"]


def collect_references(sb):
    """统计分镜里实际要喂给模型的参考素材量（按 storyboard 的引用关系）。"""
    images = set()
    for ch in sb.get("characters", []):
        images.update(ch.get("reference_images", []))
    for a in sb.get("assets", []):
        if a.get("reference"):
            images.add(a["reference"])
    first_frames = 0
    roles = set()
    for s in sb.get("shots", []):
        for r in s.get("references", []):
            roles.add(r.get("role"))
            if r.get("role") == "first-frame":
                first_frames += 1
    return {"images": len(images), "first_frames": first_frames, "roles": sorted(roles)}


def adapt(sb, model_id, facts, facts_version):
    m = facts[model_id]
    shots = sb.get("shots", [])
    total = sum(s.get("duration_s", 0) for s in shots)
    warnings, errors, notes = [], [], []
    dur = m.get("duration_s") or {}
    dmin, dmax = dur.get("min"), dur.get("max", m.get("max_duration_s"))

    # 逐镜时长
    for s in shots:
        d = s.get("duration_s", 0)
        if dmax and d > dmax:
            errors.append(f"{s['id']}: 单镜 {d}s 超过 {m['display_name']} 单次上限 {dmax}s，必须拆镜或改模型")
        if dmin and d < dmin:
            warnings.append(f"{s['id']}: 单镜 {d}s 短于该模型最短时长 {dmin}s，提交时会被抬到 {dmin}s，节奏会变")

    # 画幅
    ar = (sb.get("style") or {}).get("aspect_ratio")
    supported_ar = m.get("aspect_ratios")
    if ar and supported_ar and ar not in supported_ar:
        warnings.append(f"画幅 {ar} 不在 {m['display_name']} 支持列表 {supported_ar} 里，渠道会拒绝或自动改画幅")
    if ar and not supported_ar:
        notes.append(f"{m['display_name']} 在事实文件里未列画幅清单，画幅 {ar} 提交前在渠道确认")

    # 参考素材上限
    refs = collect_references(sb)
    ri = m.get("reference_inputs") or {}
    if ri.get("images_max") and refs["images"] > ri["images_max"]:
        errors.append(f"参考图 {refs['images']} 张超过 {m['display_name']} 上限 {ri['images_max']} 张，必须取舍（优先 identity 角色图）")
    if ri.get("combined_max") and refs["images"] > ri["combined_max"]:
        errors.append(f"参考素材合计超过 Omni combined 上限 {ri['combined_max']}")

    # 关键帧（Kling 4.0）
    kf = m.get("keyframes") or {}
    if kf.get("max") and refs["first_frames"] > kf["max"]:
        warnings.append(f"首帧/关键帧引用 {refs['first_frames']} 处超过关键帧上限 {kf['max']}，多余的只能降级为普通参考")

    # 音频与对白
    has_dialogue = any(
        any(h in (s.get("sound") or "") for h in DIALOGUE_HINTS[1:]) or "：" in (s.get("sound") or "")
        for s in shots
    )
    sound_shots = [s["id"] for s in shots if (s.get("sound") or "").strip()]
    if sound_shots and not m.get("native_audio"):
        warnings.append(f"{m['display_name']} 无原生音频：{', '.join(sound_shots)} 的声音设计不会被生成，需后期单独做音频轨")
    if has_dialogue and m.get("dialogue_languages"):
        notes.append(f"含对白镜头：该模型已确认对白语种 {m['dialogue_languages']}，用其他语种先小样验证口型")
    if m.get("audio_as_clock"):
        notes.append("该模型以音频为时钟：对白/音乐先定时长，画面跟音频走，分镜时长按音频长度复核")

    # 原生文字渲染
    needs_text = any(
        any(h in (s.get("prompt_text") or "") for h in TEXT_HINTS)
        and "无文字" not in (s.get("prompt_text") or "")
        for s in shots
    )
    if needs_text and not m.get("native_text_rendering"):
        warnings.append(f"{m['display_name']} 未确认原生文字渲染：画面内文字大概率出错，改走后期合成或换模型")

    if m.get("ip_name_blocking"):
        notes.append("该平台屏蔽 IP/品牌名：prompt_text 里如有 IP 名会被拦，提交前人工过一遍（脚本不猜名单）")
    if m.get("channel_dependent"):
        notes.append(f"渠道相关：{m.get('channel_note', '档位按所用渠道确认')}")

    # 生成模式
    multi = m.get("multi_shot") or {}
    if multi.get("supported") and dmax and total <= dmax and len(shots) <= (multi.get("max_shots") or 99):
        mode = "multi_prompt"
        notes.append(f"总时长 {total}s、共 {len(shots)} 镜，可一次多镜头生成（multi_prompt 逐镜提交）")
    elif dmax and total <= dmax and len(shots) == 1:
        mode = "single"
    else:
        mode = "per_shot"
        if dmax and total > dmax:
            warnings.append(f"总时长 {total}s 超过单次上限 {dmax}s：按逐镜生成 + 后期拼接执行，或用视频延长链总长")
        elif len(shots) > 1:
            notes.append(f"{m['display_name']} 不支持多镜头一次生成：逐镜生成后拼接，尾帧衔接按 21-retake-protocol 处理")

    plan_shots = [
        {"id": s["id"], "duration_s": s.get("duration_s"), "prompt": s.get("prompt_text", "")}
        for s in shots
    ]
    request = {
        "model": model_id,
        "duration": total if mode != "per_shot" else None,
        "aspect_ratio": ar,
        "resolution_max": m.get("resolution_max"),
    }
    if mode == "multi_prompt":
        request["multi_prompt"] = plan_shots
    elif mode == "single" and plan_shots:
        request["prompt"] = plan_shots[0]["prompt"]
        request["duration"] = plan_shots[0]["duration_s"]

    return {
        "model": model_id,
        "display_name": m.get("display_name"),
        "model_facts": f"adapters/model_facts.yaml@{facts_version}",
        "mode": mode,
        "total_duration_s": total,
        "request_preview": request,
        "shots": plan_shots,
        "warnings": warnings,
        "errors": errors,
        "notes": notes,
    }


def main():
    ap = argparse.ArgumentParser(description="分镜 → 分模型生成计划（读 model_facts 硬限制）")
    ap.add_argument("storyboard")
    ap.add_argument("--model", action="append", required=True,
                    help="模型 id（model_facts.yaml 里的键），可重复；all = 全部真实模型")
    ap.add_argument("--facts", default=str(REPO / "adapters" / "model_facts.yaml"))
    ap.add_argument("--out", help="输出前缀，写 <out>.<model>.json")
    args = ap.parse_args()

    sb = json.loads(Path(args.storyboard).read_text(encoding="utf-8"))
    meta, facts = load_facts(args.facts)
    targets = [k for k in facts if k != "kling_family"] if "all" in args.model else args.model
    rc = 0
    results = []
    for mid in targets:
        if mid not in facts:
            print(f"[error] model_facts 里没有模型 {mid}", file=sys.stderr)
            rc = 1
            continue
        plan = adapt(sb, mid, facts, meta.get("version"))
        results.append(plan)
        if plan["errors"]:
            rc = 1
        if args.out:
            out = Path(f"{args.out}.{mid}.json")
            out.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"[ok] {mid}: mode={plan['mode']} warnings={len(plan['warnings'])} errors={len(plan['errors'])} -> {out}")
    if not args.out:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    return rc


if __name__ == "__main__":
    sys.exit(main())
