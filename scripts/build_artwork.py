"""Build the one-page profile. Usage: python scripts/build_artwork.py FONT.ttf

Requires fonttools. Space Grotesk is outlined for portable GitHub rendering.
License: assets/FONT-LICENSE.txt. No runtime fonts or external image services.
"""
from pathlib import Path
from html import escape
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


def text(value, x, y, size, color=PAPER, spacing=0):
    scale, cursor, paths = size / units, 0, []
    for char in value:
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            paths.append(f'<path transform="translate({cursor:.3f} 0)" d="{pen.getCommands()}"/>')
        cursor += glyphs[name].width + spacing / scale
    return f'<g fill="{color}" transform="translate({x} {y}) scale({scale:.6f} {-scale:.6f})">' + ''.join(paths) + '</g>'


def chevrons(x, y, size, color):
    return ''.join(f'<path d="M{x+i*size*.3} {y}l{size*.5} {size*.5}l{-size*.5} {size*.5}" fill="none" stroke="{color}" stroke-width="{size*.11}"/>' for i in range(3))


def ribbon(y, width, height, angle, label, size):
    return (f'<g transform="translate({width/2} {y}) rotate({angle})">'
            f'<rect x="{-width*.6}" y="{-height/2}" width="{width*1.2}" height="{height}" fill="{PAPER}"/>'
            + text(label, -width*.45, size*.32, size, INK, -size*.025)
            + chevrons(width*.32, -height*.28, height*.56, INK) + '</g>')


def save(name, w, h, body):
    title = 'Sriram M. Make it fast. Performance engineering, full-stack and local-first apps.'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="{w}" height="{h}" fill="{INK}"/>{body}</svg>\n'
    (ROOT / 'assets' / name).write_text(svg, encoding='utf-8')


desktop = '<rect width="555" height="422" fill="#D4FF63"/>'
desktop += text('SRI', 35, 174, 205, INK, -6)
desktop += text('RAM.', 35, 349, 205, INK, -6)
desktop += text('Software engineer.', 610, 88, 40)
desktop += text('Chennai, India / Batcave765', 613, 129, 23, MUTED)
desktop += text('Performance + automation', 613, 208, 30)
desktop += text('Cognizant / Macy\'s supply chain', 613, 246, 23, MUTED)
desktop += text('3,000 TPS workloads.', 613, 303, 27, LIME)
desktop += text('3–4h saved per release.', 613, 342, 27, LIME)
desktop += ribbon(423, 1200, 112, -4, 'MAKE IT FAST.', 88)
desktop += text('Koda', 49, 561, 52, LIME, -1)
desktop += text('Audio → BPM + musical key.', 51, 601, 25)
desktop += text('Go / Next.js / FFmpeg', 51, 635, 22, MUTED)
desktop += '<path d="M580 518V651" stroke="#465044"/>'
desktop += text('Recur', 625, 561, 52, LIME, -1)
desktop += text('Subscriptions. Local-first. Instant.', 627, 601, 25)
desktop += text('React Native / Expo / MMKV', 627, 635, 22, MUTED)
desktop += '<path d="M50 682H1150" stroke="#465044"/>'
desktop += text('TypeScript · Go · Python · Java · SQL · React · Next.js · React Native · Expo', 51, 724, 23)
desktop += text('Tailwind · MMKV · Zod · Spring Boot · SpacetimeDB · Drizzle · MySQL · MongoDB', 51, 760, 23)
desktop += text('k6 · GCP · Grafana · Dynatrace · GitLab CI/CD · Docker · Bun · Git · FFmpeg', 51, 796, 23, MUTED)
save('profile.svg', 1200, 834, desktop)

mobile = '<rect width="600" height="219" fill="#D4FF63"/>'
mobile += text('SRIRAM M.', 26, 107, 100, INK, -3)
mobile += text('Software engineer / Chennai', 30, 160, 29, INK)
mobile += ribbon(237, 600, 82, -5, 'MAKE IT FAST.', 54)
mobile += text('Performance + automation', 30, 344, 32)
mobile += text('Cognizant / Macy\'s supply chain', 31, 386, 26, MUTED)
mobile += text('3,000 TPS workloads.', 31, 438, 28, LIME)
mobile += text('3–4h saved per release.', 31, 478, 28, LIME)
mobile += '<path d="M30 512H570" stroke="#465044"/>'
mobile += text('Koda', 28, 574, 48, LIME)
mobile += text('Audio → BPM + key. Go / Next.js.', 31, 615, 27)
mobile += text('Recur', 28, 692, 48, LIME)
mobile += text('Local-first subscriptions.', 31, 733, 27)
mobile += text('React Native / Expo / MMKV', 31, 771, 26, MUTED)
mobile += '<path d="M30 809H570" stroke="#465044"/>'
mobile += text('TypeScript · Go · Python · Java · SQL', 31, 851, 25)
mobile += text('React · Next.js · React Native · Expo', 31, 889, 25)
mobile += text('MMKV · Zod · Spring Boot · SpacetimeDB', 31, 927, 24)
mobile += text('k6 · GCP · Grafana · CI/CD · Docker · Git', 31, 965, 24, MUTED)
save('profile-mobile.svg', 600, 1000, mobile)
print('Built desktop + mobile single-page profile artwork.')
