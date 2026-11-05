# 2026 项目与黑客松作品集

核查与开发日期：2026-11-04至2026-11-05。四个开发代理并行实现、交叉审查；每个项目都有独立公开仓库、运行说明、测试与许可。这里汇总原始五个小红书方向与 Kiro、后来补充的小荷包活动，以及额外筛选的十个赛事，共十七个独立项目。**代码已交付不等于已报名、已提交或已满足平台技术使用条件。**

## 额外十个赛事与对应项目

用户已确认个人开发者身份；年龄、学生身份与居住地区尚未确认，先按成年中国大陆个人筛选，不保证个人最终资格。以下十项与原始七方向分别对应独立项目。现金赛事、社区 Game Jam 和需入围的分阶段比赛分别说明；GitHub 推送不等于正式参赛。

| 官方赛事 | 截止与阶段 | 独立项目及已实现差异 | 参赛仍需补齐 |
| --- | --- | --- | --- |
| [PayPal AI Hackathon](https://paypalaihackathon.devpost.com/rules) | 北京2026-11-13 04:00 | [Cart Consent](https://github.com/misakamikotoghr-5205/cart-consent-paypal)：购物篮逐字段人工批准、变更撤销、调用竞态复核 | 合法可用的 Business/sandbox 账号、真实 PayPal+AI 演示、英文材料与视频 |
| [Aholo 全球3D AI黑客松](https://www.aholo3d.cn/hackathon) | 北京2026-11-19 19:00 | [留白实验室](https://github.com/misakamikotoghr-5205/scene-clearance-lab)：本地模型布置、可解释几何间距、A/B报告 | 单人也须建队；真实 Lux3D 核心资产与兼容性、视频、提交 |
| [支付宝智能体涌现奖](https://emerge.alipay.com/) | 按北京2026-12-06 00:00准备 | [余量接力](https://github.com/misakamikotoghr-5205/pantry-relay)：标签来源门禁、受约束选菜、库存消费回执 | 本人实名账号、真实 AI 演示、URL/ZIP提交；同一作品不重复投别赛 |
| [Codegeist 2026](https://codegeist2026.devpost.com/rules) | 北京2026-12-23 04:00 | [Dependency Evidence for Jira](https://github.com/misakamikotoghr-5205/dependency-evidence-forge)：依赖证据快照、循环/缺失说明、旧审阅漂移复核；实际 Forge SDK模块 | Atlassian/Forge账号注册、lint/deploy/install、评委安装链接与视频；目前无真实Jira调用 |
| [Builder.io Agent-Native Hackathon](https://www.builder.io/hackathon/rules) | 北京2026-11-10 15:59 | [Patch Review Desk](https://github.com/misakamikotoghr-5205/patch-review-desk)：实际 Agent-Native动作合同、逐hunk人审、基线漂移撤销和持久化回滚 | 真实完整操作录屏与公开Clips演示、本人提交；目前是本机文件工具 |
| [魔搭×Qoder AI+∞第三期](https://mseo-ai-inf.ms.show/) | 官网2026-12-01 12:00报名；18:00交件，未明示时区 | [纸路邮局](https://github.com/misakamikotoghr-5205/paper-route-playtest)：四关可重放派送谜题、精确搜索试玩、隔离变异体反例 | 本人先发构想帖并审核报名、魔搭创空间公开托管、手记/视频；Qoder不是硬性工具要求 |
| [GitHub Game Off 2026](https://itch.io/jam/game-off-2026) | 北京2026-12-02 05:37 | [Lumen Shift](https://github.com/misakamikotoghr-5205/lumen-shift)：八关循环位移与XOR信号解谜、实时搜索提示、可验证重放 | itch.io报名与可玩提交、如实披露AI辅助；社区评奖，未核实现金奖 |
| [Apart AI × Epistemics Research Sprint](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15) | 北京2026-11-16 19:59；11月13–15日研究冲刺 | [Source Trail](https://github.com/misakamikotoghr-5205/source-trail-otari)：精确引用锚点、人工立场冲突门禁与可重复合成评估；Otari是可选适配 | 本人报名、赛期新增研究、官方模板≤8页PDF及局限/双重用途附录；现有代码和试验均标赛前工作，不以旧仓库代替研究报告 |
| [Next Horizon 2026](https://eisociety.org/hackathon.php?slug=next-horizon-2026) | 11月15日构想，未标具体时刻；11月28–30日48小时构建 | [Watt Window](https://github.com/misakamikotoghr-5205/watt-window)：非关键负载时间窗排程、功率约束、可解释成本与敏感性 | 有限名额/入围、本人的PPT与路演；本轮代码是赛前原型，不冒称48小时成果 |
| [Through Your Eyes](https://itch.io/jam/through-your-eyes-first-person-game-jam) | 官网11月15日；按平台倒计时核对时区 | [Parallax Postcards](https://github.com/misakamikotoghr-5205/parallax-postcards)：软件光线投射第一人称房间、不同深度碎片对齐、三张原创明信片 | itch.io报名与可玩提交、AI辅助披露；社区Game Jam，无已确认现金奖 |

所有项目的个人资格、第三方账号与正式提交均待本人核验。Apart 官网明确全球线上、允许个人参与，11月5日实查可打开启用的报名表；作品提交窗口尚未开启，不把它与报名关闭混淆。已有代码必须披露为赛前工作；奖金收取另须符合[官方条款](https://apartresearch.com/sprints/prize-terms)。Next Horizon 的 FAQ 允许初次构想附已有原型，正式构建与入围安排仍须遵守主办方规则。

支付宝[延期公告](https://www.yuque.com/shanxian/dfe94a/xgqqg05f9n3l6lzg?singleDoc#)写12月6日零点；[规则正文](https://www.yuque.com/shanxian/dfe94a/xzter263dyio4ge3?singleDoc#)另有23:59:59的冲突表述，按更早时点准备。

未将 OPC 3.0 第二季计入本轮：官网日期列11月30日，但实际顶部按钮显示“报名已截止”，开放状态矛盾尚未解决。也没有把学生专属赛、已过报名截止的 EthnoHack 或要求未确认组织身份的 AWS MSP 计入十场。[Mozilla Developers Wilding](https://otari.ai/devs-wilding)仍展示邮件报名，但晚报名接受情况和截止时区未确认，仅保留为候选，不占十场名额；Source Trail 的可选 Otari 适配没有实际远程调用或参赛记录。

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

- **实际复用**：Pocket Pause 使用原样 vendored `idb-keyval@6.3.0`（Apache-2.0）；留白实验室使用原样 vendored `three@0.180.0` 与 OrbitControls（MIT），保留原始署名、完整许可和可验证哈希。Patch Review Desk 实际依赖 `@agent-native/core@0.223.0`（MIT）、`diff@9.0.0`（BSD-3-Clause）及 `zod`（MIT），保留完整许可。Jira 项目实际依赖 Forge SDK，其许可受 **Atlassian Developer Terms** 管理，不把 SDK 称为 MIT。
- **API 适配**：BriefMint 可选官方支付宝 A402 SDK；Cart Consent 可选官方 PayPal sandbox Orders API 与本地 Ollama；Pantry Relay、Patch Review Desk 可选本地 Ollama；Source Trail 可选官方托管 Otari API。未把合同 mock 测试声称为远程集成或真实推理。
- **设计比较而非拷贝**：各仓库列出的其余对照项目仅作设计参考，未复制其代码或素材。AGPL 项目、Spot 的特定 SDK 许可、Chatwoot enterprise 目录和 StepMania 资产的单独授权均有说明，不将“公开源码”一概视为 MIT。

## 交付与核验

各项目 README 提供启动、样例和验证命令，累计 326 项本地测试通过。机器可读交付清单见 [portfolio.json](portfolio.json)，十七个项目 GitHub 本地/远端提交一致性见 [github-verification.json](github-verification.json)。本地模拟和 API 合同测试验证的是代码行为，不证明真实支付、硬件、模型或主办方后台已联通。

可用的托管预览保持**仅所有者可访问**：

- [慢递愿望局](https://pocket-pause-xhb.ghraurora1024.chatgpt.site)
- [留白实验室](https://scene-clearance-lab-aholo.ghraurora1024.chatgpt.site)
- [Deadlock Manor](https://deadlock-manor-kiroween-2026.ghraurora1024.chatgpt.site)
- [爱奇艺 Play Lab](https://iqiyi-play-lab-2026.ghraurora1024.chatgpt.site)
- [纸路邮局](https://paper-route-playtest-2026.ghraurora1024.chatgpt.site)
- [Lumen Shift](https://lumen-shift-gameoff-2026.ghraurora1024.chatgpt.site)
- [Parallax Postcards](https://parallax-postcards-2026.ghraurora1024.chatgpt.site)

公开 GitHub 的本地运行说明可用于代码审阅；所有者私有预览不能直接当作评委可访问的公开 Demo。尚未替用户注册、接受赛事条款、发帖、上传视频或正式提交。Kiro 实际贡献、Lux3D 真实生成、支付 sandbox 与模型运行等未完成条件均在对应仓库明确列出。
