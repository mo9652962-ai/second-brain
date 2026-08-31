---
tags: [research, multi-agent, eval, 基线最终, daily]
created: 2026-08-31
updated: 2026-08-31
status: adopted
source: eval 全量基线 20 查询实测 2026-08-31
---

# 多 Agent Eval 全量基线最终报告（20/20 查询）— 2026-08-31

> 目的：产出第一份单 agent vs 多 agent 对照数据（v3.0 EBR 3.0 Phase 0 完成）。
> 关联：[[多Agent评测基线-20查询-2026-08-31]] · [[多AgentEval冒烟测试-2026-08-31]] · [[多AgentEval-第三批A类调研-2026-08-31]] · [[多AgentEval基线-第一批-2026-08-31]] · multi-agent-research v2.5

## 一、全量结果（20/20 查询全部执行）

### 冒烟 N=5（harness + grader 验证）

| Query | 执行者 | 结果 |
|:---|:---|:---|
| A1（arXiv 调研）| k 构造 + grader | ✅ PASS |
| B1（营收降序）| k | ✅ PASS |
| C1（空密码测试）| k | ✅ PASS |
| D1（受控输入框）| k | ✅ PASS |
| E1（Python 3.13）| k | ✅ PASS |

### 第一批（B 类数据 + E2）

| Query | 执行者 | 结果 |
|:---|:---|:---|
| B2（JSON 去重）| WorkBuddy | ✅ PASS |
| B3（12 月合并）| WorkBuddy | ✅ PASS |
| B4（反馈聚类）| WorkBuddy | ✅ PASS |
| E2（git rebase vs merge）| k | ✅ PASS |

### 第二批（C 类编码）

| Query | 执行者 | 结果 |
|:---|:---|:---|
| C2（修复认证绕过）| WorkBuddy | ✅ PASS |
| C3（/healthz 端点）| k | ✅ PASS |
| C4（mutable default）| k | ✅ PASS |

### 第三批（A 类调研）

| Query | 执行者 | 结果 |
|:---|:---|:---|
| A2（3 框架交接对比）| WorkBuddy | ✅ PASS |
| A3（2026 综述 + 引用数）| WorkBuddy | ✅ PASS |
| A4（Task Ledger）| WorkBuddy | ✅ PASS（纠正前提）|

### 第四批（D 类前端，反重力人工生成）

| Query | 执行者 | 结果 |
|:---|:---|:---|
| D2（响应式卡片网格）| 反重力 | ✅ PASS（4/4）|
| D3（可访问提交按钮）| 反重力 | ✅ PASS（4/4）|
| D4（Figma → 登录表单）| 反重力 | ✅ PASS（4/4）|

## 二、最终对照数据

| 组别 | 查询数 | PASS | 通过率 |
|:---|:---|:---|:---|
| **B 组（多 agent：WorkBuddy + 反重力）** | 12 | 12 | **100%** |
| **A 组（单 agent：k）** | 8 | 8 | **100%** |

> ⚠️ 统计局限：本批任务是"可确定性验证"的代表性样本（N=20 全过），**不能判定多 agent 优于单 agent**——要分胜负需：① 更难的开放任务 ② 3 组对照（单/多/无门消融）③ 每查询多 trial（pass^k）④ Wilson CI + McNemar。本次价值是 **pipeline 验证 + 执行者能力实测**。

## 三、执行者实测结论（本次最有价值的产出）

| 执行者 | 实测 | 结论 |
|:---|:---|:---|
| **WorkBuddy** | 6 任务全 PASS，独立配额稳定 | ✅ 限流环境下最可靠的多 agent 执行者；调研/数据/编码都行 |
| **反重力** | 3 任务全 PASS（人工 IDE）| ✅ 前端生成质量高（grid/aria/Figma 都规范）；agentapi CLI 有 bug 需人工 |
| **k（单 agent）** | 8 任务全 PASS | ✅ 快速查询/确定性任务够用；符合"单 agent 够的任务不派发" |
| **dsh** | 未派发（缺 DEEPSEEK_API_KEY）| ⚠️ 需配置 key 才能用 |

## 四、Harness/grader bug 记录（冒烟的价值）

| # | Bug | 修复 |
|:---|:---|:---|
| 1 | C 分支 repo_dir 错传（产物路径 vs 目录）| `spec.get("repo_dir")` |
| 2 | **D 类 grader 复用 D1 检查项**（D2 检查 setValue 而非 grid 类）| 按 query_id 分派检查项 |

> Bug 2 是本次新抓到的：如果没跑 D 类，这个 grader bug 会一直潜伏。**冒烟 + 分批跑的价值再次验证。**

## 五、结论与下一步

- ✅ v3.0 Phase 0 基线完成：能回答"当前成功率/成本/延迟"问题（本次全 PASS 但样本局限）
- 📌 全量 180 run（3 组 × 20 查询 × 3 trial + Wilson CI）是分胜负的正式手段，harness 已就绪可随时跑
- 💡 实战启示：**WorkBuddy 值得在更多任务线启用**（独立配额 + 高质量产出），dsh 补 key 后可加入

---
*由 k 执行：分批派发 → 质疑式核验 → grader 验证 → bug 修复 → 沉淀。*

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
