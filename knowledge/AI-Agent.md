---
tags: [ai-agent, openclaw]
created: 2026-07-21
---

# AI Agent 知识库

## 我的 Agent 架构

- **Agent**: k（基于 OpenClaw 2026.7.1-2, build 0790d9f）
- **模型**: deepseek-v4-pro → kimi-k2.6 → qwen3.7-plus → glm-5.2 → mimo-v2.5-pro（视觉回退）
- **Skills**: 26 个（9 论文 + 6 PPT + 7 图片 + 3 自我改进 + 1 搜索）
- **搜索**: Tavily + Firecrawl + Exa 三引擎冗余
- **记忆**: WAL Protocol + Working Buffer + 三层 Memory（向量+图混合架构）

## 核心能力

### PPT 制作
- 6 个 skills 全家桶协同
- 2026 趋势：Async-First、移动端、卡片式、AI 图像
- 支持学术/商业/故事三种叙事框架

### 学术论文
- 9 个 skills 覆盖检索→翻译→润色→SCI 精修
- 知网高级检索 + SCI/SSCI 期刊索引检查

### 图片生成
- 7 个 skills 覆盖文生图、图生图、风格迁移
- 支持中英文提示词

## 配置要点

- 受保护路径 → 直接编辑 `openclaw.json` → `gateway restart`
- 搜索超时 → 120s
- npm 安装 → 先切 npmmirror 镜像

## OpenClaw 生态（2026-07）

- **OpenClaw Foundation**: 2026-07-08 成立，非营利化转型，全职团队 + NVIDIA 合作
- **SkillSpector**: NVIDIA 合作安全扫描，所有 ClawHub skills 自动检测
- **Skill Workshop**: 2026-06-03 上线，技能提案 review/revise/apply/reject 流程
- **版本**: 2026.7.1-2，当前最新稳定版

## 2026 Memory 范式

> Memory 是一等架构组件，不是「塞进 context window 就行」

| 层级 | 方案 | 能力 |
|------|------|------|
| 初级 | RAG only | 基础检索 |
| 中级 | + Memory layer | 上下文持续 |
| 生产级 | + Knowledge Graph + 治理 | 全链路推理 |

- **Vector + Graph 混合**: 向量语义检索 + 图数据库关系推理 → 2026 生产标准
- **Observational Memory > RAG**: LongMemEval 84.23% vs 80.05%
- **新基准**: GraphRAG-Bench / HopRAG（多跳推理）
- **趋势**: VentureBeat 2026 — Contextual Memory 将超越 RAG

### 我的 Memory 架构

```
SESSION-STATE.md (WAL Protocol) → 活跃工作记忆
memory/working-buffer.md → 危险区防丢失
memory/YYYY-MM-DD.md → 每日原始日志
MEMORY.md → 长期 curated 记忆
.learnings/ → Pattern-Key 结构化改进
```

## 安全态势

- **CVE (2026-01)**: 1-click RCE → 48h内修复，当前版本不受影响
- **Command owner**: 尚未配置 `commands.ownerAllowFrom`（需 sora 手动设置）
- **Cross-Component Trust**: 远程节点事件默认 untrusted
- **Session store**: 定期清理孤儿 transcript（已执行：4→2 entries）

## 成本优化策略

- 💰 **低成本模型路由**: 心跳/简单任务用 cheap model，省 60-70% token
- 📦 **Semantic caching**: 嵌入相似度缓存，消除 20-40% LLM 调用
- 🧹 **Session store 清理**: 每月清理孤儿 transcript

## 变现路径

- 🥇 AI PPT 代做（50-500 元/份，6 个 skills 优势）→ 详见 [[PPT-Design]]
- 🥈 学术论文服务（200-800 元/篇）→ 详见 [[Academic]]
- 🥉 AI Agent 定制（3000-15000 元/个）
- 4️⃣ AI 自媒体内容
- 5️⃣ 图片生成接单
- 6️⃣ Skills/SaaS 产品化

---

## 🔗 知识关联

- **[[AI-Workflow]]** — Skill 编排与 Pipeline 设计（如何让 26 个 Skills 自然联动）
- **[[PPT-Design]]** — PPT 制作能力的技术实现与设计方法论
- **[[Academic]]** — 学术检索/阅读/写作全流程
- **[[Vibe-Coding]]** — Agent 运行环境、工具链与系统维护
- **[[projects/current]]** — 当前所有项目的实时状态
- **[[HOME]]** — 返回知识中枢
