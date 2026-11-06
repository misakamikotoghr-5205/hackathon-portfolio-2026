import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { PresentationFile, FileBlob } from '@oai/artifact-tool';
const here = path.dirname(fileURLToPath(import.meta.url));
const finalPath = path.resolve(here, '../../../artifacts/watt-window-next-horizon-draft.pptx');
const deck = await PresentationFile.importPptx(await FileBlob.load(finalPath));
console.log('Slides loaded:', deck.slides.items.length);
for (let i = 0; i < deck.slides.items.length; i++) {
  const png = await deck.export({ slide: deck.slides.items[i], format: 'png', scale: 1 });
  await fs.writeFile(path.join(here, 'rendered', `slide-${i+1}.png`), new Uint8Array(await png.arrayBuffer()));
  console.log('Rendered:', i + 1);
}
console.log('Final slide rasters exported; run review-pdf.py for the review-only PDF.');
