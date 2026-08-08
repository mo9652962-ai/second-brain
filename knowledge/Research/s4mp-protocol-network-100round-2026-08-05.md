---
aliases:
  - s4mp-protocol-network-100round-2026-08-05
tags:
  - research
  - s4mp
  - sims4
  - multiplayer
  - protocol
  - network
created: 2026-08-05
updated: 2026-08-05
status: adopted
---

# 🔌 S4MP 消息协议（网络层）百轮研究 + 自制 mod 改进

> 知识库消息协议笔记 + 4 批搜索引擎研究（借鉴 S4MP/业界标准）+ 百次虚拟测试（v9.12）
> 目标：对照 S4MP 网络层，找出自制 mod 协议差距并改进

---

## 一、现状盘点（自制 mod v9.11 协议）

- **序列化**：pickle 二进制帧（8 字节大端长度前缀 + pickle）——比 JSON 快 2.8x、体积 84%
- **消息类型**：29 种（hello/welcome/lobby/ready/in_lot/heartbeat/chat/clock/mood/money_sync/stats_sync/sim_pos/save_*/travel_*）
- **可靠性**：TCP 保证有序可靠；seq 序号（位置丢包检测）；心跳 5s + 超时 15s
- **容错**：断线重连（指数退避 + jitter）、主机迁移、8MB 帧上限、线程锁

## 二、百轮研究结论（4 批搜索）

### 第 1 批：协议架构与帧格式
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| Protobuf vs Flatbuffers vs JSON | 二进制比文本小 3 倍；Protobuf 序列化快 | pickle 已满足局域网需求 ✅ |
| Length-prefix framing（Eli Bendersky）| 长度前缀帧是标准做法 | 我们的 8 字节前缀 ✅ |
| **协议版本协商**（MCP handshake / QUIC RFC 9368）| **握手时交换版本，不兼容拒绝** | **❌ 缺失 → 已实现** |

### 第 2 批：心跳/可靠性/安全
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| WebSocket heartbeat（WebSocket.org）| 应用层心跳是唯一可靠检测僵尸连接的方法 | 心跳 5s/15s ✅ |
| Reliable Ordered（Gaffer）| TCP 本身处理可靠有序，无需应用层重传 | seq 仅用于丢包检测 ✅ |
| HMAC（RFC 2104/FIPS 198-1）| 包签名防篡改；局域网信任对端可省略 | 低优先（局域网）|

### 第 3 批：S4MP 具体实现
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| S4MP 官方 | 最新 0.74.1；host 权威 + 同家庭多控 | 我们对齐 ✅ |
| SmartFoxServer 房间 | public/private（密码）+ 6 位房间码 | 我们已实现 ✅ |
| **位置量化**（Gaffer 4096 values/meter）| 位置量化到整数大幅省带宽 | **❌ 缺失 → 已实现（0.01m）** |

### 第 4 批：编码/连接管理
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| varint（Protobuf encoding）| 小整数 1 字节 vs 固定 8 字节 | 低价值（局域网）|
| 连接池/复用（OneUptime）| 服务器管理多连接 | host 多 client ✅ |
| **player_id 管理**（知识库 S4MP 笔记）| 重连 ID 递增 → KeyError:2 | **❌ 递增 → 已实现复用池** |

## 三、改进实施（v9.12）

### 1. 协议版本协商（MCP/QUIC 模式）
```python
PROTO_VERSION = 2  # 1=JSON时代, 2=pickle帧(当前)
# hello 带 proto_version → host 校验 → 不匹配发 version_mismatch + 拒绝
# 客户端收到 version_mismatch → 提示"协议版本不兼容，请更新"
```
- 防旧 mod 连新 host 导致消息字段错乱
- welcome 也带 proto_version（客户端可校验）

### 2. player_id 复用池（防 KeyError:2）
```python
_released_pids = []  # 断开时回收，重连复用原 ID
# 连接分配：优先 _released_pids.pop(0)，否则 _next_player_id
```
- 断开 → `_clients.pop` + 加入复用池
- 重连 → 复用原 player_id（不递增）→ 不会 KeyError

### 3. 位置量化（Gaffer 4096 values/meter）
```python
def _quantize(v): return int(round(float(v) * 100))  # 0.01m 精度
# 发送：delta_q = [量化后的整数 delta]
# 接收：pos = base + delta_q[i] / 100.0
```
- 传输整数（pickle 体积更小），接收端 /100 还原
- 0.01m 精度远小于人物可见位移
- 兼容旧协议（delta 未量化仍可处理）

## 四、百次虚拟测试（v9.12，19 断言全过）

| 测试 | 内容 | 结果 |
|:-----|:-----|:-----|
| A. 版本协商 | 匹配加入 / 旧版本拒绝 / 无版本拒绝 / 客户端提示 | ✅ |
| B. player_id 复用 | 断开进池 / 重连复用 / 20 次循环不递增 | ✅ |
| C. 位置量化 | 0.01m 精度 / banker's rounding / 还原累加 / 20 步误差 <0.5m | ✅ |
| D. 兼容性 | 旧 delta / position 绝对值 / welcome 带版本 | ✅ |

## 五、回归体系（11 套件 / 165 断言）

```
v92 端到端(12) + v93 传输层(10) + v94 协议语义(15) + v95 生命周期(11)
+ v96 纯逻辑(10) + v97 内存GUI(8) + v98 新领域(17) + v99 同步行为(19)
+ v910 容错(19) + v911 旅行(26) + v912 协议增强(19) = 一键全跑全过
```

---

## 变更记录
- 2026-08-05: 初版（百轮研究 + 3 项协议改进 + v9.12 测试）

## 六、第二轮改进（v9.13——批处理 + 协议目录）

### 研究（第 5-6 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| 消息批处理（Vanilla Java/Unity）| TCP 小消息合并到阈值（4KB）大幅提吞吐 | **❌ 无批处理 → 已实现 `_send_batch`** |
| 帧损坏恢复（工业标准）| 坏帧边界检测是关键；TCP 校验已覆盖局域网 | 低价值跳过 |
| Schema Registry（Kafka）| 集中管理消息 schema + 兼容规则 | **❌ 无文档 → 已写 docs/PROTOCOL.md** |
| 自适应拥塞（TCP BBR）| RTT 调整速率；已有自适应 tick | 低优先 |

### 改进
1. **`_send_batch(sock, payloads)`**：多条小消息合并成一个 `{"type":"batch","msgs":[...]}` 帧
   - 单条→直发，空→跳过，多条→batch 帧
   - 接收端 `_process_incoming` 拆包逐个处理
2. **`docs/PROTOCOL.md` 协议消息目录**：30 种消息类型全表（方向/字段/用途）+ 帧格式 + 版本兼容规则

### 测试（v9.13，14 断言全过）
- A. _send_batch 逻辑（空/单条/多条/20 次合并正确）
- B. batch 拆包（拆开处理/chat 分发/空不崩/非 dict 跳过）
- C. **真实 TCP 批处理闭环**（client batch → host 拆包 → add_chat）
- D. 协议目录完整性（30 种消息全覆盖检查）

### 回归体系升级（12 套件 / 179 断言）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)
+v98(17)+v99(19)+v910(19)+v911(26)+v912(19)+v913(14) = 一键全跑全过
```

## 七、第三轮改进（v9.14——连接健康监控）

### 研究（第 7-8 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| 游戏 QoS（pvigier）| 消息可分级（可靠/不可靠）+ 多流分离 | 位置低优/聊天高优思路 |
| RTT 测量（游戏 ping）| 应用层 ping/pong 带时间戳测 RTT | **❌ 无 RTT → 已实现** |
| 自适应频率（DACC/RFC 6298）| 高延迟降频防拥塞 | **❌ 无自适应 → 已实现** |
| 健康评分（Cloudflare/PingPlotter）| latency/jitter/loss → 质量分 | **❌ 无评分 → 已实现** |

### 改进
1. **应用层 ping/pong RTT 测量**（network.py）
   - `ping` 带 ts → 对端回 `pong`（带原 ts）→ RTT = now - ts
   - 主动 ping 每 3s（alarm 循环 `_send_ping`）
   - 滚动窗口 20 样本，异常值（>5s）过滤
2. **连接健康评分**（Cloudflare 模型）
   - `get_health_score()`：100 - RTT 扣分（50ms 内不扣，每超 5ms 扣 1，上限 60）
   - `get_health_label()`：🟢优秀/🟡良好/🟠一般/🔴差
3. **自适应位置广播频率**（sync.py）
   - RTT > 200ms → 间隔 1.5x；RTT > 400ms → 2x（网络差降频防拥塞）

### 测试（v9.14，19 断言全过）
- A. ping/pong RTT（回 pong/计算/异常过滤/无 ts 不崩）
- B. 健康评分（无样本/优秀/差/20 次范围）
- C. 滚动平均（20 窗口/平均正确/新样本挤旧）
- D. 自适应频率（无 RTT 默认/200-400 1.5x/>400 2x/低 RTT 默认）
- E. **真实 TCP ping/pong 闭环**（host 发 ping → client 回 pong → host 算 RTT）

### 修复（百次测试挖出）
1. **ping 处理引用未定义 `sock` 变量**（NameError 被吞→不回 pong）——改为 sender_pid 查 _clients
2. v911 `_fake_timer` 立即执行改变旅行时序——改 no-op
3. PROTOCOL.md 缺 ping/pong——已补（32 种消息）

### 回归体系升级（13 套件 / 198 断言）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)+v98(17)
+v99(19)+v910(19)+v911(26)+v912(19)+v913(14)+v914(19) = 一键全跑全过
```

## 八、协议层累计 9 项增强（三轮）
```
v9.12: 版本协商 + player_id 复用 + 位置量化
v9.13: 消息批处理 + 协议目录
v9.14: RTT 测量 + 健康评分 + 自适应频率
```

## 九、第四轮改进（v9.15——CRC 帧校验 + 消息优先级）

### 研究（第 9-10 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| CRC32（Ethernet FCS）| 0x04C11DB7 标准，检测突发错误强于校验和；Python binascii.crc32 | **❌ 无校验 → 已实现** |
| CRC vs 校验和 | CRC 检测模式错误（burst errors），简单 checksum 漏检 | 用 CRC32 |
| QoS 优先级（pvigier）| 消息分级（可靠/不可靠）+ 多流分离 | **❌ 无分级 → 已实现** |

### 改进
1. **CRC32 帧校验**（network.py）
   - 帧格式升级：`[8长度][4 CRC32][pickle]`（12 字节头）
   - 发送 `_send_json` 算 CRC；接收 `_recv_loop` 校验——坏帧丢弃不崩
   - 帧损坏/位翻转 → 丢弃；坏帧后连接存活（TCP 连续流不受影响）
2. **消息优先级**（QoS，pvigier 多流分离）
   - `_send_json(sock, payload, prio)`：0=紧急 1=普通 2=低优
   - 紧急（hello/welcome/ready/travel_*）直发；位置（sim_pos）低优可 batch
   - PROTOCOL.md 记录优先级分级

### 测试（v9.15，16 断言全过）
- A. CRC 帧格式（8长度+4CRC/20 次 CRC 正确）
- B. CRC 校验（正常通过/数据位翻转检测/CRC 字段损坏/20 次随机损坏全检测）
- C. **真实 TCP CRC 闭环**（正常帧到达/坏帧丢弃/坏帧后连接存活）
- D. 消息优先级（默认 1/紧急 0/低优 2/batch 合并低优）

### 百次测试挖出 3 个真实 bug（帧格式升级连锁）
1. **测试 mock `Net._send_json` 缺 prio 参数** → host 发 welcome 崩溃 → recv 线程没启动（v913/v914 真实 TCP 失败根因）
2. **v93 手工帧没带 proto_version** → 版本协商拒绝 → 握手失败
3. **v93 缺 binascii import**（单行 import 替换没匹配）+ **`fc` 变量覆盖全局失败计数器**

### 回归体系升级（14 套件 / 208 断言）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)+v98(17)+v99(19)
+v910(19)+v911(26)+v912(19)+v913(14)+v914(19)+v915(16) = 一键全跑全过
```

## 十、协议层累计 11 项增强（四轮）
```
v9.12: 版本协商 + player_id 复用 + 位置量化
v9.13: 消息批处理 + 协议目录
v9.14: RTT 测量 + 健康评分 + 自适应频率
v9.15: CRC 帧校验 + 消息优先级
```

## 十一、第五轮改进（v9.16——HMAC 消息签名，跨网安全）

### 研究（第 11 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| HMAC（RFC 2104）| 密钥散列消息认证，防篡改+认证；TLS 1.3 用 HMAC 派生密钥 | **❌ 裸 pickle → 已实现** |
| HKDF（RFC 5869）| 主密钥 → 会话密钥派生；TLS 1.3 同款 | 握手 nonce 交换派生 |
| MAC 性能 | HMAC-SHA256 每消息微秒级，游戏无感 | 始终签名不降级 |

### 方案
1. **握手密钥交换**：client 生成 client_nonce（随机16B hex）→ hello 携带；host 生成 host_nonce → welcome 携带；双方独立派生 `key = HMAC-SHA256(房间密码, client_nonce + host_nonce)`
2. **帧签名**：帧格式升级 `[8长度][4CRC][32 HMAC-SHA256][pickle]`（44 字节头）——发送算 HMAC，接收**先验签再反序列化**（Encrypt-then-MAC 顺序）
3. **多客户端独立密钥**：`_hmac_keys[pid]` 每 client 各自 key，互不通用；host 按 pid 反查，client 用自己的 key

### 关键 bug 修复（5 个，测试挖出）
1. **帧头长度不固定**：无 key 返回 0 字节签名 → 收端固定 44 偏移错位（把 data 前 32 字节当签名）→ **修正：无 key 填 32 字节零签名占位，帧头恒 44 字节**
2. **client 端发送 key 选择**：`_sock_to_pid` 对 client socket 无效 → 改用 `_my_player_id` 查 key
3. **同进程双端测试的 `_my_nonce` 覆盖**（host 覆盖 client）——真实双端独立进程无此问题；测试手动按握手语义重建 key
4. **lobby.network = Net 污染**（C 段 mock 后 D 段真实 TCP 写错对象）——D 段前恢复真实引用
5. **旧测试帧格式连锁**：v92-v915 全部升级 44 字节头（+真 null 字节转义修复）

### 测试（v9.16，22 断言全过）
- A. 密钥派生（相同输入→同 key/不同密码/不同 nonce/20 次确定性）
- B. 签名/验签（正确通过/篡改拒绝/错误 key 拒绝/无 key 通过/20 次随机篡改检测）
- C. 握手密钥交换（host/client 各自派生 32B key）
- D. **真实 TCP 签名闭环**（签名消息到达/篡改帧被拒/篡改后连接存活）
- E. 多客户端独立密钥（各自验签/跨 client 互斥）

### 回归体系升级（15 套件全过）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)+v98(17)+v99(19)
+v910(19)+v911(26)+v912(19)+v913(14)+v914(19)+v915(16)+v916(22)
```

## 十二、协议层累计 12 项增强（五轮）
```
v9.12: 版本协商 + player_id 复用 + 位置量化
v9.13: 消息批处理 + 协议目录
v9.14: RTT 测量 + 健康评分 + 自适应频率
v9.15: CRC 帧校验 + 消息优先级
v9.16: HMAC 消息签名 + 握手密钥交换（跨网安全）
```

### 安全评估（跨网 pickle 风险闭环）
- 签名前：pickle 反序列化任意代码执行（跨网风险高）
- 签名后：**无密钥无法构造合法帧**（HMAC-SHA256 前像不可伪造）；篡改必被拒绝（先验签再反序列化）
- 残余风险：pickle 数据本身仍明文（未加密）——签名防伪造/篡改，不防窃听；局域网/信任对端可接受
- 下一步候选：Protobuf 序列化（S4MP 方案）——类型安全 + 跨语言，替代 pickle


## 十三、真机排障实战（2026-08-05 双机实测挖出 3 个测试没抓到的 bug）

> 虚拟测试全绿 ≠ 真机没问题——真机日志是最终裁判。

### 1. 模块内 `network.` 前缀 NameError
- 现象：房主建房后房间页不显示自己（members 空 + room_code 空）
- 根因：`mp_host`/`mp_apply` 里 `network._my_player_id = 0` —— **network.py 模块内没有 `network` 这个名字**（函数内 `network.xxx` 是全局查找）→ NameError → 被 `except: _log("lobby setup error")` 吞 → `add_host_self` 没执行
- 教训：**模块内函数引用自己模块的全局变量，直接写变量名，不要加模块名前缀**；真机日志 `lobby setup error: name 'network' is not defined` 是排障关键信号
- 虚拟测试没抓到：测试直接调 add_host_self，不走 mp_host 命令路径

### 2. 帧格式不兼容 → 对端秒断（协议升级破坏性实测）
- 现象：对端连上主机 1 秒内断开，host 日志 `send error: [WinError 10053]`（对端已关）
- 根因：对端装 v9.15 及更早（12 字节帧头）→ 收到 v9.16 的 44 字节头 welcome → 解析错位 → unpickle error → 主动断开
- 更早版本（JSON 时代）：客机日志 `recv error: 'utf-8' codec can't decode byte 0x81` —— **v9.16 根本不按 utf-8 解码**，出现 utf-8 解码错误 = 对端是 v7.2 之前的 JSON 协议时代
- 教训：**帧格式升级是 breaking change，两端必须同版本**；分发时强调版本一致 + 验证日志首行版本号

### 3. 打包交付完整性（bat 版本号）
- 现象：zip 里安装mod.bat 显示 v5.3（用户误以为旧版）
- 根因：bat 标题行版本号从未随版本递增
- 教训：打包核对清单含 mod/说明/bat/zip 文件名四件套版本一致性

## 十四、协议版本协商深度研究（2026-08-05 web 研究）

> 触发：真机遇到「旧客户端连新服务器秒断」——版本协商的行业最佳实践是什么？

### 研究结论
| 来源 | 方案 | 借鉴点 |
|:-----|:-----|:-------|
| **MCP spec（modelcontextprotocol.io）** | `server/discover` 协商——客户端先问服务器支持的版本列表 → 选双方都支持；不兼容返回结构化错误（`UnsupportedProtocolVersionError`）而非静默断连 | 协商放握手早期；错误要**结构化可识别**（客户端能据此给用户友好提示） |
| **Martin Evans（游戏网络协议）** | 协议必须有**版本标识符**，旧消息可检测并丢弃；向后兼容 = 同时支持新旧版本，连接建立时协商 | 帧头 magic number 快速识别协议时代 |
| **TLS / OneUptime** | 客户端服务器对齐支持的版本，双方声明支持列表 | 版本列表协商是标准做法 |
| **jser.dev** | 版本比较 + 降级计划（先支持新旧，一段时间后移除旧） | 兼容窗口期概念 |

### 我们的差距与改进候选（后续）
- ✅ 已有：PROTO_VERSION 协商（hello 带版本，不匹配发 version_mismatch）
- ❌ **盲点：帧格式不兼容发生在握手之前**——旧客户端 hello（12 字节头）在新服务器（44 字节解析）上错位 → 版本字段都读不到 → 无法发 version_mismatch → 秒断
- 🔧 候选改进：**帧头加 magic number + 协议版本**（固定偏移，任何版本都能读）→ 收端先读 magic → 判断对端协议时代 → 能兼容则降级解析，不能则发结构化错误（含"请更新到 vX"提示）而非裸断连
- 🔧 或：hello 帧用"版本无关最小编帧"（前 8 字节 = magic + version，之后才是长度前缀 + 载荷）
- 优先级：局域网信任对端场景收益低（知道更新即可），**跨网公开场景才值得做**（防恶意/误连错版本）

## 十五、五轮总结（v9.12-v9.16 完整链路）
- **研究驱动**：4 批 web 研究 → 12 项增强（版本协商/ID 复用/量化/批处理/协议目录/RTT/健康评分/自适应频率/CRC/优先级/HMAC/密钥交换）
- **测试体系**：15 套件 237 断言（端到端 TCP + 传输层 + 协议语义 + 生命周期 + 纯逻辑 + 内存/GUI/配置/fuzz + UDP 发现 + 迟滞阈值 + 容错 + 场景切换 + 版本协商 + 批处理 + 健康 + 帧校验 + 签名闭环）
- **真机验证**：双机 LAN 实测（建房/加入/聊天/位置同步）+ 双机排障（NameError/版本不兼容）
- **最大短板**：跨网真机验证（UPnP/STUN 代码就绪但从未在真实公网环境跑通）


## 十六、外部架构建议的逐项研究验证（2026-08-05 web 研究）

> 来源：用户提供的一份"S4MP 类联机框架从零设计建议"（Master Server 可选 / 同步操作 / Hook API / 网络库选型 / Host Authority / Tick / Save / 分阶段开发）。逐项用 web 搜索验证 + 对照我们实现。

### 0. 许可边界确认（最重要）
- **S4MP = All Rights Reserved（保留所有权利），非开源**（CurseForge 页面明确标注 License: All Rights Reserved）
- **不能**：复制其代码 / 反编译其 mod 后再发布
- **可以**：借鉴设计思路（架构/流程），自己实现全部代码；反编译**游戏本身 API**（Data/Simulation/Gameplay 的 pyc）做 hook 是合法 mod 开发
- **我们的合规状态**：✅ 全部自研（pickle 帧/HMAC/房间系统/启动器都是自己写的），只参考 S4MP 的设计思想（host 权威/房间码/同家庭多控），反编译对象是游戏 API 不是 S4MP——合规

### 1. Master Server（建议：可选）
| 研究 | 结论 |
|:-----|:-----|
| Unity Master Server Kit / Dedicated Server Kit | master server = 认证 + 房间列表 + matchmaking，spawn 独立 game server 实例 |
| Unity listen server 文档 | **listen server（房主托管）= 免费、无需基础设施、LAN 首选**；需 port forwarding 才能跨网 |
| AccelByte P2P vs Relay vs Dedicated | P2P 便宜、dedicated 贵、relay 居中；从 early access 到 live service 最终会走向 dedicated |
| **我们现状** | ✅ **listen server 模式**（房主托管 + 局域网 UDP 发现 + 房间码 + UPnP 跨网）——完全符合"小规模免费优先"的行业建议 |
| **候选增强** | 跨网房间列表 Master Server（部署成本高，非必须；有朋友约玩用房间码足够） |

### 2. 同步"操作/状态"而非整个游戏（建议核心思想）
| 研究 | 结论 |
|:-----|:-----|
| gamedev.stackexchange 51522 | **state sync 简单**（新客户端发全量 state 即加入）；event sync 需更多重发/流控逻辑 |
| ruoyusun.com Game Networking Demystified | 核心问题 = "发的是游戏状态还是输入"；没有金架构，大多混合 |
| Deterministic Lockstep 论文 | 三种同步方法：lockstep（只传命令）/ snapshot interpolation（host 跑模拟广播快照）/ state-sync 混合 |
| **我们现状** | ✅ **状态同步为主**（位置 Delta/需求/金钱/心情/时间）+ 事件同步（聊天/旅行/准备/存档）——正是行业推荐的混合模式 |
| **差距** | ❌ 交互队列事件同步未做（S4MP 深度协议，需 hook interaction 系统 + pie menu + 目标选择）——复杂度高，保持远期 |

### 3. 网络库选型（建议：ENet/LiteNetLib/WebSocket 别自己写 socket）
| 研究 | 结论 |
|:-----|:-----|
| StackOverflow WebSockets UDP benchmarks | WebSocket 基于 TCP，有 TCP 同样优缺点；实时游戏偏好 UDP 是历史惯性 |
| CodeSmile TCP/UDP/WebSocket 详解 | 游戏偏好不可靠 UDP；可靠 UDP（ACK/重发）需传输层实现（Unity Transport） |
| gamedev 120054 / AWS re:Post | 低丢包下 TCP 延迟与 UDP 几乎无差；ENet 缺文档、KCP 中文社区流行 |
| **我们现状** | ✅ 自写 TCP + pickle 帧，**已实现 ENet 等效能力**：可靠传输（TCP 自带）+ 帧 CRC 校验（防损坏）+ 消息优先级 + HMAC 签名（防伪造）+ 8MB 帧上限 |
| **评估** | 🔧 换库收益低：游戏内嵌 Python 3.7 环境装 ENet/LiteNetLib 有兼容风险；我们自写的帧协议已覆盖 ENet 核心能力。**保留现状**，WebSocket 仅当未来需要浏览器端才考虑 |

### 4. Host Authority（建议：Host 是唯一真相）
| 结论 | 我们现状 |
|:-----|:---------|
| 行业标准：server-authoritative（服务器权威）防作弊 + 一致性 | ✅ 完全对齐：时间（GameClock hook 主机掌控）、房间（host 建/踢/转交）、存档（host 分发）、广播（host 中继）|

### 5. Tick 同步（建议 5-20Hz）
| 研究 | 结论 |
|:-----|:-----|
| Donnybrook 论文 | p2p 更新按 n² 增长（Quake III ~12n kb/s/player），16-32 人上限 |
| Monstarlab | 状态同步 200-300ms 延迟可接受（RPG），50ms 才敏感（RTS）|
| **我们现状** | ✅ 2-5Hz（0.2-0.5s 自适应）+ 快照插值（v7.0）——低 tick + 插值 = Gaffer 标准做法，Sims4 慢节奏完全够 |
| **候选** | 可测 10Hz 提升平滑度（低优先，插值已覆盖观感）|

### 6. Save 同步（建议：避免 A/B 存档冲突）
| 研究 | 结论 |
|:-----|:-----|
| LWW（Last-Write-Wins）/ Cassandra / Vector Clock | LWW 最简单但有数据丢失风险；Vector Clock 复杂防丢失 |
| **我们现状** | ✅ **host 权威分发**（房主存档是唯一真相，天然无冲突）+ base64 分块 + SHA256 完整性 + 缺块自动重传 + 本地 .bak 备份——优于 LWW 场景（不是双方同时写）|
| **候选** | 可加"存档版本号对比"提示（客户端存档比房主旧时提醒），低优先 |

### 7. 2-12 人扩展可行性
| 结论 | 依据 |
|:-----|:-----|
| **LAN 12 人可行** | 我们 star topology（每 client 直连 host）避免 n² 全互联；状态同步 ~12n kb/s 量级 → 12 人 LAN 轻松 |
| 跨网 12 人需 host 上行 ~1-2 Mbps | 家庭宽带够；但 host 是玩家机器（非数据中心）→ 延迟/稳定性由 host 网络决定（gamedev 67738 确认这是 listen server 的固有限制）|
| 防作弊 | host 权威天然防作弊（client 不能改世界）✅ |

### 8. 分阶段开发路线对照（我们已走完）
| 建议阶段 | 我们的版本 |
|:---------|:-----------|
| 1. 连接+聊天验证网络层 | v4.2 ✅ |
| 2. 时间/暂停/倍速同步 | v5.5 ✅ |
| 3. Sim 移动+交互队列 | 移动 ✅（v4.9+）；交互队列 ❌（远期候选）|
| 4. 需求值/背包/关系 | 需求/金钱/心情 ✅（v7.1/v8.2/v8.4）；背包/关系 ❌（候选）|
| 5. Build/Buy + 存档同步 | 存档 ✅（v6.2）；Build/Buy ❌（复杂度高）|
| 6. 断线重连/状态恢复/版本校验 | ✅（v7.0 重连 + v9.12 版本协商 + v9.16 HMAC）|

### 总结论
- **架构建议与我们实现高度一致**（listen server + host 权威 + 状态同步为主 + 分阶段）——方向被行业实践验证 ✅
- **真正差距**：交互队列事件同步（阶段 3 后半）、背包/关系同步（阶段 4 后半）、Build/Buy（阶段 5 后半）——都是 S4MP 深度协议，复杂度高，保持远期候选
- **不建议换的**：网络库（自写 TCP 已等效 ENet 能力）、Master Server（小规模房间码足够）
- **合规**：All Rights Reserved 下借鉴设计思路 + 自研实现 = 完全合法


## 十七、三大深度同步领域可行性研究（2026-08-05 web 研究 + 游戏 pyc 反编译）

> 对「交互队列事件同步 / 背包关系同步 / Build-Buy 同步」三项远期候选做系统性验证。
> 方法：web 搜索（竞品行为 + 社区库）+ **直接反编译游戏 pyc 确认 API**（uncompyle6 + dis 字节码探测，比 web 更准）。

### 一、交互队列事件同步（阶段 3 后半）—— 🟡 中高可行性（比预期好）

**反编译 `interactions/si_state.pyc`（dis 字节码探测）确认 API：**
| 能力 | API | 用途 |
|:-----|:-----|:-----|
| 读交互列表 | `all_si_gen()` / `queued_interactions` / `queued_super_interactions_gen` | 遍历当前交互 |
| 读交互状态 | `started` / `start_time` / `is_finishing` / `interaction` | 同步生命周期 |
| 查询 | `find_interaction_by_id` / `get_interaction_type` / `get_si_by_affordance` | 定位交互 |
| **写（执行交互）** | **`push_super_affordance`** | 对端执行同款交互 |
| 取消 | `cancel` / `on_interaction_canceled` | 同步取消 |

**务实版方案**（比 S4MP 全流程简单）：
1. Hook 交互启动事件（`sim.si_state` 的交互加入）→ 广播 `{type:"interaction", sim_id, affordance_id, target_id}`
2. 对端收到 → `sim.si_state.push_super_affordance(...)` 执行同款交互 → **看到对方小人在做饭/聊天**
3. **回环抑制**（关键，同位置同步 echo suppression）：对端 push 的交互会触发本地 hook 又广播回去 → 需要 `_applied_interaction_ts` 抑制窗口
4. 交互参数序列化：affordance 类型 ID + target 对象 ID（两端同存档 → 对象 ID 天然对齐 ✓）

**复杂度点**：交互参数多样性（姿势/道具/目标）、双方同控一 Sim 的冲突（host 权威裁决）、交互 ID 对齐。工作量 ~2-3 天。

### 二、背包/关系同步（阶段 4 后半）—— 🟢 背包低中 / 🟡 关系中

**背包（S4CL 开源库 CC BY 4.0 证明 API 存在）：**
- `CommonSimInventoryUtils.get_all_objects_in_inventory_gen(sim_info)` / `add_to_inventory(sim_info, definition_id, count)` / `move_object_to_inventory`
- 务实版：读背包物品（definition_id + count）→ 广播 → 对端 add_to_inventory——**和 stats_sync（需求/技能）同一模式**，低复杂度
- 两端同存档 → 对象 ID 天然对齐 ✓；工作量大半天~1 天

**关系（反编译 `relationships/relationship_tracker.pyc` 成功，API 完整）：**
| 能力 | API |
|:-----|:-----|
| 读分数 | `get_relationship_score(target_sim_id, track)` / `get_relationship_track` |
| 写分数 | `set_relationship_score` / `add_relationship_score` |
| 读关系位 | `get_all_bits` / `has_bit` / `has_bits` |
| **写关系位** | **`add_relationship_bit(target, bit, force_add)` / `remove_relationship_bit`** |
| 创建 | `create_relationship(target_sim_id)` |

- 务实版：读分数 + bits → 广播 → 对端 set/add——和 stats_sync 几乎一样
- 复杂度点：关系**双向**（A→B 和 B→A 都同步）、关系位 tuning ID、双方同时改同一关系的冲突（host 权威 + 阈值过滤，同 stats_sync 迟滞）。工作量 ~1-2 天

### 三、Build/Buy 同步（阶段 5 后半）—— 🔴 高（两家竞品都不做 build）

**决定性证据（两个竞品行为一致）：**
| 来源 | 原话 |
|:-----|:-----|
| Reddit r/simsmultiplayer（S4MP 社区）| "build mode doesn't sync in real time with the rest of the players, **buy mode fully works** for everyone; furnishing, rotating, etc." |
| SimSync FAQ（竞品 mod）| "Buy mode works but is in an **experimental** phase. **Build mode will cause issues and is not recommended.** The host controls items placed in buy mode." |

**结论**：
- **Buy（家具放置/旋转/移动）**：两家都做到了（S4MP 完全可用、SimSync 实验性）——对象 position/rotation 广播，中复杂度 ~2-3 天
- **Build（墙/地板/房间编辑）**：**两家都不做**——建筑操作是离散编辑事件流 + 全局重绘，复杂度爆炸，**明确不做**（和我们的评估一致）

### 四、实施优先级建议
| 优先级 | 项目 | 复杂度 | 工作量 | 价值 |
|:---:|:-----|:-----|:---:|:-----|
| 🥇 | **交互队列事件同步** | 🟡 中高 | 2-3 天 | **最高**（"看到对方做饭/聊天"= 真正一起生活）|
| 🥈 | 背包同步 | 🟢 低中 | 0.5-1 天 | 高（摸对方背包/共享物品）|
| 🥉 | 关系同步 | 🟡 中 | 1-2 天 | 中（依赖交互同步先做，否则关系变化少）|
| 4 | Buy 家具同步 | 🟡 中 | 2-3 天 | 中（S4MP 也实验性）|
| ❌ | Build 建筑同步 | 🔴 极高 | — | **不做**（两家竞品都不做）|

### 五、方法论沉淀
- **验证可行性最可靠手段 = 反编译游戏 pyc 确认 API**（uncompyle6 对复杂控制流会失败 → 用 `dis` 字节码探测 `co_names` 提取关键 API 名，快速确认能力存在）
- **竞品行为是可行性金标准**：S4MP 和 SimSync 都不做的功能（build mode）→ 大概率复杂度超出投入价值
- **务实版原则**：能"读状态→广播→写状态"的（背包/关系/需求）都是低-中复杂度；要"hook 操作事件流"的（交互/Build）都是高复杂度——先做读写的，再做事件的


## 十八、v9.17 四大深度同步模块落地（2026-08-05 实施）

> §17 研究结论直接落地——四个新模块全部实现 + 虚拟测试 25/25 + 16 套件回归全过。

### 新增模块（13 模块）
| 模块 | 同步内容 | 核心 API（反编译确认） | 广播消息 |
|:-----|:---------|:----------------------|:---------|
| `interaction_sync.py` | 交互队列事件（🥇 看到对方做饭/聊天）| `sim.push_super_affordance(aff, target, ctx)` + `si_state.sis_actor_gen()` | `{type:interaction, sim_id, affordance, target_id}` |
| `inventory_sync.py` | 背包物品（🥈 互相给东西）| `inventory_component` 迭代 + `player_try_add_object` / `try_remove_object_by_id` | `{type:inventory, sim_id, items:{def_id:count}}` |
| `relationship_sync.py` | 关系分数+bits（🥉 交朋友双方显示）| `get/set_relationship_score` + `add_relationship_bit(force_add)` | `{type:relationship, sim_a, sim_b, score, bits}` |
| `buy_sync.py` | Buy 家具位置/旋转（阶段 5 后半）| `object.location.clone` + `set_location` + `yaw_to_quaternion` | `{type:object_pos, obj_id, x,y,z,rot}` |

### 设计要点（踩坑沉淀）
- **回环抑制**（interaction_sync）：对端 push 的交互会触发本端检测又广播回去 → `_applied_ts[sim_id]` 3s 窗口跳过（同位置同步 echo suppression 思路）
- **迟滞阈值**（inventory/relationship）：接收端差异 <阈值 时反向修正广播（防双向打架）；≥阈值 才应用
- **Buy 只同步家具**：排除 Floor/Wall/Stairs 等建筑类（Build 不做——竞品共识）
- **互斥参考**：`sim_info._sim = self` 缓存（get_sim_instance 返回同一实例）——mock 测试关键
- **静态方法绑定坑**：mock 类属性赋 lambda/函数会被绑定成实例方法（self 自动传入）→ 必须 staticmethod
- **InteractionContext**：`InteractionContext(sim, SOURCE_SCRIPT, PRIORITY_MEDIUM)` 构造——mock 要有 __init__

### 集成
- `network._process_incoming` + 4 种新 mtype 分发（interaction/inventory/relationship/object_pos）
- `sync.mp_sync` 自动带起 4 个模块（同 mood 模式）
- 命令：`mp_intsync` / `mp_invsync` / `mp_relsync` / `mp_buysync`
- **v9.17 字节数 69,194B（13 模块）**；测试 `tools/virtual_test_v917.py` 25/25；全套 16 套件通过

### 真机待验证（最大短板延续）
- 交互同步：`push_super_affordance` 在真实游戏里对端执行是否正常（context 构造、AOP test 通过性）
- 背包补物品：`create_new_object` + `player_try_add_object` 真实可用性
- 关系 bits：STATISTIC instance manager 查 bit 的 guid64 路径
- 双机实测优先级：交互同步 > 背包 > 关系 > Buy


## 十九、第二份架构建议的逐项验证（2026-08-05 web 研究）——四项目分离 / TCP+UDP / MessagePack / 五层模块化

> 来源：用户提供的第二份架构建议（SimSync.Server/Client/Mod/Launcher 四项目分离 + TCP+UDP 混合 + MessagePack + Event Capture/Networking/Replication/Conflict Resolution/Versioning 五层）。针对"仅供自己和朋友用"场景逐项验证。

### 1. 四项目分离（独立 Server）—— 🟢 建议正确但对我们过度设计
| 研究 | 结论 |
|:-----|:-----|
| Unity Netcode listen server 文档 | **"Listen servers are best suited for a smaller player group (< 12) and games that don't require a persistent world"**——我们正是 <12 朋友场景 |
| Epic/Unreal 论坛 | listen server = 免费、玩家电脑当服务器；dedicated 要服务器成本 |
| 游戏联机经验（40% 流量案例）| **私人朋友 P2P/房主托管足够**（朋友间不担心主机掉线破坏体验）|
| **决策** | ✅ **保持房主托管**——独立服务器要部署/维护/跨网处理，对 2-12 人朋友联机是过度设计。S4MP 用独立服务器是为**公开 12 人**，我们自用不需要 |

### 2. TCP+UDP 混合 —— 🟡 建议正确但对我们收益低
| 研究 | 结论 |
|:-----|:-----|
| Gaffer (Glenn Fiedler) | UDP 用于位置（可丢包取最新），TCP 用于可靠有序命令——FPS 级需求 |
| pvigier blog | **"Many successful games, such as World of Warcraft, Minecraft or Terraria, use TCP"**——非实时游戏 TCP 完全够用；LAN 下 TCP 延迟几乎无差 |
| gamedev 59703 | UDP 用于时间敏感（移动），TCP 用于不敏感（心跳/交易）；取决于游戏类型 |
| **决策** | ✅ **保持纯 TCP**——Sims4 是慢节奏模拟（非 FPS），位置 2-5Hz + 阈值过滤后 TCP 延迟无感；UDP 要自己实现可靠性/顺序/重连，复杂度高收益低。已配 TCP_NODELAY + 自适应频率 |

### 3. MessagePack —— 🟡 性能好但换不动
| 研究 | 结论 |
|:-----|:-----|
| MessagePack benchmark | 比 JSON 快 ~4x；protobuf 更小但需 IDL；MessagePack 类型系统完整 |
| HN 讨论 | protobuf 比 MessagePack 更小但灵活性差；自描述格式 vs 外部 schema |
| **决策** | ✅ **保持 pickle**——我们实测 pickle 2.8x JSON（C 实现，Python 原生最快）；瓶颈是消息频率不是序列化。MessagePack 在 Python 里的收益（相对 pickle）不足以支付协议升级成本。**未来跨语言（C# 服务器）时才考虑** |

### 4. 统一数据包格式 —— ✅ 已对齐
建议 `{packet, tick, player, sim, ...}` = 我们的 `{type, ts, sender_pid, ...}`——字段语义完全一致（消息类型/时间戳/发送者/目标）。位置消息带 seq 序号、交互带 affordance+target——**已实现等效协议**。

### 5. 五层模块化架构 —— ✅ 已天然实现（映射）
| 建议层 | 我们的实现 |
|:-------|:-----------|
| Event Capture（事件采集）| 10 个监听模块（sync/stats/mood/money/interaction/inventory/relationship/buy/clock/lobby）|
| Networking（网络层）| network.py（帧协议 + CRC + HMAC + 优先级 + 批处理）|
| Replication（状态复制）| _process_incoming 分发 + 各模块 process_message 应用 |
| Conflict Resolution（冲突解决）| host 权威 + 迟滞阈值（stats/relationship）+ 回环抑制（interaction）+ 阈值过滤 |
| Versioning（版本兼容）| PROTO_VERSION 协商 + version_mismatch + HMAC 握手 |

### 6. 同步频率表 —— ✅ 已对齐（甚至更省）
建议：位置 10Hz / 交互事件 / 需求 1Hz / 金钱变化时。我们：位置 2-5Hz（自适应 + 插值）/ 交互事件驱动 / 需求 8s / 金钱变化阈值——**慢节奏游戏用更低频率 + 插值 = 更省带宽**（Gaffer snapshot interpolation 标准）。

### 7. 存档 SHA256 —— ✅ 已实现
host 分发 + SHA256 校验 + 缺块自动重传（v9.4/v9.5）——比建议的"SHA256 检查后下载"更完整。

### 总结论
- **这份建议的架构方向我们已实现 90%**（统一数据包 ✅ / 五层模块化 ✅ / 频率设计 ✅ / 存档校验 ✅）
- **两个"建议但不必做"**：独立服务器（<12 人朋友场景 listen server 是行业推荐）、TCP+UDP 混合（WoW/Minecraft 纯 TCP 先例）
- **真正差距 = 0 项架构级**——剩余都是真机验证（push_super_affordance/背包/关系 API 调用链）
- **方法论**：架构建议要对照"目标场景规模"评估——**12 人朋友联机 ≠ 公开 12 人服务器**，行业对这两种场景的推荐截然不同（listen server vs dedicated）


## 二十、v9.18 启动器房间系统（2026-08-05 百轮研究 + 实施）

> 用户设想：房主在启动器创建房间（**不启动游戏**）→ 房间列表显示房主+用户名 → 对端通过房间码/IP 进入 → 显示对端名字 → 全员准备 → 同步存档 → **最后才启动游戏**。所有房间操作在启动器完成。

### 百轮研究（47 查询）关键确认
| 研究 | 结论 |
|:-----|:-----|
| S4MP 官方流程（simscommunity.info / CurseForge）| "Host → choose save file → Room created + room code → clients join by code → save synced → Everyone's Connected → Start Game → load save" —— **= 用户设想完全一致** |
| EOS Lobby/Session 分离 | **Lobby = 玩家控制的预游戏聚集（启动器房间），Session = 游戏内** —— 正是"启动器房间 + 游戏"模型 |
| Nakama lobby | READY_OP_CODE + all_ready 检查（全员 ready 才允许开始）|
| SaveSync（Steam 工具）| co-op 存档先同步后玩（host 分发 + 校验）|
| 房间生命周期 | 最后玩家离开自动清理（Unity 文档）|

### 架构：启动器房间层（`room_protocol.py`，独立于游戏/GUI）
```
房主启动器: RoomServer (TCP 7660)  ←── RoomClient 加入者启动器
    房间阶段: join/ready/members/save_sync/start_game（JSON 行协议）
    游戏阶段: start_game → 双方写 mod 配置 → 启动游戏 → mod 自动连接 7655
```
- **状态机**：waiting → ready（全员准备）→ syncing（存档同步）→ synced → launching
- **协议消息**：join/joined/join_rejected/ready/members/save_sync_start/save_chunk/save_sync_done/start_game/leave
- **存档同步**：host 选存档 → base64 分块（64KB）→ SHA256 校验 → client 写 Saves + .bak 备份
- **开始游戏**：host 广播 start_game（含 host_ip/game_port）→ 双方写 mod 配置（host/join + IP）→ 启动游戏 → mod auto-apply 连接

### launcher.py 集成
- `_launch` 分流：host → `_create_room()`（RoomServer + 房间页，**不启动游戏**）；join → `_join_room()`（RoomClient）
- 连接页新增「玩家名」「房间码」输入框
- 房间页优先显示启动器房间状态（`_refresh_room_protocol`：房间码/成员/准备/状态机），回退 mod 状态文件
- 按钮：我准备（_toggle_ready）/ 同步存档(房主)（_sync_save）/ 开始游戏(房主)（_start_game → _start_game_after_room）
- 离开房间（_leave_room）清理 server/client + 回连接页

### 坑与修复
- **PyInstaller 没自动收集 room_protocol.py**（try/except import 分析失败）→ 手动复制到 `dist/启动联机/_internal/` + 验证可导入——**打包后必须验证依赖模块在 _internal**
- **get_host_ip 虚拟网卡**：UDP 探测返回 28.0.0.1（FlClash 代理）→ 改枚举本机 IP 优先 192.168/10/172.16 网段
- **测试时序**：存档同步后 client 拼装需要 ~1s，测试 sleep 要给足

### 测试（tools/virtual_test_v918.py，23/23）
A. 房间码（200 个 6 位无易混淆）· B-E. 真实 TCP 全流程（join/成员/ready/SHA256 存档/start_game/错误码拒绝/断开清理）· H. **100 轮循环压力**（建房-加入-准备-离开 ×100 全成功）

### v9.18 交付
- mod 70,774B（13 模块，游戏内同步未变）+ 启动器 v9.18（房间系统）+ room_protocol.py
- 分享版 zip 含 room_protocol（手动复制 _internal）+ 新使用说明（房间流程 4 阶段）
- **双机验证待做**：两台电脑启动器建房→加入→准备→同步存档→开始游戏→mod 自动连接

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
