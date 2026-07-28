---
tags: [cross-domain, index]
domain: cross-reference
created: 2026-07-21
status: adopted
---

# 🔀 交叉领域索引 — 知识串联地图

> 所有知识不是孤立的，它们的连接点才是价值所在。

---

## 🗺️ 知识领域关系图

```
                      ┌──────────────────┐
                      │   🤖 AI-Agent    │
                      │   (核心引擎)      │
                      └────┬──┬──┬──┬───┘
                    ┌──────┘  │  │  └──────────────┐
                    ▼         │  │                 ▼
           ┌────────────┐    │  │    ┌──────────────────┐
           │ AI-Workflow │◄──┘  └──►│  LLM-Providers   │
           │ (编排方法)   │         │  (模型架构)       │
           └──┬──┬──┬───┘         └──────────────────┘
              │  │  │
    ┌─────────┘  │  └──────────┐
    ▼            ▼             ▼
┌──────────┐ ┌────────┐ ┌──────────┐
│ Academic │ │ PPT    │ │ Vibe-    │
│ (学术)   │ │ (设计) │ │ Coding   │
└──┬───────┘ └──┬─────┘ └──┬───────┘
   │            │          │
   │     ┌──────┘          │
   ▼     ▼                 ▼
┌──────────────┐   ┌──────────────┐
│ Programming  │   │ CAD-Design   │
│ (编程基础)   │   │ (CAD建模)    │
└──────┬───────┘   └──────┬───────┘
       │                  │
       ▼                  ▼
┌──────────────┐   ┌──────────────┐
│ 8051-MCU    │   │ freeCodeCamp │
│ (嵌入式)    │   │ (全栈学习)   │
└──────────────┘   └──────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 🆕 扩展领域                                                    │
│ ┌─────────────┐ ┌──────────────────┐ ┌──────────────────┐     │
│ │ Desktop     │ │ 微信小程序开发    │ │ 变现分析         │     │
│ │ 美化        │ │ 校园便利盒       │ │ monetization     │     │
│ └─────────────┘ └──────────────────┘ └──────────────────┘     │
│ ┌─────────────┐ ┌──────────────────┐                           │
│ │ AI 工具集   │ │ 极简编程方法论   │                           │
│ │ ai-tools    │ │ ponytail         │                           │
│ └─────────────┘ └──────────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💡 领域交叉点 — 在哪里用得上

### 场景一：学术论文 + AI 辅助

```
学术写作(Academic) 
    + AI 模型(LLM-Providers) 
    + PPT 演示(PPT-Design)
    = 完整的论文产出流水线
```

### 场景二：AI Agent + 工作流编排

```
AI Agent 技术(AI-Agent)
    + 编排方法(AI-Workflow)
    + 模型容灾(LLM-Providers)
    + 搜索配置(hermes-search-config)
    = Hermes 智能助手核心
```

### 场景三：编程 + 嵌入式开发

```
编程基础(Programming)
    + 嵌入式(8051-MCU)
    + Vibe Coding 工具(Vibe-Coding)
    = 嵌入式开发完整链路
```

### 场景四：CAD + AI 编程

```
CAD 设计(CAD-Design)
    + AI 编程(Vibe-Coding)
    + AI 工作流(AI-Workflow)
    = build123d + AI 参数化设计
```

### 场景五：PPT + AI 图片生成

```
PPT 设计(PPT-Design)
    + 图片生成(ai-image-generation skill)
    + 反推提示词(reverse-prompting)
    + AI 辅助(Academic)
    = 高质量学术汇报
```

### 场景六：自我进化 + 上下文工程

```
上下文工程(k-self-improvement)
    + 极简原则(ponytail)
    + 任务分解(self-improvement-guide)
    + 4步循环(AI-Workflow)
    = Agent 持续优化的方法论闭环
```

### 场景七：AI 科研全流程

```
科研工具(vibe-research)
    + 7阶段流程(researchpilot-skills)
    + 知网插件(cnki-browser-plugin)
    + 110亿Token经验(ai-research-collaboration)
    = 从选题到发表的 AI 辅助流水线
```

### 场景八：闲鱼变现实战

```
价目表(ai-monetization-costs)
    + 能力盘点(monetization-analysis)
    + 服务套餐(academic-service-research)
    + PPT技能(PPT-Design)
    = 学术服务变现闭环
```

---

## 📊 关联矩阵

```dataview
TABLE domain AS "领域", cross-domain AS "交叉域", file.mtime AS "最后更新"
FROM "knowledge"
WHERE cross-domain
SORT domain ASC
```

---

## 🔗 所有知识文件快速导航

| 领域 | 文件 | 核心交叉 |
|:-----|:-----|:---------|
| 🤖 **AI-Agent** | [[AI-Agent]] | Workflow / LLM / PPT / Academic |
| 🔀 **AI-Workflow** | [[AI-Workflow]] | Agent / Skills / CAD |
| 🎨 **PPT-Design** | [[PPT-Design]] | Academic / AI / Vibe |
| 📚 **Academic** | [[Academic]] | PPT / AI / LLM |
| 💻 **Programming** | [[Programming]] | 8051 / CAD / Vibe |
| 🏗️ **CAD-Design** | [[CAD-Design]] | Programming / Vibe / 3D |
| 🔧 **8051-MCU** | [[8051-MCU]] | Programming / Coding |
| 📘 **freeCodeCamp** | [[freeCodeCamp]] | Programming / Fullstack |
| 🌐 **LLM-Providers** | [[LLM-Providers]] | AI-Agent / Fallback |
| 🎮 **Vibe-Coding** | [[Vibe-Coding]] | AI / PPT / Academic |
| 🖼️ **reverse-prompting** | [[reverse-prompting]] | AI-Image / PPT |
| 💡 **desktop-beautify** | [[desktop-beautify]] | Windows / UX |
| 📱 **campus-box-design** | [[campus-box-design]] | WeChat / Fullstack |
| 📐 **CAD-Postmortem** | [[CAD-Project-Postmortem]] | CAD / 3D-Printing |
| 💰 **monetization-analysis** | [[monetization-analysis]] | 变现 / 学术 / 技术接单 |
| 🧪 **ai-monetization-costs** | [[ai-monetization-costs]] | 闲鱼 / 定价 / 利润测算 |
| 🔬 **vibe-research** | [[vibe-research]] | AI科研 / 工具选型 |
| 📝 **researchpilot-skills** | [[researchpilot-skills]] | 科研全流程 / ML |
| 🧩 **k-self-improvement** | [[k-self-improvement]] | 上下文工程 / Agent进化 |
| 🎯 **ponytail** | [[ponytail]] | 极简编程 / 方法论 |
| 🔧 **show-me-the-story** | [[show-me-the-story]] | 长篇小说 / 去AI味 |
| 🛠️ **ai-tools-reference** | [[ai-tools-reference]] | AI工具目录 / 设计 / 视频 |

---

> 文件之间用 `[[wiki link]]` 相互引用，Obsidian 图谱面板会自动绘制关系网络。
> 更新任一文件后，在图谱面板中即可看到新的连接。
