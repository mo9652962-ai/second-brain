---
tags: [skill-audit]
created: 2026-08-12
type: audit
---

# 技能审计报告 (2026-08-12)

## 📊 概览
- 内置(bundled): 82 个（不可修改）
- 用户创建(agent): 212 个
- 社区安装(hub): 27 个
- 非内置总数: 239 个

## ✅ 已修复（11 技能）

### 描述修复（YAML >- 块标量 → inline 引号 + 触发词）
| 技能 | 问题 | 修复 |
|:---|:---|:---|
| light-consistency | description: >- 空描述 | 230 字触发词描述 |
| light-figure | 同上 | 同上 |
| light-idea-critique | 同上 | 同上 |
| light-literature-search | 同上 | 同上 |
| light-paper-writing | 同上 | 同上 |
| light-research-ethics | 同上 | 同上 |
| light-research-plan | 同上 | 同上 |
| productivity/service-quality | 同上 | 同上 |

### 短描述补触发词
| 技能 | 原描述 | 新增 |
|:---|:---|:---|
| microcontroller-edge-ai | 仅 30 字 | 加 6 个触发词 |
| modern-web-development | 仅 30 字 | 加 6 个触发词 |
| platform-development | 仅 30 字 | 加 6 个触发词 |
| 前序轮次已升级 7 技能 | 描述优化 | 加触发词 + 负向约束 |

## 🔍 发现

### 重复对（需你确认）
| 重复 | 来源 | 建议 |
|:---|:---|:---|
| 8051-embedded-dev | 顶层 + openclaw-imports/ | 合并（保留顶层，删 openclaw-imports 副本）|
| cad-design-master | 顶层 + openclaw-imports/ | 同上 |
| engineering-workflow | 顶层 + openclaw-imports/ | 同上 |
| web-dev-2026 | 顶层 + openclaw-imports/ | 同上 |
| ai-image-generation | @@okaris + 顶层 | 顶层为旧版，保留 hub 版 |

### 描述无触发词（121 个）
大多数 agent 创建技能描述无触发词——这是下一批优化目标。当前已修复最关键的 11 个（空描述 + 极短描述）。

## 📋 建议操作
- [ ] 合并 4 对 openclaw-imports 重复（删除副本，保留顶层同名技能）
- [ ] 保留 @okaris/ai-image-generation 覆盖顶层旧版
- [ ] 下一轮批量优化 121 个无触发词技能（优先级低，按需处理）

## 说明
- 社区 hub 技能（27 个）未修改——由原作者维护
- 内置技能（82 个）未修改——bundled 不可编辑
- 本次聚焦最高优先级：描述为空/极短导致技能永不被加载的 bug

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
