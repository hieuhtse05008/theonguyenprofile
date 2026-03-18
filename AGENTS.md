# AI Agent Project Guide

This file is the shared working guide for AI agents contributing to the website project inside this `web/` folder.

## Project Scope

- This project is a static portfolio site for Theongyn / Thao Nguyen.
- The current implementation starts with the homepage in `index.html`.
- The site is plain HTML, CSS, and JavaScript.
- Do not introduce a framework, package manager, or build system unless the user explicitly asks for it.

## Project Structure

```text
web/
|-- AGENTS.md
|-- index.html
`-- assets/
    |-- fonts/
    `-- images/
```

## External Design References

The design source files live outside this folder:

- Desktop homepage reference: `../Design png/Desktop/Home.png`
- Mobile homepage reference: `../Design png/Mobile/Home.png`
- Original design assets: `../Design png/`
- Original font files: `../source fonts/`

Use those folders as design references only. The live website should use assets from `./assets/`.

## Runtime Asset Rules

- Keep runtime images in `./assets/images/`.
- Keep runtime fonts in `./assets/fonts/`.
- If a design asset is needed on the live site, copy it into `./assets/`.
- Do not make the website depend on `../Design png/` or `../source fonts/` at runtime.

## Styling Rules

- Use Bootstrap for common layout, spacing, alignment, and utility styling.
- Use custom CSS only for brand-specific or design-specific details.
- Match the provided desktop and mobile mockups instead of falling back to generic Bootstrap styling.
- Keep the implementation lightweight and easy to open directly in a browser.

## Typography Rules

- Use `CirrusCumulus.otf` or `CirrusCumulus.ttf` for the welcome text and other intentional display text.
- Use `SFPRODISPLAYREGULAR.OTF` and other relevant SF Pro Display variants for standard UI and body text.
- Load fonts locally with `@font-face`.
- Prefer `font-display: swap`.

## Branding Rules

- Use `./assets/images/logo_Theongyn.png` for the logo.
- Preserve the existing bright green and bright pink palette from the design.
- Current homepage color tokens:
  - Green: `#3cd362`
  - Pink: `#fe45ee`
  - Ink: `#262626`

## Homepage Rules Already Implemented

- Main file: `index.html`
- Bootstrap is loaded via CDN.
- Fonts are loaded locally from `./assets/fonts/`.
- The header is responsive:
  - Desktop: logo plus navigation links
  - Mobile: logo plus custom hamburger toggle
- The hero uses a responsive `<picture>` element.
- The welcome block uses Cirrus Cumulus.

## Important Homepage Caveat

- A separate standalone hero source image was not clearly available in the provided asset set.
- The current hero uses reference-based runtime images:
  - `./assets/images/home-desktop-reference.png`
  - `./assets/images/home-mobile-reference.png`
- If a proper hero image is provided later, replace those files with the real asset.

## HTML / CSS / JS Conventions

- Keep HTML semantic and accessible.
- Use simple DOM scripting for interactions.
- Add `aria-label` values where helpful.
- Avoid unnecessary abstractions.
- Keep the code easy for another agent or human to continue.

## Expectations For Future Changes

- Extend the current visual language instead of redesigning the site by default.
- Preserve the homepage behavior unless the user requests a redesign.
- Keep desktop and mobile parity with the mockups.
- Update this file when new rules, pages, or structure are established.

## Suggested Workflow

1. Check the relevant mockup in `../Design png/`.
2. Copy any needed runtime asset into `./assets/`.
3. Reuse Bootstrap where it fits.
4. Add custom CSS only for unique visual details.
5. Verify both desktop and mobile behavior after changes.
6. Update this guide if the working rules change.

## Avoid

- Do not rely on external design folders at runtime.
- Do not casually rename or move the original design files.
- Do not replace the chosen fonts with defaults unless the user asks.
- Do not add a build system without explicit approval.
- Do not assume missing design details carelessly; stay close to the references.
