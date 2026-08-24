# 数模 Agent 开源生态实证评估（2026-08-23）

> 来源：抖音「雾离欢」作品（2026-07-07 发布，播放 7.1K）→ 数模 agent Beacon 开源
> 实证：GitHub 搜索确认仓库真实存在 + star 数 + README 全文核对 + 创建时间与抖音发布吻合

## 一、抖音主角：123-qw-as/Beacon（34★）

| 项 | 值 |
|:---|:---|
| 仓库 | https://github.com/123-qw-as/Beacon |
| Star/Fork | 34 / 1（小众但完整） |
| 创建 | 2026-07-06（抖音 07-07 发布，吻合 ✓） |
| 协议 | MIT |
| 作者 | 123-qw-as（vibe coding 一个月） |

**架构：LangGraph 10 节点端到端流水线**
```
Analyst → Modeler → Model Critic(重试) → Coder → Sensitivity
→ Figure Pipeline → Writer → Paper Critic(重试) → Evaluation
→ Human Review → LaTeX/PDF
```

**能力：**
- ✅ 问题→论文全自动：分析→建模→批评→编码→灵敏度→图表→写作→评审→评分
- ✅ **XeLaTeX 直接编译 PDF**，无 xelatex 时降级 Markdown
- ✅ HITL 人机协作（关键节点暂停人工审批）+ checkpoint 崩溃恢复（resume/recover）
- ✅ RAG 可选（注入经典模型模式 + 获奖论文片段）
- ✅ LiteLLM 支持 100+ 提供商（openai/ollama/deepseek 等）
- ✅ 模板切换：默认英文 / `--template gmcm`（国赛 gmcmthesis 中文封面队号）
- ✅ 统一 complete() 容错：JSON 修复、thinking 标签剥离、LaTeX 转义修复、重试

## 二、生态对比（按 star 排序）

| 项目 | Star | 形式 | 输出 | 特点 |
|:---|:---|:---|:---|:---|
| **jihe520/MathModelAgent** | **3674** | Agent+SKILL+桌面版 | **Typst**（17套模板） | 多 agent 多 LLM、9步验收、HIL、四层容错、Web Search+RAG、桌面版开箱即用 |
| **123-qw-as/Beacon** | 34 | LangGraph 流水线 | **LaTeX PDF** | 10节点全自动、checkpoint、评分评估 |
| wangling-miao/mathmodel-latex-skill | 8 | Codex/Claude skill | LaTeX | 身份关键词检查、PDF preflight |
| Yoki-cmd/math-modeling-single | 7 | Claude Code skill | LaTeX | 四阶段流程、MATLAB MCP |
| ll2010650-coder/mathmodel-pro | 3 | Skill 工作流 | **Word+MathType** | 六阶段手册、Word 生产线 |

## 三、定位判断（对标/互补/替代）

**对 sora 数模代写业务：这些是「提效工具 + 对标物」，不是替代品。**

- 客户付钱买的是**确定性交付**（时限内拿到可提交论文），agent 输出仍需人工润色/去AI味/质检
- 但 agent 流水线可以**大幅降低初稿成本**：
  - 用 agent 生成初稿（建模+代码+图表+LaTeX）→ 人工做去AI味+质检+交付
  - 特别适合「LaTeX 交付」高端单：agent 出排版底稿，省去手工排版
- MathModelAgent 3674★ 是生态标杆——17 套 Typst 模板、9 步验收、桌面版免配置，**值得实测当生产工具**

## 四、落地建议

1. **试用 MathModelAgent 桌面版**（github.com/jihe520/MathModelAgent releases）——免费、开箱即用，填一个 API key 就能跑
2. **LaTeX 高端单**：Beacon 或 mathmodel-latex-skill 做排版底稿 → 人工去AI味 → 交付
3. **自家流水线对标**：学 Beacon 的「Human Review 检查点 + checkpoint 恢复」设计，融入 paper-service 生产链路
4. ⚠️ 注意：agent 产出论文需过「去AI味」关（已有 ai-content-humanization / de-AI-writing 技能），不能直接交付

## 五、网络备注

- GitHub API/codeload 在本机代理下不通（HTTP 000），web_extract 走 Hermes 通道可读页面/raw
- 下载 zip 需代理正常后：codeload.github.com/<owner>/<repo>/zip/refs/heads/main
