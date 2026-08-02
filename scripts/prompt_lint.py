#!/usr/bin/env python3
"""Prompt Lint — Anti-Slop 提示词质量检查工具
Usage:
    python scripts/prompt_lint.py "your prompt text here"
    python scripts/prompt_lint.py --file prompt.txt
"""
import argparse
import re
import sys

# ── ANSI colors ──────────────────────────────────────────────
RED, YEL, GRN, CYN, DIM, RST = "\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[2m", "\033[0m"

# ── Slop word → replacement table (from 09-anti-slop.md) ─────
SLOP_TABLE = {
    "cinematic": "具体景别 + 镜头运动 + 光线 + 色调 (specific shot size + movement + light + tone)",
    "beautiful": "色彩、质感、构图、材质、光线行为 (color, texture, composition, material, light behavior)",
    "stunning": "可见的对比、揭示、运动或细节 (visible contrast, reveal, motion or detail)",
    "breathtaking": "可见的对比、揭示、运动或细节 (visible contrast, reveal, motion or detail)",
    "epic": "物理规模、风险、人群大小、镜头距离 (physical scale, risk, crowd size, lens distance)",
    "amazing": "删除；用一个可观察细节替代 (delete; replace with one observable detail)",
    "gorgeous": "色彩、质感、构图、材质 (color, texture, composition, material)",
    "masterpiece": "删除；质量不是请求 (delete; quality is not a request)",
    "4k": "删除；分辨率是渲染设置 (delete; resolution is a render setting)",
    "8k": "删除；分辨率是渲染设置 (delete; resolution is a render setting)",
    "ultra detailed": "命名的两个重要细节 (name two important details)",
    "ultra realistic": "材质行为、皮肤质感、镜头伪影、自然运动 (material behavior, skin texture, lens artifacts)",
    "hyper realistic": "材质行为、皮肤质感、镜头伪影、自然运动 (material behavior, skin texture, lens artifacts)",
    "premium": "产品光线设置、干净背景、受控镜头 (product lighting, clean background, controlled lens)",
    "luxurious": "材质描述：磨砂、金属光泽、织物纹理 (material: matte, metallic sheen, fabric weave)",
    "moody": "光线来源 + 色温 + 声音环境 (light source + color temp + sound environment)",
    "atmospheric": "光线来源 + 色温 + 声音环境 (light source + color temp + sound environment)",
    "jaw-dropping": "观众记住的那一帧，描述出来 (describe the one frame the audience remembers)",
    "mind-blowing": "观众记住的那一帧，描述出来 (describe the one frame the audience remembers)",
    "incredible": "删除；用一个可观察细节替代 (delete; replace with one observable detail)",
    "awesome": "删除；用一个可观察细节替代 (delete; replace with one observable detail)",
    "perfect": "删除；描述具体的物理状态 (delete; describe a specific physical state)",
    "flawless": "删除；描述具体的物理状态 (delete; describe a specific physical state)",
}

# ── Keyword lists ────────────────────────────────────────────
LIGHT_KW = [
    "sun", "window", "lamp", "neon", "candle", "spotlight", "backlight",
    "rim light", "golden hour", "overcast", "fluorescent", "fire", "moon",
    "street light", "太阳", "自然光", "侧光", "逆光", "窗光", "霓虹",
    "烛光", "台灯", "月光", "路灯", "光线", "光源", "light",
]
CAMERA_KW = [
    "push in", "pull out", "pull back", "tracking", "pan", "tilt", "orbit",
    "dolly", "crane", "handheld", "static", "locked", "rack focus",
    "推进", "拉远", "跟随", "环绕", "固定", "手持", "摇", "移",
    "锁定", "跟拍", "升降", "环绕", "镜头",
]
SOUND_KW = [
    "sound", "audio", "music", "silence", "silent", "quiet", "score",
    "音效", "配乐", "声音", "音乐", "静默", "环境音", "无音乐",
    "production audio", "no music", "no score",
]
NEGATION_PATTERNS = [
    r"no blur", r"no distortion", r"no artifacts", r"no extra fingers",
    r"no watermark", r"no text", r"无模糊", r"无畸变", r"无伪影",
    r"不要模糊", r"不要变形", r"无多余手指", r"无水印", r"无文字",
]
CONSTRAINT_MARKERS = ["约束", "constraint", "constraints", "无文字", "无水印"]

# ── Helpers ──────────────────────────────────────────────────
def find_slop(text: str) -> list[tuple[str, str]]:
    """Return list of (slop_word, replacement) found in text."""
    found = []
    lower = text.lower()
    for word, repl in SLOP_TABLE.items():
        # word-boundary match for single words; substring for phrases
        if " " in word:
            if word in lower:
                found.append((word, repl))
        else:
            if re.search(rf"\b{re.escape(word)}\b", lower):
                found.append((word, repl))
    return found


def has_keyword(text: str, keywords: list[str]) -> bool:
    lower = text.lower()
    return any(kw.lower() in lower for kw in keywords)


def find_negations_outside_constraints(text: str) -> list[str]:
    """Find negation phrases that appear outside a constraints section."""
    hits = []
    # Split into constraint vs non-constraint zones
    lower = text.lower()
    constraint_start = -1
    for marker in CONSTRAINT_MARKERS:
        idx = lower.find(marker.lower())
        if idx != -1 and (constraint_start == -1 or idx < constraint_start):
            constraint_start = idx
    non_constraint = text[:constraint_start] if constraint_start != -1 else text
    for pat in NEGATION_PATTERNS:
        if re.search(pat, non_constraint, re.IGNORECASE):
            hits.append(pat.replace("\\b", "").replace("r\"", "").strip('"'))
    return hits


def count_action_sentences(text: str) -> int:
    """Rough heuristic: count sentences with action/motion verbs."""
    action_verbs = (
        r"(walk|run|turn|reach|grab|lift|drop|push|pull|throw|catch|open|close|"
        r"rise|fall|spin|slide|roll|jump|stand|sit|enter|exit|cross|pass|"
        r"走|跑|转|拿|放|推|拉|扔|接|打开|关|升|降|旋转|滑|滚|跳|站|坐|进|出|穿|过|"
        r"涌|冲|飘|飞|落|涌|冲|扑|挥|踢|打|舞|摇|摆|伸|缩|抬|低|仰|俯)"
    )
    sentences = re.split(r"[。.！!？?\n]", text)
    count = 0
    for s in sentences:
        s = s.strip()
        if len(s) < 4:
            continue
        # skip camera/sound/constraint lines
        if re.search(r"(镜头|声音|约束|camera|sound|constraint|light|光线)", s, re.IGNORECASE):
            continue
        if re.search(action_verbs, s):
            count += 1
    return count


def word_count(text: str) -> int:
    """Count words (CJK chars count as 1 word each, latin words split by space)."""
    cjk = len(re.findall(r"[\u4e00-\u9fff\u3400-\u4dbf]", text))
    latin = len(re.findall(r"[a-zA-Z]+", text))
    return cjk + latin


# ── Main lint ────────────────────────────────────────────────
def lint(prompt: str) -> int:
    errors = warnings = infos = 0
    print(f"\n{CYN}{'='*60}")
    print(f"  Prompt Lint — Anti-Slop 提示词质量检查")
    print(f"{'='*60}{RST}\n")

    # 1. Slop words (ERROR)
    slops = find_slop(prompt)
    if slops:
        errors += len(slops)
        print(f"{RED}❌ [ERROR] 空话词 Slop words detected ({len(slops)}):{RST}")
        for w, r in slops:
            print(f"   {RED}\"{w}\"{RST} → {DIM}{r}{RST}")
    else:
        print(f"{GRN}✅ [PASS] 无空话词 No slop words{RST}")

    # 2. Missing light source (WARNING)
    if has_keyword(prompt, LIGHT_KW):
        print(f"{GRN}✅ [PASS] 光源已声明 Light source declared{RST}")
    else:
        warnings += 1
        print(f"{YEL}⚠️  [WARN] 缺少光源 Missing light source{RST}")
        print(f"   {DIM}添加具体光源：太阳/窗光/台灯/霓虹/烛光… (add a concrete light source){RST}")

    # 3. Missing camera movement (WARNING)
    if has_keyword(prompt, CAMERA_KW):
        print(f"{GRN}✅ [PASS] 镜头运动已声明 Camera movement declared{RST}")
    else:
        warnings += 1
        print(f"{YEL}⚠️  [WARN] 缺少镜头运动 Missing camera movement{RST}")
        print(f"   {DIM}添加镜头运动：推进/环绕/固定/手持… (add camera motion or 'static/锁定'){RST}")

    # 4. Missing sound (WARNING)
    if has_keyword(prompt, SOUND_KW):
        print(f"{GRN}✅ [PASS] 声音已声明 Sound declared{RST}")
    else:
        warnings += 1
        print(f"{YEL}⚠️  [WARN] 缺少声音设计 Missing sound design{RST}")
        print(f"   {DIM}添加声音：环境音/音效/配乐/静默… (add sound: ambient/SFX/music/silence){RST}")

    # 5. Negation outside constraints (WARNING)
    negs = find_negations_outside_constraints(prompt)
    if negs:
        warnings += len(negs)
        print(f"{YEL}⚠️  [WARN] 否定词在约束区外 Negation outside constraints ({len(negs)}):{RST}")
        for n in negs:
            print(f"   {YEL}\"{n}\"{RST} → {DIM}否定会召唤概念；描述存在的东西 (negation summons the concept; describe what IS there){RST}")
    else:
        print(f"{GRN}✅ [PASS] 否定词使用正确 Negation usage OK{RST}")

    # 6. Too many actions (WARNING)
    actions = count_action_sentences(prompt)
    if actions > 3:
        warnings += 1
        print(f"{YEL}⚠️  [WARN] 动作过多 Too many actions ({actions} sentences){RST}")
        print(f"   {DIM}一镜一拍：一个镜头 = 一个节拍 = 一个变化 (one shot = one beat = one change){RST}")
    else:
        print(f"{GRN}✅ [PASS] 动作密度合理 Action density OK ({actions} action sentences){RST}")

    # 7. Prompt length (INFO)
    wc = word_count(prompt)
    if wc > 150:
        infos += 1
        print(f"{CYN}ℹ️  [INFO] 提示词较长 Prompt length: {wc} words (>150){RST}")
        print(f"   {DIM}单片段建议 ≤150 词；考虑拆分 (consider splitting for a single clip){RST}")
    else:
        print(f"{GRN}✅ [PASS] 提示词长度 Prompt length: {wc} words{RST}")

    # ── Summary ──────────────────────────────────────────────
    total = errors + warnings + infos
    score = max(0, 100 - errors * 15 - warnings * 5 - infos * 1)
    print(f"\n{CYN}{'─'*60}")
    print(f"  评分 Score: {score}/100")
    print(f"  ❌ Errors: {errors}  ⚠️  Warnings: {warnings}  ℹ️  Info: {infos}")
    if score >= 90:
        print(f"  {GRN}优秀 Excellent — 可直接使用 ready to use{RST}")
    elif score >= 70:
        print(f"  {YEL}良好 Good — 建议修复警告 fix warnings for best results{RST}")
    else:
        print(f"  {RED}需改进 Needs work — 请修复错误 fix errors before generating{RST}")
    print(f"{'─'*60}{RST}\n")

    return 1 if errors > 0 else 0


# ── CLI ──────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Anti-Slop Prompt Lint — 提示词质量检查工具"
    )
    parser.add_argument("prompt", nargs="?", help="Prompt text to check")
    parser.add_argument("--file", "-f", help="Read prompt from a file")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as fh:
                prompt = fh.read().strip()
        except FileNotFoundError:
            print(f"{RED}Error: file not found: {args.file}{RST}", file=sys.stderr)
            sys.exit(2)
    elif args.prompt:
        prompt = args.prompt.strip()
    else:
        parser.print_help()
        sys.exit(2)

    if not prompt:
        print(f"{RED}Error: empty prompt{RST}", file=sys.stderr)
        sys.exit(2)

    sys.exit(lint(prompt))


if __name__ == "__main__":
    main()
