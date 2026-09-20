---
created: 2026-09-20
updated: 2026-09-20
type: weekly-review
domain: knowledge-graph
tags: [graphify, research, weekly]
---

# Graphify 知识图谱周更 2026-09-20

> 覆盖 2026-09-06 → 2026-09-20（2 周积累；9-13 一次运行中断未完成，本次合并处理）

## ⚠️ 重要修复：图谱已冻结 6 周（2026-08-09 → 2026-09-20）

**发现根因**：`build_merge()` 返回 `nx.Graph` 但**不写 graph.json**（graphifyy 0.9.25 源码验证：函数体内无 write_text/to_json）。旧版 rebuild_graph.py 在 build_merge 后读回 graph.json —— 读到的是**上一次的旧图谱**，过滤后重建的仍是旧图。结果：09-06 那次运行（3 周积累 773 文件）实际**从未把新内容合入图谱**，图谱停留在 2026-08-09 的状态。

- 验证：本次运行前 graph.json 最新 dated 节点 = 2026-08-09；本周新文件（arxiv-2026-09-18、2026-09-19、2026-09-20 等）节点数全部为 0
- 修复：rebuild_graph.py 改为直接序列化 build_merge **返回的 G**（nodes/edges/hyperedges），再过滤 `.obsidian`、重建、写盘
- 已把修复版写回 skill（`graphify-vault-maintenance/scripts/rebuild_graph.py`），后续周更直接用
- 教训：verify_graph_output.py 只查「graph.json 可解析、数量达标」，查不出「图谱没更新」——周更后应抽查**本周日期文件是否出现在 graph.json**（`grep 2026-09-20 graph.json | wc -l`）

## 本次更新概况

| 指标 | 数值 |
|:---|:---|
| 新增文件 | 507（code 25 / document 450 / paper 11 / image 21） |
| 删除文件 | 108 |
| 语料总量 | 1213 文件 |
| 语义提取分块 | 22 chunks（含 2 图片块） |
| 提取节点 | 1113（语义）+ 156（AST）= 1238 合并 |
| `.obsidian` 过滤 | 0（旧图已干净；本次 code 新增无插件 JS） |
| 图谱规模 | **2598 节点 / 5193 边 / 229 社区**（上一版 1925/3487/140 → 本次真实增量 ~673 节点） |
| Token 消耗 | 35.2M input / 0.75M output（历史累计 173.6M / 3.6M，4 次运行） |
| 异常 | 4 个 phantom 路径（detect 把 memory/2026/09/*.md 的父目录丢了）→ 子代理按真实文件读取、source_file 已修复 |

## 知识域关联（本周新增重点）

### 图谱 Hub（God Nodes）
| 节点 | 度数 | 说明 |
|:---|:---|:---|
| Home 第二大脑入口 | 413 | 全库枢纽，跨 20+ 社区 |
| 知识地图 | 299 | 第二枢纽 |
| Knowledge Map 知识地图 | 107 | |
| Research 研究域 MOC | 94 | 研究域锚点 |
| Cron 自动化体系 | 48 | 自动化体系 |
| AI Agent / LLM / AI Image Gen / Agent Memory / Agent Safety | 33-44 | AI 域核心 |

### 本周新增知识域（2026-09-11 → 09-20）
- **2026-09-11 十领域自我强化研究**（Research/2026-09-11-self-study/）：AI 安全、CAD、内容工业、边缘 AI、变现、动机 AI、PCB 自动化、自举、Web2026 —— 10 个研究文件挂到 Research 域
- **PPT 高级动画 SOP**（09-20）：扇叶开场 Morph + 镂空结尾页，配图（fan_blade_slide_*.png）与 SOP 互相引用，形成「图片 ↔ 教程」双向边
- **AI 视频 Agent 全流程**（09-20）：四 Skill 协同架构
- **arXiv agent-llm 日报**（09-14 → 09-19）：6 篇新日报挂 arXiv Research 域
- **知识卡片**（09-08 → 09-19）：heihe-top5、eval-reactivity、desert-ant、ai-commercial-ad、rubygems-ai-attack、ai-query-plan-optimization、overclaimbench、zcode-silent-upload —— 8 张卡构成卡片子域
- **memory 每日回顾/反思/自举**：09-14 → 09-19 的 daily-review / reflection / self-improvement 系列挂 Learnings 与每日回顾域

### Surprising Connections（跨域桥）
- `arXiv Weekly Roundup` ↔ `AI Blogger Strategy`（研究 → 变现策略）
- `MEMORY.md 长期记忆` ↔ `WeKnora 腾讯知识平台`（本地记忆 → 外部平台）
- `Fan Blade Slide 图片` ↔ `PPT 扇叶开场 SOP`（图片与教程自动配对）

### 高介数桥节点
- `Home 第二大脑入口`（betweenness 0.354）—— 连接所有域
- `知识地图`（betweenness 0.127）—— 第二桥
- `arXiv 核心贡献精选` —— Agent 协作与 arXiv 域的桥

## 验证
- verify_graph_output.py：13/14 通过（唯一 FAIL 是 git 提交信息检查，本次提交后通过）
- 抽查确认：arxiv-2026-09-18 / 2026-09-19 / 2026-09-20 / github-trending-w38 / AI视频Agent全流程 等本周文件节点已在 graph.json

## 产物
- `graphify-out/graph.html`（2.6MB，交互可视化）
- `graphify-out/graph.json`（2598 节点 / 5193 边）
- `graphify-out/GRAPH_REPORT.md`（74KB 审计报告）
