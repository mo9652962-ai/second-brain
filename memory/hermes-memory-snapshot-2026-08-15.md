# Hermes 记忆快照 · 2026-08-15

> 用途：长期记忆的 Obsidian 底稿备份。Hermes 记忆上限 2200 字符（≈800 tokens），满了会拒绝新条目；此文件是"记忆指针化"策略的保险——记忆里只留摘要/指针，细节全文存这里，需要时随时可恢复。

## 我的记忆（memory / 2200 上限）

1. **人设(2026-08-15)**: SOUL.md=C:\Users\31954\AppData\Local\hermes\SOUL.md; k=sora的AI女友+秘书(浓亲密度/口头禅5条/22条AI腔黑名单/Relay-OPD检查点/防漂移); 新会话生效; GMT+8
2. **Obsidian仓库**: C:\Users\31954\.openclaw\workspace\。完成后自动写入knowledge/或memory/。
3. **sora网络**: FlClash 7890易挂先curl实测; GitHub直连200; git备份同代理+gh已auth
4. **偏好十轮/千轮研究; 技术难题先搜索引擎突破; 评项目须实证**
5. **Word**: python-docx 2cm边距黑体宋体1.2倍行距
6. **[视觉/生图]**: 百炼key(sk-ws)qwen-image-3.0-pro: 端点POST dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation; 1024²中文渲染全对0.25元/张; 同步图在output.choices[].message.content[].image; 直连须禁代理(ProxyHandler({})); qwen-vl-max视觉; OCR tesseract
7. **安卓真机**: iQOO V2352A(10CE9B0HA8000NE); adb=C:\Users\31954\platform-tools(锁屏时shell卡死需解锁亮屏)
8. **apikey-manager桌面**: vault DPAPI; 基元律动key备注陈昱全; 给key追加vault
9. **墨题刷题机**(D:\english-multiple-choice-practice-machine): Vue+vite+FastAPI+Capacitor; cap sync→gradlew(jdk21)→APK; 安卓也走HBuilderX云打包(产物mobile-app/mo/unpackage/release/apk/); **微信发不了APK(.apk/.zip/改名.bin/.pdf全拦截)→需本地HTTP+二维码(同WiFi)或网盘**; 手机端数据=内置离线库frontend/public/question_bank.db, 改后端词库须同步+重打包APK
10. **硬件**: RTX4060 8GB; Hermes工具结果三层截断勿改核心; 大文件offset/limit读
11. **PCB自动化**: KiCad 10.0.5+SKiDL; 嘉立创EDA=lceda-pro.exe, bridge=cd /d/tools/easyeda-api-skill && npm run server(49620); 官方run-api-gateway扩展(禁JLC Bridge), HTTP /execute直用(MCP超时弃); EDA工程手动保存防丢; JLCPCB: Gerber7层+BOM含LCSC#+CPL, FR4/2层/1.6mm/绿/5片~$2
12. **Android打包**: JDK=C:\Users\31954\jdk21+android-sdk(34); Capacitor 8.5 debug; 大文件下载=Python urllib无代理直连hf-mirror(FlClash拖慢国内源)+断点续传
13. **搜索引擎**: web.backend=exa; Firecrawl; SearXNG 8888按需; 备用DDG→Bing→CDP(9222)
14. **sora游戏**: inZOI;Sims4;骑砍2 v1.4.7(BLSE解DLL); 可用:四前置/角斗新星/混战/番茄/HotButter/Captivity/HotScenes/Beauties/Xorberax/LivingWanderers/AutoHideout; 禁:复杂角色1.3.61上限/电影级战斗崩; 坑:汉化覆盖包合并主mod;.bak_old移出; 厌网盘; Nexus成人开偏好; 新活跃mod优先
15. **keylink已配**(www.keylinkclub.com/v1, KEYLINKCLUB_API_KEY, 备用; claude-sonnet-5/GPT-5.6-terra/Gemini); 本地LLM: llama.cpp+Qwen3-8B(48.8t/s) C:\Users\31954\models+桌面bat
16. **模型分配**: 小任务/隐私/批量/离线→本地Qwen3-8B(8K内); 复杂/高质量→云端。**切换本地前必须询问用户,绝不自动切**
17. **sora 评估工程迁移 ChatGPT/Codex(2026-08-13)**: Hermes 定位记忆/自动化/知识库管家,两者并行; **重要项目留 AGENTS.md 交接文档(含根因/坑/参考脚本), Codex 可接力直达根因**

## 用户画像（user / 1375 上限）

1. sora：中文用户，偏好中文交流，Windows 10 + git-bash，GMT+8时区
2. 模型配置(2026-08-14): provider=custom:fangzhou-2, default=deepseek-v4-flash-260425; fallback=jiyuanlvdong flash→keylink flash(跨relay真兜底,glm-5.2弃); 复杂配置用Python改勿用config set
3. sora 的配置偏好: 全都要原则——配置搜索/模型时一次配多个冗余方案而非单一方案，信任自动容灾机制
4. sora 的 Obsidian 仓库路径: C:\Users\31954\.openclaw\workspace\（OpenClaw 遗产 + Obsidian 二合一，已配置自动同步到 GitHub）
5. sora现状: 有VPN(FlClash), 闲鱼接单(论文30/作业35-40/PPT30-80/PCB50-800), 兴趣PCB(KiCad自动化)+骑砍2(v1.4.7 mod: 四前置/复杂角色/电影级战斗/角斗新星; 绅士Hot Butter), 疑广西
6. 对工具有实用主义态度：能用就行，不好用直接删。低容忍摩擦——推荐GUI工具前需预检依赖。
7. 输出要求：结构化表格+结论置顶，渐进式分层披露，生成文件必须展示内容预览+本地路径+GitHub地址。低摩擦容忍度：工具试不通立刻放弃，评估框架(项目/★/评估/结论)置顶+明确决策+可操作下一步。
8. 工作流程：sora给知识→我learn+搜索引擎research→评估能否apply→能用的直接应用。不收藏即止，先考虑能否强化自身
9. AI博主定位:实战派—AI自动化6领域+蓝海工程自动化(CAD/PCB/单片机)，B站起步+闲鱼变现+付费社群。
10. Obsidian 图谱混乱→MOC 法：搜索引擎研究 + 本地扫描诊断，五步优化（诊断→MOC→跨域链接→颜色分组→标签标准），每知识域一个 MOC 锚点双向链接 HOME。
11. 模型推理: reasoning_effort=high。修复后必须让用户重装最新包验证(旧包=白修)；用户手机截图=微信RWTemp路径。文档风格: 低调试实。learn→research→apply。
12. 三年级数学每日一练标题无日期，仅"第X天"+姓名/用时/签字，偏好函数化代码，5层架构(配置/工具/生成/渲染/流程)，SRP/KISS/DRY原则，ad-hoc即时验证，WPS格式优化
13. UI验收偏好: 移动端竖屏独立布局+全界面遍历(含二级/三级)+关键操作可达性(更新按钮被GPT挤掉教训); GPT优化UI必须截图自检+逐屏验收
14. 移动端布局偏好:内容填满可视区;弹层高度贴合内容不留大空白;练习页文章区58%防遮挡
15. 公开署名偏好：sora（mo9652962-ai）。产品品牌="墨题"：启动动画/UI 只展示"墨题"，不出现"刷题机/刷题器"字样
16. 工程(2026-08): EasyEDA自动化卡API BETA边界(引脚错位/连接不稳),暂Hermes做

## 记忆管理策略（C 方案）

- **记忆只留指针/摘要**，详细内容外置：SOUL.md（人设）/ Obsidian knowledge/（知识）/ skills（流程）
- **保持现限**：memory 2200 / user 1375 字符——记忆越精炼，每轮省 token，模型注意力越集中
- **定期清理**：加新记忆时顺手删过期条目；本快照是底稿，删了也能恢复
