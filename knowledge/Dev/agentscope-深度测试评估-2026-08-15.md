---
tags: [agentscope, 小君AI测评, 测试评估, bug报告, 千轮研究]
type: test-report
date: 2026-08-15
status: adopted
---

# AgentScope（小君AI测评）深度测试评估报告

> 2026-08-15 · 千轮测试：API 边界 + 数据层 + 流程异常 + 代码审查
> 环境：localhost:3000 dev 实例 + DeepSeek 连接 + 真实评估

## 结论置顶

**核心功能（评估）可用，但存在 1 个「功能 100% 必挂」的严重 bug + 3 个中度问题 + 若干轻量问题**。最讽刺的是：README 宣称的「JSON 导入」功能从未成功过（任何用户导入必失败）。

## Bug 清单（按严重度）

### 🔴 严重：知识库 JSON 导入 100% 必挂
- **症状**：POST /api/knowledge/import（multipart 上传）任何合法条目都返回 400「导入失败，请上传合法 JSON 文件」
- **根因**：`upsertKnowledgeItem`（knowledgeBaseService.ts:158）SQL 引用 `@sourceType` 参数，但 import route（import/route.ts:30）构造的 entry **没传 sourceType 字段** → `Missing named parameter "sourceType"` → catch → 400
- **佐证**：sync 服务自己构造 sourceType（knowledgeSyncService.ts:16）所以 sync 正常；用户导入路径必崩
- **影响**：README 宣称的「JSON 导入」核心功能完全不可用

### 🟠 中：报告 GitHub 参考与项目不匹配
- **症状**：「考勤打卡小程序」评估 → GitHub 参考全是电商仓库（commerce 14K★ / saas-starter / vendure / saas-starter-kite）
- **根因**：curated 列表按 kind 硬编码（web → 电商仓库），isRelevant 过滤未真正按项目语义筛选
- **影响**：报告「已核验参考」与项目无关，误导用户

### 🟠 中：评估链路无降级 + 不稳定
- **症状**：正常连接偶发 `INVALID_JSON`「DeepSeek 连续两次无法生成有效搜索计划，请重试」→ 整单失败
- **根因**：generateDeepSeekSearchPlan 两次 parse 失败即抛错，无降级（不生成 plan 也能评估，plan 只是搜索提示）
- **佐证**：同样连接 3 次评估 2 成功 1 失败；单次评估 55 秒（用户体验差）

### 🟠 中：输入校验缺失 + 错误信息误导
- 空 idea 评估 → 502 INVALID_JSON（应 400「项目描述不能为空」）
- 空 body → 裸 `Unexpected end of JSON input`（无错误码）
- 导入失败统一「请上传合法 JSON 文件」（实际原因可能是内部错误/敏感字段/格式）
- 非法 JSON body → provider_and_api_key_required（误导）

### 🟠 中：报告与知识库共用 SQLite
- project_reports 和 knowledge_items 同在 `.agentscope/knowledge.sqlite`
- **重置知识库 = 删历史报告**；且 database() 用 process.cwd()（不同 cwd 启动状态分裂）

### 🟡 轻量问题
| 问题 | 详情 |
|:---|:---|
| 超长 API key 无校验 | 50K key 被接受（201）|
| knowledge/sync 忽略 body | 非法 sources 参数照跑默认同步 |
| GitHub 搜索失败静默空 | 无 token 401 时不报错，报告缺 GitHub 参考无提示 |
| 无 error.tsx/not-found.tsx | 404 页面返回 200 空壳 |
| 连接持久化依赖 DATABASE_ENCRYPTION_KEY | 不配则重启丢连接（已解决：配置即可）|

## 已验证正常的部分

- ✅ 评估主流程（真实 DeepSeek 分析，55s 出 54KB 报告）
- ✅ 无 Provider / selected 不存在 → 503 明确失败（README 承诺遵守）
- ✅ 敏感字段导入拦截（api_key/token 正则检测）
- ✅ sourceUrl 协议白名单（防 javascript:）
- ✅ .gitignore 覆盖 .env.*/.agentscope（无泄露）
- ✅ 报告存储 SQLite（可查历史）
- ✅ 并发导入不会写坏数据库（但都会被 schema 挡）
- ✅ DeepSeek 模型名官方 ID 校验（test 接口）

## 修复建议（给作者的 PR 素材）

1. **import route**：safe 构造时补 `sourceType: "community"`（或改 upsert 默认值）——1 行修复
2. **输入校验**：analyze 前校验 idea 非空 → 400
3. **curated 按 kind 硬编码**：改为「curated + 项目语义关键词」双通道，或让 AI 从候选里选相关
4. **searchPlan 降级**：plan 失败不阻断评估（用默认 queries 或空 plan）
5. **错误信息**：导入失败区分「格式错误/敏感字段/内部错误」
6. **数据库拆分**：reportStore 单独库或加表前缀

## 测试方法备忘

- 导入是 multipart（formData + file），不是 JSON body
- schema 校验严格（id/name/kind/summary/capabilities/tags/stack/platforms/sourceUrl 全要）
- 坏连接测试：selectedConnectionId 指向不存在 → 503；但会 fallback 到默认连接
- git-bash 中文 JSON 会 GBK 乱码 → 用 Python requests（UTF-8 安全）
