# Watt Window: Next Horizon first-stage PPT draft

Prepared 6 November 2026. This is a **pre-event prototype/application draft**, not work completed during the future 28–30 November event and not evidence of registration or shortlisting. The author details remain pending confirmation. The official first-stage deliverable is a PowerPoint file up to 15 MB; the PDF is only a review copy.

## Six-slide narrative

1. **Problem:** A cheap slot can conflict with another load or a deadline. Introduce a small offline advisory scheduler for explicitly confirmed noncritical jobs.
2. **Method:** Enter tariffs, power/energy assumptions, windows and capacity. Search a finite model with exact rational costs and bounded branch-and-bound. Preserve the distinction between a proven optimum, an unproven feasible plan, budget exhaustion and proven infeasibility.
3. **Model result:** Actual local execution of the fictional household example gives estimated total costs 3.958750 CNY (original) and 2.326250 CNY (proposed), a 1.632500 CNY modeled difference. Background cost is included. Estimated energy stays 4.3 kWh. Peak rises from 1,850 W to 2,250 W inside the entered 2,600 W limit. No field trial, actual bill saving or carbon reduction is claimed.
4. **Originality and evidence:** Energy scheduling already exists. Compare EMHASS/MIT and FlexMeasures/Apache-2.0 honestly; this independently implemented prototype narrows scope to inspectable local artifacts. Seventeen tests include an independent brute-force oracle. The infeasible example has a 4,800 versus 3,300 watt-slot witness; a one-node run remains labeled unproven.
5. **Future 48-hour plan:** If shortlisted and permitted to extend the declared pre-event baseline, create new cases, evaluate failures, improve explanations and record the dated work delta. All these tasks are prospective.
6. **Team/readiness:** “Solo project” and “Author details pending confirmation” only. Confirm actual identity/eligibility, organizer treatment of the pre-event baseline, and the official application before submitting.

## Source and claim boundary

- Official rules, checked 6 November 2026: <https://eisociety.org/hackathon.php?slug=next-horizon-2026>. Initial idea deadline is 15 November; no precise first-stage clock/timezone cutoff is published on this page. The event is 28 November 09:00 EST to 30 November 09:00 EST. An optional existing-prototype video may be 2–4 minutes.
- Project source: `projects/watt-window/docs/pitch-outline.md`, `docs/model.md`, `docs/landscape.md`, `docs/landscape-sources.json` and the fictional example JSON files.
- Actual presentation evidence: `pptx-build/model-results.json`, generated directly by the project solver; `prepare-results.py` records how.
- The input schedule timestamp 28 November is fictional model data, not a future research or deployment claim.
- Entered power/capacity is a scheduling model, not an electrical safety assessment. No appliance is controlled. No real tariff, user, affiliation or pilot installation is invented.
- The table compares pinned upstream README/license sources, with full links in speaker notes. No upstream code was copied into Watt Window or the deck.
- Deck text, chart, tables and the build script were produced with AI assistance and reviewed against actual local outputs. No hidden gameplay/model inference is represented.

## Rebuild

Requires the provisioned `@oai/artifact-tool` Node runtime and the immutable Presentations skill validators. Make `@oai/artifact-tool` resolvable in `pptx-build/` (this session uses an ignored node_modules symlink to the provisioned runtime); the builder sets the provisioned runtime paths for validator subprocesses. This intentionally uses artifact-tool, not `python-pptx`.

```sh
python3 portfolio/submissions/drafts/watt-window/pptx-build/prepare-results.py
python3 projects/watt-window/scripts/verify.py
# Run with the provisioned Node binary and node_modules resolution.
node portfolio/submissions/drafts/watt-window/pptx-build/build.mjs /absolute/path/in/workspace/new-output-name.pptx
```

The build refuses to overwrite a finalized output; use a new file in a separate output directory for revisions (for example, `portfolio/submissions/artifacts/`). The output directory must not contain the private build/validation-receipt directory. It exports a separate candidate, runs package/layout/font/native-table/native-chart and first-party reimport checks, renders all six final slides and writes a raster PDF companion from those inspected final renders. The provisioned direct PDF adapter lacked standard-font metric modules, so the auxiliary PDF uses ReportLab without altering the PPTX. The chart contains an editable literal-data workbook snapshot of the two actual solver outputs, not a live connection or formula model. Text, both tables and chart remain native editable objects.

Local font: Liberation Sans, verified available via fontconfig. Canvas: 1280×720, 16:9. No external images, third-party decoration or fabricated screenshots. Final checks and per-slide preview images are under `pptx-build/`.

Author details are deliberately unresolved for review; they must be filled with the user's verified details before filing. No application, account registration, terms acceptance or external publication is performed by this build.
