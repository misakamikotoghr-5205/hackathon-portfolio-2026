# Watt Window — Next Horizon first-stage draft, 2026-11-06

Official [event and FAQ](https://eisociety.org/hackathon.php?slug=next-horizon-2026). Its [Apply/Register redirect](https://eisociety.org/go/apply/next-horizon-2026?s=direct) currently leads to [this Google Form](https://docs.google.com/forms/d/e/1FAIpQLSe8dF2jynROjU4mEbypJJhNY-oyfxaY_c7wPLDBggET2gMOrQ/viewform?usp=send_form). The official form has now actually required Google sign-in. The browser is waiting at the existing account’s password/passkey sign-in page for the owner to complete login; the form fields and required markers have **not** been seen. No form content has been prefilled or submitted. Use the link reached from the official event if it changes.

Idea deadline **November 15, 2026**; no exact cutoff hour is published. First stage requires a PowerPoint up to 15 MB, not just a repository. A prototype video of 2–4 minutes is optional. Places are limited; shortlisting and notice are November 16/17. The actual 48-hour event is **November 28 09:00 EST–November 30 09:00 EST** (14:00 UTC / 22:00 Beijing each day), including final presentations.

## Title / primary theme

English: **Watt Window — explainable time windows for noncritical energy use**

中文：**Watt Window · 非关键负载的可解释时间窗**

Primary theme: **Smart Cities and Sustainable Development** (energy management). The prototype performs no runtime AI inference; do not choose an AI theme based solely on AI-assisted coding.

## English abstract — paste-ready

Watt Window is an offline advisory scheduler for user-confirmed noncritical household or shop loads. A cheap tariff slot can still violate a closing-time window, locked task or concurrent power limit. The tool takes an explicit time grid, entered tariffs, estimated energy and power, background load and job windows. It evaluates the original plan, searches for a lower-cost valid allocation and explains both the chosen schedule and cases where no plan fits.

The working pre-event prototype uses Python's standard library and exact rational cost comparisons. Bounded search distinguishes proven model optimality, a valid plan without proof, budget exhaustion without a plan and proven finite-model infeasibility. Reports preserve assumptions and baseline validity, with JSON/HTML/CSV/ICS exports and hypothetical sensitivity cases. Seventeen local tests include independent small-instance brute-force comparisons.

This code was created November 5, before the November 28–30 event. It is explicitly preexisting preparation, not work completed in the future 48-hour window. No real electricity saving, carbon reduction, device control, measured tariff or actual household trial is claimed. If shortlisted, the proposed event work is a documented new evaluation with independently authored workload cases and a clearer assumption-review workflow, while preserving honest proof/budget status. Basic identity has been privately confirmed, and a private signed first-stage PowerPoint is prepared. The official Google sign-in and application process still need to be completed; no registration or submission receipt is claimed.

## 中文摘要

最便宜时段不一定满足营业窗口、固定作业与并发功率约束。Watt Window 对用户确认的非关键负载，显式录入时间窗、电价与估计能耗，比较原计划和候选排程，并区分模型内已证最优、预算内找到可行解、预算耗尽未找到、已证不可行。离线Python原型可导出可审阅报告及日历文件，没有设备控制、真实节能或碳减排测量。11月5日代码是赛前准备；若入围，未来48小时内新增评估与改进会单独记录，不把现成仓库冒充赛期成果。

## Technology, difference, process and disclosures

- Technology: Python 3.11+ standard library, Fraction arithmetic, bounded branch-and-bound, necessary interval-capacity witnesses, IANA timezones, escaped HTML and structured/calendar exports. No account, network/device API or expensive hardware needed.
- Difference: a small inspectable advisory artifact emphasizing invalid-baseline disclosure, bounded-search status, infeasibility witnesses and sensitivity assumptions. No battery/PV, thermal/forecast or real-time automation model.
- Process: write explicit finite-grid assumptions → check baseline → implement exact-cost search and proof statuses → add explanations/exports → compare with an independent enumeration oracle and exercise CLI exports. All examples are fictional, user-input estimates.
- AI: Codex assisted planning, implementation, tests and documentation; no model-based scheduling or runtime inference. No fabricated users, measured savings or institutional affiliation.
- OSS: original code/fictional examples MIT. EMHASS(MIT) and FlexMeasures(Apache-2.0) were design comparisons only, with no copied code/assets/tests or dependency. Energy optimization is established work; no novelty or superiority guarantee.
- Preexisting disclosure: all current November 5 prototype code predates the event build window. After actual shortlisting, record any event-period evaluation/code separately.

## Official material mapping

| Material | Prepared content / state |
|---|---|
| Team details | Basic identity confirmed privately; personal values remain outside the public repository, with no invented affiliation |
| Problem | Abstract and slide 2 in [pitch-draft.md](pitch-draft.md) |
| Solution/technical approach | Slide 3 and technical disclosure above |
| Impact/feasibility | Slide 4, explicitly estimated rather than measured benefits |
| Implementation plan | Slide 5, preexisting vs future event work separated |
| PowerPoint up to 15 MB | Six-slide anonymous public draft and a separate completed private signed PowerPoint are prepared; the private version is not published |
| Optional 2–4 minute prototype video | Concrete [video-script.md](video-script.md); not yet recorded |
| Repository | https://github.com/misakamikotoghr-5205/watt-window |

For any authenticated/Google-form field not publicly visible, root should map this content after observing its actual label rather than inventing an answer or required limit. Registration/shortlisting and the final 10-minute pitch plus 5-minute Q&A remain separate steps.
