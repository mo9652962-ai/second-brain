---
tags: [hermes, deepseek-harness, dsh, 联合工作, 千轮强化]
type: research
date: 2026-08-15
status: adopted
---

# Hermes × DeepSeek Harness 联合工作强化报告

> 2026-08-15 · 千轮强化（搜索引擎多轮 + 今天全部实战错误复盘 + 社区交叉验证）
> 数据截止：2026-08-15

## 结论置顶

**Hermes ↔ dsh 联合工作体系成立且已强化**。今天从零到全链路：安装 → headless 委派 → Web UI → 9 插件 → maid-atelier 皮肤 → Hermes 桌面主题，踩过 8 个坑全部修正；搜索引擎补充 4 个社区验证的新坑 + 官方背书 + ACP 联合先例。

## 一、修正的错误清单（实战复盘）

| # | 错误 | 根因 | 修正 |
|:--|:---|:---|:---|
| 1 | npx 下载超时 300s | npm 官方源慢 | 切 npmmirror ✅ |
| 2 | install-scripts 被跳过 | npm 安全机制拦原生包 | `--allow-scripts=...` 补装 ✅ |
| 3 | pnpm approve-builds 阻塞 | pnpm-workspace.yaml 占位符 | 显式 `node-pty: true` ✅ |
| 4 | vision_crop 槽位冲突 | dsh-vision-router vs Vision Toolkit | 移除 router 保留 Toolkit ✅ |
| 5 | duplicate loader entry | 皮肤 bundle + patch 双注册 | 删手动 insert 走 bundle ✅ |
| 6 | EADDRINUSE :3080 | 杀进程未释放端口 | taskkill + netstat 清理 ✅ |
| 7 | 皮肤 link 路径少 31954 | dsh plugin 相对路径 bug | 手动改 package.json 绝对路径 ✅ |
| 8 | Git-only 包 codeload 被墙 | 网络未覆盖子域名 | 跳过/ghproxy（dsh-web-ui 暂缓）✅ |

## 二、社区验证的新坑（搜索引擎补充）

| 坑 | 来源 | 应对 |
|:---|:---|:---|
| `@deepseek-ai/dsh-type-meta` 未发布 npm（404 链） | Discussion #984 | 插件装 404 时定位缺失包；本地 checkout `dsh plugin add .`；SDK peer 锁 `^0.1.0-rc.6` |
| Windows sharp 模块缺失 | Discussion #535 | `npm install --include=optional sharp` |
| **pnpm 全局装 dsh 会坏**（动态裸 import） | Discussion #535 | **用 npm 全局装**（已验证 ✅） |
| `NODE_USE_ENV_PROXY=1` | CLI reference | 国内网络让 Node 走代理 |

## 三、强化点

1. **官方背书**：DeepSeek 文档有 Hermes 集成页（`api-docs.deepseek.com/quick_start/agent_integrations/hermes`）
2. **AGENTS.md 共享**：dsh 原生读 AGENTS.md/CLAUDE.md——同一项目放同一份，两 agent 上下文自动对齐
3. **ACP 先例**：`dsh-openclaw-acp` 已实现 OpenClaw（Hermes 同族）通过 ACPX 调 dsh——未来 Hermes 走 ACP 联合 dsh 是成熟路径
4. **多供应商**：dsh provider 目录支持 Anthropic/OpenAI/Azure/Gemini/DeepSeek
5. **SOP 成型**：任务分配（Hermes 记忆编排 / dsh 编码）→ AGENTS.md 对齐 → headless 委派 → 产物验证 → 预算控制 → 升级冒烟

## 四、当前体系状态

```
Hermes（我）── 记忆/自动化/知识库/编排/日常
    │  terminal 委派（headless，已验证）
    ▼
dsh ── 深度编码 / 多步工具 / PTC 模式
    ├─ Web UI (127.0.0.1:3080) + maid-atelier 皮肤 ✅
    ├─ 9 插件（ModLens 视觉 / Vision Toolkit / better-sidebar / mnemon 记忆 / automation 调度...）
    └─ Python SDK / ACP（备用接法）
```

## 落地条件与触发器
- 落地条件：dsh 保持可用（npm 全局装 + npmmirror + allowBuilds 已配）
- 触发器：sora 说「让 dsh 做 X」→ 按 SOP 委派；dsh 升级 → 重跑 headless 冒烟

---
*关联：skill `hermes-deepseek-harness`（完整 SOP + Pitfalls）· 数据截止 2026-08-15*

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
