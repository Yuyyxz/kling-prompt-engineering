#!/usr/bin/env python3
"""
综合验证脚本 v2 — 同时覆盖 .skill (YAML) 和 .md 文件

用法:
  python scripts/validate_all.py            # 验证所有 .skill + .md
  python scripts/validate_all.py --skill-only  # 只验证 .skill
  python scripts/validate_all.py --md-only     # 只验证 .md
  python scripts/validate_all.py path/to/file  # 验证单个文件

只依赖 Python 标准库，不装第三方包。
"""

import sys
import os
import re
import yaml

# ─── 项目根目录 ───
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# ─── Anti-Slop 词表 ───
# 这些词出现在 09-anti-slop.md 的替换表里。作为正向风格词使用时 flagged。
SLOP_WORDS = [
    # 中文
    '电影感', '史诗感', '高级感', '氛围感', '震撼', '唯美',
    '超写实', '戏剧性', '魔幻感', '专业感', '视觉冲击力',
    '令人窒息的', '华丽的', '迷人的', '美感',
    # 英文（prompt 里常见）
    'cinematic', 'epic feel', 'epic sense', 'aesthetic feel',
]

# ═══════════════════════════════════════════════════════════
#  通用检查
# ═══════════════════════════════════════════════════════════

def check_trailing_newline(content):
    """文件末尾要有空行（POSIX 惯例，也避免 git diff 噪音）"""
    if content and not content.endswith('\n'):
        return False, "文件末尾缺空行"
    return True, ""


# ═══════════════════════════════════════════════════════════
#  Markdown 格式检查
# ═══════════════════════════════════════════════════════════

def check_heading_hierarchy(lines):
    """标题层级不跳级：# 之后可以直接 ## 或 ###，但不能直接 ####"""
    errors = []
    prev_level = 0
    for i, line in enumerate(lines, 1):
        m = re.match(r'^(#+)\s', line)
        if not m:
            continue
        level = len(m.group(1))
        if prev_level > 0 and level > prev_level + 1:
            errors.append(
                f"第 {i} 行: h{prev_level} → h{level}，跳了一级"
            )
        prev_level = level
    if errors:
        return False, "; ".join(errors)
    return True, ""


def check_code_blocks(lines):
    """代码块必须闭合：``` 开了就得关"""
    errors = []
    in_block = False
    block_start = 0
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```'):
            if not in_block:
                in_block = True
                block_start = i
            else:
                in_block = False
    if in_block:
        errors.append(f"第 {block_start} 行开的代码块没关")
    if errors:
        return False, "; ".join(errors)
    return True, ""


def check_table_format(lines):
    """
    表格格式检查：
    - 有 | 分隔的行，前后必须是表头+分隔行或另一个表格行
    - 分隔行必须匹配 |---|---| 模式
    """
    errors = []
    in_table = False
    table_start = 0
    separator_seen = False

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        is_table_row = bool(re.match(r'^\|.*\|', stripped))
        is_separator = bool(re.match(r'^\|[\s\-:|]+\|$', stripped))

        if is_table_row:
            if not in_table:
                in_table = True
                table_start = i
                separator_seen = False
            if is_separator:
                separator_seen = True
        else:
            if in_table:
                if not separator_seen:
                    errors.append(
                        f"第 {table_start} 行开始的表格缺分隔行 (|---|---|)"
                    )
                in_table = False

    # 文件末尾正好在表格里
    if in_table and not separator_seen:
        errors.append(
            f"第 {table_start} 行开始的表格缺分隔行 (|---|---|)"
        )

    if errors:
        return False, "; ".join(errors)
    return True, ""


# ═══════════════════════════════════════════════════════════
#  交叉引用检查
# ═══════════════════════════════════════════════════════════

def extract_references(content):
    """
    提取 .md 文件里对其他文件的引用。
    两种形式：
      1. Markdown 链接 [text](path/to/file.ext)
      2. 裸引用：正文里直接写 01-directing-engine.md 或 adapters/xxx.yaml
    """
    refs = []

    # ── Markdown 链接 ──
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        url = m.group(2)
        # 跳过纯锚点、外部链接、图片 base64
        if url.startswith('#') or url.startswith('http') or url.startswith('data:'):
            continue
        # 去掉锚点部分
        url = url.split('#')[0]
        if url:
            refs.append(url)

    # ── 裸引用 ──
    # 先把 markdown 链接替换掉，避免重复匹配
    stripped = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', ' ', content)
    # 去掉代码块内容（```...```），代码里的文件名不算引用
    stripped = re.sub(r'```[\s\S]*?```', ' ', stripped)
    # 去掉行内代码 `...`
    stripped = re.sub(r'`[^`]+`', ' ', stripped)

    # 匹配模式：至少含一个数字的文件名，可带路径前缀
    for m in re.finditer(
        r'(?:^|(?<=\s)|(?<=：)|(?<=:)|(?<=→)|(?<=（)|(?<=\())'
        r'((?:[a-zA-Z0-9_\-]+/)*'
        r'[a-zA-Z0-9_\-]*[0-9][a-zA-Z0-9_\-]*'
        r'(?:-[a-zA-Z0-9_\-]+)*'
        r'\.[a-zA-Z]{1,5})'
        r'(?=$|[\s）)\],;:，。；：、]|「)',
        stripped
    ):
        refs.append(m.group(1))

    return list(set(refs))


def resolve_reference(ref_path, source_file):
    """把引用路径解析成绝对路径，判断文件是否存在"""
    source_dir = os.path.dirname(source_file)

    # 相对当前文件所在目录
    candidate = os.path.normpath(os.path.join(source_dir, ref_path))
    if os.path.exists(candidate):
        return True

    # 相对项目根目录
    candidate = os.path.normpath(os.path.join(PROJECT_ROOT, ref_path))
    if os.path.exists(candidate):
        return True

    return False


def check_cross_references(content, file_path):
    """检查所有交叉引用是否指向真实存在的文件"""
    refs = extract_references(content)
    broken = []
    for ref in sorted(refs):
        if not resolve_reference(ref, file_path):
            broken.append(ref)
    if broken:
        return False, "断链: " + ", ".join(broken), broken
    return True, "", []


# ═══════════════════════════════════════════════════════════
#  Anti-Slop 检查
# ═══════════════════════════════════════════════════════════

def _is_slop_teaching_context(lines, line_idx, word):
    """
    判断某行某词是否在教学/否定语境里。
    教学语境 = 这个词在被讨论、被批评、被当反面教材，而不是被当正向风格词用。
    """
    line = lines[line_idx]

    line_lower = line.lower()
    word_lower = word.lower()

    # 找到 word 在 line 中的实际位置（大小写不敏感）
    pos = line_lower.find(word_lower)
    if pos < 0:
        return False
    pre = line[:pos]
    post = line[pos + len(word):]

    # ── 当前行检查 ──

    # 否定指令：别写/不要/禁止/避免/勿 + slop 词
    if re.search(r'(?:别写|不要|禁止|避免|勿|不用|别用|拒绝|少用|慎用|莫用)$', pre):
        return True

    # 替换箭头：slop 词 → 正确写法
    if re.search(re.escape(word) + r'.*(?:→|=>|改为|替换为|换成)', line, re.IGNORECASE):
        return True

    # 判断句："X 不是 Y" / "X 是 Y 不是 Z"
    if re.search(r'^(?:不是|是.*?不是)', post):
        return True

    # 引号包裹：在讨论这个词本身
    if re.search(
        r'["""\'\u2018\u2019\u300a\u300b]' + re.escape(word),
        pre[-3:] if len(pre) >= 3 else pre,
        re.IGNORECASE
    ):
        return True

    # 表格行（markdown table）：表格里 slop 词几乎都是反面教材或对照项
    if re.match(r'^\s*\|', line) and '|' in line[1:]:
        return True

    # 标题里提到 slop 词（讨论这个词）
    if re.match(r'^#+\s', line):
        return True

    # 冒号引入：「空话：电影感」这种
    if re.search(r'[:：]\s*$|[:：]\s*' + re.escape(word), pre, re.IGNORECASE):
        return True

    # ── 宽窗口检查（前后 3 行）──

    start = max(0, line_idx - 3)
    end = min(len(lines), line_idx + 4)
    window = '\n'.join(lines[start:end])

    # 替换表模式：「| 空话 | 替换为 |」表头附近
    if re.search(r'空话.*替换|替换.*空话', window):
        return True

    # 附近有否定指令
    for j in range(start, end):
        if j == line_idx:
            continue
        nearby = lines[j]
        if re.search(r'(?:别写|不要写|禁止使用|避免使用)', nearby):
            return True

    return False


def check_anti_slop(content, file_path):
    """
    检查是否在非教学语境里使用空话词。
    教学语境（09-anti-slop.md 本身、替换表、反面示例）不算违规。
    """
    lines = content.split('\n')
    violations = []

    # 教学文件：anti-slop 词典本身、本项目的 lexicon 参考
    basename = os.path.basename(file_path)
    if basename in ('09-anti-slop.md', 'anti_slop_lexicon.md'):
        return True, "", []

    for i, line in enumerate(lines):
        for word in SLOP_WORDS:
            if word.lower() not in line.lower():
                continue
            if _is_slop_teaching_context(lines, i, word):
                continue
            violations.append(f"第 {i+1} 行: 「{word}」作为正向词使用")

    if violations:
        return False, "; ".join(violations[:5]), violations
    return True, "", []


# ═══════════════════════════════════════════════════════════
#  .skill (YAML) 验证 — 保留原有逻辑
# ═══════════════════════════════════════════════════════════

def validate_yaml_format(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        return True, "YAML 格式正确"
    except yaml.YAMLError as e:
        return False, f"YAML 格式错误: {e}"
    except FileNotFoundError:
        return False, f"文件不存在: {file_path}"
    except Exception as e:
        return False, f"未知错误: {e}"


def validate_required_fields(file_path):
    REQUIRED_FIELDS = ["name", "version", "description", "philosophy"]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            return False, "文件内容不是有效的字典格式"
        missing = [f for f in REQUIRED_FIELDS if f not in data]
        if missing:
            return False, f"缺少必需字段: {', '.join(missing)}"
        return True, "所有必需字段都存在"
    except Exception as e:
        return False, f"验证失败: {e}"


def validate_naming_convention(name):
    return bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name))


def validate_version_format(version):
    return bool(re.match(r'^\d+\.\d+\.\d+$', version))


def validate_skill_file(file_path):
    """验证 .skill YAML 文件"""
    results = []

    # 1. YAML 格式
    ok, msg = validate_yaml_format(file_path)
    results.append(("YAML 格式", ok, msg))
    if not ok:
        return results

    # 2. 必需字段
    ok, msg = validate_required_fields(file_path)
    results.append(("必需字段", ok, msg))

    # 3. 命名规范
    name = os.path.splitext(os.path.basename(file_path))[0]
    ok = validate_naming_convention(name)
    results.append(("命名规范", ok, f"文件名: {name}"))

    # 4. 版本号
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if 'version' in data:
            ok = validate_version_format(data['version'])
            results.append(("版本号", ok, f"版本: {data['version']}"))
    except Exception:
        pass

    return results


# ═══════════════════════════════════════════════════════════
#  .md 验证（聚合所有检查）
# ═══════════════════════════════════════════════════════════

def validate_md_file(file_path):
    """验证 .md 文件：格式 + 交叉引用 + anti-slop"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    results = []

    # 1. 末尾空行
    ok, msg = check_trailing_newline(content)
    results.append(("末尾空行", ok, msg))

    # 2. 标题层级
    ok, msg = check_heading_hierarchy(lines)
    results.append(("标题层级", ok, msg))

    # 3. 代码块闭合
    ok, msg = check_code_blocks(lines)
    results.append(("代码块闭合", ok, msg))

    # 4. 表格格式
    ok, msg = check_table_format(lines)
    results.append(("表格格式", ok, msg))

    # 5. 交叉引用
    ok, msg, _ = check_cross_references(content, file_path)
    results.append(("交叉引用", ok, msg))

    # 6. Anti-Slop
    ok, msg, _ = check_anti_slop(content, file_path)
    results.append(("Anti-Slop", ok, msg))

    return results


# ═══════════════════════════════════════════════════════════
#  主流程
# ═══════════════════════════════════════════════════════════

def main():
    args = sys.argv[1:]

    skill_only = '--skill-only' in args
    md_only = '--md-only' in args
    args = [a for a in args if not a.startswith('--')]

    if skill_only and md_only:
        print("错误: --skill-only 和 --md-only 不能同时用")
        sys.exit(1)

    # ── 收集文件 ──
    files = []
    if args:
        for target in args:
            if os.path.isfile(target):
                files.append(target)
            elif os.path.isdir(target):
                for root, dirs, filenames in os.walk(target):
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    for fn in filenames:
                        fp = os.path.join(root, fn)
                        if fn.endswith('.skill') or fn.endswith('.md'):
                            files.append(fp)
            else:
                print(f"路径不存在: {target}")
                sys.exit(1)
    else:
        for root, dirs, filenames in os.walk(PROJECT_ROOT):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for fn in filenames:
                fp = os.path.join(root, fn)
                if fn.endswith('.skill') and not md_only:
                    files.append(fp)
                elif fn.endswith('.md') and not skill_only:
                    files.append(fp)

    if skill_only:
        files = [f for f in files if f.endswith('.skill')]
    elif md_only:
        files = [f for f in files if f.endswith('.md')]

    files.sort()

    if not files:
        print("没找到要验证的文件")
        sys.exit(1)

    # ── 逐个验证 ──
    total = len(files)
    passed = 0
    failed = 0

    print(f"开始验证 {total} 个文件...\n")

    for fp in files:
        rel = os.path.relpath(fp, PROJECT_ROOT)
        print(f"  {rel}")

        if fp.endswith('.skill'):
            results = validate_skill_file(fp)
        elif fp.endswith('.md'):
            results = validate_md_file(fp)
        else:
            print(f"    ?? 未知文件类型\n")
            continue

        file_ok = True
        for check_name, is_valid, message in results:
            mark = "OK" if is_valid else "FAIL"
            detail = f" — {message}" if message else ""
            print(f"    [{mark}] {check_name}{detail}")
            if not is_valid:
                file_ok = False

        if file_ok:
            passed += 1
        else:
            failed += 1
        print()

    # ── 总结 ──
    print("=" * 50)
    print(f"总计: {total}  |  通过: {passed}  |  失败: {failed}  |  通过率: {passed/total*100:.1f}%")

    if failed > 0:
        print(f"\n有 {failed} 个文件验证失败")
        sys.exit(1)
    else:
        print("\n全部通过")
        sys.exit(0)


if __name__ == "__main__":
    main()
