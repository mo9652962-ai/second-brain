---
title: "System Prompts 精选存档"
type: note
domain: Dev
status: active
tags: [knowledge/dev]
source: null
---
# System Prompts 精选存档

> 来源：asgeirtj/system_prompts_leaks (42K★, CC0-1.0) · 2026-08-01 精选
> 用途：AI 系统提示词设计参考——学习大厂如何设计行为总则/工具调用/上下文管理

## 存档文件

| 文件 | 来源 | 大小 | 学习价值 |
|------|------|:---:|---------|
| `hermes-own-prompt.md` | Misc/hermes.md（仓库作者自己的 Hermes 配置） | 17.8KB | **对照学习**——我们用的同框架提示词结构（SOUL.md+记忆+USER PROFILE） |
| `claude-code-opus-5.md` | Anthropic/Claude Code/ | 138KB | Claude Code 完整提示词（工具/安全/上下文管理） |
| `gpt-5.6-sol-codex.md` | OpenAI/Codex/ | 17.3KB | **Codex 主力模型**（与我们 opencode-go 相关） |
| `deepseek-chat.md` | DeepSeek/ | 438B | 我们主力 provider 的官方提示词 |

## 从 GPT-5.6-Sol 学到的（已吸收到思维）

1. **Compaction 后不重启**："Assume compaction occurred while you were working. Do not restart from scratch; you continue naturally." → 呼应规则 #15 跨天会话管理
2. **60 秒 commentary 规则**："should not be left without a commentary update for more than 60 seconds" → 呼应规则 #10 中间检查点
3. **Lead with outcome**："Lead with the outcome rather than the steps you took" → 呼应输出要求"结论置顶"
4. **判断用户意图**：新消息可能是 replace 或 add——评估后决定 drop 旧任务还是合并处理

## 从 Hermes 自身学到的

- "Be genuinely helpful, not performatively helpful"（真诚帮助，不走形式）
- "Have opinions"（有观点，不是搜索引擎）
- "Be resourceful before asking"（先自己查再问）
- 这些原则我们已在用——验证了设计方向

## 使用方式

- 想优化自己的系统提示词 → 对照 claude-code-opus-5.md 的工具/安全章节
- 想理解我们用的模型 → 看 gpt-5.6-sol-codex.md / deepseek-chat.md
- 想了解 Hermes 生态 → hermes-own-prompt.md

## 来源
- 仓库：https://github.com/asgeirtj/system_prompts_leaks (CC0-1.0)
- 注意：这些是社区抓取的快照，非官方字节级精确版本

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
