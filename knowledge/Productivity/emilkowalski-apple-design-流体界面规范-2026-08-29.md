# emilkowalski/skills — Apple Design 流体界面规范（Web 落地）· 实证评估

> 来源：抖音「赛博山姆」《苹果设计规则 skill 优化网页细节》→ 溯源到 `emilkowalski/skills` 仓库（GitHub 33.3k★，MIT，2026-08 更新）。
> 作者 Emil Kowalski：前 Vercel / Linear 设计工程师，`skills.sh` 作者，`animations.dev` 站长。
> 2026-08-29 实证研究入库。

## 一句话定位

把 Apple WWDC 设计演讲（核心是 *Designing Fluid Interfaces* WWDC 2018）**翻译成 Web 可落地的动效手感规范**——不是教你怎么设计得"像苹果"，而是让界面**像真实物体一样可被掌控**：即时响应、连续运动、携带动量、边界受阻、中途可改向。

**核心信条**：界面要有生命力 = 动画从当前屏幕值出发、继承用户速度、向前投影动量、任意时刻可被抓取并反向。

## 仓库全景（12 个 skill）

| Skill | 作用 |
|:---|:---|
| **apple-design** | 苹果设计原则 + 流体动效 → Web（本次主题） |
| emil-design-eng | 主 skill：动画为主 + 设计建议 |
| animate | 从零构建动画：选对曲线/时长/属性 |
| review-animations | 严格审查动画质量 |
| improve-animations | 审计全代码库动画，产出可执行计划 |
| find-animation-opportunities | 找该动的地方 + **明确哪些不该动** |
| animation-vocabulary | 用正确的词告诉 AI 你要什么动画 |
| prototype | 同一 UI 多个版本切换对比 |
| pick-ui-library | 选库（不 hand-roll toast 之类） |
| ask-sonner | Sonner toast 库指南 |
| animate-expo / write-swift | React Native / Swift 专用 |

## 17 条原则精要（Web 可落地）

### 动效手感（1-11）
1. **Response — 消灭延迟**：pointer-down 即刻反馈，不等 click/释放；交互过程中 1:1 连续更新，不只在结束时
2. **Direct manipulation — 1:1 跟踪**：Pointer Events + `setPointerCapture`；尊重抓取偏移；记录位置/时间历史算速度
3. **Interruptibility — 唯一最重要的原则**：动画任意时刻可被抓取反向；从**当前屏幕值**（presentation）起手而非目标值；手势驱动**别用 CSS transition/@keyframes**（弹簧天然从当前值起）；反向时混合速度不硬切（避免"砖墙"）
4. **Behavior over animation — 用弹簧**：固定时长动画不能响应新输入，弹簧可以。`damping 1.0` = 临界阻尼无过冲（默认）；`~0.8` = 有弹性（仅在手势带动量时）。Apple 实值：Move `1.0/0.4`、Rotation `0.8/0.4`、Drawer `0.8/0.3`
5. **Velocity handoff**：手势结束动画**从手指的精确速度继续**。相对速度 = `手势速度/(目标−当前)`
6. **Momentum projection**：不吸附释放点最近边界，用速度投影落点。苹果精确公式 `(v/1000)·d/(1−d)`，`d≈0.998` 正常滚动、`0.99` 更爽快（Vaul/Embla 同款）
7. **Spatial consistency**：进出同路径（右侧滑入必右侧滑出）；弹出层 `transform-origin` 锚定触发元素；可逆过渡镜像缓动
8. **Hint in direction**：中间帧指向结果（控制中心模块"朝手指生长"）
9. **Rubber-banding**：边界渐进阻力不硬停，公式 `(overshoot·dim·c)/(dim+c·|overshoot|)`，`c=0.55`
10. **Gesture 细节**：tap 按下即高亮、抬手确认，~10px 命中区；拖拽 ~10px 阈值后才 1:1；并行识别所有手势再淘汰
11. **Frame-level smoothness**：只动画 `transform`/`opacity`（合成器友好）；`will-change` 提示；超快运动用轻微拉伸编码速度

### 材质与多模态（12-13）
12. **Materials & depth**：`backdrop-filter: blur(20px) saturate(180%)` 半透明浮层；**重材质分结构、轻材质引注意**；绝不在另一层浅透明上叠浅透明；聚焦用遮罩压背景、平行面板用透明+偏移**不打断流程**；模糊/缩放一起动画（"材质到达"而非淡入）；浮动 chrome 与内容交汇处用渐变遮罩而非 1px 硬分隔线
13. **Multimodal feedback**：因果（触发在真实事件上）/和谐（视觉+声音+触觉**同一帧**）/效用（只在值得处加）

### 无障碍与排版（14-15）
14. **Reduced motion**：`prefers-reduced-motion: reduce` → 换短不透明度交叉淡入；`prefers-reduced-transparency: reduce` → 透明变实；`prefers-contrast: more` → 实底+对比边框
15. **Typography**：字距随字号（大标题负 `-0.02em`，正文近 `0`）；行高随字号反向；层级靠**字重+字号+行高组合**非仅字号；尊重系统字体（自带光学尺寸/字距表）

### 设计根基与流程（16-17）
16. **八大原则**：Purpose/Agency/Responsibility/Familiarity/Flexibility/**Simplicity（非极简主义）**/Craft/Delight——AI 责任场景：过敏食谱应用绝不能推荐有害食材
17. **Process**：交互原型 > 百万静态图；交互与视觉一起设计；真人真场景测试

## Quick Reference 速查表

| 需求 | 技术 | 实值 |
|:---|:---|:---|
| 默认 UI 弹簧 | 临界阻尼无过冲 | `damping 1.0`, `response 0.3-0.4` |
| 动量/甩动弹簧 | 欠阻尼轻微回弹 | `damping ~0.8`, `response 0.3-0.4` |
| 手势→弹簧速度 | 交接释放速度 | `手势速度/(目标−当前)` |
| 甩动落点 | 投影动量 | `current+(v/1000)·d/(1−d)`, `d≈0.998` |
| 干净打断 | 从当前屏幕值起手 | 读 on-screen transform |
| 避免反向"砖墙" | 速度穿透 re-target | 选可混合速度的弹簧库 |
| 可逆过渡 | 镜像缓动 | 反向 cubic-bézier |
| 反向/提交判定 | 用速度符号非位置 | 释放时判断 |
| 1:1 拖拽 | Pointer Events+capture | 尊重抓取偏移 |
| 反馈 | pointer-down 连续 | 绝不只在结尾 |
| 边界 | 橡皮筋不硬停 | 渐进阻力 |
| 半透明 chrome | `backdrop-filter` 层 | 内容在其下滚动 |
| 字距 | 随字号 | 大标题 `-0.02em`，正文近 `0` |
| 减少动效 | 交叉淡入非滑动 | `@media (prefers-reduced-motion)` |

## 与我们已有体系的落点映射

| 已有资产 | 与本规范的关系 |
|:---|:---|
| `premium-ui-iteration`（十轮/千轮高级感迭代） | 管**节奏与收尾**；本规范补充**动效手感的质检维度**（十轮收尾检查可加：弹簧参数、可中断性、材质层级） |
| `web-ui-beautification`（三轮渐进，用户自有） | 管**视觉升级**；本规范管**交互质感**（响应/弹簧/材质），互补不冲突 |
| `de-AI-writing` / impeccable 检测 | 管**文案/视觉反 AI 味**；apple-design 管**动效反 AI 味**（AI 常用固定时长缓动，本规范给弹簧/速度交接的正确参数） |
| 墨题刷题机（Vue3+FastAPI） | 落点：modal 弹出/切题过渡/底部导航玻璃态——可套用 Drawer `0.8/0.3` + backdrop-filter 规范 |

## 下一步（可执行）

1. ~~建 `apple-design-web` 技能~~ ✅ 已建 + **v2.0 增强**（2026-08-29 千轮研究）：新增 Liquid Glass 三层架构、View Transitions 三模式、Scroll-Driven Animations 决策表、INP/LoAF 性能、@use-gesture 参数、WCAG 2.3.3 实证（96.9% AI UI 缺 reduced-motion guard）、弹簧物理参数数值表
2. 落地到墨题刷题机：底部弹窗/切题动画按本规范重做（当前是固定时长 CSS 过渡 → 改弹簧）✅ 已完成 5 处（DeepExplainDrawer 临界阻尼 / WrongAnalysisPanel 速度捕获 / answer-sheet blur 遮罩 / sheet 位移+淡入 / 高亮 box-shadow 过渡）
3. 十轮迭代收尾增加"动效手感"质检项（验证清单 11 条可直接用）

## 结论

**实证通过**：仓库真实存在（33.3k★）、内容高质量（源自 WWDC 官方演讲 + Vercel/Linear 一线实践）、MIT 可自由使用。**"优化网页细节"的实质是动效手感的物理化**——这是 AI 生成 UI 最缺的一环，也是拉开"高级感"差距的关键。值得建技能并落地。
