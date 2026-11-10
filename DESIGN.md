---
name: Batcave765
description: An after-hours engineering editorial for Sriram M's GitHub profile.
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
  hero:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.ivory}"
    typography: "{typography.artwork}"
  project-koda:
    backgroundColor: "{colors.electric-lime}"
    textColor: "{colors.charcoal}"
    typography: "{typography.artwork}"
  project-recur:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.charcoal}"
    typography: "{typography.artwork}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.ivory}"
    typography: "{typography.artwork}"
  signature:
    textColor: "{colors.electric-lime}"
---

# Design System: Batcave765

## Overview

**Creative North Star: "After-hours engineering editorial"**

Oversized geometric lettering, warm paper, dark ink, and an electric accent give the profile an independent editorial voice. Precise repeated geometry connects the artwork to engineering without obscuring the work itself.

The audience is engineering recruiters and hiring managers. Authored SVG artwork establishes identity; native GitHub Markdown carries selectable project details, experience, and contact links.

**Key Characteristics:**
- Bold outlined lettering and generous graphic space.
- A compact palette with sharply contrasted project treatments.
- Static, repeatable geometry paired with readable engineering substance.

## Colors

### Primary
- **Electric lime:** emphasis in the hero, the Koda field, Recur's motif panel, and the closing signature.

### Neutral
- **Charcoal:** hero and footer fields; dark project lettering and geometry.
- **Ivory:** primary lettering on dark artwork and Recur's main field.
- **Muted sage:** supporting hero labels.
- **Divider:** the quiet horizontal rule inside both hero compositions.

The frontmatter defines artwork colors. GitHub supplies the surrounding document's colors in each reader's theme.

## Typography

**Artwork:** Space Grotesk at semibold weight (600), converted to SVG paths by `scripts/build_artwork.py`. Font files are unnecessary at render time; the font license is retained in `assets/FONT-LICENSE.txt`.

The desktop name uses a large display size (152 SVG units), while the mobile name is recomposed over two lines (115 units). Project names share a display size (99 units). Supporting artwork labels range from 25 to 29 units. These are source-coordinate sizes and scale with each SVG, not fixed browser font sizes.

**Document:** GitHub determines prose, heading, link, table, and inline-code typography. Technology lists use native inline code. No custom prose font, CSS type scale, or font fallback is imposed.

## Layout

The README is a single flowing document. Artwork fills its available width; headings, lists, tables, native links, and a disclosure carry the body. Centered contact links sit below the hero. Explicit `<br>` elements separate major content blocks.

The `<picture>` selects `hero-mobile.svg` at a maximum viewport width of 600px. Desktop and mobile hero viewBoxes are 1200 by 530 and 600 by 570 respectively. The mobile hero deliberately reflows the name and statement. Project artwork uses 1200 by 250 viewBoxes; the footer uses 1200 by 110. All images retain their intrinsic aspect ratio.

## Elevation & Depth

Flat color fields, typographic scale, and contrast establish hierarchy. The artwork has no shadows, gradients, or simulated surface elevation. GitHub owns the treatment of native document elements.

## Shapes

Rectangular artwork frames contain precise, authored geometry. Three repeated ascending chevrons form the recurring signature; their mitered strokes scale with the mark. Koda uses an abstract sequence of narrow rounded bars. Recur uses three offset circular loops within a lime panel.

**The Geometry Rule.** The waveform and loops are decorative signatures, not measured data or product screenshots.

## Components

- **Hero:** dark field, ivory identity, lime statement, muted labels, quiet divider, and chevron signature. The mobile asset is a separate composition with the same visual language.
- **Koda banner:** lime field, dark project title and statement, abstract waveform. Its image links to the verified repository; the native heading and prose repeat the essential project identity.
- **Recur banner:** ivory field, dark project title and statement, lime geometry panel. The native heading and prose carry the project details.
- **Footer:** compact dark field with ivory handle, lime closing line, and repeated signature.
- **Native content:** GitHub headings, links, lists, table, inline code, and `<details>` retain platform interaction and focus behavior. No custom button or input system exists.

Artwork is static. Each SVG has a title and image semantics, while README images have descriptive alternative text. Substantive claims and contact actions remain accessible as native text.

## Do's and Don'ts

### Do:
- **Do** preserve the palette, semibold outlined lettering, and repeated geometry when extending the artwork.
- **Do** keep substantive information and navigation in native, selectable README text.
- **Do** maintain alternative text and SVG titles, and check both hero compositions when editing identity artwork.
- **Do** regenerate authored SVGs through `scripts/build_artwork.py` so geometry and font treatment stay consistent.

### Don't:
- **Don't** introduce custom page CSS or scripted interactions that GitHub cannot render.
- **Don't** treat decorative geometry as evidence, analytics, or a product screenshot.
- **Don't** replace native text with image-only claims or links.
- **Don't** substitute generated raster artwork for the authored SVG system.
