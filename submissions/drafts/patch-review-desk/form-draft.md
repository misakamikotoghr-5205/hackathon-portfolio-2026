# Patch Review Desk — submitted Builder entry record

Updated 2026-11-06 07:53:18 UTC. After the owner confirmed this final submission, required processingConsent was checked, optional marketing remained unchecked, and Submit was clicked. The official submission page displayed **“Thank you for submitting.”** and **“Your project submission has been received.”** **private success-page evidence held**. No receipt number, confirmation email, judging result or award is claimed. Identity and the private screenshot remain outside this public record.

Official [submission form](https://www.builder.io/hackathon/submit), [rules](https://www.builder.io/hackathon/rules), [Clips](https://clips.agent-native.com/). Deadline: November 9 23:59 America/Los_Angeles = November 10 07:59 UTC / **15:59 Beijing**.

## Exact public form mapping

| Form label | Value or handling |
|---|---|
| First name * | Entrant's real/private form value |
| Last name | Optional; entrant's own value |
| Email * | Entrant's own reachable email; do not publish here |
| Project name * | Patch Review Desk |
| Project description * | English paragraph below, including actual human team and prior-work disclosure |
| Project or GitHub URL | https://github.com/misakamikotoghr-5205/patch-review-desk |
| Public Clips recording URL * | https://clips.agent-native.com/share/r01FTO1ytVvm — saved actual fixture/model-off clip; verification scope below |
| Slides URL | Optional; no slide link is claimed |
| Required agreement / processingConsent | Checked after the owner confirmed this final submission; covers rules, member authorization and personal-data processing |
| Marketing offers | Optional and unchecked |

## Exact submitted English project description

Patch Review Desk gives an agent a narrow job: propose replacement text in a private workspace while a reviewer decides which individual diff hunks may be applied. Shared actions actually import @agent-native/core@0.223.0 and use defineAction() for schema validation, authorization and tool metadata. The agent capability can inspect and propose, but cannot approve, apply or roll back. Approval binds server-generated hunks to baseline content; observed drift revokes approval. Partial application creates a durable SQLite receipt with the exact backup, and rollback refuses to overwrite later edits.

This is a working local Node.js 24+ app with its own HTTP transport and SQLite persistence, rather than Agent-Native's full hosted runtime. The linked 2:04 silent screen recording shows review of a two-hunk fixture proposal prepared through the separate agent capability before capture: approve only the time change, apply 09:00 to 09:30 while leaving the unapproved final sentence unchanged, then roll back to the original text and retain both receipts. The text generator in this recording is deterministic and explicitly labelled Fixture demo / model off. Fourteen local behavior tests and an isolated interactive UI exercise cover the permission and recovery workflow. No cloud deployment or external project access is claimed.

A separate November 6 production modelDraft() probe genuinely called local Ollama on the complete fictional fixture. The original qwen2.5:0.5b request timed out at 45 seconds; a bounded same-base-model alias returned text in 19.261 seconds. It passed the text contract and preserved 09:00 but missed the requested two-line format and heading. Both outcomes and raw text are in docs/evidence/local-model-20261106.json. That probe did not run the proposal, approval or UI workflow and did not generate the two fixture edits in this recording.

Human team: the individual entrant identified in this form; no other human teammate is claimed. Codex assisted design, implementation, tests and documentation. Original app work was created November 5, 2026, during this hackathon. Original application code and fictional fixtures are MIT. Dependencies: Agent-Native 0.223.0 (MIT), diff 9.0.0 (BSD-3-Clause), Zod 4.4.3 (MIT); original notices are retained. Prior libraries and design comparisons are disclosed in the repository. No claim of worldwide novelty or general editing success is made.

## 中文标题与摘要

标题：**Patch Review Desk · 逐段确认的文件草稿桌**

智能体只提交私有工作区内的文本草稿，用户逐个差异段批准或撤销。所有角色调用真正的 Agent-Native 动作定义；智能体没有批准、写入或回滚权限。批准绑定文件基线，观测到基线变化后失效；部分应用保存精确备份与持久化回执，后续文件被改动时拒绝破坏性回滚。当前为本地 Node.js 应用；录屏中的两处示例修改是明确标注的固定规则，不冒充模型推理。

## Technology, difference and process

- Built with: Node.js 24 built-in SQLite, JavaScript ES modules, local HTTP/HTML/CSS, Agent-Native action layer, jsdiff, Zod; optional Ollama `/api/chat` adapter.
- Specific difference: shared, permission-separated agent/UI actions plus per-hunk decisions, stale-baseline revocation and recoverable receipts in a small text-only workspace. It lacks a full editor, Git worktree/merge operations, cloud identity and multi-process filesystem locking.
- Build process: define capability boundary → wire actual framework actions → calculate server-owned diffs → add approval/revision checks and receipt recovery → exercise HTTP/permission and crash-edge tests → build a runnable source distribution. Real local-model probes preserve an original timeout and a valid text response that missed the full editing goal. The saved recording is a separate completed deterministic-fixture review/apply/rollback sequence; it does not show an LLM-driven sequence.
- Original source/fixture: MIT. Real dependencies: Agent-Native 0.223.0 MIT, diff 9.0.0 BSD-3-Clause, Zod 4.4.3 MIT; original notices retained. VS Code was a design comparison, with no copied code/assets. Dependency graph retains its own notices; the application MIT license does not relicense dependencies.
- Status: actual saved Clips fixture recording, runnable local fixture and real framework integration; the separate model probe has disclosed limitations. The entry was submitted after the owner’s current confirmation and the official success page acknowledged receipt. Marketing remained unchecked. No hosted app, judging acceptance, general editing success or completed LLM/UI workflow is asserted.

## Actual recording and verification scope

- Saved clip: [Fixture ModelOff](https://clips.agent-native.com/share/r01FTO1ytVvm); metadata duration 124,936 ms, 1280×720, hasAudio=false, hasCamera=false, status=ready, agentReadiness=ready.
- Clips login and Builder Free storage activation completed after the owner's current consent; capture was restricted to the fictional project tab with camera and microphone off.
- Anonymous no-Cookie GET of share and context returned HTTP 200. Four official media frames returned HTTP 200 and showed only fictional project UI.
- In the logged-in browser, playback naturally reached its player duration/currentTime of 124.794 seconds without seeking: ended=true, paused=true, readyState=4, error=null. This is not a claim of full anonymous-browser playback.
- The proposal's two fixture hunks were prepared through the separate agent capability before capture. The video shows reviewer approval of only the first hunk, partial application, the unchanged unapproved final sentence, rollback and both receipts; it does not display LLM reasoning.

## Official submission receipt

Recorded at **2026-11-06 07:53:18 UTC**. All Builder fields, including the actual Clips URL and the exact description above, were submitted after the owner's current confirmation. Required **processingConsent was checked**; optional **marketing remained unchecked**. Submit was clicked, and the official [submission page](https://www.builder.io/hackathon/submit) displayed:

> Thank you for submitting.
>
> Your project submission has been received.

**private success-page evidence held**. The webpage showed no receipt number; no confirmation email is claimed. This confirms project receipt, not judging, shortlisting or a prize. The portfolio records **one final project submission (Builder)**, **one separate event signup (Apart only)** and **two skipped directions**. Apart still requires actual sprint-period research and its final report/submission.
