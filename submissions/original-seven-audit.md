# Original seven directions — registration and submission audit

规则核对日期：**2026-11-06 UTC**；阶段进度更新：**2026-11-09 UTC**。本文件可公开，不包含身份、联系方式、账户标识或凭据。它记录入口与尚未完成的条件，不是报名/发布/签约/获奖证明。账号持有人在登录后填写的字段、接受的条款及最终回执应保存在私密交付记录中。

“开放”仅表示官方日程尚未截止，不代表当前项目已满足参赛资格。没有以 GitHub 推送、Owner-only 预览或本地测试替代平台提交。

## 状态总表

| 方向 / 当前项目 | 2026-11-06 结论 | 截止与时间边界 | 下一项实际门槛 |
| --- | --- | --- | --- |
| PAYATHON / `briefmint-skillpay` | 正式比赛，官方报名开放 | **北京时间**报名 12/1 23:59:59、作品 12/9 23:59:59；12/26 线下决赛 | 支付宝手机绑定/大陆身份实人认证；报名与支付接入同账户；选定赛道并真实接入 |
| AIMA / `aima-story-director` | 持续创作者扶持计划，无当前明确硬截止；不是单次通用代码比赛 | 未公布可据以承诺的统一截止 | 用户确认申请已交，后续跟进审核/原生有效作品；GitHub 工具不自动满足作品门槛 |
| 火山 / `volc-casedesk` | Agent 先锋申请表明确仅面向企业开发者；当前已声明的个人身份不足以确认资格 | 官方公告未列截止；不等于承诺永久开放 | 真实公司全称、企业邮箱、岗位、微信与火山账号、实际产品案例；不能编造企业身份 |
| 华为×小红书 / `move-light-skill` | 正式 Skill 创新赛，当前开放；11/6 官方门户实读 | 报名/作品截止 **11/24**，未写具体时分；12/11–13 线下决赛 | 华为云报名建队；真实 CodeArts/OfficeAce 使用；两个市场都发布，至少一条指定话题笔记 |
| 爱奇艺 / `iqiyi-play-lab` | AI 互动小应用征集赛，投稿期内 | 11/4 00:00–12/3 23:59；页面未显式标注时区，按北京时间提前准备并后台核对 | 用户确认四款后台已投稿；继续跟进审核通过、上线及活动归属 |
| Kiroween / `deadlock-manor` | 真实Kiro只读审查已完成；Story及项目资料已保存、仍2/5步骤；Additional未保存，未最终交件 | **12/4 14:00 PST = 12/4 22:00 UTC = 12/5 06:00 北京时间** | 完成Additional保存，上传已完成的本地成片到公开YouTube并最终交件；额度申请已收件，待审核及Didit身份核验，尚无到账确认 |
| 小荷包 / `pocket-pause` | 原活动已结束；不能按原届补交 | 原官方置顶截止 10/31；未核实延期/新届 | 仅作为后续普通创作候选；有新活动才重新核对 |

## 1. PAYATHON 2026 — BriefMint

**官方入口：**[赛事与报名](https://aipay.alipay.com/community/events/payathon-2026)、[活动细则](https://render.alipay.com/p/yuyan/180022670000190962/index.html)。11/6 主赛页直接读取；细则动态页面的官方[公开内容资源](https://gw.alipayobjects.com/render/p/yuyan/180022670000190962/async.5d83c7dc.js)下载后仅静态提取正文，未执行 JavaScript、登录或接受协议。细则明确所有时间为北京时间。

官方允许个人或 2–5 人团队，未成年需监护同意；个人或队长需支付宝绑定手机号并完成实人认证，港澳台或外籍实名身份当前不能报名。**报名账户必须与接入 AI 付产品的账户相同。**细则列必要资料含手机号、邮箱、昵称与头像，账号页面可能还有队伍等字段，仍以实际表单为准；报名账号承担团队管理与奖励结算责任。同一作品不得跨赛道重复投递。[官方细则](https://render.alipay.com/p/yuyan/180022670000190962/index.html)

作品需原创且权利合法、正式部署发布并在评审期可体验，接入至少一款 AI 付产品的完整付款与交付链路。开发工具不限；当前本地模拟不构成真实交易或商业验证。[官方细则](https://render.alipay.com/p/yuyan/180022670000190962/index.html)

接受前需本人完整阅读细则中的知识产权授权、平台产品衍生成果归属、个人信息用途与线下影像等条款。本审计不代作法律解释或接受；尤其不能把参赛授权描述为“无额外条款”。

**Skill Pay 路径：**[商品上架](https://skillpay.alipay.com/creator/product-new)公开页面显示 Skill 文件、商品名称、售卖模式及价格配置；支持 ZIP/Markdown/文件夹，单文件不超过 20 MB。需完成 SkillPay、AI 按量付费、即刻收三项协议授权，最终以账号审核为准。买断/订阅模式选择后不可更改，不能代用户随意选择价格或签约。[官方上架页](https://skillpay.alipay.com/creator/product-new)

**当前可交材料：**MIT 公共仓库、`dist/briefmint-skill.zip`、本地 preflight/付款门禁/确认重试演示、`docs/submission-draft.md`。当前 API 的 A402 适配对应独立的 [Machine Pay](https://aipay.alipay.com/products/machine-pay)，不能写成 SkillPay 商城已接通。尚无真实商户/服务开通、沙箱交易、生产收款、付费用户、平台上架或正式报名。先由账号持有人确定赛道，再核对产品准入和服务注册。

## 2. 智元 AIMA 百大创作者计划 — Story Director

**当前主入口：**[官方创作者计划](https://open.agibot.com/creator-plan)、[官方 PDF 细则](https://open.agibot.com/files/creator-plan-rules.pdf)；[灵创平台](https://linkcraft.agibot.com/)和[灵心平台](https://linksoul.agibot.com/)是实际内容平台。11/6 主智能体通过官方首页 Banner 到达新入口并读取，旧活动 query 会重定向首页；本审计另以公开 HTTP 下载七页官方 PDF、用 pypdf 提取正文交叉确认，不是凭旧链接推断开放状态。

官方面向个人/团队且无粉丝门槛。至少一件在灵心/灵创发布的有效作品才满足入门作品门槛；申请“新秀”需至少十件有效作品、累计至少二十次有效使用；AIMA 之星还需季度评审。实际创作能力与有效作品接受评审，单个 GitHub 仓库不自动符合。当前未见明确统一硬截止，属持续扶持计划；不保证任何申请会获准或获得真机。真机体验需运营/元苼等另行申请。[官方计划](https://open.agibot.com/creator-plan)

“报名加入”实际跳转智元统一登录页，支持手机验证码、邮箱或账号密码；登录/注册勾选项包含用户协议、隐私政策和本人已满十八岁确认。11/6 初次公开核查时未勾选、未输入、未登录。随后已在本人当次确认账号协议后完成短信账号登录；实际页面显示已登录账号入口，并另外弹出“智元AIMA开放平台用户协议及隐私政策”，该份平台协议后来已按本人当次同意接受。11月7日用户又明确确认AIMA申请已交，按申请阶段记录、不重复申请；操作者未独立取得申请回执或通过结果，原生作品有效性仍待核验。

当前离线导演可提供三个原创场景、分支排练、时间线和 SVG，但未发布任何灵心/灵创作品、无真实有效使用次数、无 AimDK/机型适配或硬件记录。不能填“已有十件作品”或以离线 JSON 当作原生动作资源。`docs/submission-draft.md`仅是申请介绍候选。

## 3. 火山引擎 Agent 先锋计划 — CaseDesk

**主源：**[原官方招募公告](https://www.xiaohongshu.com/discovery/item/6ae40ee40000000025019237)、[作者置顶申请表](https://bytedance.larkoffice.com/share/base/form/shrcn1BuElmO6eHhOOYd3IBdvzb)。11/6 主智能体浏览器以原分享令牌读取公告及置顶链接：面向企业开发者、技术骨干、架构师与 AI 负责人的持续成长计划，不是普通现金比赛；正文未列截止。本公开文件去除分享令牌，不承诺无令牌即可打开 XHS。不能把未列日期视为无限期开放。

**11/6 实际申请表已读取：**身份字段帮助文字明确“本次 Agent 先锋计划仅面向企业开发者”，虽然下拉也列学生、个人开发者和其他，不能据此忽略资格说明。必填包括姓名、联系电话、身份类型、公司全称、企业邮箱、岗位职责、微信号、常用火山账号 ID（10 位数字）、约 300 字真实产品/模型使用感受、实际火山案例附件和案例超链接（已传演示/PDF时帮助文字允许链接填“无”）；行业、城市为可选。申请通过后才加入社群，表内说约两周审核。未输入身份资料、未提交。

当前仅已确认个人开发者身份，不能认定符合企业限定；若确有真实企业任职或主办方明确批准，再按实际资料申请。不要为了满足字段编造公司、职位、企业邮箱、客户、使用体验或平台调用记录。

CaseDesk 可作为真实工作流演示：虚构工单与政策、来源定位、过期策略、冲突暂扣和人工交接。本地四角色是确定性流程。可选 [Ark Chat API](https://docs.volcengine.com/docs/ark/chat-api?lang=zh&redirect=1) 适配存在，但未实际调用；付费调用默认关闭，无客户消息外发。若活动要求 Ark 实际案例，需要真实授权、模型、预算和调用记录，不能仅凭适配代码声称完成。准备文案位于 `docs/submission-draft.md`。

## 4. 华为×小红书 Skill 创新赛 — Move Light

**官方入口：**[赛事门户](https://developer.huaweicloud.com/competition/information/1300000350/introduction)、[官方 Skill 创作与上传步骤](https://support.huaweicloud.com/offers-codeartsagent/codeartsagent_offers_0008.html)、[华为云 Skill 市场](https://skills.huaweicloud.com/)、[小红书创作平台](https://creator.xiaohongshu.com/)。

11/6 主智能体通过浏览器实读官方赛事页：个人或 2–5 人团队，每人仅可加入一队；登录华为云报名后在“我的团队”建队。报名/作品截止 2026-11-24，未写具体时分；12/11–13 线下决赛。[赛事门户](https://developer.huaweicloud.com/competition/information/1300000350/introduction)

赛事[创作与提交页](https://developer.huaweicloud.com/competition/information/1300000350/html3)要求至少实际使用 CodeArts 或 OfficeAce 之一，并将 Skill **同时发布华为云和小红书两个市场**；至少发布一条小红书笔记，带 `#小红书Skill创新赛` 和 `#2026华为开发者大赛`。比赛规则高于通用文档中“或”市场的操作例子。已有本地 Skill 可按官方建议在 IDE 上传/优化；当前 Linux 环境优先 CodeArts 网页/IDE，OfficeAce 的 Windows 版本和免费订阅是不同工具路径，不虚构已使用。

官方步骤建议先华为市场，再通过 `redskillhub-upload` 发布小红书；授权过程中按实际提示填写。CodeArts 的[通用上传说明](https://support.huaweicloud.com/offers-codeartsagent/codeartsagent_offers_0008.html)还说明如何查询作品与重新生成过期授权二维码。不要把 ZIP 打包视为市场上架；具体身份/实名认证与提交表单仍需实际登录核对。第三方 11/13、11/16 等日期不采用。

**可交候选：**`submission/move-light.zip`、虚构家庭与尺寸样例、README、MIT 与 `docs/submission-draft.md`。当前未在 CodeArts/OfficeAce 实际创作或改进、未上传任一市场、未完成报名/平台演示/社交发布。需真实平台贡献后才可填写使用证明。工具不联系搬家商、不预订或付款。

## 5. 爱奇艺“玩点新花样” — four independent apps

**主源与入口：**[官方活动](https://aic.iqiyi.com/activity/ai-contest-2026)、[爱奇艺号创作者后台](https://creator.iqiyi.com/)、[使用手册 v11](https://aic.iqiyi.com/activity/campaign/assets/interactive-app-guide-v11.pdf)、[投稿操作手册 v6](https://aic.iqiyi.com/activity/campaign/assets/submission-guide-v6.pdf)、[完整开发者规范](https://pages.iqiyi.com/up/interactive-app.html)。11/6 官方搜索索引和主智能体浏览器实读交叉确认活动正文；两份投稿 PDF 经公开 HTTP 下载、pypdf 提取读取，未触碰账号。完整开发者规范网页本轮未能读取，不宣称完成了其全部条款核验。

活动面向爱奇艺创作者，通过后台上传作品，并在参与活动中勾选本届名称。现金相关奖项要求至少四款实质不同的原创应用在截止前提交、审核通过并上线；换皮、重复、未经实质创作的模板不能凑数。需纯前端离线 ZIP、≤20 MB、根目录 `index.html`、无外部请求/外链，竖屏可用，素材有合法权利。[官方规则](https://aic.iqiyi.com/activity/ai-contest-2026)

四款已准备独立 ZIP：`rain-alley.zip`、`cat-dispatch.zip`、`frame-director.zip`、`echo-rhythm.zip`，并有体积/SHA 清单与四份简介（`docs/submission-draft.md`）。不能把合集上传一次算四款。没有第三方影视 IP；不申报需要授权 IP 的专项事实。官方邀请使用纳逗 Pro“等工具”，当前不能声称实际用了纳逗 Pro。

当前 v11 使用手册明确发布前须实名认证，进入“互动小应用 → 去发布”，校验代码、上传后填**名称、简介、分类、封面**并预览。未看到发布入口时联系运营确认权限，不断言所有账号均须白名单；较旧 v6 另有“面向全量创作者开放”和“开通白名单”字样，按当前 v11 与真实账号结果核对。提交成功不等于上线，应在“内容管理 → 互动小应用”查看审核状态；审核中不能修改。[v11 官方使用手册](https://aic.iqiyi.com/activity/campaign/assets/interactive-app-guide-v11.pdf)、[v6 投稿手册](https://aic.iqiyi.com/activity/campaign/assets/submission-guide-v6.pdf)

此前浏览器短信登录曾遇账号安全认证；11月7日用户明确确认四款已在创作者后台投稿，按该阶段记录，不要求重复上传。后台投稿不等于审核通过、上线或赛事归属已确认；操作者未独立核验官方回执。四款独立ZIP及8张原创封面、四款共5张真实桌面局部截图、中文字段、AI/版权声明已备，见[逐款上传材料](https://github.com/misakamikotoghr-5205/iqiyi-play-lab/tree/main/submission)。分类、版权与 AI 声明等完整字段以登录后的真实表单为准，未伪称全部已核实必填。还需手机平台 WebView 的触控、存档、音频与切后台验证，以及四个真实作品 ID/上线审核结果。当前不接激励广告，无需为本原型虚构广告合作或分成记录。

## 6. Kiroween 2026 — Deadlock Manor

**入口：**[Join hackathon / Devpost](https://kiroween.devpost.com/)、[官方规则](https://kiroween.devpost.com/rules)。11/6 两页直接读取。成年个人、最多三人团队或合格组织可参加；中国大陆未列于明确排除名单，但本人所在地、雇佣/亲属利益冲突及当地法律条件仍须如实核对。注册需 Devpost 账户；提交即构成接受规则，须由账号持有人处理。

仅接受 10/30 09:00 Pacific 后新建、比赛期间完成且**真实使用 Kiro**的作品。需公共 GitHub 与开源许可、根 `.kiro`、可测试应用 URL、功能描述、Kiro 使用说明、公开 YouTube 演示（小于三分钟；英文或英文翻译）。选择 Costume Contest。无事实依据不勾学生/创业/往届等奖项。[赛事要求](https://kiroween.devpost.com/)

Kiro 账户/模型可用性另有地区条件。[官方 FAQ](https://kiro.dev/faq/)目前列 China 为个人付费计划账单支持地区，同时明确模型依提供者地区要求而异；不能从可付费推断任意模型可用。Startup credits 排除与本赛事积分不同，不混写。无需通过购买取得参赛资格。

11月9日已在Devpost现有草稿保存名称Deadlock Manor，随后已实际保存Story、JavaScript标签与仓库，Save & continue进入Additional Info；仍显示2/5 steps，Additional编辑尚未保存，尚未最终提交；不从草稿进度推断新的官方报名回执。同日已通过已认证官方Kiro CLI 3.0.0完成92.614秒只读审查，仅fs_read；Codex复现其中两项警告问题、拒绝推测性发现并实现修复，另行发现修复备份删除顺序问题，27项测试通过。Kiro未编写原应用或执行测试，Codex写的`.kiro`仍不冒充Kiro产物（[真实记录及评估](https://github.com/misakamikotoghr-5205/deadlock-manor/blob/83ab65a92bcfdaebb04589cd7a8fa1a272ada2b3/docs/kiro-usage.md)）。准确说明已随Story保存，仍须完成Additional保存，上传现有本地成片到公开YouTube及最终交件；主办方是否认可全部参赛条件尚未确认。现另有[公开GitHub Pages游戏入口](https://misakamikotoghr-5205.github.io/deadlock-manor/)，官方构建成功，匿名主页及5个运行资产200、MIME和源码字节匹配；随后实际完成两线索→暂停→回滚→验证，turn3解决、capacity3、score90；单步比较、显式继续分支与返回原记录均已操作，并下载JSON。146.8秒本地MP4以11张真实浏览器截图剪辑，明确不是连续录像；已完整解码并检查15帧、31条字幕，未完整人工听审（[记录及哈希](https://github.com/misakamikotoghr-5205/deadlock-manor/blob/5fb8bf1abc3bf1b6f05561b2052ff1565400b54a/docs/local-demo-20261109.json)）。YouTube未上传，不能将本地成片记作公开演示或最终交件。原Owner-only Sites预览仍不作为公开入口。11月9日4000额度申请表明确显示“Your response has been recorded.”，已确认申请收件（[脱敏回执](evidence/kiroween-credits-request-20261109.json)）；待审核及Didit身份核验，身份核验尚未完成，未确认获批或到账。额度申请收件不计作赛事最终交件。`docs/submission-draft.md`和`docs/demo-script.md`仍是准备稿。

## 7. 支付宝小荷包 AI 插件活动 — Pocket Pause

**主源：**[官方账号原活动公告](https://www.xiaohongshu.com/discovery/item/6a96b088000000001103af07)。11/6 主智能体用原分享链接在浏览器重新读到支付宝小荷包官方置顶，仍写“10月31日”截止；当前可见页面未发现官方延期声明。项目创建于 11/4，不能把晚于截止的作品报作原届已参赛。未核实新的活动届次，不将普通用户的新评论当成重开依据。

当前可保留浏览器原型和`creator-pack/xiaohobao-prompt.txt`，以后在本人支付宝小荷包真实创作界面核实当前入口与能力后，作为普通创作候选。没有已验证公开插件 SDK、官方部署清单、自动转账/提醒/账户核验能力。当前无平台插件 ID、报名回执或支付账户连接。`docs/submission-draft.md`明确为后续创作，不是补交稿。

## Private handoff checklist

账号协调人只在私密渠道收集必要资料；以下不是要求把所有项目都填写相同信息。

1. 确认报名主体：本人年龄是否达当地成年、常住国家/地区、个人还是实际团队、真实组织/雇佣与利益冲突。未满足的专项不申报。
2. 确认已有且愿用于报名的支付宝、华为云、爱奇艺号、AIMA、Devpost、Kiro 与必要小红书账号。登录、验证码、授权与接受条款由账号持有人处理；不在公开文件保存标识或凭据。
3. 先读取每个平台当前实际表单，逐项确认真实必填材料。缺公司、资质、原生作品、支付开通或平台贡献时保留阻塞，不能编造记录。
4. 使用七份 `docs/submission-draft.md`填充事实描述；补真实截图、演示视频、平台作品 ID、商品/应用 URL 和必要使用记录。
5. 仅在收到实际成功页面/邮件/后台状态后记录“已报名/已提交”，区分草稿、待审、上架、入围。回执与身份资料私存，公开索引只写非敏感状态及公开链接。

## Audit boundaries

初次审计只读取公开官方资料与本地项目。11/6后续接受智元账号及开放平台协议并登录；11/7按用户确认记录AIMA申请、爱奇艺四款后台投稿完成，PAYATHON由用户尝试报名。仍未独立保存这些国内阶段的官方回执，不升级为审核通过或最终作品收件。新投稿素材已分别推送，未操作付费服务。动态/登录后尚不可见的字段保留为待核实，而非猜测。最新逐项状态见[国内推进记录](domestic-progress-20261106.md)。
