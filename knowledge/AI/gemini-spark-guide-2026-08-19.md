# Gemini Spark 使用指南（千轮研究 2026-08-19）

> 来源: 官方帮助文档 + 台湾媒体实测（104職場力/遠見）+ 大陆可用性实测报告
> 状态: 已开放台湾（Pro 用户），美国 Ultra beta，大陆不支持

## 一、Spark 是什么

```
Gemini 的「AI 代理模式」（不是模型）:
  - 24/7 云端后台运行（关电脑/锁屏也干活）
  - 由 Gemini 3.7 Flash 驱动（2026-08-19 起）
  - 核心三件套: Task（做什么）/ Schedule（何时做）/ Skill（怎么做）
  - 深度集成 Google Workspace（Gmail/日历/Drive/Docs/Sheets/Slides/Keep/Tasks）
  - MCP 工具: Canva/OpenTable/Instacart
```

## 二、使用前提（必须全满足）

```
✅ 年满 18 岁
✅ 个人 Google 账号（公司/学校账号不支持）
✅ Google AI Pro 或 Ultra 订阅
✅ 开启「保留活动记录」（Keep Activity）
✅ 账号国家 + IP 在支持地区（台湾/美国等，大陆不支持）
```

## 三、入口

```
网页版: gemini.google.com → 侧栏「切换至 Spark」（或直链 gemini.google.com/spark）
Mac App: v1.80+ 侧栏 Spark 标签（可开 Connected Folders 读本地文件夹）
移动 App: Gemini App 侧栏
检查是否开通: 侧栏看到 Spark = 已开通
```

## 四、使用步骤（网页版）

```
① 打开 gemini.google.com → 侧栏点 Switch to Spark
② 描述任务（自然语言，如「每天早上 7 点查看邮件日历整理待办」）
③ 可选增强:
   - 指定时间/事件（Schedule）: 对话式描述即可
   - 指定 Skill: 输入 / 选技能
   - 附文件: Upload & tools → 上传/Drive/Notebook
④ Submit → Spark 规划执行步骤
⑤ 工作面板监控: Progress（步骤进度）/ Files（读写的文件）/ Schedules（排程）
⑥ 远程浏览器任务: 可接管（Take over task）或交回（Go back to Gemini）
```

## 五、排程类型（Schedule）

| 类型 | 触发方式 | 例子 |
|:---|:---|:---|
| 时间型 | 一次/每小时/每天/每周/每月/每年 | 「每天早上7点整理待办」|
| Gmail 监控 | 收到符合筛选条件的邮件 | 「收到客服信→查规范→草稿回复」|
| 主题监控 | 事件触发（新闻/财经/体育/本地活动）| 「新展览→邮件通知+日历建议」|

```
管理: Schedules 页面（Ongoing/Paused/Completed）
上限: 50 个活跃排程
注意: 不适合快速变化数据/时间紧迫任务
```

## 六、Skills（技能）——和 Hermes skill 同理念

```
创建: 对话式 / 模板 / 上传技能文件
命名: 全小写+连字符（如 my-new-skill）
描述: 「Use when…」开头，1024 字符内
加载: 只读名称+描述判断相关性 → 需要时才读全文
适用: 重复性工作规则（格式/流程/偏好）
注意: 与 Gemini 的 Gem 不同（Skill 是 Spark 专属）
```

## 七、安全设置

```
✅ 高风险操作（付款/发邮件/删日历）默认需确认
✅ 活动日志: gemini.google.com/spark/activity（建议每周审计，防提示注入）
✅ 权限: Settings → Safety → 消费确认门槛（默认 $0 = 不能自主花钱）
⚠️ 敏感信息（登录/付款）不要直接输入 Task 对话
```

## 八、大陆可用性（sora 关键）

```
❌ 大陆不支持（GFW 硬墙 + 订阅检查账号国家）
✅ 可用路径: 海外账号（非+86）+ 稳定 VPN + 账号国家匹配
   - 台湾/美国/日本/新加坡均可（Pro 支持地区）
   - 账号国家 1 年冷却才能改
   - 节点不要跳国家（会被风控）
⚠️ sora 现状: Gemini Pro 已开通 + FlClash VPN
   → 需验证: 侧栏是否出现 Spark（台湾已开放 Pro）
   → 风险: 账号地区动态评估（Antigravity 曾回中国）
```

## 九、实战案例（媒体实测）

```
① 定时排程: 「每天早上8点整理行程+待办+需回邮件，列优先3件事」
② Gmail 监控: 「收到客服信→整理问题→查 Drive 规范→草稿回复（不寄出）」
③ 跨服务整理: 「查最近2周 Gmail/Drive/Calendar 的『新品上市』资料→整理进 Docs」
④ 订阅监控: 「每月1号查账单发票→找涨价/到期订阅→草拟取消信」
⑤ 旅行规划: 「收到航班/酒店确认信→存进行程试算表→查当地活动→填日历」
⑥ 写作风格: 「读我过去50封邮件→归纳风格→设为『代笔专家』技能」
```

## 十、适用判断

```
✅ 适合 Spark: 多步骤连续工作 / 跨 Google 服务 / 等待条件触发 / 背景执行
❌ 一般 Gemini 即可: 问答/写文案/单次摘要
```

---
> 🗺️ 属于 [[MOC-AI]] · [[Home|🏠 Home]]
