# SOP 知识库索引（Hermes Learning Loop）

> 体系: 借鉴 Nous Research Hermes Agent 闭环自进化 + 程序性技能架构
> 目标: 将日常探索/多步试错/排障经验沉淀为高价值 SOP，跨会话能力复利
> 建立: 2026-08-19

## SOP 标准 Schema（5 维）

```
① ID & Category         唯一标识 + 分类（DEV 开发 / OPS 排障 / DATA 数据 / RES 研报 / SEC 安全）
② Prerequisites & Triggers  前置条件（环境/工具/依赖）+ 触发场景
③ Action Sequence       确定性执行步骤（按序无歧义）
④ Verification Criteria 验证/验收边界（客观依据）
⑤ Gotchas & Recovery    已知报错模式 + 修复策略
```

## SOP 清单

| SOP ID | 分类 | 名称 | 状态 | 最近触发 |
|:---|:---|:---|:---|:---|
| SOP-001 | OPS | [[SOP-001-fault-diagnosis\|复杂多步故障排查与根因修复]] | Active | 2026-08-19 |
| SOP-002 | RES | [[SOP-002-deep-research\|技术与研报深度调研自闭环]] | Active | 2026-08-19 |
| SOP-003 | OPS | [[SOP-003-dsh-upgrade\|dsh 升级（npm 12 ETARGET 绕道）]] | Active | 2026-08-19 |
| SOP-004 | SEC | [[SOP-004-src-recon\|SRC 资产侦察标准流程]] | Active | 2026-08-19 |
| SOP-005 | OPS | [[SOP-005-miniapp-audit\|小程序反编译密钥审计]] | Active | 2026-08-19 |
| SOP-006 | DEV | [[SOP-006-ai-code-review\|AI 代码审查协作流程（Gemini 第二意见）]] | Active | 2026-08-19 |
| SOP-007 | RES | [[SOP-007-knowledge-empowerment\|知识赋能：知识库手册/复盘蒸馏为实战技能]] | Active | 2026-08-22 |

## 文件结构

```
knowledge/SOP/
  SOP-INDEX.md               ← 本文件（索引 + 演进日志）
  SOP-001-fault-diagnosis.md
  SOP-002-deep-research.md
  SOP-003-dsh-upgrade.md
  SOP-004-src-recon.md
  SOP-005-miniapp-audit.md
  SOP-006-ai-code-review.md
  SOP-007-knowledge-empowerment.md
  archive/                   ← 归档区（60 天未触发）
```

## Evolution Log（演进日志）

| 日期 | SOP | 变更类型 | 变更原因与详情 | 维护者/状态 |
|:---|:---|:---|:---|:---|
| 2026-08-19 | SOP-001 | 新建 | 初始化排障与根因定位标准工作流 | k / Active |
| 2026-08-19 | SOP-002 | 新建 | 初始化深度技术研报与交叉验证工作流 | k / Active |
| 2026-08-19 | SOP-003 | 新建 | dsh rc.6→rc.7 升级踩坑（npm 12 ETARGET bug 手动绕道）| k / Active |
| 2026-08-19 | SOP-004 | 新建 | 联想 SRC 第一轮侦察全流程（391 子域→48 存活→16 深挖）| k / Active |
| 2026-08-19 | SOP-005 | 新建 | 微信小程序反编译+密钥审计流程（unveilr 链）| k / Active |
| 2026-08-19 | SOP-006 | 新建 | Gemini 代码审查协作闭环（9 项发现→验证→修复→测试→push）| k / Active |

## Governance（治理规范）

```
🔄 巡检周期: 每 7-14 天一次知识库健康度审查
🔀 合并原则: 同类问题重合度 > 70% → 合并为单一泛化 SOP
📦 归档准则: 连续 60 天未触发 或 依赖技术栈废弃 → 移入 archive/
```

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
