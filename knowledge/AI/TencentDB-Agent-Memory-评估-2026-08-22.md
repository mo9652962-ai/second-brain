# TencentDB Agent Memory 评估（2026-08-22）

> 来源：抖音「AI产品破壁者-小易」视频（省61% Token / 成功率+51%）+ GitHub/腾讯云官方文档研究
> 项目：https://github.com/TencentCloud/TencentDB-Agent-Memory（MIT 开源，腾讯云数据库团队）
> 关联：已适配 **Hermes Gateway**（TdaiCore + HostAdapter）+ OpenClaw 插件，开箱即跑

## 一、是什么

面向 AI Agent 的分层记忆引擎——把对话/文档/代码沉淀成四类资产（Chat Memory / Skill / LLM-Wiki / Code-Graph），核心是**分层 + 符号化记忆**：

| 层 | 内容 | 用途 |
|:---|:---|:---|
| L0 Conversation | 原始对话/工具日志全量 | 溯源取证（精确措辞/时间戳） |
| L1 Atom | 原子事实/偏好/约束/事件 | 精确召回可执行信息 |
| L2 Scenario | 按项目/场景归纳的知识块 | 快速恢复工作上下文 |
| L3 Persona | 长期画像/稳定模式 | Agent 秒进用户/团队上下文 |

**召回分层**：平时 L2/L3 快速引导（轻），需要具体事实时 BM25+向量+RRF 下钻 L1/L0（重）——结果按条数/字符/超时三重封顶防撑爆上下文。

**符号化短期记忆**：完整工具日志卸载到外部文件（refs/*.md），上下文只留**轻量 Mermaid 任务画布**（node_id 溯源，100% 可找回）——这是省 61% Token 的核心。

## 二、核心数据（官方）

- Token 最高省 **61%**，任务成功率 **+51%**
- 本地部署：SQLite + sqlite-vec 开箱即用；云端：腾讯云 TCVDB
- 混合检索：BM25（zh 用 jieba）+ 向量 + RRF 融合
- 接入：OpenClaw 插件 / Hermes Gateway 适配 / 自研 Agent SDK（召回+写入两步）
- 配置：pipeline.everyNConversations=5 触发 L1、persona.triggerEveryN=50 生成画像等

## 三、对我们的价值评估（Hermes × 联合研究架构）

| 维度 | 评估 |
|:---|:---|
| Hermes 适配 | ✅ 官方 TdaiCore + HostAdapter，接入了就是增强 |
| 与现有记忆体系 | 互补——Hermes 有 memory/skills/session_search，Agent Memory 是**外部记忆引擎**（团队级记忆 Hub + 分层召回），适合多 Agent 共享经验 |
| 省 Token | 61% 对成本敏感（我们 fallback 链+闲鱼成本核算）有价值 |
| 长任务 | **符号化 Mermaid 画布**解决单次长任务信息过载——对千轮研究/大项目有吸引力 |
| 团队记忆 | 多 Agent（k/WorkBuddy/dsh）共享记忆资产——正好服务联合架构 |
| Skill 生成 | Roadmap 中（未完成），与我们 skill-evolution 重叠，等官方做 |

## 四、结论

**值得关注，暂缓接入**——原因：
1. 我们记忆体系已成熟（memory + skills + session_search + Obsidian 知识库），Agent Memory 是「增量优化」不是「必需」
2. 视频的 61%/51% 是官方数据，需在自己场景实测才信
3. 接入成本：需跑本地 SQLite 后端 + Hermes Gateway 适配，属中等工程

**建议触发时机**：① 多 Agent 团队记忆成为痛点时 ② 长任务 token 成本明显上升时 ③ 官方 Skill 自动生成落地后。届时再评估接入。

## 五、技术要点速记（研究价值）

- 存储分层：底层海量事实/日志→数据库（稳定可全量检索）；高层画像/场景/画布→Markdown（白盒可调）——「低层保留证据，高层保留结构」
- 100% 可溯源：任何摘要沿「高层符号 → 中层索引 → 底层原文」链路完美恢复，无不可逆黑盒
- 三套配置档：Level1 日常调参 / Level2 进阶 / Level3 完整参数表（openclaw.plugin.json）
