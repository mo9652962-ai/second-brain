---
aliases:
  - arxiv-2026-08-21-agent-llm
  - arxiv-agent-llm-2026-08-21
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-21
updated: 2026-08-21
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-21（⚠️ 补全性质）

> **检索时间**: 2026-08-21 GMT+8
> **⚠️ 补全性质声明**: arXiv 索引仍冻结在 **08-19T17:58Z**（全局最新 2608.19197 SPADE，与 08-20 速览同一提交池）。本次对 08-18+08-19 同池（652 篇唯一）做全量比对，在 08-20 已收录 20 篇之外**补录 17 篇强相关漏网**，不重写已收录内容。
> **数据源**: [export.arxiv.org](https://export.arxiv.org)

---

## 一、Agent RL 训练与自改进（5 篇）

### 1. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
- **ID:** [2608.17253v2](https://arxiv.org/abs/2608.17253v2) | [📄 PDF](https://arxiv.org/pdf/2608.17253v2)
- **作者:** Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, et al.
- **分类:** cs.AI, cs.LG, cs.CV
- **摘要:** 自奖励 RL 从模型自身推导奖励信号，但纯自生成反馈会强化偏差、降低多样性、最终同质化崩溃。Co-RL 让多个**不共享参数**的解耦模型同时做 RL，奖励来自同伴（peer-derived）。关键：增大群组多样性（异质模型族/规模/改写样本）可减少驱动自强化反馈环的相关误差，持续提升推理性能、保持行为多样性、抑制训练崩溃。无需任何 ground-truth：7 个文本基准平均 +3.0–8.6%，4 个多模态基准 +2.3–7.2%。开源 github.com/DrStranded/Co-RL。
- **关联度:** ★★★★ 对「自奖励 RL」的群体正则化——与 Hermes 多模型容灾/自改进主线相关

### 2. Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR
- **ID:** [2608.18574v1](https://arxiv.org/abs/2608.18574v1) | [📄 PDF](https://arxiv.org/pdf/2608.18574v1)
- **作者:** Lirui Luo, Guoxi Zhang, Hongming Xu, Rongqing Li, Cong Fang, et al.
- **分类:** cs.LG
- **摘要:** 新任务不断到来时重跑多任务 RLVR（MTRL）成本很高，故研究持续 RLVR（每个任务增量更新）。Continual Reasoning Gym 用文本+视觉推理任务组成 5 条序列。发现：①顺序 RLVR 遗忘温和但性能仍低于 MTRL；②共享推理让一个任务的训练平均支撑其他任务。提出 Continual Prompt Replay(CPR)：重放旧任务提示、用当前策略重新生成响应——唯一达到 MTRL 级性能的方法。
- **关联度:** ★★★★ 增量 RLVR 的实用解法——贴合墨题增量更新与 Hermes 持续自改进

### 3. Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements
- **ID:** [2608.17310v1](https://arxiv.org/abs/2608.17310v1) | [📄 PDF](https://arxiv.org/pdf/2608.17310v1)
- **作者:** Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, et al.
- **分类:** cs.LG
- **摘要:** 长时程 agentic RL 有稀疏奖励、credit assignment 难、训练栈重等瓶颈。本文主张**进化策略（ES）**更适合：全参数优化只需 inference 级显存、黑盒反馈易与 prompt 进化组合、轨迹级归因免跨时域分解奖励。Agentic ESOpt 用 reward-weighted 更新 + 扰动 σ 的余弦衰减。WebArena-Lite 上 Qwen3.5-27B 全量优化较 No-Skill 基线 +6.69%。
- **关联度:** ★★★ 轻量替代训练范式——RTX4060 8GB 本地微调场景相关；不依赖重 RL 基建

### 4. Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
- **ID:** [2608.17941v1](https://arxiv.org/abs/2608.17941v1) | [📄 PDF](https://arxiv.org/pdf/2608.17941v1)
- **作者:** Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, et al.
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** RLVR 依赖昂贵的 rollout，给不同难度样本统一预算低效。提出 plug-and-play **图结构在线难度估计器**：difficulty-aware 样本图 → Potts 先验共享隐难度 → Beta-Binomial 聚合 → 在线 mean-field 持续更新。可接入 sample-selection / rollout 分配调度器，无需专用探测，降低成本。
- **关联度:** ★★★ 直接命中 RLVR/GRPO 训练微调——图结构难度估计降探索成本，可迁移 Hermes 后训练实验

### 5. Debate Training Reduces Reward Hacking in RLAIF
- **ID:** [2608.17776v1](https://arxiv.org/abs/2608.17776v1) | [📄 PDF](https://arxiv.org/pdf/2608.17776v1)
- **作者:** Zachary Kenton, Lili Janzer, Rory Greig, Tian Huey Teh, Kirill Tyshchuk, et al.
- **分类:** cs.LG
- **摘要:** 用**辩论**（generator+critic 双玩家对抗、弱 LLM judge 裁决）做 RL 微调比 RLAIF 更抗 reward-hacking——judge 弱于 policy 时（监督更强 AI）问题最严重。数学任务（Gemini2.5 Flash 级 policy + 更弱 Flash Lite judge）：基线很快 hack judge，辩论全程维持其状态，峰值准确率恢复 45% gap。judge 更弱时也可用额外辩论轮补偿。
- **关联度:** ★★★ 「AI 监督 AI」风险的正向证据——呼应 Hermes 审批/验证/互证理念

---

## 二、Agent 记忆系统（4 篇）

### 6. MemFuse: Multi-Source Memory Fusion from Fragmented Observations
- **ID:** [2608.18704v1](https://arxiv.org/abs/2608.18704v1) | [📄 PDF](https://arxiv.org/pdf/2608.18704v1)
- **作者:** Chao Li, Yuanfa Li, Wenhao Wu, Xule Liu, Zhi Wang, et al.
- **分类:** cs.AI, cs.CL
- **摘要:** 长时记忆系统/基准多聚焦单一源文本，但真实情境信息常跨应用/设备/用户/时间片，须整合为连贯情景记忆并保留来源。**MemFuseBench**（多源融合基准）：Scene-to-Sensor 合成场景、证据锚定、对抗干扰，评估时间推理/跨源融合/抗噪。配套 MemFuse：事件层原子记忆保留源级证据，cluster 层在因果融合图上组织。
- **关联度:** ★★★★★ 与 Obsidian 第二大脑跨源融合直接对齐——跨目录/设备/时间线正是知识库融合痛点；MemFuseBench 方法论可借鉴做质量评估

### 7. ArborMem: Navigating Interaction States with Memory Forests
- **ID:** [2608.17534v1](https://arxiv.org/abs/2608.17534v1) | [📄 PDF](https://arxiv.org/pdf/2608.17534v1)
- **作者:** Zongwei Lv, Yuemeng Xu, Yilun Yao, Siyi Ding, Xinyu Tan, et al.
- **分类:** cs.CL
- **摘要:** 长期记忆把存取当「检索相关旧信息」，而不先判断当前回复对应哪个交互状态；多任务/多人/多计划交错、打断后重访时成瓶颈。ArborMem 用**可导航的交互态森林**：分支持局部一致轨迹、森林存多条可恢复轨迹。对每个输入定位状态、恢复分支上下文、跨支取用证据。比最强基线 +3.4–10.3pp。
- **关联度:** ★★★★ 显式维护「当前状态」而非只做检索——贴合多轮对话/跨任务切换；「树/森林」建模可借鉴知识图谱

### 8. D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory
- **ID:** [2608.17756v2](https://arxiv.org/abs/2608.17756v2) | [📄 PDF](https://arxiv.org/pdf/2608.17756v2)
- **作者:** Xule Liu, Yijun Liu, Chao Li, Kun Shao, et al.
- **分类:** cs.AI
- **摘要:** 持久记忆多阶段管线（接纳入库→检索→过滤→生成）错误难定位。D²ACCI 双环协议：外环的 paired 证据 + 受保护切片监测 + 阶段级诊断 trace，对记忆干预 promote/feature-flag/reject；引入分级可观测度 DCR、可复用伪迹。基线：LoCoMo 93.59%、LongMemEval 90.93%、PersonaMem-V2 57.20%，五组消融显著；诊断 trace 达 DCR@3 98–100%。
- **关联度:** ★★★ 记忆系统可归因方法论——「trace 级可定位性」恰是 Hermes 三层截断想解决的痛点

### 9. CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion
- **ID:** [2608.17911v1](https://arxiv.org/abs/2608.17911v1) | [📄 PDF](https://arxiv.org/pdf/2608.17911v1)
- **作者:** Zheling Tan, Jin Gao, Dequan Wang
- **分类:** cs.CL
- **摘要:** 语义检索对主题召回有效，却常漏语义距离远的早年经验/计划/动机（evidence-reachability 问题）。记忆图虽提供跨记忆结构，但弧多由语义重合驱动。CABLE 研究**互补前置化链接与展开**——用逻辑前置而非语义重叠补齐检索缺口，扩证据可及范围（前件、计划、动机）。
- **关联度:** ★★★★ 语义相似≠相关——对应观察到的知识图谱「缺链接」痛点；retrieval 盲区的学术回答

---

## 三、Agent 失败归因与评测（4 篇）

### 10. Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution
- **ID:** [2608.18575v1](https://arxiv.org/abs/2608.18575v1) | [📄 PDF](https://arxiv.org/pdf/2608.18575v1)
- **作者:** Ting-Wei Li, Yuanchen Bei, Xiao Lin, Hanghang Tong
- **分类:** cs.CL
- **摘要:** 多智能体（MAS）失败需归因于「哪个 agent+哪类错误」。现多靠 LLM（贵，长推断）。AFANet 用 step 级语义信号 + agent 级关系 GNN，参数小、推理近零，却匹配或超过 LLM 基线（in-domain），跨 GNN 结构稳健、OOD 可低成本测时优化。暗示归因不一定需要重型 LLM。
- **关联度:** ★★★ 低成本归因——调试/日志诊断用结构化方法替代部分 LLM 推理；「轻量初判 + 重 LLM 复查」可搬到交付质量门

### 11. StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows
- **ID:** [2608.17800v1](https://arxiv.org/abs/2608.17800v1) | [📄 PDF](https://arxiv.org/pdf/2608.17800v1)
- **作者:** Liya Zhu, Xin Ma, Tao Liu, Haodong Wang, Ge Zhang, et al.
- **分类:** cs.AI
- **摘要:** 现有基准多研究者主观选题，不能反映真实用户所需。StartupBench 基于**市场验证的 AI 创业产品**端到端流程：研究已获采纳的产品+流程+用户，识别真实任务转交付导向+细粒度评分。统一 harness 下最强模型只完成约 **30%**，多数部分完成；复杂指令遵循 + 领域专家知识是主要失败源。
- **关联度:** ★★★★ 真实用户任务的 E2E 测度——与闲鱼/代做「真实交付」评估一致；验证 agent 真实干活能力

### 12. FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents
- **ID:** [2608.18423v1](https://arxiv.org/abs/2608.18423v1) | [📄 PDF](https://arxiv.org/pdf/2608.18423v1)
- **作者:** Tianyou Wang, Chongyang Gao, Kezhen Chen, Chen Dong, Yinghao He, et al.
- **分类:** cs.AI
- **摘要:** LLM agent 能稳任一有界任务，但能否在长期规划（行动累积、环境反馈）保持稳定很难测。FM-Bench 让 agent 经营足球俱乐部 20 赛季、26 工具约 340–400 决策点。关键**确定性累计引擎**无需 LLM judge。15 个前沿模型几乎都能跑满整个赛季，头部由长期管理行为（如后期少透支预算）而非 token 消耗决定。
- **关联度:** ★★★ 长期竞技评测维度——长时程 agent 表现参考

### 13. What Makes Software Issue Resolution Tasks Difficult for Agents?
- **ID:** [2608.18280v1](https://arxiv.org/abs/2608.18280v1) | [📄 PDF](https://arxiv.org/pdf/2608.18280v1)
- **作者:** Ebtesam Al-Haque, Brittany Johnson
- **分类:** cs.SE
- **摘要:** agent 评测分数饱和但难度差异难解释。用大规模编码轨迹（patch 碎片、仓库规模等静态特征）+SHAP 归因：**任务难度可被静态属性显著预测（AUC 0.863）**，patch 碎片化与仓库规模主导，prompt 语言特征在中难度才显现。为「难度可控」基准铺路。
- **关联度:** ★★★★ 难度可静态预测——接单/定价分级的直觉一致；可用于排测试门槛

---

## 四、长时程 Web / GUI Agent（2 篇）

### 14. Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents
- **ID:** [2608.17319v1](https://arxiv.org/abs/2608.17319v1) | [📄 PDF](https://arxiv.org/pdf/2608.17319v1)
- **作者:** 腾讯 AIMAE 团队（Tianxiang Chen 等 37 作者）
- **分类:** cs.AI
- **摘要:** 浏览器 agent 短时干净演示表现好，但真实部署须维持数十次决策并稳定恢复错误、穿越复杂 UI。统一框架覆盖四层（execution/supervision/optimization/eval）并开源 **BrowserBench**（350 个双语任务、均 37.9 步，因现基准太短测不出长程失败）。结构化浏览器 harness 稳定原力、在线策略改良长时 credit、等价 SFT。27B：WebVoyage 81%、Online-Mind2Web 67%、BrowserBench 65%，开源下。同管线还迁移到一般 agent（Tau2/Claw/BFCL 平均 73.8）。
- **关联度:** ★★★★ 真实浏览器长时 agent 全套——浏览器自动化 + harness RL 双线；BrowserBench 补了评测实证

### 15. MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android
- **ID:** [2608.17659v1](https://arxiv.org/abs/2608.17659v1) | [📄 PDF](https://arxiv.org/pdf/2608.17659v1)
- **作者:** Sujin Chen, Lijun Li, Tianyi Du, Jing Shao
- **分类:** cs.AI
- **摘要:** LLM 驱动 GUI agent 自主操作手机进入真实部署，但处理不受信任环境内容（间接 prompt 注入/对抗指令）时可被用户无感知地操纵。MobileWorldSafety 建 142 个风险任务于真实 Android 应用，可编程验证 + 两阶段判定（规则+LLM）把负边从能力失败分开。**结果：6 个 agent 成功率 40.4%–66.9%，全部仍高度脆弱**。
- **关联度:** ★★★★ 环境注入攻击基准——sora 有真实 Android 自动化（uiautomator2/ADB）；环境注入是自主 agent 安全必解面

---

## 五、推理时学习与可扩展（2 篇）

### 16. Chain-of-Experience for Continual LLM Improvement
- **ID:** [2608.18027v1](https://arxiv.org/abs/2608.18027v1) | [📄 PDF](https://arxiv.org/pdf/2608.18027v1)
- **作者:** Haoqin Tu, Yunhao Fang, Yizhong Wang, Cihang Xie, Shen Yan
- **分类:** cs.CL
- **摘要:** 传统评测忽略测试时从经验继续改进的能力。CoE 在推理时通过迭代与自我/环境反馈形成持续改进环（超越 zero-shot）。八个 LLM 验证：迭代经验大多数一致超越无反馈基线，仅自反馈就获得可观增益（总体 +5.6%、成本低），并可与正确性等信号加成；弱反馈仍稳健。
- **关联度:** ★★★★ 推理时学习与自反馈——与「每日回顾/学习→研究→应用」互为佐证；强化 self-improving、gemini-second-opinion

### 17. Chain-of-Thought-Free Inference-Time Self-Reflection for LLMs (EvoResearcher)
- **ID:** [2608.18884v1](https://arxiv.org/abs/2608.18884v1) | [📄 PDF](https://arxiv.org/pdf/2608.18884v1)
- **作者:** Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Bing Li
- **分类:** cs.AI
- **摘要:** RL 训练推理（如 GRPO）昂贵且需可控环境。EvoResearcher 是**训练免费、纯推理时**的自反射协议：对冻结骨干迭代 generate→self-critique→revision，直到最大深度或收到 CONFIRMED 停止。四组件（正确/效率/深度/工具多样性）。在 BBH100/GSM8K/MATH 验证：**不提升高难精度，但 CONFIRMED 早停可同准确率省 82–88% 成本**——价值在成本而非精度。
- **关联度:** ★★★★ 推理时自校验/早停——低成本高质量确认，与 Hermes 交付门理念相投

---

## 本周值得关注的主题信号

1. **Agent 训练「去黑盒」**: Co-RL（同伴奖励群体正则）、ESOpt（进化策略替代 RL）、Continual RLVR（增量）、RLAIF 辩论治 hack —— 与 08-20 Harness-RL 互文，都偏省算力、免大量标注。
2. **记忆进入「结构+诊断」时代**: 多源融合（MemFuse）、交互态树（ArborMem）、阶段归因（D²ACCI）、前置链接（CABLE）——记忆不只是检索，而是结构+可调试管线，与 Obsidian 第二大脑同向。
3. **评测回归「真实任务/真实交付」**:market-validated（StartupBench）、长期竞技（FM-Bench）、难度可预测（CS 0.863）—— 与 sora 接单/定价「真实交付」直觉一致。
4. **长时程 Web/移动 Agent 的安全滞后**: Wuying-B（浏览器长空档真实页）与 MobileSafety（Android 环境注入 40–67%）—— 长空部署已到，安全仍严重滞后。
5. **RLAIF 治理与推理时护术**: 辩论（Debate）、自省早停（EvoResearcher）——都以「模型自我校验/互相制衡」之优于纯性能暴冲，与 Hermes 审批/验证理念同调。

---

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
---

## 📌 处理状态

- **reading → processed**（2026-08-23，arxiv-summarize cron）
- 核心贡献总结：[[arxiv-2026-08-21-core-contributions]]（MemFuse / StartupBench / MobileWorldSafety）
