#!/usr/bin/env python3
"""T2I Generate — 文生图提示词生成器（创意意图 → 三模型 prompt）

读 adapters/t2i_adapter.yaml 的翻译规则，把一句创意意图翻译成
Kolors / Qwen Image 3 Pro / Seedream 5.0 各自格式的 prompt。

Usage:
    python scripts/t2i_generate.py "深夜便利店窗前一个年轻人捧着热咖啡"
    python scripts/t2i_generate.py --model qwen "雨夜，女孩在霓虹灯下回头"
    python scripts/t2i_generate.py --model all --check "..."   # 生成 + lint

原理：这不是 LLM 改写，是结构化翻译。
  - 拆创意意图 → 主体/场景/光线/风格
  - 按模型脾气套格式（Kolors 精简 / Qwen 全展开 / Seedream 七要素）
  - 缺要素时明确提示，不编造
"""
import argparse
import os
import re
import sys

# ── ANSI colors ──────────────────────────────────────────────
RED, YEL, GRN, CYN, DIM, RST = "\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[2m", "\033[0m"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ADAPTER_PATH = os.path.join(PROJECT_ROOT, "adapters", "t2i_adapter.yaml")

# ── 内嵌规则（yaml 缺失时兜底；与 t2i_adapter.yaml 保持一致）──
RULES = {
    "kolors": {
        "meta": "精简到骨头——中文短句，质量后缀收尾",
        "quality": "高清, 精细, 专业品质",
        "camera": None,  # Kolors 对镜头不敏感，不写
        "lighting": "用一个词：暖色光 / 冷色光 / 自然光",
        "negative": "独立 negative prompt 参数提交",
        "length": "80-120 字中文",
    },
    "qwen": {
        "meta": "展开所有细节——风格标签开头，相机镜头写上去",
        "quality": None,  # 细节描述本身就是质量，不需要质量后缀
        "camera": "Sony Venice 拍摄，85mm f/1.2，浅景深",
        "lighting": "光源方向 + 色温 + 环境反射 + 光晕效果（全展开）",
        "negative": "negative_prompt 参数（≤500 字符）",
        "length": "150-250 词",
    },
    "seedream": {
        "meta": "套 7 要素模板——一行一个要素，不省不混",
        "quality": "质量：高清，毛孔可见，自然肤质",
        "camera": "风格：写实摄影，电影质感",
        "lighting": "光线：[光源]从[方向]照射，环境[色温]光，[冷暖关系]",
        "negative": "写在约束要素里",
        "length": "7 要素齐全即可",
    },
}

SEEDREAM_TEMPLATE = """主体：{subject}
细节：{detail}
动作：{action}
环境：{setting}
风格：写实摄影，{style}质感
光线：{lighting}
质量：高清，{quality_detail}
约束：无文字，无水印，{constraint}"""

# ── 创意意图解析 ─────────────────────────────────────────────

def parse_intent(intent: str) -> dict:
    """拆创意意图 → 主体/场景/光线/风格。拆不到的标 None，不编造。"""
    parts = {
        "subject": None,   # 谁/什么
        "setting": None,   # 在哪
        "lighting": None,  # 光
        "style": None,     # 风格
        "action": None,    # 在做什么
    }

    # 主体：优先找"一个/一位/一名/个"开头的名词短语
    # 例："一个穿连帽衫的年轻人捧着热咖啡" → "一个穿连帽衫的年轻人"
    m = re.search(r'((?:一个|一位|一名|个)[^，。,]{2,18}?)(?:站|坐|躺|走|穿|拿|捧|举|看|望|回头|转身|低头|抬头|靠|在)', intent)
    if m:
        parts["subject"] = m.group(1).strip()
    if not parts["subject"]:
        # 兜底：第一句话的主语
        m = re.match(r'^(.{2,20}?)(?:站|坐|躺|走|穿|拿|捧|举|看|在|于|背对|面对)', intent)
        if m:
            parts["subject"] = m.group(1).strip()

    # 场景：地点词
    place_kw = ["便利店", "房间", "街道", "城市", "海边", "森林", "沙漠", "建筑",
                "窗", "桥", "巷", "山", "湖", "市场", "屋顶", "花园", "废墟",
                "studio", "street", "room", "city", "beach", "forest", "desert"]
    for kw in place_kw:
        if kw in intent:
            parts["setting"] = kw
            break

    # 光线：优先具体词（灯光/阳光/霓虹/烛光/月光），避免单字"光"
    light_kw = ["灯光", "阳光", "霓虹", "烛光", "月光", "路灯", "黄昏", "黎明",
                "日光", "窗光", "晨光", "夕光",
                "neon", "sunlight", "moonlight", "candle", "dawn", "dusk"]
    for kw in light_kw:
        if kw in intent:
            parts["lighting"] = kw
            break
    if not parts["lighting"]:
        for kw in ["光", "light", "sun"]:
            if kw in intent:
                parts["lighting"] = kw
                break

    # 风格
    style_kw = ["写实", "胶片", "日系", "港风", "水墨", "油画", "赛博", "国风",
                "realistic", "film", "cinematic", "cyberpunk", "ink", "oil"]
    for kw in style_kw:
        if kw in intent:
            parts["style"] = kw
            break

    # 动作：动词短句（捧/看/走/回头/转身/拿…）
    m = re.search(r'((?:捧|拿|举|看|走|跑|回头|转身|低头|抬头|靠|坐|站)[^，。]{1,10})', intent)
    if m:
        parts["action"] = m.group(1).strip()

    return parts


def check_intent(parts: dict) -> list:
    """完整性检查：缺哪个要素提示哪个，不自动补。"""
    missing = []
    if not parts["subject"]:
        missing.append("主体（谁/什么，一句话讲清楚）")
    if not parts["setting"]:
        missing.append("场景（在哪，什么环境）")
    if not parts["lighting"]:
        missing.append("光线（光源/方向/色温）")
    return missing


# ── 各模型 prompt 组装 ───────────────────────────────────────

def build_kolors(parts: dict, intent: str) -> str:
    body = intent.rstrip("。，, ")
    return f"{body}。\n{RULES['kolors']['quality']}。"


def build_qwen(parts: dict, intent: str) -> str:
    subject = parts["subject"] or "主体"
    setting = parts["setting"] or "场景"
    lighting = parts["lighting"] or "光线"
    style = parts["style"] or "写实"
    camera = RULES["qwen"]["camera"]
    return (
        f"<photography> {intent}。\n"
        f"{subject}为主体，位于{setting}中，{lighting}为主要光源。\n"
        f"{camera}，中景，背景自然虚化。\n"
        f"整体风格：{style}，细节层次丰富，色彩自然。"
    )


def build_seedream(parts: dict, intent: str) -> str:
    subject = parts["subject"] or "主体"
    setting = parts["setting"] or "场景"
    lighting = parts["lighting"] or "光源"
    style = parts["style"] or "写实"
    action = parts["action"] or "静止"
    detail = "肤质自然，布料纹理可见" if "人" in subject or "女孩" in subject or "男孩" in subject else "材质纹理清晰"
    constraint = "无其他人物" if "人" in subject or "女孩" in subject or "男孩" in subject else "无人物"
    return SEEDREAM_TEMPLATE.format(
        subject=subject,
        detail=detail,
        action=action,
        setting=setting,
        style=style,
        lighting=f"{lighting}从[方向]照射，环境[色温]光，[冷暖关系]",
        quality_detail=detail,
        constraint=constraint,
    )


# ── 输出 ─────────────────────────────────────────────────────

def generate(intent: str, model: str = "all") -> int:
    parts = parse_intent(intent)
    missing = check_intent(parts)

    print(f"\n{CYN}{'='*60}")
    print(f"  T2I Generate — 文生图提示词生成器")
    print(f"{'='*60}{RST}\n")
    print(f"{DIM}创意意图：{intent}{RST}")

    # 完整性检查
    if missing:
        print(f"\n{YEL}⚠️  创意意图缺要素（不自动补，请补充后重跑）：{RST}")
        for m in missing:
            print(f"   {YEL}- {m}{RST}")
    else:
        print(f"\n{GRN}✅ 要素完整：主体/场景/光线 齐全{RST}")
    if parts["style"]:
        print(f"{DIM}  识别风格：{parts['style']}{RST}")
    else:
        print(f"{DIM}  未识别风格（可选：写实/胶片/日系/港风/水墨/油画/赛博）{RST}")

    # 模型输出
    targets = ["kolors", "qwen", "seedream"] if model == "all" else [model]
    for m in targets:
        print(f"\n{CYN}{'─'*60}")
        print(f"  {GRN}{m.upper()}{RST} — {DIM}{RULES[m]['meta']}{RST}")
        print(f"{'─'*60}{RST}")
        if m == "kolors":
            print(build_kolors(parts, intent))
        elif m == "qwen":
            print(build_qwen(parts, intent))
        else:
            print(build_seedream(parts, intent))
        print(f"\n{DIM}规则提示：")
        for k, v in RULES[m].items():
            if v and k not in ("meta",):
                print(f"  {k}: {v}")
        print(f"{RST}")

    # 结尾建议
    print(f"{CYN}{'─'*60}")
    print(f"  下一步：")
    print(f"  1. 用 prompt_lint 质检：python scripts/prompt_lint.py --mode t2i \"<生成的prompt>\"")
    print(f"  2. 需要分镜首帧 → 23-first-last-frame.md 的 T2I 生成首帧 6 步流程")
    print(f"  3. 完整方法论 → 22-text-to-image.md | 模型适配 → adapters/t2i_adapter.yaml")
    print(f"{'─'*60}{RST}\n")

    return 1 if missing else 0


# ── CLI ──────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="T2I Generate — 文生图提示词生成器（创意意图 → Kolors/Qwen/Seedream prompt）"
    )
    parser.add_argument("intent", help="一句话创意意图，例如：深夜便利店窗前一个年轻人捧着热咖啡")
    parser.add_argument(
        "--model", "-m", choices=["kolors", "qwen", "seedream", "all"], default="all",
        help="生成哪个模型的 prompt（默认 all 三个都出）"
    )
    args = parser.parse_args()

    intent = args.intent.strip()
    if not intent:
        print(f"{RED}Error: 创意意图不能为空{RST}", file=sys.stderr)
        sys.exit(2)

    sys.exit(generate(intent, model=args.model))


if __name__ == "__main__":
    main()
