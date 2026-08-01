---
tags: [research, github, article-study, disk-tools, neodisk]
created: 2026-08-01
status: absorbed
source: https://github.com/tkslucas/Neodisk
---

# Neodisk — 研究笔记（macOS 磁盘可视化分析工具）

> 来源：小黑盒文章（软件格律诗 07-26）· 2026-08-01 验证 + 评估

## 项目验证

| 项 | 值 |
|----|-----|
| 仓库 | tkslucas/Neodisk |
| Stars | 70（小项目但真实） |
| License | GPL-3.0 |
| 语言 | Swift（原生 macOS，Apple Silicon 优化） |
| 创建 | 2022-06 |
| 架构 | NeodiskKit（扫描核，衍生自 Radix）+ TreemapKit（几何）+ NeodiskUI（SwiftUI） |

## 功能（文章与仓库一致）

| 功能 | 说明 |
|------|------|
| Tree Map + Sunburst 双视图 | 矩形树状图 + 旭日图，快速定位大文件 |
| 只读设计 | **不提供删除功能**，双击文件用 Finder 打开，自行处理（降低误删风险） |
| 文件变化检测 | 找出"为什么磁盘突然变少"（node_modules/缓存增长） |
| 重复文件检测 | content-hash 验证的重复文件查找 |
| 按时间/类型筛选 | 一年以上未用的大文件、占空间最多的视频等 |
| Cloud Scan | iCloud/云盘本地占用分析 |
| 并行扫描 | 提升扫描速度 |

## 竞品全景（验证时发现 4 个同类）

| 工具 | 平台 | License | 特点 |
|------|------|:---:|------|
| **Neodisk** | macOS | GPL-3.0 | 只读双视图，衍生自 Radix |
| OpenDisk | macOS | MIT | 17s 扫 1TB（DaisyDisk 的 2.2 倍快） |
| Radix | macOS | 私有 | Neodisk 的灵感来源，sunburst+treemap |
| DiskSage | macOS | MIT | 带安全顾问（知道什么能安全删） |
| **WizTree** | **Windows** | 免费 | **Windows 最佳平替**（NTFS MFT 直读，秒级扫描） |

## 我们的评估

| 选项 | 决策 | 理由 |
|------|:---:|------|
| 安装 Neodisk | ❌ | **macOS 专用（Swift），sora 是 Windows 10** |
| 安装 WizTree（Windows 平替） | 🟡 可选 | 系统盘 38%（170G/448G）无紧迫需求；装可备用 |
| **只读设计理念吸收** | ✅ | 工具负责发现问题，不直接删文件——降低误删风险 |

## 理念吸收：只读设计（有普适价值）

**Neodisk 最值得学的不是功能，是设计哲学**：
- 工具负责"发现问题"（分析、展示、定位）
- 删除操作交给用户自己完成（Finder/手动）
- 作者明确说：担心误删，所以不做删除功能

**与我们的映射**：
- 呼应规则 #16（状态优先）：分析工具应该基于真实状态，不越权操作
- 呼应安全原则：自动化工具的高风险动作（删除）应交还人工
- 类似"只读模式"：我们做练习册生成、文件操作时的干跑/预览模式同理

## 结论
- 项目真实但 macOS-only，对我们（Windows）**不安装**
- 若 Windows 磁盘告急，推荐 **WizTree**（NTFS MFT 直读，比 DaisyDisk 类工具快得多）
- 设计理念（只读）已吸收——自动化工具的高风险操作交还人工
