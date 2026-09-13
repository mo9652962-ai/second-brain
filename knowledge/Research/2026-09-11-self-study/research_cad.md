---
title: "CAD智能制造自动化-千轮研究-2026-09"
type: note
domain: Research
status: active
tags: [knowledge/research, 千轮研究, cad, 智能制造]
date: 2026-09-12
---

# CAD/智能制造自动化 · 2026 千轮研究报告

> 调研时间：2026-09-12（UTC+8）｜方法：多轮 web_search + web_extract + 本机实测（FreeCAD 1.1.1 无头脚本验证）
> 目标读者：sora 的 CAD 路线（FreeCAD 自动化 + AI 工作台 + 2D工程图→3D打印→智能制造技能树），闲鱼 CAD 接单可行性
> 实证原则：关键结论附官方文档/GitHub/实测来源，不编造数据。

---

## 结论速览（TL;DR）

2026 年 CAD 自动化已进入"**B-Rep 优先 + AI 生成初稿 + 无头验证闭环**"阶段：
- **FreeCAD 1.1（2026-03-25 发布）** 内置 Assembly 工作台（Ondsel 求解器），TNP 已修，freecadcmd 无头 Part API 稳定可用（本机实测通过）；但 **Assembly 脚本化仍不成熟**（官方 issue #27914 未关闭，需 GUI 手工初始化）。
- **代码 CAD 仍是 AI 自动化最可靠通路**：OpenSCAD 生成可靠性 ≈0.4 错误/代（GrandpaCAD 23 模型实测），Build123d/CadQuery 的错误率是其 3-4 倍，但 B-Rep/STEP 能力更强；**双引擎策略**（build123d 出 STEP + OpenSCAD 兜底）是当前最优解。
- **线上 AI 建模二分**：B-Rep 生成（Zoo Design Studio 最工程化，Zookeeper 对话代理）vs 网格生成（Meshy 6 等，只适合外观件）；📌 面向制造必须走 B-Rep/STEP。
- **切片自动化已成熟**：OrcaSlicer CLI 支持完全无头切片（Printago 已跑 3.5 万+ 次），`slice_info.config` 可直接做成本核算。
- **ECAD-MCAD 共用基建明确**：KiCad STEP 导出（KiCad 10+ 官方库纯 STEP）+ KicadStepUp 双向同步 + jlc-mcp 与 freecad-ai 同属 **MCP + Python/uv 无 Docker 模式**，完美贴合本机（无虚拟化）环境。

---

## 1. FreeCAD 自动化现状 2026

### 1.1 版本与内置能力（实证基线）

| 项 | 值 | 来源 |
|---|---|---|
| 最新稳定版 | 1.1.0（2026-03-25 发布）；1.1.1 patch 本机安装 | github.com/FreeCAD/FreeCAD/releases/tag/1.1.0 |
| 本机实测 | FreeCAD 1.1.1 Revision 20260414，OCC 7.8.1，Python 3.11.14 | freecadcmd --version |
| 1.1 里程碑 | TNP 修复（1.0 起）、内置 **Assembly 工作台**（Ondsel 求解器）、Create Simulation 动画、Insert New Part、BOM、Exploded View、全新 CAM 工具库系统、FEM 改进 | github.com/FreeCAD/FreeCAD-documentation wiki/Release_notes_1.1.md |
| 1.2 进行中（milestone 1.2） | Assembly 过约束报告（PR#24623）、关节 90° 旋转（PR#29717）、装配内编辑草图不崩溃（PR#29271）、仿真导出视频（PR#25307）、临时爆炸视图（PR#25456）、**TNP 改进进 Python API**（PR#24632，插件稳定性） | reqrefusion.github.io Release_notes_1.2 / blog.freecad.org 2026-01-28 WIP |

> 💡 1.1 的 Assembly 已可用但未"默认成熟"——官方开发者路线图（DevelopersHandbook/roadmap）仍将 Assembly 列为长期目标（数据格式、求解器、80% 用户需求集三件套）。

### 1.2 Python API / freecadcmd 无头（本机实测 ✅）

```
freecadcmd.exe script.py → Part.makeBox → doc.addObject("Part::Feature") → recompute → Shape.isValid()==True
                          → Part.export([shape], "*.step") + Mesh.tessellate(0.3).write("*.stl") 均成功
```
- **Part API 全链路无头可用**：基础体/挤出/布尔（fuse/cut/common）/tessellate/STEP+STL 导出，全部 CLI 可跑、无 GUI 依赖。
- 实测陷阱确认：`App.Gui` 在 freecadcmd 中不存在（需判空）；内联 `-c` 命令崩溃（skill 已记录）；脚本路径必须用 Windows 格式 `C:\...`。
- OCC 7.8.1 的 B-Rep 精度与 2026 商业内核（Parasolid 同期版本）差距在缩小，复杂曲面仍弱（NURBS 编辑靠 Surface 工作台）。

### 1.3 Assembly 工作台：GUI 已能用，脚本化是短板 ⚠️

- **现状**：内置工作台 + Ondsel 求解器，支持固定/旋转/滑动等关节、Simulation 动画、BOM、爆炸视图、ASMT 调试导出。
- **官方未解决的脚本化问题**（github.com/FreeCAD/FreeCAD/issues/27914，2026-02-27 开，至今 open）：
  - 用脚本从 FCStd 创建装配体"初始化不 100% 正确"，改 Assembly Placement 会引发奇怪行为；
  - Python 控制台不暴露关节最终化/旋转关节角度设置方式（旋转角度应是一等公民但缺失）。
- **社区绕行方案**（forum.freecad.org t=103531 / t=104928 / t=105451，作者 onekk）：
  - 需"人肉先初始化一次"（双击装配→双击关节→OK）脚本才能动；
  - 移动关节用 `joint.Offset2 = Placement(..., Rotation(angle,0,0))` + recompute 的 hack；
  - `recompute()` 对关节不可靠，常留 pending 状态；
  - 关节参考建议用 **LCS（局部坐标系）** 而非面/边，规避 TNP——这是目前最稳的脚本化方向。
- **建议**：装配体交付仍走 GUI + 现成脚本模板（onekk 的 assembly_move.py 可参考，codeberg.org/onekk/freecad-macro）；把"关节脚本化"标记为**等 1.2**，届时 PR 已合并过约束/角度偏移等能力。

### 1.4 AI 辅助建模：freecad-ai 工作台（已装 v0.21.2-alpha）

- 仓库实证：**ghbalf/freecad-ai，440★ / 70 fork，2026-02-20 创建，v0.15.0-alpha 发布于 2026-05-23**；本机为 v0.21.2-alpha（2026-08-15，Git b6c950f）。
- 能力（README 实证）：Plan/Act 双模式（Plan 默认=代码审查后执行）、50 个结构化 FreeCAD 工具、20 家 LLM 供应商（Moonshot/DeepSeek/Qwen 等 + Custom）、**MCP 服务器（mcp_server_entry.py / mcp_server_http.py）**、错误自纠正最多 3 次、视觉路由（非视觉模型走 llm-vision-mcp 降级）、8 个内置技能（enclosure/gear/fastener-hole/thread-insert/sketch-from-image/lattice 等，本机 ls 确认）、/optimize-skill 自优化、hooks、session 恢复。
- **明示风险（README 原话）**：Alpha software——LLM 生成的代码可能弄崩 FreeCAD，必须**频繁保存 + Plan 模式**。
- 配置坑（本机 skill 实测 2026-08-22）：
  1. **版本化目录**：FreeCAD 1.1+ 用户目录带版本号 `%APPDATA%\FreeCAD\v1-1\Mod\`（连字符 v1-1），不再是 `Mod\`；
  2. **param store 覆盖层**：只写 `FreeCADAI/config.json` 不够，首次加载会写入默认 anthropic 到 ParamGet("User parameter:BaseApp/Preferences/Mod/FreeCADAI")，必须双写：`SetInt("ProviderIndex",5)`（moonshot）+ SetString(Model/BaseUrl/ApiKey) + SetInt ModeIndex/MaxTokens + SetBool EnableTools；
  3. **首次加载迁移 rename**：freecad-ai 会把已存在的 config.json 目录改名 `FreeCADAI.pre-v0.13-snapshot`——先让 FreeCAD 跑一次建 marker，再写 config；freecadcmd 内联 -c 崩溃、MSYS 路径报 Unknown file，用 Windows 路径脚本文件。

### 1.5 FreeCAD 坑清单（2026 汇总）

1. Assembly 脚本初始化不完整 → 等 1.2 或 GUI 手初始化；2. 关节用 LCS 参考；3. freecadcmd 无 App.Gui；4. 版本化用户目录（v1-1）；5. freecad-ai param store 双写；6. 打印 emoji 进脚本在 gbk 控制台崩溃（用 ASCII）；7. AI 生成代码会崩 FreeCAD → Plan 模式 + 频繁保存 + 事务（undo）；8. 复杂布尔用 Part API 而非 build123d（OCCT 原生更稳）。

---

## 2. 其他 CAD 自动化 / AI 建模工具对比（带实证）

### 2.1 代码 CAD（CAD-as-Code）横评 —— AI 生成可靠性实测

GrandpaCAD（grandpacad.com，提示词→可打印模型的商业产品）用同一模型（gemini-3.5-flash）跑 23 模型评测套件：

| 引擎 | 内核/范式 | 代码错误/代 | 实证备注 |
|---|---|---|---|
| **OpenSCAD** | CGAL/声明式 CSG | **~0.4**（23 模型共 10 错） | 语言小、稳定；网格输出、无 STEP，$fa/$fs 控制精度 |
| **Build123d** | OCCT/B-Rep Python | **1.4-1.7**（40 错；给了自动生成 API 参考后 33 错） | API 面大，模型幻觉方法名；3-4 倍 OpenSCAD 修复循环 |
| **CadQuery** | OCCT/B-Rep Python | 高（早期一半场景败在导出） | 自带 3MF 导出丢颜色需自写；工作平面链式 API 易错 |

> **结论**：瓶颈不在内核，在**模型能写出什么**。OpenSCAD 当前 AI 最稳；Build123d/CadQuery 能力更强但需修复循环。两者都保留、按模型能力切换（GrandpaCAD 策略）。

- **Build123d**：~2,000★ 快速增长、535★ 单日峰值；context manager + Mode 显式布尔更 Pythonic；性能快于 CadQuery（100mm 方盒 0.8ms vs 1.2ms）；**pre-1.0 API 变动频繁需锁版本**；无内置 2D 工程图（可导 DXF）。
- **CadQuery**：~3,500★ 稳定；workplane 链式；STEP 导出稳。
- **生态**：`pzfreo/build123d-mcp`（MCP 服务器：逐步建模+测量+导出+PNG 预览，CADGenBench 分数 0.360→0.457、合法率提升）；`jdilla1277/agentcad`（79★，CadQuery/build123d 双运行时的 agent CAD CLI+MCP）；`cyberchitta/cad-khana`（12★，**诊断优先**：生成 diagnostics.json 报干涉/间隙/壁厚/悬垂，断言即构建失败，`khana draw` 出工程图 PNG 给多模态 agent 看——正好补 AI 建模"看不见"的反馈环）。60 Alternativies 全景图：cyberchitta.cc/articles/cad-llm-tools.html（2026-05）。
- **OpenSCAD 生成式落地**：**AdamCAD**（开源，YC W25）OpenSCAD 编译到 WebAssembly 纯浏览器跑，每个尺寸变 slider，确定性代码编辑即时迭代、零成本，BOSL/BOSL2/MCAD 库，OpenRouter 模型无关，导出 STL/OBJ/GLB/FBX/DXF——"AI TinkerCAD"。

### 2.2 生成式 B-Rep / Text-to-CAD（面向制造的正路）

- **Zoo Design Studio**（zoo.dev）：Text-to-CAD 输出 **KCL（KittyCAD 语言）→ B-Rep → STEP**，可编辑特征树+尺寸 slider；**Zookeeper 会话式代理**（2026-01）可对话迭代（"再加两个孔""壁厚改 3mm"）+ 质量属性计算（表面积/体积/质量/质心）；桌面 App 开源（MIT），云端几何引擎专有；免费档 40 credits/月 + Zookeeper 20 分钟/月；Pro $99/月；弱点：复杂装配体仍不行——当"初稿工具"。
- **Prompt2CAD / WebCAD / TextoCAD**：浏览器提示词→STEP/DXF，TextoCAD 有特征树+slider；Momaking 负责制造交接（报价）。
- **判据**（swiftwand litmus test）：*以后要不要改一个尺寸？→ 要就 B-Rep 起步；文件会不会交给别人？→ 要就 STEP*。B-Rep→网格是单向易转（切片器直接吃 STEP），网格→B-Rep 逆向工程基本不可行（三角形不携带设计意图）。

### 2.3 网格生成（只适合外观件）

Meshy 6（2026-01-18 GA，5k-100k 面，Remesh 一步重构拓扑+UV）、Tripo（~19.9$/月，秒级+绑定）、Rodin/Hyper3D（30$/月，高精度角色）、Sloyd（11$/月，参数化模板）——全部 STL/OBJ/GLB 类，**无 STEP、无尺寸意图**，打印功能件前必须重做或网格清理。

### 2.4 SolidWorks 2026 AI（商业标杆，仅供参考）

2026x FD03（2026-07-11 起 Beta）：**LEO/MARIE/AURA 虚拟伴侣**——自然语言直接生成 **VBA 宏**（"按公司标准导出交付物"等，生成后进编辑器审查）、生成装配体结构树、紧固件模式助手、图像→网格、STEP 加参数特征、装配说明书（带截图）；token 消耗计量。API 自动化仍是 VBA/.NET。可迁移经验：**"自然语言→生成宏→人工审查"** 正是 freecad-ai Plan 模式的同构。

### 2.5 AI 逆向工程（2D/扫描 → CAD）

- **Backflip AI copilot**（2026-08-05 上线）：3D 扫描/STL → 可编辑参数化 CAD（特征树），宣传"$1500/件→$10/件"，Fast/Thinking 双模式，擅长中复杂度 3 轴铣削件。
- **CADENA**（arXiv 2608.00799，开源）：**逐步** CAD 逆向（每步执行后与目标对比残差再决定下一步），CadQuery DSL + OCCT 执行，超 DeepCAD/Fusion360/MCB 基准；代码 github.com/zhemdi/cadena。
- **Detessellate**（FreeCAD 工作台，Addon Manager 可装，v1.1.0 2026-05-12）：网格/点云 → 参数化草图（CoplanarSketch/PointPlaneSketch/EdgeLoopToSketch/SketcherWireDoctor），免费替代商业 scan-to-CAD 的草图环节。
- 商业：ZEISS REVERSE ENGINEERING（点云→STEP/IGES，草图分区+约束自动优化）。

### 2.6 总对比表

| 工具 | 类型 | 输出 | AI 可编辑性 | 成本 | 实证 |
|---|---|---|---|---|---|
| FreeCAD 1.1 + freecadcmd | 开源 CAD+无头 API | STEP/STL/DXF | 脚本全参 | 免费 | 本机实测 ✅ |
| freecad-ai | AI 工作台 | FCStd→STEP | Plan/Act | API key | 440★ v0.21.2-alpha |
| OpenSCAD | 声明式代码 CAD | STL（无 STEP） | ★★★ AI 最稳 | 免费 | 0.4 错/代 |
| Build123d | Python B-Rep | STEP/STL/DXF | ★★ | 免费 | ~2k★，pre-1.0 |
| CadQuery | Python B-Rep | STEP/STL | ★★ | 免费 | ~3.5k★ |
| Zoo Design Studio | 云 Text-to-CAD | STEP (KCL) | ★★★ 会话式 | $0-99/月 | Zookeeper 代理 |
| AdamCAD | 浏览器 OpenSCAD | STL/DXF/OBJ | ★★★ slider | 免费开源 | YC W25 |
| Meshy/Tripo/Rodin | 网格生成 | STL/OBJ/GLB | ✗ 重生成 | $10-30/月 | 外观件专用 |
| SolidWorks 2026 | 商业 CAD+AI | 原生 | LEO 宏生成 | 订阅+token | FD03 Beta |

---

## 3. 2D 工程图 → 3D 模型 → 3D 打印：自动化工序优化

### 3.1 完整流水线（2026 最优实践）

```
输入                       自动化锚点                      交付
─────────────────────────────────────────────────────────────
DXF/DWG 图 ──▶ freecadcmd 脚本(读DXF→Sketcher/Part挤出)
图片/照片 ──▶ freecad-ai sketch-from-image 技能 / vision LLM
STL/扫描 ──▶ Detessellate(网格→草图) 或 CADENA(→CadQuery)   ──▶ STEP(B-Rep, 参数化)
AI 提示词 ──▶ Zoo Zookeeper / AdamCAD 初稿 → 人工定稿
                                     │
                                     ▼
                          FreeCAD 无头验证脚本(壁厚/悬垂/干涉断言)
                                     │
                                     ▼
                 OrcaSlicer CLI --slice → .gcode.3mf（Bambu 直接吃）
                                     │  slice_info.config：耗材mm/g、时间、层数
                                     ▼
                         打印机(API 推送) → 打印 → 实物验证 → 回填参数
```

### 3.2 切片自动化实证（成熟度最高的环节）

- **OrcaSlicer CLI**（官方文档缺失，Printago 实战 35,000+ 次无头切片整理出完整参考）：核心标志 `--slice 1`（0=全部底板）、`--load-settings "machine;process"`（顺序敏感）、`--load-assemble-list`（多物体排板无需项目文件）、`--export-3mf`、`--pipe`（JSON 进度到命名管道）、`--min-save`；**输出是 `.gcode.3mf`（ZIP 内含 G-code 于 Metadata/plate_1.gcode）而非裸 .gcode**——Bambu 打印机原生接受；**`slice_info.config` 含每槽耗材 mm/g、预估时长、层数**，直接喂成本核算。
- **坑**：`printer_model` 必须与机器设置 JSON 匹配否则切片失败/错误（换机型要补 3MF 元数据）；CLI 各版本间悄悄变，上线前锁版本并 `--help` 检查。
- **服务化三选一**：① 原生 CLI（本机首选，无 Docker）；② OrcaSlicer 官方 PR #14161：SliceCore 库 + `orca-server` REST（POST /v1/jobs、PNG 预览、逐物体摆放、结构化指标）；③ escalopa/orcaslicer-api（FastAPI 封装，自动解析时长/耗材/层数元数据）——⚠️ Docker-first，本机无虚拟化请绕开，用原生 CLI。
- **PrusaSlicer CLI** 同样支持 `--export-gcode`（成熟），但**读不了 OrcaSlicer 配置**，两者不要混用。
- 3MF > STL 已是行业方向（颜色/材质/元数据/多物体原生）。

### 3.3 DFAM 自动校验清单（建模脚本内置断言）

壁厚=喷嘴整数倍（0.4mm→1.2/1.6mm）；悬垂 ≤45°；桥接 ≤10mm；最小孔 ≥2mm（水平孔泪滴形）；配合间隙 0.2-0.3mm 单侧；受力方向避 Z 轴（层间强度仅 XY 的 50-70%）；文字 ≥4mm 字体、0.5mm 深。**cad-khana 的 diagnostics.json 断言机制就是为此设计**——把上述规则写成断言 = 打印失败在建模期前拦截。

---

## 4. 与 PCB 流水线共用的自动化基建

### 4.1 现状与组件

- **KiCad 10+ 官方 3D 库纯 STEP**（File→Export→STEP 导出实心几何；注意 STEP **不含**铜皮/丝印/阻焊，那是 2D 图形层——机械装配够用，渲染走 VRML/pcb2blender）。
- **KicadStepUp**（easyw/kicadStepUpMod，FreeCAD 工作台）：双向 ECAD-MCAD——载入 .kicad_pcb 全板+元件→FreeCAD、导出 STEP/IGES 给机械、**PCB 边框 PUSH/PULL**（FreeCAD Sketcher ↔ KiCad Edge.Cuts 双向同步）、STEP→VRML 供 KiCad、**干涉/碰撞检查**（外壳 vs 板子）；支持 KiCad 5.1-9.x / FreeCAD 0.19-1.0+。注意：约束/构造几何在 KiCad 往返中会丢——板框以 FreeCAD 侧为准单向同步是更稳的工作流。
- **jlc-mcp（jlcmcp）**：EasyEDA Pro 的 MCP 桥——pcb_get_state/pcb_route_track/pcb_run_drc/pcb_screenshot 等 38 个工具，走 bridge→MCP 模式。与 freecad-ai 的 MCP server、build123d-mcp 属**同一套基建范式**。

### 4.2 可复用的共用基建（重点）

| 基建 | CAD 侧用途 | PCB 侧用途 |
|---|---|---|
| **Python 3.11/3.12 + uv**（无 Docker） | build123d/cad-khana/FreeCAD 脚本 | kicad-cli、EasyEDA bridge、jlc-mcp |
| **MCP 服务器模式** | freecad-ai MCP、build123d-mcp、agentcad | jlc-mcp |
| **无头 CLI 验证闭环** | freecadcmd（建模）、khana diagnostics（几何断言） | kicad-cli `pcb render`/D 导出、jlc DRC |
| **STEP 中性交换** | 外壳/结构件 | 板级 STEP → 干涉检查 |
| **参数化外壳生成** | build123d/FreeCAD 从 Edge.Cuts 生成外壳 | KiCad 板框 → 外壳布尔 |

> 💡 串联想象：KiCad 导出 Edge.Cuts → FreeCAD/KicadStepUp PULL → build123d 参数化生成外壳（插槽/柱位/开口按元件高度表）→ 无头 STEP → OrcaSlicer CLI → 打印验证 → **同一个 uv 虚拟环境 + MCP 客户端管 PCB 和外壳两条流水线**。本机无 Docker 不是障碍——全部组件原生 Windows 可跑（freecadcmd、kicad-cli、orca-slicer CLI、uv tool 安装的 MCP 服务器）。

---

## 5. 立即行动建议（5 条）

1. **固化 FreeCAD 无头建模流水线**：以本机已验证的 freecadcmd + Part API 模板（建体→布尔→STEP/STL 导出→isValid 断言）为底座写 `cad_pipeline.py` 脚本库；确认 freecad-ai 双写配置（config.json + param store ProviderIndex=5 moonshot）后保持 Plan 模式默认，所有 AI 生成代码走"生成→freecadcmd 无头试跑→人工审查"。
2. **部署 CAD-as-Code 双引擎**：`uv tool install cybergit cad-khana` 跑通 `khana build/check/diff` 诊断闭环，主引擎 build123d（锁版本，pre-1.0 API 会变），复杂布尔回退 FreeCAD Part API；OpenSCAD 作为纯 CSG/快速初稿备胎。所有脚本内置 DFAM 断言（壁厚/悬垂/间隙）。
3. **打通 2D→3D→打印全自动链**：DXF→freecadcmd 挤出→STEP→OrcaSlicer CLI `--slice --export-3mf`→`.gcode.3mf` 直推 Bambu；用 `slice_info.config` 自动生成成本报价（材料 g × 单价 + 时长 × 电费 + 后处理）；锁 OrcaSlicer 版本并记录 `--help` 差异。
4. **ECAD-MCAD 共用基建落地**：本机装 KicadStepUp + 配置 jlc-mcp；首个联调项目 = 现有 PCB 板框 → 参数化外壳（含柱位/开口）→ 干涉检查 → 3D 打印外壳，跑通"PCB 与外壳同一条 MCP+uv 流水线"样板。
5. **闲鱼接单 SOP 化**（结合 1-4）：建参数化模板库（外壳/法兰/支架/齿轮，AI 初稿+人工定稿）；交付物固定 STEP+STL 双格式；装配类订单明确告知 GUI 环节（Assembly 脚本化未熟，报价含人工装配时间）；打印件带 slice_info 成本表报价，用"设计+打印+验证"闭环升级客单价。

---

## 参考来源（关键实证链接）

- FreeCAD 1.1 发布：github.com/FreeCAD/FreeCAD/releases/tag/1.1.0；Release notes 1.1/1.2（wiki.freecad.org，Anubis 反爬；镜像 reqrefusion.github.io）
- Assembly 脚本化 issue #27914；论坛 t=103531/104928/105451（onekk 脚本化关节：Offset2 hack、LCS 参考）
- freecad-ai：github.com/ghbalf/freecad-ai（440★，v0.15.0-alpha 2026-05-23，README 功能清单与 Alpha 警告）；本机 v0.21.2-alpha + docs/specs
- GrandpaCAD 引擎评测：grandpacad.com/en/blog/openscad-vs-cadquery-vs-build123d（0.4 vs 1.4-1.7 vs 高）
- build123d：ainews.cool 分析（2k★ 535★/日、性能表）；thepixelspulse.com（Fluent API 陷阱）；build123d-mcp（CADGenBench 0.360→0.457）；agentcad 79★；cad-khana 12★
- Zoo/Zookeeper：swiftwand.com/text-to-cad-guide-2026；dupple.com（定价与档位）；AdamCAD（开源 OpenSCAD→WASM）
- SolidWorks 2026x FD03：blogs.solidworks.com；3dswym wiki（2026-07-11 Beta、宏生成）
- 逆向：Backflip AI（automationmag 2026-08-05）；CADENA arXiv:2608.00799；Detessellate v1.1.0；ZEISS
- 切片：printago.io/orca-slicer-cli-reference（35k+ 次实战）；OrcaSlicer PR #14161（SliceCore/orca-server）；escalopa/orcaslicer-api；PrusaSlicer DeepWiki CLI
- ECAD-MCAD：easyw/kicadStepUpMod；pcbsync.com/kicad-3d-integration；luisllamas.es（KiCad 10 STEP 库）
- 本机实测：FreeCAD 1.1.1 freecadcmd 建体+STEP/STL 导出+Assembly 模块导入 ✅（2026-09-12）

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
