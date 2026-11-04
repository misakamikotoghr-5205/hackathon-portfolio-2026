# 2026 项目与黑客松作品集

核查与开发日期：2026-11-04。四个开发代理并行实现、交叉审查；每个项目都有独立公开仓库、运行说明、测试与许可。这里汇总原始五个小红书方向与 Kiro、后来补充的小荷包活动，以及新筛选的三个线上赛事，共十个独立项目。**代码已交付不等于已报名、已提交或已满足平台技术使用条件。**

## 新筛选的三个线上赛事

以下按“中国大陆成年个人开发者”的暂定情况筛选；用户身份、账号、利益冲突和领奖条件尚未逐人核验。截止均为北京时间 UTC+8，须以主办方最新公告为准。

| 官方赛事与截止 | 独立项目 | 差异化落点 | 仍需真实完成的参赛条件 |
| --- | --- | --- | --- |
| [PayPal AI Hackathon](https://paypalaihackathon.devpost.com/rules)，2026-11-13 04:00 | [Cart Consent](https://github.com/misakamikotoghr-5205/cart-consent-paypal) | 模型提议商品，人工批准精确购物篮；价格、运费、地址、预算等变化撤销批准；持久化幂等与调用期间竞态检查 | 合法可用的 PayPal Business/developer/sandbox 账号，真实 sandbox 与 AI 运行，英文材料及三分钟内公开视频。公开排除地区清单未列中国大陆，不代表保证个人资格或账号可用。 |
| [Aholo 全球 3D AI 黑客松](https://www.aholo3d.cn/hackathon)，2026-11-19 19:00 | [留白实验室](https://github.com/misakamikotoghr-5205/scene-clearance-lab) | 生成模型的下游布局工具：本地 glTF/GLB、保守几何间距解释、A/B 方案与来源报告 | 个人也要创建团队；实际用 Lux3D 生成核心资产并合法导出、验证兼容、制作运行视频。目前内置场景是原创程序几何，不能替代 Lux3D 证据。 |
| [支付宝智能体涌现奖](https://emerge.alipay.com/)，按最早截止 2026-12-06 00:00 准备 | [余量接力 · Pantry Relay](https://github.com/misakamikotoghr-5205/pantry-relay) | 标签证据与人工确认门禁，受约束的菜谱选择，库存原子扣减与可重试消耗回执 | 本人合法实名支付宝及赛事账号、真实 AI 演示、提交材料。个人或 2–4 人团队；同一作品不能重复投其他大赛；Q Muse 推荐但可选。 |

支付宝[最新延期公告](https://www.yuque.com/shanxian/dfe94a/xgqqg05f9n3l6lzg?singleDoc#)明确写 12 月 6 日零点；[规则正文](https://www.yuque.com/shanxian/dfe94a/xzter263dyio4ge3?singleDoc#)另有 23:59:59 的矛盾表述。因此按较早时点准备，正式提交前再核对门户。上述三件作品用途、数据与实现相互独立，不用同一个项目换名重复投递。

## 原始七个方向与本次改进

原清单混合了比赛、创作者计划与增长计划，不能全部视作仍开放的黑客松。

| 项目 / 对应方向 | 已有相似项目或产品 | 本轮实际实现的改进 |
| --- | --- | --- |
| [BriefMint](https://github.com/misakamikotoghr-5205/briefmint-skillpay) / PAYATHON | ChatPRD、GitHub Spec Kit、ACT | 免费需求预检：标记缺失材料、重复陈述和来源问题；预检不会创建付费订单或生成付费内容。保留 SQLite 幂等交付与可选官方 A402 适配器。 |
| [AIMA Story Director](https://github.com/misakamikotoghr-5205/aima-story-director) / 智元创作者计划 | Spot 编舞、BehaviorTree.CPP | 从单条 dry-run 扩展为所有可行固定事件分支排练，输出可复现 fixture、时间线与覆盖率；缺失事件不冒充 false。无真实机器人控制。 |
| [CaseDesk](https://github.com/misakamikotoghr-5205/volc-casedesk) / 火山 Agent 先锋计划 | Chatwoot、Haystack | 同日有效政策冲突时保留候选原文，撤回实质性回复并明确交人工；冲突写入追踪与运行标识。 |
| [Move Light](https://github.com/misakamikotoghr-5205/move-light-skill) / 华为 Skill 创新赛 | OR-Tools、py3dbp | 加入箱子/物品边长与直角旋转可放入性；缺失尺寸明确未验证，避免把容积足够当作一定放得下。不是完整三维最优装箱。 |
| [爱奇艺 Play Lab](https://github.com/misakamikotoghr-5205/iqiyi-play-lab) / 玩点新花样 | Bemuse、StepMania、Twine、Shove | 保留四款独立离线应用和四个 ZIP；节奏游戏增加 12 拍校准、异常点过滤和稳定性门槛，静音可玩；修正分镜预览与键盘控件行为。 |
| [Deadlock Manor](https://github.com/misakamikotoghr-5205/deadlock-manor) / Kiroween | T3SF、KubeInvaders（已有模拟模式） | 新增因果回放：回到实际决策时点、保留当时证据、比较同一步替代操作，继续分支并可返回原记录。角色是透明规则，无真实模型。 |
| [慢递愿望局 · Pocket Pause](https://github.com/misakamikotoghr-5205/pocket-pause) / 支付宝小荷包 AI 插件创作 | Actual Budget、wishthis | 购买冷静期与回信流程，把“放下的消费意向”和“手动记录的存入”分开；关联额度校验、保留撤销历史、备份恢复及原创创作词。 |

新补充的[小荷包活动帖](https://www.xiaohongshu.com/discovery/item/6a96b088000000001103af07)已在浏览器查看；官方置顶评论的截止是 **10 月 31 日**，11 月 4 日已结束，未核实后续重开。慢递愿望局是可复用原型及候选创作词，未声称存在已验证的第三方插件 SDK、官方 manifest 或已上架插件。

## 开源调查与真实复用

这些方向普遍已有成熟产品和开源实践。这里的“差异化”是已实现的具体用途与工作流，不是全球首创、专利新颖性或比赛获奖保证。每个仓库的 `docs/landscape.md` 记录官方来源、固定版本、许可证、相似能力与本项目短板；各文档记录核查版本，部分项目另附 JSON 与文件指纹。

- **实际复用**：Pocket Pause 使用原样 vendored `idb-keyval@6.3.0`（Apache-2.0）；留白实验室使用原样 vendored `three@0.180.0` 与 OrbitControls（MIT）。均保留原始署名、完整许可和可验证哈希。
- **API 适配**：BriefMint 可选官方支付宝 A402 SDK；Cart Consent 可选官方 PayPal sandbox Orders API 与本地 Ollama；Pantry Relay 可选本地 Ollama。未把合同 mock 测试声称为远程集成或真实推理。
- **设计比较而非拷贝**：其他表列仓库未复制代码或素材。AGPL 项目、Spot 的特定 SDK 许可、Chatwoot enterprise 目录和 StepMania 资产的单独授权均有说明，不将“公开源码”一概视为 MIT。

## 交付与核验

各项目 README 提供启动、样例和验证命令，累计 211 项本地测试通过。机器可读交付清单见 [portfolio.json](portfolio.json)，十个项目 GitHub 本地/远端提交一致性见 [github-verification.json](github-verification.json)。本地模拟和 API 合同测试验证的是代码行为，不证明真实支付、硬件、模型或主办方后台已联通。

可用的托管预览保持**仅所有者可访问**：

- [慢递愿望局](https://pocket-pause-xhb.ghraurora1024.chatgpt.site)
- [留白实验室](https://scene-clearance-lab-aholo.ghraurora1024.chatgpt.site)
- [Deadlock Manor](https://deadlock-manor-kiroween-2026.ghraurora1024.chatgpt.site)
- [爱奇艺 Play Lab](https://iqiyi-play-lab-2026.ghraurora1024.chatgpt.site)

公开 GitHub 的本地运行说明可用于代码审阅；所有者私有预览不能直接当作评委可访问的公开 Demo。尚未替用户注册、接受赛事条款、发帖、上传视频或正式提交。Kiro 实际贡献、Lux3D 真实生成、支付 sandbox 与模型运行等未完成条件均在对应仓库明确列出。
