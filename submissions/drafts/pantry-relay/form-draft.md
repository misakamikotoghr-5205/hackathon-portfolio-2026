# 余量接力 — 支付宝智能体涌现奖材料与提交记录，2026-11-10

官方入口：[智能体涌现奖](https://emerge.alipay.com/)。按用户授权，通过官网实际账号页面办理，未调用内部创建/提交接口。本稿不公开账号、手机号或私有资料。11 月 9 日报名记录已核验，用户已确认实名；这些事实不代表主办方已审核全部参赛资格。

**当前状态：已正式提交审核。** 11 月 10 日短信登录后恢复现有草稿，重新选择修正 ZIP 并点击“提交审核”。官方先显示“正在创建发布任务”，随后返回个人中心：同一余量接力卡片由“草稿”变为 **“审核中”**，有“撤销审核”按钮，子文本为 **“ZIP 安全审核尚未完成”**；“我的作品”仍为 1。09:08:24 UTC 已保存页面证据。脱敏回执位于项目仓库 [`docs/evidence/submission-receipt-20261110.json`](https://github.com/misakamikotoghr-5205/pantry-relay/blob/main/docs/evidence/submission-receipt-20261110.json)。不重复交件；提交审核成功不等于 ZIP 安全审核通过、上线或赛事评审通过。

## 已使用的报名材料

实际工作台已核验现有报名和草稿，现已提交审核。早期公开前端代码显示的名称、方向和协议字段仅作为准备依据；创建报名记录本身不等于完整交件或审核通过。

作品名：**余量接力：开封时钟与库存回执**

方向：**AI 生活好帮手 / life**

活动规则、客户端软件许可及服务协议、蚂蚁阿宝服务协议和隐私政策已按用户确认办理。没有代用户完成证件核验，也不将用户确认实名写成主办方已审核全部资格。

## 可直接填的中文介绍

余量接力把家庭自行录入的包装标签、开封记录、实际库存与自有菜谱，连接成“有来源的先用计划 → 人工核查 → 一次使用的原子扣减 → 可恢复库存回执”。缺少开封说明、日期冲突、未来记录或经过标签时限的批次保持待核查，不能只凭“没过期”自动放行。补货缺口与待核查的实物库存分开，避免把未核查食材当作零库存重复购买。

智能体选择器的权限被限制为：理解用户自然语言偏好后，只返回已经通过门禁的自有菜谱ID；不能创造菜谱、改数量、绕过忌口/缺货或宣称安全。确定性规则负责来源、日期、分配与消费，SQLite事务保证整道菜全量扣减或全部回滚，相同请求重试只返回原回执。

现有Python CLI与鉴权JSON API保留，26项测试覆盖并发、幂等、回滚、日期和模型越权。11月7日新增完整离线交互网页，支持食材/菜谱录入、来源核查、份数/成本上限/偏好、逐笔审阅确认、消费回执/撤回和导入导出；新增19项前端测试，消费、刷新、撤回及导出/导入已实际在桌面浏览器验证。另备 React+Vite 生产网页，审阅、消费、刷新和撤回已实际验证。网页使用确定性规则和本地浏览器账本，不含运行时LLM、外部API或支付调用，不能用网页交互代替后端SQLite事务或模型演示。真实本地Ollama适配器已在11月6日用Ollama 0.40.15和qwen2.5:0.5b运行两次请求；输入为固定11月4日虚构回放，不是真实家庭库存。首次“只用一种配料早餐”返回plain_oats与tomato_eggs：结构合法，但偏好未完全满足；第二次明确只要plain_oats才返回该ID，不能据两次小例声称模型质量已验证。当前交件为[97,252字节React生产ZIP](https://github.com/misakamikotoghr-5205/pantry-relay/blob/main/releases/pantry-relay-react-html.zip)，已正式提交审核，平台显示ZIP安全审核尚未完成。尚未接入支付宝/阿宝业务后台，不能宣称已上线或平台运行验收通过。

## English title and summary

**Pantry Relay — source-aware meal plans with atomic inventory receipts**

Pantry Relay connects user-entered package labels, opening records, inventory and personally supplied recipes to an auditable use-first workflow. Missing or conflicting dates and uncertain batches remain held for review. A natural-language adapter may select only an already eligible recipe ID; it cannot rewrite quantities, invent recipes, bypass exclusions or assert that food is safe. Deterministic rules and a SQLite transaction recheck the complete allocation before consuming inventory, with exact retry receipts rather than repeated deductions.

The Python CLI and authenticated JSON API have twenty-six behavior tests. A complete offline browser UI was added on November 7, with nineteen additional front-end tests and actual desktop checks of review, consumption, reload, undo and file export/import. The React production build was also checked in the actual browser. Its planner is deterministic with no runtime LLM call, payment or remote API. The browser ledger is separate from the backend SQLite transactions. The actual local Ollama adapter ran on November 6 with Ollama 0.40.15 and qwen2.5:0.5b, using a fictional November 4 replay. One request for a single-ingredient breakfast returned both plain_oats and tomato_eggs: schema-valid, but not fully preference-compliant. A second, more explicit request returned only plain_oats. These two small observations are not a quality benchmark. On November 10 the corrected 97,252-byte React ZIP was submitted through the official workspace. The existing entry now shows under review, with ZIP security review still incomplete. This confirms submission for review, not security approval, a live deployment, or Alipay/Abao integration.

## 技术、差异、构建与AI/开源披露

- 技术：Python 3.11+标准库、SQLite事务、十进制数量、IANA时区、Bearer JSON API/OpenAPI、可选Ollama结构化输出。默认离线，不需要付费服务。
- 差异：来源/不确定性会直接阻止执行；区分实物库存与可分配库存；消费按版本和幂等意图原子完成。不是完整家庭ERP，没有扫码识别、联网食谱摄取或多租户隔离。
- 过程：先定义标签/记录/菜谱来源 → 时间和人工确认门禁 → FEFO分配 → 事务消费/审计/回执 → 限制模型只选合格ID → 实测错误与并发路径。本地合约测试与11月6日两次真实请求分开记录，不把小例当质量评测。
- AI：Codex辅助设计、代码、测试和文档；运行时规则明确标 `deterministic-rules`。11月6日已发生两次本地Ollama真实请求，首次偏好未完全满足，仍需人工复核；这份静态React ZIP未接入适配器。官方QMuse CLI **1.0.14** 已安装并进行真实本地格式预检，未通过CLI远端导入或发布；不能写“已接阿宝”或“模型质量已验证”。Q Muse是赛事推荐但可选工具。
- OSS：原创实现MIT。Grocy(MIT)、Mealie(AGPL-3.0)仅为固定提交的设计比较，未复制代码、素材、测试或菜谱；没有把AGPL改标MIT。外部模型许可由使用者单独核验。
- 真实边界：日期门禁不是食品安全证明；忌口是用户标签过滤，不检测未知过敏原或交叉接触。本稿不提供食用保证。

## 完整材料映射与尚缺证据

| 内容 | 可用值/现状 |
|---|---|
| 名称、方向、介绍、技术/过程 | 上述草稿 |
| 封面候选与中文说明附件 | [cover-zh.png](cover-zh.png) 是1200×675原创说明封面，标明本地原型/未接支付宝，非平台截图；[evidence-deck.html](evidence-deck.html) 为静态证据说明，不是可交互作品。生成与使用边界见 [materials-zh.md](materials-zh.md)，是否接受该封面/说明附件以真实UI为准 |
| 源码和启动说明 | https://github.com/misakamikotoghr-5205/pantry-relay |
| URL或ZIP/HTML作品 | 11月10日实际登录UI显示ZIP上限 **50MB**，替代早期公开代码100MiB准备假设。已提交97,252字节React生产ZIP，SHA256 `bcacef8b7012c38fa20f43b252b72904322334ccc63e9c48f2b323ab84d34228`；根index.html/package.json、CRC、本地依赖及与qmuse/dist运行文件一致性已核对。官方现为审核中，ZIP安全审核尚未完成；GitHub、普通API地址不能冒称合格平台URL。QMuse CLI1.0.14仅本地格式预检，不是远端导入或发布证据 |
| 实际AI交互 | 已有11月6日两次本地真实adapter响应；首次偏好未完全满足，第二次显式约束成功，仍需复核/录制，不是质量benchmark |
| 模型/接口配置与访问方法 | README、OpenAPI和部署说明可用；评委凭据只能私下交付，不写公开稿 |
| 视频/运行证据 | [video-script.md](video-script.md)提供具体脚本；真实推理JSON在项目docs/evidence/local-model-20261106.json。未新增录屏或上传成功宣称；11月10日实际UI视频上限 **100MB** |
| 完整提报工作台必填/附件 | 公开代码曾核名称2–30字、life/business、简介/正文100–3000字、恰好1张封面及封面5MiB。当前提交以11月10日实际登录UI为准；修正ZIP已提交，作品卡片为审核中，有撤销审核按钮，仍待ZIP安全审核及后续结果 |

当前官方日程仍写 **12月6日零点**，保守按 **2026-12-06 00:00北京 / 12-05 16:00 UTC** 处理后续材料。另有规则正文23:59:59冲突；早期公开报名成功面板代码还出现12月31日23:59，不当成正式延期。后续仍核对实际门户与公告。作品已提交审核，不重复交件，也不把同一作品重复投其他赛事。

真实运行证据：项目 `docs/evidence/local-model-20261106.json`（仅固定虚构场景）。记录实际adapter、模型与原始返回；自然偏好仍需人工核查，不升级成食品安全或用户效果结论。

当前公开URL校验允许 `alipay.com`、`lebuding.com`、`qmuse.pub`、`app.weavefox.cn` 本身及子域，或满足格式校验的支付宝小程序启动URL。应通过官网按钮进入，不伪造这些平台域名、不向内部API直发请求。关联愿望ID在schema中为可选；没有真实响应的愿望就不乱填。正式简介可用上面的中文正文，长度在100–3000范围内；封面公开schema已核数量/类型/大小，但未据此确认必须是界面截图。新增封面仅为如实标注的原创说明图，不伪造已上线/已接阿宝界面；若实际UI要求真实界面，应另录真实运行画面。公开代码显示ZIP上传还依赖构建服务配置，接受扩展名不等于我们的Python服务已能运行，须现场验证。

11月7日新增真正React+Vite工程，保留早期生产模块加载失败及修复证据。11月10日修正[生产HTML ZIP](https://github.com/misakamikotoghr-5205/pantry-relay/blob/main/releases/pantry-relay-react-html.zip)仅补根package.json元数据，运行文件保持已实际生产浏览器确认、刷新、撤回复验的产物。官方QMuse CLI1.0.14离线格式预检接受该工程，但未通过CLI远端导入或发布。赛事官网已接受本次提交审核，后续仍待ZIP安全审核、平台运行与赛事评审结果。
