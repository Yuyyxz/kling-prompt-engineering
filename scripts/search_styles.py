#!/usr/bin/env python3
"""按关键词/ID 检索风格库，只取需要的条目，不整篇加载 24 号文档。

用法:
    python3 scripts/search_styles.py 砼核
    python3 scripts/search_styles.py cyberpunk --field keywords
    python3 scripts/search_styles.py A5 --exact-id
    python3 scripts/search_styles.py 雨夜 --json

匹配范围: id / 中英文名 / 触发词 / 关键词 / 示例。默认输出人读格式。
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX = REPO / "data" / "styles.json"
LABELS = [
    ("trigger", "触发词"), ("keywords", "关键词"), ("negative", "负面词"),
    ("lighting", "光线"), ("color", "色彩"), ("composition", "构图"),
    ("example", "示例"), ("adapter_notes", "适配"), ("see_also", "详见"),
    ("visual", "画面"), ("sound", "声音"), ("mood", "氛围"),
]


def main():
    ap = argparse.ArgumentParser(description="检索风格库（data/styles.json）")
    ap.add_argument("query")
    ap.add_argument("--exact-id", action="store_true", help="按条目 ID 精确匹配，如 A5")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    data = json.loads(INDEX.read_text(encoding="utf-8"))
    q = args.query.lower()
    hits = []
    for e in data["entries"]:
        f = e["fields"]
        if args.exact_id:
            ok = e["id"].lower() == q
        else:
            hay = " ".join([
                e["id"], e.get("name_zh") or "", e.get("name_en") or "",
                f.get("trigger", ""), f.get("keywords", ""), f.get("example", ""),
            ]).lower()
            ok = q in hay
        if ok:
            hits.append(e)
    hits = hits[: args.limit]
    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
        return 0 if hits else 1
    if not hits:
        print(f"没有匹配「{args.query}」的条目（索引共 {data['count']} 条）")
        return 1
    for e in hits:
        title = e["name_zh"] + (f"（{e['name_en']}）" if e.get("name_en") else "")
        print(f"\n### {e['id']}. {title}  [{e.get('section') or ''}]")
        for key, label in LABELS:
            if e["fields"].get(key):
                print(f"- {label}: {e['fields'][key]}")
        for k, v in e.get("extra", {}).items():
            print(f"- {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
