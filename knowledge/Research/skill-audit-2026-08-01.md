---
tags: [skill-audit]
---

# 双周技能审计 (2026-08-01)

## 📊 概览
- 总 Skills: 193 个（skills_list 计数；含分类目录技能）
- 内置(bundled): 69 个（.bundled_manifest）
- 安装(hub): 27 个（@作者 目录，28 个作者目录中 2 个为空）
- 创建(agent): 111 个（顶层 + 分类目录中的 agent 创建技能，含 OpenClaw 迁移）
- 文件系统技能目录: 138 个非 bundled SKILL.md

## ✅ 已更新

### DeepSeek 直连模型名退役同步（8 处，5 个技能）
旧别名 `deepseek-chat` 已退役（2026-07-31 起官方 API 必须用 `deepseek-v4-flash`，见 hermes-model-configuration v0731 更新记录），以下技能仍引用旧名，已全部修正：

| 技能 | 修正内容 |
|:-----|:---------|
| hermes-provider-matrix | fallback 链 ⑧ + YAML 配置示例 `model: deepseek-v4-flash` |
| model-supplier-strategy | 9 级链 ⑧ `deepseek直连 / deepseek-v4-flash` |
| low-cost-model-guide | 价格表 🥉 + 配置清单 + 省钱方案第 3 条（3 处） |
| hermes-smart-model-router | 7 层 fallback 第 8 位 `deepseek-v4-flash` |
| hermes-model-strengths | 模型清单 ⑦ `deepseek-v4-flash` |

### 审计工具
- 新增 `scripts/skill-audit-scan.py`：批量提取非 bundled 技能 frontmatter + 分类清单，供后续审计复用。

## 🔍 发现

### 重复技能（建议合并，待确认后操作）
| 重复对 | 证据 | 建议 |
|:-------|:-----|:-----|
| `ai-image-generation`（顶层，474行，use=11） vs `creative/image-generation-workflow`（263行，use=0） | 内容高度重叠；workflow 版注明"原文件名 ai-image-generation 改名解决重名冲突"但旧文件仍保留 | 保留顶层完整版，删除 creative/ 旧副本 |
| `@guipi888/find-skills`（v1.7.0，场景驱动） vs `@miknasbh-stack/miknas-find-skills`（v1.0.0，SkillKit CLI） | 同为技能发现工具 | 保留 @guipi888（已声明替代官方），归档 miknas 版 |
| `fangzhou-ark-config`（use=2） vs `hermes/fangzhou-ark-setup`（use=0） | 内容几乎相同（方舟 Coding Plan 配置） | 合并到 fangzhou-ark-config |
| `development/android-automation`（use=3） vs `hardware/uiautomator2-android-automation`（use=0） | 同为 adb+uiautomator2 安卓自动化 | 合并到 development/android-automation（含实测记录） |
| `hermes-search-config`（use=57） vs `productivity/hermes-web-search-config`（use=10） | 同主题搜索后端配置，前者中文更完整 | 合并到 hermes-search-config |
| `openclaw-imports/8051-embedded-dev`、`cad-design-master`、`engineering-workflow`、`web-dev-2026`（4 个） | 与顶层同名技能 **diff 完全一致**（OpenClaw 迁移遗留副本） | 删除 openclaw-imports/ 副本（顶层在用） |

### 模型配置类技能重叠（6 个，各有侧重，暂不合并）
`hermes-model-configuration`（564行）/ `hermes-smart-model-router`（271行）/ `hermes-provider-matrix`（166行）/ `model-supplier-strategy`（91行）/ `low-cost-model-guide`（140行）/ `model-capability-reference`（53行）
- 主题重叠（fallback 链/供应商/模型能力），但视角不同（配置实操/路由决策/供应商对比/成本/能力矩阵）。**2026-08 建议**：以 hermes-model-configuration 为主入口，其余技能首部加互链，避免同一事实多处维护。

### 教育类技能重叠（3 个）
`educational-worksheet-generator` / `primary-math-daily-practice`（721行）/ `math-worksheet-generation`（388行）
- 主题重叠（数学练习册生成），但侧重点不同（通用架构 / 40天每日一练 / 人教版标准）。暂不合并，建议以 math-worksheet-generation 为标准引用。

### 空目录（可清理）
- `@evolinkai/`、`@nitishgargiitd/` — 0 条目空目录（skill 已合并删除但作者目录残留）

### 其他观察
- `@miknasbh-stack/` 目录在 skills_list 中显示为 `find-skills`，实际目录名为 `miknas-find-skills`（显示名与目录名不一致）
- SiliconFlow 余额不足(402)问题未写入 `@axdlee/siliconflow-media` 技能（只有通用风险提示），建议补充"余额不足时报 402，需充值/换 DeepSeek 官方 key"
- 2025 年份引用检查：均为合理历史引用（检测研究、期刊影响因子、Stripe API 版本），非过时内容

## 📋 建议操作
1. **清理 6 组重复技能**（见上表）：删除 4 个 openclaw-imports 副本 + creative/image-generation-workflow + miknas-find-skills，合并 fangzhou-ark-setup、uiautomator2-android-automation、hermes-web-search-config 到主版本
2. **清理空目录** `@evolinkai/`、`@nitishgargiitd/`
3. **模型配置 6 技能加互链**，确定单一事实源（hermes-model-configuration）
4. **siliconflow-media 补充 402 故障说明**

> 按审计规则，以上合并/删除操作均需 sora 确认后执行。本次仅完成 8 处过时模型名修正。

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
