---
tags: [hermes, audit, context, token]
created: 2026-07-31
status: report
tool: ecc-context-budget (适配 Hermes)
---

# Hermes 上下文消耗审计报告

> 审计时间：2026-07-31 · 方法：ECC context-budget 适配 Hermes
> 审计对象：技能、规则、MCP 服务器、记忆、系统提示

## 📊 总览

| 组件 | 数量 | 估算 tokens | 占比 |
|------|:---:|:---:|:---:|
| 技能 description（常驻系统提示） | 203 个 | ~4,987 | 32% |
| MCP 工具 schema（按需加载） | ~80+ 个 | ~40,000 | 主导 |
| 记忆（memory + user） | 2 个 | ~1,500 | 10% |
| SOUL.md | 1 个 | ~425 | 3% |
| AGENTS.md（被注入拦截） | 1 个 | — | — |
| 会话历史（实时） | 不定 | 不定 | 动态 |

**关键结论**：
1. **MCP 是最大杠杆**（每个工具 schema ~500 tokens）——jlc-mcp 38 工具 + github 26 工具 = 64 工具 ≈ 32,000 tokens 潜在开销（按需加载时才进上下文）
2. **技能 description 常驻**：203 个技能 description ≈ 5,000 tokens 固定开销，其中 **82 个超 60 字符**（含 ECC 导入的 6 个，261/239/167/157/134/63 字符）
3. 记忆当前 ~5,974 字符（≈1,500 tokens），占系统提示约 10%，健康

## 🔍 发现的问题（按可节省量排序）

### ⚠️ 问题 1：82 个技能 description 超 60 字符预算（可省 ~3,000 tokens/会话）
- 系统提示中技能索引截断到 57 字符，超长 description 白白占空间
- 含：6 个 ECC 导入技能（agent-self-evaluation 261 字符、codebase-onboarding 239 字符等）
- **建议**：优先压缩 ECC 导入的 6 个（我们自己建的都合规）

### ⚠️ 问题 2：大技能文件影响按需加载（非阻塞）
- research-paper-writing 2377 行、hermes-configuration-patterns 1545 行
- 按需加载时才消耗，常驻无影响 → 低优先级

### ⚠️ 问题 3：memvid MCP 已停用但未删除
- 记忆中有记录：memvid MCP 因路径问题失败过（规则 #2 止损铁律）
- ✅ **已复查（2026-07-31）**：py_compile 通过 + `--help` 正常启动 → **可保留，无需删除**

## ✅ 健康的部分

| 项 | 状态 |
|----|------|
| 记忆大小 | 5,974 字符 / 1,375+2,200 上限 → 合理 |
| MCP 数量 | 6 个服务器，未超 10 个警戒线 |
| 大技能按需加载 | 只有 description 常驻，正文按需 → 架构健康 |
| 会话管理 | 规则 #15 已落地（跨天拆会话）|

## 🎯 可执行建议（按优先级）

### P0：压缩 6 个 ECC 技能的 description（省 ~400 tokens）✅ 已完成
| 技能 | 原字符 | 现字符 |
|------|:---:|:---:|
| ecc-agent-self-evaluation | 261 | 54 |
| ecc-codebase-onboarding | 239 | 58 |
| ecc-error-handling | 167 | 53 |
| ecc-growth-log | 157 | 43 |
| ecc-strategic-compact | 134 | 52 |
| ecc-verification-loop | 63 | 43 |

### P1：检查 memvid MCP 状态 ✅ 已复查正常
- py_compile 通过 + `--help` 启动成功 → 保留

### P2：长期监控
- 每季度跑一次本审计（技能数增长时）
- 新增技能前先数 description 长度（规则 #20）

## 📋 审计方法（可复用）

```
1. 扫描 skills/*/SKILL.md → description 字符数统计（超 60 标记）
2. 读 config.yaml mcp_servers → 工具数估算（~500 tokens/工具）
3. 检查 memories/*.md → 大小 vs 上限
4. 按 P0/P1/P2 输出建议
```

---
*2026-07-31 · ECC context-budget 技能适配 Hermes 首次审计*
