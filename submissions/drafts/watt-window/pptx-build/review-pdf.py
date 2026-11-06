"""Build the review-only raster PDF from the inspected final-slide PNGs."""
from pathlib import Path
import sys
import os
from reportlab.pdfgen import canvas
from pypdf import PdfReader

here = Path(__file__).resolve().parent
build_dir = Path(os.environ.get('PRESENTATION_BUILD_DIR', str(here))).resolve()
author = os.environ.get('PRESENTATION_AUTHOR', '').strip()
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else here.parents[2] / 'artifacts' / 'watt-window-next-horizon-draft.pdf'
output.parent.mkdir(parents=True, exist_ok=True)
pdf = canvas.Canvas(str(output), pagesize=(960, 540))
pdf.setTitle('Watt Window - Next Horizon application draft (review copy)')
pdf.setAuthor(author or 'Solo project - author details pending confirmation')
pdf.setSubject('Pre-event prototype. Review copy; submit the editable PPTX.')
for number in range(1, 7):
    image = build_dir / 'rendered' / f'slide-{number}.png'
    if not image.is_file():
        raise SystemExit(f'Missing inspected slide render: {image}')
    pdf.drawImage(str(image), 0, 0, width=960, height=540)
    pdf.showPage()
pdf.save()
output.chmod(0o600)
reader = PdfReader(str(output))
assert len(reader.pages) == 6
assert all(tuple(map(float, page.mediabox[2:])) == (960.0, 540.0) for page in reader.pages)
print(f'Review PDF: {output}; 6 pages; {output.stat().st_size} bytes')
