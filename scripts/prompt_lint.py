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
    "street light", "glow", "beam", "ray", "shaft", "bloom", "flare",
    "practical", "ambient light", "key light", "fill", "sunlight", "daylight",
    "太阳", "自然光", "侧光", "逆光", "窗光", "霓虹",
    "烛光", "台灯", "月光", "路灯", "光线", "光源", "light",
    "天光", "微光", "光柱", "光斑", "光束", "光晕", "散射",
    "冷光", "暖光", "日光", "晨光", "夕光", "火光", "灯光",
    "反光", "高光", "荧光", "磷光", "光",
    # 中文光源补充（修复中文示例检测不全）
    "夕阳", "斜照", "阳光", "晨雾", "薄雾", "雾", "晨光", "暮色",
    "余晖", "朝阳", "日出", "日落", "黄昏", "黎明", "正午", "天光",
    "灯", "照明", "星", "星空", "极光", "反照", "映照", "透光",
    "光透", "光洒", "光落", "明", "暗", "亮",
]
CAMERA_KW = [
    "push in", "pull out", "pull back", "tracking", "pan", "tilt", "orbit",
    "dolly", "crane", "handheld", "static", "locked", "rack focus",
    "推进", "拉远", "跟随", "环绕", "固定", "手持", "摇", "移",
    "锁定", "跟拍", "升降", "环绕", "镜头",
]
SOUND_KW = [
    "sound", "audio", "music", "silence", "silent", "quiet", "score",
    "drone", "hum", "echo", "rumble", "roar", "tick", "drip", "whistle",
    "howl", "creak", "splash", "thunder", "rain", "breathing", "footstep",
    "ambient", "noise", "ringing", "buzz", "crackle", "rustle", "clank",
    "音效", "配乐", "声音", "音乐", "静默", "环境音", "无音乐",
    "production audio", "no music", "no score",
    "回响", "嗡鸣", "风声", "水滴", "鹰啸", "滴答", "呼吸声", "脚步声",
    "轰鸣", "咆哮", "鸟鸣", "蝉鸣", "雷声", "雨声", "浪声", "潮汐",
    "引擎", "电机", "嗡", "鸣", "啸", "响", "声",
]
NEGATION_PATTERNS = [
    r"no blur", r"no distortion", r"no artifacts", r"no extra fingers",
    r"no watermark", r"no text", r"无模糊", r"无畸变", r"无伪影",
    r"不要模糊", r"不要变形", r"无多余手指", r"无水印", r"无文字",
]
CONSTRAINT_MARKERS = ["约束", "constraint", "constraints", "无文字", "无水印"]

# ── T2I 特有关键词 ───────────────────────────────────────────
# 景别/角度骨架（图片 prompt 基本结构）
SHOT_KW = [
    "特写", "近景", "中景", "远景", "极远景", "微距", "全景",
    "仰拍", "俯拍", "平视", "侧面", "正面", "背面", "四分之三",
    "close-up", "close up", "macro", "wide shot", "low angle",
    "high angle", "eye level", "over-the-shoulder", "profile",
    "景别", "角度", "构图",
]
# 相机锚定（真实相机型号 + 镜头参数）
CAMERA_MODEL_KW = [
    "arri", "alexa", "sony", "venice", "canon", "fujifilm", "leica",
    "kodak", "nikon", "hasselblad", "phase one", "red camera",
    "panavision", "cinema camera", "dslr", "mirrorless",
    "35mm", "50mm", "85mm", "135mm", "24mm", "28mm", "105mm",
    "f/1.4", "f/1.8", "f/2.8", "f/4", "f/8", "f/11", "f/16",
    "光圈", "焦段", "mm 镜头", "胶片", "portra", "ektar", "velvia",
    "xtrans", "cmos", "full frame", "aps-c",
]

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


def detect_multi_shot(text: str) -> list[str]:
    """Detect multi-shot/timeline format and split into shot segments.
    Returns list of shot text segments. Empty list = not multi-shot."""
    # Pattern: "0-3秒画面：" or "3-7秒画面：" or "0-3s：" etc.
    timeline_pat = r"\d+\s*[-–~到]\s*\d+\s*秒(画面|镜头)?[：:]"
    # Pattern: "Shot 1:" or "镜头1：" or "S1:"
    shot_pat = r"(?:Shot\s*\d+|镜头\s*\d+|S\d+)\s*[：:]"
    
    if re.search(timeline_pat, text):
        # Split by timeline markers
        parts = re.split(timeline_pat, text)
        # First part is the header/style description, rest are shots
        shots = [p.strip() for p in parts[1:] if p.strip()]
        return shots if len(shots) >= 2 else []
    elif re.search(shot_pat, text, re.IGNORECASE):
        parts = re.split(shot_pat, text, flags=re.IGNORECASE)
        shots = [p.strip() for p in parts[1:] if p.strip()]
        return shots if len(shots) >= 2 else []
    return []


def count_action_sentences(text: str) -> int:
    """Count action sentences. For multi-shot prompts, return max per shot."""
    action_verbs = (
        r"(walk|run|turn|reach|grab|lift|drop|push|pull|throw|catch|open|close|"
        r"rise|fall|spin|slide|roll|jump|stand|sit|enter|exit|cross|pass|"
        r"走|跑|转|拿|放|推|拉|扔|接|打开|关|升|降|旋转|滑|滚|跳|站|坐|进|出|穿|过|"
        r"涌|冲|飘|飞|落|涌|冲|扑|挥|踢|打|舞|摇|摆|伸|缩|抬|低|仰|俯|"
        r"停|抬头|低头|转身|回头|迈步|跨|攀|爬|蹲|跪|躺|靠)"
    )
    
    def _count_in_segment(segment: str) -> int:
        sentences = re.split(r"[。.！!？?\n]", segment)
        count = 0
        for s in sentences:
            s = s.strip()
            if len(s) < 4:
                continue
            # skip camera/sound/constraint/style lines
            if re.search(r"(镜头|声音|约束|camera|sound|constraint|light|光线|配乐|音效|Shot on|Simulated)", s, re.IGNORECASE):
                continue
            if re.search(action_verbs, s):
                count += 1
        return count
    
    # Check if multi-shot
    shots = detect_multi_shot(text)
    if shots:
        # Return the MAX actions in any single shot (each shot should be ≤3)
        per_shot = [_count_in_segment(s) for s in shots]
        return max(per_shot) if per_shot else 0
    
    # Single shot: return total
    return _count_in_segment(text)


def word_count(text: str) -> int:
    """Count words (CJK chars count as 1 word each, latin words split by space)."""
    cjk = len(re.findall(r"[\u4e00-\u9fff\u3400-\u4dbf]", text))
    latin = len(re.findall(r"[a-zA-Z]+", text))
    return cjk + latin


# ── Main lint ────────────────────────────────────────────────
def lint(prompt: str, mode: str = "t2v") -> int:
    errors = warnings = infos = 0
    mode_label = "文生图 T2I" if mode == "t2i" else "文生视频 T2V"
    print(f"\n{CYN}{'='*60}")
    print(f"  Prompt Lint — Anti-Slop 提示词质量检查 ({mode_label})")
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

    if mode == "t2i":
        # ── T2I 模式：图片特有检查 ──
        # 3a. 景别/角度骨架 (WARNING)
        if has_keyword(prompt, SHOT_KW):
            print(f"{GRN}✅ [PASS] 景别/角度已声明 Shot framing declared{RST}")
        else:
            warnings += 1
            print(f"{YEL}⚠️  [WARN] 缺少景别/角度 Missing shot framing{RST}")
            print(f"   {DIM}图片 prompt 基本骨架：特写/中景/远景 + 仰拍/俯拍/平视 (shot size + angle){RST}")

        # 4a. 相机锚定 (WARNING)
        if has_keyword(prompt, CAMERA_MODEL_KW):
            print(f"{GRN}✅ [PASS] 相机锚定已声明 Camera anchor declared{RST}")
        else:
            warnings += 1
            print(f"{YEL}⚠️  [WARN] 缺少相机锚定 Missing camera anchor{RST}")
            print(f"   {DIM}真实相机型号比\"电影感\"有效 10 倍：Sony Venice + 85mm f/1.2 (real camera model){RST}")

        # 5a. 负面提示词 (INFO)
        if has_keyword(prompt, ["negative", "负面", "避免", "不要"]):
            print(f"{GRN}✅ [PASS] 负面提示词已考虑 Negative prompt considered{RST}")
        else:
            infos += 1
            print(f"{CYN}ℹ️  [INFO] 未提及负面提示词 Negative prompt not mentioned{RST}")
            print(f"   {DIM}写实人像建议加负面：塑料感/畸变/多余手指 (plastic skin, distortion){RST}")
    else:
        # ── T2V 模式：视频特有检查 ──
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

        # 6. Too many actions (WARNING)
        actions = count_action_sentences(prompt)
        if actions > 3:
            warnings += 1
            print(f"{YEL}⚠️  [WARN] 动作过多 Too many actions ({actions} sentences){RST}")
            print(f"   {DIM}一镜一拍：一个镜头 = 一个节拍 = 一个变化 (one shot = one beat = one change){RST}")
        else:
            print(f"{GRN}✅ [PASS] 动作密度合理 Action density OK ({actions} action sentences){RST}")

    # 5. Negation outside constraints (WARNING)
    negs = find_negations_outside_constraints(prompt)
    if negs:
        warnings += len(negs)
        print(f"{YEL}⚠️  [WARN] 否定词在约束区外 Negation outside constraints ({len(negs)}):{RST}")
        for n in negs:
            print(f"   {YEL}\"{n}\"{RST} → {DIM}否定会召唤概念；描述存在的东西 (negation summons the concept; describe what IS there){RST}")
    else:
        print(f"{GRN}✅ [PASS] 否定词使用正确 Negation usage OK{RST}")

    # 7. Prompt length (INFO)
    wc = word_count(prompt)
    if mode == "t2i":
        limit = 150
        opt = "80-150 词（中文 120-200 字）"
    else:
        limit = 150
        opt = "≤150 词；单片段建议拆分"
    if wc > limit:
        infos += 1
        print(f"{CYN}ℹ️  [INFO] 提示词较长 Prompt length: {wc} words (>{limit}){RST}")
        print(f"   {DIM}{opt}{RST}")
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
    parser.add_argument(
        "--mode", "-m", choices=["t2v", "t2i"], default="t2v",
        help="检查模式：t2v=文生视频（默认） t2i=文生图"
    )
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

    sys.exit(lint(prompt, mode=args.mode))


if __name__ == "__main__":
    main()
