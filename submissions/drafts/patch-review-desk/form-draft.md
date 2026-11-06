# Patch Review Desk — Builder submission draft

Prepared 2026-11-06. No registration, agreement or submission has been made by this document. Do not insert a fabricated recording URL. Account identity stays in the private form.

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
| Public Clips recording URL * | Must be the actual completed recording, viewable without login; currently absent |
| Slides URL | Optional; no slide link is claimed |
| Required agreement | Entrant/root handles only after identity and eligibility are settled; includes rules, each member's authorization and personal-data processing |
| Marketing offers | Optional; no consent is implied |

## Paste-ready English project description

Patch Review Desk gives an agent a narrow job: propose replacement text in a private workspace while a person decides which individual diff hunks may be applied. Shared actions actually import `@agent-native/core@0.223.0` and use `defineAction()` for schema validation, authorization and tool metadata. The agent capability can inspect and propose, but cannot approve, apply or roll back. Human approval binds server-generated hunks to baseline content; observed drift revokes approval. Partial application creates a durable SQLite receipt containing the exact backup, and rollback refuses to overwrite later edits.

This is a working local Node.js 24+ application with its own HTTP transport and SQLite persistence, rather than a deployment of Agent-Native's full hosted runtime. The built-in two-edit helper is explicitly deterministic; no LLM inference is claimed in that demonstration. On November 6, production `modelDraft()` genuinely called local Ollama with the complete fictional fixture. The original `qwen2.5:0.5b` request timed out at 45 seconds; a bounded same-base-model alias returned text in 19.261 seconds. It passed the text-only contract and preserved 09:00, but did not follow the requested two-line format/heading. Both outcomes and the raw accepted text are retained in `docs/evidence/local-model-20261106.json`, with a reproducible Modelfile. This probe used no role token, private workspace, proposal, approval or UI sequence. Fourteen local behavior tests cover permissions, drift, partial review, retries, interruption recovery and rollback.

Human team: the individual entrant identified in this form; no other human teammate is claimed by this draft. Codex assisted design, implementation, tests and documentation. Original application work was created November 5, 2026, during this hackathon; prior third-party libraries are disclosed below. This is not a claim that patch review or baseline hashes are novel inventions.

## 中文标题与摘要

标题：**Patch Review Desk · 逐段确认的文件草稿桌**

智能体只提交私有工作区内的文本草稿，用户逐个差异段批准或撤销。所有角色调用真正的 Agent-Native 动作定义；智能体没有批准、写入或回滚权限。批准绑定文件基线，观测到基线变化后失效；部分应用保存精确备份与持久化回执，后续文件被改动时拒绝破坏性回滚。当前为本地 Node.js 应用；录屏中的两处示例修改是明确标注的固定规则，不冒充模型推理。

## Technology, difference and process

- Built with: Node.js 24 built-in SQLite, JavaScript ES modules, local HTTP/HTML/CSS, Agent-Native action layer, jsdiff, Zod; optional Ollama `/api/chat` adapter.
- Specific difference: shared, permission-separated agent/UI actions plus per-hunk decisions, stale-baseline revocation and recoverable receipts in a small text-only workspace. It lacks a full editor, Git worktree/merge operations, cloud identity and multi-process filesystem locking.
- Build process: define capability boundary → wire actual framework actions → calculate server-owned diffs → add approval/revision checks and receipt recovery → exercise HTTP/permission and crash-edge tests → build a runnable source distribution. Subsequent real local-model probes preserve an original timeout and a valid text response that did not meet the full editing goal. No browser/model approval sequence is presented as completed.
- Original source/fixture: MIT. Real dependencies: Agent-Native 0.223.0 MIT, diff 9.0.0 BSD-3-Clause, Zod 4.4.3 MIT; original notices retained. VS Code was a design comparison, with no copied code/assets. Dependency graph retains its own notices; the application MIT license does not relicense dependencies.
- Status: runnable local fixture and actual framework integration, plus real local-model output and disclosed limitations; a public Clips recording and the entrant's submission remain. No hosted app, official acceptance, successful general editing or completed model/UI workflow is asserted.

## Minimum legitimate submission route

Record the real fixture workflow using [video-script.md](video-script.md), explicitly keeping the model-off disclosure. The official rules require a functional Agent-Native app and a public Clips demo; they do not state that an LLM provider must be used. Do not imply that this narrower action-layer integration has already been accepted by judges. A public repo/live deployment is encouraged, not required. The description can honestly submit the working fixture while explaining the optional model path; a stronger actual model demonstration is separate work, not a result to invent.
