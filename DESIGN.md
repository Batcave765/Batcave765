---
name: Ideas into software
description: A light editorial skills poster for software engineer Sriram M.
colors:
  paper: "#F4F5F1"
  graphite: "#20262D"
  burnt-orange: "#C74628"
  secondary: "#525C60"
  rule: "#B8BFBC"
typography:
  display:
    fontFamily: "Manrope"
    fontWeight: 800
  heading:
    fontFamily: "Manrope"
    fontWeight: 650
  body:
    fontFamily: "Manrope"
    fontWeight: 450
components:
  poster:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.graphite}"
  accent-headline:
    textColor: "{colors.burnt-orange}"
    typography: "{typography.display}"
---

# Design System: Ideas into software

## Overview

A complete replacement of the previous lime/dark/ribbon world, explicitly requested by the user. Software engineering leads: web interfaces, mobile applications, and backend systems. Technologies supply substance; testing and observability are supporting tools within one of six groups.

The design follows an image-first target created with the built-in image tool, then rebuilt as precise SVG lettering and geometry. The source target, prompt and comparisons are kept in ignored review artifacts. It is a typographic poster, not a screenshot of interactive controls.

## Colors

Porcelain paper supports a light, calm reading surface. Graphite carries identity and tool names. Burnt orange emphasizes the software headline and connected-layer mark, with small squares introducing skill groups. Secondary type and thin rules use the same neutral family. The poster is theme-invariant; GitHub controls the surrounding page and native link colors.

## Typography

Manrope, licensed under the SIL Open Font License, is outlined by `scripts/build_artwork.py`. Display and group titles use weight 800; body uses 450; the mobile role uses 650. Source font files are not needed by visitors.

Desktop headline: 176 SVG units, with width fitting and tracking -5. Group headings: 39 units; tool copy: 29, fitted only when necessary. Mobile headline: 91 and 101 units; group headings: 30; tool copy: 27. Source-coordinate sizes scale with the SVG. Native links inherit GitHub typography.

## Layout

One responsive picture and four native links. Desktop: 1536×1024, matching the generated target's dimensions; identity above a large two-line headline and an offset connected-layer mark. A rule separates the hero from a three-column, two-row toolkit. Mobile: 600×1180, with compact identity and mark, a two-line headline, six vertically stacked skill groups, and a short footer. The mobile image is selected at viewport widths up to 600px.

The six groups are Languages, Web & interfaces, Mobile, Backend & data, Build & delivery, and Systems & audio. There are no project descriptions, employment metrics, availability badges, proficiency bars, or long prose sections.

## Elevation & Depth

Flat ink and paper. No shadows, gradients, texture, glass, or three-dimensional simulation. Scale, spacing and alignment establish hierarchy.

## Shapes

The connected-layer mark consists of three overlapping rectangular frames with a consistent 26-unit stroke. It suggests interface, application, and data layers. Small orange squares are editorial markers, not interactive icons. Rules separate major regions without boxing every group.

## Components

- **Poster:** role, identity, software headline, connected-layer geometry, six tool groups and footer.
- **Native links:** Koda, Projects, LinkedIn, Email; actual actions below the image. GitHub owns keyboard focus and hover behavior.
- **Accessibility:** a factual alt description contains the complete skills inventory. SVG titles, descriptions and labeled lettering groups describe the artwork. No essential action is trapped inside the image.

## Do's and Don'ts

- Do lead with software engineering and the breadth of building across web, mobile, and backend.
- Do preserve the light field, one orange accent, and Manrope typography.
- Do keep project links at the bottom and maintain exact, resume-grounded tool names.
- Don't restore lime, dark poster fields, diagonal ribbons, chevrons, employment metrics, or testing-first positioning.
- Don't put fake controls, unverified project links, proficiency ratings, or invented expertise claims inside the artwork.
