---
tags: [GitHub, W39, ai, logits, 决策, 语义if, 本地推理, 方法论]
aliases: [SemIf, OpenJev, semantic if]
date: 2026-09-20
source: https://github.com/TheoLeeCJ/SemIf
---

# SemIf（原 OpenJev）— 从 logits 直接读决策，不生成文本

> 2026-09-20 W39 精选。开源复刻 Jev（TypeSafe 的语义决策模型）思路：**读 4B 模型 logits 里的选项概率，不走文本生成**。4 天破 1.9k★，HN 621-693 分，本周新建仓库 Top #4。MIT 协议。

## 一句话定位

「语义 if」：把 agent 的小决策（路由/重试/证据支持/分类）从「让模型写 JSON → 代码再解析回 if」改成「单次前向传播直接读各选项概率」——**零输出 token，5 倍提速**。

## 核心特征 / 技术架构

| 要素 | 说明 |
|:--|:--|
| 核心思路 | 请求里带上运行时定义的标准（criteria）+ 选项描述 → 模型一次 forward 输出每个选项的概率，不做解码 |
| 基准硬件 | 单张 RTX 3090（4B BF16 模型） |
| 最佳开源模型 | Qwen3.5-4B，balanced accuracy 0.813 |
| 性能实测 | 21 个二元标准：1.023s（logits 直读）vs 5.332s + 111 tokens（生成同 JSON）——**5.21 倍** |
| 共享模式 | 多标准共享一个长 state：并行后缀评估 20.03 decisions/s vs 2.33/s（fresh scoring） |
| 后端支持 | CUDA / WebGPU（浏览器里跑量化 GGUF，零安装）/ Apple Silicon MLX |
| 可复现 | fixtures、runners、raw timings、prompt hashes、known failures 全提交，谁都能重跑数字 |
| 免责 | 独立项目，不隶属 TypeSafe；不复刻 Jev 未公开的模型/训练，只复刻「运行时定义标准 + typed options → typed probabilities」接口模式 |

## 创新点详解

1. **决策不走文本生成**：大多数 agent 决策很小（路由这个/重试那个/证据支持 X 吗）——却付全价让 chat 模型写一句话再解析。SemIf 证明小模型单次前向足够。
2. **运行时定义标准**：criteria 和 option 描述随请求进来，不 bake 进微调——决策 schema 可热更新。
3. **串行前缀复用**：多个标准共享同一长 state，一次算前缀、并行算后缀——决策批处理优化。
4. **可复现文化**：timing/prompt hash/失败全入库，「重跑数字」成为项目卖点——契合 sora「实证优先」原则。

## 生态对照（同一 Jev 趋势）

- **browser-use/jev-ultrafast**（W39 同周热点）：browser-use 出的浏览器 agent，用 TypeSafe Jev 做「动作+目标元素」二合一决策，单次往返；Google Flights 搜索 7.07s，浏览器协议调用从 1,092 降到 101（-90.8%），成本 $0.0039/任务（98.4% 是 Jev 费用）。但它依赖**付费** TypeSafe API。
- **SemIf 的意义**：Jev 思路的开源可自托管替代——免费、本地、无 API 依赖。

## 💎 可借鉴点（对 sora 工作流）

1. **决策层与生成层分离**：Hermes/墨题里凡「模型做选择/打分/分类」的地方（模型路由、任务分流、评测打分、题库难度定级），可评估「小模型 logits 直读」替代「大模型写 JSON」——省 token + 降延迟。skill-pipeline 的 6 段质检门、smort_model_routing 都是候选。
2. **本机可行性**：sora 有 RTX 4060 8GB（非 3090），4B BF16 约 8GB——刚好贴边，可量化 GGUF（Q4）降到 ~3GB 跑 WebGPU/MLX。**不必立即落地，先作为「决策不走生成」的范式参考**。
3. **可复现基准文化**：SemIf 把所有数字/哈希/失败提交进 repo——sora 的评测（eval 意图隐藏规范、service-quality 评估器）已走这条路，可把「prompt hash + raw timing 入库」固化进评测 SOP。
4. **对墨题 AI 精讲/批改**：题目难度分级、错因分类（12 类归因）这类高频小决策，未来若量大可上 logits 方案压成本——留作 P2 优化项。

## 安装 / 验证命令

```bash
git clone https://github.com/TheoLeeCJ/SemIf && cd SemIf
pip install -e '.[test]'
# 直接读模式（需要 CUDA GPU；无 GPU 可用 --backend mlx 或浏览器版）
semif-score --mode direct --model Qwen/Qwen3.5-4B
# 验证点：对比 direct 与 autoregressive JSON 生成的延迟/token 数
```

## 总结评价表

| 维度 | 评价 |
|:--|:--|
| 技术含金量 | ★★★★★ 决策范式创新（logits 直读 vs 文本生成），工程小巧完整 |
| 值得安装 | 🔵 本机 4060 贴边可试跑验证范式；先不部署生产 |
| 趋势判断 | 「语义决策模型」是 2026 新范式（Jev 闭源 + SemIf 开源 + jev-ultrafast 应用），本地决策层会成本土 agent 优化重点 |
| 风险 | 4B 模型准确率有限（0.813 balanced accuracy）；复杂语义决策仍需大模型；项目仅 4 天，成熟度待观察 |

---
> 🗺️ 属于 [[MOC-Dev]]（AI 域） · [[MOC-GitHub]] · 周报 [[../../memory/2026/09/github-trending-w39|W39]]
