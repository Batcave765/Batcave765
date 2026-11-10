"""Build the software-engineer poster: python scripts/build_artwork.py Manrope.ttf.

Requires fonttools. All lettering is outlined; no browser fonts, scripts, or
external image services are required. Manrope license: assets/FONT-LICENSE.txt.
The image-first design target and generation prompt stay in ignored review files.
"""
from html import escape
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.profile-tools'))
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

fonts = {}
for weight in (450, 650, 800):
    font = TTFont(sys.argv[1])
    if 'fvar' in font:
        font = instantiateVariableFont(font, {'wght': weight})
    fonts[weight] = (font.getGlyphSet(), font.getBestCmap(), font['head'].unitsPerEm)

PAPER, INK, ACCENT, SECONDARY, RULE = '#F4F5F1', '#20262D', '#C74628', '#525C60', '#B8BFBC'


def width(value, size, weight=450, spacing=0):
    glyphs, cmap, units = fonts[weight]
    return sum(glyphs[cmap[ord(c)]].width * size / units + spacing for c in value)


def text(value, x, y, size, color=INK, weight=450, spacing=0, max_width=None, right=False):
    if max_width and width(value, size, weight, spacing) > max_width:
        size *= max_width / width(value, size, weight, spacing)
    if right:
        x -= width(value, size, weight, spacing)
    glyphs, cmap, units = fonts[weight]
    scale, cursor, paths = size / units, 0, []
    for char in value:
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            paths.append(f'<path transform="translate({cursor:.3f} 0)" d="{pen.getCommands()}"/>')
        cursor += glyphs[name].width + spacing / scale
    return (f'<g aria-label="{escape(value, quote=True)}" fill="{color}" '
            f'transform="translate({x:.3f} {y}) scale({scale:.6f} {-scale:.6f})">'
            + ''.join(paths) + '</g>')


def layers(x, y, scale=1):
    # Three connected open frames: interface, application, and data layers.
    return (f'<g transform="translate({x} {y}) scale({scale})" fill="none" '
            f'stroke="{ACCENT}" stroke-width="26" stroke-linejoin="miter">'
            '<path d="M108 12H328V242H108Z"/>'
            '<path d="M12 118H238V320H12Z"/>'
            '<path d="M182 170H422V370H182Z"/></g>')


def rule(y, w, margin):
    return f'<path d="M{margin} {y}H{w-margin}" fill="none" stroke="{RULE}" stroke-width="1.5"/>'


def save(name, w, h, body):
    title = 'Sriram M. Software engineer. Ideas into software.'
    desc = 'Web interfaces, mobile apps, and backend systems. A toolkit of languages, web, mobile, backend, delivery, systems, and audio technologies.'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">'
           f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>'
           f'<rect width="{w}" height="{h}" fill="{PAPER}"/>{body}</svg>\n')
    (ROOT / 'assets' / name).write_text(svg, encoding='utf-8')


groups = [
    ('Languages', ['TypeScript · Go · JavaScript', 'Python · Java · C · C++ · SQL']),
    ('Web & interfaces', ['React · Next.js · Tailwind CSS', 'Radix UI']),
    ('Mobile', ['React Native · Expo · NativeWind', 'Reanimated · MMKV · Zod']),
    ('Backend & data', ['Gin · Spring Boot · SpacetimeDB', 'Drizzle ORM · MySQL · MongoDB']),
    ('Build & delivery', ['Docker · Compose · GitLab CI/CD', 'Bun · Git · Postman']),
    ('Systems & audio', ['GCP · Grafana · Dynatrace', 'Elasticsearch · k6 · FFmpeg · Gonum']),
]

desktop = text('Sriram M.', 36, 84, 64, weight=800, spacing=-1.5)
desktop += text('Software engineer', 1500, 50, 32, right=True)
desktop += text('Chennai, India', 1500, 90, 30, color=SECONDARY, right=True)
desktop += text('Ideas into', 29, 283, 176, weight=800, spacing=-5, max_width=870)
desktop += text('software.', 29, 439, 176, color=ACCENT, weight=800, spacing=-5, max_width=870)
desktop += text('Web interfaces. Mobile apps. Backend systems.', 40, 508, 34, max_width=885)
desktop += layers(956, 146)
desktop += rule(552, 1536, 30)
for i, (label, lines) in enumerate(groups):
    x, y = (36, 538, 1040)[i % 3], (620 if i < 3 else 794)
    desktop += f'<rect x="{x}" y="{y-25}" width="19" height="19" fill="{ACCENT}"/>'
    desktop += text(label, x+35, y, 39, weight=800, spacing=-.8, max_width=440)
    for j, line in enumerate(lines):
        desktop += text(line, x, y+48+j*39, 29, max_width=460)
desktop += text('Batcave765', 36, 984, 34, weight=800, spacing=-.5)
desktop += text('Build with curiosity. Ship with care.', 1500, 984, 31, right=True)
save('engineer.svg', 1536, 1024, desktop)

mobile = text('Sriram M.', 30, 75, 52, weight=800, spacing=-1.3)
mobile += text('Software engineer', 32, 119, 26, weight=650)
mobile += text('Chennai, India', 32, 154, 23, color=SECONDARY)
mobile += layers(459, 31, .24)
mobile += text('Ideas into', 26, 255, 91, weight=800, spacing=-2.5, max_width=548)
mobile += text('software.', 26, 346, 101, color=ACCENT, weight=800, spacing=-3, max_width=548)
mobile += text('Web interfaces. Mobile apps. Backend systems.', 32, 397, 24, max_width=536)
mobile += rule(425, 600, 30)
for i, (label, lines) in enumerate(groups):
    y = 486 + i*104
    mobile += f'<rect x="32" y="{y-19}" width="13" height="13" fill="{ACCENT}"/>'
    mobile += text(label, 58, y, 30, weight=800, spacing=-.5)
    for j, line in enumerate(lines):
        mobile += text(line, 32, y+37+j*32, 27, max_width=536)
mobile += rule(1104, 600, 30)
mobile += text('Batcave765', 32, 1151, 26, weight=800)
mobile += text('Build. Learn. Ship.', 568, 1151, 24, right=True)
save('engineer-mobile.svg', 600, 1180, mobile)
print('Built new light/orange software-engineer posters with outlined Manrope.')
