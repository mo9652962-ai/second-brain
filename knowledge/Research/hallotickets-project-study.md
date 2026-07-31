---
tags: [research, project-study, hallotickets, android-automation, uiautomator2]
created: 2026-07-31
status: absorbed
---

# HalloTickets 项目研究 — 工程模式吸收

> 2026-07-31 · 对 `Joho6666/hallotickets`（大麦抢票自动化）的完整研究
> 结论：**功能不采用，工程模式全吸收**（已落地 `hermes-automation-patterns`）

## 项目概况

| 项 | 内容 |
|----|------|
| 仓库 | [Joho6666/hallotickets](https://github.com/Joho6666/hallotickets)（currycan/HaTickets 改名 fork） |
| 用途 | 基于 Android 真机的本地自动化：控制大麦 App 抢票 |
| 技术栈 | Python 3.10-3.13 + Poetry + UIAutomator2 + adb |
| 演进 | Web(Selenium 已移除) → Desktop(已废弃) → **Mobile(UIAutomator2 主推)** |
| 规模 | 199 commits，CI 覆盖，pytest 测试，文档齐全 |

## 为什么功能不采用

1. **平台风控**：大麦有 x-sign/x-mini-wua 等加密签名防线（逆向分析证实），对抗升级是猫鼠游戏，模拟器必被风控，真机也有封号风险
2. **法律/合规**：黄牛倒票违法；代抢票是闲鱼封禁的灰色服务，与正规接单业务冲突
3. **项目自身免责**：DISCLAIMER 明确"仅供学习研究，风险自负"

## 吸收的 4 个工程模式

### 1. 语义化退出码（U-12）
- `0` 成功 / `10` 可重试 / `11` 不可重试（防重复副作用）/ `12` 配置设备错误 / `130` 用户中断
- 编排器按 `>=10` 判定运行层结果，pre-flight 失败固定 `1-4`
- **核心价值**：可重试 vs 不可重试的区分，防止自动重启造成重复下单/重复副作用

### 2. 危险操作安全分离（probe/commit）
- `--probe` 安全探测：走到"立即购买"前停，绝不点击下单
- `--commit` 正式执行：唯一真实下单旗标，打印摘要 + 倒数 3 秒 + Ctrl-C 可取消
- 漏敲 `--probe` 直接报错退出（不静默降级）→ 资金误操作防护

### 3. 机器可读运行摘要（run_summary.json）
- 每次运行原子写 JSON（outcome/exit_code/mode/attempts/duration_ms）
- 写失败只记 warning 不影响退出码
- 固定路径 = "最近一次 run"语义，`--result-json` 可覆盖保留历史

### 4. AI 自然语言 → 配置生成（run_from_prompt）
- `summary`（只解析不写）→ `apply`（生成配置）→ `probe`（配置+安全探测）三步分离
- "给张三李四抢 4 月 6 号张杰北京站内场 1680 元" → 结构化 config.jsonc

## 落地位置

- Skill: `hermes-automation-patterns` → `references/exit-code-orchestration.md`（完整规范 + 落地映射）
- 落地映射：闲鱼上架 probe/commit、git push dry-run、批量删除清单预览、export_traces.py 加 --result-json

## 延伸：UIAutomator2 安卓自动化

项目证明了 UIAutomator2 直连真机 App 的成熟度。sora 的 AI 自动化 6 领域（Office/编程/修图/工程/视频/硬件）暂无安卓自动化——这是一个可探索的新方向（合法合规场景：App 自动化测试、信息采集、辅助操作）。

---

*研究完成 2026-07-31 · learn→research→apply 全流程*
