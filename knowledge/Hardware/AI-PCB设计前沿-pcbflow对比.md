---
tags: [千轮研究, pcb, AI设计, pcbflow, 验证门控]
domain: Hardware
status: fresh
date: 2026-08-21
---

# AI PCB 设计前沿：PCB Flow 12 阶段 + KiCad AI 助手（千轮研究 2026-08-21）

> 来源：NijoP/pcbflow（AI PCB 设计工作流）+ paul356/KiCad-AI-Assistant + Siemens Xpedition AI 自动化

## PCB Flow 12 阶段（可对照我们的 AI PCB 工作流）

```
需求 → 可行性 → BOM → EasyEDA 建项目 → AI 原理图 → 工程审查
→ 布局规划 → 可视化布局图 → 自动布局 → KiCad 导出 → AI 布线 → 验证 → 制造
```

**核心思想**：
- **每阶段一个检查点**——PASS/CONDITIONAL/FAIL 判定，FAIL 阻断下一阶段
- **「可回放 90%，人掌判断 + 不可逆操作」**——AI 做重复劳动，人做工程决策
- **验证门控全机械**：ERC 0 错误 / DRC 0 错误 / DFM JLCPCB 档 / 丝印 0 压盘 / 大电流走线铺铜
- **布线在 KiCad 不做 EasyEDA**（pcbnew/kicad-cli 可脚本化铺铜/DRC）
- 路由规则表每条**引用来源**（IPC-2152/IPC-2221/JLCPCB）——不是拍脑袋

## 对照我们的工作流（ProtoFlow → KiCad → DeepPCB → JLCPCB）

| 维度 | 我们已有 | PCB Flow 可借鉴 |
|:---|:---|:---|
| 草图 | ProtoFlow（RESET/LED 修正）| 可行性检查（密度/电流层数判断）|
| 原理图 | SKiDL/KiCad | 网表重建审查（读回真实板子验证）|
| 布局 | 半自动 | 布局知识图 + 可视化布局图（先批准再执行）|
| 布线 | KiCad | 规则表带来源引用（IPC 标准）|
| 验证 | DRC | 每阶段门控 + DFM + 丝印 + 大电流检查 |

**最大启发**：① 布局前先生成「可视化布局图」给客户/自己批准；② 验证门控前置到每阶段（不是最后一次性）。

## KiCad AI Assistant（可考虑集成）

- KiCad 插件内嵌 LLM chat + MCP server
- 工具：原理图编辑/网表提取/封装库搜索/布局评分/DRC/版本快照/技能系统
- **布局评分** `score_placement` + 建议顺序 `suggest_placement_order` ——正好补我们布局自动化缺口

## 关联

- `pcb-design` / `kicad-automated-pcb` / `skidl-schematic-automation` 技能
- 记忆：AI PCB 工作流（ProtoFlow→KiCad→DeepPCB→JLCPCB）

---
> 🗺️ 属于 [[MOC-Hardware]] · [[Home|🏠 Home]]
