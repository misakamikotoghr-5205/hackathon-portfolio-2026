# 留白实验室 — Aholo 报名与作品草稿，2026-11-06

官方[中国活动页](https://www.aholo3d.cn/hackathon)、[英文活动页](https://www.aholo.ai/hackathon)。截止 **2026-11-19 19:00 北京 / 11:00 UTC / 06:00 EST**。本稿未登录、未报名或接受条款。网页文字抽取为空；下列字段来自活动页直接加载的官方公开前端代码，不冒称已查看用户登录后的实际表单。

## 先报名/选题，再交件

当前公开流程：个人报名 → 创建/加入团队并确认 → 队长提交选题 → 提交作品。单人也须建队，队伍 1–3 人。

公开代码显示个人报名有姓名、邮箱、国家/地区和城市、身份，以及本人阅读同意报名须知；姓名提示 2–30 字符。团队名提示 2–20 字符。实际身份、地区和联系方式仅在私有表单填写，不存入此处。

选题名称（2–40 字符）：**留白实验室**

选题简介（10–500 字符，可直接填）：

> 面向需要摆放生成模型的个人创作者，计划用 Aholo Lux3D 生成核心陈列物件，再在本地导入、调整位置与尺度，解释保守几何代理的重叠、间距与留白带，保存 A/B 方案并导出可审阅报告。当前下游工具已实现；尚未真实生成 Lux3D 资产或验证其导出兼容性。选题阶段先明确这项缺口，正式作品将以真实使用记录为准。

English title: **Scene Clearance Lab**

English idea summary (short, within the published 500-character idea limit):

> A local layout desk for generated 3D objects: place supported models, inspect conservative footprint gaps and overlaps, compare two layouts and export an auditable report. The downstream tool works today. Core Lux3D generation and actual export compatibility still need to be demonstrated; current built-in geometry is original procedural test content, not Lux3D output.

## 完整作品介绍 / English project description

留白实验室把“看见一个模型”接到“这版如何摆放”的具体流程：受支持 glTF/GLB 文件在本地导入，记录 SHA-256 与人工单位覆盖，拖动或数值调整位置、旋转和尺度，用定向包围矩形说明重叠、接触和最近水平间距；保存两种方案时核对检查参数是否一致，导出 JSON/Markdown 报告。数据不上传，运行时无远程模型/CDN。WebGL2 不可用时可使用明确标注的俯视降级视图。

当前实际复用 Three.js/OrbitControls，受限格式解析器、几何代理、报告、存档及程序物件独立实现。包围代理不是精确网格碰撞、人体通行、承重或法规判断；0.6m/1m仅示例参数。尚未使用 Aholo 账号生成核心资产，不能把自述来源或本地示例当作 Lux3D 证据。

Scene Clearance Lab connects model preview to a reviewable layout workflow. It imports a documented local glTF/GLB subset, records file hashes and human-confirmed units, supports placement/rotation/scale, explains conservative footprint overlap and clearance, and compares two layouts under explicit parameters. JSON and Markdown reports retain transforms, provenance declarations, pairwise distances and limitations. Nothing is uploaded by the runtime.

The working tool uses real vendored Three.js and OrbitControls, with independently implemented parsing, footprint checks and reports. Built-in objects are original procedural fixtures. No Aholo generation or actual Lux3D export compatibility has yet been demonstrated, and the project must not be submitted as having met that requirement until a genuine authorized asset workflow has been completed.

## 公开作品表字段与当前可填内容

| 字段/校验 | 本作品真实内容 |
|---|---|
| 选题名/简介 | 上述内容，可在截止前修改 |
| 项目报告书 | [report-draft.md](report-draft.md) 是正文草稿；真实过程/资产迭代/效果截图仍需取得，再制作 PDF/PPT/PPTX 或评委可访问报告链接 |
| 完整 Demo / 宣传视频 | 需真实可运行链接或含真实运行的录屏，可链接或上传；当前所有者私有预览不能当公开评委链接 |
| 应用赛道 | 当前公开代码要求选 1–3 项或“无”；未核实所有实际选项，不捏造赛道名 |
| 生态合作设备/技术 | 未使用相应生态设备/技术时选择“无”；没有云深处、影石、WorkBuddy使用证据 |
| “作品使用 Aholo Lux3D 完成且可运行演示”确认 | **当前不可如实确认**；需真实生成与导出运行证据 |
| 提交须知/真实性确认 | 本人/root核对后操作，本稿不代同意 |
| 源代码/压缩包（加分材料） | https://github.com/misakamikotoghr-5205/scene-clearance-lab |
| 社媒发布链接（加分材料） | 未发帖；中国页要求 #Aholo黑客松，不能伪造公开链接 |

## 技术、差异、过程与披露

- 技术：JavaScript ES modules、Canvas降级视图、Three.js 0.180.0 / OrbitControls、Web Crypto、原创静态 glTF 样例、本地存档。16项行为测试是本地验证，不证明所有平台导出都兼容。
- 差异：具体的“单位与指纹 → 放置 → 可解释保守间距 → 同参数 A/B → 报告”流程；不是通用 glTF 优化器或专业空间设计系统。
- 构建过程：先定义可导入格式和拒绝边界，再实现几何代理与独立几何测试、布置与参数比较，最后核对本地库许可、打包与浏览器降级。不能虚构 Lux3D 生成步骤。
- AI：Codex辅助设计、编码、测试和文档；运行时没有模型调用。Lux3D后续生成必须独立保留真实账户/生成/授权记录。
- OSS：原创代码/物件 MIT；实际复用的 Three.js/OrbitControls 原始 MIT、版权和指纹均保留。glTF Viewer 与 glTF Transform 仅为设计比较，没有复制其代码或第三方美术资产。
- 当前状态：可运行下游原型；Aholo核心资产条件、真实报告截图/视频、账号和正式提交均未完成。
