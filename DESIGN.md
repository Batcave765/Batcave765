---
name: Batcave765
description: A single-page engineering poster for Sriram M's GitHub profile.
colors:
  charcoal: "#151916"
  ivory: "#F3F1E8"
  electric-lime: "#D4FF63"
  muted-sage: "#B8C1B5"
  divider: "#465044"
typography:
  artwork:
    fontFamily: "Space Grotesk"
    fontWeight: 600
components:
  profile:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.ivory}"
    typography: "{typography.artwork}"
  name-field:
    backgroundColor: "{colors.electric-lime}"
    textColor: "{colors.charcoal}"
    typography: "{typography.artwork}"
  ribbon:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.charcoal}"
    typography: "{typography.artwork}"
  signature:
    textColor: "{colors.electric-lime}"
---

# Design System: Batcave765

## Overview

**Creative North Star: "Make it fast"**

Oversized geometric lettering, warm paper, dark ink, and an electric accent give the profile an independent editorial voice. Precise repeated geometry connects the artwork to engineering without obscuring the work itself.

The audience is engineering recruiters and hiring managers. The user explicitly requested a very short, single-page README and authorized one image for its content. A responsive SVG poster carries the content; native GitHub links below it provide project and contact actions. Comprehensive alt text supplies the content to screen readers.

**Key Characteristics:**
- Bold outlined lettering and generous graphic space.
- A compact palette with sharply contrasted project treatments.
- Static, repeatable geometry paired with readable engineering substance.

## Colors

### Primary
- **Electric lime:** name field, project titles, and engineering proof.

### Neutral
- **Charcoal:** poster ground and dark lettering on the name field and ribbon.
- **Ivory:** primary lettering on dark artwork and the diagonal ribbon.
- **Muted sage:** supporting role, project stack, and toolkit copy.
- **Divider:** quiet separators between information groups.

The frontmatter defines artwork colors. GitHub supplies the surrounding document's colors in each reader's theme.

## Typography

**Artwork:** Space Grotesk at semibold weight (600), converted to SVG paths by `scripts/build_artwork.py`. Font files are unnecessary at render time; the font license is retained in `assets/FONT-LICENSE.txt`.

Desktop name: 205 SVG units over two lines. Mobile name: 100 units on one line. Ribbon: 88 desktop / 54 mobile. Supporting copy: 22–40 desktop / 24–32 mobile. These source-coordinate sizes scale with each SVG.

**Document:** GitHub determines native link typography and interaction. The README has no prose sections or skills table.

## Layout

The README consists of one responsive picture and one centered line of four real links. The desktop poster splits the name and professional context across the upper half. A diagonal ribbon joins them; projects and a three-line toolkit finish the composition. Mobile reflows this into a single compact column.

The `<picture>` selects `profile-mobile.svg` at a maximum viewport width of 600px. Desktop and mobile viewBoxes are 1200×834 and 600×1000. At a typical desktop README width the poster occupies about 620px of height; on a 390px phone it occupies about 600px. Both retain their intrinsic aspect ratio.

## Elevation & Depth

Flat color fields, typographic scale, and contrast establish hierarchy. The artwork has no shadows, gradients, or simulated surface elevation. GitHub owns the treatment of native document elements.

## Shapes

Rectangular color fields and an ivory ribbon rotated -4° on desktop / -5° on mobile carry the composition. Three repeated ascending chevrons continue the existing signature. No extra project banners or icons.

**The Geometry Rule.** The chevrons and ribbon are graphic signatures, not measured data or product screenshots.

## Components

- **Profile:** one static composition, alternate desktop and mobile layouts, outlined name, role/proof, two projects, toolkit.
- **Ribbon:** the MAKE IT FAST statement crossing the name and role fields.
- **Native actions:** Koda, all code, LinkedIn, and email. GitHub owns hover/focus states. No fake buttons inside the image.

Artwork is static. Each SVG has a title and image semantics. README alternative text supplies its factual content; contact and project actions remain native links.

## Do's and Don'ts

### Do:
- **Do** preserve the palette, semibold outlined lettering, and repeated geometry when extending the artwork.
- **Do** keep native links and comprehensive alternative text for this explicitly image-led profile.
- **Do** maintain SVG titles and check both poster compositions when editing artwork.
- **Do** regenerate authored SVGs through `scripts/build_artwork.py` so geometry and font treatment stay consistent.

### Don't:
- **Don't** introduce custom page CSS or scripted interactions that GitHub cannot render.
- **Don't** treat decorative geometry as evidence, analytics, or a product screenshot.
- **Don't** put fake interactive links inside the poster or omit its factual alternative text.
- **Don't** substitute generated raster artwork for the authored SVG system.
