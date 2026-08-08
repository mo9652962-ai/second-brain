---
tags: [browser-automation, best-practices, adopted]
date: 2026-07-29
domain: tools
status: adopted
source: Browser-Use Deep Research + Desktop-Delta Bench
---

# 浏览器自动化最佳实践

> 来源：Browser-Use-Hermes-Integration 深度研究 + Desktop-Delta Bench 验证模式
>
> 核心原则：**用 Hermes 内置工具，不装 MCP；每次操作后必须验证。**

---

## 🚫 第一条：不要安装 agent-browser MCP

| 操作 | 原因 |
|-----|------|
| ❌ 不要配置 agent-browser MCP | 与 Hermes 内置 `browser_*` 工具**完全重复**，导致加载超时/运行时冲突 |
| ✅ 使用 Hermes 内置工具 | 12 个 browser_* 工具覆盖所有场景 |

> ⚠️ 这是踩过的坑：曾尝试配置 agent-browser MCP → 加载超时 → 记忆库已记录为禁止项。

---

## 🛠 可用工具速查

| 工具 | 用途 | 示例 |
|-----|------|------|
| `browser_navigate` | 打开 URL | 打开网页 |
| `browser_snapshot` | 可访问性树快照 | 获取页面元素 @e1, @e2... |
| `browser_click` | 点击元素 | `ref="@e5"` |
| `browser_type` | 输入文本 | `ref="@e3" text="search"` |
| `browser_press` | 按键 | Enter, Tab, Escape |
| `browser_scroll` | 滚动 | up / down |
| `browser_back` | 后退 | 返回上一页 |
| `browser_get_images` | 获取图片列表 | 提取图片 URL |
| `browser_vision` | 截图+视觉分析 | 描述页面内容 |
| `browser_console` | 控制台日志 | JS 错误/调试 |
| `browser_cdp` | 原生 CDP 命令 | 高级调试 |
| `browser_dialog` | 处理对话框 | alert/confirm/prompt |

---

## ✅ 操作验证规范（DDB 三步法）

每次浏览器操作后，必须执行以下三步：

### 1. 等待（1-2 秒）
```
browser_click → 等 1-2s → 别立即 snapshot
```
原因：推理/远程输入/渲染/截图是**异步的**，下个观察可能延迟/遮挡/瞬变/无关。

### 2. 确认（snapshot 对比）
```
browser_snapshot → 对比前后状态 → 确认目标变化
```
检查：元素消失？新元素出现？URL 变化？文本更新？

### 3. 重试（最多 2 次）
```
无变化 → browser_click 重试 → 等 1-2s → snapshot 再确认
2 次仍无变化 → 报告失败，不继续
```

### Drag 专项注意
- Drag 动作定位能力 F1 仅 **0.76**（vs Click 0.96）
- 验证时必须检查**目标位置坐标**是否真的变化了
- 重试 2 次仍无效 → 改用 Click 模拟或告知用户

---

## 📋 常用工作流

### 工作流1：网页 → 知识库归档
```
browser_navigate URL
  → browser_snapshot full=true 提取内容
  → AI 结构化（标题/标签/摘要）
  → write_file 保存到 knowledge/
```

### 工作流2：表单填写
```
browser_navigate URL
  → browser_snapshot 获取表单元素
  → browser_type @e_input "text"
  → browser_click @e_submit
  → 等 1-2s → browser_snapshot 确认提交结果
```

### 工作流3：批量信息抓取
```
browser_navigate 列表页
  → browser_scroll down 多次加载
  → browser_snapshot 获取所有条目
  → 逐条 browser_click → 等 1-2s → snapshot 提取详情
```

---

## ⚡ 性能优化

| 技巧 | 效果 | 场景 |
|-----|------|------|
| `browser_snapshot full=false` | 节省 50% Token | 只需交互元素时 |
| `browser_vision` vs snapshot | 节省 95% Token | 只需"看"页面时 |
| 先 scroll 后 snapshot | 避免重复请求 | 长列表/无限滚动 |
| `web_extract` 替代 browser | 快 10x | 纯文本页面（.md/.txt/.json） |

---

## 🛡 反检测策略

| 场景 | 方案 |
|-----|------|
| 普通网站 | 内置 browser_* 工具足够 |
| 轻微反Bot | 用 browser_vision 而非频繁 snapshot |
| Cloudflare 盾 | 需要 `/browser connect` 连真实 Chrome + Camofox |
| 验证码 | 需要 Browserbase 云服务或人工介入 |

---

## ⚠️ 踩坑记录

| 坑 | 解决 |
|---|------|
| Chrome 未开启调试模式 | 用 `/browser connect` 连接 |
| CDP 端口拒绝连接 | 检查 Chrome 是否以 `--remote-debugging-port` 启动 |
| agent-browser MCP 重复 | **不要安装**，用内置工具 |
| WSL2 网络隔离 | 不用 CDP，用内置工具即可 |

---

*固化时间：2026-07-29 | 下次更新：遇到新的浏览器踩坑时*

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
