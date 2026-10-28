---
tags: [academic, thesis, reference, crossref]
domain: research
created: 2026-10-16
updated: 2026-10-16
---

# 文献核验流程升级：Crossref 初筛与 OpenAlex/Unpaywall 接口更新

- 日期：2026-10-16
- 对应技能：`academic-thesis-engine` v2.16.0

## 为什么更新

本地 Hermes `academic-paper-writing` 旧版仍将 OpenAlex、Crossref 列作检索源，但没有区分 API 候选结果、书目真实性、全文可读性、版本状态和正文主张匹配；其旧示例也未涵盖 2026-09-18 Unpaywall 关键词搜索接口的退役。因此需要将平台查询从“找到一个 DOI/结果”改为可复核的多层证据流程。

## 外部一手文档核验

- Crossref REST API 可按 DOI 查元数据，也可用书目信息查找候选；其记录来自成员和可信来源提交。无注册公共查询，但需礼貌请求、处理状态码并避免高频访问。
- Crossref 页面说明一些记录有全文访问链接和用途/许可元数据；元数据 API 本身不是全文仓储。
- Crossmark 面向更正、撤稿和其他更新信息；提供了更新线索机制，不等于每篇文章都有完整状态数据。
- OpenAlex 官方说明 `best_oa_location` 代表所选开放版本副本，适合提供线索；仍需打开检查是预印本、作者接受稿或出版版本，并核许可与可访问性。
- Unpaywall 官方 API 文档在 2026-10-16 标明 `/v2/search` 关键词搜索于 2026-09-18 退役，应改用 OpenAlex 搜索。按 DOI 查询 OA 状态的 `/v2/:doi` 不是该关键词接口，二者须分开描述。

## 新增工具与运行验证

新增 `C:\Users\USERNAME\.agents\skills\academic-thesis-engine\scripts\crossref_reference_audit.py`：

- 输入 CSV：`reference_id,title,author,year,doi`。
- 有 DOI 时查该 DOI 的 Crossref 记录；无 DOI 时根据题名/作者/年份找候选。
- 输出题名相似度、候选 DOI、作者、年份、刊名、卷期页和人工复核标记。
- 只用 Python 标准库，无需 API key；每条候选都明确写“元数据候选，不认证真实性/全文/主张匹配”。

验证：编译检查通过；用 Crossref 真实记录 DOI `10.1038/nature12373` 查询成功，返回题名 `Nanometre-scale thermometry in a living cell`；以同一准确题名检索返回题名相似度 `1.000`。输出仍标为 `strong_title_candidate_manual_review`。

## 失败处理/证据上限

- Crossref `not_found`：记“Crossref 未命中”，不得判文献虚假；尤其中文期刊、论文、图书章节和地区性出版物应去期刊/出版社/机构库查原始记录。
- DOI 记录返回：只证明本次 Crossref API 返回了元数据，不证明文章质量、完整性、未撤稿或全文免费。
- OpenAlex/Unpaywall 显示 OA：还要实际打开落地页与全文，记录版本、许可、访问状态；让导师用可用网络重试。
- 文献论断匹配仍需读原文并写页/段/表图位置，确认研究对象、指标、时间和条件。自动字符串相似度不能代替语义判断。
- 用户旧工作中提出的“导师简易查到”应登记为 `公开直达全文 / 仅题录摘要 / 需订阅或申请 / 链接失效` 之一；不可把 DOI 可解析直接标记成可读全文。

## 来源链接

- Crossref REST API：https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- Crossref API 使用与礼仪：https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/
- Crossref 全文链接元数据：https://www.crossref.org/documentation/retrieve-metadata/text-and-data-mining/
- Crossmark：https://www.crossref.org/documentation/crossmark/
- OpenAlex 搜索：https://help.openalex.org/api/searching/
- OpenAlex 版本位置：https://help.openalex.org/data/locations/
- OpenAlex API 认证/额度：https://help.openalex.org/api/authentication/
- Unpaywall API 端点变更：https://unpaywall.org/api

## 本地来源

- OpenClaw：`Research\Academic.md`、上一条“抖音学术工具主张核验”研究记录，以及近期论文引用与 DOCX 连接复盘。
- Hermes：`academic-paper-writing\SKILL.md` 的检索工具章节，仅作技能流程参考；旧信息须按上列当前官方文档校正。
- Codex：`academic-thesis-engine\references\literature-search-and-citation-protocol.md`、`source-access-and-docx-linkage.md`。

## 追加验证与维护备注

- 对有效 DOI、题名检索、无效 DOI 三类样本分别通过：`metadata_returned`、`candidates_returned`（相似度 1.000，仍需人工复核）、`not_found`。DOI-only 行显示“metadata_returned_title_unchecked”，不生成虚假的题名 mismatch。
- 技能 `quick_validate.py` 与 Python 编译检查通过。Windows 默认代码页会让检查器按 GBK 解读 UTF-8 的 SKILL.md；本地使用 UTF-8 模式重跑通过，并移除不被当前校验器接受的顶层 `version` 键，仅保留 `metadata.version`。
- 工具将参考题名、作者和 DOI 发给 Crossref 进行查询；未公开或保密课题先脱敏，不直接上传查询。
