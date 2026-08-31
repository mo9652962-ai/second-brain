---
title: "Summer Checkin 复现方案书"
type: plan
domain: Development
status: draft
tags: [knowledge/development, ai-agent, rag, 复现方案]
date: 2026-08-31
---

# Summer Checkin 复现方案书

> 目标：评估如何复现「AI 学习平台 Summer Checkin」的核心功能（Agent 智能体 / RAG / 聊天室 / Model Pool）
> 来源研究：`AI全栈项目-SummerCheckin自习室平台-2026-08-31.md`（已 clone 实证，48⭐/MIT）
> 决策待定：sora 确认路线后进入实施

---

## 一、结论置顶

1. **Summer Checkin 可复现，但不应整体照抄**——我们的墨题已覆盖「学习数据层」80%，真正增量只有 3 块：**Agent Runtime（智能体）**、**RAG 知识库**、**WebSocket 聊天室**。
2. **推荐路线：在墨题上加 3 个增量模块**（成本约 2-3 周兼职），而不是从零复刻 Next.js 项目（成本 2-3 个月）。理由：墨题已有登录/题库/练习/统计/日历/AI 对话/每日限额，Summer 的「打卡/计划/番茄钟」与墨题 Goal/Calendar/Focus 功能重叠。
3. **最大技术债风险在 pgvector**：墨题用 SQLite，Summer 用 PostgreSQL+pgvector。两个选择：墨题换库（大工程）或 RAG 用「SQLite 存文本 + 内存/文件做余弦相似度」轻量替代（Summer 自己 retriever.ts 就是 JS 余弦，说明向量检索可以不做数据库原生）。
4. **Agent Runtime 是最有价值的复刻**：Observe→Analyze→Plan→Execute 四步循环 + AgentRun/AgentStep/AgentDecision 审计表，这个设计可平移到墨题的「AI 学习管家」。
5. **Model Pool 直接抄**：Summer 的 403 降级/429 冷却机制是我们 Hermes fallback 链的精细版，代码 MIT 可直接参考。

---

## 二、功能差距矩阵（Summer vs 墨题 vs 复现策略）

| Summer 模块 | 墨题现状 | 差距 | 复现策略 |
|:---|:---|:---|:---|
| 用户认证 | ✅ auth.py（含管理员） | 无 | 不动 |
| 打卡 Checkin | 🟡 Goal/Calendar 有目标日历 | 无「打卡+心情+连续天数」 | 低优先：日历视图已有，补打卡接口 |
| 学习计划 Plan/PlanTask | 🟡 Goal 有目标管理 | 无「文档→AI 拆任务」 | **中**：Plan 表 + AI 拆任务接口 |
| 番茄钟 StudyRecord | ✅ FocusView 专注页 | 完成自动记录 | 补：专注记录落库 |
| 统计可视化 | ✅ Dashboard/Report | 近7天趋势/学科分布 | 低：已有类似 |
| **Agent Runtime** | 🟡 AiAssistant 对话 + ai_recommend 规则推题 | **无自主循环** | **高优先：核心增量** |
| **RAG 知识库** | ❌ 无 | **从零** | **高优先**（轻量版） |
| **WebSocket 聊天室** | ❌ 无 | **从零** | 中优先（sidecar 方案现成） |
| Model Pool | 🟡 ai_client 有模型列表/切换 | 无自动降级链 | **低**：直接移植 model-pool.ts |
| Markdown 编辑器 | ❌ 无 | 从零 | 低：第三方库（md-editor-v3） |
| OSS 直传 | ❌ 无 | 从零 | ⚪ 跳过（本机部署不需要） |
| 多场景主题 | ✅ 墨题已有主题 | 无 | 不动 |

---

## 三、架构设计（墨题增量版）

```
浏览器 (Vue3)
   │
   ├─ HTTP ──► FastAPI（墨题现有 :8765）
   │              ├─ /api/agent/*     ← 新增：Agent 四步循环
   │              ├─ /api/rag/*       ← 新增：知识库上传/检索
   │              └─ 现有路由不动
   │
   ├─ WebSocket ──► 新增 sidecar（:8766，FastAPI 独立进程或 uvicorn app）
   │                  ├─ 聊天室广播
   │                  └─ @AI 流式回复（SSE 或 WS 分块）
   │
   └─ SQLite（墨题现有 question_bank.db）+ 新增 rag_chunks 表
```

### 3.1 数据库设计（新增表，不动现有表）

| 表名 | 用途 | 关键字段 | 参考 Summer |
|:---|:---|:---|:---|
| `agent_runs` | Agent 运行记录 | id/user_id/mode/status/goal/max_steps | AgentRun |
| `agent_steps` | 四步循环明细 | run_id/step_type/status/input/output | AgentStep |
| `agent_decisions` | 决策记录 | run_id/type/priority/reason/status | AgentDecision |
| `agent_tool_calls` | 工具调用审计 | run_id/tool_name/args/result/success | AgentToolCall |
| `user_memories` | 长期记忆 | user_id/type/content/importance/confidence | UserMemory |
| `knowledge_docs` | 知识库文档元数据 | user_id/source_name/source_type/size | KnowledgeDoc |
| `knowledge_chunks` | 文档分块 | doc_id/chunk_index/content/embedding(JSON) | DocumentChunk |
| `chat_messages` | 聊天室消息 | user_id/content/role/created_at | ChatMessage |
| `token_usage` | token 记账 | user_id/surface/tier/model/tokens | TokenUsage |

> 全部用 SQLite 兼容类型（TEXT/INTEGER/REAL/JSON），不引 PostgreSQL。

### 3.2 RAG 轻量方案（避开 pgvector）

Summer 的 retriever.ts 实际是 **JS 余弦相似度**（非数据库向量检索），验证了轻量路线可行：

```
上传 md/pdf/docx/txt
  → splitText（500字+50重叠 / 按##分片）
  → 调 embedding API（阿里百炼 text-embedding-v4 或硅基流动）
  → 存 SQLite knowledge_chunks.embedding = JSON数组
检索：
  → 查询词 embedding → 全表余弦相似度 topK
  → 数据量 <1万 chunk 时性能可接受（Python 全表扫描 <100ms）
```

> 若未来 chunk 超 5 万，再考虑换 pgvector 或 sqlite-vec 扩展（SQLite 有 `sqlite-vec` 可装）。

### 3.3 Agent Runtime 设计（核心增量）

```
runLearningAgent(userId)
  ├─ Step1 observe:    并行收集 目标/计划/练习统计/错题/词汇/打卡（墨题全有！）
  ├─ Step2 analyze:    LLM 分析学习状态（基于墨题真实数据）
  │                       └─ 失败兜底：规则引擎（薄弱题型统计）
  ├─ Step3 plan:       LLM 生成行动列表（JSON 结构化）
  └─ Step4 execute:    按 action type 调工具
                          ├─ CREATE_TASK → 写 todo
                          ├─ ADJUST_PLAN → 改目标
                          ├─ SEND_REMINDER → 生成通知
                          ├─ GENERATE_REPORT → 生成学习报告
                          └─ RECOMMEND_QUESTIONS → 调现有 ai_recommend 推题
```

**关键差异**：Summer 的 Agent 面向「学习计划」，墨题的 Agent 面向「刷题数据」——数据源换成墨题已有的题库/练习/错题/词汇，这个反而是**更强**的应用场景（有真实高频数据）。

### 3.4 Model Pool 移植

直接参考 `model-pool.ts` 移植为 Python：

```python
class ModelPool:
    HIGH_CHAIN = [{"model": "agnes-2.5-flash", "provider": "agnes"}, {"model": "qwen3.7-max...", "provider": "aliyun"}, ...]
    LOW_CHAIN = [{"model": "agnes-2.5-flash"}, {"model": "qwen-flash..."}]
    
    def __init__(self):
        self.exhausted = set()          # 403 永久禁用（进程内）
        self.rate_limited_until = {}    # 429 冷却 60s
    
    def is_quota_error(self, err): ...  # 403/429/quota/balance 识别
    def with_fallback(self, tier, fn):  # 逐个尝试，降级
```

> 墨题已有 ai_client 的模型列表/切换，只需加「自动降级链」+「429 冷却」。

---

## 四、分阶段计划（推荐 3 阶段）

### Phase 1：Agent Runtime + Model Pool（核心，约 1 周）
- [ ] 新增 5 张 agent 表（runs/steps/decisions/tool_calls/memories）
- [ ] 移植 model_pool.py（403 降级 + 429 冷却）
- [ ] 实现 observe（收墨题数据）/analyze/plan/execute 四步
- [ ] Agent 页面（前端 agent-workspace 类似 Summer）
- [ ] 验证：mock 数据跑通 3 次完整循环

### Phase 2：RAG 知识库（约 4 天）
- [ ] 上传接口（md/pdf/docx/txt 解析，Python: pypdf/python-docx）
- [ ] chunk 分片（500+50 / ## 语义分片）
- [ ] embedding 接入（复用 ModelPool 的 embedding 档）
- [ ] 检索接口（余弦 topK）+ 文档问答
- [ ] 前端知识库页面

### Phase 3：WebSocket 聊天室（约 4 天）
- [ ] FastAPI WebSocket 端点（或独立 sidecar :8766）
- [ ] 聊天室广播 + 在线人数 + 心跳
- [ ] @AI 流式回复（LOW 档模型池）
- [ ] 「温柔宝/嘴欠宝」双人格（可选，有意思但非必需）

**总计约 2-3 周兼职。** 相比从零复刻（2-3 个月）省 80%。

---

## 五、风险与对策

| 风险 | 对策 |
|:---|:---|
| SQLite 并发写（聊天室高频） | 聊天室消息走 WAL 模式 + 批量落库；或独立 sidecar 用内存队列 |
| embedding API 成本 | 用 ModelPool 的免费档（agnes/百炼免费额度）；chunk 缓存 |
| 全表余弦慢（chunk>5万） | 换 sqlite-vec 扩展或降级 pgvector |
| Agent 幻觉（乱改计划/乱推题） | 沿用 Summer 的 AgentApproval（人工审批）机制 |
| 墨题现有功能被破坏 | 只加表不加改；新模块独立路由前缀 /api/agent /api/rag |

---

## 六、可选增强（Summer 没有、我们可以有）

1. **Agent 推题闭环**：Agent 分析错题 → 直接调 ai_recommend 生成针对性练习 → 学生做完回流统计 → 下轮 Agent 看效果。Summer 的 Agent 只能改计划，我们的能直接推题，闭环更强。
2. **学习周报**：Summer weekly.ts 是纯统计（不依赖 LLM），墨题 Report 页可直接加「周报视图」。
3. **长期记忆**：UserMemory 表 + 记忆提取（从对话/打卡中提取偏好），Agent 注入上下文。

---

## 七、决策请求

请 sora 确认：

1. **路线**：墨题增量（推荐）还是独立复刻？
2. **范围**：全做（Agent+RAG+聊天室）还是只做 Agent（最小可用）？
3. **时间**：现在开工 Phase 1，还是先存方案书以后排期？

---
> 🗺️ 属于 [[MOC-Development]] · 关联 [[AI全栈项目-SummerCheckin自习室平台-2026-08-31]] · [[Home|🏠 Home]]
