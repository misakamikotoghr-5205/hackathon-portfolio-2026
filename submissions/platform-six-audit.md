# 六个非游戏新增赛事：提交入口与材料审计

规则核查日期 **2026-11-06 UTC**，阶段进度更新于 **2026-11-10 UTC**。仅记录公开规则、当前公开页面/前端字段和本地证据；不含参赛者姓名、邮箱、手机号、地址、账号、凭据或私密回执URL。账号操作与正式报名、最终作品提交分开记录，只有真实成功页或回执才计为相应阶段完成。

所有草稿都可直接作为真实内容起点；没有虚构视频、安装链接、平台使用记录或身份。隐藏于登录后的字段、实时账号资格与未取得的材料均明确区分。

当前共用状态：基础身份资料已私密确认；平台账号/适用条款/实际材料仍待处理，公开文件不记录个人资料。Clips已真实登录；本人同意Builder Free免费存储及仅项目标签页、摄像头/麦克风关闭录制后，实际录屏已保存。Builder已在本人当次最终提交确认后勾选processingConsent、保持marketing未勾并点击Submit，官网成功页已确认收件。**已确认独立报名阶段7项（Apart、PAYATHON个人报名、涌现奖已建记录、PayPal、MINMAX问卷报名、QNX、Aholo），正式作品提交回执7份（Builder、Kiroween、QNX、PayPal、Aholo、支付宝涌现奖、MINMAX），跳过2个方向。** Apart公开官网见[四项目审计](game-research-four-audit.md)，private success-page evidence held；不公开私密回执URL或邀请码。 小荷包原届过期、火山表单仅面向企业，均跳过，不虚构可报名资格。

## Builder：正式作品提交已收件

直接表单 **https://www.builder.io/hackathon/submit**，截止 **北京11月10日15:59**。当前公开表单必填 First name、Email、Project name、Project description、Public Clips recording URL 和资格/授权/数据处理同意；Last name、GitHub URL、Slides URL可选。[表单](https://www.builder.io/hackathon/submit)、[规则](https://www.builder.io/hackathon/rules)支持这一映射。

[填表稿](drafts/patch-review-desk/form-draft.md)已同步实际提交的英文description，[录屏记录](drafts/patch-review-desk/video-script.md)区分录制前独立agent能力生成的两hunk固定草稿与录制中的human/reviewer操作。视频展示只批准第1段、partial apply、保留未批准末句、rollback及两份回执。始终明确 **fixture、model off**，不把固定规则说成推理。官方要求实际Agent-Native应用和公开Clips演示，没有写强制某个LLM；狭窄动作层集成能否获评仍由评委决定。

Clips已真实登录，获本人当次同意后激活Builder Free免费存储，并以仅项目标签页、摄像头/麦克风关闭录制；[Fixture ModelOff](https://clips.agent-native.com/share/r01FTO1ytVvm)已保存。元数据124,936ms、1280×720、hasAudio/hasCamera=false、status/agentReadiness=ready。匿名无Cookie访问share/context均200，4个官方媒体帧均200且仅含虚构项目UI；已登录浏览器未seek自然播放至124.794秒片尾，ended=true、readyState=4、无error。未声称匿名浏览器全片实播。 录屏本身不等于Builder作品提交；本次已另外完成实际提交。截至2026-11-06 07:53:18 UTC，已在本人对本次最终提交确认后勾选必填processingConsent，保持marketing未勾，点击Submit；[官网提交页](https://www.builder.io/hackathon/submit)实际显示“Thank you for submitting.” / “Your project submission has been received.”。private success-page evidence held；网页未给回执编号，不声称收到确认邮件或评审结果。

Patch已于11月6日取得真实本地模型响应：原45秒超时保留，受限别名随后返回合法文本，但未满足目标两行公告，`exact_target_match=false`。该独立模型探针只运行modelDraft，没有执行proposal、角色HTTP、人工批准、应用/回滚，也未生成实际录屏中的两处固定修改。另已完成的fixture/model-off录屏不构成模型推理或完整模型工作流成功。

## 六场入口、截止与交件阶段

| 赛事 / 项目 | 当前官方入口 | 截止/阶段 | 真实材料缺口 |
|---|---|---|---|
| Builder / Patch Review Desk | [公开提交表](https://www.builder.io/hackathon/submit)；无需提前报名 | 11/09 23:59 America/Los_Angeles = 11/10 07:59UTC / 15:59北京 | 已提交并收到官网“Thank you for submitting.” / “Your project submission has been received.”网页回执，记录于2026-11-06 07:53:18 UTC；processingConsent已勾、marketing未勾。private success-page evidence held，无编号/邮件确认声明。模型探针与fixture录屏仍分开披露 |
| PayPal / Cart Consent | [官网](https://paypalaihackathon.devpost.com/)；11月9日已在官方manage/submissions观察到报名成功 | 11/12 12:00PST = 20:00UTC / 11/13 04:00北京 | 11月9日报名确认；11月10日真实AI＋sandbox未付款订单、[138.8秒Public视频](https://youtu.be/icz2WX1DXZ4)已完成。本人当次同意规则后已正式Submit，[官方项目页](https://devpost.com/software/cart-consent)显示“Project submitted!”及“Submitted to PayPal AI Hackathon”；提交源版本da95fd1b，正式收件已核验；公共托管非强制 |
| Next Horizon / Watt Window | [官方Apply重定向](https://eisociety.org/go/apply/next-horizon-2026?s=direct) → [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSe8dF2jynROjU4mEbypJJhNY-oyfxaY_c7wPLDBggET2gMOrQ/viewform?usp=send_form) | 11/15构想截止，无具体时刻；11/28 09:00EST至11/30 09:00EST正式48小时，先申请/入围 | 用户确认构想表已交，不重复填表；私密署名PowerPoint已完成、不公开。未独立保存官方回执，构想提交不等于入围/最终交件；保留赛前原型披露 |
| Aholo / 留白实验室 | [中国活动页](https://www.aholo3d.cn/hackathon) “立即报名 / 我的参赛”：个人报名→确认组队→选题→作品 | 11/19 19:00北京 = 11:00UTC = 06:00EST | 个人报名、一人团队及选题已确认；真实Lux3D GLB生成/导出/实际导入完成，同设置A/B提醒4→2；五页PDF及128秒视频已正式提交，官网显示“已提交”及“作品已进入资格与完整性审核”；[脱敏交件记录](https://github.com/misakamikotoghr-5205/scene-clearance-lab/blob/main/docs/evidence/submission-receipt-20261110.json)，待审核 |
| 支付宝涌现 / 余量接力 | [官网](https://emerge.alipay.com/)；现有作品材料重新选ZIP后提交审核 | 保守按12/06 00:00北京准备 | 11月10日09:08正式提交审核成功，卡片显示“审核中”、可撤销审核，ZIP安全审核尚未完成；[脱敏回执](https://github.com/misakamikotoghr-5205/pantry-relay/blob/main/docs/evidence/submission-receipt-20261110.json) |
| Codegeist / Dependency Evidence | [官网](https://codegeist2026.devpost.com/) Join hackathon → Devpost认证 → 本赛事提交 | 12/22 12:00PST = 20:00UTC / 12/23 04:00北京 | 真正Forge注册/deploy/install、评委安装链接、英文公开YouTube演示；本地SDK模块/typecheck/bundle不能替代安装 |

公开规则复核主源：[PayPal要求](https://paypalaihackathon.devpost.com/rules)、[Codegeist要求](https://codegeist2026.devpost.com/rules)、[Next Horizon FAQ](https://eisociety.org/hackathon.php?slug=next-horizon-2026)、[Aholo官方页](https://www.aholo3d.cn/hackathon)、[支付宝规则](https://www.yuque.com/shanxian/dfe94a/xzter263dyio4ge3?singleDoc#)、[延期公告](https://www.yuque.com/shanxian/dfe94a/xgqqg05f9n3l6lzg?singleDoc#)。前四个有公开HTML或明确官方重定向；Aholo/支付宝的动态字段另按下述公开脚本核对，不假称看过登录后的实际表单。

## 必填与公开可见性的界限

### PayPal

规则明示文字说明、可运行Demo访问（完整仓库启动说明或托管地址）、模型/AI工具用途、公开开源仓库和公开YouTube视频，视频应少于3分钟。作品须实质使用PayPal sandbox及AI，官方不强制公共托管。11月9日主操作者已在官方manage/submissions看到“Thanks for registering!”、空白My hackathon projects及Start project，确认报名成功、尚无项目交件；私密截图另存，不公开回执或编辑URL。不以报名成功推断最终交件表全部字段已核验。合法账号与用户个人资格由本人核验；中国大陆未被规则直接列名排除不等于个人资格/奖金或账号可用保证。

现成 [双语填表稿](drafts/cart-consent-paypal/form-draft.md) 与 [录屏脚本](drafts/cart-consent-paypal/video-script.md)。仓库的sandbox适配器只建订单链接，不执行capture；未创建真实sandbox订单前不可说完成PayPal演示，mock也不能替代。

历史11月6日Cart本地qwen2.5:0.5b记录生成1398/5000美分的DRAFT，无批准或PayPal调用，超时/超预算失败保留。另在11月10日，fresh模型5.899秒后经开发者审阅虚构快照并明确批准，真实sandbox创建一个未付款订单，返回PAYER_ACTION_REQUIRED并通过严格绑定检查；后续缓存重放零网络。首次OAuth401在Orders前停止，修正私密配置后沿用原cart/请求身份，无适配器改动。无买家登录、结账、授权或capture；不称买家身份确认。[真实组合证据](https://github.com/misakamikotoghr-5205/cart-consent-paypal/blob/main/docs/evidence/sandbox-model-20261110.json)与[138.8秒Public视频](https://youtu.be/icz2WX1DXZ4)已提供；视频是证据卡和独立mock HTTP实际终端截图剪辑、英文合成旁白，非连续录屏。本人当次同意规则后已正式Submit，[官方项目页](https://devpost.com/software/cart-consent)显示“Project submitted!”及“Submitted to PayPal AI Hackathon”；提交源版本da95fd1b，正式收件已核验。

### Aholo

当前页直接加载的公开[官方前端脚本](https://qhstaticssl.kujiale.com/__p/static/-holo-site-aholo-hackathon/pages/holo-global-main-hackathon/entry.dec1c8dc2e080e64.js?pn=holo-global-main-hackathon&ps=1851411)包含报名/选题/作品表定义；本次只读静态文件，未请求账户API。脚本可更新，应在提交时核对实际UI。

个人报名包含姓名、邮箱、国家/地区/城市、身份与报名须知；队伍1–3人，单人也建队。选题名2–40字符、简介10–500；正文草稿已控制在范围内。作品表含项目报告(PDF/PPT/PPTX或报告链接，需要过程/资产迭代/效果截图)、Demo/视频链接或上传、应用赛道1–3或“无”、生态设备/技术或“无”、真实Lux3D确认和提交须知。源代码与社媒在公开代码中为加分部分。具体文件大小和所有赛道选项不在此稿假定。

[填表稿](drafts/scene-clearance-lab/form-draft.md)、[报告正文](drafts/scene-clearance-lab/report-draft.md)、[视频脚本](drafts/scene-clearance-lab/video-script.md)可用。真实Lux3D导出物件、平台完成状态、实际导入与同设置A/B已有独立记录；其余五件内置程序几何不当Lux3D证据。实际浏览器为2D俯视代理降级，不冒称完整3D网格展示。五页PDF与128秒视频均已正式提交。本人当次确认[作品提交须知](https://www.aholo3d.cn/hackathon/submission)后，实际UI显示“已提交”、“第1版·提交于11月10日09:02”及“作品已进入资格与完整性审核”。提交卡列视频Aholo.mp4（1.3MB）、PDF（807KB）、空间设计应用奖、生态合作设备/技术“无”和正确源码链接；[脱敏交件记录](https://github.com/misakamikotoghr-5205/scene-clearance-lab/blob/main/docs/evidence/submission-receipt-20261110.json)另存，收件不等于资格审核通过或获奖。

### 支付宝涌现

当前官网公开加载的[页面脚本](https://gw.alipayobjects.com/render/p/yuyan/180022670000174287/async.f648d116.js)显示初次报名只需名称2–30字符、life/business方向和协议同意，成功后需“完善作品”。不能把生成报名记录视为作品完整提报或审核通过。

官网构造的[工作台页面](https://render.alipay.com/p/yuyan/180022670000174278/index.html)直接加载的[公开脚本](https://gw.alipayobjects.com/render/p/yuyan/180022670000174278/async.975f9313.js)另有完整校验：名称2–30字符、life/business、简介/正文提取纯文本后100–3000字符、恰好1张封面；封面上限5MiB，ZIP/HTML附件上限100MiB。愿望关联ID可选，视频状态另行保存，不能因此捏造视频。URL方式只允许 `alipay.com`、`lebuding.com`、`qmuse.pub`、`app.weavefox.cn` 本身/子域或合法支付宝小程序启动URL，不能把GitHub或普通API地址当可交件URL。ZIP上传依赖实际构建服务配置；扩展名通过不等于当前Python后台可在平台运行。实际生效账号和UI仍须本人确认，不向内部API直发提交。

日期仍保守按最新已核延期公告的12月6日零点。规则正文另有23:59:59；本次公开报名成功面板又出现硬编码12月31日23:59，不能据面板当作正式延期证明。提交前核对门户/公告，而非自动选择最晚时点。

[双语填表稿](drafts/pantry-relay/form-draft.md)、[录屏脚本](drafts/pantry-relay/video-script.md)已更新真实证据：root于11月6日用Ollama0.40.15/qwen2.5:0.5b运行实际生产adapter，项目`docs/evidence/local-model-20261106.json`记录两次请求；均为11月4日固定虚构库存回放。首次“单一配料早餐”返回两个菜谱，结构合法但偏好未全满足；第二次明确约束返回plain_oats。不能当质量benchmark、安全保证或支付宝调用/正式提报证据。

### Codegeist

规则要求实际Forge应用、至少一个Atlassian产品/能力、可在评委环境安装的sharing链接、完整安装说明、英文或英语翻译说明、主类别/适用奖金说明及公开YouTube运行演示。视频少于5分钟，实际目标<3分钟，因为评委不需继续看。源码仓库不能代替安装链接。本人注册与SDK条款另行核验。

[双语稿](drafts/dependency-evidence-forge/form-draft.md)选 Apps for Software Teams；[视频脚本](drafts/dependency-evidence-forge/video-script.md)区分离线fixture与真正安装。没有Rovo/MCP/Teamwork Graph/Marketplace证据，不勾相应bonus。实际Forge模块与19项本地检查存在，尚无真实Jira调用/安装链接证据。

### Next Horizon

官方FAQ允许单人，主要主题选 Smart Cities and Sustainable Development；公开规则要求PowerPoint≤15MB，覆盖团队、问题、方案技术、影响可行性、实施计划；已有原型可附2–4分钟视频。此前浏览器核查曾遇Google强制登录；11月7日用户明确确认构想表已提交，据此更新阶段并不再要求重复填表。操作者未独立核验最终表单或回执，不虚构其字段、提交时间、入围或审核结果。

[双语稿](drafts/watt-window/form-draft.md)、[演示内容提纲](drafts/watt-window/pitch-draft.md)、[视频脚本](drafts/watt-window/video-script.md)完整可用；六页PowerPoint及私密署名版现已完成，个人资料不进入公开文件。基础身份资料已私密确认；平台账号/适用条款/实际材料仍待处理。构想表按用户确认记已交；仍不虚构单位/学历或官方回执。赛前17项本地测试与虚构成本示例，不是节能实测或未来48小时成果。若入围，再记录真实赛期新增工作与最终10分钟演示/5分钟问答。

## 交付与不应替代的材料

六个项目都已有独立公开源码和运行说明，草稿逐项披露真实使用、AI辅助、原始/第三方许可和边界。Builder真实导入Agent-Native/jsdiff/Zod；Aholo实际vendored Three.js/OrbitControls；Forge SDK受Atlassian Developer Terms，不冒称MIT。其余比较项目未复制代码/素材，外部模型权重仍有各自许可。

公开仓库、源码压缩包、本地测试、私有预览、适配器合同通过均不等于报名、真实平台调用、公开录屏、安装链接或最终交件。本文件不发布任何凭据，也不把尚未发生的步骤改成完成时态。每次实际表单操作后，root应私下保存成功回执并更新状态，不能只凭按钮点击或草稿保存说提交成功。

## 11月7日执行补记

11月7日，PayPal的Join hackathon当时进入Devpost登录/注册页；11月9日已观察到官方报名确认、项目列表为空，仍未交件。支付宝“我要参赛”当时进入扫码登录，按用户指示先跳过认证。官方[QMuse CLI文档](https://docs.qmuse.cn/docs/qmuse-cli)说明导入与发布是独立步骤；CLI 1.0.14 的本地只读预检不接受原生静态web目录，真实React工程已构建并通过本地格式预检，不能将离线ZIP或Sites私有预览称为QMuse发布。最新准确状态见[总表](README.md)与[机器记录](status.json)。


11月10日Codegeist只读复核：官方规则仍要求评委可安装链接、Forge使用理由、少于5分钟的公开英文YouTube演示。Forge CLI15在Node24下再次whoami失败（exit1，Not logged in/keychain）；随后Google SSO产生账号邮箱同步通知，已请本人审阅，进一步Forge账号操作等待本人确认；没有新CLI认证、token、部署或安装。Devpost现有会话已登录并打开Codegeist报名表，单人/来源Devpost.com/AI Medium/目标Learning已填、营销未选；既有开发者账号、产品/Forge经验、往届Codegeist三项本人答案待补。资格/规则及Register均未操作，仍无新增报名/作品回执。
