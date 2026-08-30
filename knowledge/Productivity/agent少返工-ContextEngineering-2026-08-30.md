# 抖音学习研究：Agent 少返工 80% 的核心方法论（Context Engineering）

> 来源：抖音 @叙白《只需一句话，让你的agent少返工80%》https://v.douyin.com/7gEACgrl24Q/ （89s，973赞）
> 研究日期：2026-08-30 · 方法：元数据抓取 + 千轮搜索

## 视频核心

"只需一句话，让你的 agent 少返工 80%"——背后的真实方法论是 **Context Engineering（上下文工程）**，不是 Prompt 技巧。2026 年 Prompt Engineering 已接近过时，Context Engineering 成为 coding agent 的核心技能。

## 关键概念（搜索结果验证）

### 1. Prompt Engineering → Context Engineering 的范式转移

| 维度 | Prompt Engineering | Context Engineering |
|:---|:---|:---|
| 关注点 | 如何编写有效指令 | 每一轮推理时，把哪些信息以什么结构交给模型 |
| 作用对象 | 一次性指令文本 | 整个上下文状态（工具/MCP/外部数据/历史）|
| 生命周期 | 离散任务：写一次 | 迭代过程：每轮重新决定 |
| 适用 | 单次分类/生成 | 多轮推理、长时间运行的 Agent |

**核心洞察**：Prompt 只能说明"应该怎么做"，不能提供完成任务所需的实时信息。Agent 是持续运行的循环，决定性能的是每一轮"组装进上下文的信息"。

### 2. 上下文腐化（Context Rot）——少返工要防的敌人

Chroma 2025 实测 18 个模型：**token 越多，模型准确回忆信息的能力越低**。上下文是"边际收益递减的有限资源"，不是越大越好。

四个经典失败模式（Drew Breunig）：
- **毒化（Poisoning）**：无关/恶意信息污染上下文
- **分心（Distraction）**：模型被不相关内容吸引注意力
- **混淆（Confusion）**：相似信息冲突导致判断错误
- **冲突（Clash）**：指令互相矛盾

### 3. 四个上手手段（立刻可用）

1. **上下文预算与组装**：放什么/放多少，按优先级分层
2. **JIT 动态加载**（渐进披露）：只保留轻量标识符（文件路径/查询/链接），需要时再加载具体内容——"先给模型目录，它自己决定展开哪页"
3. **Compaction（压缩续跑）**：接近窗口上限时总结成摘要+"最近内容"重新开窗
4. **Contextual Retrieval（chunk 身份证）**：给每个 chunk 加"身份说明"，让向量/BM25 都能看懂

### 4. 成本杠杆：Prompt Caching

- 缓存命中时输入成本约打一折（省 90%）
- 稳定内容放 system（每轮不变→缓存命中），动态内容放 messages（保护缓存）
- 改 system prompt 会让缓存失效——用 system-reminder 注入动态指令

### 5. 2026 最新动态（对我们是重要信号）

- **Anthropic 给 Claude Code 删掉 80%+ 系统提示词，评测不掉点**（2686 词 → 514 词）——旧护栏对新模型是噪音
- **上下文编辑**成为平台级能力：`clear_tool_uses` 清理过期工具结果（单独使用 +29% 性能，配合记忆工具 +39%）
- **Subagent 隔离**：把吵闹操作（全量测试/构建日志）交给子代理独立 context，主 context 只看结构化摘要
- **Harness Engineering 兴起**：2026-02 提出，AI 交互第三阶段（Prompt → Context → Harness）

## 与我们的联合工作映射

| 概念 | 我们的实现 | 差距 |
|:---|:---|:---|
| JIT 渐进披露 | 8 槽密任务包（先给目录再展开）| ✅ 已用 |
| 上下文预算 | 密任务包 8 槽限长 | ✅ 部分 |
| Compaction | session_search 回忆 | ⚠️ 手动为主 |
| Subagent 隔离 | delegate_task 隔离上下文 | ✅ 可用 |
| Prompt Caching | 未主动设计 | ❌ 可优化（cron 提示词稳定化）|
| 上下文编辑 | 未用 | ❌ 新能力待研究 |

## 可执行下一步

1. **cron 提示词稳定化**：把 40 个 cron 任务的 prompt 前缀统一固定（触发缓存命中，省成本）
2. **密任务包升级**：加"上下文预算"槽——明确每轮只给必要信息，不堆历史
3. **子代理隔离推广**：长任务验证/测试跑 delegate_task，主 context 只看结论
4. **研究 Anthropic 上下文编辑 API**：`clear_tool_uses` 是否适用于我们的 provider

## 结论

"少返工 80%"不是靠一句神奇 Prompt，而是靠**上下文治理**：预算化、JIT、压缩、隔离、缓存。我们已在用其中一部分（密任务包、子代理），差距在缓存设计与上下文编辑——这是下一步优化点。
