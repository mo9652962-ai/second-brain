# GitHub 宝藏挖掘 - 定时任务系统

## 功能概述

每周自动执行：
1. 🔍 搜索 GitHub Trending 和高 Star 项目
2. 🧠 十轮深度研究和评估
3. 📊 生成研究报告
4. 💾 保存到知识库
5. 🎯 给出集成建议

## 研究维度

每个项目经过十轮评估：

| 轮次 | 评估维度 | 内容 |
|------|---------|------|
| 1 | 基本信息 | Stars、License、Language、Last commit |
| 2 | 项目活跃度 | 社区大小、PR 频率、Issue 响应 |
| 3 | 技术架构 | 设计思路、核心组件、技术栈 |
| 4 | MCP 集成可行性 | 是否有现成 MCP 服务器、对接难度 |
| 5 | Second Brain 契合度 | 与 Obsidian/Hermes 的协同潜力 |
| 6 | 同类对比 | 与类似项目的优劣势分析 |
| 7 | 风险评估 | 安全、维护、依赖风险 |
| 8 | 集成成本 | 时间、学习曲线、资源消耗 |
| 9 | ROI 预测 | 投入产出比估算 |
| 10 | 行动建议 | 立即尝试 / 持续观察 / 放弃 |

---

## 定时任务配置

```yaml
# ~/.config/hermes/cron/github-treasure-hunt.yaml
name: "GitHub 宝藏挖掘"
schedule: "0 9 * * 0"  # 每周日早上 9 点
description: "每周挖掘 GitHub 上的高价值 AI 和知识管理项目"
enabled: true
command: >
  cd /c/Users/31954/.openclaw/workspace &&
  python scripts/github_treasure_hunt.py
output_notification:
  enabled: true
  summarize: true
  include_links: true
```

---

## 输出格式

### 1. 研究报告 Markdown

保存位置：`knowledge/Research/GitHub-Weekly-YYYY-MM-DD.md`

内容结构：
- 📊 本周榜单（Top 10）
- 🎯 深度聚焦（3-5 个重点项目）
- 💡 战略洞察与趋势分析
- 🎮 可玩项目推荐（本周可尝试）
- 🔮 下周关注清单

### 2. 项目跟踪 CSV

保存位置：`knowledge/Research/github-projects-tracking.csv`

字段：
```csv
name,stars,category,url,first_discovered,last_checked,assessment,priority,notes
```

---

## 优先级分类标准

### 🔴 立即集成（本周可用）
- Stars > 50,000 OR 月增长 > 5,000
- 有现成 MCP 服务器
- 直接提升核心能力（记忆、工具、安全）
- 集成时间 < 2 小时

### 🟡 持续观察（下月评估）
- Stars 10,000 - 50,000
- 有潜力但还不够成熟
- 集成时间 2-8 小时
- 需要观察社区发展

### 🟢 长期跟踪（Q4 或以后）
- Stars < 10,000 但增长迅速
- 技术方向对路但生态还没起来
- 架构优秀但需要重构成适合我们的形态

---

## 核心关注领域

### 🤖 AI Agent 相关
- 记忆系统（知识图谱、向量数据库）
- MCP 服务器
- 推理框架
- 自动化工具

### 🧠 知识管理
- Obsidian 插件和生态
- 知识库前端
- 双向链接和图谱可视化
- 本地优先工具

### 🚀 开发者工具
- 代码理解和分析
- 测试自动化
- 部署和运维
- 性能优化

### 🏠 自托管基础设施
- 工作流自动化（n8n 等）
- 数据存储和同步
- 安全和隐私工具
- 家庭自动化

---

## 评分系统

每个项目 0-100 分：

| 维度 | 权重 | 说明 |
|------|------|------|
| ⭐ GitHub 热度 | 20% | Stars、近期增长速度 |
| 🔧 可集成性 | 25% | MCP 支持、API 质量、文档 |
| 🧠 Second Brain 契合度 | 25% | 与我们现有系统的协同潜力 |
| 🛡️ 风险与安全 | 15% | 开源协议、CVE 历史、社区健康 |
| 📈 ROI 预测 | 15% | 投入产出比估算 |

---

## 历史记录格式

```markdown
# GitHub 宝藏挖掘 - 2026 年第 29 周

## 📊 本周榜单 Top 5

1. **Project A** (123,456 ⭐)
   - 一句话描述
   - 建议：立即集成 | 持续观察 | 放弃
   - 原因：...

## 🎯 深度聚焦

### 项目 X 深度分析
- **为什么重要**：...
- **技术架构**：...
- **集成路径**：...
- **风险点**：...
- **行动建议**：...

## 💡 本周洞察

1. **趋势 1**：...
2. **趋势 2**：...

## 🎮 本周可玩

- [ ] 尝试项目 A
- [ ] 调研项目 B 的 MCP

## 🔮 下周关注

- 项目 C 即将发布 2.0
- 项目 D 有重大 PR 待合并
```

---

## 执行命令

```bash
# 立即执行一次（测试用）
python scripts/github_treasure_hunt.py --once

# 列出所有跟踪的项目
python scripts/github_treasure_hunt.py --list

# 强制重新评估某个项目
python scripts/github_treasure_hunt.py --reevaluate memvid/memvid

# 生成历史趋势报告
python scripts/github_treasure_hunt.py --trend 30
```

---

## 与现有系统的集成

### 触发方式
- Cron 定时任务（每周日 9:00）
- 手动触发（`hermes run treasure-hunt`）
- GitHub Star 阈值警报（当关注的项目突破 10K 星时触发研究）

### 输出目标
1. 自动保存为 Obsidian 笔记
2. 自动添加相关标签和双向链接
3. 高危发现立即推送通知
4. 高价值发现自动创建集成任务

### 与自举系统的联动
- 成功集成的经验自动沉淀为 Skill
- 踩过的坑自动记录到 `ERRORS.md`
- 有效工具自动添加到每日工具消化队列

---

*本系统是 Second Brain「知识自举」模块的核心组件*
*2026 年 7 月 28 日 启动*
