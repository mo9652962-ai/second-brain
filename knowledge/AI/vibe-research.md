# Vibe-Research：AI 辅助科研全流程

来源：小黑盒 + GitHub modelscope/Awesome-Vibe-Research
更新：2026-07-25

## 核心思路

AI 深度融入科研全流程，按"科研怎么干"而不是"工具叫什么"组织。
9 个阶段：方向扫描 → 文献研究 → 方法设计 → 实验执行 → 可视化 → 写作 → 投稿 → 复现发布 → 传播

## 各阶段推荐工具

### 阶段一：Idea（灵感与选题）
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **STORM** | 29k | 多视角提问+检索，自动生成研究综述 |
| **paperseek** | 60 | 自然语言检索文献，自动迭代扩展 |
| **SciAgentsDiscovery** | 616 | 知识图谱+多智能体，跨学科生成假说 |
| **AutoDiscovery** | 186 | 从数据中发现可验证假说 |

### 阶段二：实验设计
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **Curie** | 363 | 自动化科学实验 agent，从假说澄清到实验方案 |

### 阶段三：实验执行
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **RD-Agent**（微软） | 13.6k | AI 驱动研发流程自动化 |
| **EurekAgent**（清华） | 55 | Docker 隔离实验环境，自动迭代 |
| **autoresearch**（Karpathy） | 87.8k | 单 GPU 自动跑 ML 实验 |
| **PaperBanana** | 6.6k | 多 agent 学术插图生成 |

### 阶段四：论文撰写
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **academic-research-skills** | 33.1k | Claude Code skill 套件，写作/润色/投稿 |
| **nature-skills** | 21.6k | Nature 级学术表达和绘图 skill |
| **RefChecker** | 407 | 检查引用真实性，防 AI 编造 |

### 阶段五：Review Loop
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **AI-Scientist**（Sakana AI） | 14k | 端到端自动科研+模拟审稿 |
| **AI-Scientist-v2** | 6.6k | 升级版，agentic tree search |
| **AutoResearchClaw** | 13.5k | 多阶段自进化研究流水线 |
| **EvoScientist** | 3.7k | 多 agent，持久记忆+技能演化 |
> 关联: [[researchpilot-skills]] · [[ai-research-collaboration]] · [[academic-service-research]] · academic-paper-writing（skill）
## 关键原则

1. **组合拳**：别指望一个工具从选题干到发表，分阶段配不同工具
2. **AI 主导 ≠ 你甩手**：关键判断（idea值不值、结果说明什么、rebuttal怎么回）还是你来
3. **从一个阶段切入**：先挑最头疼的那一步试一个工具
4. **注意学术规范**：很多会议要求披露 AI 使用情况
