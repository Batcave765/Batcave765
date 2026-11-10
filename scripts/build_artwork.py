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
    title = 'Sriram M. Make it fast. Languages, web and mobile, backend and data, cloud and performance, build and audio.'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="{w}" height="{h}" fill="{INK}"/>{body}</svg>\n'
    (ROOT / 'assets' / name).write_text(svg, encoding='utf-8')


desktop = '<rect width="555" height="329" fill="#D4FF63"/>'
desktop += text('SRI', 35, 139, 170, INK, -4)
desktop += text('RAM.', 35, 282, 170, INK, -4)
desktop += text('Software engineer.', 610, 92, 40)
desktop += text('Chennai, India / Batcave765', 613, 136, 24, MUTED)
desktop += text('Full-stack. Mobile.', 613, 211, 34)
desktop += text('Performance.', 613, 254, 34, LIME)
desktop += ribbon(329, 1200, 91, -4, 'MAKE IT FAST.', 76)

rows = [
    ('Languages', ['TypeScript · Go · JavaScript · Python · Java · C · C++ · SQL']),
    ('Web + mobile', ['React · Next.js · React Native · Expo · Tailwind CSS', 'NativeWind · Reanimated · Radix UI']),
    ('Backend + data', ['Gin · Spring Boot · SpacetimeDB · Drizzle ORM', 'MySQL · MongoDB · MMKV · Zod']),
    ('Cloud + perf', ['GCP · k6 · Grafana · Dynatrace · Elasticsearch']),
    ('Build + audio', ['Docker · Compose · GitLab CI/CD · Bun · Git', 'Postman · FFmpeg · Gonum']),
]
for y, (label, lines) in zip([455, 529, 621, 713, 787], rows):
    desktop += text(label, 49, y, 27, LIME)
    for i, line in enumerate(lines):
        desktop += text(line, 296, y + i * 35, 26)
    if y != 787:
        desktop += f'<path d="M50 {y + (len(lines)-1)*35+25}H1150" stroke="#465044"/>'
save('profile.svg', 1200, 854, desktop)

mobile = '<rect width="600" height="219" fill="#D4FF63"/>'
mobile += text('SRIRAM M.', 26, 107, 100, INK, -3)
mobile += text('Software engineer / Chennai', 30, 160, 29, INK)
mobile += ribbon(237, 600, 82, -5, 'MAKE IT FAST.', 54)
mobile_rows = [
    (330, 'Languages', ['TypeScript · Go · JavaScript · Python', 'Java · C · C++ · SQL']),
    (461, 'Web + mobile', ['React · Next.js · React Native · Expo', 'Tailwind CSS · NativeWind', 'Reanimated · Radix UI']),
    (625, 'Backend + data', ['Gin · Spring Boot · SpacetimeDB', 'Drizzle ORM · MySQL · MongoDB', 'MMKV · Zod']),
    (789, 'Cloud + performance', ['GCP · k6 · Grafana · Dynatrace', 'Elasticsearch']),
    (920, 'Build + audio', ['Docker · Compose · GitLab CI/CD · Bun', 'Git · Postman · FFmpeg · Gonum']),
]
for y, label, lines in mobile_rows:
    mobile += text(label, 30, y, 29, LIME)
    for i, line in enumerate(lines):
        mobile += text(line, 31, y + 40 + i*34, 26)
    if y != 920:
        mobile += f'<path d="M30 {y+40+(len(lines)-1)*34+23}H570" stroke="#465044"/>'
save('profile-mobile.svg', 600, 1020, mobile)
print('Built desktop + mobile single-page profile artwork.')
