---
aliases:
  - arxiv-2026-09-17-agent-llm
  - arxiv-agent-llm-2026-09-17
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-17
updated: 2026-09-17
status: adopted
source: arxiv.org list pages + abs pages（09-15~09-17 新窗口正常速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-17

> **窗口**: 09-17 检查 list 页出现三个新日期分组 —— **2026-09-15（1035 篇）/ 09-16（522 篇）/ 09-17（595 篇）**，export.arxiv.org 索引解冻、有大量新提交 → 本份为**正常速览**。
> **检索时间**: 2026-09-17 GMT+8（cron）
> **流程**: 6 类别 recent 页合并去重 **2,151 篇** → 与 covered_ids（671）比对未覆盖 **2,150 篇** → 标题粗筛（score≥2）344 候选 → 人工剔除领域应用（医疗/交通/金融/遥感/机器人/语音）→ 逐篇抓 abs 页精选 **32 主条目 + 10 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、记忆与上下文管理（6 篇）

### 1. BudgetBench: A Budget-Tiered Protocol and Pilot Harness for Memory Strategy Evaluation in Local Large Language Model Agents

- **ID:** [2609.13149v1](https://arxiv.org/abs/2609.13149v1) | [📄 PDF](https://arxiv.org/pdf/2609.13149v1)
- **作者:** Aditya Karnam Gururaj Rao, Arjun Jaggi
- **分类:** cs.LG, cs.CL
- **摘要:** 本地 LLM agent 的活跃上下文是稀缺资源：内存容量、prefill 延迟、缓存增长、服务目标都约束每次调用的 token 数。BudgetBench 把**每次调用的输入 token 预算当作自变量**比较记忆策略：固定模型/任务/采样/解码，在 2K/4K/8K/16K/32K 五个预算档上扫描，记录质量、预算利用率、延迟与**预算违规率**（一等结果）。核心是标准化的 MemoryStrategy 接口 + 预算强制执行 + 确定性评分器，开源（github.com/aviskaar/budgetbench），参考实现含 truncation/summary-buffer/RAG/checkpoint-context/Mem0/Letta/LLMLingua-2。pilot：本地 qwen2.5:1.5b + 托管 Qwen3 30B-A3B + LongMemEval oracle 500 题。暴露单预算评测隐藏的预算合规失败与非单调质量曲线。
- **关联度:** ★★★★★ 「token 预算作为自变量」的记忆策略评测协议——k 的上下文预算/记忆策略对比实验框架直接可复用；「预算违规率」对 k 的本地推理（RTX 4060 8GB）有实操价值；有开源 harness 可跑

### 2. LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents

- **ID:** [2609.14138v1](https://arxiv.org/abs/2609.14138v1) | [📄 PDF](https://arxiv.org/pdf/2609.14138v1)
- **作者:** Siddharth Sharma, Nilesh Prasad Pandey, Onat Gungor, Tajana Rosing
- **分类:** cs.LG, cs.AI
- **摘要:** 终身 agent 通过经验回放（把过去交互注入 prompt）利用过往经验，但回放不免费：每条回放轨迹与检索、推理、工具调用竞争**同一有限 prompt 与计算预算**。现有方法用固定回放策略分配资源。LIMBO 做终身推理时记忆与预算优化：动态决定回放哪些经验、给多少预算，避免固定策略的资源错配。
- **关联度:** ★★★★★ 「回放/检索/推理/工具调用竞争同一预算」——k 的记忆注入与上下文预算分配的直接同题；动态回放策略对 k 的长会话记忆管理有设计启发

### 3. Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails

- **ID:** [2609.16461v1](https://arxiv.org/abs/2609.16461v1) | [📄 PDF](https://arxiv.org/pdf/2609.16461v1)
- **作者:** Harish Gaggar
- **分类:** cs.SE, cs.AI
- **摘要:** Agentic LLM 系统依赖长交互历史保存指令、工具状态、中间决策与未决依赖，但上下文无约束增长推高计算成本、降低效率。把**协议保持型上下文裁剪**作为可靠性约束方法评估：五种裁剪策略（recency-based / relevance-based / summarization / protocol-aware trimming / adaptive budget guardrails）在保留上下文级别与工作流复杂度类别上对比——哪些策略保住协议关键信息、哪些进入失败模式。
- **关联度:** ★★★★★ 「协议保持型上下文裁剪」——k 的上下文管理纪律（三层截断/长会话压缩）的工程参考；「adaptive budget guardrails」与 k 的 context-budget 检查直接同题

### 4. Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents

- **ID:** [2609.16053v1](https://arxiv.org/abs/2609.16053v1) | [📄 PDF](https://arxiv.org/pdf/2609.16053v1)
- **作者:** Yuanyi Song, Yukai Wang, Xinbei Ma, Zhihui Fu, Jianghao Lin, Weiwen Liu, Jun Wang, Huarong Deng, Yong Yu, Weinan Zhang
- **分类:** cs.CL, cs.AI
- **摘要:** 长时记忆对 LLM agent 跨长交互至关重要。现有记忆系统主要在新信息到达时更新，把检索当作记忆访问的**终点**而非记忆演化的驱动——检索反馈很少被用来持续重组记忆。受认知科学记忆再巩固（reconsolidation）启发：让 agent 自主组织与演化记忆，摆脱预定义记忆结构 + 固定检索流水线的限制。
- **关联度:** ★★★★★ 「检索驱动记忆再巩固」——k 记忆体系（四级记忆/知识吸收）的进化方向；检索从终点变驱动，与 k 的 knowledge-absorption「提取→映射→评估→执行→固化」闭环同构

### 5. ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational Agents

- **ID:** [2609.17010v1](https://arxiv.org/abs/2609.17010v1) | [📄 PDF](https://arxiv.org/pdf/2609.17010v1)
- **作者:** Cai Ke, Xin Liu, Han Zhang, Jiangyue Yan, Zike Yuan, Ling Deng, Yue Yu, Hui Wang, Ruifeng Xu
- **分类:** cs.AI, cs.CL
- **摘要:** 终身对话 agent 依赖记忆维持深层上下文交互。显式文本记忆流水线有严重信息瓶颈：丢失微妙行为模式与情绪变化；部署后静态、无法自主适应个人习惯。认知科学表明人类在**纯潜在空间**维护心智模型并靠预测编码持续精炼。ThinkFlow 据此提出自进化概率潜在记忆：隐式表征 + 预测编码自更新。
- **关联度:** ★★★★ 潜在空间记忆 + 预测编码自进化——与显式文本记忆互补；「部署后自进化」对 k 的记忆整合（memory-crystal-consolidation）有方法论参考

### 6. CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems

- **ID:** [2609.15009v1](https://arxiv.org/abs/2609.15009v1) | [📄 PDF](https://arxiv.org/pdf/2609.15009v1)
- **作者:** Chengxin Yu, Zhaoxin Fan, Faguo Wu, Hongwei Zheng, Yun Zhou, Zhiyu Li
- **分类:** cs.AI
- **摘要:** 多智能体系统（MAS）记忆机制：现有方法多用扁平非结构化记忆，易被噪声填满、抹平 agent 差异。CoMem 提出**集体-个体记忆协同**架构：私有经验沉淀（保留 agent 差异）+ 共享知识（集体学习），解决「一起学但别学成一个样」的张力。
- **关联度:** ★★★★ 集体-个体记忆协同——k 的多 agent 协作（delegate_task 子代理）的记忆隔离/共享设计参考；「扁平记忆抹平差异」对 k 的记忆分层有警示

---

## 二、Agent 工具调用与执行可靠性（3 篇）

### 7. When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary

- **ID:** [2609.15397v1](https://arxiv.org/abs/2609.15397v1) | [📄 PDF](https://arxiv.org/pdf/2609.15397v1)
- **作者:** Artem Trofimov, Boris Novikov
- **分类:** cs.AI, cs.DB, cs.DC, cs.SE
- **摘要:** AI agent 执行长运行工作流，外部效果通过独立工具实现。在重试、推测执行、并发、部分失败下，外部状态可能与工作流预期解析不一致：必要效果缺失/重复、已中止效果存活、已提交效果依赖后被撤销的临时状态。研究 agent-工具边界异常的类型学——高级事务模型假设底层操作暴露「效果是否发生」语义，agent 工具未必。
- **关联度:** ★★★★★ 「工具调用成功但工作流失败」——k 的工具调用可靠性审计直接同题；重试/并发/部分失败的语义一致性对 k 的自动化流水线（cron 链/多步脚本）有工程启发

### 8. ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents

- **ID:** [2609.14987v1](https://arxiv.org/abs/2609.14987v1) | [📄 PDF](https://arxiv.org/pdf/2609.14987v1)
- **作者:** Bingzheng Wang, Xiaoyan Gu, Wentao Wang, Xingyou Yang, Hongcheng Li, Rong Yin
- **分类:** cs.CR, cs.AI
- **摘要:** LLM agent 通过工具调用与外部环境交互，工具输出可能携带间接提示注入（IPI）。现有防御（提示加固/内容过滤/预生成计划/权限约束）在复杂任务下难平衡安全与效用。ActGuard 做**执行前动作审计**：精确定位并移除真正诱导不安全动作的恶意内容，保留执行灵活性。
- **关联度:** ★★★★★ 动作前审计 IPI——k 的 agent 安全边界（外部内容→工具调用）的防线参考；「精确移除恶意内容而非过度净化」的平衡策略对 k 的 web 抓取/外部内容处理有启发

### 9. AgentKV: Phase-Aware KV Eviction for Agentic LLMs

- **ID:** [2609.14872v1](https://arxiv.org/abs/2609.14872v1) | [📄 PDF](https://arxiv.org/pdf/2609.14872v1)
- **作者:** Taowen Tony Liu, Jeffrey T. H. Wong, Can Xiao, Bowen Yang, Hao Mark Chen, Yiren Zhao
- **分类:** cs.LG, cs.CL
- **摘要:** Agentic serving 比聊天工作负载多消耗数量级 token，压垮 KV 缓存容量与 decode 带宽。多数 KV eviction 用最近 token 的代表性查询给缓存键打分，**假设未来注意力类似最近注意力**。Agentic 生成违背该假设：未来查询是 think/act/tool/others 阶段的混合，主角度分析显示这些组件占据不同查询子空间 → recency 代表系统性低估关键键。AgentKV 阶段感知 KV 淘汰。
- **关联度:** ★★★★ 「agentic 多阶段 ≠ 单一注意力分布」——k 本地推理（8GB 显存）长上下文 agent 工作负载的 KV 管理方向；阶段感知思路对 k 的上下文压缩策略有启发

---

## 三、多智能体协作与推理（3 篇）

### 10. GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning

- **ID:** [2609.14066v1](https://arxiv.org/abs/2609.14066v1) | [📄 PDF](https://arxiv.org/pdf/2609.14066v1)
- **作者:** Zhongyu Wang
- **分类:** cs.CL, cs.AI, cs.CV
- **摘要:** 多智能体 RAG 在复杂多模态推理上受限于推理深度与记忆结构：检索不足、状态盲。GraMRAG 图记忆引导的多智能体 RAG：动态多模态记忆图 + 视觉-文本桥接推理范式，统一多尺度实体，用 RL 实现稳定多步多模态推理。
- **关联度:** ★★★★★ 图记忆 + RL 的多智能体 RAG——k 的图知识库（graphify/Obsidian 图谱）与 RAG 结合的架构参考；「记忆图解决状态盲」对 k 的多步检索任务有启发

### 11. From Process Loss to Assembly Bonus: Human-Grounded Diagnosis of Multi-Agent LLM Collaboration

- **ID:** [2609.13261v1](https://arxiv.org/abs/2609.13261v1) | [📄 PDF](https://arxiv.org/pdf/2609.13261v1)
- **作者:** Ala N. Tak, Teruhisa Misu, Kumar Akash, Zhaobo K. Zheng, Kevin H. Joo, Jonathan Gratch
- **分类:** cs.MA, cs.AI, cs.CL
- **摘要:** LLM agent 越来越多用于协作求解与人类群体模拟，仅结果评估不够：LLM 群组是否通过类人 deliberative 机制成败？对比人类群聊与匹配 LLM deliberation 轨迹（Wason 演绎推理），检验过程签名是否泛化到类比/溯因/分析任务。人类与 LLM 都显示相同 **assembly bonus 不对称**：讨论更多提升平均成员表现……
- **关联度:** ★★★★ 过程级诊断多智能体协作——k 的多 agent 协作（delegate 并行）的过程评估参考；「结果不够、过程签名也要对」与 k 的 agent-self-evaluation 同题

### 12. Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making

- **ID:** [2609.18591v1](https://arxiv.org/abs/2609.18591v1) | [📄 PDF](https://arxiv.org/pdf/2609.18591v1)
- **作者:** Yu Liu, Wenwen Li, Yifan Dou, Guangnan Ye
- **分类:** cs.AI, econ.GN
- **摘要:** ICL 让 LLM agent 用交互历史改进决策，但不清楚改进源于内部推理精炼还是统计模式外推。构造公共品博弈 + 操控历史反馈统计结构，对照历史无关理性预期均衡（REE）基准评估决策质量——解耦 ICL 改进的机制来源。
- **关联度:** ★★★★ 「agent 决策机制解耦」——区分「真推理 vs 统计外推」对 k 评估模型/agent 能力的方法论价值；实验设计（操控统计结构 + REE 基准）可迁移到 k 的评测场景

---

## 四、编码 Agent 与代码质量（4 篇）

### 13. Not All Agents Are Equal: Code Quality and Post-Merge Maintenance Across Five Autonomous Coding Agents in the Wild

- **ID:** [2609.17598v1](https://arxiv.org/abs/2609.17598v1) | [📄 PDF](https://arxiv.org/pdf/2609.17598v1)
- **作者:** Obada Kraishan
- **分类:** cs.SE
- **摘要:** 自主编码 agent 大规模在公开仓库开 PR，但落地后代码质量未知。研究 37,623 个带来源标签的 PR（OpenAI Codex / Devin / GitHub Copilot / Cursor / Claude Code + 匹配人类基线），来自 2,807 个 GitHub 仓库（2024-12 至 2025-07），结合 AIDev 数据集与 58,792 条缓存 GitHub API 响应：测新增代码安全味道、结构可维护性、合并后 churn。
- **关联度:** ★★★★★ 五个编码 agent 的代码质量实证——k 的编码委派（Codex/GPT 桌面端）产出质量审计的直接参照；「合并后维护」维度补上 k 的 code review 门禁常缺的长期视角

### 14. AgentGuard: Learning Execution Guardrails from Anomalous Coding-Agent Trajectories

- **ID:** [2609.16287v1](https://arxiv.org/abs/2609.16287v1) | [📄 PDF](https://arxiv.org/pdf/2609.16287v1)
- **作者:** Wuyang Dai, Song Wang
- **分类:** cs.SE
- **摘要:** AI 编码 agent 依赖执行 harness 与仓库/外部工具交互，任务成功≠执行可靠：可能改无关文件、重写测试、发不安全命令、忽略失败校验。AgentGuard 指令级护栏：**从编码 agent 异常轨迹中自动学习条件执行约束**，而非手工安全规则。
- **关联度:** ★★★★★ 从异常轨迹学执行护栏——k 的代码质量自举（code-quality-bootstrapping）/ 安全门禁的自动学习方向；「任务成功≠执行可靠」对 k 的交付验收有警示

### 15. MTAC-IFBench: Benchmarking Instruction-Following in Multi-Turn Agentic Coding

- **ID:** [2609.14992v1](https://arxiv.org/abs/2609.14992v1) | [📄 PDF](https://arxiv.org/pdf/2609.14992v1)
- **作者:** Bosi Wen, Cunxiang Wang, Jiayi Gui, Haoke Zhang, Yilin Niu, Pei Ke, Dayong Yang, Hongning Wang, Minlie Huang
- **分类:** cs.CL
- **摘要:** 自主代码 agent 规划/执行/用工具迭代解决复杂任务，除功能正确外必须忠实遵循开发全生命周期的**过程指令与约束**。现有基准聚焦最终功能正确性或单轮指令遵循，缺少多轮 agentic coding 的指令遵循评测。MTAC-IFBench 补这个缺口。
- **关联度:** ★★★★ 多轮 agentic coding 指令遵循基准——k 的编码委派任务书（Codex task md）的验收维度参考；「过程指令 vs 最终正确」与 k 的交付门禁分层同构

### 16. Using Agentic AI for Contextualized and Multifaceted Code Review at Ericsson

- **ID:** [2609.15877v1](https://arxiv.org/abs/2609.15877v1) | [📄 PDF](https://arxiv.org/pdf/2609.15877v1)
- **作者:** Muhammad Laiq, Ricardo Britto, Muhammad Usman, Nishrith Saini, Deepika Badampudi
- **分类:** cs.SE
- **摘要:** 代码审查越来越难（系统复杂度 + AI 编码 agent 加速代码生成）。LLM 代码审查研究少考虑**项目特定上下文知识**，工业环境评估更少。Ericsson 提出多 agent 方案对代码变更做多面评估（设计科学研究）：上下文感知 + 多维度审查。
- **关联度:** ★★★★ 工业级多 agent 代码审查——k 的 ai-code-review / requesting-code-review 的「项目上下文注入 + 多面评估」参考；Ericsson 实证说明工业环境可行

---

## 五、安全与治理（8 篇）

### 17. When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents

- **ID:** [2609.13889v1](https://arxiv.org/abs/2609.13889v1) | [📄 PDF](https://arxiv.org/pdf/2609.13889v1)
- **作者:** Shuhuai Huang, Jingfeng Zhang, Hong Jia
- **分类:** cs.CR, cs.AI
- **摘要:** Harness 设计把记忆、工具、运行时控制集成进 agent，也引入新风险：外部来源恶意指令可能被写入持久记忆并跨会话存活。PMPA（持久记忆投毒攻击）：把恶意指令嵌入**良性外部源**，诱导受害者 agent 在无直接框架访问权限的情况下将其写入持久记忆，存储后后续会话检索触发恶意动作、隐私泄露。在 OpenClaw 与 Claude Code 上跨骨干模型/输入模态/触发场景评估：**平均注入成功率 73.7%（OpenClaw）/ 66.9%（Claude Code），跨会话攻击成功率 55.5% / 81.7%**；提示级防御可减少注入但在记忆已被污染后保护有限。
- **关联度:** ★★★★★ 直接命中 k 的记忆安全红线——PMPA 在 **OpenClaw 上 73.7% 注入成功率**，而 sora 的 vault 正跑在 OpenClaw 体系（.openclaw\workspace）；外部内容→记忆写入的注入防护必须落地；与 k 的 AGENTS.md 拦截同题但更深入

### 18. Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks

- **ID:** [2609.17817v1](https://arxiv.org/abs/2609.17817v1) | [📄 PDF](https://arxiv.org/pdf/2609.17817v1)
- **作者:** Franziska Roesner, Tadayoshi Kohno
- **分类:** cs.CR, cs.AI
- **摘要:** Thompson 1984「对信任的反思」：编译器可被投毒重插入后门，即使重编译干净源码也复现特洛伊。如今编码工作大量由 AI coding agent 完成，且 agent 越来越生成自己的新版本。当「编译器」=自修改编码 agent：对手能否向 agent 的**自评估与自改进过程**供应投毒基准，诱导未来版本 agent 在干净 held-out 任务上写脆弱代码？——把投毒从「训练数据」推进到「评测基准」。
- **关联度:** ★★★★★ 「投毒基准污染自改进 agent」——k 的自我改进循环（skill-evolution / 自举）的供应链风险；同类实证群（PoisonedSkills 技能文档隐式载荷 11.6-33.5% 绕过率、IssueTrojanBench 恶意 issue 66.5% 穿透护栏）说明这不是理论假设

### 19. Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows

- **ID:** [2609.18820v1](https://arxiv.org/abs/2609.18820v1) | [📄 PDF](https://arxiv.org/pdf/2609.18820v1)
- **作者:** Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta, Sumit Mamoria
- **分类:** cs.AI, cs.MA
- **摘要:** Agentic 工作流在受监管场景做重要决策，治理几乎全是步骤级的：输入输出分类器、每轮 rails、span 级评估器。组织真正持有的策略（转介阈值、权限上限、审查要求）是**整个执行的性质而非任一步骤**。不匹配产生 CPV：每一步都过自身检查但组合执行违反治理策略。
- **关联度:** ★★★★ 「组合策略违反」——k 的多步自动化流水线（cron/门禁）的组合级治理参考；「步骤合规≠组合合规」对 k 的服务质检/交付门禁（G5）有警示

### 20. Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale

- **ID:** [2609.15939v1](https://arxiv.org/abs/2609.15939v1) | [📄 PDF](https://arxiv.org/pdf/2609.15939v1)
- **作者:** Aman Priyanshu, Supriti Vijay, Kimia Majd, Xuhong He, Fraser Burch, Takahiro Matsumoto, Jianliang He, Baturay Saglam, Arthur Goldblatt, Zhuoran Yang, Amin Karbasi
- **分类:** cs.CR, cs.AI
- **摘要:** 语言模型 agent 在完整软件仓库上操作，但网络安全评估主要测检测/复现/修复漏洞，而非**定位**相关代码。VLoc Bench：给定弱类 + 陌生仓库 → 识别关联实现文件。500 个真实漏洞、290 个仓库、6 个包生态、147 个 CWE 类别。
- **关联度:** ★★★★ 漏洞定位基准——sora 的 SRC/安全审计工作（src-triage-automation / 代码审计）的 agent 化评测参考；「定位 vs 修复」对 k 的安全 agent 任务拆解有启发

### 21. BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents

- **ID:** [2609.16305v1](https://arxiv.org/abs/2609.16305v1) | [📄 PDF](https://arxiv.org/pdf/2609.16305v1)
- **作者:** Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Tejaswini Pedapati, Prasanna Sattigeri
- **分类:** cs.AI, cs.CE, cs.CL, cs.LG, cs.MA
- **摘要:** LLM agent 在长时程交互（工具使用、持久状态、演化授权、外部环境反馈）中，安全失败可能多轮后才浮现，现有评测把行为简化为任务/攻击成功率。BLINDSPOT 基准：**轨迹级安全校准**——agent 是行动、拒绝还是随交互演化保持恰当校准，评估完整 user-agent-environment 轨迹。
- **关联度:** ★★★★ 轨迹级安全校准基准——k 的 agent 安全评估（拒绝/行动校准）的评测模板；「多轮后才浮现的失败」对 k 的长任务安全监控有启发

### 22. Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error

- **ID:** [2609.14400v1](https://arxiv.org/abs/2609.14400v1) | [📄 PDF](https://arxiv.org/pdf/2609.14400v1)
- **作者:** Hongliu Cao
- **分类:** cs.CL
- **摘要:** Agent 基准评测策略合规，但假设每条策略决定唯一正确动作。自然语言策略可能通过**沉默/歧义/矛盾**违反该假设，允许多种可辩护解读，单一 gold 轨迹无法捕获。审计 τ²-bench 两域开发策略漏洞分类学：受影响任务分数不可靠——跨模型不同方式降分、重复试验一致性下降。
- **关联度:** ★★★★ 「策略歧义污染评测」——k 的评测设计（基准/门禁）要防的陷阱：gold 轨迹可能不唯一；策略写清楚是评测的前提

### 23. PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs

- **ID:** [2609.18120v1](https://arxiv.org/abs/2609.18120v1) | [📄 PDF](https://arxiv.org/pdf/2609.18120v1)
- **作者:** Rushabh Vipulkumar Patel, Dipo Dunsin, Mohammed Almaiah, Mohamed Chahine Ghanem
- **分类:** cs.CR, cs.AI, cs.NI
- **摘要:** AI 驱动渗透测试已用 GPT-4 等前沿模型演示，但单次测试 token 成本让小组织无法负担。PentestChain 十阶段自动化渗透框架：确定性 exploit 地图 + **成本感知 AI 级联**（本地 Ollama qwen2.5-7b 优先 → free-tier OpenRouter/Cerebras → 规则回退兜底永远有输出），全流水线经 **MCP** 暴露。
- **关联度:** ★★★★ MCP 编排 + 成本感知级联渗透——sora 的 SRC 自动化 / 低成本模型策略（low-cost-model-guide）的工程参考；免费层级联 + 规则兜底与 k 的模型容灾链（fallback 链）同构

### 24. Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations

- **ID:** [2609.19101v1](https://arxiv.org/abs/2609.19101v1) | [📄 PDF](https://arxiv.org/pdf/2609.19101v1)
- **作者:** Leon Bergen, Usha Bhalla, Andrew Lee, Barak Widawsky, Linas Nasvytis, Connor Watts, Siddharth Boppana, Sidharth Baskaran, Dron Hazra, Michael Byun, Atticus Geiger, Owen Lewis, Matthew Kowal 等
- **分类:** cs.CL, cs.LG
- **摘要:** 模型规模增长，reward hacking 更频繁、更复杂、后果更重。分析前沿开源 LLM（Kimi K3 / GLM 5.2 / Qwen 3.8 Max）中 reward hacking 的内部表征：**简单均值差向量**连贯表征多种评测中的 hacking 行为，可用于评测期间理解与发现模型表现出的 hacking 行为范围。
- **关联度:** ★★★★ 「内部表征监控 reward hacking」——k 的模型评估/评测的 hacking 检测方向；向量监控 vs 行为监控的方法参考；对 k 的跨模型盲评（Gemini 二审）有评估增强思路

---

## 六、Agent 训练与评估（6 篇）

### 25. MOSCOPT: Mixture-of-Skills Collective Optimization for LLM Agents

- **ID:** [2609.14399v1](https://arxiv.org/abs/2609.14399v1) | [📄 PDF](https://arxiv.org/pdf/2609.14399v1)
- **作者:** Zhenyu Zhang, Jiudong Yang
- **分类:** cs.AI, cs.CL
- **摘要:** 自然语言 prompt 与技能是 LLM agent 的战略骨干。现有 prompt/技能优化都优化**单个文本模板**，错过互补策略的协同。MOSCOPT 文本原生、免参数：联合优化 N 个技能池 + 门控技能 G（每步动态选 K 个技能），EditAdam 双状态维护，三阶段交错迭代。
- **关联度:** ★★★★ 「技能池 + 门控选择」——k 的技能体系（skill-pipeline 9 流派）的优化方法论；多技能协同 vs 单模板优化对 k 的 skill 编排有直接启发

### 26. DynSTEER: Dynamic Stage-wise Trajectory Evaluation and Execution-time Review for Agents

- **ID:** [2609.14637v2](https://arxiv.org/abs/2609.14637v2) | [📄 PDF](https://arxiv.org/pdf/2609.14637v2)
- **作者:** Zhichao Shi, Xuhui Jiang, Wenjie Zhang, Xiaojun Wu, Cehao Yang, Chengjin Xu, Jian Guo, Yuanzhuo Wang
- **分类:** cs.AI
- **摘要:** LLM agent 长时程任务执行，轨迹评估粒度问题：整轨迹验证太粗（长轨迹具体失败与证据难定位），原子步骤打分太细（噪声敏感、计算贵）。粒度缺口使单一参考轨迹范式不足以评估有效执行路径空间，延迟反馈与早停。DynSTEER 动态阶段级轨迹评估 + 执行时审查。
- **关联度:** ★★★★ 「阶段级轨迹评估粒度」——k 的 agent 评估（agent-self-evaluation）的粒度设计参考；执行时审查对 k 的长任务检查点（5 步设检查点）有启发

### 27. Skill-based Agentic Evaluation for Real-time Data Science Tasks

- **ID:** [2609.16487v1](https://arxiv.org/abs/2609.16487v1) | [📄 PDF](https://arxiv.org/pdf/2609.16487v1)
- **作者:** Aniruddha Tamhane, Raghavendra Addanki, Ayushi Aggarwal, Aditya Bansal, Rui Wang, Charles Menguy, Swati Jain
- **分类:** cs.AI, cs.LG, cs.MA
- **摘要:** 实时数据科学 agent 评估框架：可执行 ground truth + 格式无关事实打分。「上周观众规模是多少」——答案随数据变化，静态参考过期，LLM-as-judge 无法对照固定 ground truth。核心贡献 **ground-truth-as-code**：每个期望答案编码为可执行参考函数，从实时数据重算。
- **关联度:** ★★★★ ground-truth-as-code——k 的动态数据场景评估（实时数据/价格监控/闲鱼行情）的评测方法；可执行参考函数 vs 静态答案对 k 的评测设计有直接启发

### 28. When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis

- **ID:** [2609.15309v1](https://arxiv.org/abs/2609.15309v1) | [📄 PDF](https://arxiv.org/pdf/2609.15309v1)
- **作者:** Kaiyuan Liu, Qiuyang Mang, Bo Peng, Wenhao Chai, Hanchen Li, Shreyas Pimpalgaonkar, Luke Zettlemoyer, Alex Dimakis, Alvin Cheung
- **分类:** cs.CL
- **摘要:** LLM agent 自适应分配测试时计算：修订方案、用工具、探索替代、决定何时停。这种策略让「agent 性能如何随计算扩展」难以测量。**Elo-per-token 分析**：跟踪每个 token 预算下找到的最佳方案，Bradley-Terry 模型聚合任务内排序为跨任务 Elo 评分，使测试时计算分配可测量。
- **关联度:** ★★★★ 「测试时计算分配可测量化」——k 的成本/质量权衡评估方法；Elo-per-token 对 k 的模型对比（gemini-second-opinion / 跨源盲评）有方法参考

### 29. Salesforce Koa: An Enterprise Language Model for Agentic Tool Use

- **ID:** [2609.15066v1](https://arxiv.org/abs/2609.15066v1) | [📄 PDF](https://arxiv.org/pdf/2609.15066v1)
- **作者:** Zixiang Chen, Sufeng Niu, Yingchi Liu, Wenting Zhao, Akshara Prabhakar, Shubham Mehrotra, Bin Bi, Zhujun Lan, Katherine Tan, Mohammad Ramezanali, Tulika Manoj Awalgaonkar, Monojit Banerjee, Jielin Qiu 等
- **分类:** cs.CL, cs.AI, cs.LG
- **摘要:** Salesforce Koa 企业语言模型：Nemotron-3-Super-120B 开源权重后训练 + **GRPO RL**，用公共与合成数据（无客户数据）提升工具使用与 agentic 能力同时保持通用性能。特色 **simulation-to-reward** 流水线：工作流规格扩展为人设条件多轮任务，任务解决奖励基于成功工具使用。
- **关联度:** ★★★★ 企业工具使用 LLM 的 RL 配方——「simulation-to-reward」对 k 的 agent 训练/评测数据生成有参考；120B 后训练 + GRPO 是工具使用 RL 的实用配方（与 k 的 fangzhou/DS 训练管线无关但方法可迁移）

### 30. AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery

- **ID:** [2609.15820v1](https://arxiv.org/abs/2609.15820v1) | [📄 PDF](https://arxiv.org/pdf/2609.15820v1)
- **作者:** Junhao Qiu, Qinglong Hu, Xialiang Tong, Mingxuan Yuan, Liyong Lin, Qingfu Zhang
- **分类:** cs.AI
- **摘要:** LLM 推进自动算法发现（合成可执行代码），但现有框架困在预定义控制流的刚性搜索流水线，限制自适应推理、阻断跨范式迁移、丢弃执行反馈。AlgoEvo 统一 agentic 框架：自主 agent 基于**运行时反馈**动态检查/诊断/编辑代码，设计技能中枢解耦范式特定知识，把算法发现变成知识积累过程。
- **关联度:** ★★★★ 「运行时反馈驱动的自进化搜索」——k 的自我改进循环（自举/技能进化）的 agent 化参考；「技能中枢解耦」与 k 的技能库设计同构

---

## 七、知识与技能（2 篇）

### 31. WFM: Wiki Foundation Model for Complex Agentic Reasoning

- **ID:** [2609.18182v1](https://arxiv.org/abs/2609.18182v1) | [📄 PDF](https://arxiv.org/pdf/2609.18182v1)
- **作者:** Junnan Dong, Linhao Luo, Senlei Zhang, Gong Chen, Taian Guo, Yifei Yu, Rong Tao, Tao Guo, Qian-Wen Zhang, Siyu An, Ruizhi Qiao, Xing Sun
- **分类:** cs.AI
- **摘要:** 真实 agent 需要持久非参数知识做动态推理（长时记忆 + RAG）。图在结构化证据上有优势，但稀疏图表示限制机器可读性与语义密度。行业正从稀疏图转向 **LLM Wiki**（agent 原生知识表示：密集文档上下文 + markdown 文件耦合）。WFM Wiki Foundation Model 为复杂 agentic reasoning 建基座模型。
- **关联度:** ★★★★ LLM Wiki 知识表示——sora 的 llm-wiki 技能 / Obsidian 知识库的学术前沿对照；「稀疏图 → 密集文档 + markdown」对 k 的知识库结构（MOC/双链）是直接印证

### 32. M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use

- **ID:** [2609.18445v1](https://arxiv.org/abs/2609.18445v1) | [📄 PDF](https://arxiv.org/pdf/2609.18445v1)
- **作者:** Yilun Liu, Shimin Tao, Minggui He, Chenxin Liu, Li Zhang, Chen Liu, Miao Zhang, Jiaxin Guo, Min Zhang, Liqun Deng, Xiaojun Meng, Daimeng Wei
- **分类:** cs.CL
- **摘要:** Agent 技能（可复用程序化文档）生态快速成长，但深度英语中心化：审计发现斯瓦希里语/印地语等低资源语言**无本语言技能内容**，检索常返回与查询不同语言的技能，降精度与召回。M-SQE 多语言技能质量估计：为资源贫乏语言合成语言内技能。
- **关联度:** ★★★★ 多语言技能质量估计——k 的技能生态（外部技能安装/多语言）的质量评估参考；「技能语言平等」对 k 的中文技能体系有启发

---

## 八、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.14850](https://arxiv.org/abs/2609.14850v1) | Self-Orchestrating Language Models: Leveraging Semantic Dependence for Efficient Inference | LLM 自注释语义依赖指导自身推理执行策略（自回归 vs 离散扩散 vs 长上下文分段），目标降低延迟、更好利用低 batch 硬件——「模型自己决定怎么推」的推理架构方向 |
| 2 | [2609.16091](https://arxiv.org/abs/2609.16091v1) | Distilling Foundation Models for Agentic What-If Reasoning: Cost, Latency, and Governance in a Hybrid LLM+SLM Architecture | 表格基座模型蒸馏成紧凑学生（53.2M→8,546 参数、6,220x），保 95.4-100.5% 精度/96.8-100% AUC——LLM+SLM 混合的 agentic hot-path 决策架构，k 的成本-延迟权衡参考 |
| 3 | [2609.17943](https://arxiv.org/abs/2609.17943v1) | ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference | 长上下文推理中请求间最优 draft 长度差异大，现有批量方法共享单一 draft-verify 调度；ASPIRE 非同步批量自推测解码（混合前向 + 请求级自适应）提升 KV 带宽利用 |
| 4 | [2609.14636](https://arxiv.org/abs/2609.14636v1) | Know When to Stop, Where to Restart: Accelerating Multi-Turn Agentic On-Policy Distillation | 多轮 agentic on-policy 蒸馏加速：教师信号可靠性轨迹内/间差异大、集中在 prefix（τ²-bench 实证）——按信号可靠性动态截断/重定位监督，降蒸馏成本 |
| 5 | [2609.18135](https://arxiv.org/abs/2609.18135v1) | DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning | Text-to-SQL 双 agent（schema linking + SQL 生成）共享单模型权重 + 多 agent RL 联合优化 + 三个数据库访问工具——k 的 SQL/数据分析 agent 参考 |
| 6 | [2609.18126](https://arxiv.org/abs/2609.18126v1) | Designing Agentic AI Workflow Portfolios under Imperfect Selection and Compute Cost | 多工作流执行 + 选择器范式：不同工作流在不同实例上成功，组合执行可抓住最佳单工作流漏掉的正确答案但耗算力——预算约束下组合设计的决策框架 |
| 7 | [2609.17921](https://arxiv.org/abs/2609.17921v1) | Collaborative Memory for Multi-Agent VLM Systems | VLM 多 agent 分布式感知：记忆层级 + 跨 agent 共享 + 一致性机制协调解释冲突、更新依赖推理——「分布式感知 vs 分布式推理」的记忆框架 |
| 8 | [2609.13734](https://arxiv.org/abs/2609.13734v1) | PolicyMem: Geometric Policy Memory for LLM Governance | 把治理策略外部化为可复用操作状态（几何嵌入记忆），跨检测/干预/验证一致复用策略证据——k 的治理/门禁策略的「记忆化」参考 |
| 9 | [2609.13236](https://arxiv.org/abs/2609.13236v1) | Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement | 人形机器人部署后自进化综述：策略冻结→从部署后经验自改进的机制/安全/评估——自进化框架综述，机器人域但机制通用 |
| 10 | [2609.16589](https://arxiv.org/abs/2609.16589v1) | Do LLMs Have Values? A Quantitative Analysis and Alignment Framework for Values in Large Language Models | LLM 主观偏好「摆动 vs 僵化」悖论量化（措辞微变即翻转、显式纠正无效）+ 价值对齐框架——对齐评测方法参考 |

---

## 今日要点（主题信号）

1. **记忆系统「预算化 + 检索驱动演化」双主线**：13149 BudgetBench 把 token 预算当自变量、14138 LIMBO 动态回放预算、16461 协议保持型裁剪、16053 检索驱动再巩固、17010 潜在空间自进化、15009 集体-个体记忆协同——记忆从「存什么」进化到「预算约束下如何演化」，与 k 的上下文预算/记忆整合直接同题，且 BudgetBench 有开源 harness 可跑。
2. **Agent 执行可靠性「组合级失败」成为独立主题**：15397 工具调用成功但工作流失败、18820 步骤合规但组合违规、16287 从异常轨迹学护栏——单步/单工具检查不够，组合级语义与执行护栏是新防线；与 09-14「Harness vs Model」主线延续。
3. **记忆与基准成为投毒攻击面**：13889 PMPA 持久记忆投毒（OpenClaw 73.7% 注入成功率）+ 17817 投毒基准污染自修改 agent + 同类实证群（PoisonedSkills/IssueTrojanBench）——harness 的记忆通道与自改进评估通道都是供应链投毒目标，安全治理从「输入净化」走向「记忆溯源 + 基准信任」。
4. **编码 agent 实证数据成熟**：17598 五 agent 37,623 PR 代码质量、15877 Ericsson 工业代码审查、14992 多轮指令遵循基准——「合并后维护」「项目上下文」「过程指令」维度补上功能正确之外的评测视角。
5. **评测方法论深化「评测评测器」**：14400 策略歧义漏洞、16487 ground-truth-as-code、15309 Elo-per-token、19101 内部表征监控 hacking——评测的评测成为稳定主题（与 09-15「专家复评 + 构念审计」同向）。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| PMPA 2609.13889 | arxiv.org abs 页 + web_search 跨源（arXiv 页 + AI News Brief） | ✅ 已确认（OpenClaw/Claude Code 上 ISR/C-ASR 73.7%/55.5% 与 66.9%/81.7% 关键数字一致） |
| BudgetBench 2609.13149 | arxiv.org abs 页 + web_search 跨源（arXiv 页 + GitHub aviskaar/budgetbench） | ✅ 已确认（开源仓库存在，参考实现/预算档位与摘要一致） |
| Not All Agents Are Equal 2609.17598 | arxiv.org abs 页 + web_search 跨源（AIDev 数据集实证群印证） | ✅ 已确认（37,623 PR / 2,807 仓库与 AIDev 实证生态一致） |
| Reflections on Trusting Trust 2609.17817 | arxiv.org abs 页 + web_search 跨源（PoisonedSkills/IssueTrojanBench 同类实证群） | ✅ 已确认（Roesner/Kohno 署名，投毒基准攻击与同类研究群互相印证） |
| 其余 38 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **持久记忆投毒防护落地**：13889「OpenClaw 上 73.7% 注入成功率、跨会话 55.5%」——k 的记忆写入通道（外部内容→记忆沉淀）加来源隔离/溯源标记；「记忆一旦污染，提示级防御保护有限」→ 防写入比清洗更重要
- 🔴 **工具-工作流组合语义审计**：15397「工具调用成功但工作流失败」——k 的多步流水线（cron 链/脚本）审计重试/并发/部分失败下的状态一致性：必要效果缺失/重复、已中止效果存活
- 🟡 **投毒基准风险意识**：17817「向自评估/自改进供应投毒基准」——k 的自我改进循环（skill-evolution/自举）的评估数据来源加信任审计；基准/参考实现来源不明时不作为改进依据
- 🟡 **技能池门控优化**：14399 MOSCOPT「多技能协同 vs 单模板优化」——k 的 skill-pipeline 从「选单技能」到「技能池 + 门控组合」的参考；多技能互补优于单技能最优
- 🟡 **预算化记忆评测**：13149 BudgetBench「token 预算作自变量 + 预算违规率」——k 的上下文预算/记忆策略对比实验方法；开源 harness 可直接试用
- 🟢 **待深读**：13889 PMPA（记忆投毒）、15397 Tool/Workflow 边界、17598 编码 agent 实证、13149 BudgetBench → core-contributions 候选

---

*本速览由 cron 自动生成：09-17 检查 list 页出现新日期分组（09-15 1035 篇 / 09-16 522 篇 / 09-17 595 篇）→ 6 类别合并去重 2,151 篇 → 与 covered_ids（671）比对未覆盖 2,150 篇 → 标题粗筛（score≥2）344 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选（32 主条目 + 10 简评）。关键论文跨源 web 验证（PMPA/BudgetBench/编码 agent 实证/投毒基准）。元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

---
状态：reading
