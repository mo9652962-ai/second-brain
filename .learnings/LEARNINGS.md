# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260722-001] best_practice

**Logged**: 2026-07-22T14:15:00+08:00
**Priority**: high
**Status**: resolved
**Area**: config

### Summary
Plan-and-Execute 模式 + 异构模型架构：Frontier 模型负责规划和复杂推理，cheap model 执行高频任务，综合降本 90%

### Details
来自 MachineLearningMastery 2026 趋势分析：
1. **Plan-and-Execute Pattern**: 强大模型制定策略 → 便宜模型执行 → 降本 90%
2. **异构架构三层级**: Frontier models (复杂推理/编排) → Mid-tier (标准任务) → SLMs/Small models (高频执行)
3. **成熟模式**: 语义缓存 (0.92 阈值嵌入相似度) 消除 20-40% LLM 调用
4. **企业落地关键**: 识别高价值流程 → agent-first 重设计 → 明确成功指标 → 持续改进
5. **OpenClaw 实践**: 当前 fallback 链 (pro→kimi→qwen→glm) 已实现线性降级，但缺少 task-aware 路由

### Suggested Action
- 将 task-aware model routing 纳入架构改进（简单任务自动路由到更便宜模型）
- explore: cron/heartbeat 用 qwen3.7-plus 或 glm-5.2 而非 deepseek-v4-pro
- 评估 semantic caching 可行性

### Metadata
- Source: web_search
- Tags: cost-optimization, plan-and-execute, heterogeneous-architecture, model-routing
- Pattern-Key: config.plan-execute-pattern
- Recurrence-Count: 1
- First-Seen: 2026-07-22
- Last-Seen: 2026-07-22

### Resolution
- **Resolved**: 2026-07-25T11:32:00+08:00
- **Notes**: 已实施异构建模降本（主力 pro→flash -68%）、心跳模型 mimo-v2.5、跨供应商 fallback 链。Plan-and-Execute 核心思想已落实为 cron/心跳隔离 + 低成本模型 tiering。Task-aware routing 为下一跳改进方向。

---

## [LRN-20260722-002] insight

**Logged**: 2026-07-22T14:15:00+08:00
**Priority**: high
**Status**: completed
**Area**: docs

### Summary
2026 AI Agent 开发范式转型：Prompt Engineering → System Engineering。焦点从提示词技巧转向 guardrails、feedback loops、observability

### Details
1. **核心转变**: 2026 年 AI 开发不再靠更好的 prompt，而是靠健壮的系统架构
2. **系统工程三要素**: Guardrails (行为边界) + Feedback Loops (自纠正循环) + Observability (可观测性)
3. **Bounded Autonomy**: 清晰的操作限制 + 必须的人工升级路径 + 完整审计追踪
4. **验证我们的方向正确**: 
   - ✅ .learnings/ + Pattern-Key = Feedback Loop
   - ✅ ADL/VFM Protocol = Guardrails
   - ✅ Daily notes + MEMORY.md 追溯体系 = Observability
   - ✅ Skill Workshop + skill-vetter = Safety guardrails

### Suggested Action
- 在架构文档中显式标注每个组件的「系统工程属性」(Guardrail/Feedback/Observability)
- 增强 observability：定期 review session logs 的自动化
- 评估是否需要更正式的 feedback loop 指标（如每次改进后的成功率变化）...## [LRN-20260905-001] insight

**Logged**: 2026-09-05T12:14:00+08:00
**Priority**: high
**Status**: completed
**Area**: config
**Summary**: OpenClaw 2.0 ���� (v2026.8.1) �����򻯰�װ��Э�� Agent ������Local-First �� Model-Agnostic �����ƶ��๩Ӧ�� fallback �����йܼܹ������� Agent �������ܡ�
**Details**: ���� Tavily �����ͽ����ԸĽ��о���OpenClaw 2.0 ���˰�װ���̣���ǿ��Э���������û��ƶ����ݱ��ػ��Ϳ�ܶ����ԣ�OpenClaw �Ŀ繩Ӧ�� fallback �������й��������ϣ����� Agent �� Claude Code��Devin��Cursor ��Ϊ��������ѡ��
**Suggested Action**: �ڼ�������������ʹ�� coding agent skills������ά���๩Ӧ�� fallback ���������� cron ������ʹ�ø����˵�ģ�͡�
**Metadata**: Source: tavily_search + self-improvement cron
Tags: openclaw-2.0, local-first, model-agnostic, coding-agent
Pattern-Key: config.openclaw-2.0-release
Recurrence-Count: 1
First-Seen: 2026-09-05
Last-Seen: 2026-09-05
