# 2026-11-09补充活动与新作状态

本页记录11月9日用户新链接补充的两项已交付项目与其余条件候选。总目录现为19项、412项本地测试；QNX和MINMAX独立于已经交付的额外十场，不改变十场名额。独立报名阶段现为6项、最终作品回执现为2份（Builder与Kiroween）；MINMAX问卷报名已确认，以下两项目均未取得新的正式作品收件确认。代码发布、测试通过、活动报名和正式收件分别记录，不公开私人联系方式、授权链接或账号凭据。

## MINMAX｜字幕交接台 Caption Relay

**状态：源码、PDF与本地成片已完成，真实本地模型HTTP调用和显式保存响应导出有证据；11月10日问卷报名已完成，作品邮件已发送；待组委会确认，无正式作品收件回执。**

实际发送包对应已核验源版本[e28bb9f0a228fbb74b18852ef788bd268233427f](https://github.com/misakamikotoghr-5205/caption-relay/tree/e28bb9f0a228fbb74b18852ef788bd268233427f)，28项本地测试及严格TypeScript检查通过。程序导入SRT/VTT，检查时间、阅读负担与术语；程序生成保留其余原文的字面词表候选，真实本地模型检查有限上下文、选择建议或保留并解释理由，人逐条确认。模型不能自由改写字幕或改时间码。

真实HTTP调用返回200，用时59.729753秒，读取cue-1/2并给出cue-2候选；另一次保存响应工作流明确采用cue-2，导出SRT、VTT和审计JSON且时间码未变。不是第二次模型调用，也不是全文件模型质量证明。浏览器实际核查过五句导入及三项提示；完整浏览器AI审阅、采用和导出仍未验证。历史超时、误选与删除原文失败均保留，不把确定性规则或程序候选冒充AI创作（[运行证据](https://github.com/misakamikotoghr-5205/caption-relay/blob/e28bb9f0a228fbb74b18852ef788bd268233427f/docs/evidence/http-review-20261109.json)）。

八页商业计划书PDF为109761字节，SHA256为bce9bb95e194bbca8ab2968e66866590506d01e794a3c18b28ff806a7eb2e98d，逐页视觉检查完成。中文通用合成旁白与同步字幕MP4为106.8秒、2124112字节，SHA256为79e119fb450de9ef5d7bc54371b19a2366eec3974b8fa918ad20ce1c3183de1f，已完整解码并抽看十个实际帧。成片是实际保存HTTP/CLI结果的原创编辑证据卡，明确不是GUI或终端录屏，不虚构界面操作；没有完整人工音轨听审声明（[媒体记录](https://github.com/misakamikotoghr-5205/caption-relay/blob/e28bb9f0a228fbb74b18852ef788bd268233427f/docs/local-demo-20261109.json)）。两文件已作为11月10日作品邮件的附件发送，Sent Items中已打开核对；不代表已在公网托管或收到组委会作品收件确认；问卷报名已另行完成并核验官方完成页。原发送版本保持e28bb9f，后续状态文档更新不冒充新的代码、模型调用或视频。

原生Sites部署已成功，但[预览](https://caption-relay-hengrui-2026.ghraurora1024.chatgpt.site)仅所有者可访问，且远端UI不能连接开发机的loopback Ollama，不是评委公开AI运行入口。正式试用方式为[公开仓库README](https://github.com/misakamikotoghr-5205/caption-relay#run-locally)的本机运行：Node.js、Ollama及指定模型，无需测试账号、卡片或付费订阅。

[主办方官方18问](https://www.gba-base.com/newsDetail.html?id=2892&active=true)明确支持个人或1–4人、不限专业/学历/职业；每人仅一队一作，各成员独立问卷星报名。报名和交件截止为**2026-11-10**，未注明具体时刻或时区。MINMAX为该赛事品牌，不强制使用同名企业产品。

Q9–Q14要求遵守开源许可并披露来源；交付PDF商业计划书、可试用产品及3分钟以内MP4，视频须有清晰中文旁白和同步字幕。制作材料采用PDF小于10M、视频小于300M；确需本地运行可附运行说明。组委会对完整合规作品邮件回复确认，发出邮件不等于收件确认。入围作品有赛事宣传与成果展示的非商业授权；未见既有作品政策或明确地域限制，不据此补推未写明的资格。本项目邮件已通过Outlook UI发送并核对Sent Items，待组委会确认；问卷报名已完成，主操作者已在本人当次明确同意后提交并核验官方完成页。Outlook显示日期2026/11/10、时间11:10，时区未确定，不将其作为精确UTC发件时间。报名完成页确认个人报名成功；邮件发送不计作正式作品收件。

## QNX Global Hackathon｜Boot Order Atlas

**状态：公开主机工具及[151.6秒Public YouTube演示](https://youtu.be/K55o50_Tus4)已完成；本人确认资格及规则后已Register，官方Thanks for registering!及项目0已核验，报名成功；项目创建进行中，未最终交件。**

已核验GitHub远端版本[7079c6eeed414aff2cb14b1591c6bd07c97e21e1](https://github.com/misakamikotoghr-5205/boot-order-atlas/tree/7079c6eeed414aff2cb14b1591c6bd07c97e21e1)，32项本地测试通过。工具读取QNX 8启动脚本的受支持子集和显式资源契约，生成带源行证据的JSON、离线HTML及修订比较。它是host tool；没有申请/使用QNX SDK、构建IFS、运行QNX或证明实际启动成功，示例服务为原创虚构输入。

[官方规则](https://qnx.devpost.com/rules)§4允许在Windows/macOS/Linux主机运行、分析或支持QNX 8软件的工具；本项目对应Developer Tooling & Host Tools。截止为**2026-12-15 14:00 EST**，即19:00 UTC / 北京12月16日03:00。规则允许18岁以上个人，仍须核对适用法、利益冲突等具体排除条件；不能把未列出某地区视为全部资格保证。

本地主机CLI成片为151.6秒、6129190字节，带英文通用合成旁白和字幕，SHA256为038c9f53408f4dd1766c82b199012b3b76bf393dd335dd4b03705b24fc524b1c。内容为真实命令及输出的编辑演示，已解码及检查实际帧，不冒充QNX目标执行（[媒体记录](https://github.com/misakamikotoghr-5205/boot-order-atlas/blob/7079c6eeed414aff2cb14b1591c6bd07c97e21e1/docs/local-demo-20261109.json)）。

[151.6秒YouTube演示](https://youtu.be/K55o50_Tus4)已Public发布，保留真实主机CLI编辑演示及QNX未运行边界。正式交件仍需完成Devpost活动注册、说明/类别/工具平台资料、公开源码与QNX相关功能证据及最终entry；本人已确认资格及规则并Register，官方报名成功页已核验、项目数0；仍需完成项目创建及后续材料与交件。公开视频不等于独立匿名播放验证或正式entry。[官方资源页](https://qnx.devpost.com/resources)列有SDK与技术资源，不构成本项目已注册、获得许可或运行SDK的证据。

## UGREEN AI NAS Hackathon｜排除

**中国大陆个人候选结论：排除，不报名，不为本活动新增项目。**

[正式规则](https://ugreenhackathon.devpost.com/rules)§2列主办/管理方为AMERICA UGREEN LIMITED；§3给出居住地白名单，并在“IS NOT open”排除名单中明确列出China。[品牌活动页](https://ai.ugreen.com/pages/ugreen-hackathon)的Register和Official Rules指向同一Devpost活动，并非另一场面向大陆的国内赛。品牌来源或中文介绍不能替代正式居住地资格条款，也不通过改填地区规避限制。

## Firebase #BuildHybridAI 2026｜等待正式规则

**状态：未预注册、未接受未来规则，未确认大陆个人资格或完整交件要求。**

2026-11-10复核：[规则页](https://firebasehybridaihackathon.devpost.com/rules)仍明确说正式规则尚未提供，并说明注册即同意受未来公布规则约束；本轮不执行这类预先接受。[首页](https://firebasehybridaihackathon.devpost.com/)的Requirements仍显示“This is a test.”，并称完整规则与提交要求将于11月11日发布；不可把占位内容当作完整要求。

[官方赛程](https://firebasehybridaihackathon.devpost.com/details/dates)现显示提交期为**2026-11-11 09:00 PST至11-30 14:00 PST**，即**11月11日17:00 UTC开始，11月30日22:00 UTC截止**（北京时间11月12日01:00至12月1日06:00）。开始时间已不同于此前记录的11月9日；按当前带PST的赛程表核对，不沿用首页星期文案的笔误。赛程和首页的全球性概述不替代尚缺的正式资格、排除地区、技术及交件细则；须待规则实际公布后重新核对，不在本页认定可正式参赛。

## Rokid 2026｜条件尚未满足

**状态：条件候选，未报名，未取得或承诺借用设备，未承诺线下出席。**

[官方赛事平台](https://spatialjoy.rokid.com/2026)经本轮官方页面实查，作品涉及AIUI Studio、AI APP与真实眼镜设备；不是仅交普通网页即可替代的纯软件线上流程。页面列作品截止为**2027-01-28**，决赛为2027年3月中旬线下活动，具体安排须随官方更新核对。

设备借用另有协议、损坏责任与归还要求，本轮未接受借用合同。硬件获取、真实设备验收、个人适用资格以及线下参赛可行性仍未解决；不承诺主办方会借出设备、无需硬件或可以远程替代决赛。

## BII科学骑士大科学装置专项赛｜等待具体赛题与规则

**状态：已核官方活动预告，尚不能确认当前可提交的具体赛题、截止或个人远程资格。**

[官方专项赛预告](https://hsc.beijing.gov.cn/hsc/ywdt8/zxdt72/744155330/index.shtml)和[怀客松AI for Science赛道公告](https://hsc.beijing.gov.cn/hsc/ywdt8/zxdt72/744156513/index.shtml)确认北京科学智能研究院、深势科技与DeepModeling开源社区参与，专项赛围绕大科学装置实际科研问题开展，并计划2026年11月启动。具体赛题、赛程和评测安排另行公布，指定关注[科学骑士赛事平台](https://play.bohrium.com/)。

公告中常规怀客松的11月14–17日线下安排，不能直接当作此专项赛的交件时间或远程规则。正式赛题、数据/模型许可、评测环境、个人/团队与线上资格未核清前，不创建假题目、不宣称已报名或已完成科学验证。
