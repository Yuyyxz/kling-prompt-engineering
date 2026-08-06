#!/bin/bash
# 安装脚本 - 支持多平台安装

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 显示帮助信息
show_help() {
    echo "用法: $0 [平台] [选项]"
    echo ""
    echo "平台:"
    echo "  claude      安装到 Claude Code"
    echo "  cursor      安装到 Cursor"
    echo "  codex       安装到 Codex"
    echo "  windsurf    安装到 Windsurf"
    echo "  trae        安装到 Trae"
    echo "  qwen        安装到 Qwen Code"
    echo "  generic     安装到自定义目录"
    echo ""
    echo "选项:"
    echo "  -h, --help            显示帮助信息"
    echo "  -d, --dir             指定安装目录"
    echo "  --skip-validation     跳过验证脚本安装（默认安装）"
    echo "                        验证脚本用于 prompt 质量检查，普通用户可跳过"
    echo ""
    echo "示例:"
    echo "  $0 claude"
    echo "  $0 cursor --skip-validation"
    echo "  $0 generic -d ~/.custom/skills/"
}

# 检查依赖
check_dependencies() {
    if ! command -v curl &> /dev/null; then
        print_error "curl 未安装，请先安装 curl"
        exit 1
    fi
    
    if ! command -v mkdir &> /dev/null; then
        print_error "mkdir 未安装，请先安装 mkdir"
        exit 1
    fi
}

# 下载 Skill 文件
download_skills() {
    local install_dir=$1
    
    print_info "正在下载 Skill 文件..."
    
    # 创建目录
    mkdir -p "$install_dir"
    
    # 下载所有 .skill 文件（不递归，跳过 archive/ 等子目录）
    for skill_file in skills/*.skill; do
        if [ -f "$skill_file" ]; then
            filename=$(basename "$skill_file")
            print_info "下载 $filename..."
            curl -sL "https://raw.githubusercontent.com/Yuyyxz/kling-prompt-engineering/main/$skill_file" -o "$install_dir/$filename"
            print_success "下载完成: $filename"
        fi
    done
}

# ============================================================
# 验证脚本安装（可选）
# 这些脚本用于 prompt 质量检查（Anti-Slop 检测、语法验证等）。
# 普通用户只装 Skill 文件就够用了，可以用 --skip-validation 跳过。
# 适合需要批量校验 prompt 或做 CI 集成的进阶用户。
# ============================================================
download_scripts() {
    local install_dir=$1

    # 检查 scripts/ 目录是否存在
    if [ ! -d "scripts" ]; then
        print_warning "scripts/ 目录不存在，跳过验证脚本安装"
        return 0
    fi

    print_info "正在安装验证脚本（高级功能）..."

    local scripts_dir="$install_dir/scripts"
    mkdir -p "$scripts_dir"

    local found_scripts=0
    for script_file in scripts/*.py; do
        if [ -f "$script_file" ]; then
            filename=$(basename "$script_file")
            print_info "安装 $filename..."
            curl -sL "https://raw.githubusercontent.com/Yuyyxz/kling-prompt-engineering/main/$script_file" -o "$scripts_dir/$filename"
            found_scripts=1
        fi
    done

    if [ "$found_scripts" -eq 1 ]; then
        print_success "验证脚本已安装到: $scripts_dir"
        print_info "运行 python $scripts_dir/prompt_lint.py --help 查看用法"
    else
        print_warning "scripts/ 目录为空，无验证脚本可安装"
    fi
}

# 安装到 Claude Code
install_claude() {
    local install_dir="$HOME/.claude/skills"
    print_info "安装到 Claude Code..."
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 安装到 Cursor
install_cursor() {
    local install_dir="$HOME/.cursor/skills"
    print_info "安装到 Cursor..."
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 安装到 Codex
install_codex() {
    local install_dir="$HOME/.codex/skills"
    print_info "安装到 Codex..."
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 安装到 Windsurf
install_windsurf() {
    local install_dir="$HOME/.windsurf/skills"
    print_info "安装到 Windsurf..."
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 安装到 Trae
install_trae() {
    local install_dir="$HOME/.trae/skills"
    print_info "安装到 Trae..."
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 安装到 Qwen Code
install_qwen() {
    local install_dir="$HOME/.qwen/skills"
    print_info "安装到 Qwen Code..."
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 安装到自定义目录
install_generic() {
    local install_dir=$1
    if [ -z "$install_dir" ]; then
        print_error "请指定安装目录"
        show_help
        exit 1
    fi
    print_info "安装到自定义目录: $install_dir"
    download_skills "$install_dir"
    print_success "安装完成！Skill 文件已保存到: $install_dir"
}

# 主函数
main() {
    # 检查依赖
    check_dependencies
    
    # 解析参数
    local platform=""
    local custom_dir=""
    local skip_validation=0
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            claude|cursor|codex|windsurf|trae|qwen|generic)
                platform=$1
                shift
                ;;
            -d|--dir)
                custom_dir=$2
                shift 2
                ;;
            --skip-validation)
                skip_validation=1
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                print_error "未知参数: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # 如果没有指定平台，显示帮助
    if [ -z "$platform" ]; then
        show_help
        exit 1
    fi
    
    # 执行安装
    case $platform in
        claude)
            install_claude
            [ "$skip_validation" -eq 0 ] && download_scripts "$HOME/.claude/skills"
            ;;
        cursor)
            install_cursor
            [ "$skip_validation" -eq 0 ] && download_scripts "$HOME/.cursor/skills"
            ;;
        codex)
            install_codex
            [ "$skip_validation" -eq 0 ] && download_scripts "$HOME/.codex/skills"
            ;;
        windsurf)
            install_windsurf
            [ "$skip_validation" -eq 0 ] && download_scripts "$HOME/.windsurf/skills"
            ;;
        trae)
            install_trae
            [ "$skip_validation" -eq 0 ] && download_scripts "$HOME/.trae/skills"
            ;;
        qwen)
            install_qwen
            [ "$skip_validation" -eq 0 ] && download_scripts "$HOME/.qwen/skills"
            ;;
        generic)
            install_generic "$custom_dir"
            [ "$skip_validation" -eq 0 ] && download_scripts "$custom_dir"
            ;;
        *)
            print_error "不支持的平台: $platform"
            show_help
            exit 1
            ;;
    esac
    
    if [ "$skip_validation" -eq 1 ]; then
        print_info "已跳过验证脚本安装（--skip-validation）"
    fi
}

# 运行主函数
main "$@"
