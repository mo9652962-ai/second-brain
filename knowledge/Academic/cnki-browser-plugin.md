# 科研工具：攻玉学术·知网浏览器插件

来源：小黑盒 "吃太饱骑士"
更新：2026-07-25

## 痛点
- AI 搜索底座遭遇知网认证墙，无法访问封闭文献库
- AI 整理的资料不全或造假（链接存在但文不对题）
- 国外模型（Grok/Gemini）对国内文献检索能力弱

## 插件：攻玉学术·知网浏览器插件
- **原理**：借助你的浏览器认证身份访问知网，绕过 AI 机器人拦截
- **功能**：
  - AI 对话（内置 DeepSeek v4 Pro/Flash）
  - 知网文献检索（AI 自动拆解检索需求）
  - 文献解析 + PDF 下载（开发中）
  - AI 自动操作（AI 自主调用插件检索）
- **获取**：jadense.com/plugin/browser-extension 或 搜"攻玉学术"→插件生态
- **状态**：Chrome 审核中，可手动安装

## MIMO PLAN API（免费）
- API Key: `tp-cmab578xzriowahx3mb22swlb6pp61p71odtluxklu7rmfsf`
- 额度：460亿 Credits（量大管饱）
- API URL：`https://api.xiaomimimo.com/v1`
- 模型：`mimo-v2-flash`（快速）/ `mimo-v2-pro`（深度推理）
- 兼容 OpenAI 格式，可用在 Codex / Claude Code / OpenClaw 等工具
- 认证方式：Header `api-key: $KEY` 或 `Authorization: Bearer $KEY`
