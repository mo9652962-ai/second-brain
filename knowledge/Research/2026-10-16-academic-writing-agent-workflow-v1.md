---
tags: [academic, thesis, evidence, workflow]
domain: research
created: 2026-10-16
updated: 2026-10-16
status: adopted
---

# 学术写作智能体工作流与证据账本 v1.0

## 定位

将选题、开题、论文写作、文献核验、方法审查、格式和交付变成可追溯流程。此文是可执行工作规范，不宣称已运行多 Agent，也不承诺录用、通过或检测结果。

## 本地落地

- 可执行技能规程：[academic-writing-agent-workflow.md](C:/Users/31954/.agents/skills/academic-thesis-engine/references/academic-writing-agent-workflow.md)
- 技能入口：[academic-thesis-engine/SKILL.md](C:/Users/31954/.agents/skills/academic-thesis-engine/SKILL.md)
- 相关既有知识：[[2026-10-16-douyin-academic-tools-audit]]、[[2026-10-16-reference-metadata-audit-upgrade]]、[[2026-10-16-academic-writing-ecosystem-evaluation]]

## 核心升级

1. **来源三分**：书目身份、全文可访问性、主张支持关系分别记录。`content_verified`、`metadata_verified_only`、`pending_evidence`、`conflict_or_misuse` 不可混为单一真伪标签。
2. **证据账本**：重要论断记录 claim_id、来源版本、页/表/节定位、支持关系、适用对象和时间、局限/反证及处理决定。
3. **阶段门**：规范与边界→选题/研究设计→文献核验→主张综合→方法与数据→写作/引用→反方审查→格式与可见交付→诚信披露。
4. **按设计审查**：定量、定性、混合、案例、设计实践、综述采用各自适配的质量问题，不机械套用通用指标。
5. **阻断项优先**：证据造假/不可追溯、方法不适配、伦理/权限风险、严重格式缺项均阻断；内部分数不能抵消阻断问题。
6. **审查身份诚实**：同一执行者的多轮检查是自检；只有实际独立审阅者/代理完成才称独立复核。没有代理时不虚构多 Agent。
7. **格式遵循适用层级**：学校/学院当届模板优先；标准登记表记录版本、发布日期/生效日期、范围和查阅日期。文档结构、COM、目标软件界面操作是不同验证层级。
8. **学术诚信**：用户对论文负责；不得编造数据、来源、审批、检测或作者贡献；不承诺规避 AI 检测或保证接收。

## 已核验的官方依据（2026-10-16）

- 国家标准平台：[GB/T 7714-2025](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C6CE52E55AC09B9C79A20AEA77CEDD14)，实施日期 2026-07-01；实际论文格式仍先看学校/期刊当届要求。
- 国家标准平台：[GB/T 7713.2-2022](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0B963916637B8F34B295FCF4A51A1BE5)，学术论文编写要求，适用范围需核任务类型。
- [Zotero 文字处理器集成说明](https://www.zotero.org/support/word_processor_integration)列 Word、LibreOffice、Google Docs，未列 WPS；技能因此把 WPS 插件兼容标为需目标环境实测。
- [ICMJE AI recommendations](https://www.icmje.org/recommendations/browse/artificial-intelligence/)强调人类作者对准确性、完整性和诚信负责；学校/期刊 AI 规则另行核验。

## 使用限制

- “研究轮数”只按可审计日志计数，不能把一次检索或一份草稿描述成“千轮”。
- 元数据正确、DOI 可打开、网页可访问、AI 摘要和搜索结果都不自动证明内容或论断。
- 付费/机构全文不可访问时明确记录访问边界，不以“导师肯定能查到”替代验证。
- 该流程是当前技能版本的工作约定；每次具体任务仍须核目标机构、规范版本和实际原始材料。
