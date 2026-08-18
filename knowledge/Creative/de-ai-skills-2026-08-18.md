# 去 AI 味开源技能研究（2026-08-18 小黑盒帖子 + 千轮研究）

> 来源: 小黑盒「吃太饱骑士」《整理了十个高星开源"去AI味"技能还有心得》
> 已安装: humanizer-zh / stop-slop-zh / ai-flavor-remover → Hermes skills/creative/

## 帖子核心观点

```
① AI 同质化原理: AI = 计算概率最大的回复 → 同质化是必然 = AI 味
② 关键洞察: 「仅拒绝低质量回答」不够
   拒绝 prompt 本身会成为公共上下文 → 新 AI 味（道高一尺魔高一丈）
③ 答案: 去 AI 味最好办法 = 「扮演」+ 私人化角色塑造
   两步: 先排除低质量生成(开源技能) + 然后塑造角色(和 AI 共同沉淀)
   终极: 蒸馏自己（女娲技能 = 实践）
```

## 十项技能生态（GitHub 验证）

| # | 技能 | 仓库 | Star | 定位 | 已装 |
|:---|:---|:---|:---|:---|:---|
| 01 | Humanizer | blader/humanizer | 36.1k | 英文 24 种 AI 痕迹 | ✅ 已有 |
| 02 | Humanizer-zh | op7418/Humanizer-zh | 15.5k | 中文去 AI 腔(抽象→具象+5维评分) | ✅ 本次 |
| 03 | Stop-Slop | hardikpandya/stop-slop | 15.8k | 去套路废话(5维评分<35重写) | ✅ 本次 |
| 04 | Taste-Skill | Leonxlnx/taste-skill | 77.4k | 给 AI 装品味(13个UI子技能) | ✅ 本次 |
| 05 | AI 味去除 | hylarucoder/ai-flavor-remover | 1.1k | 深度清洗(分析→诊断→重写) | ✅ 本次 |
| 06 | 说人话 | MrGeDiao/shuorenhua | 1.1k | 中文改人话 | ✅ 本次 |
| 07 | 女娲 | huashu/nuwa-skill | 30.8k | 蒸馏个人文风/思维DNA | ✅ 已有 |
| 08 | Writing Agent | oaker-io/wewrite | 379 | 公众号全流程(10个模块) | ✅ 本次 |
| 09 | 对比检测 | Hello-SimpleAI/chatgpt-comparison-detection | 1.4k | 检测哪里像 AI(HC3) | ✅ 本次 |
| 10 | De-AI 增强 | OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL | 640 | 提示词源头降 AI 味 | ✅ 本次 |

额外发现: B1lli/remove-ai-flavor-writing-skill（模板壳清理）✅ 本次

## 安装记录（2026-08-18）

```
已装: 10/10 + 1 额外 = 25 个技能（creative 分类 52 个）
  去AI味: humanizer/humanizer-zh/stop-slop/stop-slop-zh/ai-flavor-remover/
         shuorenhua/remove-ai-flavor/chatgpt-comparison-detection/de-AI-writing
  taste-skill: 13 个 UI 品味子技能（gpt-taste/design-taste-frontend 等）
  wewrite: 10 个公众号写作模块（主入口+选题/写作/改写/发布等）
踩坑: 仓库结构不统一(有的SKILL.md在子目录/有的是README) → 需提升到根目录
     wewrite 主技能在清理时被误删 → 重新 clone 恢复
     description 过长会膨胀技能列表 → 全部修成短句
```

## 关键发现

```
① 中文圈是去 AI 味品类主力（Humanizer-zh/nuwa/stop-slop-zh 远超英文）
② 安装方式: npx skills add <repo> 或 git clone 到 skills 目录
③ 中文 AI 味指纹: 套话/排比三件套/名词化/抽象主语/金句收尾/总分总八股
④ 注意: 公文/法律/学术的规范表达不是 AI 味, 保守使用
⑤ 去具体≠编具体: 无真实细节就退回平实陈述, 不许编数据
```

## 已安装技能对比（Hermes skills/creative/）

| 技能 | 用途 | 触发 |
|:---|:---|:---|
| humanizer | 英文去 AI 痕迹 | 英文文本 |
| humanizer-zh | 中文去 AI 腔 | 中文文本润色 |
| stop-slop-zh | 中文套路检测(黑名单+评分) | 任何中文写作 |
| ai-flavor-remover | 深度清洗(结构化输出) | 中文稿件清洗 |
| nuwa-skill | 蒸馏个人文风 | 塑造人设/风格 |

## 工作流建议（交付前过一遍）

```
① 初稿: 正常生成
② stop-slop-zh: 检测套话/排比/金句 → 修
③ humanizer-zh: 抽象→具象, 加真实细节
④ ai-flavor-remover: 深度重写(结构化分析+优化)
⑤ 人工: 添加自己知道的真实细节(最强武器)
```
