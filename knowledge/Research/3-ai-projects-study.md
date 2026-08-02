---
tags: [research, github, project-study, video, hardware, esp32, robotics]
created: 2026-07-31
status: absorbed
---

# 3 个 AI 项目研究（小黑盒文章来源）

> 2026-07-31 · 来自小黑盒文章《GitHub 上翻到了 3 个让室友哇出声的 AI 项目》
> 全部经搜索引擎验证，数据比文章更新

## 1. MoneyPrinterTurbo — 输入标题自动生成短视频 ✅ 已集成

| 项 | 内容 |
|----|------|
| 仓库 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) |
| Stars | **100k**（文章 34.5k 已过时，2026-05 就 61.7k） |
| 语言 | Python (98.5%)，MIT |
| 功能 | 主题/关键词 → 脚本 → 素材 → 配音 → 字幕 → BGM → 高清视频 |
| 用法 | AI Agent / WebUI / API / CLI 四种 |
| 语音 | edge TTS (免费) / Azure / SiliconFlow / MiMo / ElevenLabs / Chatterbox |
| 尺寸 | 竖屏 9:16 (1080x1920) / 横屏 16:9 (1920x1080) |

**已落地**：
- ✅ 官方 Agent Skill 已集成到 Hermes (`skills/moneyprinterturbo-video/`)
- ✅ SKILL.md + mpt_agent.py 已安装，可随时调用

**应用场景**：
- B站 AI 博主内容生产（我们定位！）
- 闲鱼"AI 视频代做"接单
- 批量生成 → 选最优

## 2. xiaozhi-esp32 — 100 元内 AI 语音助手 🔥 高契合待采购

| 项 | 内容 |
|----|------|
| 仓库 | [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) |
| Stars | **28.4k**（文章 2.7k 严重过时） |
| 协议 | MIT（可商用） |
| 硬件 | ESP32-S3 开发板（十几元）+ 扩展板，总成本 <¥100 |
| 技术 | WebSocket/流式 ASR+LLM+TTS，**MCP 协议设备控制** |
| 模型 | Qwen / **DeepSeek**（我们官方 key 可用） |
| 特性 | 声纹识别、25+ 语言、OLED 表情、设备端+云端 MCP |

**为什么高契合**：
- 我们有 DeepSeek 官方 key ✅
- 我们研究过 MCP 协议 ✅
- sora 有嵌入式(8051 skill) + PCB 设计能力 ✅
- MIT 可商用 → 做成品闲鱼卖 ✅

**待行动**：淘宝买 ESP32-S3 开发板（~¥15）+ 麦克风/喇叭扩展板 → 刷固件 → 配 DeepSeek → 语音助手

## 3. OpenDuckMini — 3000 元具身智能双足机器人 🐦 长期项目

| 项 | 内容 |
|----|------|
| 仓库 | [apirrone/Open_Duck_Mini](https://github.com/apirrone/Open_Duck_Mini)（原作者）<br>[Tongjilibo/OpenDuckMini](https://github.com/Tongjilibo/OpenDuckMini)（同济子豪兄中文复刻） |
| 成本 | $400 内（~¥3000） |
| 硬件 | 3D 打印 + 14 舵机 + 树莓派 Zero 2W |
| 技术 | MuJoCo 仿真 + 强化学习平衡 + sim2real + 大模型语音 |
| 教程 | 同济子豪兄 B站视频 + 飞书 wiki 完整教程 |

**价值**：
- 简历亮点：机械设计 + 嵌入式 + 强化学习 + 具身智能
- 毕设/竞赛 Demo
- 3000 元投资较大，需 3D 打印设备 → **长期规划**

## 落地优先级

| 优先级 | 项目 | 行动 |
|:---:|------|------|
| 🔴 P0 | MoneyPrinterTurbo | ✅ 已集成 skill，随时可生成视频 |
| 🟡 P1 | xiaozhi-esp32 | 淘宝采购 ESP32-S3（~¥15），周末刷固件 |
| 🟢 P2 | OpenDuckMini | 存档，评估 3D 打印资源后启动 |

---

*2026-07-31 研究沉淀 · 3 项目全部验证*

---
> 关联: [[github-trending-25-projects]]（小黑盒 25 项目总览） | [[HOME|🏠 首页]]
