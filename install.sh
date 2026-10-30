#!/bin/bash
# 安装脚本 — 安装标准技能目录（skills/<name>/SKILL.md + references/）
#
# 变更（2026-10-30）：旧版遍历下载 skills/*.skill 文件，那是 legacy 自定义
# 格式，没有 AI 工具会原生加载。新版安装标准技能目录，整目录复制，
# references/ 里的详细数据跟着一起走（渐进加载靠这个目录结构）。
#
# 来源优先级：
#   1. 脚本所在目录就是仓库克隆时，直接用本地 skills/，不联网
#   2. 否则 git clone --depth 1 拉仓库到临时目录再复制
# git 不可用时报错说明，不再用逐文件 curl 拼凑（拼不齐目录结构）。

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info()    { echo -e "${BLUE}ℹ️  $1${NC}"; }
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_error()   { echo -e "${RED}❌ $1${NC}"; }

REPO_URL="https://github.com/Yuyyxz/kling-prompt-engineering.git"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR=""
TMP_CLONE=""

cleanup() { if [ -n "$TMP_CLONE" ]; then rm -rf "$TMP_CLONE"; fi; }
trap cleanup EXIT

show_help() {
    echo "用法: $0 [平台] [选项]"
    echo ""
    echo "平台:"
    echo "  claude      安装到 Claude Code (~/.claude/skills)"
    echo "  cursor      安装到 Cursor (~/.cursor/skills)"
    echo "  codex       安装到 Codex (~/.codex/skills)"
    echo "  windsurf    安装到 Windsurf (~/.windsurf/skills)"
    echo "  trae        安装到 Trae (~/.trae/skills)"
    echo "  qwen        安装到 Qwen Code (~/.qwen/skills)"
    echo "  generic     安装到自定义目录（需 -d）"
    echo ""
    echo "选项:"
    echo "  -h, --help            显示帮助"
    echo "  -d, --dir <dir>       自定义安装目录（generic 用）"
    echo "  --skip-validation     跳过验证脚本安装（默认安装）"
    echo ""
    echo "只安装已迁移的标准技能目录（内含 SKILL.md 的目录）。"
    echo "未迁移的 legacy .skill 文件不会被安装，它们没有工具能原生加载；"
    echo "迁移进度见 skills/README.md。"
    echo ""
    echo "示例:"
    echo "  $0 claude"
    echo "  $0 cursor --skip-validation"
    echo "  $0 generic -d ~/.custom/skills/"
}

# 决定技能来源：本地克隆优先，否则浅克隆
resolve_source() {
    if [ -d "$SCRIPT_DIR/skills" ] && ls "$SCRIPT_DIR/skills"/*/SKILL.md >/dev/null 2>&1; then
        SRC_DIR="$SCRIPT_DIR"
        print_info "使用本地仓库: $SRC_DIR"
        return 0
    fi
    if ! command -v git >/dev/null 2>&1; then
        print_error "找不到本地 skills/，且 git 未安装，无法拉取仓库。"
        print_error "请先 git clone $REPO_URL 后在仓库内运行本脚本。"
        exit 1
    fi
    TMP_CLONE="$(mktemp -d)"
    print_info "正在拉取仓库..."
    git clone --depth 1 -q "$REPO_URL" "$TMP_CLONE/repo"
    SRC_DIR="$TMP_CLONE/repo"
}

# 复制所有标准技能目录到目标目录
install_skills() {
    local install_dir=$1
    mkdir -p "$install_dir"
    local count=0
    for skill_dir in "$SRC_DIR/skills"/*/; do
        [ -f "${skill_dir}SKILL.md" ] || continue
        local name
        name="$(basename "$skill_dir")"
        rm -rf "$install_dir/$name"
        cp -R "$skill_dir" "$install_dir/$name"
        print_info "已安装 $name"
        count=$((count + 1))
    done
    if [ "$count" -eq 0 ]; then
        print_error "来源里没有找到任何标准技能目录，安装中止。"
        exit 1
    fi
    print_success "共安装 $count 个技能到: $install_dir"
}

# 验证脚本（可选）：从来源的 scripts/ 整目录复制关键脚本
install_scripts() {
    local install_dir=$1
    if [ ! -d "$SRC_DIR/scripts" ]; then
        print_warning "来源里没有 scripts/，跳过验证脚本安装"
        return 0
    fi
    local scripts_dir="$install_dir/scripts"
    mkdir -p "$scripts_dir"
    local found=0
    for f in prompt_lint.py validate_storyboard.py adapt_prompt.py build_style_index.py search_styles.py retake_report.py; do
        if [ -f "$SRC_DIR/scripts/$f" ]; then
            cp "$SRC_DIR/scripts/$f" "$scripts_dir/$f"
            found=1
        fi
    done
    if [ "$found" -eq 1 ]; then
        print_success "验证脚本已安装到: $scripts_dir"
    else
        print_warning "scripts/ 里没有可安装的验证脚本"
    fi
}

main() {
    local platform=""
    local custom_dir=""
    local skip_validation=0

    while [[ $# -gt 0 ]]; do
        case $1 in
            claude|cursor|codex|windsurf|trae|qwen|generic)
                platform=$1; shift ;;
            -d|--dir)
                custom_dir=$2; shift 2 ;;
            --skip-validation)
                skip_validation=1; shift ;;
            -h|--help)
                show_help; exit 0 ;;
            *)
                print_error "未知参数: $1"; show_help; exit 1 ;;
        esac
    done

    if [ -z "$platform" ]; then
        show_help; exit 1
    fi

    local install_dir=""
    case $platform in
        claude)   install_dir="$HOME/.claude/skills" ;;
        cursor)   install_dir="$HOME/.cursor/skills" ;;
        codex)    install_dir="$HOME/.codex/skills" ;;
        windsurf) install_dir="$HOME/.windsurf/skills" ;;
        trae)     install_dir="$HOME/.trae/skills" ;;
        qwen)     install_dir="$HOME/.qwen/skills" ;;
        generic)
            if [ -z "$custom_dir" ]; then
                print_error "generic 需要 -d 指定目录"; show_help; exit 1
            fi
            install_dir="$custom_dir" ;;
    esac

    print_info "安装到 $platform: $install_dir"
    resolve_source
    install_skills "$install_dir"
    if [ "$skip_validation" -eq 0 ]; then
        install_scripts "$install_dir"
    else
        print_info "已跳过验证脚本安装（--skip-validation）"
    fi
    print_success "安装完成"
}

main "$@"
