# Prospective research plan — prepared 2026-11-06, not executed sprint research

## Official template and boundary

[Official template linked by the event's Guidelines](https://docs.google.com/document/d/17b3JWki-ZkaqdmqGI5d0gof-HwlGuWU9Mc1_klNZXKs/copy?usp=sharing). The copy action currently requires Google login; no copy/export was made. Use the template current on the [event page](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15) rather than guessing its formatting.

The required deliverable is a research PDF, not a repository/demo alone: ≤8 body pages excluding references/appendices; 150–250-word abstract; real authors and affiliations; mandatory **Limitations and Dual-Use / Ethical Considerations** appendix. The project form limits the PDF upload to25MB. A 3–5 minute video and public code are optional. Current public submit is disabled; signup and report submission are different steps.

## Preexisting material — disclose verbatim in the future report

> Source Trail's core implementation, sixteen synthetic pilot cases, pilot protocol, runner and published pilot outputs were created on November 5, 2026 before the sprint. They are exploratory preparation and are not counted as new work conducted during November 13–15. The pilot uses no model or human participants and does not measure semantic truth.

Observed existing pilot (invalid selected citation release; required-review miss; eligible selection withholding): quote-only **4/4;5/5;0/7**, exact-span **0/4;5/5;1/7**, full-gate **0/4;2/5;2/7**. Keep these as preexisting results with their existing hashes. Do not rename them as new/held-out outcomes.

## Proposed question and new work

**Question:** For new authored tasks, how do whole-packet citation validation and disagreement-label gates behave when annotation coverage and correctness change, and which uncontested selections are unnecessarily withheld?

Proposed primary Track2, optional Track3; not a model benchmark. The entrant must actually undertake and log new work during the sprint. Suggested bounded design:

1. Before new scoring, freeze a dated protocol and commit/hash. Declare case-level primary metrics, eligible subsets, input-reject vs review-hold decisions, stopping rule, all planned perturbations and exclusions. This draft is not an independently registered preregistration.
2. During the sprint, create/version **24 new fictional source packets**, separate from the sixteen pilot cases. Keep a separate author expectation for selected-span fidelity and whether manual review is intended. Where another real reviewer participates, record their actual role/consent and report disagreements; otherwise state single-author expectations and do not claim independent adjudication.
3. Include clean/repaired controls, moved/missing citations, opposed annotated statements omitted by selection, absent opposing annotations, wrong same labels, compatible text with wrong differing labels and an unrelated/invalid unselected anchor. Balance variants before seeing aggregate results; do not tune expectations to make a gate win.
4. Execute fixed selections on the same three policy definitions. Both stronger policies validate the entire packet; only the full-gate disagreement rule differs. Keep the oracle outside policy execution. Record every input, raw decision, released text, failure class and source/protocol/code hash.
5. Publish n/N and per-case data. Distinguish invalid-citation releases, author-intended review misses and eligible-selection withholding; also raw input rejection and annotation hold counts. Use N/A for zero denominator. Do not add subsets into one accuracy score or call deterministic reruns independent trials.
6. Compare failure strata, discuss whole-packet conservatism and annotation dependencies, and write only conclusions supported by the new data actually obtained. Negative results remain in the report.

## Actual sprint log — leave blank until performed

| Actual date/time and timezone | Commit/data version | What actually changed or ran | Output hash / evidence |
| --- | --- | --- | --- |
| [NOT YET PERFORMED] | | | |

No mock future results or participants are supplied. If the study is unfinished, report that honestly; the official FAQ accepts unfinished work, with evaluation of actual accomplishment.

## Report outline

1. Problem and bounded contribution, including preexisting-work box.
2. Related work with real primary references and accurate licenses/provenance.
3. New protocol, data construction and policy ablation.
4. Actual new results only; separate table for the preexisting pilot if useful.
5. Discussion: interpretation, failure cases, limits and next steps.
6. References.
7. Required limitations/dual-use appendix: exact-looking excerpts can launder misleading context; users can omit/relabel sources; hashes are not signatures; synthetic expectations are fallible; no real personal data or participants used unless actually documented and authorized.

Deadline: Nov15 23:59 AoE = Nov16 11:59 UTC / Beijing19:59. Signup/terms, actual study, final PDF, any optional media and the official submission receipt remain undone.
