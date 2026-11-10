"""Build portable profile artwork. Usage: python scripts/build_artwork.py FONT.ttf

Requires fonttools. All lettering is outlined: GitHub needs no fonts or scripts.
Font: Space Grotesk, SIL Open Font License (see assets/FONT-LICENSE.txt).
"""
from pathlib import Path
from html import escape
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.profile-tools'))
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

font = TTFont(sys.argv[1])
if 'fvar' in font:
    font = instantiateVariableFont(font, {'wght': 600})
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
units = font['head'].unitsPerEm
INK, PAPER, LIME, MUTED = '#151916', '#F3F1E8', '#D4FF63', '#B8C1B5'


def text(value, x, y, size, color=INK, spacing=0):
    scale = size / units
    paths, cursor = [], 0
    for char in value:
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            paths.append(f'<path transform="translate({cursor:.3f} 0)" d="{pen.getCommands()}"/>')
        cursor += glyphs[name].width + spacing / scale
    return f'<g fill="{color}" transform="translate({x} {y}) scale({scale:.6f} {-scale:.6f})">' + ''.join(paths) + '</g>'


def svg(name, width, height, title, body, bg):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<rect width="{width}" height="{height}" fill="{bg}"/>
{body}
</svg>\n'''
    (ROOT / 'assets' / name).write_text(content, encoding='utf-8')


def mark(x, y, size, color=LIME):
    # Three ascending chevrons: one repeated, precisely constructed signature.
    return ''.join(f'<path d="M {x+i*size*.28:.2f} {y+size:.2f} L {x+i*size*.28+size*.48:.2f} {y+size*.5:.2f} L {x+i*size*.28:.2f} {y:.2f}" fill="none" stroke="{color}" stroke-width="{size*.12}" stroke-linejoin="miter"/>' for i in range(3))


(ROOT / 'assets').mkdir(exist_ok=True)
svg('hero.svg', 1200, 530, 'Sriram M — software engineer. Fast systems. Thoughtful software.',
    text('SRIRAM M.', 48, 190, 152, PAPER, -3)
    + text('Software Engineer', 54, 251, 27, MUTED)
    + '<path d="M54 287H1146" stroke="#465044"/>'
    + text('Fast systems.', 49, 385, 88, LIME, -2)
    + text('Thoughtful software.', 49, 469, 74, PAPER, -2)
    + mark(974, 335, 110), INK)

svg('hero-mobile.svg', 600, 570, 'Sriram M — software engineer. Fast systems. Thoughtful software.',
    text('SRIRAM', 27, 133, 115, PAPER, -3)
    + text('M.', 29, 242, 115, PAPER, -3)
    + mark(405, 166, 83)
    + text('Software Engineer', 32, 296, 28, MUTED)
    + '<path d="M32 332H568" stroke="#465044"/>'
    + text('Fast systems.', 28, 402, 65, LIME, -2)
    + text('Thoughtful', 28, 472, 65, PAPER, -2)
    + text('software.', 28, 538, 65, PAPER, -2), INK)

# Deterministic waveform geometry is an abstract motif, not measured project data.
wave = ''
for i in range(45):
    h = 16 + 106 * abs(math.sin(i * .29) * math.cos(i * .13))
    wave += f'<rect x="{723+i*9}" y="{125-h/2:.2f}" width="4" height="{h:.2f}" rx="2" fill="{INK}"/>'
svg('koda.svg', 1200, 250, 'Koda — audio in, insight out.',
    text('Koda', 44, 126, 99, INK, -3)
    + text('Audio in. Insight out.', 49, 181, 29, INK)
    + wave, LIME)

loops = ''.join(f'<rect x="{834+i*63}" y="{45+i*11}" width="150" height="150" rx="75" fill="none" stroke="{INK}" stroke-width="9"/>' for i in range(3))
svg('recur.svg', 1200, 250, 'Recur — your subscriptions, closer to home.',
    '<path d="M740 0H1200V250H740Z" fill="#D4FF63"/>'
    + text('Recur', 44, 126, 99, INK, -3)
    + text('Your subscriptions. Closer to home.', 49, 181, 26, INK)
    + loops, PAPER)

svg('footer.svg', 1200, 110, 'Batcave765 — built with intent.',
    text('BATCAVE765', 40, 68, 25, PAPER, 1)
    + text('Built with intent.', 839, 68, 27, LIME)
    + mark(655, 37, 34), INK)
print('Built five outlined SVG assets in assets/.')
