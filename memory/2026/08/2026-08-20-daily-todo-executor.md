---
tags: [cron, daily-todo-executor, 待办落实, infrastructure]
date: 2026-08-20
status: completed
---

# 🧹 每日待办落实报告 · 2026-08-20（周四）

> 全库扫描 `- [ ]` 待办，处理可自动执行的项，其余列入「需你处理」。

---

## ✅ 已执行（自动处理）

### 1. 修复 cache-hit-monitor cron 挂死（每日复习 P1 项 + 8/18 反思遗留）
- **根因**：jobs.json 中该 no_agent job 的 `script` 字段被误写成 `cache_hit_monitor.py --days 3 --threshold 50`（文件名 + 参数混在一个字段）。Hermes cron 只按裸文件名定位脚本，于是报 `Script not found: ...cache_hit_monitor.py --days 3 --threshold 50`。
- **处置**：
  - 脚本修改：`AppData/Local/hermes/scripts/cache_hit_monitor.py` 默认值改为 `--days 3` / `--threshold 50`（等价于原意图，`argparse` 仍允许 CLI 覆盖）
  - job 修复：`cron/jobs.json` id=58a2481eb588 的 `script` 改回裸文件名 `cache_hit_monitor.py`
- **验证**：json 解析回读 OK（38 jobs）；脚本本地跑 exit 0（命中率达标则静默），下次 23:00 执行应恢复 ok
- **顺带修正**：`scripts/README.md` 登记表曾误记该脚本「已删除/无源码」——实际一直在 `AppData/Local/hermes/scripts/`，实为 cron 字段写错。已更正记录。

### 2. 脚本登记表维护
- scripts/README.md 更正 cache_hit_monitor 条目 + 补充修复过程注释

---

## ⏳ 需你处理（人工决策项，未改动原文件）

| 优先级 | 项 | 说明 |
|:--|:---|:-----|
| 🔴 P0 | 闲鱼上架决策「上架 or 放弃」 | **悬置第 19 天**，素材第 9 次核对 100% 就绪，只差 sora 30min 手动上架 |
| 🔴 P0 | 主 provider 切换（方舟-2 配额耗尽至 08/28） | 功能未中断（fallback 已接管），但建议把 default 切到 jiyuanlvdong 避免单点 |
| 🟡 P1 | 语义缓存最小版落地 | P0 硬截止 8/22；属核心代码改动，需工作会话精改，不宜在 cron 静默动核心 agent |
| 🟡 P1 | health_provider_check.py 加余额阈值告警 | 需按各 provider 余额 API 逐家实现（reflection 已注明「非当场可安全完成」） |
| 🟡 P1 | SRC 侦察收敛（补天 1 有效漏洞，2h 时间盒） | 补天实名审核中，需 s 介入 |
| 🟡 P1 | 墨题巡检 git status 硬检查脚本化 / hermes-health-check 产物 stat 检查 | 脚本开发项，需工作会话 |
| 🟡 | 人工项：PPT 样例导出、零感 AI 付费实测、随身 WiFi 下单、DeepSeek 直连充值、Skill 合并 6 组确认 | 均为 s 手动/决策 |

---

## 📊 统计

| 指标 | 数值 |
|:-----|:-----|
| 扫描文件数（含 `- [ ]`） | 约 180 个 md（全库） |
| 有效待办项（当前活跃） | ~15 项（projects/current + 每日记录） |
| 已自动执行 | 1 项（cache-hit-monitor cron 修复） |
| 需人工决策 | 12 项（列出如上，未改原文件） |
| 评估暂缓 | 3 项（语义缓存/余额告警/巡检脚本——需工作会话，非静默 cron 可安全完成） |

> ⚠️ 系统信号：`deterministic-verify` cron 报 2026-08-19 的 daily-todo-executor 无产物——即本次运行正补上空缺。

---

## 关联
- 项目状态：[[projects/current]]
- 脚本登记表：[[scripts/README]]
- 返回首页：[[HOME]]

---
*由 k (Hermes) · daily-todo-executor cron · 2026-08-20*