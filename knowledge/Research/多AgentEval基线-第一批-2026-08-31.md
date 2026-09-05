---
tags: [knowledge]
title: "多 Agent Eval 全量基线（第一批 + 第二批）— 2026-08-31"
type: note
created: 2026-09-05
updated: 2026-09-05
---

# 多 Agent Eval 全量基线（第一批 + 第二批）— 2026-08-31

> 对照设计：A=单 agent（k 自己）/ B=多 agent（WorkBuddy/dsh 派发）
> 冒烟（N=5）已过：harness + grader 无 bug。本文件记录分批真实派发结果。

## 第一批结果（B 类数据 + E 类快速）

| Query | 执行者 | 产物 | Grader 结果 | 备注 |
|:---|:---|:---|:---|:---|
| B2（JSON 去重）| WorkBuddy（多 agent）| artifact-B2.json（3 条）| ✅ PASS | 去重正确（5→3）|
| B3（12 月合并）| WorkBuddy | artifact-B3.csv（12 行）| ✅ PASS | 数值 1100→2200 与源一致 |
| B4（反馈聚类）| WorkBuddy | artifact-B4.json（3 类）| ✅ PASS | 计数和=9，类互斥 |
| E2（git rebase vs merge）| k（单 agent）| artifact-E2.md（3 条）| ✅ PASS | 互不重复 + 无幻觉 flag |

## 第二批结果（C 类编码）

| Query | 执行者 | 产物 | Grader 结果 | 备注 |
|:---|:---|:---|:---|:---|
| C1（空密码拒绝测试）| k（冒烟已过）| test_empty_pw.py | ✅ PASS | 3 passed |
| C2（修复认证绕过）| WorkBuddy | auth.py 修复 + test_auth_fix.py | ✅ PASS | 2 测试真过 + 行为验证 |
| C3（/healthz 端点）| k | api.py + healthz | ✅ PASS | 200 + status ok |
| C4（mutable default 修复）| k | utils.py + test_utils_fix.py | ✅ PASS | AST 0 残留 + 3 测试 |

## 数据点（第一批 + 第二批）

- **B 组（多 agent）5/5 PASS**（B2/B3/B4/C2 WorkBuddy + 冒烟 A1）
- **A 组（单 agent）5/5 PASS**（E2/C1/C3/C4 k + 冒烟 B1）
- 副作用干净：repo git diff 只触 3 个预期文件 + 2 新增测试
- WorkBuddy 独立配额稳定（今天 6/6 成功）

## 过程记录

- dsh 缺 DEEPSEEK_API_KEY → 无法派发（记录：需要配 key）
- 反重力 agentapi CLI 有 project_id bug → D 类暂用 k 生成 + grader 验证（或人工 IDE）
- WorkBuddy 任务包：B2/B3/B4 三个任务合并一个任务包派发（数据类适合批量）

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
