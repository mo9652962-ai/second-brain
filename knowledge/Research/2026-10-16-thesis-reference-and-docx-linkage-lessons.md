---
tags: [academic, citation, docx, wps, research]
domain: academic
created: 2026-10-16
updated: 2026-10-16
status: adopted
---

# 论文文献可获取性与 DOCX 引用链接实战复盘

## 本轮案例

对《OPPO 手机在柬埔寨市场营销策略研究》开题报告核查第 15 条来源时，原候选机构报告页面真实，但公开入口要求申请报告，不满足导师无需付费/申请即可复核的使用目标。替代为 MRTS Consulting 2022 年柬埔寨手机品牌考虑度调查页面，样本 468。它只可支持“受访者考虑购买某品牌”的历史意向描述，不能推出实际销量、保有量或市场份额。来源：[MRTS Consulting 柬埔寨手机品牌意向调查](https://mrtsconsulting.com/news/which-smartphone-brand-are-you-considering-the-most-to-buy-next/)。需要市场份额时必须换销量/出货量等直接数据。

同份 DOCX 的技术验证：Word COM 统计 10 页、76 个链接（15 个外部、61 个内部）；LibreOffice 重新渲染为 13 页。document.xml 没有显式 w:hyperlink，但 Word 仍识别链接，因为链接存为 HYPERLINK 复杂字段。Hyperlink 样式内部 ID 是 22，显示名称才是 Hyperlink；按样式名称找到蓝色字体设置后改成黑色。保存关闭阶段发生过 RPC 错误，独立进程重新打开确认文件可用。没有在用户实际 WPS 界面 Ctrl+单击，因此 UI 跳转仍属未验证。

## 可复用工作法

1. 每条文献分开核：身份真伪、具体主张匹配、全文是否免费直达。记录访问门槛，不把题录/摘要当全文可读。
2. 调查购买意向不得写成销量或市场份额；出版年份与调查年份可能不同，必须分开记。
3. 动态网页必须加访问日期；当前页面不证明历史事实。替换来源后连同正文措辞、文内序号、书目条目、正反链接一起更新。
4. DOCX 检查两种链接结构：w:hyperlink 节点与 w:instrText 字段码。COM Follow 只作对象模型证据，真实界面点按要单列。
5. 字色修复检查样式名称、内部 styleId、直接 Run 格式和已访问链接样式，完成后查看目标应用渲染。
6. Word、WPS、LibreOffice 分别记页数，不能用一个排版引擎证明另一个引擎版式相同。COM 保存/退出报错要用新进程重开验证。
7. 记录真实查询、独立来源、原文阅读、本地资料和修订循环；不把重复搜索折算成“千轮”。

## 官方技术与规范依据

- Microsoft Word Hyperlink.SubAddress：[官方说明](https://learn.microsoft.com/en-us/office/vba/api/word.hyperlink.subaddress)
- Microsoft Word Bookmarks.Add：[官方说明](https://learn.microsoft.com/en-us/office/vba/api/word.bookmarks.add)
- 国家标准信息公共服务平台：[GB/T 7714-2025](https://std.samr.gov.cn/gb/search/gbDetailedCNF?id=4507EFE13D37CB6AE06397BE0A0A601F)
- PRISMA-S 检索报告清单（仅适用于相应系统综述，不是所有毕业论文的强制要求）：[官方清单](https://www.prisma-statement.org/prisma-search)

## 来源与边界

本地对照了 Codex academic-thesis-engine 的引文核验、交付 QA、WPS 链接防御与避坑规程；OpenClaw Research 的学术索引、学术检索踩坑研究及深度研究 SOP；Hermes 中 academic-paper-writing、paper-writing-workflow、chinese-academic-writing 技能。它们作为流程参考，不等同原始研究证据。官方页面通过直接 HTTP HEAD 返回 200；Web MCP 本轮连接失败。目标 WPS 实际鼠标操作仍待验。
