---
tags: [research, self-evolution, agent, skills, ACL-2026]
created: 2026-08-12
type: research
---

# AI Agent 自我进化前沿研究 · ACL 2026 千轮研究

> 研究于 2026-08-12：ACL 2026 长文 + arXiv 2026 最新论文，覆盖技能生成/图结构/协同进化/记忆管理

## 结论置顶

**Agent 自我进化的核心范式已从"单通道技能积累"转向"多通道协同进化"：技能图 + 反模式记忆 + 工具协同 + 量化验证。**

## 1. SkillDAG：技能图结构（ACL 2026）

将技能库组织为**有向无环图**，边类型：
- **prerequisite**（前置依赖）：技能 A 需要技能 B 先执行
- **specialization**（特化）：技能 A 是技能 B 的特化版本
- **composition**（组合）：技能 A 和 B 常一起使用
- **conflict**（冲突）：技能 A 和 B 不应同时使用

**双视角嵌入**：`self`（技能做什么）vs `needs`（技能需要什么）——恢复跨功能桥接。
**在线编辑协议**：`propose-edge` → `edit-edge`（实验证明后才提交），三个不变性（无环/无矛盾/可回滚）。

**落地**：技能间显式关系，避免"技能膨胀→上下文污染"。

## 2. SkillGen：验证驱动的技能生成（ACL 2026）

**对比归纳**：同时分析成功和失败轨迹，提取"成功有但失败没有"的关键模式。
**经验验证门（Verification Gate）**：候选技能在部署前必须通过**配对验证**（同一任务有/无技能的对比）——净效果为正才部署。
**最佳-of-K 选择**：多轮细化后选验证集净收益最大的候选，而非最后一轮。

**落地**：失败后先对比成功与失败轨迹 → 提取模式 → 在验证集上确认收益 → 写入技能。

## 3. SkillSmith：技能-工具协同进化（ACL 2026）

**原子化提议包**（Bundle）：一次变异**同时修改技能和工具**（工具操作：WRAP/EDIT/COMPOSE/SPLIT/RETIRE）。
**Lotka-Volterra 生态效用**：技能间交互矩阵（互补/竞争）——技能变异优先级不仅看自身性能，还看是否抑制邻居、重复能力、缺乏必要互补。
**反模式记忆**：记录失败签名 + 归因 + 修复方案；新变异先检查是否匹配已知模式 → 匹配则否决。

**落地**：技能膨胀时先检查工具层是否需要修复而非扩技能；记录失败签名防重复犯。

## 4. COVE：协调式自我进化（ACL 2026）

**双通道协调**：harness-based（外部记忆/技能——快速但浅）vs parameter-based（权重更新——慢但深）。
**任务感知路由**：根据任务特征/反馈/失败信号分配进化通道。
**阶段性调度**：性能平台/数据充足/冷启动失败三个触发条件决定何时切换通道。
**知识反背诵**：防止模型记忆不稳定知识。

**落地**：简单修复用技能更新（harness），深层模式用参数更新（需更多计算）。

## 5. AgeMem：统一记忆管理（ACL 2026）

**记忆操作工具化**：ADD/UPDATE/DELETE/RETRIEVE/SUMMARY/FILTER 作为 agent 可控工具。
**三阶段渐进训练**：先学 LTM → 再学 STM 控制 → 最后协调两者。
**Step-wise GRPO**：解决记忆操作带来的稀疏不连续奖励问题。

## 对 Hermes Agent 的启发

| 方向 | 可落地 |
|:---|:---|
| 技能间关系图 | 在 skills/ 目录加 `depends:` 字段，暴露技能图 |
| 对比归纳学习 | 失败时自动对比成功与失败轨迹，提取模式链入技能 |
| 反模式记忆 | 记录失败签名 + 归因，新方案匹配已知模式时提示 |
| 工具-技能协同 | 技能膨胀时优先检查工具层是否需要修复 |
| 经验验证门 | 技能更新前在验证集上确认净收益为正 |

## 来源

- Feng et al. 2026. SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents. ACL 2026.
- Yang et al. 2026. EVOTOOL: Self-Evolving Tool-Use Policy Optimization. ACL 2026.
- FLUXMEM / COVE / AgeMem. ACL 2026.
- SkillGen / SkillDAG / SkillSmith. arXiv 2026.

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
