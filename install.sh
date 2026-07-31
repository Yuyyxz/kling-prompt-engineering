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
    echo "  -h, --help  显示帮助信息"
    echo "  -d, --dir   指定安装目录"
    echo ""
    echo "示例:"
    echo "  $0 claude"
    echo "  $0 cursor"
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
    
    # 下载所有 .skill 文件
    for skill_file in skills/*.skill; do
        if [ -f "$skill_file" ]; then
            filename=$(basename "$skill_file")
            print_info "下载 $filename..."
            curl -sL "https://raw.githubusercontent.com/Yuyyxz/kling-prompt-engineering/main/$skill_file" -o "$install_dir/$filename"
            print_success "下载完成: $filename"
        fi
    done
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
            ;;
        cursor)
            install_cursor
            ;;
        codex)
            install_codex
            ;;
        windsurf)
            install_windsurf
            ;;
        trae)
            install_trae
            ;;
        qwen)
            install_qwen
            ;;
        generic)
            install_generic "$custom_dir"
            ;;
        *)
            print_error "不支持的平台: $platform"
            show_help
            exit 1
            ;;
    esac
}

# 运行主函数
main "$@"
