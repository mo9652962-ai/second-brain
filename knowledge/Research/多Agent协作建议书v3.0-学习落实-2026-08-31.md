---
tags: [research, multi-agent, 建议书, 证据审计, daily]
created: 2026-08-31
updated: 2026-08-31
status: adopted
source: agent协作演进建议书-v3.0 + 证据审计附录（2026-08-31）
---

# 多 Agent 协作演进建议书 v3.0 学习落实 — 2026-08-31

> 流程：k 学习两份文档（v3.0 建议书 + 证据审计附录）→ 审计现有体系传播的错误说法 → 纠错 → 吸收 v3.0 增量 → 技能 v2.0。
> 关联：`multi-agent-research` v2.0 · [[多Agent协作增强-千轮研究-2026-08-30]]

## 一、纠错清单（审计附录点名，已落实）

| 错误说法 | 处置 |
|:---|:---|
| "Princeton 64% / +2.1pp / 2x cost" | ❌ 未找到原始出处 → 技能 + 知识库已删除归因，换 equal-budget 对照（arXiv 2604.02460）条件性表述 |
| "MARCH 幻觉率大幅下降" | ⚠️ 过强 → 技能改为"信息不对称/RAG 场景设计启发，非生产效果承诺" |
| CASS 3-5 组合 knockout / 90%/85% Judge / 42% 共享文件 / 60-90% 缓存 | 均已在建议书中降级为待验证/条件性——我们技能未引用这些，无需改 |

## 二、v3.0 吸收增量（已入技能 v2.0）

1. **证据分级**（A 官方/B 论文/C 预印本/D 内部）——每条结论标注等级
2. **TBHC v3 任务契约**——密任务包升级为状态化授权信封（objective/scope/budget/success_criteria/幂等/过期/产物身份）
3. **验证门 G0-G4**——G1 交接核验扩展为五道门（含 G3 副作用前 Action Broker）
4. **RACIV 2.0**——增加 V（Verifier），A 分域不默认 k，执行/审批/证据/审查四权分离
5. **统计纪律**——N=5 只冒烟 / pass^1+pass^k / 95% CI / CI 跨 0 标不确定

## 三、尚未落地（30 天路线图候选）

- Action Broker 原型（参数化授权替代 shell 包装器）——D8-D14
- SQLite/WAL 黑板 + fencing token 租约——D8-D14
- 约 20 个代表性 eval 查询 + 基线报告——D1-D7
- Wiki provenance（valid_from/contradicts/supersedes + shadow index）——D15-D30

## 三、工程化落地（同日执行，v2.1）

### 4 项工具全部就位并验证

| 工具 | 位置 | 验证结果 |
|:---|:---|:---|
| Action Broker 原型 | `scripts/action_broker.py` | ✅ deny-by-default / 黑名单拒绝 / 全链路 submit→approve→execute→audit |
| SQLite 黑板 + fencing | `scripts/blackboard.py` | ✅ 租约互斥 / 旧 epoch 拒绝 / 幂等命中 / 读写正常 |
| 20 查询 eval 基线 | `knowledge/Research/多Agent评测基线-20查询-2026-08-31.md` | ✅ WorkBuddy 设计，5 类×4，3 个 deterministic grader，Wilson CI 计划 |
| Wiki provenance | `scripts/wiki_provenance.py` | ✅ 504 笔记扫描：359 缺必填 / 489 缺 provenance / 231 零引用候选 |

### 评测决策门（下次跑基线用）

```markdown
冒烟 N=5 → 全量 180 run（3 组 × 20 查询 × 3 trial）→ 读 ≥10 失败 transcript
→ 多 Agent − 单 Agent > 10pp 且 p<0.05 → 编排值得
→ B vs C（无门消融）> 5pp → 验证门值得
```

---
*由 k 执行：学习→审计→纠错→吸收→沉淀。技能 v1.7 → v2.0 → v2.1。*

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
