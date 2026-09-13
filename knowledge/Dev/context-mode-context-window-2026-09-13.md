---
tags: [dev, context-window, MCP, agent, 上下文优化, github-trending, W38]
aliases: [context-mode, Context Mode, 上下文沙箱]
date: 2026-09-13
source: https://github.com/mksglu/context-mode
domain: Dev
status: active
---

# Context Mode — 上下文窗口优化 MCP Server

**22.4k★（W38 +1,936）** · 「The other half of the context problem.」——把工具输出挡在 context 之外（98% 减少）、跨压缩保持会话记忆、跨 17 平台强制路由。TypeScript 68.8%，2,182 commits · 120 contributors · 195 releases · v1.0.169，安装量 331,200+，Microsoft / Google / Meta / Amazon / IBM / NVIDIA / ByteDance 团队在用。许可证 ELv2（MIT 改，仅禁托管服务）。

## 核心特征

1. **Context Saving（沙箱化工具输出）**：315 KB → 5.4 KB（98% 减少）。工具输出 >100KB 自动索引进 FTS5 并返回指针——**不截断，索引化**（旧版 60/40 head+tail 截断已废弃）。
2. **Session Continuity（SQLite + FTS5 会话记忆）**：每个文件编辑、git 操作、任务、错误、用户决策都记进 SQLite；压缩（compaction）时不把数据倒回 context，而是索引进 FTS5、用 BM25 按需检索。不 `--continue` 则旧 session 数据立即删除（干净会话 = 干净 slate）。
3. **Think in Code（让 LLM 写脚本而非读文件）**：47 × Read() = 700 KB → 1 × ctx_execute() = 3.6 KB。「别把 LLM 当数据处理机，当代码生成器」——这是 17 个平台的强制范式。
4. **No prose-style enforcement（不做文风注入）**：曾注入「terse/caveman 简洁文风」提示，被 Moonshot 实测证明会降低编码/推理基准（kimi-k2.5 退化证据）后**全量移除 22 处注入点**——只路由数据流向，不规定模型怎么说话。
5. **11 个 MCP 工具 + 6 类 hooks**：六个沙箱工具（ctx_batch_execute/ctx_execute/ctx_execute_file/ctx_index/ctx_search/ctx_fetch_and_index）+ 五个 meta 工具（ctx_stats/ctx_doctor/ctx_upgrade/ctx_purge/ctx_insight）；PreToolUse/PostToolUse/UserPromptSubmit/PreCompact/SessionStart/Stop 全挂。
6. **17 平台适配**：Claude Code / Gemini CLI / Copilot CLI / Antigravity CLI(agy) / Cursor / OpenCode / Zed / Pi / Codex / OpenClaw gateway 等，HookAdapter 模式统一事件。

## 技术架构（文字图）

```
Agent (17 平台任一)
   │  MCP + hooks
   ▼
┌─────────────────────────────────────────────┐
│ context-mode server (MCP, TypeScript)         │
│  ├─ Sandbox: ctx_execute → 结果只留 console  │
│  ├─ FTS5 索引: >100KB 输出 → 指针不截断      │
│  ├─ SessionDB: 编辑/git/任务/决策 → SQLite    │
│  └─ Routing: SessionStart 注入路由指令        │
└─────────────────────────────────────────────┘
   │ 压缩时 BM25 按需检索，不 dump 回 context
   ▼
模型永远只看到「该看的」
```

## 💎 可借鉴点（⭐ 核心价值）

1. **「截断 vs 索引化+指针」的哲学差异**。Hermes 工具结果三层截断（记忆红线：勿改核心），context-mode 的答案是大输出索引进 FTS5、模型需要时按需检索——不丢信息、不占窗口。sora 的 context-management-bootstrapping 可把「截断」升级为「截断 + 可检索兜底」双层策略（如 web_extract 的全文落盘 + read_file 续读已经是同思路的雏形）。
2. **压缩时的记忆策略：索引事件而非重放事件**。context-mode 把「压缩后忘掉什么」变成「压缩后能检索什么」——对应 sora 的五级记忆体系，session 事件不该靠重放保留，而该靠结构化沉淀（skills/memory 本来就是干这个的）。
3. **Think in Code 范式是 execute_code 的正确用法**：批量统计/过滤/解析用脚本做、只把结论带回来，而非把 N 个文件读进上下文——sora 的 execute_code 已实践此范式，可作为技能写作的默认原则。
4. **文风注入的教训（kimi-k2.5 证据）**：强制「简洁输出」会伤推理质量——约束应该放在数据路由层，不是表达层。sora 的 SOUL.md「默认简洁」是用户偏好设定，与注入式压缩有本质区别；但在做 AI 产品/技能时，不要用 brevity prompt 换 token。
5. **ELv2 许可证策略**：免费使用 + 禁托管服务——比 MIT 更保护商业化的「开源核心」模式，sora 的墨题/网站产品可参考。

## 安装/验证

```bash
# Claude Code（插件市场）
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
/context-mode:ctx-doctor   # 验证 runtimes/hooks/FTS5

# MCP-only 尝鲜
claude mcp add context-mode -- npx -y context-mode
```

## 总结评价

| 维度 | 评分 | 说明 |
|:--|:--|:--|
| 技术含金量 | ★★★★★ | FTS5 外部化 + HookAdapter 多平台，工程极深 |
| 关联度 | ★★★★☆ | 直击 Hermes context 三层截断 / 记忆体系 / execute_code 范式 |
| 可迁移性 | ★★★★☆ | 「索引化+指针」「按需检索」「数据路由不碰表达」三条都可落地 |
| 安装意愿 | ⚪ 观望 | 本机 Hermes 核心不可改，思路借鉴 > 工具安装（ELv2 也不适合商用托管） |
| 趋势判断 | 📈 涨 | 上下文治理是 agent 规模化的必争之地（+1,936/周 持续） |

关联：[[context-management-bootstrapping]] · [[ecc-context-budget]] · [[ecc-strategic-compact]] · [[knowledge/knowledge-map|知识地图]]
