# 纸路邮局：让一条派送路线留下可检查的证据

状态：2026年11月10日更新的发布底稿，尚未在魔搭公开发布。主操作者已在原生浏览器完整查看[官方创作手记模板](https://modelscope.cn/posts/437860)（MSEO，页面更新于2026年10月31日），本稿按其六个部分组织。[赛事主页](https://mseo-ai-inf.ms.show/)已于11月10日重新查看；实际报名、公开创空间和最终交件仍未完成，账号独立条款待本人确认。

- 作品名称：纸路邮局 · Paper Route
- 参赛方向：AI 游戏作品
- 试玩链接：待魔搭创空间真实公开部署后填写；[源码与本机运行说明](https://github.com/misakamikotoghr-5205/paper-route-playtest)已公开，本机地址不是创空间试玩链接。
- 演示视频：[158秒中文静音演示MP4](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/media/paper-route-local-demo.mp4)已完成，完整解码、16段中点和实际画面检查通过；真实本地截图剪辑，非连续录屏，无旁白。[媒体记录](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/local-demo-20261110.json)列明制作方式。尚未在魔搭发布视频。已查看的主页和模板正文未见固定时长或配音格式要求。

## 一、创意与玩法

纸路邮局是一款四关网格取送解谜。派送员只能携带一件包裹，小写a/b是取件点，对应大写A/B是收件点；关卡进一步引入开关桥和步数预算，必须全部送达后返回邮局。seed只选择四种手工地图镜像。

除手动游玩，游戏提供免费路线提示、规则自动试玩、撤销和可导入的动作重放。缺陷实验室把一个故意取消门牌匹配的错误版本与严格规则并排比较，解释同一条路线为什么会在投递边界分歧。目标是让玩家能分享可复现的过程，而不仅是一张胜利截图。网格解谜、寻路和自动求解都有成熟先例，本作的差异是这套取送规则与动作证据、严格重放及隔离反例的组合。

## 二、创作过程：AI与参赛者各自完成什么

参赛者提供活动方向、差异化项目与投稿要求、个人身份资料和账号/投稿授权。Codex及并行代理完成方案细化、原创引擎、四关布局、程序视觉、页面交互、测试、证据检查和材料整理；主操作者通过CUA实际操作浏览器，其他代理只读核对导出与源码。本文的开发和操作事实来自这些记录，不据此推定参赛者本人编写代码或亲自体验过每一项操作。

实现先把位置、口袋、已送达集合、桥开关、预算和动作历史放入纯状态引擎，再接入界面、撤销、导入导出与本地恢复。BFS从当前合法状态搜索剩余最短路线，规划和实际移动共用严格规则；缺陷搜索使用独立的人工变异开关。

证据分两批保留：

- **11月6日，本地Node引擎批次。** 固定seed20261106，四关路线为12/20/12/28步，逐步执行、导出并严格重放；隔离变异体得到四次右移的反例。原始manifest、日志和产物保持不变。这一批没有浏览器或平台操作。
- **11月10日，实际本地浏览器批次。** 观察日志覆盖09:25:52.776–09:28:26.281 UTC。第一关手动右移、撤销、提示和12步规则试玩通关后，实际下载重放、重置并通过文件选择器重新导入，页面验证重放12步。第三关两次右移打开桥，实际刷新后恢复位置、2/24步与桥状态；隔离变异体观察0/3/4步并实际导出报告。仅这些流程完成了本次UI核验。

当前源码与历史manifest的八个文件一致，dist四个运行资产与源码字节一致；本次新增文档和证据，没有为补材料修改引擎、重跑全套测试或重新构建。

## 三、工具应用与体验

| 工具或方法 | 实际使用场景与效果 | 可检查记录与边界 |
| --- | --- | --- |
| Codex与并行代理 | 设计、实现、交叉检查、材料整理；把“能运行”拆为可逐项验证的规则与界面操作 | [源码](https://github.com/misakamikotoghr-5205/paper-route-playtest)、[AI辅助开发记录](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/ai-development.md)及下述实际执行证据；不虚构个人编程经历或未记录的工具体验 |
| Node.js、既有验证器 | 执行纯状态引擎、严格重放及固定种子证据校验 | [11月6日manifest](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/manifest.json)、[日志](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/run.log)；本地执行不等于创空间运行 |
| 原生浏览器与CUA | 实际点击移动、撤销、提示、规则试玩、文件导出/导入、桥开关和刷新恢复 | [11月10日UI记录](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/browser-verification-20261110.json)与实际JSON下载；原始截图因浏览器/账号上下文保持私密，发布视频需使用另外检查过的裁切画面 |
| 自行实现的BFS | 第一关提示剩余12步、检查35状态且不执行动作；隔离错误门牌反例检查9状态 | 确定性状态搜索，无运行时LLM调用，不计为模型推理、AI NPC或DGX Spark部署 |

实际工作方式的收益是把证据缺口暴露出来：Node验证可以确认规则重放，却不能确认浏览器文件按钮、本地存储或平台发布。将这些步骤分开后，新增的UI记录可以明确回答“具体哪项真的操作过”。Qoder、魔搭模型/API和DGX Spark均没有实际使用记录；游戏运行时没有模型、远程素材、遥测或网络API。

## 四、问题与解决：补齐浏览器证据缺口

最初的材料只有11月6日Node引擎执行证据，手记仍把真实浏览器导入、刷新恢复与演示列为待办。它不足以证明用户在浏览器里能通过文件选择器恢复同一局，也不足以证明页面刷新后桥开关仍正确。这里解决的是验证材料的缺口，没有声称发现并修复新的引擎漏洞。

11月10日实际操作后，新增了两个原样下载文件：

| 文件 | 实际结果 | 大小及指纹 |
| --- | --- | --- |
| [第一关重放](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/browser-export-first-mile-20261110.json) | UI导出、重置、同文件严格导入，恢复12/18步通关；独立重放核对口袋空且返回邮局 | 369字节；SHA-256 `ed19852affd40c6f865f0e47960824109d6042fe78ecd25228e6864da8ed3215` |
| [隔离错误投递报告](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/browser-export-defect-20261110.json) | 两边前3步完整状态相同；第4步严格版仍携带a、已投递为空，人工变异体口袋空且错误记a已送达，投递事件的`valid=false` | 1,053字节；SHA-256 `7e6f48372a1c9584bbd99429332b1f0011c517987fb92fff520ec77d771288f0` |

两份UI下载与11月6日对应文件解析后的JSON相同，原始字节不同：旧文件各多一个末尾LF。本次保留实际下载字节，没有为对齐旧哈希修改文件。第三关桥状态则由真实刷新观察确认。15张静态截图是分步观察，不能据此声称连续录屏、四关全量浏览器验证、移动端验证或公开平台上线。

## 五、经验总结

把规则、界面和平台三层分别留证据，能减少“本地测试通过”被误写成“已经公开部署或参赛”的情况。重放文件比单张通关截图多保留初态、seed和动作；重新导入时从严格规则重算结果，能让别人复核路线。

人工变异体适合解释一条具体不变量：错误门牌不能收货。反例针对这个隔离演示，不是线上产品安全漏洞或真人试玩发现。提示中的状态数是BFS出队计数，不是模型思考次数或用户表现指标。

当前仍需完成账号条款确认、公开构想帖及报名审核、真实创空间部署和公开试玩核验、演示视频在魔搭发布、创作手记发布、最终官网交件。后续应把真实公开链接与官方回执补入材料；GitHub仓库、私有预览、本地端口和本文底稿分别承担自己的用途。

## 六、工具与素材来源

- [Paper Route公开源码](https://github.com/misakamikotoghr-5205/paper-route-playtest)采用[MIT许可](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/LICENSE)。代码、四关手工地图和CSS/程序图形为本次独立实现；没有捆绑第三方运行时代码、图片、音频、字体、角色或商标资产。
- AI辅助工具是Codex；具体贡献见第二、三部分。原始开发与操作记录仅在不暴露个人资料、账号或凭据的范围内作为材料使用。游戏没有外部模型权重、推理API或在线知识库依赖。
- [PuzzleScript](https://github.com/increpare/PuzzleScript)与[PathFinding.js](https://github.com/qiao/PathFinding.js)是已阅读的设计比较来源，均按固定版本查过MIT许可；没有复制、修改或捆绑它们的代码、关卡或美术。固定版本与差异见[开源调查](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/landscape.md)。BFS为通用算法，本项目状态搜索独立编写。
- 官方材料来源：[赛事主页](https://mseo-ai-inf.ms.show/)、[创作手记模板](https://modelscope.cn/posts/437860)、[ModelScope官方Static部署说明](https://github.com/modelscope/modelscope-skills/blob/main/skills/ms-studio-deploy/SKILL.md)。它们用于核对投稿和部署要求，不是已完成报名或部署的证明。
- 事实证据索引：[11月6日Node批次与11月10日UI批次说明](https://github.com/misakamikotoghr-5205/paper-route-playtest/blob/main/docs/evidence/README.md)。原始私密截图不直接公开；视频和任何新增素材的实际来源、制作方式及完成状态由后续媒体记录单独披露。


可用于发布的脱敏实际画面（取自上述MP4）：

![严格重算导入](https://github.com/misakamikotoghr-5205/paper-route-playtest/raw/main/docs/media/reimport-verified.png)

![隔离人工缺陷对照](https://github.com/misakamikotoghr-5205/paper-route-playtest/raw/main/docs/media/injected-defect.png)

![桥开关刷新恢复](https://github.com/misakamikotoghr-5205/paper-route-playtest/raw/main/docs/media/bridge-restored.png)
