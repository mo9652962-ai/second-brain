---
tags: [daily-todo-executor, maintenance, todo-cleanup, cron]
created: 2026-09-07
type: daily-todo-executor
---

# 📋 每日待办落实 · 2026-09-07（周一）

> 生成：daily-todo-executor cron · k (Hermes)
> 今日主线：**闲鱼第 37→38 天状态漂移修复（4 处）+ cad 技能三副本合并落地（9/1 skill-audit 遗留）+ 全库待办分类**

---

## 📊 统计

| 指标 | 数值 |
|:-----|:-----|
| 扫描范围 | 全 vault（排除 .git/.obsidian/模板/系统/归档/历史报告） |
| 含 `- [ ]` 的文件 | **44 个** |
| 原始匹配行数 | 239 行（大部分为模板/参考/backlog，非每日待办） |
| ✅ 本次自动处理 | **5 项**（状态对齐 4 处 + 待办打勾 3 个 + 技能合并 1 组） |
| ⏳ 需 sora 处理 | 8 组（详见下） |
| 📋 模板/参考不修改 | 12 个文件（质检清单/SOP/验收标准/项目 backlog） |
| ⏳ 条件触发 backlog | 10+ 项（保持未勾选，触发器未到） |

## ✅ 已执行

### 1. 闲鱼倒数状态漂移修复（第 37→38 天，4 处）
昨日 vault-suggestion-executor 只更新了 current.md 正文 2 处 + 反思区 1 处，**同文件仍残留 3 处「第 37 天」+ MEMORY.md 1 处**（sibling cron 不对称更新复发）：
- `projects/current.md` L211「悬置第 37 天」→ 第 38 天
- `projects/current.md` L215「悬置第 37 天起」→ 第 38 天起
- `projects/current.md` L262 表格「决策悬置第 37 天」→ 第 38 天
- `MEMORY.md` L232「决策悬置第 37 天」→ 第 38 天
- 验证：current.md 第 38 天 ×6、MEMORY.md 第 38 天 ×1 / 第 37 天残留 0 ✅

### 2. cad 技能三副本合并（9/1 skill-audit L68 遗留，真相核对后落地）
- 验证：顶层 `cad/`（SKILL.md 111 行 = text-to-cad/cad 102 行**严格超集**，仅多「2026 千轮研究增强」9 行）+ `freecad-automation` 子技能 + references/scripts/requirements 与两副本 `diff -r` 全一致
- `text-to-cad/cad/` 与 `text2cad-cad/`（SKILL.md 完全相同）为**纯冗余副本** → `rm -rf` 删除
- 结果：`skills_list` 只剩顶层 `cad` + `freecad-automation`（category: cad），零内容损失 ✅
- skill-audit L68 已标 `[x]` ✅

### 3. Built-but-unchecked 打勾（2 个）
- `knowledge/Productivity/token-usage-report-20260906.md` L103「jiyuanlvdong-2 作为备用链路」→ `[x]`（fallback 链已配置，实测可用）
- `knowledge/cards/2026-09-05-false-positive-tax.md` L41「通用纪律：先自检检测器再动手修」→ `[x]`（已内化：9/5 knowledge-lint 2 检测器 bug 修复实践）

## ⏳ 需 sora 处理（置顶）

| 优先级 | 项 | 说明 |
|:--|:-----|:-----|
| 🔴 P0 | **闲鱼试水决策**（悬置第 38 天） | 一句话二选一（试水 30min 可逆 / 放弃归档），k 侧 100% 就绪，再顺延仅耗注意力 |
| 🟡 P1 | 外部生图修复 | XAI 换 key / FAL 充值 / SILICONFLOW 充值（三路全断） |
| 🟡 P1 | 墨题云服务器选型 | 腾讯云 38/99 或 阿里云 99（花钱决策，P1 商业线阻塞） |
| 🟢 P2 | MCP 解除 | 打开 Obsidian + Local REST API + /mcp reconnect（1min） |
| 🟢 P2 | 微信推送通道凭据 | serverchan/pushplus token（触达升级最后一环）；若明确不用微信则维持现状 |
| 🟢 P2 | 内容类审校 | 内容-Agent操作系统之争-B站初稿（选标题+改口播）、AI 博主 B 站是否启用、harness 抖音脚本 |
| 🟢 P2 | 零感 AI 付费实测 | 1 元/千字实测（涉及小额付费授权） |
| 🟢 P2 | 安全待决策项 | BOLA/IDOR 等（current.md L88） |

## 📋 模板/参考（不修改，每轮扫描均出现）

- `docs/WPS数学练习册标准化优化指南.md` — 质检清单（页边距/字体/跨页等）
- `knowledge/Research/接单工作流-SOP.md` / `论文Pipeline-数据契约.md` — SOP 步骤
- `knowledge/Research/eval-v2-2026-08-31/EVAL_PLAN.md` — 评估标准清单
- `knowledge/Dev/墨题-P0/P1-*.md` — 验收指标
- `knowledge/Dev/cloudbase-learning-s1~s8` / `刷题机*千轮研究` ×5 — 学习/研究文档
- `projects/ai-blogger/*`（content-template/tools-setup）— 项目模板
- `knowledge/Development/复现方案书-SummerCheckin` — 开发任务清单

## ⏳ 条件触发 backlog（保持未勾选）

- false-positive-tax L39/L40（knowledge-lint 加固，触发器=使用>2次/周检报错未到）
- S4MP protocol-version-negotiation L39/L40（项目 backlog，需真机实测）
- xianyu-operation-algorithm L40-44（5 项运营动作，依赖商品上架）
- harness-engineering L43-45（通读论文自查/ACP 跟进，研究任务留会话执行）
- 墨题上云部署 L144-149（依赖 L143 服务器决策）
- memory-portability L38-40 → 已列入 09-08 daily-review 明日行动项（k 可做）
- token-usage-report L101/L102（glm-5 监控/state.db 增长，持续观察）

## 💡 建议

1. **闲鱼试水决策是当前唯一 P0 阻塞**——悬置 38 天已远超 fallback，若 sora 明确不试水，给一句「放弃」，k 归档素材包收尾，避免无限顺延
2. **skill-audit 剩余 2 组待合并**（下轮维护会话处理）：`android-automation` vs `uiautomator2-android-automation`（中英双版重叠）、`hermes-search-config` v1.6.0 vs `hermes-web-search-config` v1.1.0——需逐段 diff 确认覆盖关系后再合并，非纯副本
3. **9/7 反思行动区无新 agent 可做项**（vault-suggestion-executor 已核实）；明日 09-08 daily-review 已排 4 项 k 可做（外部 API 探活 cron / 记忆可移植性抽查 / 墨题 RAG embedding 备份 / 技能蒸馏四篇并读）

---

_生成: daily-todo-executor cron · k (Hermes) · 2026-09-07_

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
