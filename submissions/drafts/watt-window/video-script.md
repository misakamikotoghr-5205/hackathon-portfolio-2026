# Optional Next Horizon prototype video — 3 minutes

This is the optional first-stage 2–4 minute video plan, not the later 10-minute final pitch. Label all current code **pre-event prototype, created November 5** and all prices/loads **fictional estimates**.

| Time | Actual command/view | English narration |
|---|---|---|
| 0:00–0:25 | Title and entered household assumptions | “The cheapest slot is not enough when tasks compete for a limited window and power budget.” |
| 0:25–1:00 | `python3 -m watt_window solve examples/household.json --out output/video-household` | “The report evaluates the original plan and proposed cost under the same entered model. A number here is an estimate, not a measured bill saving.” |
| 1:00–1:35 | `python3 -m watt_window sensitivity examples/household.json --scenarios examples/sensitivity.json --out output/video-sensitivity` | “Each hypothetical change gets its own solve and proof status; cross-tariff differences are not causal savings.” |
| 1:35–2:10 | `python3 -m watt_window solve examples/infeasible.json --out output/video-infeasible` | “This interval has more unavoidable workload than the declared capacity. The witness explains finite-model infeasibility.” |
| 2:10–2:40 | `python3 -m watt_window solve examples/household.json --max-nodes 1 --out output/video-budget` | “A bounded search can return a valid plan without proof or no plan within budget. It must not mislabel those outcomes as optimal or impossible.” |
| 2:40–3:00 | Export files, scope and event plan | “No appliance commands are sent. If shortlisted, I will do new evaluation during the event and report it separately from this prototype.” |

Use a new output directory for every command: existing exports are intentionally preserved. Show actual JSON/HTML status, not a prewritten preferred result. No contact details, private household data or real bill is needed. No video has been recorded or uploaded by this preparation.
