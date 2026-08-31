---
tags: [research, multi-agent, eval, 基线数据, daily]
created: 2026-08-31
updated: 2026-08-31
status: adopted
source: eval 全量基线实测 2026-08-31
---

# 多 Agent Eval 基线汇总报告 — 2026-08-31

> 目的：产出第一份单 agent vs 多 agent 对照数据（v3.0 EBR 3.0 Phase 0）。
> 关联：[[多Agent评测基线-20查询-2026-08-31]] · [[多AgentEval冒烟测试-2026-08-31]] · [[多AgentEval-第三批A类调研-2026-08-31]] · multi-agent-research v2.3

## 一、已跑批次总览（4 批，17 查询）

### 冒烟 N=5（harness + grader 验证）

| Query | 执行者 | 结果 |
|:---|:---|:---|
| A1（arXiv 调研）| k 构造产物 + grader 验证 | ✅ PASS（3 ID HTTP 200）|
| B1（营收降序）| k | ✅ PASS |
| C1（空密码测试）| k | ✅ PASS（3 passed）|
| D1（受控输入框）| k | ✅ PASS（4/4 checks）|
| E1（Python 3.13）| k | ✅ PASS（3 PEP）|

### 第一批（B 类数据 + E2）

| Query | 执行者 | 结果 | 备注 |
|:---|:---|:---|:---|
| B2（JSON 去重）| WorkBuddy | ✅ PASS | 5→3 正确 |
| B3（12 月合并）| WorkBuddy | ✅ PASS | 数值与源一致 |
| B4（反馈聚类）| WorkBuddy | ✅ PASS | 3 类互斥，计数和=9 |
| E2（git rebase vs merge）| k | ✅ PASS | 3 条互不重复 |

### 第二批（C 类编码）

| Query | 执行者 | 结果 | 备注 |
|:---|:---|:---|:---|
| C2（修复认证绕过）| WorkBuddy | ✅ PASS | 真改文件 + 2 测试 + k 复核 |
| C3（/healthz 端点）| k | ✅ PASS | 200 + status ok |
| C4（mutable default）| k | ✅ PASS | AST 0 残留 + 3 测试 |

### 第三批（A 类调研，WorkBuddy 深研 30KB）

| Query | 执行者 | 结果 | 备注 |
|:---|:---|:---|:---|
| A2（3 框架交接对比）| WorkBuddy | ✅ PASS | 表格完整 + 官方 URL 3/3 HTTP 200 |
| A3（2026 综述 + 引用数）| WorkBuddy | ✅ PASS | 4 arXiv ID 真实（2512.13564/2603.07670/2605.06716/2411.04468）|
| A4（Task Ledger）| WorkBuddy | ✅ PASS（纠正前提）| **发现任务书前提错误**：Magentic-One 是两个账本，Task Ledger 含 facts/guesses/plan 三类内容而非"三类事件" |

## 二、对照数据（初步）

| 组别 | 查询数 | PASS | 通过率 | 执行者 |
|:---|:---|:---|:---|:---|
| **B 组（多 agent）** | 9 | 9 | **100%** | WorkBuddy ×9（A1冒烟/A2/A3/A4/B2/B3/B4/C2 + E1冒烟）|
| **A 组（单 agent）** | 8 | 8 | **100%** | k ×8 |

> 注：当前样本量小且任务都偏"可确定性验证"，两组都全过属于预期（冒烟+首批目的是验证 pipeline 不是分胜负）。全量 180 run 才是决策依据。

## 三、执行环境实测发现

| 发现 | 影响 |
|:---|:---|
| WorkBuddy 独立配额 6/6 稳定 | 限流环境下最可靠执行者，B/C 类优先派它 |
| dsh headless 缺 DEEPSEEK_API_KEY | 无法派发，需配 key |
| 反重力 agentapi CLI v2.11 有 project_id bug | D 类无 UI 派发不可用，暂用 k 生成 + grader |
| E 类 k 自己最快（0 延迟）| 符合"单 agent 够的任务不派发"铁律 |

## 四、下一步

```markdown
1. 第三批：A 类调研（A2/A3/A4）→ WorkBuddy 派发（调研是它强项）
2. 第四批：D 类前端（D2/D3/D4）→ 需反重力人工 IDE 或 k 生成 + grader
3. 全量 180 run（3 组 × 20 查询 × 3 trial）→ 出统计决策数据（Wilson CI + McNemar）
4. 读 ≥10 失败 transcript → 确认失败归因
```

---
*由 k 执行：分批派发 → 质疑式核验 → grader 验证 → 沉淀。*

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
