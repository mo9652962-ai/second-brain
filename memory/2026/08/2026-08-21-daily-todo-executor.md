---
tags: [cron, daily-todo-executor, daily-maintenance]
date: 2026-08-21
status: completed
---

# 🧹 每日待办落实报告 · 2026-08-21（周五）

> 全 vault `- [ ]` 扫描（排除 .git/.obsidian/site/skills/archive）、分类过滤、可自动执行项直接落地。
> 依据 8/20 反思机制：**「agent 可执行项直接跑而非只提醒」**（8/4 起"反思≠执行"第 4 次复发的根治执行）。

---

## ✅ 已执行（自动处理，2 项 P0/P1 反思行动项）

### 1. P0 语义缓存最小版 —— **真落地（硬截止 8/22 前完成）**
**根因**（为何"已落地"却判"未落地"）：`plugins/web/search_cache.py` 早在 8/17 提交，但**只接入 tavily provider**；而实际搜索常因 Tavily 配额 432 走 exa/searxng/firecrawl 兜底 → 缓存从未触发（`~/.hermes/cache/web_search_cache.json` 从未生成）。所以 8/20 反思判"未落地"准确。

**修复**：在 `tools/web_tools.py::web_search_tool()` 的**统一 chokepoint**（L722 `provider.search()` 处）加两级缓存（exact + n-gram 近似），覆盖**全部 8 个后端**，无论流量走哪个都去重。全 try/except 包裹，缓存异常自动回落 live search，绝不阻塞主流程。

**验证**：mock provider 实测 —— 首个 query 写缓存文件 → 同 query 二次 `_cache_hit=true`(exact)。近似命中 0.773<阈值0.80 不命中（正确设计）。
**提交**：`hermes-agent` 分支 `feat/smart-routing` · commit `84d813bf2`（已本地提交，未 push 官方 upstream）。

### 2. P1 health_provider_check.py 余额阈值告警
**关键洞察**：中转站（keylink/jiyuanlvdong/tokenrhythm）**无独立余额端点**，余额枯竭直接体现在 HTTP 错误体里（如 `剩余额度: ¥0.05`）。

**实现**：`scripts/health_provider_check.py` 新增 `_balance_flag()`，解析 HTTP 402/403/429 错误体中的 "额度/余额/quota/suspended/insufficient balance" 词 → 自动追加 `[⚠️余额告警]`。workspace 与 hermes-health-check skill 双副本同步，skill 判读节已补充文档。
**验证**：7/7 单测通过；实跑探测：`custom:kimi`（suspended）与 `custom:fangzhou-2`（quota 8/28 重置）被正确标红。
**附带发现**：**keylink 已恢复 OK**（预算 ¥0.05 裸奔解除）——实测 6718ms OK。

---

## 📊 统计

| 指标 | 数值 |
|:---|:---|
| 扫描到含 `- [ ]` 的 md 文件（排除 site/skills/archive） | **90 个** |
| `- [ ]` 中属真实待办（projects/current.md + MEMORY.md 为主） | ~45 条 |
| 其余（约 95%） | Skill 检查清单 / SOP 模板 / 研究追踪项 / dreaming 压缩语料 —— 文档正常内容，**不改动** |
| 本次自动执行并标记 `[x]` | **2 条**（P0 语义缓存 ×2、P1 余额告警） |
| 改动文件 | hermes-agent/web_tools.py（提交）、health_provider_check.py ×2 副本、projects/current.md×3、hermes-health-check skill |

---

## ⏳ 需你处理（人工决策，未改原文件）

### 🔴 闲鱼变现（连续顺延第 19 → 决策悬置第 20 天）
- [ ] **上架「AI 代做 PPT」**：素材 `outputs/xianyu-master/上架素材包/` 100% 就绪，30min 复制即上架 → 决策「上架 or 放弃」
- [ ] 同步上架「论文排版/润色」+「数学练习册」文案（现成）
- [ ] 补 PPT 样例页（需手动从 pptx 导出）+ 小红书引流首篇

### 🟡 待 sora 一句话确认
- [ ] Skill 重复合并 6 组（合并方案已备好，说"确认合并"即执行）
- [ ] 随身 WiFi 下单（赫电 Pro 399/年）
- [ ] 桌面美化部署（TranslucentTB + Rainmeter 就绪）
- [ ] SRC 侦察收敛（P1，8/20 反思项，仍开放）

### 🟡 遗留 agent 可执行 P1（本次未做，留 next 轮或按需）
- [ ] 墨题巡检 git status 硬检查脚本化（未提交改动即报警）
- [ ] hermes-health-check 加产物 stat 检查（产出型 cron 当日文件缺失即告警，不标全绿）

---

## 附注
- 语义缓存后续验证：若 Tavily 配额仍复发，确认 `web.backend` 未被手动固定 + 检查 `~/.hermes/cache/web_search_cache.json` 有写入。
- P0 语义缓存代码 8/17 已存在但未生效——**本次根因（只在 tavily provider 挂了缓存）已根治**；8/20 反思判"未落地"得到证实并闭环。

_生成: 2026-08-21 20:15 | 由 daily-todo-executor cron 自动触发_