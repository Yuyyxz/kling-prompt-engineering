#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════
#  KPE 文本→视频 完整流水线（Text-to-Video Pipeline）
#
#  用法:
#    bash workflows/text-to-video.sh "你的故事一句话" [--duration 5] [--mode t2v]
#
#  流程:
#    1. 分镜图生成   → 调用导演引擎 (skills/director-engine.skill)
#    2. prompt 质检  → prompt_lint.py (Anti-Slop/光源/运镜/声音)
#    3. 多模型适配   → 按目标模型转换 (adapters/)
#    4. 首帧生成     → t2i_generate.py (可选)
#    5. 输出交付     → 最终 prompt + 质检报告
#
#  前置: python3 + 项目 scripts/ 在 PATH 或同目录
# ═══════════════════════════════════════════════════════════
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS="$ROOT/scripts"
# Windows/MSYS: bash 的 /c/... 路径要转成 C:/... 才能给 Windows Python
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*)
    SCRIPTS_WIN="$(echo "$SCRIPTS" | sed 's|^/\([a-zA-Z]\)/|\1:/|')"
    ;;
  *)
    SCRIPTS_WIN="$SCRIPTS"
    ;;
esac
TMPDIR="${TMPDIR:-/tmp}/kpe-pipeline-$$"
mkdir -p "$TMPDIR"

# ─── 参数解析 ─────────────────────────────────────────────
STORY=""
DURATION=5
MODE="t2v"
MODEL="kling"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --duration) DURATION="$2"; shift 2 ;;
    --mode) MODE="$2"; shift 2 ;;
    --model) MODEL="$2"; shift 2 ;;
    --help|-h)
      echo "用法: bash workflows/text-to-video.sh \"故事\" [--duration 5] [--mode t2v] [--model kling]"
      exit 0 ;;
    *) STORY="$1"; shift ;;
  esac
done

if [[ -z "$STORY" ]]; then
  echo "❌ 错误: 需要故事描述"
  exit 1
fi

echo "════════════════════════════════════════════"
echo "  KPE 文本→视频流水线"
echo "  故事: $STORY"
echo "  时长: ${DURATION}s | 模式: $MODE | 模型: $MODEL"
echo "════════════════════════════════════════════"

# ─── 1. prompt 质检（无论生成与否，先过 lint）────────────
echo ""
echo "▶ Step 1/4: prompt_lint 质检"
if [[ -f "$SCRIPTS/prompt_lint.py" ]]; then
  python3 "$SCRIPTS_WIN/prompt_lint.py" --mode "$MODE" "$STORY" 2>&1 | tee "$TMPDIR/lint.txt" || true
  SCORE=$(grep -oE "[0-9]+/100" "$TMPDIR/lint.txt" | head -1 | cut -d/ -f1 || echo "0")
  echo "  质检分: ${SCORE:-0}/100"
  if [[ -n "$SCORE" && "$SCORE" -lt 60 ]]; then
    echo "  ⚠️  质检分偏低(<60)，建议先按 Anti-Slop 规则改写"
  fi
else
  echo "  ⚠️  prompt_lint.py 不存在，跳过质检"
fi

# ─── 2. 多模型适配 ───────────────────────────────────────
echo ""
echo "▶ Step 2/4: 模型适配 ($MODEL)"
if [[ -f "$SCRIPTS/t2i_generate.py" && "$MODE" == "t2i" ]]; then
  python3 "$SCRIPTS_WIN/t2i_generate.py" --model "$MODEL" "$STORY" 2>&1 | tee "$TMPDIR/adapt.txt"
elif [[ "$MODE" == "t2v" ]]; then
  echo "  T2V 模式：模型适配参考 adapters/ 目录的 yaml 规则"
  ls "$ROOT/adapters/"*.yaml 2>/dev/null | sed 's/^/    /'
else
  echo "  (模式 $MODE 无需适配步骤)"
fi

# ─── 3. 首帧生成（可选，t2v 需要首帧时）──────────────────
echo ""
echo "▶ Step 3/4: 首帧检查"
echo "  提示: 如需首帧，用 t2i_generate.py 生成后作为 I2V 输入"
echo "  参考: 22d-type-specials.md「为 I2V 构图」+ 23-first-last-frame.md"

# ─── 4. 交付总结 ─────────────────────────────────────────
echo ""
echo "▶ Step 4/4: 交付"
OUT="$ROOT/workflows/outputs/$(date +%Y%m%d-%H%M%S).prompt.txt"
mkdir -p "$ROOT/workflows/outputs"
cat > "$OUT" <<EOF
# KPE 流水线输出
# 生成时间: $(date '+%Y-%m-%d %H:%M:%S')
# 模式: $MODE | 时长: ${DURATION}s | 模型: $MODEL

## 原始需求
$STORY

## 质检结果
$(cat "$TMPDIR/lint.txt" 2>/dev/null | grep -E "评分|WARN|ERROR" | head -10 || echo "无")

## 使用指引
1. 复制最终 prompt 到可灵/对应模型
2. 首帧图用 t2i_generate.py 生成
3. 生成后对比 retake-protocol.md 判定是否重试
EOF
echo "  已保存: $OUT"
echo ""
echo "✅ 流水线完成"
rm -rf "$TMPDIR"
