---
tags: [research, github, trending, daily]
created: 2026-07-31
status: absorbed
---

# GitHub Trending 日报 2026-07-31 — 15 项目研究

> 抓取：github.com/trending?since=daily（12 个）+ since=weekly 补充 3 个 = 15 个
> 方法：GitHub API 验证 star + web_search 验证价值

## 📊 总览（15 个）

| # | 项目 | Stars | 类型 | 决策 |
|:-:|------|:---:|------|------|
| 1 | geo-tp/ESP32-Bit-Pirate | 4.8k | ESP32-S3 硬件黑客工具（24 协议模式） | 🔴 **高契合**（配 xiaozhi/嵌入式方向） |
| 2 | earthtojake/text-to-cad | 12.2k | CAD/CAE/CAM agent skills（build123d） | 🔴 **已装 CAD 技能** |
| 3 | mvanhorn/last30days-skill | 56k | 跨平台 30 天研究（Reddit/X/YT/HN/Polymarket） | 🟡 存档（需 API keys） |
| 4 | agavra/tuicr | 2k | 代码审查 TUI（vim 键位） | 🟡 存档（与 open-code-review 互补） |
| 5 | github/copilot-sdk | 10.1k | Copilot Agent SDK（6 语言） | ⚪ 与 Hermes 定位重叠 |
| 6 | microsoft/AI-For-Beginners | 55k | 微软 AI 入门课程（12 周 24 课） | ⚪ 旧课程，与体系重叠 |
| 7 | chatwoot/chatwoot | 35k | 开源客服平台（Ruby） | ⚪ 与我们无关 |
| 8 | usekaneo/kaneo | 4.8k | 开源项目管理 | ⚪ 我们已有 Obsidian |
| 9 | paperswithbacktest/awesome-systematic-trading | 11.6k | 量化交易资源列表 | ⚪ 存档（不搞量化） |
| 10 | zhaoxuya520/reverse-skill | 10.3k | 逆向/渗透测试技能 | ⚪ 合规风险，存档 |
| 11 | earendil-works/pi | 81.4k | AI agent 工具包（统一 LLM API+TUI） | 🟡 存档（参考架构） |
| 12 | pingdotgg/t3code | 16k | (待查) | ⚪ 存档 |
| 13 | citrolabs/ego-lite | 6.9k | AI agent 浏览器自动化 | ⚪ 我们已有 browser 工具 |
| 14 | different-ai/openwork | 19.2k | Claude Cowork 开源替代 | ⚪ 已研究过 |
| 15 | deepfakes/faceswap / 1jehuang/jcode | 56.8k/14.5k | 换脸/内存高效 harness | ⚪ 已研究过 |

## 🔴 重点落地

### 1. earthtojake/text-to-cad（12.2k★）— 已安装 CAD 技能
- 11 个技能：CAD（STEP-first 参数化）、DXF、URDF、SDF、G-code、CAD Viewer 等
- **技术栈 build123d 与我们 cad-design-master 技能完全一致** → 直接互补
- 已导入 `text2cad-cad` 到 Hermes skills（SKILL.md + scripts + references）
- 价值：自然语言/图片 → 参数化 CAD 模型 → STEP 导出 → 接 3D 打印/闲鱼接单

### 2. ESP32-Bit-Pirate（4.8k★）— 高契合存档
- ESP32-S3 固件 → 24 种协议模式（I2C/SPI/UART/CAN/JTAG/蓝牙/Wi-Fi/RFID）
- Web CLI + Python 脚本 + Web Flasher（浏览器直接刷）
- 与我们：xiaozhi-esp32 方向（ESP32）+ 8051/嵌入式 skill 互补
- 需要：ESP32-S3 开发板（¥15-30）→ 待硬件采购后启用

## 📄 产出
- 技能：`text2cad-cad`（Hermes skills）
- 本笔记存档（15 项目全景）

## 结论
- 15 个项目中 2 个高契合、3 个存档关注、8 个与现有体系重叠/无关、2 个已研究过
- 今日最大收获：**text-to-cad 的 CAD 技能**（与我们的 CAD 方向直接打通）
- 次优：ESP32-Bit-Pirate（待硬件）
