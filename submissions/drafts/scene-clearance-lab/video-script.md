# Aholo真实录屏计划 / honest recording plan

建议3分钟，非已核实的视频时长硬限制。当前没有视频、真实Lux3D资产或公共评委Demo链接；私有预览不是交件证据。

| 时间 | 真实操作 | 中英旁白要点 |
|---|---|---|
| 0:00–0:25 | 标题、目标用户、布局A | “生成模型之后，怎样解释这一版布置？” / “A generated model is only the beginning; this desk makes layout choices inspectable.” |
| 0:25–0:55 | **仅在实际生成后**展示Lux3D关键资产/迭代及导出，隐藏账号信息 | 讲清哪些核心资产确实由Lux3D生成，哪些是原有程序几何。未发生时不能用程序样例代替这一段。 |
| 0:55–1:30 | 导入真实导出文件，查看单位与指纹，再拖动/数值摆放 | “文件不上传；单位人工核对，来源声明不自动等于已核验。” / “The source hash binds this local file; units still need human review.” |
| 1:30–2:00 | 解释一次实际代理重叠，修改位置 | “这是保守包围矩形，不是精确网格或人体通行判断。” / “These are conservative footprint checks, not exact mesh or safety certification.” |
| 2:00–2:35 | 保存B、同参数比较A/B，导出JSON/Markdown | “保留坐标、检查参数和逐对间距，让变化能复核。” / “The report retains assumptions and pairwise distances.” |
| 2:35–3:00 | 限制、开源署名、可访问项目地址 | “目前支持明确的静态glTF子集；没有法规结论。” / “This is a narrow local layout workflow with documented import limits.” |

本地准备：项目目录 `npm run build`、`npm run dev`，访问 `http://127.0.0.1:4187`。可先用原创测试资产练习录屏，但该片段必须标“原创程序样例，非Lux3D”，不能据此勾选赛事的真实Lux3D确认。完整报告正文见 [report-draft.md](report-draft.md)；真正拍到的过程截图再加入PDF/PPT。
