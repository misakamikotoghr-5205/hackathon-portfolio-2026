import fs from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { Presentation, PresentationFile, FileBlob } from '@oai/artifact-tool';

const runtimeRoot = process.env.CODEX_ARTIFACT_RUNTIME || path.join(os.homedir(), '.cache/codex-runtimes/codex-primary-runtime');
process.env.RUNTIME_NODE_MODULES ||= path.join(runtimeRoot, 'dependencies/node/node_modules');
process.env.RUNTIME_NODE ||= path.join(runtimeRoot, 'dependencies/node/bin/node');

// Uses the provisioned Codex artifact-tool runtime; no Python PPTX authoring.
const here = path.dirname(fileURLToPath(import.meta.url));
const workspaceDir = path.resolve(here, '../../../../..');
const privateRoot = path.join(workspaceDir, '.private');
const author = (process.env.PRESENTATION_AUTHOR || '').trim();
const buildDir = path.resolve(process.env.PRESENTATION_BUILD_DIR || here);
const finalPath = path.resolve(process.argv[2] || path.join(workspaceDir, 'portfolio/submissions/artifacts/watt-window-next-horizon-draft.pptx'));
const inside = (parent, child) => {
  const relative = path.relative(parent, child);
  return relative !== '' && relative !== '..' && !relative.startsWith('..' + path.sep) && !path.isAbsolute(relative);
};
if (author.length > 80 || /[\x00-\x1F\x7F]/u.test(author)) throw new Error('Author display value must be a short, single-line name.');
if (author && (!inside(privateRoot, buildDir) || !inside(privateRoot, finalPath))) {
  throw new Error('Personalized author output and build/QA artifacts must remain inside the private workspace directory.');
}
await fs.mkdir(buildDir, { recursive: true, mode: 0o700 });
const skillDir = process.env.PRESENTATIONS_SKILL_DIR || path.join(os.homedir(), '.codex/plugins/cache/openai-primary-runtime/presentations/26.1103.10131/skills/presentations');
const runtimePython = path.join(runtimeRoot, 'dependencies/python/bin/python3');
const { finalizePresentation, applyPresentationChartFont } = await import(pathToFileURL(path.join(skillDir, 'container_tools/artifact_tool_utils.mjs')));
const results = JSON.parse(await fs.readFile(path.join(here, 'model-results.json'), 'utf8'));
const household = results.household;
const baseCost = Number(household.baseline.estimated_cost.decimal);
const planCost = Number(household.proposed.estimated_cost.decimal);
const delta = Number(household.estimated_cost_delta_from_baseline.decimal);
if (baseCost !== 3.95875 || planCost !== 2.32625 || delta !== 1.6325) throw new Error('Unexpected example result; review slide evidence.');
const font = 'Liberation Sans'; // Verified with local fontconfig before authoring.
const c = { bg: '#F5F4EB', ink: '#202C29', muted: '#53615B', green: '#477451', line: '#C7CEC1', light: '#E3E8DD', white: '#FFFFFF' };
const deck = Presentation.create({ slideSize: { width: 1280, height: 720 } });
const official = 'https://eisociety.org/hackathon.php?slug=next-horizon-2026';
const repo = 'https://github.com/davidusb-geek/emhass/blob/2306a87445e939bbc3350240d9467af4dd108751/README.md';
const flex = 'https://github.com/FlexMeasures/flexmeasures/blob/8a1f5087496d82794bb262ecdb7ba6eec280a03f/README.md';
function text(slide, name, value, x, y, w, h, size = 26, opts = {}) {
  const shape = slide.shapes.add({ name, geometry: 'textbox', position: { left: x, top: y, width: w, height: h }, fill: 'none', line: { fill: 'none', width: 0 } });
  shape.text = value;
  shape.text.style = { typeface: font, fontSize: size, color: c.ink, verticalAlignment: 'top', ...opts };
  return shape;
}
function rule(slide, y, x = 64, w = 1152) {
  slide.shapes.add({ name: `rule-${y}`, geometry: 'rect', position: { left: x, top: y, width: w, height: 1.4 }, fill: c.line, line: { fill: 'none', width: 0 } });
}
function page(title, number, kicker = 'WATT WINDOW / NEXT HORIZON 2026') {
  const s = deck.slides.add();
  s.background.fill = c.bg;
  text(s, 'section', kicker, 64, 36, 1100, 26, 17, { color: c.green, bold: true });
  text(s, 'slide-title', title, 64, 82, 1152, 66, 43, { bold: true });
  rule(s, 159);
  rule(s, 656);
  text(s, 'disclosure-footer', 'Pre-event prototype · Application draft · 6 November 2026', 64, 671, 1060, 25, 16, { color: c.muted });
  text(s, 'folio', String(number), 1164, 670, 52, 26, 17, { color: c.muted, alignment: 'right' });
  return s;
}
function table(slide, name, values, x, y, widths, height, size = 23) {
  const t = slide.tables.add({ name, rows: values.length, columns: values[0].length, left: x, top: y, width: widths.reduce((a,b)=>a+b,0), height, columnWidths: widths, values });
  t.styleOptions = { headerRow: false, bandedRows: false };
  t.borders.assign({ style: 'solid', fill: c.line, width: 1 });
  for (let row=0; row<values.length; row++) {
    for (let col=0; col<values[0].length; col++) {
      const cell = t.getCell(row, col);
      cell.fill = row === 0 ? c.ink : c.bg;
      cell.text.style = { typeface: font, fontSize: size, color: row === 0 ? c.white : c.ink, bold: row === 0 };
    }
  }
  t.cells.block({ row: 0, column: 0, rowCount: values.length, columnCount: values[0].length }).assign({ margins: { left: 14, right: 14, top: 12, bottom: 12 }, anchor: 'center' });
  return t;
}

// 1 — Problem. The cover does not imply completed event participation.
{
  const s = page('Watt Window', 1, 'NEXT HORIZON 2026 / SMART CITIES & SUSTAINABLE DEVELOPMENT');
  text(s, 'subtitle', 'Advisory scheduling for noncritical loads', 64, 191, 1130, 58, 33, { color: c.green });
  text(s, 'problem', 'A cheap time slot can conflict with another load or a deadline.', 64, 289, 1060, 148, 49, { bold: true });
  text(s, 'intent', 'Help a household or small shop compare an entered schedule with a lower-cost plan that respects an explicit capacity model.', 64, 485, 1085, 96, 28);
  s.speakerNotes.text = `Application draft, not an assertion of registration, shortlisting or work completed during the future event. This is a pre-event local software prototype. No device commands, measured savings or carbon benefit.\nOfficial event rules, checked 6 November 2026: ${official}\nLocal source: projects/watt-window/docs/pitch-outline.md and README.md.`;
}
// 2 — Method and model boundary.
{
  const s = page('Make the assumptions inspectable', 2);
  text(s, 'input-label', 'ENTERED INPUTS', 64, 194, 510, 30, 20, { color: c.green, bold: true });
  text(s, 'inputs', 'Tariff per time slot\nEstimated energy and concurrent power\nTime windows, duration and fixed starts\nBackground load and capacity', 64, 240, 520, 220, 28);
  text(s, 'method-label', 'BOUNDED SEARCH', 670, 194, 545, 30, 20, { color: c.green, bold: true });
  text(s, 'method', 'Contiguous jobs on a finite grid\nExact rational cost comparison\nBranch-and-bound with a node budget\nIndependent check of each returned plan', 670, 240, 545, 220, 28);
  rule(s, 490);
  text(s, 'proof', 'The result says what was proven', 64, 516, 1130, 38, 28, { bold: true });
  text(s, 'statuses', 'Optimal in this model · Feasible, not proven optimal · No plan within budget · Proven infeasible', 64, 566, 1145, 64, 24, { color: c.muted });
  s.speakerNotes.text = 'Local sources: projects/watt-window/docs/model.md; watt_window/core.py. Supported bounds: 1–48 slots at 15/30/60 minutes, 1–12 jobs, explicit noncritical confirmation. Estimated job energy is uniformly spread across its active slots. Only a completed search or a valid witness proves infeasibility. Output JSON/HTML/CSV/ICS is for manual review/import, without device or calendar API calls. Entered capacity is not electrical safety validation.';
}
// 3 — Actual local result, fictional underlying model. Native chart with literal workbook.
{
  const s = page('A lower estimated bill, under fictional inputs', 3);
  text(s, 'chart-unit', 'Six-hour household example · CNY, including background load', 64, 187, 1150, 32, 23, { color: c.muted });
  const chart = s.charts.add('bar', {
    name: 'household-estimated-cost',
    position: { left: 64, top: 238, width: 700, height: 307 },
    title: 'Estimated total cost (CNY)',
    titleTextStyle: { fontSize: 23, fill: c.ink, typeface: font },
    categories: ['Original schedule', 'Proposed schedule'],
    series: [{ name: 'Estimated cost (CNY)', values: [baseCost, planCost], fill: c.green, points: [{ idx: 0, fill: '#9FAE9A' }, { idx: 1, fill: c.green }] }],
    barOptions: { direction: 'column', grouping: 'clustered', gapWidth: 115 },
    hasLegend: false,
    xAxis: { textStyle: { fontSize: 21, fill: c.ink }, line: { style: 'solid', fill: c.line, width: 1 }, majorGridlines: null },
    yAxis: { min: 0, max: 5, majorUnit: 1, numberFormatCode: '0.0', textStyle: { fontSize: 18, fill: c.muted }, majorGridlines: { style: 'solid', fill: c.line, width: 1 } },
    dataLabels: { showValue: true, position: 'outEnd', numberFormatCode: '0.00000', textStyle: { fontSize: 22, bold: true, fill: c.ink } },
    chartFill: 'none', chartLine: { fill: 'none', width: 0 }, plotAreaFill: 'none', plotAreaLine: { fill: 'none', width: 0 }
  });
  applyPresentationChartFont(chart, { fontFamily: font });
  text(s, 'delta', `${delta.toFixed(5)} CNY`, 824, 255, 380, 64, 43, { bold: true, color: c.green });
  text(s, 'delta-label', 'Estimated model cost difference', 824, 329, 380, 70, 25);
  text(s, 'parameters', '12 × 30-minute slots\n3 noncritical jobs\n2,600 W entered capacity\n350 W background load', 824, 413, 380, 131, 23, { color: c.muted });
  text(s, 'pilot-caveat', 'Fictional tariffs and load estimates; no field trial. Estimated energy is unchanged (4.3 kWh). Proposed peak rises from 1,850 W to 2,250 W, within the entered limit.', 64, 576, 1145, 65, 23, { color: c.muted });
  s.speakerNotes.text = `Source: actual local solve of projects/watt-window/examples/household.json on 6 November 2026. Reproducible snapshot: model-results.json beside build.mjs. Original total ${household.baseline.estimated_cost.decimal}; proposed total ${household.proposed.estimated_cost.decimal}; baseline minus proposed ${household.estimated_cost_delta_from_baseline.decimal} CNY. Includes 2.1 kWh background plus 2.2 kWh jobs. Optimal in the entered finite model; 16 search nodes. Both schedules validate against the supplied model. This is not a measured bill, reduced energy consumption or carbon result. Fictional input schedule date 28 November is not evidence of work performed on that date. Chart data is an editable literal-data workbook snapshot, not a live data connection.`;
}
// 4 — Honest comparison. No claims about unique invention.
{
  const s = page('A narrow, reproducible advisory prototype', 4);
  table(s, 'landscape-comparison', [
    ['Project / license', 'Established capability', 'Scope of this prototype'],
    ['EMHASS / MIT', 'Residential optimization, solar, storage and Home Assistant', 'Offline, manually entered noncritical jobs; no device integration'],
    ['FlexMeasures / Apache-2.0', 'Multi-asset scheduling, time series, forecasts and API/UI', 'Small finite-grid model with standard-library Python'],
    ['Watt Window / MIT', 'Independent implementation; no upstream code copied', 'Proof status, baseline checks and inspectable exports']
  ], 64, 194, [275, 430, 447], 291, 22);
  text(s, 'evidence-title', 'Evidence available now', 64, 520, 1120, 34, 27, { bold: true });
  text(s, 'evidence', '17 automated tests, including an independent brute-force oracle. An overload witness rejects 4,800 watt-slots of demand against 3,300 available. A one-node run reports an unproven feasible plan.', 64, 568, 1145, 71, 24);
  s.speakerNotes.text = `Design comparisons, not a claim that upstream systems lack equivalent features. Existing energy scheduling is established and both systems are more mature. README and full license reviewed at pinned commits; no upstream code, fixtures or assets copied.\nEMHASS README ${repo}\nEMHASS MIT license https://github.com/davidusb-geek/emhass/blob/2306a87445e939bbc3350240d9467af4dd108751/LICENSE\nFlexMeasures README ${flex}\nFlexMeasures Apache-2.0 license https://github.com/FlexMeasures/flexmeasures/blob/8a1f5087496d82794bb262ecdb7ba6eec280a03f/LICENSE\nLocal sources: docs/landscape.md, landscape-sources.json, actual model-results.json infeasible and household_one_node entries. Witness numbers are sums over two slots, not watts or energy. 17 tests reproduced with scripts/verify.py.`;
}
// 5 — Entirely prospective event work.
{
  const s = page('A proposed 48-hour build and evaluation', 5);
  table(s, 'event-plan', [
    ['Time in event', 'Planned work', 'Reviewable deliverable'],
    ['0–8 hours', 'Validate scope and new assumptions', 'Dated input protocol and test cases'],
    ['8–24 hours', 'Evaluate new constraint / failure cases', 'Reproducible runs and oracle comparisons'],
    ['24–40 hours', 'Improve explanations and manual review', 'Usability findings and revised exports'],
    ['40–48 hours', 'Re-run checks and prepare final pitch', 'Versioned delta, limitations and demo']
  ], 64, 194, [220, 467, 465], 390, 23);
  text(s, 'event-dates', 'If shortlisted: 28 November 09:00 EST → 30 November 09:00 EST', 64, 610, 1150, 36, 25, { bold: true });
  s.speakerNotes.text = `Future work, conditional on selection and organizer confirmation of the pre-event baseline. Existing code/examples and this 6 November deck are pre-event material, not 48-hour deliverables. Keep a separate dated change log for work actually performed during the event. Official schedule: ${official}. Final event pitch is 10 minutes plus 5 minutes Q&A. No promised measured energy benefit; any real-world data collection would need truthful provenance and participant permission.`;
}
// 6 — Public placeholder by default; optional private author display.
{
  const s = page('Team and first-stage readiness', 6);
  text(s, 'team-label', 'TEAM', 64, 198, 500, 30, 20, { color: c.green, bold: true });
  text(s, 'team', 'Solo project', 64, 252, 500, 64, 42, { bold: true });
  text(s, 'identity', author || 'Author details pending confirmation', 64, 340, 460, author ? 44 : 100, 30, { color: c.muted });
  if (author) text(s, 'author-role', 'Independent developer', 64, 396, 500, 43, 27, { color: c.muted });
  text(s, 'ready-label', 'PREPARED FOR REVIEW', 650, 198, 565, 30, 20, { color: c.green, bold: true });
  text(s, 'ready', 'Working offline prototype and examples\nMIT-licensed original code\nReproducible model results and tests\nEditable first-stage presentation draft', 650, 250, 565, 196, 27);
  rule(s, 490);
  text(s, 'remaining', 'Before submission', 64, 518, 1110, 34, 27, { bold: true });
  text(s, 'remaining-detail', 'Confirm author and eligibility details, review the pre-event baseline with the organizer, and complete the official application. Registration and shortlisting are not yet claimed.', 64, 566, 1145, 74, 25, { color: c.muted });
  s.speakerNotes.text = `${author ? 'Identity limited to the supplied author display name and Independent developer. No contact details are included.' : 'Identity intentionally limited to Solo project + Author details pending confirmation.'} Do not infer nationality, contact, age, education or affiliation. First-stage idea submission deadline 15 November 2026; the official page does not publish a precise cutoff time or timezone for that date. It requests a PowerPoint up to 15 MB and optionally a 2–4 minute existing-prototype video. Submit the PPTX, not the review PDF, through the official application only after confirming actual author details and any required terms. ${official}`;
}

await fs.mkdir(path.join(buildDir, 'rendered'), { recursive: true });
const candidatePath = path.join(buildDir, 'candidate.pptx');
await (await PresentationFile.exportPptx(deck)).save(candidatePath);
await fs.mkdir(path.dirname(finalPath), { recursive: true });
const validation = await finalizePresentation({
  workspaceDir: author ? privateRoot : workspaceDir, candidatePath, finalPath,
  pythonExecutable: runtimePython,
  integrityValidatorPath: path.join(skillDir, 'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath: path.join(skillDir, 'container_tools/inspect_presentation_layout_geometry.py'),
  explicitTotalSlideCount: 6,
  requiredNativeTableOwnerSlides: [4,5],
  requiredNativeChartOwnerSlides: [3],
  materializeLiteralChartWorkbooks: true,
  fontPolicy: { basis: 'design', families: [font] },
  layoutArgs: ['--expected-slide-size-emu', '12192000,6858000', '--validate-heading-fit', '--validate-bullet-geometry', '--require-native-table-slide', '4', '--require-native-table-slide', '5'],
  verifyArtifactToolImport: true,
  receiptPath: path.join(buildDir, path.basename(finalPath) + '.validation.json')
});
// Re-import the final bytes to inspect the deliverable, not only the authoring model.
const finalDeck = await PresentationFile.importPptx(await FileBlob.load(finalPath));
for (let i=0; i<6; i++) {
  const preview = await finalDeck.export({ slide: finalDeck.slides.items[i], format: 'png', scale: 1 });
  await fs.writeFile(path.join(buildDir, 'rendered', `slide-${i+1}.png`), new Uint8Array(await preview.arrayBuffer()));
}
// The provisioned PDF adapter lacks standard-font metric modules. Use the
// already inspected final-slide rasters for the auxiliary review-only PDF.
execFileSync(runtimePython, [path.join(here, 'review-pdf.py'), finalPath.replace(/\.pptx$/, '.pdf')], { stdio: 'inherit', env: { ...process.env, PRESENTATION_BUILD_DIR: buildDir } });
await fs.writeFile(path.join(buildDir, 'authoring-model.json'), JSON.stringify(deck.toProto(), null, 2));
console.log(JSON.stringify({ finalPath, bytes: (await fs.stat(finalPath)).size, validation }, null, 2));
