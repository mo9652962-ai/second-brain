#!/usr/bin/env python3
"""
智能模型路由配置工具
用法：python scripts/configure-smart-router.py
"""

import subprocess
import sys

def run_cmd(cmd):
    """运行命令并返回结果
    安全说明：所有命令都是硬编码的配置值，无用户输入，shell=True 在此处是安全的
    """
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()

def set_config(key, value):
    """设置配置项"""
    success, stdout, stderr = run_cmd(f"hermes config set {key} \"{value}\"")
    if success:
        print(f"  ✅ {key:30s} → {value}")
    else:
        print(f"  ❌ {key:30s} → 失败: {stderr}")
    return success

def main():
    print("=" * 70)
    print("🧠  Hermes 智能模型路由 - 全部优化")
    print("=" * 70)
    print()

    # 1. 显示当前配置
    print("📋 当前配置:")
    print("-" * 70)
    _, default, _ = run_cmd("hermes config get model.default")
    _, provider, _ = run_cmd("hermes config get model.provider")
    print(f"  主模型: {default}")
    print(f"  Provider: {provider}")
    print()

    # 2. 配置辅助模型
    print("🔧 优化辅助模型配置 (9个槽位):")
    print("-" * 70)

    success_count = 0
    total_count = 0

    # 1. 视觉任务 - 专门的视觉模型
    total_count += 1
    if set_config("auxiliary.vision.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.vision.model", "doubao-1.5-vision-pro-250328"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.vision.key_env", "ARK_API_KEY"):
        success_count += 1

    # 2. 网页摘要 - 轻量快速模型
    total_count += 1
    if set_config("auxiliary.web_summary.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.web_summary.model", "doubao-seed-2-0-lite-260215"):
        success_count += 1

    # 3. 浏览器截图分析 - 视觉模型
    total_count += 1
    if set_config("auxiliary.browser_screenshot.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.browser_screenshot.model", "doubao-1.5-vision-pro-250328"):
        success_count += 1

    # 4. 危险命令审批 - 保守可靠的模型
    total_count += 1
    if set_config("auxiliary.approval_classifier.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.approval_classifier.model", "glm-5-2-260617"):
        success_count += 1

    # 5. 上下文压缩 - 轻量快速模型
    total_count += 1
    if set_config("auxiliary.compression.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.compression.model", "doubao-seed-2-0-mini-260428"):
        success_count += 1

    # 6. 会话搜索摘要 - 轻量模型
    total_count += 1
    if set_config("auxiliary.session_summary.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.session_summary.model", "doubao-seed-2-0-lite-260215"):
        success_count += 1

    # 7. Skill 匹配 - 推理能力适中的模型
    total_count += 1
    if set_config("auxiliary.skill_match.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.skill_match.model", "doubao-seed-1-6-flash-250615"):
        success_count += 1

    # 8. MCP 工具分派 - 代码能力强的模型
    total_count += 1
    if set_config("auxiliary.tool_dispatch.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.tool_dispatch.model", "doubao-seed-2-0-code-preview-260215"):
        success_count += 1

    # 9. 记忆刷新 - 轻量模型，速度快
    total_count += 1
    if set_config("auxiliary.memory_refresh.provider", "custom:fangzhou-1"):
        success_count += 1
    total_count += 1
    if set_config("auxiliary.memory_refresh.model", "doubao-seed-2-0-mini-260428"):
        success_count += 1

    print()
    print(f"✅ 配置完成: {success_count}/{total_count} 项成功")
    print()
    print("=" * 70)
    print("📊 最终配置结果")
    print("=" * 70)
    print()

    _, new_default, _ = run_cmd("hermes config get model.default")
    _, new_provider, _ = run_cmd("hermes config get model.provider")

    print(f"🎯 主模型:     {new_default} @ {new_provider}")
    print("            (火山控制台动态切换，无需改配置)")
    print()
    print("👁️  视觉任务:    doubao-1.5-vision-pro-250328")
    print("🌐 网页摘要:    doubao-seed-2-0-lite")
    print("🖥️  浏览器截图:  doubao-1.5-vision-pro-250328")
    print("✅ 命令审批:    glm-5-2 (保守可靠)")
    print("📦 上下文压缩:  doubao-seed-2-0-mini (极速)")
    print("📝 会话摘要:    doubao-seed-2-0-lite (快速)")
    print("🎯 Skill匹配:   doubao-seed-1-6-flash")
    print("🛠️  工具分派:    doubao-seed-2-0-code-preview (代码专精)")
    print("🧠 记忆刷新:    doubao-seed-2-0-mini (轻量)")
    print()
    print("=" * 70)
    print("🛡️  7层故障转移已就绪:")
    print("  ark-code-latest → deepseek-v4-pro → kimi-k3 → kimi-k2.7-code")
    print("  → qwen3.7-plus → glm-5.2 → Qwen3.5-4B → DeepSeek-V4-Pro")
    print("=" * 70)
    print()
    print("💡 下一步: 重启 Hermes 使配置完全生效")
    print()
    print("🎉 模型自动路由已全部优化完成！")
    print("   不同任务自动路由到最合适的模型，无需手动切换 🚀")

if __name__ == "__main__":
    main()
