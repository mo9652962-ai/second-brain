---
tags: [python, dev, toolchain, knowledge-map]
domain: Dev
created: 2026-07-30
updated: 2026-07-30
---

# 🐍 Python 生态速览

> 本库实际使用的 Python 工具链速查。不是全面教程，是**日常工作中真实在用**的东西。

## 包管理

| 工具 | 本库状态 | 说明 |
|------|---------|------|
| **uv** | ✅ 主力 v0.11.32 | Rust 编写的包管理器，比 pip 快 8-10x。负责：创建 venv、安装依赖、运行脚本 |
| pip | ✅ 备用 | uv 兼容模式 `uv pip install` |
| venv | ✅ `.venv/` | 虚拟环境位于仓库根目录 |

**日常命令**：
```bash
uv venv                          # 创建虚拟环境
uv pip install <pkg>             # 安装包
uv run python <script.py>        # 无需激活 venv，直接运行
uv pip install -r requirements.txt  # 批量安装
```

## 核心依赖（实际使用）

```python
python-docx       # 练习册生成（核心产出）
pillow            # 图片处理（OCR相关）
pytesseract       # OCR 文字识别
markitdown        # 文件转 Markdown（v0.1.6 已安装）
```

## 脚本工具

| 脚本 | 功能 | 技术栈 |
|------|------|--------|
| `generate_math_workbook_standard.py` | 数学练习册生成器 | python-docx, OOP Config |
| `memory_tracker.py` | 记忆贡献度追踪 | json, pathlib |
| `memory_dashboard.py` | 可视化仪表盘生成 | http.server, Chart.js |
| `github_treasure_hunt.py` | GitHub 宝藏挖掘 | gh CLI, markdown |

## Hermes Agent Python 集成

Hermes 目前使用 **opencode-go** 作为主力 provider，Python 环境主要用于：
- 脚本执行（`uv run python scripts/xxx.py`）
- 练习册/docx 生成
- 自定义工具（memory_tracker/dashboard）

[[MOC-Dev]] · [[knowledge/AI/hermes-agent-ecosystem|Hermes 工具生态]]
