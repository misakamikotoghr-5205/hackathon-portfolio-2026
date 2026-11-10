# 2026 项目与黑客松作品集

核查与开发日期：2026-11-04至2026-11-09；投稿进度更新至2026-11-10。四个开发代理并行实现、交叉审查；每个项目都有独立公开仓库、运行说明、测试与许可。这里汇总原始五个小红书方向与 Kiro、后来补充的小荷包活动、额外筛选的十个赛事，以及11月9日用户新链接补充的两项，共十九个独立项目。**代码已交付不等于已报名、已提交或已满足平台技术使用条件。**

## 额外十个赛事与对应项目

用户已确认个人开发者身份及基础身份资料，详情保留在私密报名资料中；平台实名、账号可用性和其他个人资格仍须按各赛事核验。以下十项与原始七方向分别对应独立项目。现金赛事、社区 Game Jam 和需入围的分阶段比赛分别说明；GitHub 推送不等于正式参赛。

| 官方赛事 | 截止与阶段 | 独立项目及已实现差异 | 参赛仍需补齐 |
| --- | --- | --- | --- |
| [PayPal AI Hackathon](https://paypalaihackathon.devpost.com/rules) | 北京2026-11-13 04:00 | [Cart Consent](https://github.com/misakamikotoghr-5205/cart-consent-paypal)：购物篮逐字段人工批准、变更撤销、调用竞态复核 | 11月9日官方报名已确认，项目列表为空、未交件；仍缺真实 PayPal sandbox+AI 组合证据及公开少于3分钟YouTube；公共托管非强制 |
| [Aholo 全球3D AI黑客松](https://www.aholo3d.cn/hackathon) | 北京2026-11-19 19:00 | [留白实验室](https://github.com/misakamikotoghr-5205/scene-clearance-lab)：本地模型布置、可解释几何间距、A/B报告 | 单人也须建队；真实 Lux3D 核心资产与兼容性、视频、提交 |
| [支付宝智能体涌现奖](https://emerge.alipay.com/) | 按北京2026-12-06 00:00准备 | [余量接力](https://github.com/misakamikotoghr-5205/pantry-relay)：交互式库存/菜谱录入、来源门禁、预算/偏好、逐笔确认、消费/撤回回执 | 11月9日life方向报名记录与材料草稿已保存，作品1；平台ZIP/安全下线状态待确认、材料待完善，尚无最终交件确认 |
| [Codegeist 2026](https://codegeist2026.devpost.com/rules) | 北京2026-12-23 04:00 | [Dependency Evidence for Jira](https://github.com/misakamikotoghr-5205/dependency-evidence-forge)：依赖证据快照、循环/缺失说明、旧审阅漂移复核；实际 Forge SDK模块 | Atlassian/Forge账号注册、lint/deploy/install、评委安装链接与视频；目前无真实Jira调用 |
| [Builder.io Agent-Native Hackathon](https://www.builder.io/hackathon/rules) | 北京2026-11-10 15:59 | [Patch Review Desk](https://github.com/misakamikotoghr-5205/patch-review-desk)：实际 Agent-Native动作合同、逐hunk人审、基线漂移撤销和持久化回滚 | 11月6日正式提交，官网已确认收到；公开Clips录屏已完成；目前是本机文件工具 |
| [魔搭×Qoder AI+∞第三期](https://mseo-ai-inf.ms.show/) | 官网2026-12-01 12:00报名；18:00交件，未明示时区 | [纸路邮局](https://github.com/misakamikotoghr-5205/paper-route-playtest)：四关可重放派送谜题、精确搜索试玩、隔离变异体反例 | 本人先发构想帖并审核报名、魔搭创空间公开托管、手记/视频；Qoder不是硬性工具要求 |
| [GitHub Game Off 2026](https://itch.io/jam/game-off-2026) | 北京2026-12-02 05:37 | [Lumen Shift](https://github.com/misakamikotoghr-5205/lumen-shift)：八关循环位移与XOR信号解谜、实时搜索提示、可验证重放 | itch.io报名与可玩提交、如实披露AI辅助；社区评奖，未核实现金奖 |
| [Apart AI × Epistemics Research Sprint](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15) | 北京2026-11-16 19:59；11月13–15日研究冲刺 | [Source Trail](https://github.com/misakamikotoghr-5205/source-trail-otari)：精确引用锚点、人工立场冲突门禁与可重复合成评估；Otari是可选适配 | 报名已确认；赛期新增研究、官方模板≤8页PDF及局限/双重用途附录；现有代码和试验均标赛前工作，不以旧仓库代替研究报告 |
| [Next Horizon 2026](https://eisociety.org/hackathon.php?slug=next-horizon-2026) | 11月15日构想，未标具体时刻；11月28–30日48小时构建 | [Watt Window](https://github.com/misakamikotoghr-5205/watt-window)：非关键负载时间窗排程、功率约束、可解释成本与敏感性 | 用户确认构想表已交，待主办方回复/入围；如入围再按48小时构建与路演要求完成 |
| [Through Your Eyes](https://itch.io/jam/through-your-eyes-first-person-game-jam) | 官网11月15日；按平台倒计时核对时区 | [Parallax Postcards](https://github.com/misakamikotoghr-5205/parallax-postcards)：软件光线投射第一人称房间、不同深度碎片对齐、三张原创明信片 | itch.io报名与可玩提交、AI辅助披露；社区Game Jam，无已确认现金奖 |

用户确认 Next Horizon 构想表、AIMA 申请及爱奇艺四款后台投稿已交，PAYATHON 个人报名已在官方参赛中心确认生效、作品仍为0；已进入SkillPay作品表但未提交，尚缺平台链接与有效交易凭证；按所报阶段记录，不重复提交，尚不代表审核通过或最终交件。Builder 已于11月6日在本人确认后正式交件，官网显示收到作品；网页回执私密保留，尚不代表评审通过。Apart 官网明确全球线上、允许个人参与，11月6日已观察到正式报名成功页，回执私密保留；作品提交窗口尚未开启。已有代码必须披露为赛前工作；奖金收取另须符合[官方条款](https://apartresearch.com/sprints/prize-terms)。Next Horizon 的 FAQ 允许初次构想附已有原型，正式构建与入围安排仍须遵守主办方规则。

支付宝[延期公告](https://www.yuque.com/shanxian/dfe94a/xgqqg05f9n3l6lzg?singleDoc#)写12月6日零点；[规则正文](https://www.yuque.com/shanxian/dfe94a/xzter263dyio4ge3?singleDoc#)另有23:59:59的冲突表述，按更早时点准备。

未将 OPC 3.0 第二季计入本轮：官网日期列11月30日，但实际顶部按钮显示“报名已截止”，开放状态矛盾尚未解决。也没有把学生专属赛、已过报名截止的 EthnoHack 或要求未确认组织身份的 AWS MSP 计入十场。[Mozilla Developers Wilding](https://otari.ai/devs-wilding)仍展示邮件报名，但晚报名接受情况和截止时区未确认，仅保留为候选，不占十场名额；Source Trail 的可选 Otari 适配没有实际远程调用或参赛记录。

## 11月9日新链接补充的两项

以下两项独立于已经交付的额外十场，不改变十场名额；MINMAX问卷报名已确认，作品收件仍待组委会确认。

| 官方赛事 | 截止与阶段 | 独立项目及本地证据 | 正式参赛尚缺 |
| --- | --- | --- | --- |
| [QNX Global Hackathon](https://qnx.devpost.com/rules) | 2026-12-15 14:00 EST，即19:00 UTC / 北京12月16日03:00 | [Boot Order Atlas](https://github.com/misakamikotoghr-5205/boot-order-atlas)：分析QNX 8启动脚本受支持子集与显式资源契约，源行诊断、条件等待与修订比较；32项测试、151.6秒英文旁白/字幕的本地主机CLI成片 | [151.6秒YouTube演示](https://youtu.be/K55o50_Tus4)已Public发布；本人确认资格及规则后已Register，官方Thanks for registering!及项目0已核验；正在创建项目，未最终交件。主机工具不等于QNX SDK构建、IFS验证或目标运行；个人具体资格仍按规则核验 |
| [MINMAX AI Agent黑客松](https://www.gba-base.com/newsDetail.html?id=2892&active=true) | 2026-11-10，官方未列具体时刻或时区 | [字幕交接台 Caption Relay](https://github.com/misakamikotoghr-5205/caption-relay)：SRT/VTT检查、程序生成字面词表候选、真实本地模型选择、人审与审计导出；28项测试、8页PDF、106.8秒中文旁白/同步字幕的编辑证据成片 | 11月10日问卷报名已完成，作品邮件已发送；待组委会确认。评委可按公开README本地运行。Sites仅所有者预览且无法连接开发机Ollama，不是公开AI体验 |

Caption的实际HTTP调用返回一条第二句术语候选，另由显式保存响应流程采用`cue-2`并导出SRT、VTT与审计JSON，时间码未变。它不证明全文件模型质量或完整浏览器AI审校/采用/导出。两项演示现均已Public发布：[Deadlock Manor](https://youtu.be/L3BpOsPHobo)和[Boot Order Atlas](https://youtu.be/K55o50_Tus4)。视频发布不等于独立匿名播放验证或赛事最终收件。详细来源和材料状态见[新链接审计](submissions/new-events-20261109.md)。

## 原始七个方向与本次改进

原清单混合了比赛、创作者计划与增长计划，不能全部视作仍开放的黑客松。

| 项目 / 对应方向 | 已有相似项目或产品 | 本轮实际实现的改进 |
| --- | --- | --- |
| [BriefMint](https://github.com/misakamikotoghr-5205/briefmint-skillpay) / PAYATHON | ChatPRD、GitHub Spec Kit、ACT | 免费需求预检：标记缺失材料、重复陈述和来源问题；预检不会创建付费订单或生成付费内容。保留 SQLite 幂等交付与可选官方 A402 适配器。 |
| [AIMA Story Director](https://github.com/misakamikotoghr-5205/aima-story-director) / 智元创作者计划 | Spot 编舞、BehaviorTree.CPP | 从单条 dry-run 扩展为所有可行固定事件分支排练，输出可复现 fixture、时间线与覆盖率；缺失事件不冒充 false。无真实机器人控制。 |
| [CaseDesk](https://github.com/misakamikotoghr-5205/volc-casedesk) / 火山 Agent 先锋计划 | Chatwoot、Haystack | 同日有效政策冲突时保留候选原文，撤回实质性回复并明确交人工；冲突写入追踪与运行标识。 |
| [Move Light](https://github.com/misakamikotoghr-5205/move-light-skill) / 华为 Skill 创新赛 | OR-Tools、py3dbp | 加入箱子/物品边长与直角旋转可放入性；缺失尺寸明确未验证，避免把容积足够当作一定放得下。不是完整三维最优装箱。 |
| [爱奇艺 Play Lab](https://github.com/misakamikotoghr-5205/iqiyi-play-lab) / 玩点新花样 | Bemuse、StepMania、Twine、Shove | 保留四款独立离线应用和四个 ZIP；节奏游戏增加 12 拍校准、异常点过滤和稳定性门槛，静音可玩；修正分镜预览与键盘控件行为。 |
| [Deadlock Manor](https://github.com/misakamikotoghr-5205/deadlock-manor) / Kiroween | T3SF、KubeInvaders（已有模拟模式） | 新增因果回放：回到实际决策时点、保留当时证据、比较同一步替代操作，继续分支并可返回原记录。运行时角色是透明规则，不调用模型；11月9日开发阶段已完成真实Kiro只读审查，Codex据复现结果修复持久化警告并另行修复备份删除顺序。 |
| [慢递愿望局 · Pocket Pause](https://github.com/misakamikotoghr-5205/pocket-pause) / 支付宝小荷包 AI 插件创作 | Actual Budget、wishthis | 购买冷静期与回信流程，把“放下的消费意向”和“手动记录的存入”分开；关联额度校验、保留撤销历史、备份恢复及原创创作词。 |

新补充的[小荷包活动帖](https://www.xiaohongshu.com/discovery/item/6a96b088000000001103af07)已在浏览器查看；官方置顶评论的截止是 **10 月 31 日**，11 月 6 日复查仍无已核实的官方延期，按用户要求跳过。火山申请表明确限定企业开发者，按用户的个人身份跳过。慢递愿望局是可复用原型及候选创作词，未声称存在已验证的第三方插件 SDK、官方 manifest 或已上架插件。

## 开源调查与真实复用

这些方向普遍已有成熟产品和开源实践。这里的“差异化”是已实现的具体用途与工作流，不是全球首创、专利新颖性或比赛获奖保证。原十七个项目和Boot Order Atlas的 `docs/landscape.md` 记录官方来源、固定版本、许可证、相似能力与本项目短板；Caption Relay的来源和比较见其README。各文档记录核查版本，部分项目另附 JSON 与文件指纹。

- **实际复用**：Pocket Pause 使用原样 vendored `idb-keyval@6.3.0`（Apache-2.0）；留白实验室使用原样 vendored `three@0.180.0` 与 OrbitControls（MIT），保留原始署名、完整许可和可验证哈希。Patch Review Desk 实际依赖 `@agent-native/core@0.223.0`（MIT）、`diff@9.0.0`（BSD-3-Clause）及 `zod`（MIT），保留完整许可。Jira 项目实际依赖 Forge SDK，其许可受 **Atlassian Developer Terms** 管理，不把 SDK 称为 MIT。
- **API 适配**：BriefMint 可选官方支付宝 A402 SDK；Cart Consent 可选官方 PayPal sandbox Orders API 与本地 Ollama；Pantry Relay、Patch Review Desk 可选本地 Ollama；Source Trail 可选官方托管 Otari API。未把合同 mock 测试声称为远程集成或真实推理。
- **设计比较而非拷贝**：各仓库列出的其余对照项目仅作设计参考，未复制其代码或素材。AGPL 项目、Spot 的特定 SDK 许可、Chatwoot enterprise 目录和 StepMania 资产的单独授权均有说明，不将“公开源码”一概视为 MIT。

## 交付与核验

各项目 README 提供启动、样例和验证命令，累计 412 项本地测试通过：原351项、Boot Order Atlas 32项、Caption Relay 28项，以及Parallax修复DDA零方向边界新增1项。机器可读交付清单见 [portfolio.json](portfolio.json)，十九个项目 GitHub 本地/远端提交一致性见 [github-verification.json](github-verification.json)。Parallax当前17项测试，上传ZIP已同步到新源码并通过6个根文件、CRC及逐文件匹配核查；未因此记为itch投稿。本地模拟和 API 合同测试验证的是代码行为，不证明真实支付、硬件或主办方后台已联通。Cart、Pantry、Patch及Caption已另存真实本地模型请求与失败记录，仍不等于端到端平台接入。

Deadlock Manor另有[公开GitHub Pages入口](https://misakamikotoghr-5205.github.io/deadlock-manor/)：官方构建成功，匿名主页与5个运行资产200、MIME及源码字节匹配。随后实际完成两条线索→暂停→回滚→验证，在第3回合解决、剩余capacity3、得分90；单步比较、明确继续替代分支及返回原记录均已操作，并下载实际JSON报告。146.8秒本地成片由11张真实浏览器截图剪辑，不是连续录像；已完整解码并核查15帧与31条字幕，未全片人工听审。[媒体记录](https://github.com/misakamikotoghr-5205/deadlock-manor/blob/5fb8bf1abc3bf1b6f05561b2052ff1565400b54a/docs/local-demo-20261109.json)载有哈希；[YouTube演示](https://youtu.be/L3BpOsPHobo)已Public发布，[Devpost最终交件](https://devpost.com/software/deadlock-manor)已由官方“Project submitted!”确认，不代表资格审核或评审通过。

以下Sites托管预览保持**仅所有者可访问**：

- [余量接力](https://pantry-relay-2026.ghraurora1024.chatgpt.site)
- [慢递愿望局](https://pocket-pause-xhb.ghraurora1024.chatgpt.site)
- [留白实验室](https://scene-clearance-lab-aholo.ghraurora1024.chatgpt.site)
- [Deadlock Manor](https://deadlock-manor-kiroween-2026.ghraurora1024.chatgpt.site)
- [爱奇艺 Play Lab](https://iqiyi-play-lab-2026.ghraurora1024.chatgpt.site)
- [纸路邮局](https://paper-route-playtest-2026.ghraurora1024.chatgpt.site)
- [Lumen Shift](https://lumen-shift-gameoff-2026.ghraurora1024.chatgpt.site)
- [Parallax Postcards](https://parallax-postcards-2026.ghraurora1024.chatgpt.site)
- [字幕交接台 Caption Relay](https://caption-relay-hengrui-2026.ghraurora1024.chatgpt.site)

公开 GitHub 的本地运行说明可用于代码审阅；所有者私有预览不能直接当作评委可访问的公开 Demo。Caption预览仅托管UI，不能访问开发机的本地Ollama；其完整AI试用路径是公开仓库README的本机运行说明。已完成Apart正式报名、Clips登录及免费视频存储开通，并保存[2分04秒公开录屏](https://clips.agent-native.com/share/r01FTO1ytVvm)。Builder 已于11月6日正式提交，官网显示“Your project submission has been received.”，未订阅营销信息。11月9日PayPal报名已由官方页面确认，项目列表仍为空；Kiroween于11月10日已保存最新Markdown Story和Additional Info，返回页面后核验仓库/公开游戏链接、测试说明、Kiro技术说明与复用披露均持久化；本人明确同意最终条款后已实际Submit，[公开项目页](https://devpost.com/software/deadlock-manor)显示“Project submitted!”及“Submitted to Kiroween 2026”，正式交件已确认；提交时源版本为3227460b，不代表资格审核或评审通过。[截图剪辑演示](https://youtu.be/L3BpOsPHobo)已Public发布；11月9日已完成一次真实Kiro CLI只读审查，Codex复现并实现持久化修复（[记录及归因](https://github.com/misakamikotoghr-5205/deadlock-manor/blob/83ab65a92bcfdaebb04589cd7a8fa1a272ada2b3/docs/kiro-usage.md)），不声称Kiro编写原应用或执行测试。4000额度申请已获[官方收件确认](submissions/evidence/kiroween-credits-request-20261109.json)，待审核及Didit身份核验，尚无获批或到账确认。Kiro使用说明入表、Lux3D真实生成、支付sandbox、公开演示与正式交件等剩余事项均在对应仓库明确列出。完整[报名材料、状态及尚缺项](submissions/README.md)已备，当前独立核验的报名阶段为6项（Apart、PAYATHON个人报名、涌现奖已建记录、PayPal、MINMAX问卷报名、QNX），最终作品提交回执现为2份（Builder、Kiroween）；独立报名阶段与最终作品收件分开计数，不将最终交件自动追加到报名数；另记录上述用户确认的阶段进度。
