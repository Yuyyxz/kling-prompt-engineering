#!/usr/bin/env python3
"""分镜结构化校验

校验一份符合 schemas/storyboard.schema.json 的分镜 JSON：
- 必填字段和 11 维齐不齐（手写检查，不依赖 jsonschema 库；装了会顺带跑一遍 schema）
- 总时长 = 各 shot 时长之和
- 相邻 shot 景别不能相同（kling-storyboard 规则）
- 角色卡逐字一致：shot 里写的 appearance 必须和 characters 里的角色卡一字不差
- 风格 token 组：每个 shot 的 prompt_text 都要带齐 style_tokens
- 引用完整性：shot.references 的 asset_id 必须在 characters/assets 里存在
- 镜号撞号：镜号 Sxx 和场景素材 Sxx 同号时报警（两个编号体系的 S 不是一个意思）
- 节拍启发式：subject_action 出现「然后/接着/随后又」时警告可能一镜多拍

用法:
  python scripts/validate_storyboard.py examples/storyboard-example.json
  python scripts/validate_storyboard.py path/to/board.json --manifest out.manifest.json

退出码：有 error 为 1，只有 warning 为 0。--strict 时 warning 也算失败。
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHOT_SIZES = {"极远景", "远景", "全景", "中景", "近景", "特写", "微距"}
FUNCTIONS = {"引入", "深化", "转折", "收束"}
MULTI_BEAT_MARKERS = ["然后", "接着", "随后又", "先是", "再然后"]
REQUIRED_SHOT_FIELDS = [
    "id", "duration_s", "shot_size", "angle", "camera_movement",
    "subject_action", "light", "sound", "transition",
    "constraints", "dramatic_function", "prompt_text",
]

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def main():
    ap = argparse.ArgumentParser(description="校验 KPE 结构化分镜 JSON")
    ap.add_argument("file", help="分镜 JSON 路径")
    ap.add_argument("--manifest", help="把 manifest 片段写到这个文件（给 workflow 仓库挂载用）")
    ap.add_argument("--otio", help="导出 OpenTimelineIO (.otio) 时间线到这个文件，给剪辑软件/ffmpeg 合成阶段接续")
    ap.add_argument("--fps", type=float, default=24, help="OTIO 导出用的帧率（默认 24）")
    ap.add_argument("--strict", action="store_true", help="warning 也算失败")
    args = ap.parse_args()

    path = Path(args.file)
    try:
        board = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[FAIL] JSON 读不了: {e}")
        return 1

    # 可选：装了 jsonschema 就先跑一遍 schema
    schema_path = ROOT / "schemas" / "storyboard.schema.json"
    if schema_path.exists():
        try:
            import jsonschema  # noqa: F401
            import json as _json
            schema = _json.loads(schema_path.read_text(encoding="utf-8"))
            v = jsonschema.Draft202012Validator(schema)
            for e in sorted(v.iter_errors(board), key=lambda x: list(x.path)):
                loc = "/".join(str(x) for x in e.path) or "(root)"
                err(f"schema: {loc}: {e.message}")
        except ImportError:
            print("[info] 未装 jsonschema，只跑手写规则检查（pip install jsonschema 可启用 schema 校验）")

    for field in ["project", "storyboard_version", "style", "total_duration_s", "characters", "shots"]:
        if field not in board:
            err(f"顶层缺字段: {field}")
    shots = board.get("shots") or []
    if not shots:
        err("shots 为空")
        return report(args, board, shots)

    # 角色卡索引
    cards = {}
    for c in board.get("characters") or []:
        cid = c.get("id")
        if cid in cards:
            err(f"角色编号重复: {cid}")
        cards[cid] = c
        refs = c.get("reference_images") or []
        if len(refs) < 2:
            warn(f"角色 {cid} 参考图少于 2 张（要求至少正面全身、侧面半身）")

    asset_ids = set(cards)
    for a in board.get("assets") or []:
        asset_ids.add(a.get("id"))

    style_tokens = (board.get("style") or {}).get("style_tokens") or []

    total = 0.0
    prev_size = None
    manifest_shots = []
    for i, s in enumerate(shots):
        sid = s.get("id", f"#{i + 1}")
        for f in REQUIRED_SHOT_FIELDS:
            if f not in s or s[f] in ("", None):
                err(f"{sid}: 缺 11 维字段 {f}")
        dur = s.get("duration_s")
        if isinstance(dur, (int, float)):
            total += dur
        if s.get("shot_size") and s["shot_size"] not in SHOT_SIZES:
            err(f"{sid}: 景别不在枚举里: {s['shot_size']}")
        if s.get("shot_size") == prev_size and prev_size is not None:
            err(f"{sid}: 与上一镜景别相同（{prev_size}），相邻镜头景别必须有变化")
        prev_size = s.get("shot_size")
        if s.get("dramatic_function") and s["dramatic_function"] not in FUNCTIONS:
            err(f"{sid}: 戏剧功能不在枚举里: {s['dramatic_function']}")
        action = s.get("subject_action") or ""
        if any(mk in action for mk in MULTI_BEAT_MARKERS):
            warn(f"{sid}: subject_action 出现串联词，可能一镜多拍，拆镜头或删到只剩一个节拍")
        # 镜号与场景素材撞号
        for a in board.get("assets") or []:
            if a.get("kind") == "scene" and a.get("id") == sid:
                warn(f"{sid}: 镜号和场景素材编号撞号，镜号建议改成 SHOT- 形式")
        # 角色逐字一致
        for ch in s.get("characters") or []:
            card = cards.get(ch.get("id"))
            if card is None:
                err(f"{sid}: 引用了未在 characters 里定义的角色 {ch.get('id')}")
            elif ch.get("appearance") is not None and ch["appearance"] != card.get("appearance"):
                err(f"{sid}: 角色 {ch['id']} 的 appearance 与角色卡不一致，角色卡必须逐字复用")
        # 引用完整性
        for r in s.get("references") or []:
            if r.get("asset_id") not in asset_ids:
                err(f"{sid}: references 引用了不存在的素材 {r.get('asset_id')}")
        # 风格 token 逐字带齐
        prompt = s.get("prompt_text") or ""
        for tok in style_tokens:
            if tok not in prompt:
                err(f"{sid}: prompt_text 缺风格 token「{tok}」，风格 token 组必须逐字追加到每个 shot")
        manifest_shots.append({
            "shot_id": sid,
            "duration_s": dur,
            "dramatic_function": s.get("dramatic_function"),
            "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest() if prompt else None,
            "references": [r.get("asset_id") for r in s.get("references") or []],
        })

    declared = board.get("total_duration_s")
    if isinstance(declared, (int, float)) and abs(total - declared) > 0.01:
        err(f"总时长对不上：声明 {declared}s，各 shot 之和 {total:g}s")

    n = len(shots)
    if isinstance(declared, (int, float)):
        if declared <= 15 and n > 4:
            warn(f"15s 以内镜头数 {n} 偏多（规则：最多 3-4 个），考虑拆集或合并")
        elif declared <= 30 and n > 8:
            warn(f"30s 镜头数 {n} 偏多（规则：最多 6-8 个）")

    if args.manifest:
        manifest = {
            "project": board.get("project"),
            "storyboard_version": board.get("storyboard_version"),
            "model_facts_ref": board.get("model_facts_ref"),
            "total_duration_s": declared,
            "shots": manifest_shots,
        }
        Path(args.manifest).write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"[ok] manifest 片段已写到 {args.manifest}")

    if args.otio:
        otio = build_otio(board, shots, manifest_shots, args.fps)
        Path(args.otio).write_text(
            json.dumps(otio, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"[ok] OTIO 时间线已写到 {args.otio}")

    return report(args, board, shots)


def build_otio(board, shots, manifest_shots, fps):
    """分镜 → OpenTimelineIO 最小子集（Timeline/Stack/Track/Clip）。

    OTIO 是剪辑时间线的行业交换格式（Academy Software Foundation），
    剪辑软件与合成管线普遍能读。这里只输出核心结构：每镜一个 Clip，
    时长用 RationalTime（帧数 + 帧率），KPE 的 11 维与 prompt 哈希放进
    metadata.kpe，成片文件后续按 shot_id 回填 media_reference。
    """
    def rt(seconds):
        return {
            "OTIO_SCHEMA": "RationalTime.1",
            "rate": fps,
            "value": round(seconds * fps),
        }

    clips = []
    cursor = 0.0
    for s, ms in zip(shots, manifest_shots):
        dur = s.get("duration_s") or 0
        clips.append({
            "OTIO_SCHEMA": "Clip.2",
            "name": s.get("id"),
            "source_range": {
                "OTIO_SCHEMA": "TimeRange.1",
                "start_time": rt(0),
                "duration": rt(dur),
            },
            "media_reference": {
                "OTIO_SCHEMA": "MissingReference.1",
                "name": s.get("id"),
                "metadata": {},
            },
            "metadata": {
                "kpe": {
                    "timeline_offset_s": cursor,
                    "shot_size": s.get("shot_size"),
                    "angle": s.get("angle"),
                    "camera_movement": s.get("camera_movement"),
                    "dramatic_function": s.get("dramatic_function"),
                    "transition": s.get("transition"),
                    "prompt_sha256": ms.get("prompt_sha256"),
                    "references": ms.get("references"),
                }
            },
        })
        cursor += dur
    return {
        "OTIO_SCHEMA": "Timeline.1",
        "name": board.get("project") or "kpe-storyboard",
        "global_start_time": rt(0),
        "metadata": {
            "kpe": {
                "storyboard_version": board.get("storyboard_version"),
                "model_facts_ref": board.get("model_facts_ref"),
                "total_duration_s": board.get("total_duration_s"),
                "exported_by": "kpe validate_storyboard.py --otio",
            }
        },
        "tracks": {
            "OTIO_SCHEMA": "Stack.1",
            "children": [{
                "OTIO_SCHEMA": "Track.1",
                "name": "V1",
                "kind": "Video",
                "children": clips,
            }],
        },
    }


def report(args, board, shots):
    for w in warnings:
        print(f"[warn] {w}")
    for e in errors:
        print(f"[FAIL] {e}")
    if errors or (args.strict and warnings):
        print(f"\n校验未通过：{len(errors)} 个 error，{len(warnings)} 个 warning")
        return 1
    print(f"\n校验通过：{len(shots)} 个 shot，{len(warnings)} 个 warning")
    return 0


if __name__ == "__main__":
    sys.exit(main())
