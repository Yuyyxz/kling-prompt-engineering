#!/usr/bin/env python3
"""
Director Engine 评估脚本
- 读取 cases.json 中的测试用例
- 调用 LLM 生成可灵视频 prompt
- 用 judge 对生成结果按 10 项 rubric 打分
- 输出结果表，低于 7 分则 exit 1
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# ─── 配置 ───────────────────────────────────────────────
CASES_FILE = Path(__file__).parent / "cases.json"
PASS_THRESHOLD = 7  # 通过线

# 生成 prompt 的系统指令
GENERATOR_SYSTEM = """\
你是一个专业的 AI 视频 prompt 工程师，使用「导演引擎」方法论为可灵（Kling）平台生成视频 prompt。

核心规则：
1. 导演五问：先回答 功能/视角/节拍/光源/镜头运动，用动词和名词，不用形容词堆砌
2. 可见节拍：每个镜头必须有一个具体的、摄影机可捕捉的动作或变化
3. 具体光源：写真实光源（如"窗外北向日光""头顶钨丝灯 3200K"），禁止写 "cinematic lighting"
4. 镜头运动：明确写出运镜（push-in / pan-left / static 等）
5. 声音意图：包含环境音/音乐/音效描述
6. 约束槽：末尾加排除项（No text, no logos, no watermark）
7. Anti-slop：禁止使用 cinematic / beautiful / 4k / epic / masterpiece / stunning / breathtaking
8. 一镜一拍：一个镜头 = 一个节拍 = 一个变化
9. 格式：使用时间轴格式（0:00-0:03 ...）或标准公式
10. 可灵适配：时长只选 5s/10s/15s；不要求画面内文字渲染；避免多主体同时复杂运动

根据用户请求，直接输出最终的可灵视频 prompt（英文），不要解释。
"""

# 评分系统指令
JUDGE_SYSTEM = """\
你是一个严格的评分员。根据以下 10 项标准对给定的视频 prompt 打分，每项 0 或 1 分。

评分标准：
1. 导演五问：回答了至少功能+视角（动词/名词描述，非形容词）
2. 可见节拍：有具体的、可被摄影机捕捉的动作/变化
3. 具体光源：指定了真实光源（非 "cinematic lighting"）
4. 镜头运动：有明确运镜或标注 static
5. 声音意图：包含声音/音乐/音效描述
6. 约束槽：有排除项（No text, no logos 等）
7. Anti-slop：未出现 cinematic/beautiful/4k/epic/masterpiece/stunning/breathtaking
8. 一镜一拍：一个镜头=一个节拍=一个变化
9. 格式规范：使用时间轴格式或标准公式
10. 可灵适配：时长合理、无文字渲染要求、无多主体复杂运动

只输出一个 JSON 数组，包含 10 个整数（0 或 1），不要输出其他内容。
示例：[1,1,0,1,1,1,1,1,0,1]
"""


# ─── 后端检测 ─────────────────────────────────────────────
def detect_backend():
    """自动检测可用后端：claude CLI > anthropic SDK > 跳过"""
    if shutil.which("claude"):
        return "cli"
    if os.environ.get("ANTHROPIC_API_KEY"):
        try:
            import anthropic  # noqa: F401
            return "api"
        except ImportError:
            pass
    return None


# ─── LLM 调用 ─────────────────────────────────────────────
def call_llm(backend: str, system: str, user: str) -> str:
    """统一调用接口，返回 LLM 文本响应"""
    if backend == "cli":
        # 使用 claude CLI（--print 模式，无交互）
        result = subprocess.run(
            ["claude", "--print", "--system-prompt", system, user],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0:
            raise RuntimeError(f"claude CLI 错误: {result.stderr[:200]}")
        return result.stdout.strip()

    # backend == "api"
    import anthropic
    client = anthropic.Anthropic()
    resp = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return resp.content[0].text.strip()


# ─── 主流程 ───────────────────────────────────────────────
def main():
    backend = detect_backend()
    if backend is None:
        print("[跳过] 未检测到 claude CLI 或 ANTHROPIC_API_KEY，无法运行评估。")
        sys.exit(0)

    print(f"[后端] {backend}")
    cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))

    results = []  # (id, scores, total)

    for case in cases:
        case_id = case["id"]
        user_input = case["input"]
        print(f"\n{'='*50}")
        print(f"[用例] {case_id}: {user_input}")

        # 第一步：生成 prompt
        gen_user = (
            f"用户请求：{user_input}\n"
            f"期望模式：{case['expected_mode']}，期望时长：{case['expected_duration']}\n"
            f"请生成对应的可灵视频 prompt。"
        )
        try:
            generated = call_llm(backend, GENERATOR_SYSTEM, gen_user)
        except Exception as e:
            print(f"  [错误] 生成失败: {e}")
            results.append((case_id, [0]*10, 0))
            continue

        print(f"  [生成] {generated[:120]}...")

        # 第二步：judge 评分
        judge_user = f"请对以下视频 prompt 评分：\n\n{generated}"
        try:
            judge_raw = call_llm(backend, JUDGE_SYSTEM, judge_user)
            # 提取 JSON 数组（兼容 markdown 代码块包裹）
            judge_clean = judge_raw.strip()
            if judge_clean.startswith("```"):
                judge_clean = judge_clean.split("\n", 1)[1].rsplit("```", 1)[0]
            scores = json.loads(judge_clean)
            scores = [int(s) for s in scores[:10]]
            # 补齐不足 10 项的情况
            while len(scores) < 10:
                scores.append(0)
        except Exception as e:
            print(f"  [错误] 评分失败: {e}")
            scores = [0] * 10

        total = sum(scores)
        status = "PASS" if total >= PASS_THRESHOLD else "FAIL"
        print(f"  [得分] {total}/10 → {status}  明细: {scores}")
        results.append((case_id, scores, total))

    # ─── 汇总表 ─────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"{'用例':<16} {'得分':>4}  {'结果':<6}")
    print(f"{'-'*36}")
    any_fail = False
    for case_id, scores, total in results:
        status = "PASS" if total >= PASS_THRESHOLD else "FAIL"
        if total < PASS_THRESHOLD:
            any_fail = True
        print(f"{case_id:<16} {total:>4}  {status}")

    print(f"{'-'*36}")
    passed = sum(1 for _, _, t in results if t >= PASS_THRESHOLD)
    print(f"总计: {passed}/{len(results)} 通过 (阈值 {PASS_THRESHOLD}/10)")

    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
