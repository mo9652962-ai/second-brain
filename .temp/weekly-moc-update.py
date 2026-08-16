#!/usr/bin/env python3
"""Weekly consolidation: update MOCs, create MOC-Finance, add knowledge-map W34 section, fix INDEX.md.
CRLF-safe: read bytes, operate on text, write back with original newline style.
"""
import pathlib, re

ROOT = pathlib.Path(r"C:/Users/31954/.openclaw/workspace")
NL = "\r\n"  # vault files are CRLF

def read(p):
    return (ROOT / p).read_bytes().decode("utf-8", errors="ignore")

def write(p, text):
    (ROOT / p).write_bytes(text.encode("utf-8"))

def insert_after(text, anchor, block):
    """Insert block after the line containing anchor (first occurrence)."""
    idx = text.find(anchor)
    assert idx >= 0, f"anchor not found: {anchor}"
    line_end = text.find(NL, idx)
    if line_end < 0:
        line_end = len(text)
    return text[:line_end] + NL + block + text[line_end:]

# ---------- 1. MOC-Research ----------
p = "knowledge/Research/MOC-Research.md"
t = read(p)
old_cnt = "**共 135 篇研究笔记** · 最后更新: 2026-08-12（新增：Agent 自进化/技能审计/技能写作最佳实践）"
new_cnt = "**共 141 篇研究笔记** · 最后更新: 2026-08-16（W34：GitHub-Weekly-08-16 / arXiv 08-16 补全 / 研究跟踪器归位）"
assert old_cnt in t, "MOC-Research count line not found"
t = t.replace(old_cnt, new_cnt)
# append W34 links right after "## 其他" heading
anchor = "## 其他"
w34 = NL.join([
    "",
    "## 🆕 W34 新增补链（2026-08-16 周度整理）",
    "",
    "- [[GitHub-Weekly-2026-08-16]] — W34 GitHub 热榜",
    "- [[arxiv-2026-08-16-agent-llm]] — arXiv 08-16 速览（08-13 池补全 15 篇）",
    "- [[charm-graph-transfer]] — CHARM 多模态图谱跟踪（归位自 research/trackers）",
    "- [[kutie-context-injection]] — KuTIE 上下文跟踪（归位自 research/trackers）",
    "- [[long-term-model-systems]] — 模型体系三件套跟踪（归位自 research/trackers）",
    "- [[三角洲干员明天过后转场教程研究-2026-08-14]] — 剪映转场教程研究（自 Hardware 归位）",
    "",
    "## 其他",
])
t = t.replace(anchor, w34, 1)
write(p, t)
print("MOC-Research updated")

# ---------- 2. MOC-Dev ----------
p = "knowledge/Dev/MOC-Dev.md"
t = read(p)
dev_w34 = NL.join([
    "",
    "## 🆕 W34 新增（08-14 ~ 08-16）",
    "",
    "- [[knowledge/Dev/OpenGameAgent-架构拆解-对标dsh-2026-08-15|OpenGameAgent 架构拆解]] — 对标 dsh",
    "- [[knowledge/Dev/Token节省千轮研究-2026-08-14|Token 节省千轮研究]] — 成本优化",
    "- [[knowledge/Dev/agentscope-小君AI测评-千轮研究-2026-08-15|AgentScope 小君 AI 测评]] — 千轮研究",
    "- [[knowledge/Dev/agentscope-架构参考-PawBench-2026-08-15|AgentScope 架构参考]] — PawBench",
    "- [[knowledge/Dev/agentscope-深度测试评估-2026-08-15|AgentScope 深度测试评估]]",
    "- [[knowledge/Dev/agentscope-部署测试-2026-08-15|AgentScope 部署测试]]",
    "- [[knowledge/Dev/ai测评-内容素材库-2026-08|AI 测评内容素材库]] — 2026-08",
    "- [[knowledge/Dev/内容-小君AI测评测评文大纲-2026-08-15|小君 AI 测评文大纲]]",
    "- [[knowledge/Dev/hermes-deepseek-harness-十轮强化-2026-08-15|harness 十轮强化]]",
    "- [[knowledge/Dev/hermes-deepseek-harness-联合工作-2026-08-15|harness 联合工作]]",
    "- [[knowledge/Dev/k-soul-persona-2026-08-15|k-soul-persona]] — 人设迭代",
    "- [[knowledge/Dev/墨题-P0错题AI诊断设计稿-2026-08-15|墨题 P0 错题 AI 诊断设计稿]]",
    "- [[knowledge/Dev/墨题-P1-AI服务层架构设计-2026-08-15|墨题 P1 AI 服务层架构设计]]",
    "- [[knowledge/Dev/墨题-借鉴研究-career-ops等-2026-08-15|墨题借鉴研究]] — career-ops 等",
    "- [[knowledge/Dev/模型速查-2026-08|模型速查]] — 2026-08",
    "- [[knowledge/Dev/prime-agent-rlm-2026-08-14|Prime Agent RLM]] — W33 热榜冠军",
    "- [[knowledge/Dev/semantica-graph-native-2026-08-14|Semantica 图原生]] — PROV-O",
    "- [[knowledge/Dev/switchyard-llm-routing-2026-08-14|Switchyard 路由网关]]",
    "- [[knowledge/Dev/agent-skills-addyosmani-2026-08-14|addyosmani agent-skills]]",
    "- [[knowledge/Dev/cloudflare-computer-2026-08-14|Cloudflare Computer 沙箱]]",
    "",
])
t = t.rstrip() + NL + dev_w34
write(p, t)
print("MOC-Dev updated")

# ---------- 3. MOC-Hardware ----------
p = "knowledge/Hardware/MOC-Hardware.md"
t = read(p)
hw_w34 = NL.join([
    "",
    "## 🆕 W34 新增补链（2026-08-16 周度整理）",
    "",
    "- [[knowledge/Hardware/USB-UART转换器设计复盘-2026-08-08|USB-UART 转换器设计复盘]]",
    "- [[knowledge/Hardware/ai-frontend-design-sites|AI 前端设计站点]]",
    "- [[knowledge/Hardware/ai-resume-prompt|AI 简历 Prompt]]",
    "",
])
t = t.rstrip() + NL + hw_w34
write(p, t)
print("MOC-Hardware updated")

# ---------- 4. MOC-Productivity ----------
p = "knowledge/Productivity/MOC-Productivity.md"
t = read(p)
prod_w34 = NL.join([
    "",
    "## 🆕 W34 新增补链（2026-08-16 周度整理）",
    "",
    "- [[knowledge/Productivity/token-usage-report-20260802|Token 用量报告 08-02]]",
    "- [[knowledge/Productivity/token-usage-report-20260814|Token 用量报告 08-14]] — W33 成本根因闭环",
    "- [[knowledge/Productivity/vault-health-baseline|Vault 健康基线]]",
    "- [[knowledge/Productivity/workbuddy-bluebook|WorkBuddy 蓝皮书]]",
    "",
])
t = t.rstrip() + NL + prod_w34
write(p, t)
print("MOC-Productivity updated")

# ---------- 5. MOC-Finance (create) ----------
fin = NL.join([
    "---",
    "tags: [MOC, finance, 股票, 分析]",
    "domain: Finance",
    "created: 2026-08-16",
    "---",
    "",
    "# 📈 金融域 — 股票分析",
    "",
    "> 🏠 [[HOME]] | 🗺️ [[knowledge/knowledge-map|知识地图]]",
    "> 每日 18:00 cron 自动生成（akshare → DeepSeek → 本域）",
    "",
    "## 📊 每日股票分析",
    "",
    "- [[knowledge/Finance/每日股票分析-2026-08-15|每日股票分析 08-15]] — 首期（茅台/宁德/比亚迪/中际旭创/东财）",
    "",
    "---",
    "*MOC 节点 — Finance 域索引（2026-08-16 周度整理创建）*",
    "",
])
write("knowledge/Finance/MOC-Finance.md", fin)
print("MOC-Finance created")

# ---------- 6. knowledge-map.md W34 section ----------
p = "knowledge/knowledge-map.md"
t = read(p)
w34_block = NL.join([
    "",
    "## 🆕 W34 新增速览（2026-08-15 ~ 08-16）",
    "",
    "> 本周主线：知识域收敛 10→7（08-15 refactor）+ AgentScope 评测资产放量 + 墨题 P0/P1 设计 + harness 十轮强化 + 闲鱼 8/17 决策倒计时。整理报告见 [[../memory/2026/08/weekly-2026-08-16|W34 周度整理]]。",
    "",
    "### 各域本周新增",
    "",
    "| 域 | 新增重点 | 入口 |",
    "|:---|:---------|:-----|",
    "| 🤖 Dev | **AgentScope 评测放量**（小君 AI 测评/架构参考 PawBench/深度测试/部署测试 4 篇）+ AI 测评内容素材库 + harness 十轮强化/联合工作 + 墨题 P0/P1 设计稿 + Token 节省千轮研究 | [[knowledge/Dev/agentscope-小君AI测评-千轮研究-2026-08-15]] · [[knowledge/Dev/墨题-P0错题AI诊断设计稿-2026-08-15]] |",
    "| 🔬 Research | GitHub-Weekly-08-16 + arXiv 08-16 补全 15 篇（SkillEvo/CrEST/Faraday）+ 研究跟踪器归位 ×3 + 剪映转场教程归位 | [[knowledge/Research/GitHub-Weekly-2026-08-16]] · [[knowledge/Research/arxiv-2026-08-16-agent-llm]] |",
    "| 🧠 人设 | k-soul-persona 2026-08-15 迭代（浓亲密度 + 负面情绪许可 + 口头禅 5 条） | [[knowledge/Dev/k-soul-persona-2026-08-15]] |",
    "| 📈 Finance | 每日股票分析 cron 落地（akshare → DeepSeek → 知识库） | [[knowledge/Finance/每日股票分析-2026-08-15]] |",
    "| 🏗️ 结构 | 知识域 10→7 收敛（Academic→Research、AI→Dev、Design→Hardware）+ dreaming 压平 + 全仓引用修复 | [[knowledge/Cross-Domain]] |",
    "",
    "### 本周关键主题",
    "",
    "1. **知识域收敛 10→7** — 08-15 大型 refactor：49 篇迁移、MOC 合并、dreaming 三层压平（light/rem/deep → 前缀命名）",
    "2. **AgentScope 评测矩阵** — 小君 AI 千轮测评 + PawBench 架构参考 + 深度测试 + 部署测试四连，沉淀 AI 测评内容素材库",
    "3. **墨题 P0/P1 设计** — 错题 AI 诊断设计稿（12 分类归因）+ AI 服务层架构（3 库模式/DPAPI/降级链）+ career-ops 借鉴",
    "4. **闲鱼 8/17 决策** — P0 上架连续顺延至 8/17 最后期限，素材已 100% 就绪",
    "5. **股票分析 cron 上线** — 每日 18:00 akshare 采集 → DeepSeek 决策报告 → knowledge/Finance/",
    "",
    "---",
    "",
])
anchor = "## ① 💻 工程与开发"
assert anchor in t, "knowledge-map anchor not found"
t = t.replace(anchor, w34_block + anchor, 1)
# update header date line
t = t.replace(
    "最后更新: 2026-08-16（知识链分支整合 10→7 域：Academic→Research、AI→Dev、Design→Hardware，dreaming 压平））",
    "最后更新: 2026-08-16（W34 周度整理：MOC 补链 + Finance MOC 创建 + memory 归位）",
)
write(p, t)
print("knowledge-map updated")

# ---------- 7. INDEX.md ASCII diagram fix ----------
p = "INDEX.md"
t = read(p)
t = t.replace(
    "      │ 📚 知识域  │   │ 📋 项目      │   │ 🧩 系统    │",
    "      │ 📚 知识域  │   │ 📋 项目      │   │ 🧩 系统    │",
)
t = t.replace(
    "      │ 14 个子域  │   │ projects/    │   │ 配置/脚本  │",
    "      │ 7 个子域   │   │ projects/    │   │ 配置/脚本  │",
)
t = t.replace(
    "      │ 622+ 笔记  │   │ 知识点       │   │ 文档/模板  │",
    "      │ 690+ 笔记  │   │ 知识点       │   │ 文档/模板  │",
)
t = t.replace("knowledge/ 14 域                system/ docs/ scripts/", "knowledge/ 7 域                 system/ docs/ scripts/")
t = t.replace("updated: 2026-08-08", "updated: 2026-08-16")
write(p, t)
print("INDEX updated")

print("\nALL DONE")
