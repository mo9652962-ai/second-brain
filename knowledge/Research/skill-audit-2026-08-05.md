---
tags: [skill-audit, skill-usage, monthly]
---

# 月度技能使用统计与审计 (2026-08-05)

> 统计区间：2026-08-01 00:00 ~ 2026-08-05 (GMT+8)。数据源：`state.db` 消息记录 + `.usage.json`。

## 📊 概览

| 指标 | 数值 |
|:-----|:-----|
| 本月会话数 | 82 |
| 本月 skill_view 调用 | 148 次（涉及 40+ 技能） |
| 本月 skill_manage 操作 | 76 次（patch 55 / create 14 / write_file 5 / 其他） |
| 技能库总条目 | usage.json 169 个（skills_list 显示 193，含 bundled 嵌套） |
| 已归档技能 | 1 个（ai-xianyu-monetization，07-25） |

## 🏆 本月最常用技能 Top 10（按 skill_view 调用次数）

| # | 技能 | 调用次数 | 涉及会话 | 用途说明 |
|:-:|:-----|:-------:|:-------:|:---------|
| 1 | hermes-automation-patterns | 28 | 10 | cron 可靠性/每日待办（高频 cron 依赖） |
| 2 | daily-knowledge-review | 28 | 18 | 每日知识回顾 cron（含 hermes: 限定名 2 次） |
| 3 | daily-knowledge-absorption-gate | 9 | 9 | 知识吸收守门员 cron |
| 4 | obsidian | 9 | 9 | Obsidian 笔记读写 |
| 5 | sims4-mod-development | 8 | 1 | 联机 mod 开发（单会话高频） |
| 6 | hermes-agent | 7 | 6 | Hermes 自身配置/排障 |
| 7 | obsidian-vault-management | 7 | 5 | Vault 管理 |
| 8 | knowledge-absorption | 6 | 4 | 知识吸收方法论 |
| 9 | arxiv-weekly-digest | 6 | 3 | arXiv 周报 cron |
| 10 | self-improving-agent | 5 | 1 | 自改进学习（本月 patch 15 次，迭代最活跃） |

**本月还被查看过**：sims-4-modding-multiplayer(4)、github-trending-digest(3)、graphify(3)、context-management-bootstrapping(3)、light-research-ethics(3)、vault-suggestion-executor(2)、skill-library-audit(2)、web-search-fallbacks(2)、hermes-search-config(2)、service-quality(2)、sims4-mp-regression-testing(2) 等。

## ✅ 已更新（本月审计 patch，agent-created 技能）

针对过时模型配置内容，本月共 patch 6 个技能 18 处：

1. **hermes-smart-model-router**（6 处）— 全部 `ark-code-latest` 主模型描述 → `deepseek-v4-pro` (custom:fangzhou-2)；头部加 2026-08-05 审计警示
2. **hermes-provider-matrix**（3 处）— fallback 链图主力行、模型名说明、配置命令示例
3. **model-supplier-strategy**（4 处）— 跨商容灾 OpenRouter、主模型行、⑨ 终极备用、按场景推荐表 2 处
4. **hermes-model-fallback**（3 处）— DeepSeek 直连兜底 `deepseek-chat` → `deepseek-v4-flash`（示例+ASCII 图+表格）
5. **low-cost-model-guide**（1 处）— "三路"→"两路"，标注 OpenRouter 已移除
6. **hermes-configuration-patterns**（1 处）— 12.4 节 yaml 示例 `default: ark-code-latest` → `doubao-seed-2-0-pro` + 警示

判断依据（config.yaml 实况）：`model.default` = deepseek-v4-pro / custom:fangzhou-2；`default_model` = doubao-seed-2-0-pro / fangzhou-1；fallback 链 8 层无 ark-code-latest、无 OpenRouter（2026-07-26 移除，402 余额耗尽）。

## 🔍 发现

### 重复对（4 组，建议删除副本）
- `openclaw-imports/{8051-embedded-dev, cad-design-master, engineering-workflow, web-dev-2026}` 与顶层同名技能 **完全一致**（diff 验证）→ 迁移遗留，建议删除 openclaw-imports/ 下副本

### 从未使用（65 个，use_count=0）
- 大部分为 **2026-07-25 批量安装的 hub 技能**（~60 个），其中 4 个 macOS 专用在 Windows 上无意义：`apple-notes`、`apple-reminders`、`findmy`、`imessage` → **建议归档**
- 其他如 airtable/notion/powerpoint/xlsx/pdf 等通用工具技能：保留无害，暂不动
- agent 新建未用：`ai-code-review`(07-31)、`graphify-vault-maintenance`(08-02) → 新建不久，正常

### 观察项
- `fangzhou-ark-config` 已正确记录 ark-code-latest 未部署（无需改）
- `.bundled_manifest` 71 项（非 JSON 格式，`name:hash` 行）——审计脚本需适配
- `hermes-configuration-patterns` L1595 为警示注释语境，正确无需改

## 📋 建议操作（需人工确认）

| 操作 | 对象 | 说明 |
|:-----|:-----|:-----|
| 删除副本 | openclaw-imports/ 下 4 个技能 | 与顶层完全一致，占用目录冗余 |
| 归档 | apple-notes / apple-reminders / findmy / imessage | macOS 专用，Windows 环境不可用 |
| 观察 | 60 个未使用 hub 技能 | 如需精简库可在下月审计后批量归档 |

---
*由月度技能审计 cron 自动生成。下次建议：2026-08-15 双周审计（skill-library-audit）。*

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
