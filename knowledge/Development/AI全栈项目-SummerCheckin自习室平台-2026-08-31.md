---
title: "AI全栈项目-SummerCheckin自习室平台-2026-08-31"
type: note
domain: Development
status: active
tags: [knowledge/development, ai-agent, rag, vibecoding]
source: "https://v.douyin.com/BU25cuBXgJs/"
date: 2026-08-31
---

# Summer Checkin：AI 驱动的自习室学习平台（Vibe Coding 大赏作品）

> 来源：抖音图文「我要成为react大神」《我的第一个全栈 AI Agent 项目。技术使用篇》
> 热度：713 赞 / 46 评论 / 528 收藏 / 91 分享（2026-08-31 抓取）
> 作者：我要成为react大神（粉丝 148，获赞 6760，疑似广工学生 gdut4140）
> 发布时间：2026-08-30 20:30:33

## 一句话

作者第一个完整 AI 全栈项目：**AI 学习平台 Summer Checkin**——把学习计划、番茄钟、打卡、AI Agent、RAG、实时聊天室串起来，已部署可在线体验。

- 在线体验：http://8.148.146.16/（HTTP，已验证 200 ✅）
- GitHub：https://github.com/gdut4140/summer-checkin（48⭐ / 6 fork / 49 commits / MIT，2026-08-31 实测）

## 技术架构（7 大核心亮点）

| # | 模块 | 技术方案 |
|:--|:---|:---|
| 1 | 全栈架构 | Next.js + TypeScript + Prisma + PostgreSQL，Docker + Nginx 部署 |
| 2 | Agent Runtime | **Observe → Analyze → Plan → Execute** Agent Loop；AI 读学习计划/任务/打卡/专注记录 → 分析状态 → 生成 Action 并执行 |
| 3 | RAG 知识库 | Markdown/PDF/DOCX 导入 → Chunk → Embedding → **pgvector** 相似度检索 → 基于用户资料回答 |
| 4 | WebSocket 聊天室 | 独立 **WebSocket Sidecar**：Cookie 鉴权、在线人数、消息广播、幂等；支持 @AI 流式回复 |
| 5 | Model Pool | 按任务选模型 + **备用模型链**；额度耗尽/429 自动切换，降成本 |
| 6 | Markdown 编辑器 | 编辑/阅读/沉浸式学习同一空间 |
| 7 | OSS 直传 | 阿里云 OSS 预签名 PUT，浏览器直传，减服务器带宽压力 |

另有：长期记忆、AI 学习报告、任务拆解、动态壁纸、3D 学习小岛（three.js）。

## 数据模型（26 张表）

- 用户认证：user / session / account（Better Auth + scrypt 哈希）
- 学习核心：plan / plantask / todo / checkin / studyrecord
- AI 智能体：agentrun / agentstep / agentapproval / agentdecision / agenttoolcall / usermemory / aihistory / conversation / conversationmessage
- 聊天室：chatmessage
- 知识库：document / documentchunk / knowledgedoc / plantemplate / documenttemplate
- 其他：notification / agentschedule / tokenusage

## 工程亮点（从 commit 历史看出的好习惯）

1. **死代码清理**：删除从未接入的 Milkdown/Recharts（-1870 行 lockfile），README 同步更新
2. **性能优化实证**：背景图 PNG 2MB+ → WebP 80-130KB；three.js 小岛改 next/dynamic ssr:false；头像 OSS 服务端缩放
3. **安全**：OSS AccessKey 仅存服务端、浏览器预签名直传；.gitignore 忽略密钥文件；docker-compose app 端口仅绑 127.0.0.1（nginx 唯一公网入口）
4. **AI Agent 落地**：AI 消息落库带 userId（ai-gentle/ai-snarky 双雨宝角色）、RAG embedding batch 25→10 优化
5. **AGENTS.md / CLAUDE.md**：AI 友好文档化（与我们组件库文档化方法论一致）

## 对我们（k + sora）的启发

| 项目亮点 | 我们的对照 | 可借鉴 |
|:---|:---|:---|
| Model Pool + 备用链 | Hermes fallback 链（fangzhou-2 → jiyuanlvdong-2）| 已超越 ✅ |
| Agent Loop (O-A-P-E) | multi-agent 研究（Observe→Analyze→Plan→Execute 同构）| 已超越 ✅ |
| RAG + pgvector | 知识库 Obsidian + 记忆系统 | 半超越：可参考文档 Chunk 策略 |
| WebSocket Sidecar | 墨题无实时功能 | ⭐ 新：墨题若加聊天/实时推送可参考独立 sidecar 方案 |
| OSS 预签名直传 | 墨题文件上传走服务端 | ⭐ 新：大文件上传可参考浏览器直传减带宽 |
| 26 表 schema 设计 | 墨题后端 | 可参考 AI 模块表设计（agentrun/agentstep 审计链）|

**结论**：作者是 Vibe Coding 实战派，工程习惯好（清理死代码、性能优化、安全兜底），项目完整度高于一般 demo。对我们是**验证级参考**——我们的模型路由/Agent 编排已超越，真正增量在 WebSocket Sidecar、OSS 直传、AI Agent 表审计链设计。

## 代码级实证（2026-08-31 clone 实测）

仓库已 clone 到 `~/summer-checkin-review` 验证（48⭐/6 fork/MIT/49 commits）：

### 1. Model Pool（`src/lib/model-pool.ts`，398 行）— 我们最该借鉴的

- **三级分档**：HIGH（agent/文档 studio）/ LOW（聊天室/标题/记忆）/ EMBEDDING，每档一条候选链
- **403 额度耗尽 → 自动降级到链上下一模型**；429/rate limit → 60s 冷却后恢复（不永久禁）
- `maxRetries=0`：SDK 不重试已耗尽模型，错误直接抛给模型池切换
- 流式场景用 `peelFirstChunk` 提前暴露 403，再合成「首块+剩余」流
- 思考类模型注入 `extra_body.enable_thinking`（否则只出 reasoning_content 不出正文）
- **对照**：与 Hermes fallback 链思路一致，但多了「限流冷却 vs 永久耗尽」的精细区分——Hermes 只有整链 fallback，没有 per-model 冷却表。这是可借鉴点

### 2. Agent Runtime（`src/lib/agent/runtime.ts`，886 行）— 结构清晰

- 四步独立函数：`observe`（并行收数据）→ `analyze`（LLM 诊断）→ `plan`（结构化 JSON 行动）→ `execute`（按 action type 调工具）
- LLM 失败有**基于规则的分析兜底**（不依赖模型也能跑）
- 每个决策落 `AgentRun + AgentStep + AgentApproval`（全链路可追溯）
- 5 种 action：ADJUST_PLAN / CREATE_TASK / SEND_REMINDER / GENERATE_REPORT / ENCOURAGE

### 3. WebSocket Sidecar（`server/index.ts`）— 独立进程方案

- 独立进程监听 3001，HTTP 仅健康检查 + WS 升级
- **升级阶段鉴权**：握手前校验 Cookie，401 直接拒绝（不建连再踢）
- 连接级去重 `seenClientIds`（幂等），心跳保活

### 4. RAG（`src/lib/rag/chunk.ts`）— 双策略分片

- `splitText`：固定 500 字 + 50 重叠，先按段落分割避免切句子
- `splitMarkdown`：按 `##` 标题语义分片（Markdown 专属）
- bge-m3 上限 8192 tokens，500 字 chunk 留足余量

## 元信息

- 话题：#全栈 #Agent #ai #vibecoding #vibecoding大赏
- 发布时间：2026-08-30
- 抓取时间：2026-08-31 22:40（Playwright 拦截 RENDER_DATA 成功）

---
> 🗺️ 属于 [[MOC-Development]] · [[Home|🏠 Home]]
