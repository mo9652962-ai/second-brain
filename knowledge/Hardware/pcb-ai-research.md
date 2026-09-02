---
tags: [pcb, ai, design-automation, research, hardware]
domain: Hardware
status: adopted
---
# PCB 设计与 AI 自动化 · 十轮研究汇总

来源：10 轮搜索引擎研究
更新：2026-07-26

## ① jlcmcp 工具参数详解
- 坐标单位：**mil（密耳）**，1 mil = 0.0254 mm
- 层定义：`layer:1`=顶层，`layer:2`=底层（双层板）
- 走线示例：`pcb_route_track {net:"GND", layer:1, width:8, points:[{x:5000,y:-4000},{x:5200,y:-3800}]}`
- 要求 45° 斜线需在 prompt 中明确

## ② 嘉立创 EDA 扩展开发
- 官方文档：prodocs.lceda.cn/cn/api/guide
- 扩展广场：ext.lceda.cn
- 已有自动化扩展：PCB RBR Autorouter、Design Copilot、MCP Bridge
- jlc-bridge 需勾选「允许外部交互」才能用 WebSocket

## ③ PCB 设计规范

| 项目 | 标准 |
|:-----|:------|
| 最小线宽 | 常规 4mil，高精度 2mil |
| 电源线 | 足够粗，功率走线开窗加锡 |
| 信号间距 | 模拟/数字间距 ≥3 倍线宽 |
| 常用封装 | 0603(1.6x0.8mm), 0805(2.0x1.25mm), 1206(3.2x1.6mm) |
| 四层板叠层 | 信号-地-电源-信号 |

## ④ AI PCB 设计工具
- **KiCad + SKiDL + Cursor**：用 Python 代码生成电路
- **华为 pEDA Space**：云原生，支撑 10 万+ pin，AI 布局布线
- **赛意善谋 PCB 大模型**：基于昇腾 + DeepSeek，10 分钟解析需求文档

## ⑤ jlcmcp 使用流程
1. 启动 relay → 2. 打开 EDA + Enable Bridge → 3. Hermes 操作
- relay 监听 127.0.0.1:18800（仅本地）
- 每次使用前需启动 relay，保持窗口打开
- Bridge 操作前建议备份工程

## ⑥ relay.js 原理
- 67 行 Node.js WebSocket 中继
- 自动分类：首条消息 `hello` → bridge，`command` → mcp
- 按 commandId 路由往返消息
- 替代了官方文档误导的 OpenClaw gateway

---
> 🗺️ 属于 [[MOC-Hardware]] · [[Home|🏠 Home]]
