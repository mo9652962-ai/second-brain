---
tags: [github, ai-agent, memory, cross-agent, handoff, rust, 研究笔记, 2026-08]
domain: Dev
aliases: [ai-memory, 跨agent记忆, akitaonrails-ai-memory]
date: 2026-08-23
source: https://github.com/akitaonrails/ai-memory
---

# ai-memory — 跨 Agent 长期记忆与交接（akitaonrails/ai-memory）

> ⭐ 4,065（本周 +2,404，2026-08-23 周榜新面孔）· Rust · MIT · 1,356 commits / 93 tags（v1.31.0，12 小时前活跃提交）
> 定位：**agent coding CLI 的长期记忆层 + 跨 agent 厂商交接方案**——换 agent 不失忆。

## 核心思路（3-5 句）

1. 解决 Agent 生态「厂商锁定记忆」痛点：Claude Code / Codex / opencode / Kimi / Devin / Kiro 各写各的记忆，切换工具就断片。
2. 用 **hooks 事件系统**接入每个 agent（11 agents × 75 个 POSIX 脚本 + .ps1 配对），按各 agent 自己的事件词汇表（CLAUDE_CODE_EVENTS / KIMI_CODE_EVENTS / KIRO_CLI_V*_EVENTS / Devin post-compaction）捕获上下文，统一落到 markdown-on-disk。
3. **自改进循环**：post-turn review → approval gates → curator boundaries（明确声明借鉴 Hermes Agent）；auto-improve 自动把会话经验写成记忆页。
4. 记忆页遵循 **A-MEM Zettelkasten 原子笔记 + 链接演化**；检索哲学是 Karpathy 的 **compile-not-retrieve**（编译而非检索）。
5. 附 OMC importer 等 companions，可导入其他记忆体系存量数据。

## 技术架构

```text
┌─ Claude Code ─┐ ┌─ Codex ─┐ ┌─ opencode ─┐ ┌─ Kimi/Devin/Kiro ─┐
└──────┬────────┘ └────┬────┘ └─────┬──────┘ └─────────┬─────────┘
       │ hooks(事件)   │ hooks       │ hooks           │ hooks
       ▼               ▼             ▼                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │              ai-memory 核心 (Rust crates)                │
   │  · 事件词汇表归一化（per-agent event vocabularies）      │
   │  · markdown-on-disk 单一事实源（basic-memory 模式）       │
   │  · auto-improve：LLM 提议→schema 校验→审批门→curator     │
   │  · A-MEM 原子笔记 + 链接演化                              │
   └─────────────────────────────────────────────────────────┘
```

## 关键创新点

| 创新 | 说明 | 含金量 |
|:--|:--|:--:|
| 跨厂商 hooks 矩阵 | 11 agents × 75 scripts + .ps1 双平台配对，parity test 防漂移 | ★★★★ |
| auto-improve 双保险 | operation 字段 = schema enum 约束（constrained decoding 厂商直接拦）+ 归一化拼写（无约束厂商兜底）| ★★★★ |
| 自改进循环借鉴 Hermes | post-turn review / approval gates / curator boundaries 与 Hermes 同构 | ★★★★ |
| compile-not-retrieve | 记忆不是检索出来的，是编译进上下文的（Karpathy LLM Wiki 模式）| ★★★★ |
| markdown-on-disk | 记忆即文件，可 diff / 可 review / 可 git 管理（basic-memory 模式）| ★★★★ |

## 竞品对比

| 方案 | 形态 | 差异 |
|:--|:--|:--|
| **ai-memory** | Rust CLI + hooks | 多厂商统一 + 自改进，最全 |
| agentmemory | Python | 概念先驱（README 自认「Rust 后继」）|
| basic-memory | Python | markdown-on-disk 首创者，单厂商 |
| cognee | Python | pipeline 组合 + triplet embeddings |
| Hermes Agent | 框架 | 自改进循环源头（被 ai-memory 借鉴）|

## 💎 可借鉴点（⭐ 最重要）

1. **sora 多 agent 体系的记忆互通**：k(Hermes) / dsh / ZCode / Codex / Claude Code 各有上下文，AGENTS.md 交接是手工方案。ai-memory 的「统一 markdown-on-disk + 各 agent hooks」思路 = 把交接从「文档」升级为「自动同步层」。现有 `cross-agent-memory-setup`（Mnemon）是路径 A，ai-memory 是路径 B，可对照。
2. **auto-improve 的 schema 双保险**（#458 教训）：LLM 自由文本字段 = 校验黑洞。对 sora 的 skill-evolution / 自举系统：operation 类字段直接上 enum 约束 + 归一化兜底，比纯提示词可靠。
3. **hooks 事件词汇表设计**：每个 agent 暴露不同事件名（CLAUDE_CODE_EVENTS ≠ KIRO_CLI_EVENTS），需要 per-agent 适配层。Hermes 插件/钩子体系可借鉴「事件词汇表 + parity test 防漂移」。
4. **编译而非检索**：sora 的 TencentDB 记忆引擎是检索式（分层召回）；ai-memory 的 compile-not-retrieve 是另一种哲学——把相关记忆直接编译进提示词。两种可互补。
5. **Claude Code 协作开发模式**：README 声明「由 Claude Opus 4.7 按 docs/design-decisions.md 计划协作构建」——与 sora 的 ZCode 协作（任务文件 + review）同模式，设计文档先行被证明可行。

## 安装/验证命令

```bash
# (Linux/macOS 为主；Windows 有 .ps1 支持但 CI 上非关键路径)
cargo install ai-memory    # 或从 release 下载
ai-memory init             # 初始化记忆仓库
ai-memory agent add claude-code   # 接入 Claude Code hooks
```

## 总结评价表

| 维度 | 评分 | 说明 |
|:--|:--:|:--|
| 技术含金量 | ★★★★ | Rust 工程质量高，1,356 commits 活跃 |
| 与 sora 关联 | ★★★★★ | 多 agent 记忆互通正是 sora 痛点 |
| 值得安装 | 🟡 观察 | 等 hooks 矩阵稳定 + Windows 一等公民后再评估；当前 Mnemon + AGENTS.md 够用 |
| 趋势判断 | ⬆️ 上行 | 跨厂商记忆标准是 Agent 生态必经之路 |

---
> 🗺️ 属于 [[MOC-Dev]] · [[MOC-GitHub]] · [[HOME|🏠 Home]]
