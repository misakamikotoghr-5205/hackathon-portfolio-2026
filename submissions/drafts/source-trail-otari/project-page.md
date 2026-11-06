# Source Trail — source-aligned notes with visible gate failures

**One-line proposal:** Investigate the trade-off between exact citation checks, human-annotation disagreement holds, and unnecessary withholding in a small reproducible note workflow.

Source Trail is an existing private CLI/JSON tool that releases only verbatim source spans with Unicode offsets. A model may optionally choose reviewed anchor IDs; deterministic code checks the entire packet and holds claims when user-assigned position labels differ on a topic. Exact spans establish text alignment, not truth, entailment, completeness or source reliability.

All current project code and the sixteen-case pilot were created on **November 5, 2026**, before the November 13–15 Apart sprint. The pilot compares a deliberately weak quote-string baseline, whole-packet exact-span validation and the full annotation gate on fixed selections. The full gate misses two of five author-intended reviews when labels are wrong/missing, and withholds two of seven otherwise eligible selections. These are synthetic mechanism results, not LLM or semantic-truth measurements.

For the sprint, we propose new, versioned cases and an annotation-perturbation study after freezing a prospective protocol. No new sprint-period experiment, participant, finding, report or official submission is claimed yet. Track 2 is the proposed primary fit; Track 3 is secondary, subject to the organizer/entrant's actual choice.

Code/MIT/pilot: https://github.com/misakamikotoghr-5205/source-trail-otari

Otari is an optional adapter, not an Apart requirement. No real hosted inference occurred in the current pilot.
