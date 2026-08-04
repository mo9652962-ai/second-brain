---
aliases:
  - arXiv Weekly Roundup 2026-08-04
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - paper-review
created: 2026-08-04
updated: 2026-08-04
status: reading
source: https://arxiv.org/
domain: research
---

# arXiv Weekly Roundup — AI Agent & LLM Papers

**Date:** 2026-08-04 | **Week 32**  
**Papers:** 15 new relevant papers (cs.AI/cs.CL/cs.SE/cs.RO/cs.MA)

---

## 📄 Paper Highlights

### [2607.29347v1] SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery

- **Authors:** Jiamin Wu, Peishan Xiang, Jingyang Chen, Yuqing Zhu, Yuxi Li, Ling Luo, Qihao Zheng, Jialiang Zu, Yongchao Wu, Mindong Liu, Haitao Wu, Chaofan Hu, Yijie Sun, Yuqi Hang, Yu Zhu, Shuo Li, Yue Fan, Shiyang Feng, Wanghan Xu, Tianlei Zhang, Jie Zhang, Wenlong Zhang, Bo Zhang, Kai Wang, Lei Bai, Mianxin Liu, Wanli Ouyang, Jiulin Du, Chunfeng Song
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.MA, cs.AI | **Primary:** cs.MA
- **Links:** [Abstract](https://arxiv.org/abs/2607.29347v1) | [PDF](https://arxiv.org/pdf/2607.29347v1)
- **💡 短评:** 多 agent 协作加速神经科学发现,科学发现自动化(Science Agents)方向

**Abstract:**  
Modern neuroscience relies on integrating multi-scale, multimodal datasets to uncover the neural principles underlying intelligence. However, analytical challenges posed by highly heterogeneous data and fragmented workflows increasingly constrain discoveries. Here we introduce SeekBrain, an autonomous multi-agent framework designed to accelerate neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis. SeekBrain dynamically constructs a repertoire of analysis recipes extracted from code-paper pairs. By coupling this codified expertise with agentic planning and execution engines, the framework scalably generates hypotheses and analytical pipelines on demand. Systematic evaluation on the expert-annotated BrainArena benchmark demonstrates that SeekBrain substantially outperforms state-of-the-art agent baselines across various analysis tasks. Crucially, when deployed in real-world research, SeekBrain integrated behavioral, neural, and anatomical data to reveal structured, distributed neural representations of larval zebrafish behavior and a shared axis of regional decoding strength across the brain in a mouse decision-making task. These results establish SeekBrain as a scalable and practical tool for accelerating data-driven discoveries in neuroscience.

---

### [2607.29320v1] MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation

- **Authors:** Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29320v1) | [PDF](https://arxiv.org/pdf/2607.29320v1)
- **💡 短评:** GUI agent 多平台自融合+结构化动作蒸馏,移动/Web/桌面统一 agent

**Abstract:**  
Graphical user interface (GUI) agents based on large language models are increasingly deployed across mobile, web, and desktop environments. However, existing agents are typically domain-specific, limiting the deployment and user experience. This motivates the consolidation of specialized models into a single cross-environment policy. Weight merging directly merges domain-specific experts but can corrupt executable actions under expert disagreement, while on-policy distillation (OPD) avoids conflicting teacher supervision yet still treats all response tokens equally during distillation, ignoring that action tokens are the only interface between the environment and the agent. To address this, We introduce MAGA that re-allocates training signal according to the structured action. Based on the correctness of the generated action, it suppresses unnecessary or invalid distillation signals and focuses learning on erroneous actions. Besides, a training-only hint optimizes the supervision signal provided by domain-specific teachers without changing the student input. Across two model scales, MAGA achieves the highest mean success rate, outperforming the strongest baseline by 2.0% at 8B and achieves almost the same average performance with teachers.

---

### [2607.29549v1] AMTFV: Agentic Mathematical Tool-Flow Verification for LLM Self-Correction

- **Authors:** Rui Zou, Yutao Zhu, Mengqi Wei, Ji-Rong Wen
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29549v1) | [PDF](https://arxiv.org/pdf/2607.29549v1)
- **💡 短评:** agentic 数学工具流验证,把「验证答案」从自然语言反思升级为工具调用链

**Abstract:**  
Large language models have demonstrated strong mathematical problem-solving capabilities, yet reliably verifying their candidate answers remains challenging. Existing representative methods mainly revise outputs through natural-language reflection or assist verification by directly generating verification programs; the former may not reliably support exact computation, whereas the latter prematurely couples mathematical modeling with low-level implementation. We propose AMTFV (Agentic Mathematical Tool-Flow Verification). By introducing Mathematical Tool Flow (MTF) as an interrupt--execute--resume interface, AMTFV decouples verification modeling from concrete execution and supports exact computation through a mathematical toolbox. Specifically, the verification agent first constructs a verification workflow, encodes the mathematical objects and computational intent requiring reliable execution in an MTF request, and sends it to the mathematical toolbox agent. The latter parses the request, generates executable calls, and dispatches them to the backend for exact computation. Tool outputs then support candidate-answer adjudication, answer revision, and verification-workflow revision. We evaluate AMTFV on five challenging mathematical reasoning datasets with seven model configurations from DeepSeek, GPT, and Gemini. Experimental results show that AMTFV outperforms the representative baselines evaluated in this study overall; under an individual model configuration, it improves average accuracy over the strongest baseline by up to 8.3 percentage points, with larger gains on samples of medium and high verification complexity.

---

### [2607.29626v1] AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers

- **Authors:** Tianyu Huai, Tingshuo Fan, Xinchi Chen, Yining Zheng, Yuxin Wang, Shuang Chen, Jie Zhou, Xuanjing Huang
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29626v1) | [PDF](https://arxiv.org/pdf/2607.29626v1)
- **💡 短评:** 把 LLM agent 当作顺序超参优化器评测——科学实验 agent 能力的首个专项基准

**Abstract:**  
As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter decisions. To address this gap, we introduce AgentHPOBench, a sequential benchmark comprising 30 executable machine learning tasks across seven research categories. Each task begins with a validated baseline run, after which an agent performs several sequential interventions. At each step, the agent observes the accumulated configurations, metrics, and logs before proposing the next valid configuration. We evaluate 12 widely used agents and conventional HPO baselines under a unified protocol. The results show that current agents exhibit measurable experimental optimization ability across domains, but still face clear limitations in sustained iterative refinement, complex log diagnosis, and consistent progress toward reported reference performance.

---

### [2607.29613v1] WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

- **Authors:** Senyu Fei, Xiaopeng Yu, Siyin Wang, Xianzhong Zhao, Jingjing Gong, Xipeng Qiu
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.RO, cs.CL, cs.CV | **Primary:** cs.RO
- **Links:** [Abstract](https://arxiv.org/abs/2607.29613v1) | [PDF](https://arxiv.org/pdf/2607.29613v1)
- **💡 短评:** VLA 强化学习的 World Critic 模型,机器人操作方向

**Abstract:**  
Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature of robot control. A naive approach to incorporate observation history into the critic incurs exponential complexity with high-dimensional visual space, and still fails because pure scalar-return regression provides insufficient supervision for learning cross-temporal dynamics. We identify the root cause as a state approximation problem: without an explicit world modeling objective, the critic's representation cannot capture the temporal structure needed for accurate value estimation. To address this, we propose the World Critic Model (WCM), built on a lightweight LeJEPA architecture; WCM jointly predicts future latent state and estimates values, such that the critic's representation is explicitly trained to capture temporal dynamics rather than merely regress scalar returns. WCM integrates seamlessly into both on-policy and off-policy training pipelines and is compatible with state-of-the-art VLA backbones including Pi0, Pi0.5, and OpenVLA-OFT. Extensive experiments on 149 tasks across four benchmarks demonstrate that WCM consistently achieves state-of-the-art performance in both in-distribution and out-of-distribution settings, with particularly strong generalization gains. We further validate WCM on seven real-world manipulation tasks using OpenVLA-OFT and Pi0.5 with off-policy RL, confirming stable deployment across diverse settings.

---

### [2607.29678v1] TokTier: Exact Stateful Tokenization for Agentic LLM Serving

- **Authors:** Zhenyu Zhang, Zhichao Cao
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.CL, cs.DC, cs.PF | **Primary:** cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.29678v1) | [PDF](https://arxiv.org/pdf/2607.29678v1)
- **💡 短评:** agentic LLM serving 的 stateful tokenization,直击 coding agent 每次重发长 transcript 的成本问题

**Abstract:**  
LLM serving systems cache prompt KV state, yet most front ends still re-tokenize the full request text on every call. The cost lands on coding agents, which resubmit a long transcript after each small tool result, and reuse is hard because even a short append can change token boundaries near the end of the previous sequence. Across 153,951 calls from two agent ecosystems, the median call appends about 1.4K characters, and only 1.0-3.6% of calls start or rebuild a session with contexts of millions of characters. At a 94.1% fleet prompt-cache hit rate, tokenization reaches up to 64% of time to first token. TokTier is a stateful tokenization service with one contract: emitted token IDs are always identical to full reference tokenization of the request text. For a session continuation, it re-tokenizes a small window around the append and splices only after a per-request stable-boundary check, widening the window or falling back to full tokenization on failure. For a call without a reusable prefix, it decomposes GPT-family regex pre-tokenization into run-local rules and runs exact pre-tokenization and BPE on a GPU. A sampled shadow verifier re-checks live traffic. Across 17 tokenizer families, differential campaigns cover 1.5x10^10 split checks, a 12.4 TB real-text corpus, and 93,000+ replayed agent steps, with zero divergence. Incremental repair takes 0.5-1.1 ms from 100K to 3M characters, up to 437x faster than HF tokenization and 2.1x faster at 1M than the strongest cache-based baseline (Gigatoken) fully prewarmed. GPU full tokenization encodes a 1M-character request in 0.87 ms, up to 491x below HF and 23.4x below the fastest published CPU method. With vLLM, median time to first token drops 16-34% and P99 drops 23% under recorded bursts. Under a 50 ms P99 objective, four repair cores plus one GPU sustain 1,821 requests/s where a 16-core stateless front end saturates at 40.

---

### [2607.29591v1] ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression

- **Authors:** Yuhang Zhan, Lisi Chen, Shuo Shang
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.CL | **Primary:** cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.29591v1) | [PDF](https://arxiv.org/pdf/2607.29591v1)
- **💡 短评:** KV cache 压缩新思路:重建被丢弃 token 的注意力贡献,长上下文推理效率

**Abstract:**  
KV cache compression is essential for efficient long-context inference. Existing eviction methods permanently discard unselected tokens and consequently remove their aggregate contribution to attention. Merging-based alternatives preserve more information but can perturb retained keys and values that should remain exact. We observe that the information omitted by cache eviction can be formulated as residual statistics in both the numerator and denominator of softmax attention. Based on this observation, we propose ResKV, which divides a fixed KV budget into an exact main cache and a compact residual cache that reconstructs the contribution of omitted tokens. ResKV lets main-cache tokens and residual entries participate in the same softmax normalization, so residual entries restore both attention numerator and denominator mass rather than acting as a post-hoc correction. A construction-time validation proxy determines residual allocation for each layer and KV head, while a decode-time dynamic gate adjusts residual contributions for individual queries. Comprehensive evaluations on LongBench and RULER, covering query-aware and query-agnostic settings, multiple backbones, cache budgets, and representative compression baselines, demonstrate broad improvements under the same retained KV budget while preserving the practical efficiency of compressed decoding, including peak memory usage and long-context decode throughput.

---

### [2607.29585v1] Sycophancy Undermines Epistemic Vigilance in Cooperative Vision-Language Tasks

- **Authors:** Rupak Sarkar, Neha Srikanth, Saloni Gupta, Claire Bonial, Philip Resnik, Rachel Rudinger
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.CL | **Primary:** cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.29585v1) | [PDF](https://arxiv.org/pdf/2607.29585v1)
- **💡 短评:** 谄媚(sycophancy)削弱多模态协作中的认知警觉,对齐研究重要发现

**Abstract:**  
To maintain common ground in cooperative conversation, humans iteratively update their beliefs as conversation participants share new information; participants who are epistemically vigilant detect when new information conflicts with prior beliefs and take steps to repair these conflicts. In order for AI systems to serve as reliable partners in complex cooperative tasks, they must similarly weigh incoming information against their own private evidence and shared context and appropriately surface inconsistencies when they arise. To measure the epistemic vigilance of vision-language models in cooperative settings, we present an information-asymmetric, dialog-based "spot-the-difference" task. Two models are privately shown one image each, and must determine through conversation whether the images are identical or, if not, identify the difference. Models routinely fail at this: they frequently overlook key evidence in their private image in favor of agreeing with their conversational partner, even when their agreement is unwarranted. We relate these violations of epistemic vigilance to the broader behavior of sycophancy, which manifests itself in cooperative goal-oriented dialog as over-accommodation and weak evidential grounding. Our results show that model steering to reduce sycophancy with a vector learned from task-agnostic sycophancy examples can reduce epistemic vigilance-related errors, making models more faithful reporters of their evidence, and in turn, more reliable partners in information-asymmetric cooperative tasks.

---

### [2607.29539v1] ARB: A Matched Authorship-Rewriting Benchmark Dataset for AI-Text Detector Evaluation

- **Authors:** Gaetano Perrone, Simon Pietro Romano
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.CL, cs.AI | **Primary:** cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.29539v1) | [PDF](https://arxiv.org/pdf/2607.29539v1)
- **💡 短评:** AI 文本检测基准升级:匹配作者+改写,评测更真实场景

**Abstract:**  
Standard AI-text detection benchmarks compare human-written text against text generated directly by large language models (LLMs). While prior work has shown that rewriting and paraphrasing can degrade detector performance, it remains unclear whether performance measured on this conventional benchmark predicts detector behavior when human-authored content is rewritten by an LLM. To address this gap, we introduce Authorship-Rewriting Benchmark (ARB), built from 1,800 human source texts (600 each from XSum, WritingPrompts, and OpenWebText) and four open-weight generators (Llama-3.2-3B, Qwen2.5-7B, Mistral-7B, Gemma-2-9B). Each source item yields four matched variants: human-written (HUMAN), direct LLM generation (Free-LLM), LLM-rewritten human text (H2L), and same-generator LLM-rewritten LLM text (LLM2L). We evaluated five detectors (FastDetectGPT, Binoculars-falcon-7b, RADAR, BERT-Defense, RoBERTa-Defense) at a strict 1%-false-positive operating point (TPR@1%FPR). FastDetectGPT and Binoculars-falcon-7b detected 91.2% and 93.5\% of direct LLM text, but only 30.8% and 15.1% of human text an LLM had rewritten, a drop of 60-78 percentage points. The same detectors retained 78.3% and 83.0% recall when LLM text was rewritten by the same model, a much smaller decline of 10-13 points. RADAR followed the same pattern (66.8% to 12.2%), while BERT-Defense and RoBERTa-Defense stayed below 3% recall across all regimes. These results show that detector performance measured on the conventional human-vs-LLM benchmark does not transfer to human-authored text revised by an LLM, even though the same detectors remain largely robust to LLM-only rewriting.

---

### [2607.29516v1] From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale

- **Authors:** Chandra Maddila, Mashrur Rashik, Euna Mehnaz Khan, Smriti Jha, James Saindon, Nachi Nagappan, Peter C. Rigby
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.SE, cs.AI | **Primary:** cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2607.29516v1) | [PDF](https://arxiv.org/pdf/2607.29516v1)
- **💡 短评:** AI 生成代码审查从 style 转向意图/漂移/聚光,直击大模型代码量超出人工评审能力的痛点

**Abstract:**  
AI coding agents are generating code at volumes that exceed the capacity of traditional peer review. At the same time, existing AI code review tools over-index on low-value suggestions such as style and best practices while under-indexing on the concerns human reviewers prioritize most: correctness, security, and performance. We present ARCTIC, an AI-powered Code Critique system that reframes code review around three capabilities: intent prediction, which infers why a change was made from conversation logs and metadata; drift detection, which measures divergence between the developer's intent and the agent's output via backtranslation; and code spotlight, which ranks the regions of a diff most warranting human scrutiny. We ground these capabilities in a six-theme taxonomy derived from 18,000 code reviews. Offline evaluation shows that intent prediction achieves 0.86 F1, drift detection reaches near-perfect ordinal agreement with human annotators (QWK = 0.907), and spotlight outperforms the baseline AI reviewer by 2.4x on quality estimation at 5x fewer tokens. In the experimental rollout, the drift scores reduces code misalignment by an additional 5.76 points (p = 0.026), intent prediction receives 90.2% approval, and zero defects have been attributed to self-reviewed diffs since launch.

---

### [2607.29422v1] AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair

- **Authors:** Michael Fu, Qiyue Mei, Patanamon Thongtanunam, Kla Tantithamthavorn
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.SE, cs.AI, cs.CR | **Primary:** cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2607.29422v1) | [PDF](https://arxiv.org/pdf/2607.29422v1)
- **💡 短评:** agentic 漏洞修复,强调程序上下文工程——修复质量的关键在上下文而非模型

**Abstract:**  
Automated vulnerability repair aims to reduce the time and effort required to patch security flaws from a vulnerability triage report. Recent agentic AI approaches have shown promising results in automated program repair. However, vulnerability repair demands richer program context than general bug repair - context that security engineers routinely assemble in practice but that existing agentic approaches do not engineer. We identify three critical gaps: code-structure context capturing cross-file data flows and memory operation patterns, runtime-execution context revealing crash semantics and memory origins, and commit-history context recovering how fragile code patterns were introduced. We present AgenticRepair, an agentic vulnerability repair framework that addresses the gaps through multi-faceted program context engineering. AgenticRepair orchestrates three specialized LLM subagents to engineer the contexts, which are then embedded into the memory of a dedicated repair subagent for context-conditioned patch synthesis. Evaluated on SEC-Bench comprising 300 real-world instances with sanitizer-based patch verification, AgenticRepair achieves a 73% success rate, substantially outperforming the strongest baseline by 29%. Our ablation study confirms that the three context facets are mutually complementary, and that multi-agent scaffolding and base-model capacity each play an essential role. Collectively, these findings establish multi-faceted program context engineering as a promising design direction for agentic vulnerability repair.

---

### [2607.29677v1] ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

- **Authors:** Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li, Simon Suo
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29677v1) | [PDF](https://arxiv.org/pdf/2607.29677v1)
- **💡 短评:** 企业文档抽取 agent 的 schema 遵循评测,补齐 RAG/抽取类 agent 的可信度度量缺口

**Abstract:**  
Enterprise workflows increasingly rely on agents for \emph{schema-guided extraction}: given a document and a user-defined schema, the agent faithfully follows the schema to produce the correct output with source evidence as grounding metadata. We present ExtractBench, a benchmark for schema-guided extraction and, to our knowledge, the first to score value accuracy, record completeness at scale, grounding, and measured cost together. The evaluation system contains 4,869 pages across 370 enterprise documents, 8 business domains, and 67 document types, with clear tags differentiating their challenge scenarios. The scalable schema and ground-truth curation pipeline combines independent-system agreement for real documents, known values for synthetic lists, and human verification for forms. We report order-insensitive value F1 for value accuracy, plus two grounding metrics for source traceability: word- and page-level F1. Commercial VLMs perform well on short documents but often truncate record lists on long ones, while coding agents retain higher accuracy at much higher cost. LlamaExtract Agentic Plus ranks first on all three metrics, with accuracy comparable to coding agents at a fraction of the cost. Dataset and evaluation code are available on \href{https://huggingface.co/datasets/llamaindex/ExtractBench}{HuggingFace} and \href{https://github.com/run-llama/ExtractBench}{GitHub}.

---

### [2607.29405v1] Beyond Component Testing: Validating Agentic AI Systems

- **Authors:** Fabio Orazio Mirto, Luca D'Agati, Giuseppe Tricomi, Stefano Silvestri, Francesco Longo, Antonio Puliafito, Giovanni Merlino
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI, cs.MA, cs.SE | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29405v1) | [PDF](https://arxiv.org/pdf/2607.29405v1)
- **💡 短评:** agentic 系统验证方法论:多步轨迹验证超出组件测试范畴,工程落地必读

**Abstract:**  
Agentic AI systems act through multi-step trajectories that combine planning, tool use, memory, interaction, and adaptation. This behavior stretches validation practice beyond component testing and one-shot input--output evaluation, because acceptable system behavior now depends on how decisions unfold over time and under changing environmental conditions. This survey synthesizes 257 papers spanning agent evaluation, software assurance, cyber-physical systems, runtime monitoring, and regulatory guidance in order to characterize the validation problem for agentic systems. The review is organized around a five-dimension taxonomy covering behavioral, safety, temporal, regulatory, and multi-agent concerns, and uses that taxonomy to map current approaches and expose recurrent coverage gaps. The analysis shows that behavioral evaluation is comparatively mature, while temporal validity, runtime evidence maintenance, regulatory legibility, and open-ended multi-agent systems assurance remain under-developed. Three cross-domain case studies (medical care, industrial operations, smart-mobility systems) provide operational illustrations of how the five taxonomy dimensions recur in safety-critical settings, grounded in the failure patterns documented in the reviewed literature. The paper concludes with a lifecycle-oriented research agenda centered on bounded-autonomy specifications, adversarial trajectory generation, runtime monitoring, and audit-ready evidence structures. The central claim is that trustworthy deployment of agentic AI depends on validating trajectories in context rather than assessing isolated components alone.

---

### [2607.29468v1] Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember

- **Authors:** Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, Haoyu Wu, Minghui Wu, Chenxu Zhao, Ante Wang, Guannan He, Changwei Wang
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29468v1) | [PDF](https://arxiv.org/pdf/2607.29468v1)
- **💡 短评:** 自博弈+技能记忆进化:搜索 agent 自己出题、解题、记住经验,与 sora 的自举体系高度呼应

**Abstract:**  
Self-play agents can generate training problems without questions from target benchmarks, but their curricula lack persistent state: failures affect gradients yet do not explicitly shape future practice. External skill memories preserve procedural experience but are typically learned from fixed task distributions. We introduce \textbf{SESA} (Self-Evolving Skill-Augmented Agent), which makes procedural memory an evolving state of tool-augmented search self-play. A challenger poses problems, while a separately parameterized solver alone retrieves skills. Informative failures are distilled into reusable skills and written back to memory. The updated memory changes solver behavior and success, which changes the challenger's reward and the distribution of future problems; the resulting frontier produces new failures that rewrite memory. This bidirectional loop makes task generation and skill memory co-evolve. Because retrieved skills shape on-policy training trajectories, their benefits can enter the model parameters as well as remain in the external bank, enabling memory-free deployment and optional inference-time retrieval. Across seven open-domain and multi-hop question-answering benchmarks, SESA improves average accuracy over SSP by 1.2--3.2 points across multiple backbones and surpasses the skill-augmented SkillRL baseline by 0.9 points under a unified evaluation protocol. On Qwen3 models, SESA-Off retains 1.8--2.2 points of improvement over SSP, while the final skill bank adds a further 0.5--1.0 points. These results show that evolving skill memory is not merely an inference-time plug-in: it changes policy learning and the future training distribution while retaining value as optional external memory. Our code is available at https://github.com/Zenghuang-Fu/SESA-Self-Evolving-Search-Agents.

---

### [2607.29440v1] Beyond Retrieval: Analytic Memory for Multimodal Agents

- **Authors:** Zhoujin Tian, Yao Tian, Hao Zhang, Cheng Chen, Yakun Li, Lei Zhang, Xiaofang Zhou
- **Published:** 2026-07-31 (updated 2026-07-31)
- **Categories:** cs.AI | **Primary:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.29440v1) | [PDF](https://arxiv.org/pdf/2607.29440v1)
- **💡 短评:** 多模态 agent 记忆从「检索」升级为「分析计算」,第二大脑系统可直接借鉴

**Abstract:**  
Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions. Existing systems largely emphasize \emph{retrieval memory}, organizing interaction histories through summaries and indexes to return query-relevant information at multiple granularities, from high-level abstractions to underlying records. In this paper, we formulate \emph{analytic memory} as a complementary abstraction that organizes recurring multimodal observations into queryable structures supporting filtering, aggregation, ranking, and temporal comparison. We present AdaMM, a framework that jointly supports retrieval and analytic memory. Rather than relying on application-defined schemas, AdaMM extracts provenance-linked attribute-value observations from dialogue, images, and contextual metadata, discovers recurring field structures, and materializes them for analytical access. At inference time, a memory-aware planner decomposes queries into retrieval and analytic operations and routes each operation to the appropriate tools. Experiments on two long-term multimodal memory benchmarks, MemEye and MemGallery, show that AdaMM improves performance by up to 11.3\% and 7.3\%, respectively.

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| Total Papers | 15 |
| cs.AI | 7 |
| cs.CL | 4 |
| cs.SE | 2 |
| cs.MA | 1 |
| cs.RO | 1 |

## 🎯 Key Themes

本周论文按主题分组:

### 🤖 Agent 评测基准
- [2607.29677v1] ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction
- [2607.29626v1] AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers
- [2607.29405v1] Beyond Component Testing: Validating Agentic AI Systems

### 🧠 Agent 记忆与进化
- [2607.29440v1] Beyond Retrieval: Analytic Memory for Multimodal Agents
- [2607.29468v1] Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember
- [2607.29347v1] SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery

### 🛠️ Agent 工程应用
- [2607.29549v1] AMTFV: Agentic Mathematical Tool-Flow Verification for LLM Self-Correction
- [2607.29516v1] From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale
- [2607.29422v1] AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair
- [2607.29320v1] MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation

### ⚡ LLM 推理效率
- [2607.29678v1] TokTier: Exact Stateful Tokenization for Agentic LLM Serving
- [2607.29591v1] ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression

### 🔬 LLM 行为与评测
- [2607.29585v1] Sycophancy Undermines Epistemic Vigilance in Cooperative Vision-Language Tasks
- [2607.29539v1] ARB: A Matched Authorship-Rewriting Benchmark Dataset for AI-Text Detector Evaluation
- [2607.29613v1] WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

---

## ✅ 论文验证状态（搜索引擎交叉验证）

| 论文 | 验证状态 | 备注 |
|-----|---------|------|
| **SeekBrain** | ✅ 高价值 | 科学发现多 agent 系统,Science Agents 方向共识 |
| **Beyond Retrieval (Analytic Memory)** | ✅ 高价值 | 记忆系统从检索到分析,与第二大脑直接相关 |
| **Self-Play + Skill Evolution** | ✅ 高价值 | 自进化 agent,与自举体系理念契合 |
| **MAGA (GUI Agent)** | ✅ 已验证 | GUI agent 跨平台融合是行业热点 |
| **AgentHPOBench** | ✅ 已验证 | LLM 科学实验能力评测新基准 |
| **TokTier** | ✅ 高价值 | Agentic serving 成本优化,coding agent 实际痛点 |
| **Sycophancy** | 🔍 理论前沿 | 谄媚与认知警觉,对齐方向需跟踪 |
| **ARB** | 🔍 研究方向 | AI 文本检测基准升级 |
| **ResKV** | 🔍 推理效率 | KV cache 压缩,工程优化 |
| **WCM** | 🔍 机器人 | VLA world critic,偏硬件方向 |

---

## 🎯 阅读优先级（基于验证 + 第二 Brain 相关性）

**立即行动**（本周内）：
1. **Beyond Retrieval: Analytic Memory**（agent 记忆分析计算,直接借鉴到记忆系统）
2. **Self-Play Meets Skill Evolution**（自进化循环,与 learn→research→apply 呼应）

**中期跟踪**（1-2 周）：
3. **TokTier**（coding agent 服务成本优化）
4. **AgentHPOBench / Beyond Component Testing**（agent 评测与验证方法论）

**长期研究**（1 个月+）：
5. **SeekBrain / MAGA / AgenticRepair**

---

*生成时间：2026-08-04 | 数据源：arXiv API | 状态：reading → adopted*

*Generated automatically via arXiv API cron job. Last updated: 2026-08-04*
