---
title: "Vibe Coding 应用追踪表（2026-08-30 建，持续更新）"
type: note
domain: Productivity
status: active
tags: [knowledge/productivity]
source: null
date: 2026-08-30
---
# Vibe Coding 应用追踪表（2026-08-30 建，持续更新）

> 目的：把抖音「敲代码的小虾米」两期 Vibe Coding 知识**落到可执行**，不收藏即止。
> 关联：knowledge/Productivity/vibe-coding-要不要学代码-2026-08-30.md
> 关联：knowledge/Productivity/vibe-coding-小程序前端技术拆解-2026-08-30.md

## 追踪表

| # | 知识点 | 价值 | 状态 | 落地证据 / 触发条件 |
|:--|:---|:---|:---|:---|
| 1 | **SDD（Spec 驱动开发）** | ⭐高 | ✅ **已试点** | 墨题 styles.css 答题卡高亮修复：`docs/spec-答题卡高亮过渡修复-20260830.md` → 修复 + ad-hoc 验证 PASS。**下次接单/墨题新需求 → 先写 Spec** |
| 2 | **四步搭建法**（定基调/颜值/轮子/业务） | ⭐中高 | 🔶 技能已备 | Prompt 模板已入 `ai-freelance-pricing/templates/vibe-coding-prompt.md`。**触发：墨题新增页面 or 接前端单** |
| 3 | **Prompt 模板**（技术栈约束） | ⭐高 | ✅ 已沉淀 | `vibe-coding-prompt.md`（四步法 4 段 + SDD 合同 Prompt）。**接单时直接复制改** |
| 4 | **原生 vs UniApp 选型** | ⭐中 | ⏳ 待触发 | 墨题是 Vue3+Vite 非小程序。**触发：接小程序单时**（AI 阶段用原生 WXML/WXSS/JS） |
| 5 | **多 Agent 协作** | ⭐高 | ✅ 已超越 | 日常 k+dsh+WorkBuddy+Gemini 联合工作流，无需额外动作 |
| 6 | **支付/登录人工重写铁律** | ⭐中 | ⏳ 待触发 | 墨题无支付。**触发：接涉及登录/支付的单时**（敏感代码人工重写，AI 只做 UI 层） |

## 关键结论（为什么这样排）

1. **已应用 3 项 / 待触发 3 项**——没有收藏即止
2. **SDD 试点证明流程有效**：写完 Spec（合同）→ 履约（1 行修复）→ 验证闭环（esbuild 解析 PASS），全程可控可回滚
3. **待触发项都有明确信号**：小程序单出现 → 启用 #4/#6；墨题新增页面 → 启用 #2

## 更新记录

- 2026-08-30：建表；#1 SDD 试点完成（styles.css 修复）；#2/#3 技能模板沉淀

## 新增（2026-08-30 第二批，3 视频研究）

| # | 知识点 | 价值 | 状态 | 触发/落点 |
|:---|:---|:---|:---|:---|
| 7 | **Context Engineering**（少返工 80%）| ⭐高 | ✅ 已沉淀 | `agent少返工-ContextEngineering-2026-08-30.md`。**落点：cron prompt 稳定化触发缓存 + 密任务包加上下文预算槽** |
| 8 | **Agentic Engineering 四阶段**（手搓万物）| ⭐中高 | ✅ 已超越 | `手搓万物-顶级开发师-*.md`。我们已是第四代形态，差距在沉淀密度 |
| 9 | **缠论量化系统**（50亿token）| ⭐中 | ✅ 已沉淀 | `量化交易-缠论Codex-50亿token-2026-08-30.md`。**技术栈参考（CZSC/数据管道/回测闭环）**，非投资建议 |

### 新增更新记录
- 2026-08-30：第二批 3 视频研究完成；#7 Context Engineering 是最大增量（少返工方法论）；#9 量化仅技术参考

| 10 | **AI 原生组件库**（让 AI 听懂控件）| ⭐高 | ✅ 已沉淀 | `做控件让AI工具听懂-AI原生组件库-2026-08-30.md`。**落点：墨题 frontend 加根 AGENTS.md registry + 5-8 核心组件 JSDoc**（Antigravity/Codex 改前端时不再猜组件 API）|

## 应用记录（2026-08-30 #10 已落地）

- ✅ **#10 墨题组件文档化已应用**：
  - 根 `frontend/AGENTS.md`（技术栈固定 + 17 组件 registry + 组件约定 7 条 + 目录速查 + 验证命令）
  - 5 核心组件 JSDoc：AppToast（经 toast 服务调用不直接 import）/ ListeningPlayer（tracks/seekable/timerPaused）/ WrongAnalysisPanel（questionIds/scopeTitle/unitIds/autoLoad）/ QuestionBankSwitcher（emit changed）/ DictationMode（words）
  - 类型检查 vue-tsc ✅ 零错误
  - **效果**：Antigravity/Codex 改墨题前端时不再猜组件 API、不发明 props、不造平行组件

| 11 | **AI 全栈项目实战**（Summer Checkin 自习室）| ⭐中高 | ✅ 已沉淀 | `AI全栈项目-SummerCheckin自习室平台-2026-08-31.md`。**启发：墨题加聊天/实时推送 → 参考 WebSocket Sidecar；大文件上传 → OSS 预签名直传；AI 模块表设计参考 agentrun/agentstep 审计链** |

## 新增更新记录（2026-08-31）

- #11 Summer Checkin 研究完成：抖音图文「我要成为react大神」第一个全栈 AI Agent 项目（48⭐）。核心增量：**WebSocket Sidecar 方案**（独立服务+Cookie 鉴权+幂等）、**OSS 预签名直传**（减服务器带宽）、**AI Agent 表审计链**（agentrun/agentstep/agentdecision/agenttoolcall 四表落执行轨迹）。模型路由/Agent 编排我们已超越。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
