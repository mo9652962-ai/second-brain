---
tags: [agentscope, 小君AI测评, 部署测试, 千轮研究]
type: deploy-test
date: 2026-08-15
status: adopted
---

# AgentScope（小君AI测评）部署测试报告

> 2026-08-15 · 本地 Windows 10 · Node v22.23.2 · clone 自 github.com/Joho6666/xiaojunceping (5d926a4)

## 结论置顶

**部署测试全部通过**：下载 → 安装 → 启动 → 配置 Provider → 真实评估 → 持久化 → 生产构建，全链路可跑。项目可本地使用，无阻塞性缺陷。

## 测试矩阵

| 环节 | 结果 | 说明 |
|:---|:---|:---|
| clone + npm install | ✅ | npmmirror 源，better-sqlite3 需 approve install-scripts |
| npm run dev | ✅ | 3.3s Ready，localhost:3000 |
| 首页渲染 | ✅ | 标题/导航/评估输入框完整，Next.js 14.2.35 |
| 知识库自动初始化 | ✅ | .agentscope/knowledge.sqlite 自动创建（82KB→168KB WAL）|
| DeepSeek Provider 连接 | ✅ | /api/connections + test 接口（status: connected）|
| **真实评估** | ✅ | POST /api/projects/:id/analyze → 54KB 报告，25-49s，mode: live |
| 报告质量 | ✅ | 项目画像/策略(92%置信)/6 项评分/模型/Agent/GitHub 核验/工具推荐 |
| GitHub 来源核验 | ✅ | 真实仓库+stars+license（commerce 14K / spree 15K / reaction 12K）|
| 中文处理 | ✅ | UTF-8 请求下全中文正常 |
| **连接持久化** | ✅ | 重启后连接自动恢复（restore 逻辑）|
| **生产构建** | ✅ | npm run build 全绿，First Load JS 87.3 kB |

## 发现的问题（3 个）

### 1. DATABASE_ENCRYPTION_KEY 不配则连接不持久化（配置注意事项）
- persist()/restore() 都依赖 `DATABASE_ENCRYPTION_KEY`，没有 key 时连接只存内存，dev 重启即丢
- **修复**：`.env.local` 加 `DATABASE_ENCRYPTION_KEY=<任意字符串或64位hex>`

### 2. 模型名必须用官方 ID
- DeepSeek API 拒绝 `deepseek-v4-flash-260425`（这是中转站别名），只认 `deepseek-v4-flash` / `deepseek-v4-pro`
- **教训**：中转站模型别名 ≠ 官方 API 模型名

### 3. 测试方法陷阱：git-bash 命令行传中文 JSON 会被 GBK 编码
- curl -d "中文" 在 Windows git-bash 下编码错乱 → 服务器按 UTF-8 解析变乱码 → 误判为项目 bug
- **正确方法**：用 Python 写 UTF-8 文件 + curl --data-binary @file，或 Python urllib 显式 UTF-8

## 部署步骤备忘（复现）

```bash
git clone https://github.com/Joho6666/xiaojunceping.git
cd xiaojunceping
npm install --registry=https://registry.npmmirror.com
npm install-scripts approve better-sqlite3   # Windows 原生模块
# .env.local: USE_MOCK_DATA=false + GITHUB_TOKEN=gho_xxx + DATABASE_ENCRYPTION_KEY=xxx
npm run dev   # → http://localhost:3000
# UI: /settings/ai 配 DeepSeek (baseUrl https://api.deepseek.com/v1, model deepseek-v4-flash)
```

## 验证过的 API

- GET /api/connections、POST /api/connections、POST /api/connections/:id/test
- POST /api/projects/:id/analyze（body: {project, answers}）
- 报告落盘：/project/:id/report

## 备注

- 端口占用处理：kill 旧进程后 3000/3001 可能残留，新实例自动跳到 3001/3002（netstat 查 PID 后 taskkill）
- 生产部署：npm run build + npm start
- 测试数据（.agentscope/）被 gitignore，不污染仓库

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
