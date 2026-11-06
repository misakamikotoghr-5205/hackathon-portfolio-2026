# Dependency Evidence for Jira — Codegeist draft, 2026-11-06

Official [event](https://codegeist2026.devpost.com/), [rules](https://codegeist2026.devpost.com/rules). Public Join redirects to Devpost authentication; authenticated question labels/limits were not inspected. Use the event's own Join and submission flow. Deadline **December 22 12:00 PST = 20:00 UTC = December 23 04:00 Beijing**. Entrant identity, age/location/conflict eligibility and permissions remain private checks.

## Title / tagline

English: **Dependency Evidence for Jira — recheck the context behind a release review**

Tagline: **Freeze visible dependency evidence, then show exactly what drifted.**

中文：**Jira 依赖证据台 · 复核审阅之后的变化**

Suggested main category: **Apps for Software Teams**. Do not select Rovo agents, Atlassian MCP, Teamwork Graph or Marketplace bonus prizes: those modules/publication are not implemented or evidenced.

## English summary — current-evidence version

Dependency Evidence for Jira turns a dependency review into an inspectable snapshot and later recheck. A reviewer selects a Jira issue-link type and direction, captures the dependencies visible to the current caller, and saves a private baseline. A later capture reports changed issue fields, dependency edges and scope. Hidden or missing issues, permission failures, pagination problems, collection limits and cycles remain explicit; they never become evidence that a release is ready.

The repository contains an actual Forge `jira:issuePanel`, UI Kit frontend, resolver and official SDK adapter using `api.asUser().requestJira`. Site and root context come from Forge, not a payload-selected tenant. The independently written engine has nineteen local behavior tests, real SDK type checks/bundles and offline fixtures. The app has not yet been registered, deployed, installed on a real Jira site or supplied with a judge installation link. Local fixtures are not presented as a live Jira integration.

The focused contribution is preserving the evidence behind a prior review and making later drift and incomplete collection visible. A snapshot is neither an organization-wide dependency proof nor authorization to release. Original code is MIT; Forge dependencies retain Atlassian's terms. A genuine Forge installation, judge-accessible sharing link and public demonstration are still required to turn this candidate into a complete Codegeist entry.

## 中文摘要

依赖审阅的结论依赖于当时可见的状态。项目按调用者权限采集指定方向和类型的 Jira 依赖，冻结证据后复查字段、连边及范围漂移；权限不足、缺失、分页不完整、环路和采集上限都保持显式未知。真实 Forge issuePanel、resolver、UI Kit 与 SDK 适配已实现并通过本地检查，但尚未部署、安装或真实调用 Jira，也没有评委安装链接。证据快照不等于发布批准。

## Technology, difference and process

- Built with: Forge manifest/native issue panel, official `@forge/api`, `@forge/resolver`, `@forge/react`, `@forge/bridge`, React/TypeScript checks, deterministic JavaScript graph collector/comparison and escaped local reports.
- Difference: a frozen review/recheck workflow with site/root/link-scope compatibility, conservative incomplete-evidence handling and changed-field explanations. No AI inference, organization-wide completeness claim, automatic release control or persistent server-side baseline service.
- Process: define context-bound capture schema → bounded permission-aware collection and pagination → inspectable digest/snapshot → compatibility and drift checks → wire real Forge UI/resolver → local fixture, SDK and failure-edge verification.
- AI disclosure: Codex assisted design, implementation, tests and documentation. Runtime behavior is deterministic; it does not call Rovo or an LLM.
- OSS disclosure: original application MIT. Forge packages are governed by **Atlassian Developer Terms**, not relabeled MIT. React/esbuild/yaml retain MIT, TypeScript Apache-2.0. Jira Dependency Graph and graphlib were MIT design comparisons only; their source/assets/tests were not copied. See repository notices and pinned landscape sources.
- Event-period work: newly created November 5, within Codegeist's October 27–December 22 window; third-party SDKs are pre-existing dependencies, not original inventions.

## Required materials and current values

| Public rule requirement | Value / remaining evidence |
|---|---|
| Text and explanation of required Forge use | Description above; actual installation still unperformed |
| Category and applicable bonus write-ups | Apps for Software Teams; no unsupported bonus claims |
| Judge installation/sharing link | **Missing**; must be created from a genuine registered/deployed app, not a GitHub URL |
| Full judge setup/configuration instructions | Repository README is a starting point; real installation must be checked |
| Public YouTube demo | Missing; under 5 minutes, target under 3 because judges need not watch further |
| English materials or English translations | English copy here; use English narration/captions and setup |
| Repository | https://github.com/misakamikotoghr-5205/dependency-evidence-forge ; public publication is our choice, not a substitute for an install link |

Only the owner/root should register app identity, deploy/install, review scopes and enable sharing on an authorized test site. Use fictional issue summaries in the final recording. No authenticated step or acceptance is claimed by this draft.
