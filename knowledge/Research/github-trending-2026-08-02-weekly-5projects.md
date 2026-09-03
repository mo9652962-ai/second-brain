---
tags: [github, trending, weekly, research, ai-agent, code-review, cad, skills]
aliases: [github-trending-weekly-2026-08-02]
date: 2026-08-02
source: https://github.com/trending?since=weekly
---

# GitHub 本周 Trending 精选研究（2026-08-02）

> 数据源：GitHub Trending Weekly（2026-07-27 ~ 08-02 快照）+ 项目 README 深度提取
> 研究方法：learn → research → apply（github-trending-digest 技能 Phase 1-3）
> 注：今日 13:09 自动脚本已产出「新建仓库口径」报告（Kimi-K3/qm/waste/rescript，见 [[github-trending-2026-08-02-study]]）；本文为 **weekly 口径**（本周 star 增速），两口径互补。

## 📋 候选（18 个）→ 精选 5 个

| # | 项目 | ⭐ | +本周 | 领域 | 筛选 |
|:-:|------|:--:|:----:|:----:|:---:|
| 1 | diegosouzapw/OmniRoute | 36.7K | +7,701 | AI 网关 | ⚪ 已入库（w31-v2 watch / 08-01 不装，ToS 灰色地带）→ 仅跟踪 |
| 2 | alibaba/open-code-review | 17.4K | +4,746 | 代码评审 | ✅ 入选 |
| 3 | virgiliojr94/book-to-skill | 14.5K | +4,603 | Skill 生成 | ✅ 入选 |
| 4 | different-ai/openwork | 20.0K | +2,213 | 桌面 Agent 协作 | ✅ 入选 |
| 5 | earthtojake/text-to-cad | 12.3K | +1,901 | CAD Agent Skills | ✅ 入选（更新 CAD-Design.md 旧数据） |
| 6 | ayghri/i-have-adhd | 15.0K | +5,133 | 输出风格 Skill | ✅ 入选 |
| 7 | block/buzz | 20.1K | +10,558 | 蜂群通信平台 | ❌ 描述模糊，与工作流无关 |
| 8 | permissionlesstech/bitchat | 33.9K | +6,761 | 蓝牙 mesh 聊天 | ❌ 非 AI/Dev 核心 |
| 9 | citrolabs/ego-lite | 7.3K | +4,741 | Agent 浏览器 | ⚪ 观望（与 browser-automation 技能重叠） |
| 10 | 1jehuang/jcode | 14.9K | +3,351 | Rust agent harness | ❌ 已 abandoned（SAC 封杀） |
| 11 | moeru-ai/airi | 46.3K | +3,125 | 虚拟伴侣 | ❌ 娱乐向排除 |
| 12 | microsoft/VibeVoice | 51.8K | +1,222 | 语音 AI | ⚪ 微软大项目，离实操远 |
| 13 | shiyu-coder/Kronos | 35.3K | +1,939 | 金融大模型 | ⚪ 模型训练项目，8GB 显存无法本地跑 |
| 14-18 | 其余（GeoLibre/t3code/AI-For-Beginners/Instatic/pascalorg-editor） | — | — | — | ❌ 非核心或老项目 |

---

## 1️⃣ alibaba/open-code-review — 确定性工程 × Agent 混合代码评审

- **URL**: https://github.com/alibaba/open-code-review
- **定位**: 阿里巴巴内部官方 AI 代码评审助手开源版（两年服务数万开发者、发现数百万缺陷），Go 写的 CLI，17.4K⭐ / 本周 +4.7K / Apache-2.0
- **核心思路**: 纯语言驱动的评审 Skill 有三大硬伤——大变更集覆盖不全（agent 挑软柿子捏）、行号漂移、质量不稳定。根因是「评审过程缺硬约束」。解法是**混合架构**：确定性工程负责「必须不出错」的步骤，LLM 只负责动态决策。

### 🏗️ 技术架构
```
Git diff / 文件扫描
      ↓
确定性工程层（模板引擎，不用 LLM 保证正确）
  ├─ 精确文件选择（哪些文件要审、哪些过滤）
  ├─ 智能文件捆绑（message_en/zh.properties 同捆；每捆一个子 agent 独立上下文 → 天然并发）
  ├─ 细粒度规则匹配（按文件特征匹配 NPE/线程安全/XSS/SQL 注入规则）
  └─ 外部定位+反思模块（独立于 LLM 校准行号与内容）
      ↓
Agent 层（LLM 只管动态决策）
  ├─ 场景调优 prompt（评审专用模板，省 token）
  └─ 场景调优工具集（从生产工具调用轨迹蒸馏，比通用 agent 工具链稳定）
      ↓
结构化行级评审意见
```

### 💎 可借鉴点（⭐ 最重要）
- **「确定性兜底」分层原则**：凡是「必须不能错」的步骤用工程逻辑而非 LLM 保证——这正是我们 skill 体系该学的：规则匹配、文件选择这类机械步骤别指望模型自觉，写成硬代码
- **Benchmark 方法论**：50 个流行 repo / 200 个真实 PR / 10 语言 / 80+ 资深工程师标注 1,505 条 ground truth —— 用真实缺陷集做 F1/Precision/Recall 评测，而非拍脑袋自评。**我们的 ai-code-review 技能可以借鉴这套评测口径**
- **显式 trade-off**：Recall 故意低、Precision 优先（少误报 > 全抓到），因为误报消耗人工 triage 成本——「有意牺牲」比「全面平庸」好
- **Delegation Mode**：文件选择/规则解析由 OCR 做，评审由 coding agent 用自己的 LLM 跑——无需配 API key，降低了接入门槛
- **token 效率**：同模型比 Claude Code 少 ~1/9 token 且 F1 更高 —— 专用工具集 + 场景 prompt 的收益量化

### 📊 评估
| 维度 | 评分 |
|------|:---:|
| 技术含金量 | ★★★★★ |
| 对 sora 价值 | ★★★★★（ai-code-review 技能 + 工程接单交付质量） |
| 可迁移性 | ★★★★★（混合架构可直接用于 Hermes 技能设计） |
| 安装需求 | ⏳ backlog：`npm install -g @alibaba-group/open-code-review`，先与现有 ai-code-review 技能对比试用 |

---

## 2️⃣ virgiliojr94/book-to-skill — 技术书 → 结构化 Agent Skill

- **URL**: https://github.com/virgiliojr94/book-to-skill
- **定位**: 把任何技术书/文档夹/资料集变成统一 agent skill，随用随加载。14.5K⭐ / 本周 +4.6K / MIT / Python
- **核心思路**: 买书读一遍三个月后全忘、搜 PDF 只得页码、问 agent 就幻觉——痛点本质是「书的内容没有进入工作流」。解法：**把书蒸馏成结构化 skill**（不是摘要，是结构），agent 按需加载章节回答，不再幻觉。

### 📦 生成物结构（Agent Skills 开放标准）
| 文件 | 用途 | 大小 |
|:----|:-----|:----:|
| `SKILL.md` | 核心心智模型 + 章节索引 | ~4,000 tokens |
| `chapters/ch01-*.md` | 每章一文件，**按需加载** | ~1,000 tokens each |
| `glossary.md` | 术语表（字母序+章节引用） | ~1,500 tokens |
| `patterns.md` | 技巧/算法/设计模式 | ~2,000 tokens |
| `cheatsheet.md` | 决策表 + 速查规则 | ~1,000 tokens |

### 💎 可借鉴点（⭐ 最重要）
- **按需加载的 skill 结构**：SKILL.md 只放索引和心智模型，章节文件不进上下文直到被问到——这正是 Hermes skill 体系的「skill 预算」管理思想，我们的大技能（如 cad-design-master）也该拆成「主文件 + references/ 按需加载」
- **5 条设计原则可直接用**：① Density over completeness（1,000 token 总结 > 10,000 token 摘录）② Practitioner voice（"用 X 当 Y" 而非 "书中讲了 X"）③ Front-loaded SKILL.md（compaction 只留前 ~5,000 token，最重要的放最前）④ On-demand chapters ⑤ Never raw text（永远综合而非照抄）
- **成本量化**：244 页书 ~$0.88 / 501 页 Pro Git ~$1.23 —— 一本技术书约 $1 变成永久 skill，**这对 sora 的「知识吸收」工作流是直接工具**：把长期要查的规范书（如 PCB 设计手册、数学题库方法论）转成 skill
- **版权安全设计**：本地处理、不发布书内容、输出是合成笔记——可放心用于自有资料

### 📊 评估
| 维度 | 评分 |
|------|:---:|
| 技术含金量 | ★★★★（思路创新，实现常规） |
| 对 sora 价值 | ★★★★★（知识库 Second Brain 直接受益） |
| 可迁移性 | ★★★★★（skill 结构设计准则可注入现有技能） |
| 安装需求 | ✅ trial：Python 工具，先拿一本自有技术书实测 |

---

## 3️⃣ different-ai/openwork — opencode 驱动的开源 Claude Cowork 替代

- **URL**: https://github.com/different-ai/openwork
- **定位**: 免费开源的桌面 app + MCP 服务，用于跨工具/团队/机器共享 AI 工作流。20.0K⭐ / 本周 +2.2K / MIT（`/ee` 目录 Fair Source）
- **核心思路**: 每个 agent（Codex/Claude Code/Cursor/OpenCode）都有一堆自己的 skills、MCP、连接服务，互不相通——重复建设。解法：**一个 OpenWork MCP 接入任意 agent，复用同一套 skills/MCP/连接服务**，桌面 app 是可选增强（团队管理用 OpenWork Den 控制平面）。

### 🏗️ 架构
```
你的 agent（Codex / Claude Code / Cursor / OpenCode…）
      │  加一个 MCP
      ↓
OpenWork MCP（https://api.openworklabs.com/mcp/agent）
      │
      ├─ search_capabilities / execute_capability 工具
      ├─ 共享 skills / MCPs / 连接服务（一次创建，处处复用）
      └─ OpenWork Den（团队控制平面：模型供给、访问控制、发布 skills 市场）
```

### 💎 可借鉴点（⭐ 最重要）
- **「agent 工具去重」范式**：工具/技能应该与 agent 解耦、通过 MCP 共享——我们 Hermes 的 skills 目录已在做类似事，openwork 验证了「一个标准接口 + 多处消费」的方向
- **opencode 血缘**：README 明确 "powered by opencode"——说明 opencode 生态是开源 agent 工具的事实底层，sora 坚持 opencode-go 路线正确
- **团队控制平面**：OpenWork Den 做模型供给/访问控制/skills 市场——若未来带团队接单（闲鱼→工作室），这套「中央管理 + 成员消费」模式可参考
- **许可提醒**：`/ee` 目录是 Fair Source 非 MIT——社区项目常有的「核心开源 + 企业功能半闭源」策略，评估时看清边界

### 📊 评估
| 维度 | 评分 |
|------|:---:|
| 技术含金量 | ★★★★ |
| 对 sora 价值 | ★★★★（工具链方向验证） |
| 可迁移性 | ★★★★（MCP 共享范式） |
| 安装需求 | ⚪ 观望：单机 Hermes 场景收益有限，团队协作时再上 |

---

## 4️⃣ earthtojake/text-to-cad — CAD/CAE/CAM Agent Skills 库（更新）

- **URL**: https://github.com/earthtojake/text-to-cad
- **定位**: CAD、机器人与硬件设计 agent 的 skills 库，12.3K⭐（07-28 记录 7.6K，**本周 +1.9K**）/ MIT
- **与已有资产的关系**: sora 已装 `text2cad-cad` skill（同源）、`cad-design-master` 技能；`knowledge/Hardware/CAD-Design.md` 有 7.6K 旧数据（本次更新）

### 🧰 Skills 清单（11 个）
| Skill | 功能 |
|:------|:-----|
| CAD | 自然语言/图片 → STEP 模型（可导出 STL/3MF/GLB） |
| CAD Viewer | 本地浏览器预览 CAD/G-code/机器人文件 |
| step.parts | 检索现成 STEP 零件（螺丝/轴承/电机/连接器） |
| DXF | 生成 2D DXF 图纸（型材/模板/垫片/切割布局） |
| URDF / SRDF / SDF | 机器人结构、MoveIt 规划组、仿真模型 |
| SendCutSend | 上传前检查 DXF/STEP |
| G-code / Bambu Labs | 切片验证、FDM 打印 |
| Implicit CAD | GLSL 隐式建模（实验性） |

### 💎 可借鉴点（⭐ 最重要）
- **基准测试先行**：10 个 benchmark（矩形校准块→行星齿轮组），从易到难定义「什么算 CAD 生成成功」——**我们的 PCB/CAD 接单质量门可以照抄这个思路**：固定 prompt 集 + 可复现输出对比
- **STEP 为主输出**：主输出 STEP（中性格式）+ 多格式导出——「用一个标准格式做核心，派生格式靠转换」是工程自动化最佳实践
- **轻量克隆设计**：GIF 等重资产走 Git LFS 且默认不拉取——仓库工程化细节（我们脚本仓库可参考）
- **Skills CLI 分发**：`npx skills install earthtojake/text-to-cad` —— skills 成为一种可安装分发的包，与我们的 skill 体系生态一致

### 📊 评估
| 维度 | 评分 |
|------|:---:|
| 技术含金量 | ★★★★（SKILL.md 质量高） |
| 对 sora 价值 | ★★★★★（PCB/CAD 蓝海直接命中） |
| 可迁移性 | ★★★★★（benchmark + 多格式导出思路） |
| 安装需求 | ✅ 已装 text2cad-cad（同源），本周涨幅说明方向正确，继续跟进 |

---

## 5️⃣ ayghri/i-have-adhd — 让 coding agent 不埋答案的输出 Skill

- **URL**: https://github.com/ayghri/i-have-adhd
- **定位**: 一个改变 agent 输出风格的 skill：Action first、Steps numbered、No "Hope this helps!"。15.0K⭐ / 本周 +5.1K / MIT
- **核心思路**: 用 **10 条规则** 约束 agent 的回复格式，从「解释型助手」变成「执行型助手」。源于成人 ADHD 工具箱，但适用所有人——解决「答案埋在铺垫里」的通病。

### 📜 10 条规则
1. 以下一步行动开头
2. 多步任务编号
3. 以一条具体下一步结尾
4. 压制跑题
5. 每轮重申状态
6. 具体时间估计（分钟，不说 "一会儿"）
7. 让成果可见
8. 就事论事报错
9. 列表最多 5 项
10. 无开场白、无复述、无收尾客套

### 💎 可借鉴点（⭐ 最重要）
- **规则 9「列表上限 5」**：和我们的渐进式披露不谋而合，但更激进——「最多 5 项」是硬约束，防止信息倾倒
- **规则 1+3「行动开头、行动结尾」**：与 sora 的「结论置顶 + 可操作下一步」偏好完全一致，说明这是社区共识而非个人口味
- **多 agent 兼容**：Claude Code/Codex/Gemini/Cursor 四端都做了插件——一个 skill 到处安装，验证了「输出风格 = 可分发技能」的形态
- **可 fork 调优**：官方鼓励 fork 改 SKILL.md 换自己的规则——我们可以考虑把「结论置顶+结构化表格」写成 Hermes 自己的风格 skill

### 📊 评估
| 维度 | 评分 |
|------|:---:|
| 技术含金量 | ★★★（思路简单，工程完整） |
| 对 sora 价值 | ★★★★（输出风格方法论） |
| 可迁移性 | ★★★★★（10 条规则可直接注入 SOUL.md/技能） |
| 安装需求 | ✅ 思路已内化（sora 偏好已含结论置顶），无需安装 |

---

## 🔭 本周趋势观察（weekly 口径）

1. **Agent 工具链进入「资产复用」阶段**：openwork（跨 agent 共享工具）、book-to-skill（书→skill）、text-to-cad（skill 库分发）——本周多个 10K+ 项目都在做「让 skill 成为一等公民、可安装可共享」
2. **确定性工程回潮**：open-code-review 的混合架构是对「纯 prompt agent 不可靠」的正面回应——LLM 管决策、代码管约束
3. **输出风格被产品化**：i-have-adhd 证明「agent 怎么说」本身可以是一个 15K⭐ 的爆款 skill——沟通规范的价值被低估了
4. **CAD/硬件自动化持续升温**：text-to-cad 两周从 7.6K 涨到 12.3K，验证 sora 的「蓝海工程自动化」定位

## 关联
- 今日新建仓库口径报告：[[github-trending-2026-08-02-study]]
- 上周 weekly 报告：[[github-weekly-2026-07-31-5projects]]
- 知识地图：[[knowledge-map]] · 研究 MOC：[[MOC-Research]]
