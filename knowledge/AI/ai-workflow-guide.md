# AI 工作流搭建实战指南

来源：10 轮搜索引擎研究 + 现有知识整合
更新：2026-07-25

## 一、工具全景

| 工具 | 定位 | 部署方式 | 适合你吗？ |
|:----|:-----|:---------|:----------|
| **Hermes Agent** | AI Agent 编排（已有） | 已部署 | ✅ **主引擎** |
| **WorkBuddy** | 腾讯 AI 办公助手 | 桌面端 | ⚠️ 可试试 |
| **n8n** | 开源工作流自动化引擎 | Docker/自部署 | ❌ Docker 不可用 |
| **Dify** | 开源 LLM 应用平台 | Docker/自部署 | ❌ Docker 不可用 |
| **Coze (扣子)** | 字节零代码 AI 平台 | SaaS 免费 | ✅ **补充** |
| **OpenClaw** | AI Agent 平台 | 本地/云 | ⚠️ 可尝试 |
| **RAGFlow** | 开源 RAG 知识库 | Docker | ❌ Docker 不可用 |

## 二、选型结论

```
你的限制：Docker 不可用、Windows 环境
你的优势：已有 Hermes（cron+delegation+skills）
你的场景：闲鱼变现（PPT/论文/PCB）

推荐方案：
  主力 → Hermes Agent（已有，够用）
  补充 → Coze（扣子），零代码免费，注册即用
```

## 三、Hermes 已有能力清单

| 能力 | 用途 | 配置状态 |
|:-----|:-----|:---------|
| **cron 定时任务** | 每日 arXiv 论文检索（7:00+8:00） | ✅ 已配 |
| **delegate_task** | 并行派生子 Agent 处理任务 | ✅ 可用 |
| **skill_manage** | 按需加载 93 个 Skills | ✅ 全活跃 |
| **web_search** | 5 路搜索引擎并行检索 | ✅ 正常 |
| **memory** | 跨会话持久记忆 | ✅ 正常 |
| **mcp_servers** | GitHub + FileSystem 接入 | ✅ 已配 |
| **curator** | Skill 自动维护 | ✅ 已启用 |

## 四、工作流搭建路线图

### 第 1 层：单次任务（已有）
```
用户需求 → Hermes 调用对应 Skill → 交付结果
例："做一份 ppt" → load ppt-design-2026 → 交付
```

### 第 2 层：定时自动化（已有 cron）
```
定时触发 → Hermes 自动执行 → 结果推送
例：每天 7:00 → arxiv-fetch → 8:00 → arxiv-summarize
```

### 第 3 层：多步骤 Pipeline
```
步骤 A → [context_from] → 步骤 B → [context_from] → 步骤 C
例：web_search(话题) → arxiv(论文) → academic-paper-writing(综述)
```

### 第 4 层：多 Agent 并行（fan-out）
```
用户需求
  ├──→ Agent A (搜索)
  ├──→ Agent B (分析)
  ├──→ Agent C (写作)
  └──→ 汇总结果
```

### 第 5 层：条件分支
```
用户需求 → 判断类型
  ├── 论文类 → academic-paper-writing
  ├── PPT类 → ppt-design
  ├── PCB类 → pcb-design
  └── 其他 → 通用处理
```

## 五、你的场景 × 工作流方案

### 场景 1：闲鱼论文接单自动化
```
收稿（手动）→ 零感AI降重（工具）→ 人工精修 → 交付
Hermes 可辅助：用文稿检查、去AI味质检
未来：Coze 可做自动回复机器人
```

### 场景 2：每日知识吸收 Pipeline
```
✅ 已配：7:00 arxiv-fetch → 8:00 arxiv-summarize
可扩展：9:00 写入 Obsidian 知识库
```

### 场景 3：多源并行调研
```python
delegate_task(tasks=[
    {"goal": "web_search: 主题趋势"},
    {"goal": "web_search: 竞品分析"},
    {"goal": "web_search: 技术方案"},
])
```

## 六、后续步骤建议

| 优先级 | 行动 | 说明 |
|:------|:-----|:------|
| ⭐⭐⭐ | **用好 Hermes 已有能力** | cron + delegation + skills 已够用 |
| ⭐⭐ | **注册 Coze 做补充** | 零代码搭建，适合快速验证想法 |
| ⭐⭐ | **搭建闲鱼自动回复** | 用开源工具或 Hermes gateway 实现 |
| ⭐ | **扩展 Pipeline 链** | 现有的 arxiv 链可扩展到更多场景 |

## 七、参考链接

- WorkBuddy 蓝皮书：https://workbuddy.homes/
- WorkBuddy 下载：https://www.workbuddy.cn
- Coze 扣子：https://www.coze.cn
- n8n：https://n8n.io
- Dify：https://dify.ai
- OpenClaw：https://github.com/openclaw/openclaw
