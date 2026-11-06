"""Original editable vector cover art and an actual-pilot chart, rasterized locally."""
from pathlib import Path
import html
import cairosvg

BASE = Path(__file__).resolve().parent / 'drafts'

def svg(body, background):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="630" height="500" viewBox="0 0 630 500"><rect width="630" height="500" fill="{background}"/>{body}</svg>'

def text(x,y,value,size=16,color='#e8e1ce',font='sans-serif',weight='400',spacing=0):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-family="{font}" font-weight="{weight}" letter-spacing="{spacing}">{html.escape(value)}</text>'

lumen = text(34,38,'GAME OFF 2026 / SHIFT',11,'#80ada6','monospace',spacing=2)
lumen += text(32,109,'LUMEN',67,'#e9edda','serif') + text(32,170,'SHIFT',67,'#e9edda','serif')
lumen += text(34,207,'Eight boards. One clear signal.',17,'#9db5ab')
for row,bits in enumerate([[1,0,0,1,0,1],[0,1,1,0,1,0],[1,1,1,1,1,1]]):
    y = 255 + row*57
    lumen += f'<rect x="32" y="{y-19}" width="566" height="44" rx="5" fill="#142e32" stroke="#345653"/>'
    lumen += text(48,y+9,['IN','XOR','OUT'][row],11,'#86b2a4','monospace')
    for col,bit in enumerate(bits):
        x=142+col*67
        lumen += f'<circle cx="{x}" cy="{y+3}" r="12" fill="{["#263f40","#e3ba77"][bit]}" stroke="#789383" stroke-width="1"/>'
    lumen += text(557,y+10,'↻',23,'#a2c9bc')
lumen += text(34,454,'CIRCULAR SHIFTS / ROTATION / XOR',10,'#88a99c','monospace',spacing=1)
lumen += text(34,480,'ORIGINAL PROCEDURAL COVER ART · NOT A GAME SCREENSHOT',8,'#66887d','monospace')

parallax = text(34,38,'A FIRST-PERSON OBSERVATION PUZZLE',10,'#98b5a4','monospace',spacing=1.7)
parallax += text(32,103,'Parallax',59,'#e9e2d0','serif') + text(32,163,'Postcards',59,'#e9e2d0','serif')
parallax += '<path d="M32 226 L315 202 L598 226 L598 423 L32 423 Z" fill="#253b39" stroke="#456154"/>'
parallax += '<path d="M32 423 L315 310 L598 423 M32 226 L315 310 L598 226" fill="none" stroke="#43564b"/>'
parallax += '<rect x="153" y="236" width="324" height="160" rx="4" fill="#102327" stroke="#7d9580" transform="rotate(-4 315 316)"/>'
for points,color in [('218,364 218,308 315,253','#e8b58e'),('315,253 412,308 412,364','#a7d9cc'),('412,364 344,364 344,327 286,327 286,364 218,364','#f2d8a5')]:
    parallax += f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
parallax += text(34,452,'Three rooms. A small change of perspective.',15,'#b3c7b8')
parallax += text(34,480,'ORIGINAL PROCEDURAL COVER ART · NOT A GAME SCREENSHOT',8,'#718c7b','monospace')

paper = text(34,38,'FOUR LITTLE DELIVERY PUZZLES',11,'#61766b','monospace',spacing=1.8)
paper += text(30,103,'PAPER ROUTE',55,'#29463e','serif')
paper += text(34,137,'One pocket. Every parcel in its right place.',15,'#6f7e70')
rows=['#######','#S..a.#','#.#.#.#','#...A.#','#######']
left,top,cell=91,177,64
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        xx,yy=left+x*cell,top+y*50
        color='#dce0d1' if char=='#' else '#fffdf3'
        if char=='a':color='#4c8270'
        paper += f'<rect x="{xx}" y="{yy}" width="58" height="44" rx="3" fill="{color}" stroke="#ccd3c1"/>'
        if char in 'aA':paper += text(xx+21,yy+30,char,24,'#fffdf3' if char=='a' else '#397363','monospace','700')
        if char=='S':
            paper += f'<circle cx="{xx+29}" cy="{yy+22}" r="13" fill="#bd523d"/>'
            paper += '<path d="M0 0" fill="none"/>'
paper += '<path d="M207 250 L335 250 M399 298 L399 326" fill="none" stroke="#c27d55" stroke-width="3" stroke-dasharray="6 6"/>'
paper += text(34,455,'REPLAY YOUR ROUTE / SEE WHY THE RULES MATTER',10,'#627a69','monospace')
paper += text(34,480,'ORIGINAL PROCEDURAL COVER ART · NOT A GAME SCREENSHOT',8,'#7e8d79','monospace')

chart = text(32,40,'SOURCE TRAIL',23,'#e5ead4','monospace',weight='700')
chart += text(32,77,'Actual synthetic pilot',32,'#e5ead4','serif')
chart += text(32,108,'PRE-SPRINT WORK / 2026-11-05',11,'#b5cbb4','monospace',spacing=1)
chart += text(32,145,'16 authored cases · fixed selections · no model calls',12,'#91aea2')
chart += text(32,205,'Policy',11,'#a5c2b2','monospace') + text(236,188,'Bad citation',10,'#a5c2b2','monospace') + text(236,205,'released',10,'#a5c2b2','monospace')
chart += text(377,188,'Review need',10,'#a5c2b2','monospace') + text(377,205,'missed',10,'#a5c2b2','monospace')
chart += text(505,188,'Eligible',10,'#a5c2b2','monospace') + text(505,205,'withheld',10,'#a5c2b2','monospace')
for n,(name,values)in enumerate([('quote-only',['4/4','5/5','0/7']),('exact-span',['0/4','5/5','1/7']),('full gate',['0/4','2/5','2/7'])]):
    y=251+n*58
    chart += f'<rect x="24" y="{y-29}" width="582" height="49" rx="3" fill="{["#1c3636","#24413c","#2d4d40"][n]}"/>'
    chart += text(36,y+1,name,16,'#e5ead4','monospace')
    for x,value in zip([250,399,526],values):chart += text(x,y+1,value,21,'#e8b58e','monospace')
chart += text(32,433,'Author-defined expectations; not an LLM or truth benchmark.',11,'#acc1ae')
chart += text(32,459,'Wrong/missing labels and false holds remain visible.',11,'#acc1ae')
chart += text(32,483,'NO NOVEMBER 13–15 RESULTS ARE CLAIMED',9,'#87a78f','monospace',spacing=1)

for project,body,bg in [('lumen-shift',lumen,'#0b2027'),('parallax-postcards',parallax,'#14272b'),('paper-route-playtest',paper,'#f1ecdf'),('source-trail-otari',chart,'#10272b')]:
    media=BASE/project/'media';media.mkdir(exist_ok=True)
    name='pilot-results' if project=='source-trail-otari' else 'cover'
    source=svg(body,bg)
    (media/f'{name}.svg').write_text(source)
    cairosvg.svg2png(bytestring=source.encode(),write_to=str(media/f'{name}.png'),output_width=630,output_height=500)
    (media/'README.md').write_text('Original 630×500 procedural vector artwork, authored with Codex assistance and rasterized locally with CairoSVG. No third-party artwork or image-generation model used. Game covers are cover illustrations, not gameplay screenshots. Source Trail image shows the actual pre-sprint 2026-11-05 synthetic pilot counts, not future sprint results. SVG source is editable; PNG is the upload image.\n')
    print(project,(media/f'{name}.png').stat().st_size,'bytes')
