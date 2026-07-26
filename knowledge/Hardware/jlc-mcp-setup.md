# JLCPCB MCP · 嘉立创 EDA AI 自动化

来源：GitHub hyl64/jlcmcp (161⭐) + 社区教程
状态：已安装配置完成

## 架构

```
Hermes ──MCP──→ jlcmcp (38 tools) ──WebSocket──→ relay.js ──WebSocket──→ 嘉立创 EDA
```

## 组件

| 组件 | 位置 | 用途 |
|:-----|:------|:------|
| **jlcmcp MCP Server** | `C:\Users\31954\jlcmcp\dist\index.js` | 38 个 PCB/原理图工具 |
| **relay.js** | `C:\Users\31954\jlcmcp\relay.js` | WebSocket 中继（替代 OpenClaw gateway） |
| **jlc-bridge.eext** | `C:\Users\31954\jlcmcp\jlc-bridge\build\` | EDA 扩展插件（已安装） |

## 使用流程

每次使用前：

1. 双击桌面 `start-jlc-relay.bat`（启动 relay）
2. 打开 嘉立创 EDA 专业版 → 打开 PCB 工程
3. 菜单 → JLC Bridge → Enable Bridge
4. 在 Hermes 中操作 PCB

## 38 个工具分类

- 状态查询 (9)：pcb_get_state / pcb_screenshot / pcb_run_drc
- 元件操作 (6)：pcb_move_component / pcb_batch_move
- 走线/过孔 (4)：pcb_route_track / pcb_create_via
- 铺铜/禁布 (4)：pcb_create_copper_pour
- 丝印 (3)：pcb_auto_silkscreen
- 差分对/等长 (6)：pcb_create_diff_pair
- 原理图 (3)：sch_get_netlist
- 计算器 (2)：calc_impedance / calc_trace_width
