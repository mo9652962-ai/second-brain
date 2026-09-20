---
tags: [ai, rag, knowledge-management, 记忆系统, 腾讯, wiki, github-trending, W38]
aliases: [WeKnora, 微可诺拉, 腾讯知识平台]
date: 2026-09-13
source: https://github.com/Tencent/WeKnora
domain: AI
status: active
---

# WeKnora — 腾讯开源 LLM 知识平台（RAG + Agent + 自维护 Wiki）

**22.7k★（W38 +1,168）** · 把原始文档变成可查询 RAG、自主推理 Agent、自维护 Wiki 的企业级知识框架。Go 为主，2,999 commits · 60 branches · v0.8.0，MIT，微信对话开放平台官方背书（weknora.weixin.qq.com），Trendshift #15289。

## 核心特征

1. **三大能力一体**：RAG 快速问答 + ReAct Agent（自主编排检索/MCP 工具/技能沙箱/网页搜索）+ Wiki Mode（agent 把原始文档蒸馏成互链 markdown 知识库 + 知识图谱 + 手动编辑 + 修订历史 + 一键回滚）。
2. **跨会话长期记忆（v0.8.0）**：profile/preference/fact/task/interest 五类记忆，自动抽取 + 确认，`search_memory` 检索。
3. **⚠️ 记忆检索按查询相关性排序（不是按重要性）**：修复 commit 直言「Importance is uncorrelated with relevance」——旧实现按 importance DESC 选 400 候选再向量打分，导致 400 名之外的记忆永久不可达；新实现直接 `SearchItemsByVector` 对 subject 全量向量排序 + 词法融合（fused），让检索逃出候选池。
4. **Chunk 编辑带修订历史**：检索分片像文档一样可编辑、diff、回滚、自动重建索引。
5. **Skill Sandbox 运行时**：会话持久 Docker / E2B / Cube 沙箱 + 租户网络策略 + 技能目录（ClawHub/SkillHub/git/zip 安装）+ 文件浏览编辑 + 环境变量。
6. **企业级基建**：多租户 RBAC（Owner/Admin/Contributor/Viewer 4 层角色矩阵 + 资源所有权 + 审计日志）、scoped API keys、Langfuse 可观测性、运行时任务队列仪表盘 + worker-pool 治理、多实例存储后端、OIDC。
7. **文档解析**：10+ 格式（PDF/Word/图片/Excel/XMind），anydoc Rust 引擎进程内解析 office（cgo），恶意 PDF 解析开销加线性上界（977KB PDF 26.7s → 5.8ms）。
8. **接入面**：20+ LLM 提供商（含 LiteLLM/Ollama）、多源摄取（飞书/GitLab/Tencent IMA/Notion/语雀/RSS）、IM 渠道（企微/飞书/Slack/Telegram/QQBot）、Chrome 扩展、**官方 DeepSeek Harness 插件**（@wxg-prc-cpg/dsh-weknora）、MCP Server 1.1.x（PyPI tencent-weknora-mcp，29 tools）。

## 技术架构（文字图）

```
文档（PDF/Word/Excel/XMind/飞书/GitLab/Notion/RSS...）
   │  anydoc 进程内解析 / DocReader OCR
   ▼
┌────────────────────────────────────────────┐
│ WeKnora（Go）                                │
│  ├─ 解析 → 分块（3 档自适应）→ 向量化        │
│  ├─ 检索：hybrid search（向量 + 词法融合）    │
│  ├─ ReAct Agent：检索 + MCP + 技能沙箱 + 搜索 │
│  ├─ 长期记忆：五类记忆，按查询相关度排序       │
│  └─ Wiki Mode：蒸馏 → 互链知识库 + 图谱 + 回滚 │
└────────────────────────────────────────────┘
   ├─► IM / Web / Chrome 扩展 / MCP / dsh 插件
   └─► Langfuse 追踪 + RBAC + 审计
```

## 💎 可借鉴点（⭐ 核心价值）

1. **「记忆按查询相关性排序，而非重要性」是记忆系统第一课**。WeKnora 用生产事故证明：importance DESC 的静态排序会漏掉「低重要但高相关」的记忆。sora 的 context-management-bootstrapping 五级记忆（瞬时/会话/任务/核心）是**分层写入**逻辑，WeKnora 给的是**检索排序**逻辑——两者互补：写入按层级、检索按查询相关度 + 词法融合，别让静态优先级卡死召回。
2. **Wiki Mode = 文档自动蒸馏知识库**是 Obsidian 知识库治理的企业级参照：修订历史 + 一键回滚 + 知识图谱，sora 的 knowledge-lint / graphify 可以对照补「版本化」能力（vault 有 git 自动同步，天然可回滚，缺的是「修订历史」UI 层）。
3. **Skill Sandbox = 沙箱化执行 + 技能目录**与 Hermes 的审批/沙箱同思路，tenant skill catalog 的「安装源（ClawHub/SkillHub/git/zip）+ 快照 + 环境变量」可借鉴到 sora 的 external-skill-installation。
4. **⚠️ 部署条件（2026-09-20 修订）**：主要部署方式 docker compose / Helm。此前记录为「本机无虚拟化（Docker 不可用）→ 不部署」，该结论**已过期**：本机虚拟化可用、Docker CLI 已装（v29.8.0），仅 Daemon 未运行（见 [[knowledge/META/current-environment]]）。**修订为**：WeKnora **暂不部署，但原因不再是"不能"**，而是「重量级系统 vs 现有 Obsidian+memory 已够用」的收益判断；若后续启动 Docker Daemon，可低成本试装验证。自托管 RAG 仍可走无 Docker 方案（墨题上云部署方案已有先例）。
5. **安全细节值得抄**：SSRF 与沙箱 URL 守卫共用同一 IP 分类器（防判定不一致）、恶意文档解析开销上界（防 CPU 耗尽）、AES-256-GCM 凭据加密——sora 做 web 服务/安全审计时的 checklist 素材。

## 安装/验证

```bash
# docker compose（生产推荐；本机需先启动 Docker Desktop 使 Daemon 就绪）
git clone https://github.com/Tencent/WeKnora && cd WeKnora
cp .env.example .env && docker compose up -d

# MCP 接入
pip install tencent-weknora-mcp
```

## 总结评价

| 维度 | 评分 | 说明 |
|:--|:--|:--|
| 技术含金量 | ★★★★★ | RAG+Agent+Wiki+记忆四合一，腾讯级工程与安全细节 |
| 关联度 | ★★★★☆ | 直击 sora 知识库治理 / 记忆体系 / RAG（墨题 DashScope） |
| 可迁移性 | ★★★★☆ | 记忆排序原则、修订历史、沙箱目录、安全 checklist 全部可落地 |
| 安装意愿 | ⏸️ 暂缓 | 非"不能装"：本机虚拟化+CLI 已就绪（仅 Daemon 未运行）。收益判断上，重量级系统 vs 现有 Obsidian+memory 已够用，故暂缓 |
| 趋势判断 | 📈 涨 | 知识平台是企业 RAG 刚需，腾讯背书持续吸星 |

关联：`context-management-bootstrapping` · `knowledge-lint` · `obsidian-vault-graph-optimization` · [[knowledge/knowledge-map|知识地图]]
