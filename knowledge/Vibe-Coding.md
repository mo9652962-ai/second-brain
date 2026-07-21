---
tags: [coding, tools, windows]
created: 2026-07-21
---

# 编程与技术

## 本地环境

- **OS**: Windows 11 (24H2)
- **Shell**: PowerShell 5.1（不支持 `&&` 和 `||`）
- **Git**: 已安装
- **Python**: python-pptx, Pillow
- **Node**: v24.18.0, npm registry → npmmirror

## 常用工具

- Visual C++ 运行库: AIO v0.105.0（全版本已安装）
- Wallpaper Engine: Steam
- OpenClaw Gateway: http://127.0.0.1:18789

## PowerShell 注意事项

- 命令分隔用 `;`（不能用 `&&`）
- 条件用 `if ($?) { ... }`
- `2>$null` 代替 `2>nul`
- 路径用 `\` 而非 `/`

## 搜索工具

- Tavily: 主力 AI 搜索
- Firecrawl: JS 渲染 + 反爬
- Exa: 语义神经搜索
- web_fetch fallback: Firecrawl

## 桌面美化

- Wallpaper Engine（已有）
- Rainmeter v4.5.26（已下载）
- TranslucentTB 2026.1（已下载）
- ExplorerPatcher（开始菜单，已下载）
- Portals（桌面分区，Fences 替代品）

## 系统维护

### VC++ 运行库
- **工具**: VisualCppRedist_AIO v0.105.0 (30.7MB)
- **全版本检查**: 2005/2008/2010/2012/2013/2015-2022
- **注意**: 2005/2008 在 WinSxS 中，不显示为独立条目

### SFC / DISM 系统扫描
- **SFC**: `sfc /scannow` — 需管理员权限
- **DISM**: `DISM /Online /Cleanup-Image /RestoreHealth` — 先执行，再 sfc
- **场景**: 系统文件损坏、游戏报错、dll 缺失

---

## 🔗 知识关联

- **[[AI-Agent]]** — k 的运行环境与基础设施
- **[[PPT-Design]]** — python-pptx + Pillow 生成环境
- **[[Academic]]** — 文献管理、写作工具链
- **[[projects/current]]** — 桌面美化与系统优化进度
- **[[HOME]]** — 返回知识中枢
