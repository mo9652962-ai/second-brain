# TOOLS.md - 本地工具笔记

## 模型与供应商

- **主力模型**: opencode-go/deepseek-v4-pro
- **Fallback 链**: deepseek-v4-pro → kimi-k2.6 → qwen3.7-plus → glm-5.2
- **注意**: 全部走 opencode-go 供应商，供应商级故障时 fallback 链也无效
- **配置修改**: agents.defaults.model 下的字段受保护，需直接编辑 `openclaw.json` → `gateway restart`

## 搜索工具

- **主力搜索**: Tavily（搜索 + 提取）
- **Fallback 增强**: Firecrawl（API: fc-7cb095...）— JS 渲染、反爬、结构化提取
- **web_fetch**: Firecrawl 作为 fallback，处理 JS 重页面
- **DuckDuckGo**: 国内被墙，不可用
- **SearXNG**: 本地部署 http://127.0.0.1:8888
- **超时**: 120s（config: tools.web.search.timeoutSeconds）

## 图片下载（国内网络）

| 源 | 状态 | 备注 |
|---|---|---|
| Wikimedia Commons | ✅ 可用 | CC 授权实景照片 |
| Unsplash | ❌ 503 | 被墙 |
| Pixabay | ❌ 403 | 可能需要 referer |
| Pexels | ❌ 403 | CloudFlare 拦截 |

- **下载方式**: `urllib.request.Request` + `User-Agent` header
- **不要用**: `urllib.request.urlretrieve`（易 403）
- **备选方案**: Pillow 本地生成原创插图

## Skills 体系

- **安装**: `clawhub install @作者/slug`（先搜索对比下载量）
- **安全**: 安装前用 skill-vetter 审计
- **更新**: `clawhub install slug` 覆盖旧版
- **总计**: 26 个已安装
- **编排**: 见 [[knowledge/Dev/AI-Workflow]] — 5 大 Multi-Agent 模式 + 5 大 Skill 设计模式
- **Skill 家族**: 论文(9) / PPT(6) / 图片(7) / 自改进(3) / 搜索(1)
- **Pipeline 触发**: 用户说「做PPT」→ 自动链式激活 outline→generator→optimizer

## Cron / Heartbeat

- **Heartbeat**: 批量检查（邮件+日历+天气），有上下文，约 30min 间隔
- **Cron**: 精确定时独立任务，isolated session
- **静默规则**: 80-95% 心跳返回 HEARTBEAT_OK
- **关键**: 自主执行的 cron 用 `isolated agentTurn`，不要用 `systemEvent`

## 配置保护

- `agents.defaults.model.primary` / `fallbacks` 等受保护路径 → 直接编辑 `openclaw.json` + restart
- 普通配置 → `config.patch` 即可

## PPT 制作流程

1. 大纲设计（JSON 骨架）
2. python-pptx 生成结构
3. 数据注入（Tavily 搜索真实数据）
4. 图片方案（Wikimedia Commons CC 图片优先）
5. 背景注入（post-processing 脚本）
6. 打破 AI 模式（润色：诗词、布局多样性）

## 环境

- **OS**: Windows 11 (x64)
- **Shell**: PowerShell（注意：不支持 `||` 和 `&&`，用 `;` 或 `if/else` 替代）
- **Workspace**: `C:\Users\31954\.openclaw\workspace`
- **Config**: `C:\Users\31954\.openclaw\openclaw.json`

## PowerShell Gotchas

- 不支持 `||` 和 `&&` 运算符，使用 `if ($?) { ... }` 或分号分隔
- 不支持 `2>nul`，使用 `2>$null` 或 `-ErrorAction SilentlyContinue`
- 路径分隔符：Windows 使用 `\`，传递给 CLI 工具时注意转义
- `dir` 可用但推荐 `Get-ChildItem`（更可靠），`rm` 对应 `Remove-Item`

## Memory 架构 (2026-07-20 引入)

| 文件 | 用途 | 触发条件 |
|---|---|---|
| `SESSION-STATE.md` | WAL Protocol 活跃工作记忆 | 每次 corrections/decisions/preferences |
| `memory/working-buffer.md` | Danger zone 交互日志 | 上下文 >60% 时激活 |
| `memory/YYYY-MM-DD.md` | 每日原始日志 | 每天 |
| `MEMORY.md` | 长期 curated 记忆 | 定期从 daily notes 提炼 |

**WAL Protocol 规则**：收到 corrections/decisions/preferences/names 时 → 先写 SESSION-STATE.md → 再回复。
上下文丢失后恢复顺序：`working-buffer.md` → `SESSION-STATE.md` → `daily notes` → `MEMORY.md`

## 2026 AI Agent 持续学习最佳实践

- **Agent 持续学习 ≠ 模型微调**：改进发生在 harness 和 memory 层
- **Verifiable Continual Learning**：失败→可重放环境→regression 测试→路由修复到正确层
- **Memory 是 #1 瓶颈**：无记忆层的 agent 会快速退化
- **Graph-based Memory**：向量检索 + 图数据库混合方案（2026前沿）
- **AgentOps**：CI/CD for agents，量化指标 + 持续监控

---

_最后更新: 2026-07-20_
