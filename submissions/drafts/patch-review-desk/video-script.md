# Builder: actual Clips fixture recording

Recorded and saved on 2026-11-06: [Fixture ModelOff](https://clips.agent-native.com/share/r01FTO1ytVvm). Metadata: **124,936 ms**, **1280×720**, **hasAudio=false**, **hasCamera=false**, **status=ready**, **agentReadiness=ready**. This is an actual silent recording, not an unrecorded script. It demonstrates a deterministic fixture and explicitly displays model off.

## Capture scope and actual sequence

The owner confirmed this Builder Free activation and recording action. Free storage was activated and the real recorder was reached after Clips login. Capture was limited to the fictional project tab; camera and microphone were off. No private role-token entry, email sign-in, personal data or unrelated desktop content is presented as part of this clip.

| Stage | Actual content / boundary |
|---|---|
| Before capture — not shown as live generation | The separate agent capability prepared a two-hunk deterministic fixture proposal before the human/reviewer page loaded for recording. This is not an LLM response. |
| Reviewer loads the desk | Show the fictional original document and the proposal's two hunks with the fixture/model-off label. |
| Per-hunk approval | Approve only the first hunk, the time change; leave the final-sentence hunk unapproved. |
| Partial application | Apply 09:00 → 09:30 while the unapproved final sentence remains unchanged; retain the apply receipt. |
| Rollback | Restore the original text and retain both apply and rollback receipts. |

Do not describe this clip as showing proposal generation during capture, live LLM reasoning, a model-approved change or Agent-Native's full hosted runtime. Agent-Native action definitions and the role boundary are supported by the repository; no code-editor segment is claimed as appearing in the recording.

## Playback and public-access verification

- Anonymous no-Cookie GET of the public share and context returned **HTTP 200**.
- **Four official media frames** returned **HTTP 200** and contained only fictional project UI.
- In the **logged-in browser**, without seeking, playback naturally reached **currentTime=duration=124.794 seconds**, **ended=true**, **paused=true**, **readyState=4**, **error=null**.
- The 124,936-ms value is the saved recording metadata; the 124.794-second value is the observed player duration. Keep these observations distinct.
- These checks do **not** claim full playback in an anonymous browser. Public HTTP/media-frame checks and authenticated full playback are separate evidence.

## Separate real-model probe

`projects/patch-review-desk/docs/evidence/local-model-20261106.json` records two genuine production `modelDraft()` requests with the complete fictional fixture and the same goal: original model 45-second timeout, bounded same-base-model alias 19.261-second text response. The latter passed the text-only contract and kept 09:00 but failed the requested two-line format/heading. That probe did not run proposal, approval or UI actions and did not produce the two edits in this clip. The saved fixture recording does not convert that probe into a completed LLM editing workflow.

## Form state after recording

All Builder fields, including this actual Clips URL, are prefilled. Read-only DOM checking found the other inputs nativeValid; the only missing required input is **processingConsent**, still unchecked. Optional marketing is also unchecked. **Submit has not been clicked**; current event-rules and individual-eligibility confirmation are pending. No Builder final-submission receipt is claimed. The portfolio still records one confirmed event signup (Apart), zero final project submissions and two skipped directions.
