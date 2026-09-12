# 『PCB 自动化深化』千轮研究报告（2026-09）

> 研究范围：2026 年 AI 辅助 PCB 设计 / 自动布线 / DRC 自动化的最新工艺与工具（AI 布局布线、KiCad 自动化脚本、DeepPCB/Quilter 类云端引擎、免费/开源方案）。
> 研究方法：多轮 web_search + web_extract 交叉验证，优先一手来源（厂商官网 / GitHub / arXiv / PyPI）。所有关键结论附实证与来源链接，不编造。
> 服务对象：sora 闲鱼 PCB 接单线（单价 50-800 元）。现状流水线：**ProtoFlow（原理图 AI）→ KiCad 10.0.5 pcbnew/kipy 脚本（放置）→ KiCadRoutingTools（布线）→ kicad-cli DRC → JLCPCB（网页下单）**；EasyEDA/jlc-mcp 双轨备用。本机 KiCad 10.0.5 锁定不升 11；pip kicad-python 导入名 kipy（GUI IPC 模式）；FreeCAD AI 已装；Quilter 实测前提为 DRC 0 违规 + 走线清空。

---

## 0. 结论置顶（TL;DR）

1. **2026 年 AI PCB 布局布线已跨过"能跑"门槛、进入"可交付"阶段**：云端 DeepPCB（RL 引擎，公开三方对比完成率 97.3%、过孔 −44%、首结果 1-2 分钟，$0.5/分钟按量付费，有 REST API + MCP）与 Quilter（物理驱动、多候选+物理评分卡、843 元件/8 层投产实证、免费层）是两强；开源侧 Freerouting 2.2.3（1.7k star，新增 REST API/MCP/CLI/多线程调度）与 KiCadRoutingTools v0.21.2（KiCad 9/10 官方路线，sora 已实战 100% 完成率）直接补位本地流水线。
2. **sora 现有流水线已属"开源阵营第一梯队"，最大差距不在布线，而在三个环节**：① DRC/DFM **交付门禁未固化**（还在手动跑命令+人眼扫报告）；② **JLCPCB 下单/报价全手动**（网页操作，无法规模化）；③ **缺"复杂板/赶工期"的云端 AI 通道**（DeepPCB/Quilter 免费层与 API 现成，未纳入流程）。原理图 AI 环节（ProtoFlow）不落后——2026 年最火的新玩家 pcbGPT（arXiv 2606.01188）也是同一赛道，证实该环节已成熟。
3. **5 条升级按性价比排序**（详见第四章）：零成本 DRC/DFM 门禁固化+AI 直驱（MCP）＞ Freerouting 第二布线路对比取优 ＞ 云端双雄免费层实测 SOP ＞ DeepPCB API 加急通道（约 $1-5/板）＞ JLCPCB OpenAPI 全自动下单（前置审批 2-4 周）。
4. **版本判断：锁 10.0.5 是正确决策**。KiCad 11 的 headless `kicad-cli api-server` + IPC 导出预计 2027-02 才发布；`kicad-python` 稳定版 0.7.1 目前仍须连 GUI。当前正确姿势 = kipy（GUI IPC，已配好）+ kicad-cli（headless DRC/导出）双通道，未来可平滑迁 11。

---

## 1. 2026 工具地图（工具 / 能力 / 实证证据 / 定价或开源）

### A. 云端 AI 布局布线（RL / 物理驱动）

#### 1.1 DeepPCB（deeppcb.ai，InstaDeep 出品，2023 年被 BioNTech 收购）
- **能力**：强化学习 placement + routing（7 年 RL 研发，NeurIPS/ICML 论文背书）；**自动从文件提取约束**（叠层/网络类/差分对/间距），无需手动录入；KiCad/Zuken 原生导入，Altium/EAGLE/EasyEDA/Proteus 可导入；输出 6 种格式；2026-07 上线 **Cooper AI 审图助手**（读板并报告理解结果，可用自然语言调整约束："保护电源区、标记差分对"）。
- **实证**：DeepPCB 官方 2026 年 3 月公开对比（3 块开源板：STRF 98 airwires / PocketBeagle 290 / BeagleConnect Freedom 414，条件一致、零人工干预）：平均完成率 **97.3% vs Quilter 87.7%**，过孔 **−44%**（29/135/191 vs 58/163/235），**首结果 1-2 分钟 vs 15-20 分钟**；414 airwire 板手工补线只留 12 条（Quilter 54 条）。独立工程师复测文章（anypcba.hashnode.dev，2026）给出相同数据。注意：此为 DeepPCB 自测（方法已公开、可复现），Quilter 官方另有内部 benchmark（未公开方法），双方各执一词——**自己板上跑一遍才是标准答案**。
- **定价**：免费试用 30 分钟（限 ≤150 airwires / 4 层 / 100 元件 / 1 块板）；正式 **$0.5 AI Credit/分钟（30 credits/小时）**，按用量付费；上限 1,000 元件 / 2,200 引脚 / 1,200 airwires / 8 层；Placement 另送 2 小时免费（≤100 元件）；**API 与网页同价**（placement 与 routing 均 0.5 credit/min）。开源：否。API 文档：api.deeppcb.ai/v1/scalar/deeppcb，Key 在 app.deeppcb.ai/api-key。

#### 1.2 Quilter（quilter.ai）
- **能力**：**物理驱动 RL**（对物理定律训练，非几何拼接）；**读原理图**理解电路关系（去耦电容验证、开关电源布局、差分对完整性+GND 连续性、IPC 载流、Simbeor 场求解阻抗、物理评分卡）；**并行多候选**布局供对比；混合流程（关键 20% 预布，其余交 AI）；KiCad/Altium/Cadence/Siemens 原生格式往返；企业侧私有部署/自托管（SOC 2 Type II，ITAR 场景）。
- **实证**：**Project Speedrun：843 元件 / 5,141 引脚 / 8 层，已投产并全验证**（官方）；免费层与付费同引擎。
- **定价**：**免费层**（个人/学术/<10 人且营收 <$50K 的创业团队；文件用于模型训练——涉密板勿用）；商业 **按未布引脚数计价、按下载付费**（预布部分不计费、迭代免费）；私有云/自托管更高价。
- **前提（sora 实测备注）**：需完整原理图 + 板框；板框内元件视为 locked；**要求提交板 DRC 0 违规 + 走线清空**（Quilter 自己做放置+布线，残留走线/违规会冲突）。适用带：100-1,000 元件、2,000-5,000 引脚、引脚密度 <20%；盲埋孔开发中、BGA fanout beta。开源：否。

#### 1.3 Flux.ai（flux.ai/pricing）
- **能力**：浏览器全链 ECAD（原理图/选型/布局/仿真）+ AI copilot + **Auto-Layout 一键布线**。
- **实证/局限**：官方明示适合 **40-100 元件、2-4 层中低复杂度**，关键信号（差分对/阻抗/高速）须手动；收敛耗时 10-24 小时。
- **定价**：Explore $20/月（含约 10 ACU）、Build $60、Pro $200（年付 $16/$48/$142）；Teams $158/editor/月（100 ACU pooled，增量 $2/ACU）；Auto-Layout 按复杂度烧 ACU（官方参考：简单 4 层 40 元件 ≈375 credits，2 层 100 元件 ≈1,250 credits）；免费=仅公共项目。开源：否。**结论：对 sora 无性价比，仅作竞品参照。**

#### 1.4 商业 EDA 巨头的 AI（参照项，非落地项）
- **Cadence AuraStack AI Super Agent**（2026-07-15 发布，Allegro AI Studio 上运行，NVIDIA Blackwell 加速）：官方宣称 2X 上市时间、15X 生产力；Allegro X AI 为 MDP 反馈优化，云上搜索数千设计变体（白皮书披露架构）；2026 年内面世，企业授权。
- **Siemens Xpedition**：AI copilot（命令预测/草图布线/智能 datasheet）+ Valor NPI 云 DFM（标准版含 12 次免费/年）+ 按 token 购买 SI/PI。
- **Altium Designer**：AI 辅助路由/器件创建（有限），已停售永久授权。→ 均为数千美元/年级，对本业务线只做技术对标。

### B. 开源 / 本地布线工具（可直接进流水线）

#### 1.5 Freerouting 2.2.3（github.com/freerouting/freerouting）
- **状态**：**1,740 star / 277 fork / GPLv3**；单维护者 Andras Fuchs；v2.2.3（2026-05-08）。
- **能力**：Specctra DSN/SES 标准接口，兼容 KiCad/EAGLE/EasyEDA/tscircuit/pcb-rnd；KiCad 插件双模式（**DSN 默认全版本稳定 + JSON/API 实验模式**，2026-06-08 合并 KiCad IPC API alpha，PR #705，+9.7k 行）；**REST API（Beta）+ MCP Server（Cursor/Cline/Claude 可驱动）+ 全功能 CLI + Docker（x64/ARM64）+ 多线程任务调度**；v2.2.3 修复了 >2 层板崩溃 bug（此前硬编码 2 层参数）。
- **坑**：JSON/API 模式尚未导入全部设计规则（铜到板边间距，issue #558）；IPC/JSON 是 KiCad 9+ 实验特性，DSN 为推荐路径。
- **定价**：免费开源。**↑ 2026 年新增 CLI/API/MCP 使其第一次真正可脚本化进流水线。**

#### 1.6 KiCadRoutingTools（github.com/drandyhaas/KiCadRoutingTools）——sora 已实战
- **状态**：**223 star / MIT / KiCad 9&10 官方兼容**；v0.21.2（2026-08-19，17 个 release，活跃）；Rust 加速 A* router + CLI + GUI 插件；支持差分对路由、"10x faster"宣称。
- **sora 实证**：空调板 26 元件：92.8%（v1 密集）→ **100% 完成 / 短路 0 / 未连接 0**（v2 拉大间距+去手动走线，布局优化闭环方法论固化在 pcb-automation 技能）。

#### 1.7 tscircuit（github.com/tscircuit/tscircuit + tscircuit-autorouter）
- **状态**：MIT；TypeScript/React 写电路 → Circuit JSON → Gerber/BOM/PnP；**@tscircuit/capacity-autorouter**（65 star，full-pipeline，SimpleRouteJson 入出）；官方声称 4 层板**亚秒级**布线、LLM 兼容调参、AI 文本生成 footprint；KiCad 双向转换（kicad-mod-converter）开发中。
- **定位**：前端/TypeScript 生态的代码化 EDA，对 sora（KiCad 脚本栈）仅是方法论参照（SimpleRouteJson 可作路由器接口层的灵感），不必引入。

#### 1.8 kicad-tools（github.com/rjwalters/kicad-tools，pip install kicad-tools[mcp]）★ 重点推荐
- **能力（CLI `kct`）**：
  - `kct route --complete`（v0.19.0+）：**只补未连通网络，其余铜皮当固定障碍，绝不删已有布线**（二遍精修利器，完美契合"KiCadRoutingTools 首遍 + 补漏"）；
  - `kct route-auto`：多策略编排路由；`kct optimize-placement`：CMA-ES/贝叶斯全局布局优化；`kct reason`：LLM 驱动布局推理（链式思考）；
  - `kct check`：**纯 Python DRC（免 kicad-cli）**；`kct drc` 解析 kicad-cli JSON；
  - 厂商制造档（**JLCPCB**/OSHPark/PCBWay/Seeed）内置；A* 路由器、trace 优化；
  - **内置 MCP Server**（`kct mcp serve`）：analyze_board / get_drc_violations / route_net / placement_suggestions / export_gerbers / start_session-commit-rollback 等 20+ 工具 → **可直接挂进 Hermes 让 AI 直驱 KiCad 板文件**。
- **状态**：PyPI 0.10→0.11 连续发布，活跃；需 KiCad 9+（kicad-cli 路径自动探测，支持 Windows）；C++ 路由器后端（build-native）声称 10-100x 提速。

#### 1.9 kicad-mcp 系（AI 代理控制 KiCad 的控制层）
- **AbdulAzeez0001/kicad-mcp**：kicad-cli headless DRC/ERC/Gerber/STEP/BOM/PDF 导出 + **kipy 实时控制**（读取/移动封装、存板）+ **kicad_preflight 认证门禁**（ERC+DRC+完整布线+板框 = 硬门，全过才生成 fab 压缩包）；自带 s-expression 解析器（无 KiCad 也能离线检查）；Python 3.10+，支持 Windows（KICAD_CLI 环境变量）。★ 与 sora 的 kipy + kicad-cli 双通道架构完全同构，`kicad_preflight` 直接可抄。
- **Gato513/kicad-mcp**：32 工具（放置/布线/DRC/导出），63 元件 E2E 验证，但 Linux 专用（Windows 未验证）。
- **oaslananka/kicad-mcp-pro**：KiCad 10.0.x 为主支持线 + KiCad 11 preview lane（headless IPC 就绪检测）；生产代码禁 SWIG；能力协商 + fail-closed（值得抄其"版本能力矩阵"思路）。
- **TensorFleet/kicad-automation**：fail-closed 命令桥 + **Codex skill**：`doctor`（环境自检）/ `inspect`（JSON 只读）/ `gate`（**DRC 任何违规即失败**+ERC+开焊盘）/ `render` / `release`（显式声明命令才放行）/ `telemetry`；原则：**验证不信任改文件的同一进程**（KiCad 10 上 pcbnew 只读）。

#### 1.10 pcbGPT（arXiv 2606.01188，2026-05-31，KIT）——自然语言 → KiCad 原理图
- **能力**：Python DSL 描述电路 + 本地 KiCad 元件库检索 + datasheet 接地知识 + 执行/结构/语义三重校验 + Web 交互迭代 + KiCad 项目同步。
- **实证**：20 个嵌入式/IoT/可穿戴设计任务基准：最佳模型 **gpt-5.3-codex 总体 pass@1=0.90、pass@5=1.00**（basic/easy 1.00、medium 0.91、hard 0.72）；qwen3.5-397b 总体 0.72。结论原文："已能生成有用、可审阅的初稿，但不足以替代专家审查"；**多轮采样（pass@5）显著优于单发**——即"候选生成器 + 人工 rerank"模式。
- **与 sora 关系**：与 ProtoFlow 同赛道（原理图阶段 AI），sora 已用 ProtoFlow；借鉴其**方法论**（DSL 表达、多采样 rerank、校验闭环）即可，无需换工具。

### C. DRC / DFM / 制造自动化

#### 1.11 KiCad 10 CLI DRC（headless 门禁标准做法）
- `kicad-cli pcb drc --output out.json --format json --exit-code-violations --refill-zones [--schematic-parity] board.kicad_pcb`：**exit code 0=干净，5=有违规**，可直接做 CI 门禁；`--refill-zones` 先重新铺铜再查（规避"未铺铜误报 unconnected"，正是 sora 踩过的坑）；salitronic/eda-agent 等新项目均采纳此模式（JSON 解析 + 违规结构化返回）。

#### 1.12 KiCad 11 前瞻（版本决策依据）
- KiCad 11 预计 **2027-02** 发布（官方论坛开发公告）；**headless `kicad-cli api-server`、IPC 输出/导出、输出 jobs 是 11 专有**；SWIG pcbnew **11 移除**；`kicad-python` 稳定版 0.7.1（2026-07）仍只支持连运行中的 GUI 会话。
- **结论**：锁 10.0.5 正确；新代码统一走 **kipy（GUI IPC）+ kicad-cli（headless）双通道**（sora 已在践行），11 发布后按"能力矩阵 + canary 测试"平滑迁移（参照 kicad-mcp-pro 的 compatibility.yaml 思路）。

#### 1.13 JLCPCB 制造侧自动化
- **JLCDFM（jlcdfm.com）**：免费在线 DFM/DFA，5 模块 30+ 检查项（走线/阻焊/钻孔/丝印/装配），可视化定位 + 一键 PDF 报告；无公开 API（网页上传）。
- **JLCPCB OpenAPI（api.jlcpcb.com）**：官方 API 平台——**PCB API**（Gerber 上传、自动报价、创建订单、实时生产跟踪）+ Stencil API + 3D 打印 API + **Parts API**（元件库检索/库存/价格，服务 BOM 匹配）；**需申请审批**（评估历史订单/公司情况，非所有申请通过）。社区 Python 客户端 i2cjak/jlcpcb_api（OpenAPI app_id/access_key/secret_key + RSA 签名，code=200 为成功、403=权限不足）。
- **嘉立创 EDA 自动化（sora 已有）**：jlc-mcp/eext-run-api-gateway（49620 端口，official easyeda-api-skill），EasyEDA 轨精修+下单，与本报告互补。

---

## 2. 与 sora 现有流水线的差距分析

**现状全链路**：
```
ProtoFlow(原理图AI) → pcb_pipeline.py[SKiDL→pcbnew放置] → KiCadRoutingTools(布线)
→ kicad-cli DRC(手动跑) → JLCDFM(网页人工上传) → JLCPCB(网页手动下单)
```

**差距矩阵**（环节 / 缺口 / 影响 / 2026 候选工具）：

| # | 环节 | 差距 | 影响（接单视角） | 候选工具 |
|---|------|------|------------------|----------|
| G1 | **DRC 门禁** | kicad-cli DRC 未固化为"自动 fail-fast + 分类报告"；铺铜/丝印假违规与真违规混在一起靠人眼挑 | 每单多花 30-60 分钟人工审 DRC；夜间无人值守出活难 | `kct check/drc`、AbdulAzeez0001 `kicad_preflight`、TensorFleet `gate`（全可抄） |
| G2 | **AI 直驱层** | AI 会话里改板/验板靠"生成脚本再跑"，无 MCP 实时通道 | 迭代慢；复杂改动要重写脚本 | `kicad-tools[mcp]`、AbdulAzeez0001/kicad-mcp（Windows 可用）、Gato513（仅 Linux） |
| G3 | **布线质量/复杂度上限** | KiCadRoutingTools 空凋板 100%，但规模化后复杂板（>4 层/高密度/电源回路）质量与完成率存疑；单路由器无对照 | 复杂订单不敢接或不自信 | Freerouting 2.2.3（第二路由器对比）、DeepPCB/Quilter（云端通道） |
| G4 | **云端 AI 通道缺失** | DeepPCB（API/MCP 现成、$0.5/min）与 Quilter 免费层均未纳入流程 | 复杂板/赶工期只能手动硬扛 | DeepPCB API + Quilter 免费层 SOP |
| G5 | **DFM 环节手动** | JLCDFM 网页逐单上传；无法与 DRC 门禁联动 | 漏检 DFM 问题=打样返工成本 | JLCPCB OpenAPI（报价前校验）；JLCDFM 无 API，用 DRC 规则前置覆盖 |
| G6 | **下单全手动** | 报价/下单/跟踪逐单网页操作 | **规模化接单瓶颈**（每天 5+ 单时不可持续） | JLCPCB OpenAPI（需审批，2-4 周前置） |
| G7 | **原理图 AI** | ProtoFlow 免费够用；未利用"多采样+rerank"方法论 | 中等 | pcbGPT 方法论（DSL+采样），非必需 |
| G8 | **版本** | KiCad 锁 10.0.5 | 无（正确决策）；11 的 headless IPC 是 2027 红利 | 现架构（kipy+cli）可平滑迁 11 |
| G9 | **布局"AI 决策"** | 放置分区靠人工制定规则脚本；无自动化布局优化闭环 | 高密度板首版布局差→布线返工 | `kct optimize-placement`（CMA-ES/贝叶斯）、DeepPCB Placement |

**一句话差距结论**：布线工具不缺（本地 100% 已达成、云端两强现成）；真正拖后腿的是**交付链路两端**——前端 DRC/DFM 门禁未固化（质量与人天），后端 JLCPCB 下单未自动化（规模化），中间再补一条云端复杂板通道（接单上限）。

---

## 3. 可立即落地的自动化升级建议（按性价比排序）

### 建议 1【零成本，约半天】DRC/DFM 门禁固化 + MCP 化，让 AI 直驱板文件
把"kicad-cli DRC json 解析→按 JLCPCB 规则（线宽/间距 ≥0.15mm（3.5mil）、孔 ≥0.15mm、丝印字高 ≥1.0mm、宽高比 1:6）分类违规→统计短路/未连接/丝印→输出 pass/fail JSON"写成 `gate.py`（fail-closed：**任何 error 级违规即 fail**，参考 TensorFleet/AbdulAzeez 模式），接入 pcb_pipeline 尾部；再 `pip install kicad-tools[mcp]` 把 `kct mcp serve` 挂进 Hermes，AI 可直接跑 DRC/导出/审板/布局建议，不再"写脚本→跑→看输出"。
- 性价比：∞（零成本）；每单省 30-60 分钟人工审 DRC，且为后续 4/5 条的地基。

### 建议 2【零成本，约 1 天】Freerouting 2.2.3 作第二布线路，与 KiCadRoutingTools 对比取优
Freerouting 2026 年新增 CLI/API/MCP + 修复多板层 bug 后已真正脚本化。在 pipeline 尾部加 DSN 导出→Freerouting CLI 布线→SES 回导→DRC 对比脚本 `compare_router.py`，拿 2 块已交付订单板各跑两路由器，以**完成率 / 过孔数 / DRC error 数 / 耗时** 四指标建档，胜者入主流程（或双通道：KiCadRoutingTools 首遍 + `kct route --complete`/Freerouting 补漏）。
- 性价比：零成本、纯本地、数据说话；彻底消除"单路由器质量焦虑"。

### 建议 3【免费层，约 2 小时】云端双雄免费度实测，建立"云端 vs 本地"决策表
用 DeepPCB 30 分钟免费额度（≤150 airwires/4 层）与 Quilter 免费层（个人/学术/开源板；不上传涉客户 IP 的板）各跑 1 块近期真实**开源/自研**订单板：记录完成率/过孔/首结果时间/导出格式/回导 KiCad 兼容性，与本地路由对比，形成决策表——"什么复杂度交给云端（≤$5 内）、什么本地跑"。这一步为建议 4 的付费决策提供实测依据。
- 性价比：免费；2 小时换来可复用的接单 SOP。

### 建议 4【约 $1-5/板，当天可启用】DeepPCB API 接入为"复杂板/赶工期"付费通道
注册 app.deeppcb.ai → 拿 API key（api.deeppcb.ai/v1/scalar/deeppcb）→ 写 `route_via_deeppcb.py`：KiCad 导出→上传→按 $0.5/min 轮询 job→下载 6 格式结果（含 KiCad 回导）→本地 gate.py 复核。单块 50-150 airwire 板预计 1-2 分钟出首结果、成本 $1-2。货源侧可推出"AI 加急布线"服务项，覆盖成本还有盈余。
- 性价比：极低单次成本（远低于手工布线人天）；直接抬高接单复杂度上限。

### 建议 5【前置审批 2-4 周】JLCPCB OpenAPI 打通"报价→下单→跟踪"全自动
在 api.jlcpcb.com 提交 OpenAPI 申请（附闲鱼接单量/历史订单证明）；获批后按 i2cjak/jlcpcb_api 或官方 SDK 建 `quote_order.py`：与 gate.py 联动——DRC 0 违规 → 自动报价 → 客户确认 → 自动下单 → 实时跟踪回写。这是**规模化接单（日 5+ 单）不可回避的一步**。审批等待期先把报价函数 mock + 文档写好。
- 性价比：单次实施一次性投入，摊薄到每单后几乎免费；建议 1 的地基直接复用。

---

## 4. 每条建议的下一个具体行动

| 建议 | 下一个具体行动（本周内可执行的第一步） |
|------|-----------------------------------------|
| 1 | 写 `gate.py`（约 150 行）：调用本机 `kicad-cli pcb drc --format json --exit-code-violations --refill-zones`（以 `kicad-cli pcb drc --help` 实际参数为准）→ 解析 violations 按 error/warning 分类 → 输出 pass/fail JSON；接入 `D:\aircon-pcb-demo\pcb_pipeline.py` 尾部；随后 `pip install "kicad-tools[mcp]" && kct doctor` 验证 MCP 通道可用。 |
| 2 | 从 GitHub releases 下载 freerouting-2.2.3-windows-x64.msi（或 `java -jar freerouting-executable.jar`）；先跑通最小 headless 命令 `java -jar freerouting-executable.jar --gui.enabled=false --api_server.enabled=true --api_server.authentication.enabled=false`；用现有空调板导出 DSN 试布一次，再写 `compare_router.py` 收集四指标。 |
| 3 | 选 1 块 ≤150 airwires 的自研/开源板下载 DSN/板文件 → 分别上传 deeppcb.ai 与 quilter.ai 免费层 → 记录完成率/过孔/时延/导出格式 → 输出对比表存 Obsidian（决策表初稿）。 |
| 4 | 注册 app.deeppcb.ai → 在 /api-key 生成 key → 读 Scalar API 文档确认"上传→job 轮询→结果下载"三个端点 → 写 50 行 `route_via_deeppcb.py` → 用建议 3 的同一块板验证 KiCad 往返 + gate.py 复核。 |
| 5 | 在 api.jlcpcb.com 提交 OpenAPI 访问申请（附业务说明与历史订单）；等待期间搭好本地 `quote_order.py` 骨架（用 mock 报价函数）；获批后在 sandbox 验证一次真实"上传→报价→下单→跟踪"闭环。 |

---

## 5. 关键版本/时间线备忘

- **2026-09（现在）**：KiCad 10.0.x = 稳定主线；`kicad-python` 0.7.1 仅 GUI 会话；SWIG pcbnew 已弃用（9.0 起），11 移除。
- **~2027-02**：KiCad 11 发布：headless `kicad-cli api-server` + IPC 输出/导出 + 输出 jobs；届时 sora 迁 11 时只迁移控制层（kipy/cli 风格不变，pcbnew 脚本冻结不扩）。
- **2026 年内**：Cadence AuraStack AI Super Agent 发布（企业向，仅参考）；DeepPCB Cooper 审图已上线（2026-07）；Freerouting 2.2.x 是当前稳定分支（IPC/JSON alpha 在 2.3 路线图）。

---

## 6. 证据来源清单（一手优先）

- DeepPCB 官网/定价/API/对比：deeppcb.ai/pricing | deeppcb.ai/help | deeppcb.ai/deeppcb-api-your-pcb-design-ai-agent/ | deeppcb.ai/deeppcb-vs-quilter-open-source-routing-compared-2026/ | deeppcb.ai/benchmarks/ | deeppcb.ai/ai-pcb-design-review-cooper/
- Quilter 官网/产品/定价/Blog：quilter.ai | quilter.ai/product | quilter.ai/pricing | quilter.ai/free-ai-pcb-design | quilter.ai/blog/the-2026-guide-to-autonomous-pcb-design-quilter-vs-deeppcb-vs-flux-ai
- ProtoFlow 对比文（三工具定位/定价）：protoflow.ai/compare/ai-pcb-autorouter-comparison | protoflow.ai/compare/best-ai-pcb-design-software-2026
- Flux：flux.ai/p/pricing | docs.flux.ai/tutorials/auto-layout
- Freerouting：github.com/freerouting/freerouting（1,740 star）| freerouting.app | releases v2.2.3 | PR #705（IPC alpha）
- KiCadRoutingTools：github.com/drandyhaas/KiCadRoutingTools（223 star，v0.21.2）
- kicad-tools：github.com/rjwalters/kicad-tools | PyPI kicad-tools 0.10/0.11
- kicad-mcp 系：github.com/AbdulAzeez0001/kicad-mcp | oaslananka/kicad-mcp-pro（KiCad 10→11 迁移/兼容性文档）
- TensorFleet：github.laiyagushi.com/TensorFleet/kicad-automation（或 github.com/TensorFleet/kicad-automation）
- KiCad 官方：docs.kicad.org cli（pcb drc 参数）| dev-docs.kicad.org IPC API/for-addon-developers（9/10 GUI-only、11 headless）| forum.kicad.info Post-V10 开发公告（11 ≈2027-02）
- pcbGPT：arxiv.org/abs/2606.01188（2026-05-31）
- tscircuit：github.com/tscircuit/tscircuit | github.com/tscircuit/tscircuit-autorouter | tscircuit.com
- JLCPCB：api.jlcpcb.com | jlcpcb.com/help/article/jlcpcb-online-api-available-now | jlcdfm.com | github.com/i2cjak/jlcpcb_api
- Cadence：newsroom.cadence.com AuraStack（2026-07-15）| Allegro X AI 白皮书
- 独立复测：anypcba.hashnode.dev/ai-generated-pcb-layout-how-far-can-kicad-gpt-4o-go

---
*报告生成：2026-09-12，多 agent 千轮研究（web_search + web_extract 交叉验证）。所有价格为研究时点官网公布值，落地前请复核最新页面。*