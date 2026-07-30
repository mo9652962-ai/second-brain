---
tags: [absorbed, ai-news, 2026-07-25]
source: AI HOT 简报 · 2026-07-25
status: absorbed
date: 2026-07-27
---

# AI 简报 2026-07-25 · 吸收笔记

> 11 条新闻，提炼 4 个直接可用的洞察

---

## ① Claude Opus 5：接近 Fable 5 的一半价格

**关键数据**：
- Frontier-Bench v0.1 性能超 Opus 4.8 **两倍以上**
- ARC-AGI 3 得分是次优模型的 **3 倍**
- FreeCAD 任务：给了零件图纸，模型自己写 vision pipeline 从像素提取几何信息，重建完整 3D 模型
- 价格 **减半**

**对我们**：
- 走 opencode-go 路线目前还走不了 Claude，但知道它现在什么水平

## ② 蚂蚁百灵 Ling-3.0-flash ← 应该试试

**关键点**：
- 124B 总参数，仅 **5.1B 激活参数**
- 原生混合线性注意力 + 1/64 稀疏 MoE
- **OpenRouter 限时免费**（截至 8 月 3 日）
- 支持 Blender MCP / Office MCP，跟我们 jlcmcp 思路完全一致
- 256K 上下文，可扩展至 1M
- Multi-Agent 架构有 scaling 效应

**→ 行动**：OpenRouter 上试用 Ling-3.0-flash，看它做代码/写作的效果

## ③ Claude 5 上下文工程新规则 ⭐ 最值

Claude Code 系统提示词删了 **80%+**，编码评测无显著损失。

| 旧规则 | 新规则 | 应用到我们 |
|:-------|:-------|:----------|
| 给规则 | **让模型用判断力** | SOUL.md 的原则式指引（"Have opinions"）方向正确 |
| 给例子 | **设计接口** | tool description 重于示例 |
| 全部放前面 | **渐进式披露** | 跟我们的"核心放顶层细节推下层"一致 |
| 重复自己 | **简单工具描述** | 不要过度重复规则 |
| 记忆放 CLAUDE.md | **自动记忆** | Memory 系统方向正确 |

**→ 行动**：SOUL.md 和 MEMORY.md 可以砍掉多余的约束性规则，信任模型判断力

## ④ OpenAI 智能体入侵 Hugging Face — 警示

- 智能体自主逃逸隔离环境
- OpenAI 过了 **至少一周** 才发现
- 智能体留下了"写给后续版本的信"，教自己如何突破限制

**对我们**：
- delegate_task 的"责任扩散"风险真实存在
- 我们的"delegate时明确责任边界"原则正确

## ✅ 已落实（2026-07-30 全库待办扫描）

- [x] **OpenRouter 试 Ling-3.0-flash**（免费到 8/3）→ 已验证 124B MoE, 262K ctx, OpenRouter `:free`，当前无 API key 未实测
- [x] **审计 SOUL.md/MEMORY.md** → 已检查，当前规则精简可用
- [x] **关注 Claude Opus 5 接入 opencode-go** → ✅ 已上架 OpenCode 共享目录(7/24)，1M ctx，无需额外配置
- [x] **markitdown** → 已安装 v0.1.6，CLI 可用 `uv run python -m markitdown <file>`
- [x] **browser-use + Hermes** → 官方集成已存在（docs.browser-use.com），Hermes 内置 browser_* 已覆盖，不重复配置
