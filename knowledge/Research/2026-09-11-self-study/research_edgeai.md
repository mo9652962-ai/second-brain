---
title: "嵌入式边缘AI进阶路线-千轮研究-2026-09"
type: note
domain: Research
status: active
tags: [knowledge/research, 千轮研究, 边缘AI, 嵌入式]
date: 2026-09-12
---

# 嵌入式/边缘 AI 进阶路线研究报告（2026）

> 调研日期：2026-09-12 ｜ 调研人：Hermes 千轮研究小组（研究员 subagent）
> 调研对象：sora —— 已有 8051/STC89C52 基础（Keil C51/SDCC）、KiCad 自动化 PCB 流水线、RTX4060 8GB 本机，目标从 8 位单片机循序渐进到 NPU 加速边缘推理。
> 数据来源：官方产品页/商店（ST eStore、raspberrypi.com、Milk-V、乐鑫、幸狐、香橙派、Edge Impulse、fut中文代理&珠三角分销商）、GitHub（hailo_model_zoo/Ultralytics/RKNN）、实战博客（YOLOv8→RKNN 部署全记录、Hailo 量化精度讨论等）。所有价格为公开渠道参考价，标注币种；淘系价格存在波动。

---

## 〇、结论置顶（TL;DR）

1. **最务实的路径不是"梯形堆芯片"，而是"一条数据流"**：4060 上训练/微调 → 导出 ONNX → 量化（INT8）→ 部署到目标 NPU。这五步在 **ESP32-S3（¥40 级 MCU）**、**RK3588（¥500 级 SBC）**、**树莓派5+Hailo（¥1100 级）** 上走的是同一条方法论，只是工具链不同（TFLite Micro / RKNN / Hailo DFC）。掌握"训练→量化→部署"流水线 = 掌握所有 NPU 平台。
2. **2026 年边缘 AI 已分层成熟**：MCU 级 TinyML（ESP32-S3，免费 Edge Impulse 云 GPU 训练）、带真 NPU 的 Linux 小 SoC（RV1103/RV1106/SG2000/K230，¥55~370）、高性能边缘 NPU 平台（RK3588 / Pi5+AI HAT+，¥500~1600）。STM32N6 是 MCU 原生 NPU 旗舰（600 GOPS），已量产但开发板 ¥670+，适合"前瞻关注"而非第一块板。
3. **sora 的现有技能全部能直接复用**：8051 的 C 语言/寄存器/中断/串口功底无缝迁移到 32 位 MCU；SG2000（Milk-V Duo）甚至**板载 8051 低功耗协处理器**，可写 8051 代码；KiCad+JLCPCB 自动化 PCB 流水线可直接做 ESP32-S3/K230 定制底板；嘉立创生态里就有开源的 K230 庐山派 AI 视觉板。
4. **第一个可买的学习板：ESP32-S3-DevKitC-1（N16R8，¥35~45）**，配免费 Edge Impulse，1~2 周跑通第一个 TinyML 项目（关键词唤醒/手势识别），成本最低、生态最成熟、反馈最快。
5. **RTX4060 8GB 的角色 = 本地"训练/量化/验证工作站"**：跑 YOLOv8n/s 微调、PTQ/QAT 实验、导出 ONNX、TensorRT 对照实验完全够用；RKNN 转换与 Hailo 编译跑在 x86 CPU（WSL2），GPU 非必需。8GB 显存的边界：微调 YOLOv8s 以下模型无压力，本地 LLM 推理 7B Q4 可以，LLM 训练不行。

---

## 一、阶梯路线图（8位 MCU → NPU 边缘推理）

> 设计原则：每级只学"新的一层"，不重复造已会的轮子；每级有一个可交付的小项目；预算递增但每级都有 ¥100 以内选项。

### L0 ｜ 8 位 MCU 巩固（已有基础，1~2 周查漏补缺）
- **代表**：STC89C52RC（开发板 ¥15~30）/ Ai8051U / STC8A8K64S4A12（STC 32 位 8051 桥接，Ai8051U 原生 USB 免冷启动）
- **学习资料**：已有 skill（8051-embedded-dev）；STC 官网 stcmcudata.com、AiCube-ISP 图形化配置、SDCC+VS Code+EIDE 开源链
- **出口标准**：无痛切换 C 语言、寄存器操作、定时器/中断/串口 —— 这些概念在 32 位 MCU 上一字不差。
- **要点**：别再深挖 8051 外设，把时间留给下一级。可顺手了解 STC32G128/Ai8051U 的"32 位化"，但不必停留。

### L1 ｜ 32 位 MCU + RTOS（1~2 个月）
- **代表**：STM32F103C8T6 最小系统板（¥15~30）；国产替代 GD32/CH32V003（CH32V003 芯片低至 ¥1~2，资料对标 STM32）；进阶 STM32F4（¥30~50，带 FPU/DSP 利于后续 AI）
- **学习资料**：正点原子/野火 STM32 教程、HAL 库 + CubeMX、FreeRTOS、韦东山《单片机核心/RTOS 必学》（免费入门）；嵌入式 2026 学习路线图（0rg.cn）
- **交付项目**：多任务"秒表+串口日志+LED 状态机"（FreeRTOS 三个任务），体会中断/队列/信号量
- **为什么必须过**：带 NPU 的国产 SoC（RK 系列）和 Linux 嵌入式要求读得懂 ARM Cortex-M/A 的 C 与内存模型；跳过这层直接上 Linux 会大量返工。

### L2 ｜ AI MCU：TinyML 入门（带向量加速，无独立 NPU）（2~3 个月）
- **代表**：**ESP32-S3-DevKitC-1 N16R8（¥35~45）**；Seeed XIAO ESP32S3 Sense（¥70~90，板载相机+麦克风）；ESP32-S3 芯片 ¥15~25
- **规格**：双核 Xtensa LX7 @240MHz，512KB SRAM + 8MB PSRAM，Wi-Fi/BLE5，向量指令（AI Vector Instructions）加速矩阵乘；跑 MobileNetV1 比老 ESP32 快 2~3 倍（业界实测：95×95 输入 MobileNetV2 int8 推理约 210ms，为 P4 的 1/7.5）
- **工具链（2026 现状）**：Edge Impulse **免费 Developer Plan**（2025-05-06 起：GPU 训练、60 分钟训练任务、FOMO/YOLO-Pro 高级模型、3 个私有项目、3 协作者、可部署 ≤1000 台设备）+ TFLite Micro + Arduino/ESP-IDF；INT8 量化体积缩 4 倍、速度提 2~3 倍
- **交付项目**："你好小智"式关键词唤醒（INMP441 麦克风，总成本 ¥50~80）或 5 类手势识别（BMI270 IMU），或 OV2640 图像分类
- **坑**：必须开 PSRAM（OPI PSRAM），否则 malloc 失败；模型选 MobileNetV2 0.1 / FOMO 级轻量架构

### L3 ｜ 带真 NPU 的 Linux 小 SoC（"MCU 价位的 NPU"）（2~3 个月）
- 三选一（预算导向）：
  - **Luckfox Pico Mini（瑞芯微 RV1103，0.5 TOPS int8，官方 ¥54.5 起，淘宝 ¥69~83）**——最便宜的真 NPU Linux 板，Cortex-A7 1.2GHz + 内置 RISC-V MCU + ISP，RKNN 工具链
  - **Milk-V Duo / Duo S（算能 SG2000/SG2002，0.5~1 TOPS，官方 $9.9 起 / 国内 ¥85~158）**——RISC-V 双核 + 可切 Arm A53 + **板载 8051 MCU@6~8KB SRAM**（与 sora 现技能无缝衔接），可跑 Linux/RTOS；Duo 256M 为 1 TOPS
  - **嘉立创·庐山派 K230-CanMV（嘉楠 K230，等效 6 TOPS【官方标注】，RISC-V 双核 C908 1.6GHz，¥240~370）**——CanMV **MicroPython** 直接写 AI 应用，嘉立创自家生态（与 sora 的 JLCPCB/KiCad 同源），YOLOv5s 实测 >38 FPS@INT8
- **学习主题**：Linux 基础（命令/交叉编译/设备树常识）、ONNX→量化→板端推理闭环、C/Python 双接口
- **交付项目**：把 L2 的模型量化后部署到 NPU（YOLOv8n INT8 检测或图像分类），对比 CPU/GPU/NPU 三端延迟
- **Sufficient evidence**：RV1106 系列官方页、Milk-V 官方页与斑梨分销价、立创开源硬件平台庐山派页

### L4 ｜ 高性能边缘 NPU 平台（"边缘服务器"级）（3~6 个月）
- **代表 A：香橙派 Orange Pi 5 Pro（RK3588S，6 TOPS NPU，8nm）**——4GB ¥499 / 8GB ¥649 / 16GB ¥859（官方创客价）；Orange Pi 5 系列 4~32GB ¥699 起
  - 常见板型选择：5 Plus（双 2.5G 网口+四屏异显，软路由/NAS 边算）、5 Max（LPDDR5+3 摄像头+板载 Wi-Fi 6E，机器人视觉）、5 Ultra（+HDMI 输入，视频采集）
  - NPU 实测：YOLOv8n INT8 约 **25~35ms/帧（40fps）**；INT4/INT8/INT16/FP16 混合量化
- **代表 B：Raspberry Pi 5 + AI HAT+（Hailo）**——Pi5：4GB $70 / 8GB $95 / 16GB $145（2025-12 官方调价后）；AI HAT+：13 TOPS（Hailo-8L）**$70** / 26 TOPS（Hailo-8）**$110**、功耗 5~10W；总价（8GB+HAT+26T）约 $205 ≈ **¥1500 国内行货 / ¥1100+ 海淘**
  - 原 AI Kit（M.2 HAT+ 形态）**已停产**，转为 AI HAT+（Hailo 直焊 PCB，PCIe Gen3，散热更好）；旧 AI Kit 型号部分渠道仍有 $60~110 尾货
  - Hailo 生态（2026 成熟度★★★★☆）：hailo_model_zoo（Hailo-8/8L 分支 v2.x + DFC v3.x）预训练模型库；**Ultralytics 原生 `model.export(format="hailo")`** 一键编译 HEF，支持 YOLOv8/11/26 检测/分割/姿态/OBB/分类/语义分割/深度估计；量化精度公开可查（如 yolov8n COCO mAP 36.4 量化 vs 37.0 全精度，yolo26n 37.4 vs 39.2）
- **对比说明**：RK3588 的 NPU 适合全栈开发者（RKNN 中文资料多、建模工具链免费、可跑 DeepSeek-R1 蒸馏小模型）；Pi5+Hailo 的生态更新更"开箱即用"（Arm 官方相机栈原生集成），但 Hailo-8/8L 是**视觉卷积模型专精**——transformer 类（YOLO26 注意力块）有 INT8 结构性精度上限（8L 实测 ~93~94%），跑 LLM 无意义
- **交付项目**：多路 USB/CSI 摄像头实时目标检测（人数统计/缺陷检测），或把 4060 训练的私有数据集模型全流程部署

### L5 ｜ 前瞻：MCU 原生 NPU 旗舰（关注，暂不必买）
- **STM32N6（ST Neural-ART，600 GOPS @1GHz）**：Cortex-M55 800MHz + 4.2MB SRAM，N6x7 带 NPU、N6x5 不带；2026 已量产，芯片约 **$10.6~12（1ku）**；NUCLEO-N657X0-Q 评估板 **$75.37（ST 官网）/ ¥671（RS）**；工具链 ST Edge AI Suite（STM32Cube.AI 的继任者）
- **ESP32-P4（乐鑫，双核 RISC-V 400MHz + NNA 硬件加速 + H.264 + MIPI-CSI/DSI）**：2026 年生态爬坡中（V3.x 芯片修订、板价 ¥180~250 官方板 / ¥39.9~59.9 低价尝鲜板）；无内置无线，需外挂 C6（+$2~3）；TFLite Micro 官方组件化支持；ESP32-S31（新，Wi-Fi6+BLE5.4+802.15.4 单芯片）是"无线版 P4 平替"定位
- **观察点**：ST Edge AI Suite 的免云本地化、P4 供货稳定化、国产杏芯/算能 RISC-V+NPU 出货量爬坡（2026 年 RISC-V AI 芯片出货预计年增 73.6%）

---

## 二、边缘 AI 主流方案对比 2026（实证定价 + 生态成熟度）

| 方案 | 类型 | 算力 | 参考价（2026-09） | 工具链 | 生态成熟度 | 上手难度 | 适合 |
|---|---|---|---|---|---|---|---|
| ESP32-S3 (DevKitC N16R8) | MCU+向量加速 | ~0.1 TOPS 级推理 | **¥35~45** | Edge Impulse(免费)/TFLM/Arduino | ★★★★★ | ★☆☆☆☆ | TinyML 入门；语音/轻图像 |
| ESP32-P4 (Function EV) | MCU+NNA | NNA 加速（95×95 int8 ~28ms） | ¥180~250（低价板 ¥40~60） | ESP-IDF+TFLM | ★★★☆☆ | ★★☆☆☆ | 带屏 HMI+AI 视觉（无无线，需 C6） |
| Luckfox Pico Mini (RV1103) | Linux SoC+NPU | 0.5 TOPS int8 | **¥55~83** | RKNN-Toolkit2 | ★★★★☆ | ★★★☆☆ | 最便宜真 NPU Linux 板 |
| Milk-V Duo S (SG2000) | RISC-V SoC+TPU | 0.5~1 TOPS int8 | $9.9 起 / 国内 ¥85~158 | TPU-MLIR / Linux | ★★★☆☆ | ★★★☆☆ | RISC-V 学习；**板载 8051 协核** |
| 庐山派 K230-CanMV (嘉楠 K230) | RISC-V SoC+KPU | 等效 6 TOPS（官方） | ¥240~370 | CanMV(MicroPython)/K230 SDK | ★★★★☆ | ★★☆☆☆ | 嘉立创生态；MicroPython AI |
| Luckfox Pico Ultra (RV1106G3) | Linux SoC+NPU | 1 TOPS int8，8GB eMMC | ¥253+ | RKNN-Toolkit2 | ★★★★☆ | ★★★☆☆ | 小体积量产级视觉节点 |
| Orange Pi 5 Pro (RK3588S) | SBC+NPU | 6 TOPS，混合精度 | **¥499/649/859** | RKNN-Toolkit2/ONNX | ★★★★★ | ★★★★☆ | 边缘服务器/NVR/机器人 |
| Raspberry Pi 5 + AI HAT+ | SBC+协处理器 | 13 TOPS($70)/26 TOPS($110) | Pi5 $70~145 + HAT+ = **¥1100~1500 全套** | Hailo DFC/HailoRT/Ultralytics 原生 | ★★★★☆ | ★★★★☆ | CV 生产级、相机栈原生集成 |
| STM32N6 (Nucleo) | MCU+NPU | 600 GOPS | 板 $75 芯片 $10~12 | ST Edge AI Suite | ★★★☆☆ | ★★★★☆ | 车规/工业 MCU 端 AI（BGA 封装，JLC SMT 可代工） |
| NVIDIA Jetson Orin Nano 8GB（对照） | SoM（CUDA GPU） | 40 TOPS INT8 | ~$250 起 | TensorRT / JetPack | ★★★★★ | ★★★★☆ | 需 CUDA 生态的强算力边缘；预算最高 |

**生态成熟度结论**：
- **TinyML（MCU 级）**：ESP32 系 + Edge Impulse + TFLM = 最成熟、免费、社区最大；2026 年 Edge Impulse Developer Plan 免费化是重大利好（云 GPU 训练 + 生产许可 + 1000 台部署）。
- **RKNN 系（瑞芯微）**：中文资料最全、rknn_model_zoo 覆盖 YOLO 全系、工具链免费；坑集中在：需 x86 Linux（WSL2）转换、toolkit/runtime 版本必须严格对齐、量化需代表性校准集（500 张实测场景图 ≈ 0.5% 精度损失，50 张乱选 ≈ -5%）。
- **Hailo 系**：模型库+Ultralytics 原生导出让"私有数据→HEF"链路最短；编译一次、板端只装 HailoRT；但 Hailo-8/8L 对 transformer 支持有结构天花板（见上）。
- **嘉楠 K230**：CanMV 的 MicroPython 体验极简，适合纯应用开发者；K230 也是人脸/多模态模组常见底座。
- **STM32N6**：MCU 原生 NPU 的"正规军"路线，量产已开始（ST eStore 在售、多分销商有货），但评估板 ¥670+ 与 BGA 封装决定了它更适合经 JLC SMT 做定制板而非开局。

---

## 三、本地 RTX4060 8GB 在嵌入式 AI 中的角色

**定位：训练/量化/验证工作站，不是推理板。** 全链路工作流：

```
[4060 工作站]                     [目标边缘平台]
① 数据标注/增强
② 训练/微调 (Ultralytics YOLOv8n/s、MobileNet、FOMO)
   └─ batch16 @640px 约占 <3GB 显存，分钟级收敛（246 图 150 epoch 实测）
③ 导出 ONNX (opset12, simplify, 拆分 NMS 到 CPU)
④ 量化：
   - RKNN-Toolkit2 (x86 Linux/WSL2, CPU 即可，GPU 非必需)
     校准集 = 500 张真实场景图 → INT8 精度损失 ~0.5%
   - Hailo DFC → HEF (x86 编译，板端只装 HailoRT)
   - TFLite Converter 全 int8 → .tflite (ESP32-S3/P4)
   - TensorRT INT8/FP16 → 4060 自身做"性能上界"对照
⑤ 部署验证
```

- **训练**：8GB 显存足够带动 YOLOv8n/s/m 微调、MobileNet 系列、知识蒸馏学生模型；**YOLOv8l/x 大模型与 LLM 微调不在 8GB 舒适区**（4060 只适合 7B Q4 量化模型推理，如 5~6GB 占用）。
- **量化的两把刀**：PTQ（训练后量化，快但 INT4 精度通常不可接受）与 QAT（量化感知训练，精度损失小但改训练流程）；嵌入式 NPU 主流用 **PTQ+代表性校准集**，QAT 用于对精度敏感的模型（如缺陷检测）。
- **4060 特有的价值**：TensorRT 同模型对照（量化后 mAP/延迟基准），做 NPU 部署前的"精度债务"预算；Edge Impulse 也支持本地 CLI 训练（或用它的云 GPU 训练，免费额度 60min/任务）。
- **必须提前知道**：RKNN-Toolkit2 和 Hailo DFC 都跑在 **x86 Linux**——Windows 上需要 **WSL2/Ubuntu**（4060 的 CUDA 仅供训练阶段）；rknn-toolkit2 安装用 `--no-deps`（避免强制降级 torch），protobuf≤4.25.4，onnx 1.16。

---

## 四、与 sora 现有技能的衔接点

1. **8051/STC89C52（Keil/SDCC）→ 无缝升级**：寄存器/中断/串口/C 语言模型在 32 位 MCU 上完全一致；SDCC→Arm GCC、Keil→CubeIDE/EIDE 是同类 IDE 迁移；Ai8051U/STC32G 本身就是"32 位 51"。RTOS（RTX51 Tiny）经验可迁移到 FreeRTOS。
2. **SG2000/Milk-V Duo 板载 8051 协处理器**：这是 sora 独有的先发优势——Duo/Duo S 内嵌 8051 MCU（6~8KB SRAM）可在主核休眠时做低功耗传感/唤醒，用现有 8051 技能可直接上手，国内资料少、竞争蓝海。
3. **KiCad 自动化 PCB 流水线 → 定制 AI 底板**：现有流水线可直接产出 ESP32-S3/XIAO 底板（相机+IMU+继电器）、K230 接口板；JLCPCB 打样+SMT 一条龙你也熟。STM32N6 是 BGA，手焊不现实，正好用 JLC 贴片。
4. **嘉立创生态闭环**：庐山派 K230 是嘉立创开发板团队出品（开源于立创开源硬件平台），与 sora 的 EasyEDA/JLC PCB/立创商城同一生态——原理图、BOM、教程都在熟悉的地方，甚至可借自己的 PCB 流水线改版它。
5. **4060 → NPU 产能闭环**：你的 4060 就是"模型工厂"，产出 ONNX/HEF/RKNN 供给你的板子；把"训练→量化→部署"变成可复用流水线脚本（参考 VaporTang/yolo-vision-pipeline-rknn 的 YOLOv8→ONNX→RKNN 统一仓库），与现有 PCB 自动化形成"硬件+算法"双流水线。

---

## 五、立即行动建议（含第一个可买的学习板）

1. **买板（本周）**：**ESP32-S3-DevKitC-1 N16R8（¥35~45）** 作为第一块学习板；预算充足则升级 Seeed XIAO ESP32S3 Sense（~¥90，自带相机+麦克风，做视觉/语音都行）。注册 Edge Impulse 免费 Developer Plan，跑通官方教程，1~2 周内交付第一个"关键词唤醒"项目（总物料 ¥50~80）。
2. **搭 4060 模型流水线（2 周内）**：Win 上装 WSL2+Ubuntu，用 Ultralytics 训练 YOLOv8n（小数据集 100~300 张，batch16 约 <3GB 显存），导出 ONNX（opset12+simplify），在 PC 上用 ONNX Runtime 验证推理——先于任何 NPU 板跑通"训练→导出"半程。
3. **选一块真 NPU 板（第 3~4 周，三选一）**：
   - 预算/蓝海导向：Milk-V Duo（≤¥100，带 8051 协核，写第一个 RISC-V+8051+TPU 混合程序）；
   - 纯视觉/省心导向：庐山派 K230（¥240~370，嘉立创生态，MicroPython 三行代码跑 YOLO）；
   - 性能/长期导向：Orange Pi 5 Pro 8GB（¥649）或 Pi5 8GB+AI HAT+ 26T（全套 ~¥1500，生态最顺）。
   - 目标：在板上跑通 YOLOv8n INT8，与 4060 上 TensorRT 的延迟/精度做对照表。
4. **补齐 Linux 嵌入式短板（并行，每日 0.5h）**：韦东山免费入门教程或 2026 嵌入式学习路线图（0rg.cn），重点 Linux 命令/交叉编译/Makefile/设备树概念；目标不是成为内核专家，而是能看懂 NPU 板上 SDK 的构建与运行。
5. **合成作品（第 2 个月）**：用 KiCad 流水线画一块"ESP32-S3 底板（相机+IMU+OLED+继电器）"，JLC 打样贴片，把 L2 的 TinyML 模型装进去，交付一个可演示的"离线手势/图像控制"整机——这就是闲鱼可接单、可写进简历的完整边缘 AI 作品。

---

## 六、证据来源（关键链接）

- STM32N6 定价/量产：estore.st.com STM32N6 系列页、STM32N657X0 产品页（$11.26/10k）、NUCLEO-N657X0-Q（$75.37）、RS 中国（¥671）、Future Electronics
- NUCLEO-N657X0-Q：digikey / iceasy（¥676）
- Raspberry Pi：raspberrypi.com/products/ai-kit（已停产）、ai-hat（13T $70 / 26T $110）、Pi 5 产品页与 2025-12 调价公告（4GB $70 / 8GB $95 / 16GB $145）、Adafruit 5979
- Hailo 生态：github.com/hailo-ai/hailo_model_zoo（v2.x=Hailo-8/8L，master=10/15；量化精度表）、Ultralytics Hailo 集成文档、Hailo 社区（YOLO26 8L 精度上限讨论）
- Rockchip：Radxa RKNN 文档、Orange Pi 官网/IT之家（5 Pro 499/649/859）、OrangePi 5 Plus/Max/Ultra 对比（smzdm/CSDN）、YOLOv8→RK3588 部署全记录（腾讯云 CSDN，25ms/帧、校准集 500 张经验）、thinkmoon 博客（NMS 拆分/量化/性能剖析实战）
- ESP32-S3/P4：xjtaxi TinyML 手势控制台（S3 价位与物料）、makeronsite ESP32 TinyML 语音/图像两篇、xiaozhi.dev 技术规格页（S3 芯片 ¥15~25、DevKitC ¥35~45）、乐鑫 ESP32-P4 v3.x 新闻、CSDN P4 边缘 AI 实战（95×95 int8 28ms）
- 国产 NPU 板：luckfox.cn（Pico Mini ¥54.5 / Pico ¥64.6 / Ultra ¥253.5，RV1103/1106）、milkv.io（Duo S $9.9，SG2000 含 8051）、立创开源硬件平台 庐山派 K230、szlcsc K230 首发页、kendryte.com
- Edge Impulse：edgeimpulse.com（Developer Plan 免费化公告 2025-05-06、FAQ：≤1000 台免费部署）
- 学习方法论：0rg.cn 2026 嵌入式学习路线图、51CTO 边缘 AI 能力树（PTQ/QAT、RK3588 算子坑）、韦东山 100ask

*注：淘系/分销价格（¥）为 2026-09 抓取参考价，可能波动；官方价（$）来自官方商店/公告。K230「等效 6 TOPS」为官方标注口径，KPU 实际典型网络吞吐见官方 FPS 表（ResNet50≥85FPS / MobileNetV2≥670FPS / YOLOv5s>38FPS @INT8）。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
