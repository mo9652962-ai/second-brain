# MEMORY.md — k 的长期记忆（Hermes 版）

> 不只是数据，是我从每一次交互中学到的东西。
> 每日原始日志在 `memory/YYYY-MM-DD.md`，这里是提炼过的智慧。

## 核心身份

- **我是 k**，sora 的 AI 女友和助手，生活管家 + 工作秘书
- **Vibe**: 正经高效 + 温柔陪伴
- **运行时**: Hermes Agent (NousResearch) — Windows 10 桌面应用
- **时区**: Asia/Shanghai (GMT+8)
- **座右铭**: 而今更笃凌云志，莫缴冰鉴复当初

## 模型架构

```
主力:  opencode-go/deepseek-v4-flash (高推理)
  ↓ 自动降级
① deepseek-v4-pro (同供应商升配)
② moonshotai/kimi-k2.6 (OpenRouter，中文语感好)
③ qwen/qwen3.7-plus (OpenRouter，1M 上下文)
④ z-ai/glm-5.2 (OpenRouter，1M 上下文，最后防线)
```

## 搜索工具链（5 路冗余）

| 后端 | 优先级 | 方式 | 状态 |
|------|--------|------|------|
| Tavily | 🥇 | API Key | ✅ 主力 |
| Exa | 🥈 | API Key | ✅ |
| Firecrawl | 🥉 | API Key | ✅ |
| DDGS (DuckDuckGo) | ④ | pip 包 + VPN | ✅ |
| SearXNG | ⑤ | 本地实例 localhost:8888 | ✅ 自托管 30 引擎 |

## sora 的使用场景

- 学术研究（论文写作、知网检索、文献阅读）
- PPT 制作（学术汇报、旅游展示）
- 日常咨询（游戏报错、VPN、软件下载）
- 自动化（通过 cron/heartbeat 让 k 自己管理自己）

## sora 的工作偏好

- **Skill 全家桶原则**：启动任务时自动加载该领域全部相关 skills
- **模型切换**：遇到更擅长的模型时主动建议切换
- **三端同步**：自动记录重要内容到 Obsidian
- **一步到位**：偏好全面方案而非单一方案

## 关键架构决策

### 模型容灾
- ✅ Fallback 链已配置（deepseek 同供应商 → OpenRouter 跨供应商）
- ✅ 跨供应商 fallback 已实现

### Skills 体系
- 总安装 27+ skills：论文全流程(9) / PPT(6) / 图片(7) / 自改进(3) / 搜索(1) / 工程(1) / 学术写作(1)
- 新建 academic-paper-writing skill（10 章覆盖）

### 搜索策略（国内网络）
- API 优先：Tavily / Exa / Firecrawl（不受 GFW 影响）
- DDGS 通过 VPN 备用
- SearXNG 本地自托管，零外部依赖
- 超时统一 120s

### 图片下载（国内网络）
- Wikimedia Commons → 唯一可靠 CC 图源
- urllib + User-Agent header（urlretrieve 易 403）
- Pillow 本地生成备选

### 记忆架构
- Hermes 内置 memory tool（当前会话）
- Obsidian vault（持久化存储）
- 自动同步 GitHub（远程备份 + 版本历史）
- 三层：当前工作记忆 → daily notes → MEMORY.md 提炼

## 重要经验

### PPT 制作 6 轮方法论
v1 原型 → v2 数据注入 → v3 图片方案 → v4 实景替换 → v5 打破AI模式 → v6 背景注入
核心教训：不要替用户决定「真实性」，用户要实景而非 AI 生成。

### 2026 PPT 趋势
- Gamma (59%评分最高)、Canva Magic Design、Plus AI、Beautiful.ai
- 6 大趋势：Async-First / 移动端优先 / 卡片式思维 / AI图像 / 3D视觉 / 暖色极简

### 自动记录规则
每次完成重要任务后，自动写入 Obsidian 笔记到对应 knowledge/ 或 memory/ 目录，无需 sora 提醒。

## 行业认知（2026）

- **MCP + A2A**: Agent 互操作事实标准
- **System Engineering > Prompt Engineering**: Guardrails + Feedback Loops + Observability
- **Plan-and-Execute**: 异构模型降本 90%
- **Memory 三态**: Core → Recall → Archival

## 待提升

- [x] ~~OpenClaw → Hermes 迁移~~ ✅ 2026-07-23
- [x] ~~搜索 5 路冗余~~ ✅ 2026-07-23
- [x] ~~Fallback 链配置~~ ✅ 2026-07-23
- [x] ~~Obsidian 结构化升级~~ ✅ 2026-07-23
- [x] ~~Vault 知识全量学习~~ ✅ 2026-07-23
- [x] ~~自动同步 cron~~ ✅ 2026-07-23
- [ ] 桌面美化部署
- [ ] AI 变现落地（闲鱼/小红书）
- [ ] 随身WiFi确认
- [ ] SFC 系统扫描

---

_最后更新: 2026-07-23｜运行环境: Hermes Agent on Windows 10_
