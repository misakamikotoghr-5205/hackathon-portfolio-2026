# 六个非游戏新增赛事：提交入口与材料审计

核查日期 **2026-11-06 UTC**。仅记录公开规则、当前公开页面/前端字段和本地证据；不含参赛者姓名、邮箱、手机号、地址、账号、凭据或报名收据。本次准备没有登录任何赛事账号、勾选协议、提交表单、发消息、付费或推送。root另行操作的私有账号/报名状态以其实际收据为准，不能由本文件推断。

所有草稿都可直接作为真实内容起点；没有虚构视频、安装链接、平台使用记录或身份。隐藏于登录后的字段、实时账号资格与未取得的材料均明确区分。

当前共用状态：姓名、邮箱、手机号已私密提供，公开文件不记录其值；18岁以上、常住国家/城市与各平台账号状态仍待确认，Clips当次注册条款确认待答。**官方报名回执0份，作品提交回执0份。** 小荷包原届过期、火山表单仅面向企业，均跳过，不虚构可报名资格。

## 最急：Builder

直接表单 **https://www.builder.io/hackathon/submit**，截止 **北京11月10日15:59**。当前公开表单必填 First name、Email、Project name、Project description、Public Clips recording URL 和资格/授权/数据处理同意；Last name、GitHub URL、Slides URL可选。[表单](https://www.builder.io/hackathon/submit)、[规则](https://www.builder.io/hackathon/rules)支持这一映射。

最少可行材料已写在 [填表稿](drafts/patch-review-desk/form-draft.md) 和 [2–3分钟录屏脚本](drafts/patch-review-desk/video-script.md)：真实打开本地工具 → 固定示例两处草稿 → 只批准一段 → 应用 → 回滚 → 展示真正的官方动作合同及范围。始终明确 **fixture、model off**，不把固定规则说成推理。官方要求实际Agent-Native应用和公开Clips演示，没有写强制某个LLM；狭窄动作层集成能否获评仍由评委决定。

[Clips](https://clips.agent-native.com/)当前公开页需要Google或邮箱/密码登录。实际录制、发布、退出登录确认可播放，再把真实链接粘入表单；没有公共Clips URL时不应伪造或先称交件完成。注册/网络活动参加非必需，录制本身也不等于提交。

Patch已于11月6日取得真实本地模型响应：原45秒超时保留，受限别名随后返回合法文本，但未满足目标两行公告，`exact_target_match=false`。这里只运行modelDraft，没有执行proposal、角色HTTP、人工批准、应用/回滚或Clips；固定fixture仍须明确model off，不把合法响应说成任务完成。

## 六场入口、截止与交件阶段

| 赛事 / 项目 | 当前官方入口 | 截止/阶段 | 真实材料缺口 |
|---|---|---|---|
| Builder / Patch Review Desk | [公开提交表](https://www.builder.io/hackathon/submit)；无需提前报名 | 11/09 23:59 America/Los_Angeles = 11/10 07:59UTC / 15:59北京 | 姓名/邮箱已私下取得；资格/账号/Clips条款确认及公开录屏待做；真实模型响应合法但未达两行目标，未proposal/审批/录屏 |
| PayPal / Cart Consent | [官网](https://paypalaihackathon.devpost.com/) Join hackathon → Devpost认证 → 本赛事提交；匿名访问Join被导向注册 | 11/12 12:00PST = 20:00UTC / 11/13 04:00北京 | 真实模型已生成1398/5000美分购物篮、DRAFT未批准；真正PayPal sandbox和组合演示/公开视频仍缺 |
| Next Horizon / Watt Window | [官方Apply重定向](https://eisociety.org/go/apply/next-horizon-2026?s=direct) → [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSe8dF2jynROjU4mEbypJJhNY-oyfxaY_c7wPLDBggET2gMOrQ/viewform?usp=send_form) | 11/15构想截止，无具体时刻；11/28 09:00EST至11/30 09:00EST正式48小时，先申请/入围 | 私密署名PowerPoint已完成、不公开；资格/地区与账号确认、报名表及回执仍待做；保留赛前原型披露 |
| Aholo / 留白实验室 | [中国活动页](https://www.aholo3d.cn/hackathon) “立即报名 / 我的参赛”：个人报名→确认组队→选题→作品 | 11/19 19:00北京 = 11:00UTC = 06:00EST | 单人也建队；核心Lux3D真实生成与导出兼容性、项目报告/过程截图、真实Demo材料，当前不能如实勾“已用Lux3D” |
| 支付宝涌现 / 余量接力 | [官网](https://emerge.alipay.com/) “报名参赛 / 我的提报 / 完善作品”，报名记录与完整提报分开 | 保守按12/06 00:00北京 = 12/05 16:00UTC；公告/正文/UI时刻有冲突见下 | 本人合法账号/实名与协议，真实可交互交付与录屏，完整提报字段复核；已发生两次本地模型请求，未支付宝/阿宝接入 |
| Codegeist / Dependency Evidence | [官网](https://codegeist2026.devpost.com/) Join hackathon → Devpost认证 → 本赛事提交 | 12/22 12:00PST = 20:00UTC / 12/23 04:00北京 | 真正Forge注册/deploy/install、评委安装链接、英文公开YouTube演示；本地SDK模块/typecheck/bundle不能替代安装 |

公开规则复核主源：[PayPal要求](https://paypalaihackathon.devpost.com/rules)、[Codegeist要求](https://codegeist2026.devpost.com/rules)、[Next Horizon FAQ](https://eisociety.org/hackathon.php?slug=next-horizon-2026)、[Aholo官方页](https://www.aholo3d.cn/hackathon)、[支付宝规则](https://www.yuque.com/shanxian/dfe94a/xzter263dyio4ge3?singleDoc#)、[延期公告](https://www.yuque.com/shanxian/dfe94a/xgqqg05f9n3l6lzg?singleDoc#)。前四个有公开HTML或明确官方重定向；Aholo/支付宝的动态字段另按下述公开脚本核对，不假称看过登录后的实际表单。

## 必填与公开可见性的界限

### PayPal

规则明示文字说明、可运行Demo访问（完整仓库启动说明或托管地址）、模型/AI工具用途、公开开源仓库和公开YouTube视频，视频应少于3分钟。作品须实质使用PayPal sandbox及AI。Devpost认证后的字段标签、长度、额外问卷未看到，不能捏造为“已核必填”。合法账号与用户个人资格由本人核验；中国大陆未被规则直接列名排除不等于个人资格/奖金或账号可用保证。

现成 [双语填表稿](drafts/cart-consent-paypal/form-draft.md) 与 [录屏脚本](drafts/cart-consent-paypal/video-script.md)。仓库的sandbox适配器只建订单链接，不执行capture；未创建真实sandbox订单前不可说完成PayPal演示，mock也不能替代。

Cart的真实本地qwen2.5:0.5b请求已通过模型输出和业务校验，生成1398/5000美分的购物篮，状态仍为DRAFT、无人工批准/PayPal调用；原超时与超预算拒绝、后续超时也保留。该证据不等于通用模型质量、真实sandbox或端到端支付/视频完成。

### Aholo

当前页直接加载的公开[官方前端脚本](https://qhstaticssl.kujiale.com/__p/static/-holo-site-aholo-hackathon/pages/holo-global-main-hackathon/entry.dec1c8dc2e080e64.js?pn=holo-global-main-hackathon&ps=1851411)包含报名/选题/作品表定义；本次只读静态文件，未请求账户API。脚本可更新，应在提交时核对实际UI。

个人报名包含姓名、邮箱、国家/地区/城市、身份与报名须知；队伍1–3人，单人也建队。选题名2–40字符、简介10–500；正文草稿已控制在范围内。作品表含项目报告(PDF/PPT/PPTX或报告链接，需要过程/资产迭代/效果截图)、Demo/视频链接或上传、应用赛道1–3或“无”、生态设备/技术或“无”、真实Lux3D确认和提交须知。源代码与社媒在公开代码中为加分部分。具体文件大小和所有赛道选项不在此稿假定。

[填表稿](drafts/scene-clearance-lab/form-draft.md)、[报告正文](drafts/scene-clearance-lab/report-draft.md)、[视频脚本](drafts/scene-clearance-lab/video-script.md)可用。报告草稿没有伪造截图，内置程序几何不当Lux3D使用证据。当前不能如实完成Lux3D确认。

### 支付宝涌现

当前官网公开加载的[页面脚本](https://gw.alipayobjects.com/render/p/yuyan/180022670000174287/async.f648d116.js)显示初次报名只需名称2–30字符、life/business方向和协议同意，成功后需“完善作品”。不能把生成报名记录视为作品完整提报或审核通过。

官网构造的[工作台页面](https://render.alipay.com/p/yuyan/180022670000174278/index.html)直接加载的[公开脚本](https://gw.alipayobjects.com/render/p/yuyan/180022670000174278/async.975f9313.js)另有完整校验：名称2–30字符、life/business、简介/正文提取纯文本后100–3000字符、恰好1张封面；封面上限5MiB，ZIP/HTML附件上限100MiB。愿望关联ID可选，视频状态另行保存，不能因此捏造视频。URL方式只允许 `alipay.com`、`lebuding.com`、`qmuse.pub`、`app.weavefox.cn` 本身/子域或合法支付宝小程序启动URL，不能把GitHub或普通API地址当可交件URL。ZIP上传依赖实际构建服务配置；扩展名通过不等于当前Python后台可在平台运行。实际生效账号和UI仍须本人确认，不向内部API直发提交。

日期仍保守按最新已核延期公告的12月6日零点。规则正文另有23:59:59；本次公开报名成功面板又出现硬编码12月31日23:59，不能据面板当作正式延期证明。提交前核对门户/公告，而非自动选择最晚时点。

[双语填表稿](drafts/pantry-relay/form-draft.md)、[录屏脚本](drafts/pantry-relay/video-script.md)已更新真实证据：root于11月6日用Ollama0.40.15/qwen2.5:0.5b运行实际生产adapter，项目`docs/evidence/local-model-20261106.json`记录两次请求；均为11月4日固定虚构库存回放。首次“单一配料早餐”返回两个菜谱，结构合法但偏好未全满足；第二次明确约束返回plain_oats。不能当质量benchmark、安全保证或支付宝调用/正式提报证据。

### Codegeist

规则要求实际Forge应用、至少一个Atlassian产品/能力、可在评委环境安装的sharing链接、完整安装说明、英文或英语翻译说明、主类别/适用奖金说明及公开YouTube运行演示。视频少于5分钟，实际目标<3分钟，因为评委不需继续看。源码仓库不能代替安装链接。本人注册与SDK条款另行核验。

[双语稿](drafts/dependency-evidence-forge/form-draft.md)选 Apps for Software Teams；[视频脚本](drafts/dependency-evidence-forge/video-script.md)区分离线fixture与真正安装。没有Rovo/MCP/Teamwork Graph/Marketplace证据，不勾相应bonus。实际Forge模块与19项本地检查存在，尚无真实Jira调用/安装链接证据。

### Next Horizon

官方FAQ允许单人，主要主题选 Smart Cities and Sustainable Development；公开规则要求PowerPoint≤15MB，覆盖团队、问题、方案技术、影响可行性、实施计划；已有原型可附2–4分钟视频。真实表单无法通过本次公开文本读取，因此不虚构其必填姓名/上传/问卷标签。

[双语稿](drafts/watt-window/form-draft.md)、[五页幻灯文字](drafts/watt-window/pitch-draft.md)、[视频脚本](drafts/watt-window/video-script.md)完整可用；六页PowerPoint及私密署名版现已完成，个人资料不进入公开文件。资格/常住地区、账号和报名提交仍待确认，不能假造单位/学历或官方回执。赛前17项本地测试与虚构成本示例，不是节能实测或未来48小时成果。若入围，再记录真实赛期新增工作与最终10分钟演示/5分钟问答。

## 交付与不应替代的材料

六个项目都已有独立公开源码和运行说明，草稿逐项披露真实使用、AI辅助、原始/第三方许可和边界。Builder真实导入Agent-Native/jsdiff/Zod；Aholo实际vendored Three.js/OrbitControls；Forge SDK受Atlassian Developer Terms，不冒称MIT。其余比较项目未复制代码/素材，外部模型权重仍有各自许可。

公开仓库、源码压缩包、本地测试、私有预览、适配器合同通过均不等于报名、真实平台调用、公开录屏、安装链接或最终交件。本文件不发布任何凭据，也不把尚未发生的步骤改成完成时态。每次实际表单操作后，root应私下保存成功回执并更新状态，不能只凭按钮点击或草稿保存说提交成功。
