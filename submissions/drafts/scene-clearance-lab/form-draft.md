# 留白实验室 — Aholo 作品草稿，更新于2026-11-10

官方[中国活动页](https://www.aholo3d.cn/hackathon)、[英文活动页](https://www.aholo.ai/hackathon)。截止 **2026-11-19 19:00 北京 / 11:00 UTC / 06:00 EST**。11月10日已真实登录并完成个人报名，官方显示“报名成功，欢迎加入！”；一人队伍“留白工坊”已确认，成员1/3，“留白实验室”选题已提交。官方第4阶段“作品提交”已打开，前三项勾选、报名积分及团队积分已发放，5页PDF报告已实际上传，材料4/4齐备后已正式交件，官网显示“已提交”、“第1版·提交于11月10日09:02”及“作品已进入资格与完整性审核”。[脱敏交件记录](https://github.com/misakamikotoghr-5205/scene-clearance-lab/blob/main/docs/evidence/submission-receipt-20261110.json)另存。下列作品表说明保留公开前端核对依据及实际提交内容；不公开联系信息或邀请标识。

## 先报名/选题，再交件

流程：个人报名 → 创建/加入团队并确认 → 队长提交选题 → 提交作品。四阶段均已完成，无需重复报名、建队、选题或正式交件，当前等待资格与完整性审核。

Lux3D真实图生3D任务已完成，官方UI已下载GLB；离线探针和实际浏览器导入成功并匹配SHA-256及几何统计。实际45,753顶点、91,530三角形、单图元、零纹理；按glTF默认米制读取尺寸，不证明真实尺寸准确。平台WebGL预览黑屏，本地实测是2D俯视代理降级。后续证据与取证步骤见 [lux3d-handoff-zh.md](lux3d-handoff-zh.md)；同参数A/B和5页PDF已完成，报告已实际上传；128秒实机截图剪辑视频已完成并随作品正式提交，原始模型不公开。

公开代码显示个人报名有姓名、邮箱、国家/地区和城市、身份，以及本人阅读同意报名须知；姓名提示 2–30 字符。团队名提示 2–20 字符。实际身份、地区和联系方式仅在私有表单填写，不存入此处。

选题名称（2–40 字符）：**留白实验室**

选题阶段简介草稿（10–500 字符；保留当时对缺口的说明）：

> 面向需要摆放生成模型的个人创作者，计划用 Aholo Lux3D 生成核心陈列物件，再在本地导入、调整位置与尺度，解释保守几何代理的重叠、间距与留白带，保存 A/B 方案并导出可审阅报告。当前下游工具已实现；尚未真实生成 Lux3D 资产或验证其导出兼容性。选题阶段先明确这项缺口，正式作品将以真实使用记录为准。

English title: **Scene Clearance Lab**

English idea summary (short, within the published 500-character idea limit):

> A local layout desk for generated 3D objects: place supported models, inspect conservative footprint gaps and overlaps, compare two layouts and export an auditable report. The downstream tool works today. Core Lux3D generation and actual export compatibility still need to be demonstrated; current built-in geometry is original procedural test content, not Lux3D output.

## 完整作品介绍 / English project description

留白实验室把“看见一个模型”接到“这版如何摆放”的具体流程：受支持 glTF/GLB 文件在本地导入，记录 SHA-256 与人工单位覆盖，拖动或数值调整位置、旋转和尺度，用定向包围矩形说明重叠、接触和最近水平间距；保存两种方案时核对检查参数是否一致，导出 JSON/Markdown 报告。数据不上传，运行时无远程模型/CDN。WebGL2 不可用时可使用明确标注的俯视降级视图。

当前实际复用 Three.js/OrbitControls，受限格式解析器、几何代理、报告、存档及程序物件独立实现。包围代理不是精确网格碰撞、人体通行、承重或法规判断；0.6m/1m仅示例参数。一个真实Lux3D导出物件已完成生成、下载及导入，其他五件为原创程序物件；来源标识仍诚实保留“用户自述、未核验”，与外部生成/下载证据分开，不把本地标签当平台认证。

Scene Clearance Lab connects model preview to a reviewable layout workflow. It imports a documented local glTF/GLB subset, records file hashes and human-confirmed units, supports placement/rotation/scale, explains conservative footprint overlap and clearance, and compares two layouts under explicit parameters. JSON and Markdown reports retain transforms, provenance declarations, pairwise distances and limitations. Nothing is uploaded by the runtime.

The working tool uses real vendored Three.js and OrbitControls, with independently implemented parsing, footprint checks and reports. Personal registration, a one-person team and the topic are confirmed. One actual Lux3D task with a 100K face target and PBR off completed; the officially downloaded GLB passed the existing offline importer and actual browser import with matching hash and geometry counts. Other objects are original procedural fixtures. The platform viewer was black and the application ran in interactive 2D footprint fallback; full WebGL mesh rendering has not been verified. Actual same-parameter A/B evidence, a five-page PDF and a 128-second edited screenshot video are complete. After the participant confirmed the final submission terms, both files were formally submitted. The official UI shows Submitted, version 1, submitted November 10 at 09:02, and entry into eligibility and completeness review. This confirms receipt, not approval or a judging outcome. Raw model bytes are private and are not covered automatically by the code's MIT license.

## 公开作品表字段与当前可填内容

| 字段/校验 | 本作品真实内容 |
|---|---|
| 选题名/简介 | “留白实验室”选题已提交；本稿保留选题阶段对实际缺口的说明，不代表后续资产条件已完成 |
| 项目报告书 | [report-draft.md](report-draft.md) 对应5页PDF已完成、逐页检查且实际上传；真实生成、导入、同参数A/B与下载报告已记录。仅生成一版，没有虚构迭代 |
| 完整 Demo / 宣传视频 | 128秒无音轨、中文字幕的真实运行截图剪辑已上传；不是连续录屏，已检查全片解码及10个关键帧 |
| 应用赛道 | 已在官方表单选择“空间设计应用奖” |
| 生态合作设备/技术 | 实际已选“无”；没有云深处、影石、WorkBuddy使用证据 |
| “作品使用 Aholo Lux3D 完成且可运行演示”确认 | 已有真实Lux3D生成、官方UI下载、成功导入及同参数A/B证据；已按本人当次确认完成本次正式提交，不主张完整WebGL预览已验证 |
| 提交须知/真实性确认 | 本人当次确认后已实际勾选并正式提交；官网收件及进入审核已核验 |
| 源代码/压缩包（加分材料） | https://github.com/misakamikotoghr-5205/scene-clearance-lab |
| 社媒发布链接（加分材料） | 未发帖；中国页要求 #Aholo黑客松，不能伪造公开链接 |

## 技术、差异、过程与披露

- 技术：JavaScript ES modules、Canvas降级视图、Three.js 0.180.0 / OrbitControls、Web Crypto、原创静态 glTF 样例、本地存档。16项行为测试是本地验证，不证明所有平台导出都兼容。
- 差异：具体的“单位与指纹 → 放置 → 可解释保守间距 → 同参数 A/B → 报告”流程；不是通用 glTF 优化器或专业空间设计系统。
- 构建过程：先定义可导入格式和拒绝边界，再实现几何代理与独立几何测试、布置与参数比较，最后核对本地库许可、打包与浏览器降级。不能虚构 Lux3D 生成步骤。
- AI：Codex辅助设计、编码、测试和文档；本地工具运行时没有模型调用。真实Lux3D参考图、3D生成、官方UI下载及实际本地导入均有记录；平台WebGL黑屏，本地实际为2D代理降级，不能冒充完整网格渲染。
- OSS：原创代码/物件 MIT；实际复用的 Three.js/OrbitControls 原始 MIT、版权和指纹均保留。glTF Viewer 与 glTF Transform 仅为设计比较，没有复制其代码或第三方美术资产。
- 当前状态：账号登录、个人报名、一人组队、选题及一个真实资产的生成/下载/导入已完成；同参数A/B及5页PDF已完成，报告已实际上传（后台4/4）；128秒实机截图剪辑视频已完成并正式提交，官网收件已核验，等待资格与完整性审核。商业或再分发授权未核实，原始模型保持私密，报告/视频为带AI标识的非商业展示。

本次实际A/B：同一资产从X0/Z0移到X-2/Z1.8，yaw0、scale1；同9×7m房间、0.6m间隙、1m留白带，6物件提醒4→2，仍保留1条重叠和1条留白带提醒。[官方提交须知](https://www.aholo3d.cn/hackathon/submission)要求完整报告，视频必须含真实运行画面且可剪辑；展示授权不等于原始GLB商业/再分发许可。
