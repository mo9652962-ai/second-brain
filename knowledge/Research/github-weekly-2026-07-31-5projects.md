---
tags: [research, github, security, skillspector, powertoys]
created: 2026-07-31
status: absorbed
---

# GitHub 本周 5 项目研究笔记（苹果微软齐出手）

> 来源：小黑盒文章 · 2026-07-31 验证 + 落地

## 📊 总览

| # | 项目 | Stars | 决策 | 理由 |
|:-:|------|:---:|:---:|------|
| 1 | **SkillSpector (NVIDIA)** | ~1K | ✅ **已安装并实测** | 技能安全扫描器，扫描我们全部 15 个第三方技能 |
| 2 | anthropics/skills | 165K | ⚪ 已有 | docx/pdf/pptx 技能已覆盖 |
| 3 | apple/container | 48K | ❌ 不适用 | Mac only，sora 是 Windows |
| 4 | PowerToys | 136K | 🟡 建议安装 | Windows 增强，sora 用户可装 |
| 5 | system-prompts-leaks | 42K | 🟡 参考 | 提示词档案，学习用 |

## 🔴 重点：SkillSpector 实测（安全扫描实践）

### 安装
- `py -3.12 -m pip install -e .`（需要 Python 3.12+）
- 遇到 pydantic_core 编译问题 → `pip install --force-reinstall pydantic pydantic-core` 解决
- 注意：当前 python 是 Hermes venv（3.11），要用 `py -3.12` 指定

### 扫描结果（15 个第三方技能）

| 技能 | 分数 | 级别 | 发现 |
|------|:---:|:---:|------|
| ecc-continuous-learning-v2 | **100** | CRITICAL | 24 issues（17 MEDIUM + 7 HIGH） |
| ecc-strategic-compact | 31 | MEDIUM | 2 issues |
| nuwa-skill | 25 | MEDIUM | 3 issues |
| goutoujunshi | 16 | LOW | 0 |
| ecc-agent-self-evaluation | 14 | LOW | 0 |
| ecc-delivery-gate / codebase-onboarding | 7 | LOW | 0 |
| 其余 8 个 | 0 | LOW | 0 |

### 人工核实结论：HIGH/CRITICAL 全部是误报！
- **AS1（读 .claude/ 目录）**：ECC 的设计功能——记忆/上下文管理必须读配置目录，不是越权
- **PE3（凭据访问）**：`/etc/passwd` 出现在**单元测试**里（测试拒绝系统路径的功能），不是真读
- **TM2（链式调用）**：`cd "$PROJECT_DIR"` 是正常 shell 操作
- **SC4（setuptools 漏洞）**：text2cad-cad 的 cadpy 用旧版 setuptools——唯一真实风险（依赖升级即可）

### 关键教训（符合规则 #17 评估器校准）
1. SkillSpector 是**有价值的初筛工具**——10 秒扫完一个技能，0 分技能可信
2. **HIGH/CRITICAL 必须人工核实**——静态扫描把正常功能代码误报为风险
3. 真实威胁特征：**主动外传数据（requests.post 到外部）+ 混淆代码（base64 隐藏意图）+ 越权删除**——这三个特征 SkillSpector 标记的才是真危险
4. 建议：导入第三方技能前用 SkillSpector --no-llm 快速初筛，HIGH 人工看代码

## 🟡 其余项目评估

### PowerToys（建议安装）
- 30+ 工具：FancyZones 分屏/PowerToys Run 搜索/Text Extractor 文本提取/Color Picker
- 对 sora 的 Windows 10 直接可用，winget 安装
- 待用户确认后安装（涉及系统级安装）

### system-prompts-leaks（学习参考）
- 42K★，CC0，14 厂商 100+ 提示词
- 价值：理解大厂提示词设计（行为总则/搜索优先/拒答处理/工具 prompt）
- 含 Hermes 自己的提示词（Misc/hermes.md）——学习参考
- 不克隆（仓库大），需要时在线查阅

### anthropics/skills（已有覆盖）
- 165K★ 官方技能仓库，docx/pdf/pptx/xlsx 文档技能
- 我们的 docx/pdf/pptx/xlsx 技能已覆盖同样功能

### apple/container（不适用）
- 48K★ 苹果官方，macOS 26 + Apple silicon only
- sora 是 Windows 10 → 不适用，存档

## 结论
- **SkillSpector 是本轮最大落地**——给"第三方技能安全"提供了可执行方案
- 15 个技能扫描完成，0 个真实恶意，2 个需注意（ECC 功能代码多 + cadpy 依赖旧）
- 教训：静态扫描是初筛不是判决，人工核实是关键（规则 #17 印证）

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
