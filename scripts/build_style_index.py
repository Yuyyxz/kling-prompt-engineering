#!/usr/bin/env python3
"""把 24-prompt-library.md 的风格/氛围条目解析成结构化索引 data/styles.json。

md 是人读的源（编辑改 md），JSON 是机器读的派生索引（agent 按需取一条，
不用整篇加载 1600 多行）。改完 md 重跑本脚本即可；CI 会重跑并比对，
索引过期会报错。

条目格式约定（24 号文档）:
    ### A1. 砼核（Concretecore / 巨构混凝土）
    - **触发词**:...
    - **关键词**:...
    - **负面词**:...
    - **光线**:... / **色彩**:... / **构图**:... / **示例**:... / **适配**:...
氛围条目字段可能是 **触发**/**画面** 等变体，未知字段原样保留在 extra 里。

用法: python3 scripts/build_style_index.py [--check]
  --check 只校验索引与 md 同步，不写文件；不同步退出码 1。
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "24-prompt-library.md"
OUT = REPO / "data" / "styles.json"

FIELD_MAP = {
    "触发词": "trigger", "触发": "trigger",
    "关键词": "keywords", "负面词": "negative",
    "光线": "lighting", "色彩": "color", "构图": "composition",
    "示例": "example", "适配": "adapter_notes", "详见": "see_also",
    "画面": "visual", "声音": "sound", "氛围": "mood",
}
ENTRY_RE = re.compile(r"^###\s+([A-Z]+\d+)\.\s+(.+?)\s*$", re.M)
FIELD_RE = re.compile(r"^-\s+\*\*(.+?)\*\*\s*[:：]\s*(.*)$", re.M)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)


def parse(text):
    entries = []
    section = None
    # 按行扫描，记录每个条目所属的二级标题（部分）
    spans = []
    pos = 0
    current_section = None
    lines = text.splitlines(keepends=True)
    offsets = []
    off = 0
    for ln in lines:
        offsets.append(off)
        off += len(ln)
    sec_at = {}
    for i, ln in enumerate(lines):
        m = SECTION_RE.match(ln)
        if m:
            current_section = m.group(1)
        m2 = ENTRY_RE.match(ln)
        if m2:
            sec_at[offsets[i]] = current_section
    matches = list(ENTRY_RE.finditer(text))
    for idx, m in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[m.end():end]
        # 条目正文到下一个 ## 或文件尾为止
        cut = re.search(r"^##\s", body, re.M)
        if cut:
            body = body[:cut.start()]
        name = m.group(2)
        name_zh, name_en = name, None
        em = re.match(r"^(.*?)（(.+?)）", name)
        if em:
            name_zh, name_en = em.group(1).strip(), em.group(2).strip()
        entry = {
            "id": m.group(1),
            "section": sec_at.get(m.start()),
            "name_zh": name_zh,
            "name_en": name_en,
            "fields": {},
            "extra": {},
        }
        for fm in FIELD_RE.finditer(body):
            key, val = fm.group(1).strip(), fm.group(2).strip()
            target = FIELD_MAP.get(key)
            if target:
                entry["fields"][target] = val
            else:
                entry["extra"][key] = val
        kw = entry["fields"].get("keywords")
        if kw:
            entry["keywords_list"] = [k.strip() for k in re.split(r"[,，]", kw) if k.strip()]
        entries.append(entry)
    return entries


def main():
    check = "--check" in sys.argv
    entries = parse(SRC.read_text(encoding="utf-8"))
    payload = {
        "source": "24-prompt-library.md",
        "generated_by": "scripts/build_style_index.py",
        "count": len(entries),
        "entries": entries,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=1) + "\n"
    if check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != rendered:
            print("[FAIL] data/styles.json 与 24-prompt-library.md 不同步，重跑 scripts/build_style_index.py")
            return 1
        print(f"[ok] styles.json 与源文档同步（{len(entries)} 条）")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")
    print(f"[ok] 已生成 {OUT.relative_to(REPO)}：{len(entries)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
