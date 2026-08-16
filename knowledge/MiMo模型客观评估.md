# MiMo-V2.5 系列客观评估（2026-08 千轮研究）

> 来源：mimo.xiaomi.com 官方 + HuggingFace + CSDN/TRAE/今日头条实测 + 多源 benchmark 交叉验证
> 一句话：**MiMo-V2.5 是小米开源的全模态/Agent 旗舰，定价恰好 = DeepSeek 涨价前的官方价（¥1/¥2、¥3/¥6），是目前 DeepSeek 涨价后最直接的平替**——但数学推理和缓存稳定性是短板。

## 一、模型家族速览

| 模型 | 总参/激活 | 上下文 | 模态 | 定位 | 开源 |
|:---|:---|:---|:---|:---|:---|
| **MiMo-V2.5-Pro** | 1.02T / 42B MoE | 1M | 文本 | 复杂任务、Agent、Coding | ✅ MIT |
| **MiMo-V2.5** | 310B / 15B MoE | 1M | **原生全模态**（文/图/视频/音频）| 多模态理解 + Agent | ✅ MIT |
| MiMo-V2.5-ASR | — | — | 音频 | 语音识别 | ✅ |

- V2.5 系列 2026-04-23 发布，V2 系列已 2026-06-30 下线
- 48T tokens 预训练（FP8）、混合 SWA 注意力、3 层 MTP 多 token 预测（提速 3 倍）
- **MIT 协议全量开源**（含 Base），SGLang/vLLM Day0 适配，可自部署

## 二、能力评估（benchmark + 第三方实测交叉）

### Benchmark（开源模型排名）
| 评测 | MiMo-V2.5-Pro | DeepSeek V4-Pro | 结论 |
|:---|:---|:---|:---|
| AA Intelligence Index | **54（开源并列第1）** | 52（第2）| MiMo 略胜 |
| ClawEval（长程 Agent）| **63.8** | 59.8 | MiMo 胜 |
| τ³-bench（跨任务协作）| **72.9** | 71.8 | MiMo 胜 |
| SWE-bench Pro（真实 Issue 修复）| **57.2** | 55.4 | MiMo 胜 |
| SWE-bench Verified | 78.9 | **80.6** | DS 胜 |
| Terminal-Bench 2.0 | **68.4** | 67.9 | MiMo 微胜 |
| Codeforces（算法竞赛）| — | **3206（人类第23名）** | DS 断层领先 |

### 第三方实测（OWenT 编码测试 / TRAE 社区 / 头条 6 场景）
- ✅ **写新项目最快最稳**（mini Redis 场景满分）、工程代码稳定性好、长上下文一致性最好
- ✅ 综合强度：DS V4-Pro > MiMo V2.5-Pro > DS V4-flash（TRAE 社区共识）
- ✅ 性价比之王：能力接近第一梯队，价格 = DS 原价
- ⚠️ **数学/算法推理明显不如 DS Pro**（推导深度不足、爱省略步骤）
- ⚠️ **降价 + 重置用量后负载激增**：吞吐降 5-8 倍、偶发降智（TRAE 社区 2026-06 反馈）
- ⚠️ 上下文压缩后幻觉变多（长任务第二轮问题率上升）

## 三、💰 价格对比（关键！）

### 官方定价（2026-05-27 永久降价后，最高降 99%）
| 模型 | 输入（命中缓存）| 输入（未命中）| 输出 |
|:---|:---|:---|:---|
| `mimo-v2.5-pro` | ¥0.025 | ¥3.00 | ¥6.00 |
| `mimo-v2.5` | ¥0.02 | ¥1.00 | ¥2.00 |

### 与 DeepSeek 对比（¥/百万 token）
| 模型 | 输入/输出 | 对比 |
|:---|:---|:---|
| **mimo-v2.5** | ¥1/¥2 | **= DS flash 涨价前官方价**；比涨价后高峰（¥3/¥9）便宜 3-4.5 倍 |
| **mimo-v2.5-pro** | ¥3/¥6 | **= DS pro 涨价前官方价**；比涨价后高峰（¥9/¥27）便宜 3-4.5 倍 |
| DeepSeek flash 新价 | 高峰 ¥3/¥9 | — |
| DeepSeek pro 新价 | 高峰 ¥9/¥27 | — |
| SiliconFlow DS flash | ¥1/¥2 | 同价但需实名+可能跟进涨价 |

**结论：DeepSeek 涨价后，MiMo 官方价就是「涨价前的 DeepSeek 价」——平替最直接的选项。**

## 四、生态与接入

- **OpenAI 兼容**：`https://api.xiaomimimo.com/v1`（sk- key）
- **Anthropic 兼容**：`https://api.xiaomimimo.com/anthropic`
- **Token Plan 订阅**：包月/包年（token-plan-cn.xiaomimimo.com，tp- key），高用量更划算
- **官方明确支持 Hermes Agent** 接入（工具列表含 Hermes Agent/Claude Code/Cline）
- 支持联网搜索插件（国内 ¥16/1000 次）
- 中转站也有（Tokeness mimo-v2.5 ¥0.59/¥1.18——比官方还便宜，但口碑待验）

## 五、客观短板（不吹不黑）

1. **数学/竞赛推理**：明显不如 DeepSeek V4-Pro（Codeforces 3206 vs 未上榜）
2. **缓存命中率波动**：早期实测 40%（DeepSeek 12h 100%）；官方 6 月发布推理优化报告称已达 93%（自研 GCache），但需实测定论
3. **负载高峰期降智**：降价后用户涌入，吞吐下降 5-8 倍、偶发降智——**建议错峰使用**
4. **生态成熟度**：比 DeepSeek 的 Codex/Responses API 适配晚，Agent 工具链兼容还在完善

## 六、🎯 给 sora 的落地建议

| 场景 | 建议 |
|:---|:---|
| **Hermes 主力（替代 flash）** | 可配 `custom:mimo`（api.xiaomimimo.com/v1）mimo-v2.5——同价、Agent 更强、还是全模态；**先小额试用观察缓存命中率** |
| **dsh 编码委派** | mimo-v2.5-pro 适合——ClawEval 63.8 超 DS Pro，工程代码稳定 |
| **复杂数学/竞赛** | 仍留 DeepSeek V4-Pro（Codeforces 断层领先）|
| **多模态任务** | mimo-v2.5 是唯一免费层级的原生全模态开源模型（图/视频/音频理解）——比 qwen-vl 便宜的替代 |
| **自部署** | MIT 开源可自托管（8GB 卡跑不动 42B 激活，需要多卡/云端）|

### 待验证清单（接入前）
1. 注册 mimo.mi.com → 创建 API Key → curl 实测 mimo-v2.5 身份/标记复述（注水测试）
2. 实测缓存命中率（usage.prompt_cache_hit_tokens）
3. 高峰 vs 空闲时段吞吐对比（避峰）
4. Hermes fallback 链加 MiMo 做第二兜底
