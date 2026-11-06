# 四项目正式提交准备审计

核验日期：2026-11-06 UTC。范围：Lumen Shift / Game Off、Parallax Postcards / Through Your Eyes、纸路邮局 / AI+∞、Source Trail / Apart。仅核验公开页面、准备文案与本地包；未登录、未接受条款、未加入赛事、未上传或点击最终提交。不能把本目录当作参赛成功凭证。

## 当前结论

| 项目 / 官方入口 | 当前状态与截止 | 仍需真实完成 |
| --- | --- | --- |
| [Lumen Shift / Game Off](https://itch.io/jam/game-off-2026) | 公开页仍显示 Join jam。官方截止 2026-12-01 13:37 PST，即12-01 21:37 UTC / 北京12-02 05:37。 | itch.io账号、加入jam、创建可玩HTML游戏页、上传ZIP、如实填写AI披露和jam表、最终参赛确认。 |
| [Parallax / Through Your Eyes](https://itch.io/jam/through-your-eyes-first-person-game-jam) | 公开页仍显示 Join jam。正文11-15；页面原始 end_date 为 `2026-11-15 17:24:24`，未标时区，不能自行换算北京时间。 | 登录确认账户倒计时及当前额外要求，创建并上传游戏页，加入并提交该jam。 |
| [纸路 / AI+∞](https://mseo-ai-inf.ms.show/) | 报名截止12-01 12:00、作品12-01 18:00；公开页未明示时区，提前完成并以登录后的官网状态核对。 | 公开构想帖及审核、魔搭账号、公开可运行的创空间、手记与真实视频、官网最终交件。 |
| [Source Trail / Apart](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15) | Sign up按钮未禁用；11-06抓到的Submit project实际带disabled，表内提示submission window closed。赛期11-13至15；截止11-15 23:59 AoE =11-16 11:59 UTC / 北京19:59。 | 可准备报名；当前不能称项目提交窗口可用。还需赛期新增研究、按官方流程填写作者资料、官方模板PDF和最终提交。现有16例pilot均是11-05赛前材料。 |

## 1. Lumen Shift：硬条件与字段证据

[GitHub官方公告](https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/)确认主题SHIFT、主要开发在赛期内、GitHub源代码和最终推送、itch.io参赛提交，以及AI辅助允许但须披露。作品11-05开始，八关实际使用循环位移/XOR，不能把GitHub推送当作jam提交。

[HTML游戏上传说明](https://itch.io/docs/creators/html5)确认New Game入口、HTML Game类型、ZIP根index、相对资源路径和嵌入设置。`https://itch.io/game/new`在本次未登录访问中返回403，**没有读取该账号的实际编辑表或Game Off自定义表单**。标题、简述、正文、上传包、类型与嵌入建议已备妥；GitHub URL / SHIFT说明 / AI使用说明是准备答案，不把未知的自定义问题名、字数限制或必填状态编造成已核验。

[itch.io官方AI披露更新](https://itch.io/t/4309690/generative-ai-disclosure-tagging)列出Code、Text & Dialog等类别。请选Yes，本次代码、文字和投稿封面均含AI辅助创作，应如实披露Code、Text & Dialog与Graphics；程序绘制视觉和合成音的边界已在credits草稿，不可填成纯人工制作。登录后如出现更具体的图形/声音问题，按真实问题与实际使用回答；没有模型生成的贴图或音频文件。

## 2. Parallax：硬条件与字段证据

[官方jam页](https://itch.io/jam/through-your-eyes-first-person-game-jam)要求主要第一视角、可玩原型、合法分发内容；允许solo/teams、新旧项目、任何引擎。三房间主交互为第一人称Canvas2D；小地图是可选辅助。未见公开规则禁止AI，但**尚未看到登录后的jam额外限制**，不能仅凭“任意引擎”推定任何账号都已通过资格。

上传设置按上述itch官方HTML文档准备，账户编辑表与jam自定义问题仍需登录后核对。公开元数据无时区的日期字符串已核对，不把其当UTC。主要页面、credits、AI披露与真实录制脚本位于drafts/parallax-postcards。

## 3. 纸路：硬条件、入口和未读取字段

官网[报名](https://mseo-ai-inf.ms.show/register)、[作品提交](https://mseo-ai-inf.ms.show/submit)链接已核验；未登录读取仅得到页面壳，不能核实真实表字段、文件限制、电话/实名等账号要求。已准备标题、概述、构想帖链接、创空间链接、手记链接、工具说明等内容，**这些是映射用材料，不是对隐藏表字段的断言**。

公开规则明确：先发布带活动话题和账号提及的构想帖，官网交链接审核；游戏部署魔搭创空间并公开可运行；按[官方创作手记模板](https://modelscope.cn/posts/437860)在[魔搭开发者实践](https://modelscope.cn/spotlight)发手记并附演示视频、真实工具截图/运行记录。该模板页本次无可读正文，草稿未假称逐字段复刻模板。作品须当期首次公开，禁止其他赛事成果参赛；纸路独立创作，不把其他游戏换名来提交。

选“AI游戏作品”，不声称已满足DGX推理的Agent赛道。Qoder在本次可读规则中不是强制工具；实际使用Codex，不能编造Qoder/DGX/魔搭推理体验。Static部署参考为[ModelScope官方说明](https://github.com/modelscope/modelscope-skills/blob/main/skills/ms-studio-deploy/SKILL.md)，须上传ZIP内文件到空间根目录；**该ZIP不是赛事官网作品链接的替代品**。目前的Sites私有预览不是魔搭创空间地址。

## 4. Source Trail：公开表单与赛期边界

官方页面公开呈现两张表。以下为11-06真实公开字段，不含任何虚构个人资料：

- 报名必填：First name、Last name、Email、Location。可选：LinkedIn、Scholar、GitHub、Current job、AI safety experience、Why joining、项目意向、获知渠道。
- 项目必填：Project title、Project summary、PDF report（≤25 MB）、是否愿意发表、Team name、Location、成员姓名与邮箱。可选/未标星：Tracks、Presentation recording、Project code、Slides（≤25 MB）、Project image（≤25 MB）、Additional material、Discord、Scholar；可增加成员。愿不愿发表是个人选择，未代选。

提交时会同意[提交与奖金条款](https://apartresearch.com/sprints/prize-terms)，不代接受。当前Submit project按钮禁用且有closed状态，不能绕过页面调用POST。报名按钮未禁用不等于已提交成功；真实账户/邮箱验证由授权操作者完成。

[官方报告模板（Google复制链接）](https://docs.google.com/document/d/17b3JWki-ZkaqdmqGI5d0gof-HwlGuWU9Mc1_klNZXKs/copy?usp=sharing)已从Guidelines提取，打开copy被要求Google登录。官方要求正文≤8页（参考文献/附录除外）、150–250词abstract、真实作者/机构、必需Limitations and Dual-Use / Ethical Considerations附录。当前只有研究计划和赛前pilot，**未生成或冒充赛期成果PDF**。可复制报名文案与前瞻计划见drafts/source-trail-otari。

## 本地交付与验证

11-06重新运行：Lumen13测试、Parallax16测试、纸路15测试全部通过；各自check/build通过。没有本轮浏览器自动化或新录屏，视频文件仍待真实录制。

| 上传准备包 | 大小 | 入口与运行资源 |
| --- | ---: | --- |
| `artifacts/lumen-shift-itch.zip` | 14,794 bytes | 根index；8文件；CRC通过；HTML/CSS/JS运行引用全本地 |
| `artifacts/parallax-postcards-itch.zip` | 18,040 bytes | 根index；6文件；CRC通过；无WebGL、外部素材或模型调用 |
| `artifacts/paper-route-playtest-modelscope-static.zip` | 18,335 bytes | 根index；6文件；CRC通过；需要解包到Static创空间 |

完整SHA和文件清单：[game-research-four-manifest.json](artifacts/game-research-four-manifest.json)。重建命令：先运行三个项目的build，再运行 `python3 portfolio/submissions/package-game-research-zips.py`。包不含.git、.openai、密钥、数据库或node_modules。SVG命名空间只是格式标识，不是远程资产请求。

## 执行者还需补齐

基础身份资料已私密确认；平台账号/适用条款/实际材料仍待处理，个人资料不写入公开文件。还需itch/魔搭登录与平台显示名确认；实际封面截图/必要视频及公开链接；登录后自定义题目或首次发布声明的真实答案；最终提交成功页面/收据。不要将占位符、私有预览、录制脚本或赛前计划当成最终已交材料。没有发送消息、操作账号、注册、付费、接受条款或提交任何赛事。

## 原创投稿图（不是截图）

三游戏drafts各有`media/cover.png`与可编辑SVG，均为630×500；已本地查看，文字/构图完整。它们是本次Codex辅助的程序矢量封面，CairoSVG2.8.2本地转PNG，不是游戏截图或图像模型输出。SourceTrail另有`media/pilot-results.png`，仅绘制实际11-05pilot的n/N，明确标赛前/合成/非LLM，不包含未来研究结果。真实游戏截图与录像仍待录制。

可用`render-game-research-media.py`复现，依赖CairoSVG2.8.2（本次仅安装在临时构建环境，未加入游戏运行依赖）；媒体SHA清单见artifacts/game-research-media-manifest.json。
