---
tags: [research, multi-agent, eval, 冒烟测试, daily]
created: 2026-08-31
updated: 2026-08-31
status: adopted
source: eval 冒烟实测 2026-08-31
---

# 多 Agent Eval 冒烟测试报告（N=5）— 2026-08-31

> 目的：验证 harness + grader 无 bug（v3.0 Phase 0 退出条件第一步）。
> 关联：[[多Agent评测基线-20查询-2026-08-31]] · multi-agent-research v2.2

## 一、结果总览

| Query | 类型 | 结果 | 关键指标 | 延迟 |
|:---|:---|:---|:---|:---|
| A1 | 调研（3 个 arXiv ID + 引用）| ✅ PASS | 3 ID 全部 HTTP 200 | 5.5s |
| B1 | 数据（营收降序表）| ✅ PASS | source_untouched=True | 0.3s |
| C1 | 编码（空密码拒绝测试）| ✅ PASS | tests_pass=True | 0.5s |
| D1 | 前端（受控输入框）| ✅ PASS | checks 4/4 | 0.0s |
| E1 | 快速（Python 3.13 特性）| ✅ PASS | peps_found=3 | 0.0s |

**正例 5/5 全 PASS，负例 3/3 正确拒绝**（假 arXiv ID / 乱序数据 / 无 useState 组件）→ harness + grader 逻辑验证通过。

## 二、冒烟抓到的 bug（harness 修复）

| Bug | 根因 | 修复 |
|:---|:---|:---|
| C1 崩溃 `NotADirectoryError` | `run_grader` C 分支把 `artifact_path` 错传为 grader 的 `repo_dir` 参数 | 改为 `spec.get("repo_dir")` |

## 三、harness 产物

| 文件 | 用途 |
|:---|:---|
| `scripts/eval_harness.py` | trial runner + 指标采集（pass/latency/metrics → JSONL）|
| `scripts/grader_arxiv_citation.py` | A 类：arXiv HTTP 200 + fuzzy 引用匹配 |
| `scripts/grader_code.py` | C 类：测试退出码 + lint + 回归 + 越界检查 |
| `scripts/grader_data.py` | B 类：语法 + 数值 diff + 排序 + 源未改 |
| `eval/` | 测试数据（sales.csv）+ 5 个产物 + 结果 JSONL |

## 四、下一步（全量基线）

```markdown
1. 冒烟 ✅（本次）→ 2. 全量 180 run（3 组 × 20 查询 × 3 trial）
3. 单 agent vs 多 agent 对照（A/B/C 组）+ 决策门
4. 读 ≥10 失败 transcript → 确认失败是 agent 真错而非 grader bug
```

**决策门**：多 Agent pass@1 − 单 Agent pass@1 > 10pp 且 p<0.05 → 编排值得；B vs C > 5pp → 验证门值得。

## 五、已知坑

- Windows 管道中 `python -c "...json.load(sys.stdin)"` 因反斜杠转义报错——用 Python 直接调 run_grader 或写临时脚本
- `grader_code.py` 需要 `repo_dir` 参数（目录），不是产物文件路径
- 缺失产物文件会 FileNotFoundError（后续可加友好提示）

---
*由 k 执行：建 harness → 构造产物 → 冒烟 → 负例验证 → 修复 bug → 沉淀。*

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
