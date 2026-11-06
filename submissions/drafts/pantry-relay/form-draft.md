# 余量接力 — 支付宝智能体涌现奖草稿，2026-11-06

官方入口：[智能体涌现奖](https://emerge.alipay.com/)。以官网“报名参赛 / 我的提报 / 完善作品”进入实际账号流程，不调用内部创建/提交接口。本稿无姓名、账号、手机号或私有资料，也没有接受协议或创建报名记录。

## 报名阶段可填

当前官网直接加载的公开前端代码显示：报名创建记录只要求作品名称 `title`（2–30字符）、参赛方向 `life/business` 及本人同意相关协议；创建记录后还须“完善作品”，不等于已正式交完整材料或通过审核。这里没有登录验证实际表单。

作品名：**余量接力：开封时钟与库存回执**

方向：**AI 生活好帮手 / life**

本人需核对：活动规则、客户端软件许可及服务协议、蚂蚁阿宝服务协议、隐私政策，以及合法支付宝账号/实名认证。协议勾选和账号步骤由本人/root处理，不在此稿中代同意。

## 可直接填的中文介绍

余量接力把家庭自行录入的包装标签、开封记录、实际库存与自有菜谱，连接成“有来源的先用计划 → 人工核查 → 一次使用的原子扣减 → 可恢复库存回执”。缺少开封说明、日期冲突、未来记录或经过标签时限的批次保持待核查，不能只凭“没过期”自动放行。补货缺口与待核查的实物库存分开，避免把未核查食材当作零库存重复购买。

智能体选择器的权限被限制为：理解用户自然语言偏好后，只返回已经通过门禁的自有菜谱ID；不能创造菜谱、改数量、绕过忌口/缺货或宣称安全。确定性规则负责来源、日期、分配与消费，SQLite事务保证整道菜全量扣减或全部回滚，相同请求重试只返回原回执。

当前是可运行的Python CLI与鉴权JSON API，本地26项测试覆盖并发、幂等、回滚、日期和模型越权。真实本地Ollama适配器已在11月6日用Ollama 0.40.15和qwen2.5:0.5b运行两次请求；输入为固定11月4日虚构回放，不是真实家庭库存。首次“只用一种配料早餐”返回plain_oats与tomato_eggs：结构合法，但偏好未完全满足；第二次明确只要plain_oats才返回该ID，不能据两次小例声称模型质量已验证。尚未部署公开体验或接入支付宝/阿宝，完整提报仍需完成。

## English title and summary

**Pantry Relay — source-aware meal plans with atomic inventory receipts**

Pantry Relay connects user-entered package labels, opening records, inventory and personally supplied recipes to an auditable use-first workflow. Missing or conflicting dates and uncertain batches remain held for review. A natural-language adapter may select only an already eligible recipe ID; it cannot rewrite quantities, invent recipes, bypass exclusions or assert that food is safe. Deterministic rules and a SQLite transaction recheck the complete allocation before consuming inventory, with exact retry receipts rather than repeated deductions.

The Python CLI and authenticated JSON API run locally and have twenty-six behavior tests. The actual local Ollama adapter ran on November 6 with Ollama 0.40.15 and qwen2.5:0.5b, using a fictional November 4 replay. One request for a single-ingredient breakfast returned both plain_oats and tomato_eggs: schema-valid, but not fully preference-compliant. A second, more explicit request returned only plain_oats. These two small observations are not a quality benchmark. No Alipay/Abao integration or public deployment is claimed; owner account validation, a public demonstration and complete submission remain.

## 技术、差异、构建与AI/开源披露

- 技术：Python 3.11+标准库、SQLite事务、十进制数量、IANA时区、Bearer JSON API/OpenAPI、可选Ollama结构化输出。默认离线，不需要付费服务。
- 差异：来源/不确定性会直接阻止执行；区分实物库存与可分配库存；消费按版本和幂等意图原子完成。不是完整家庭ERP，没有扫码识别、联网食谱摄取或多租户隔离。
- 过程：先定义标签/记录/菜谱来源 → 时间和人工确认门禁 → FEFO分配 → 事务消费/审计/回执 → 限制模型只选合格ID → 实测错误与并发路径。本地合约测试与11月6日两次真实请求分开记录，不把小例当质量评测。
- AI：Codex辅助设计、代码、测试和文档；运行时规则明确标 `deterministic-rules`。11月6日已发生两次本地Ollama真实请求，首次偏好未完全满足，仍需人工复核；Q Muse未使用，不能写“已接阿宝”或“模型质量已验证”。Q Muse是赛事推荐但可选工具。
- OSS：原创实现MIT。Grocy(MIT)、Mealie(AGPL-3.0)仅为固定提交的设计比较，未复制代码、素材、测试或菜谱；没有把AGPL改标MIT。外部模型许可由使用者单独核验。
- 真实边界：日期门禁不是食品安全证明；忌口是用户标签过滤，不检测未知过敏原或交叉接触。本稿不提供食用保证。

## 完整材料映射与尚缺证据

| 内容 | 可用值/现状 |
|---|---|
| 名称、方向、介绍、技术/过程 | 上述草稿 |
| 源码和启动说明 | https://github.com/misakamikotoghr-5205/pantry-relay |
| URL或ZIP/HTML作品 | 当前公开工作台仅接受特定平台URL，或≤100MiB的ZIP/HTML；GitHub、普通API地址不是合格URL。现有Python源码不冒充平台可自动运行的HTML/Agent包，须实际构建/部署验证 |
| 实际AI交互 | 已有11月6日两次本地真实adapter响应；首次偏好未完全满足，第二次显式约束成功，仍需复核/录制，不是质量benchmark |
| 模型/接口配置与访问方法 | README、OpenAPI和部署说明可用；评委凭据只能私下交付，不写公开稿 |
| 视频/运行证据 | [video-script.md](video-script.md)提供具体脚本；真实推理JSON在项目docs/evidence/local-model-20261106.json，尚无录屏或上传 |
| 完整提报工作台必填/附件 | 公开代码已核名称2–30字、life/business、简介/正文100–3000字、恰好1张封面；封面上限5MiB，附件ZIP/HTML上限100MiB；实际登录UI仍需核对 |

当前官方日程仍写 **12月6日零点**，保守按 **2026-12-06 00:00北京 / 12-05 16:00 UTC** 准备。另有规则正文23:59:59冲突；本次公开报名成功面板代码还出现12月31日23:59，不当成正式延期。提交前由本人核对实际门户与公告。不要把同一作品重复投其他赛事。

真实运行证据：项目 `docs/evidence/local-model-20261106.json`（仅固定虚构场景）。记录实际adapter、模型与原始返回；自然偏好仍需人工核查，不升级成食品安全或用户效果结论。

当前公开URL校验允许 `alipay.com`、`lebuding.com`、`qmuse.pub`、`app.weavefox.cn` 本身及子域，或满足格式校验的支付宝小程序启动URL。应通过官网按钮进入，不伪造这些平台域名、不向内部API直发请求。关联愿望ID在schema中为可选；没有真实响应的愿望就不乱填。正式简介可用上面的中文正文，长度在100–3000范围内；封面必须是当前作品的真实界面图，不能伪造已上线/已接阿宝的界面。公开代码显示ZIP上传还依赖构建服务配置，接受扩展名不等于我们的Python服务已能运行，须现场验证。
