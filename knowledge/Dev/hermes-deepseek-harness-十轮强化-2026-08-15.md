---
tags: [hermes, deepseek-harness, dsh, 联合工作, 千轮强化, 十轮]
type: research
date: 2026-08-15
status: adopted
---

# Hermes × DeepSeek Harness 联合工作十轮强化总报告

> 2026-08-15 · 十轮强化循环（每轮独立角度：搜索引擎研究 + 实战复盘 + 社区交叉验证）
> 完整技能：`hermes-deepseek-harness`（含 SOP + Pitfalls）

## 结论置顶

**联合工作体系从「能用」→「可靠」→「有边界认知」**。十轮产出 30+ 增量发现，其中 3 个实战验证 + 1 个安全红线。

---

## 十轮收获速查

| 轮 | 主题 | 核心发现 |
|:--|:---|:---|
| 1 | 官方集成 | DeepSeek 官方有 Hermes 集成页（推荐 v4-pro）；dsh capability seams 与 Hermes 架构同构（llm/工具/子代理/压缩/token/持久化/web/skills/jobs）；**dsh 用 Exa 搜索同款**；Windows shell=pwsh-local |
| 2 | 插件生态 | **vision_crop 冲突根因=双视觉插件争槽，只能装一个**；dshplugin Indexed/Runtime Verified 预检；层覆盖规则=patch 替换整行不深合并；免费视觉方案 dsh-vision（智谱/Ollama 离线） |
| 3 | ACP 集成 | **Hermes ACP 完整**（持久化 state.db/跨进程恢复/4级审批）vs dsh ACP 弱（仅新会话+committed text）；Buzz 多传输先例=一个 Hermes 多客户端；**resume 重放 bug（#32201/#32202）：编排避免新建会话（8万token 教训）** |
| 4 | Windows 坑 | **乱码根因=ConPTY 系统代码页(GBK936) vs node-pty 固定 UTF-8 解码**；修复=chcp 65001 / pwsh OutputEncoding 无BOM / PYTHONUTF8=1；node-pty Win 不支持 encoding 选项须改 shell 侧 |
| 5 | 模型路由 | dsh Settings→Models 支持 catalog/custom provider + 视觉 input 配置；成本策略=按任务类型路由+有序 fallback；DeepSeek 新模型名 v4-flash/pro（旧别名废弃）；OpenRouter 国内不稳需中转备线 |
| 6 | 记忆持久化 | **mnemon=dsh-mnemon 底层，支持 `mnemon setup --target hermes` 原生集成**，单一 ~/.mnemon 库=跨 agent 共享；Hermes 记忆三层（内置/SessionDB/外部 provider 限1个） |
| 7 | **安全红线** | **dsh 插件轴B无安全设计**（#454 审计：40 攻击路径/!!js 加载期 RCE/后门持久化）；#587：dsh plugin add 无签名校验+boot 期可改 approval=never；#250：loopback approval 自批准；**对策：只装可信插件 + dsh-auto-mode 千万别装 + headless 委派限权 + 审计 cordis.patch.yml 的 !!js** |
| 8 | 子代理编排 | dsh ctx.subagents：inprocess/fork/acp/codex/claude-code/dsh-sdk；官方 codex+claude-code 双 provider（每次新进程新会话）；**多级联合栈=Hermes→dsh→(codex/claude-code)** |
| 9 | 性能上下文 | 模型可见即已记录不变量+Trajectory 回放+缓存命中统计（量子位实测 99%）；ctx.compaction 与 Hermes 同构；**坑 #1453：每工具步重复携带完整上下文无统一预算→长任务 token 高须拆分/手动压缩**；PTC 模式=TS 程序组合省 round trip |
| 10 | **实战验证** | ✅ headless 中文无乱码；✅ 默认 workspace-write fail-closed 安全生效；✅ **`DSH_PERMISSION_MODE=danger-full-access` 官方覆盖→写文件全通**（真实创建+运行 fib.py F1-F10 正确）；⚠️ 路径坑：pwsh 的 /tmp=C:\tmp（git-bash 不同）+ Windows 原生路径 |

---

## 实战验证的 3 个关键结论

1. **headless 委派写文件**：默认 `workspace-write` 沙箱在 Windows 上对绝对路径边界判断有坑（工作区内写文件也触发升级）→ 需要写文件的任务用 `DSH_PERMISSION_MODE=danger-full-access`（官方显式部署覆盖，非安全绕过）
2. **路径必须用 Windows 原生路径**：dsh 用 pwsh，`/tmp` = `C:\tmp`；git-bash 传 `/c/tmp` 给 Windows python 会变 `C:\c\tmp`——委派任务时写死 Windows 路径
3. **headless 纯文本任务最稳**：读文件/推理/回答无需任何权限覆盖，直接跑

---

## 安全红线（最重要）

- **只装可信来源插件**（ModLens/Vision Toolkit/maid-atelier 等知名仓库 OK）
- **dsh-auto-mode 千万别装**（"免审批"=攻击面，等于自废 approval）
- 装新插件后**审计 cordis.patch.yml 的 `!!js` 表达式**（加载期 RCE 向量）
- headless 委派**优先纯文本/读文件**，写文件才用 DSH_PERMISSION_MODE

## 联合工作 SOP（十轮强化终版）

```
1. 任务分配：Hermes 记忆/编排/知识库；dsh 深度编码/批量
2. 上下文对齐：项目共享 AGENTS.md（dsh 原生读取）
3. 委派：export DEEPSEEK_API_KEY && DSH_PERMISSION_MODE(如需写文件) dsh --profile headless "任务"（Windows 原生路径）
4. 验证：Hermes 检查产物（文件存在/测试通过），不轻信自报
5. 预算：官方 key 余额有限；方舟 8/28 重置；长任务拆分避免 #1453 token 膨胀
6. 安全：可信插件白名单 + !!js 审计 + headless 限权
7. 升级：dsh 升级后重跑 headless 冒烟（v0.1 破坏性变更）
```

## 轮 11（追加）：错误处理与容灾

| 发现 | 内容 |
|:---|:---|
| **429 真实含义** | DeepSeek 限流是**并发制**（v4-pro 500 / v4-flash 2500，账号级累加）不是 RPM（Reasonix #1526）|
| **连接重置坑** | 本地代理（FlClash/v2rayN）空闲关闭 SSE 长连接 → reasoner 首 token 间隔断流（非 API 故障）|
| 错误分类 | 408/429/5xx 重试；400/401/402/422 不重试；认证过的 key 临时 401 重试 ≤2；burst_rate 严格预算 2 次；方舟 200 空响应按瞬时故障重试 |
| **中转站排障** | one-api/new-api 把真实原因包在 body → jiyuanlvdong/keylink 排障读 error.message |
| 容灾 SOP | Hermes 链与 dsh 官方 key **错峰使用**（防并发互挤）；429 先查并行再查配额 |

---
*关联：skill `hermes-deepseek-harness` · knowledge/Dev/hermes-deepseek-harness-联合工作-2026-08-15.md · 数据截止 2026-08-15*
