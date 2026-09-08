---
tags: [cad, mcp, ai-automation, research, 千轮研究]
type: note
created: 2026-09-08
---

# CAD 自动化 MCP 参考（pascal/editor 实证，2026-09-08）

> 来源：pascalorg/editor（22.4k★，MIT）深度研究——WebGPU 3D 建筑编辑器，原生内置 31 个 MCP 工具 + CLI。
> 价值：这是「AI 驱动 CAD/设计工具」的现成范本，直接可借鉴到 sora 的 CAD/PCB 自动化方向。

---

## 一、核心设计：MCP 语义工具层（最关键）

**不是给 AI 原始 patch 接口，而是语义化「建造」工具**——让 AI 用自然语义操作，而非猜数据结构。

### 31 个 MCP 工具分类（读源码实证）

| 分类 | 工具 | 用途 |
|:---|:---|:---|
| **① 语义建造**（AI 主用）| create_room / furnish_room / add_door / add_window / create_wall / create_level / place_item / cut_opening / set_zone / duplicate_level / delete_node | AI 直接「建房间/开门/放家具」 |
| **② 校验定案闭环** | validate_scene / check_collisions / door_clearance / layout_clearance / measure / geometry | AI 建完自查：碰撞/净空/尺寸 |
| **③ 收尾链** | validate_scene → verify_scene → save_scene → get_project_status（返回 editorUrl 交回人确认）| 全自动闭环 + 人工交接点 |
| **④ CRUD/状态** | get_scene / get_node / find_nodes / apply_patch / undo / redo / export_glb / export_json / live_sync | 读改查、兜底 patch、导出 |

### 设计要点（可直接抄）
1. **语义工具为主，patch 兜底**——AI 大部分操作走 create_room/add_door 这类语义工具（免猜数据结构），apply_patch 只作兜底
2. **校验工具闭环**——建完必须 validate/check，AI 不能盲建
3. **人工交接点**——`editorUrl` 让 agent 把草稿链接交回给人确认，人审后再继续
4. **undo/redo 内建**——AI 改坏了可回退（像 git checkout .）

---

## 二、Headless Core 设计（AI 接口能跑的关键）

**Core 不 import Three.js/GPU 依赖** —— 纯数据计算，让 Node/MCP 侧只 import 数据层。

```
apps/editor       # Next.js 宿主（编辑器壳）
packages/
  core/           # 节点 schema(Zod) + store + 事件总线 —— 纯逻辑，零 Three 依赖
  viewer/         # R3F 3D 渲染（只读预览可复用）
  mcp/            # MCP server + 存储 + 操作层（可无头 Node 跑）
  cli/            # 本地运行时安装/进程管理
```

**关键工程决策（sub-path exports）**：
```js
// 让 Node/MCP 侧只 import 数据层，不拖进 three/GPU
import { schema } from '@pascal-app/core/schema'
import { store } from '@pascal-app/core/store'
// 而非 import 整个 core（会拖进 three-mesh-bvh 等 GPU 依赖）
```

**数据模型**：扁平字典 `Record<id, Node>` + parentId/children 指针（非嵌套树）
```
Site → Building → Level → Wall → Item(门/窗)
                       ├─ Slab → Ceiling → Item(灯)
                       ├─ Roof / Zone / Scan(3D) / Guide(2D)
```

**dirty 标记**（性能关键）：GuardedDirtySet 防不可消费标记卡死、undo 幻影清扫、动画禁每帧 markDirty。

---

## 三、映射到 sora 的 CAD/PCB 自动化

### 如果给 KiCad/PCB 做 MCP（借鉴 pascal 模式）

| pascal 语义工具 | KiCad 对应（建议）| 用途 |
|:---|:---|:---|
| create_room | create_component / place_component | AI 放置元件 |
| add_door / add_window | add_track / add_via / add_pad | AI 画走线/过孔/焊盘 |
| check_collisions | run_drc / check_clearance | AI 自查 DRC |
| measure | measure_track_width / get_pad_info | 尺寸/间距查询 |
| validate_scene | run_drc_full / check_netlist | 定案前校验 |
| undo / redo | undo / redo | 改坏回退 |
| export_glb | export_gerber / export_bom | 导出制造文件 |
| editorUrl 交接 | gerber 预览链接 / 3D 视图链接 | 交回人确认 |

### 关键原则（pascal 实证）
1. **语义优先**：AI 用 create_component/route_track 而非直接 patch 文件——免猜 KiCad 内部结构
2. **校验闭环**：每个 AI 动作后 DRC/规则检查——PCB 不能盲画
3. **人工交接点**：每阶段产出（原理图/布局/DRC 报告）给 sora 确认后再继续
4. **无头可跑**：Core/数据层与 GUI 分离——服务器上也能跑 AI 自动化
5. **undo 兜底**：AI 改坏可回退

### 与现有技能的关系
- **pcb-design-automation**（已有：KiCad pcbnew API 命令行全自动生成 PCB）——已符合「语义化+校验」雏形，可参考 pascal 补「人工交接点」和「undo 兜底」
- **implicit-cad**（已有：SDF 建模）——纯浏览器端，可直接借鉴 pascal 的「浏览器原生 + MCP」路线
- **jlc-mcp-easyeda-automation**（已有：嘉立创 EDA 桥接）——已走 MCP 路线，可对照 pascal 检查工具语义化程度

---

## 四、可落地动作（优先级）

1. **给现有 KiCad 自动化补「人工交接点」**：每阶段输出 3D 预览/Gerber 链接给 sora 确认（最易做，价值高）
2. **PCB MCP 工具语义化审查**：对照 pascal 31 工具，检查现有工具是否语义化（create/validate/export 闭环）
3. **headless Core 借鉴**：如做 PCB 服务器自动化，Core 与 GUI 分离（数据层零 GUI 依赖）
4. **undo/redo 兜底**：AI 自动化加回退能力（防改坏）

---

## 五、多源实证：kicad-mcp 生态（2026-09-08 千轮研究新增）

> 除了 pascal/editor，KiCad 领域已有成熟的 MCP server 实证——这是 sora 做 PCB MCP 的**直接参考**。

### 1. blwfish/kicad-mcp（17+ 工具，单元可测）
- 工具分 **domain routers**（schematic / pcb / audit / drc / autoroute / library / project / analyze / export / lcsc）+ **standalones**（build_pcb_from_schematic / panelize_pcb / estimate_board_size / suggest_placement / analyze_placement_telemetry）
- 用 FastMCP + KiCad bundled Python subprocess bridge（`run_pcbnew_script` 单点可 mock）→ **无 KiCad 也能单元测试**
- 推荐 Claude Opus + FreeRouter v2.2.4+（10-30× 快、确定性）
- 关键设计：**PCB 操作全走 subprocess bridge，schema 操作走 kicad-sch-api**——可测试性是核心

### 2. oaslananka/kicad-mcp-pro（377 工具目录 / 渐进披露）
- **渐进披露（progressive disclosure）**：默认 profile 只暴露 24 个只读审查工具，build/release/expert 分级解锁写操作
- 明确声明：**「engineering assistant, not automated sign-off authority」**——生成物必须合格人工审查后才能制造
- 附带完整 skill 集（kicad-design-review / pcb-design / drc-check / fabrication-output / schematic-review）
- capability-parity 矩阵公开 KiCad 程序化覆盖度（76.3%）

### 3. PCB Flow Autonomy Ladder（人工分级模型，最有价值）
- **「自主性受可逆性约束」**——能重放的分析全自动（T1），活的写操作要批准（T3），下板厂订单永不自动（T6）
- 12 阶段流程，每阶段 PASS/CONDITIONAL/FAIL 书面判定，FAIL 阻断下一阶段
- 机器强制 gate：ERC 0 错误 / DRC 0 错误 / DFM 通过 / 丝印 0 覆盖——**export 拒绝出文件直到 gate 通过 + 人工批准**

### PCB MCP 语义化设计原则（三源合流）
1. **语义工具为主，patch 兜底**（pascal）：create/validate/export 闭环
2. **可测试性内置**（kicad-mcp）：subprocess bridge 单点 mock，无 GUI 也能测
3. **渐进披露**（kicad-mcp-pro）：默认只读，写操作分级解锁
4. **人工 gate 分级**（PCB Flow）：T1 全自动 / T2 确认 / T3 批准 / T6 永不

### sora 落地路径（结合 KiCad 10 锁定）
```
当前：pcb_pipeline.py（SKiDL→Gerber 一条龙，已具备 T1 自动化）
升级方向：
  ① 加 T2 布局确认点（生成 SVG 预览 → sora 确认再布线）
  ② 加 T6 DRC 签字 gate（DRC 通过 + sora 确认才允许 export Gerber）
  ③ 可选：封装成 kicad-mcp 风格 MCP server（subprocess bridge + 渐进披露）
  ④ 参考 KiCad 10 无 kicad-cli api-server → IPC 需 GUI + api.enable_server=true（记忆事实）
```

---

## 六、文件索引
- 完整 pascal 报告：`~\pascalorg-editor-research.md`
- 5 项目综合：`knowledge/Research/黑盒热榜5项目实证研究-2026-09-08.md`
- PCB Flow Autonomy Ladder 原文：`https://github.com/NijoP/pcbflow/blob/main/docs/04_HUMAN_IN_THE_LOOP.md`
