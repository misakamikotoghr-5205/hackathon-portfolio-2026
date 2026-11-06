# Builder: shortest honest Clips recording

Target 2–3 minutes; the rules do not publish a duration cap. The final link must be public and work without login/access requests. This is a recording plan, not an existing video. Use the actual [Clips service](https://clips.agent-native.com/); its current public page requires account sign-in. A local-development sign-in is not evidence of a remotely public clip.

## Prepare before recording

From the project root: `npm ci --ignore-scripts --omit=optional`, `npm run init`, `npm run dev`; open `http://127.0.0.1:4185`. `init` does not overwrite an existing fixture. Use only fictional content and a working baseline that still has the original two sample lines; inspect previous receipts rather than deleting a user's data. Paste the human token privately and click **Open the desk before recording**. The input clears after connection. Never record `.data/roles.json`, request headers, private receipts, unrelated desktop windows or email sign-in.

## Actual screen sequence and English narration

| Time | Action | Narration |
|---|---|---|
| 0:00–0:20 | Show title, `Fixture demo · model off`, original `welcome.md` | “An agent can draft a file change. A person should control exactly which pieces are written. This recording uses a fixed fixture, not model inference.” |
| 0:20–0:40 | Click **Draft two fixture edits**, then **Send for review** | “The server creates two diff hunks from this baseline. The sample helper only proposes text; it does not approve or write the file.” |
| 0:40–1:05 | Approve one hunk, revoke it, approve it again; leave the second unapproved | “Each decision is reversible before application. Approval is attached to this proposal revision and baseline.” |
| 1:05–1:30 | Click **Apply approved hunks**, confirm; show changed baseline and receipt | “Only the approved hunk is applied. A durable receipt retains the exact original text and content hashes.” |
| 1:30–1:55 | Click **Rollback**, confirm; show restored text and retained receipts | “Rollback restores the original only while the current file still matches the applied result. It refuses to overwrite later work.” |
| 1:55–2:25 | Show actual `actions/index.js` imports/definition and the README integration boundary | “These are actual Agent-Native `defineAction` contracts. The agent role can inspect and propose; approval, apply and rollback are human-only. The local transport and persistence are our own.” |
| 2:25–2:40 | Show public repository/README and model-off badge | “The local fixture is runnable. Real local-model probes returned one timeout and one text response that preserved the time but missed the short-format goal. Both are retained. This fixture segment is still model-off. This is a small file-review desk, not a full hosted framework deployment.” |

中文可用旁白：智能体只提草稿，用户逐段确认；只应用已批准段落；回执保留原文，回滚拒绝覆盖后续编辑；本次是固定示例，无模型推理；实际使用官方动作合同。

If any step fails, fix or disclose it and record again; do not narrate success over a screenshot. Record permission denial or stale-baseline behavior only if actually executed. A real model segment may be added only after an authorized local model has genuinely returned a proposal.

Current local-model evidence: `projects/patch-review-desk/docs/evidence/local-model-20261106.json` records two genuine production `modelDraft()` requests with the complete fictional fixture and identical goal: original model 45-second timeout, bounded same-base-model alias 19.261-second text response. The latter passed the text-only contract and kept 09:00 but failed the requested two-line format/heading. It did not run the browser, framework action, proposal or human approval sequence. Do not narrate it as completed editing or a Clips recording. A live model segment should expose the actual response and its review limitations.

After recording, open the public clip while signed out and confirm playback. Put that actual URL into the required form field, review creator/team and prior-work disclosure, then let root handle the authorized form submission and save its receipt privately. This document performs none of those external actions.
