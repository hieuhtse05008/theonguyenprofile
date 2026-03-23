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
- **Strict Image Fidelity:** Do absolutely NOT reuse or loop existing images as placeholders if the Figma design contains unique images. Every image block must use its exact corresponding image.
- **Missing Assets:** If a required image shown in Figma is missing from the local `./assets/` directory, you MUST extract the exact image asset directly from the Figma Dev Mode server (e.g., using `get_design_context` to find the localhost URL and downloading it via `Invoke-WebRequest` or `curl`) and save it locally. Do not guess or substitute.

## Styling Rules

- Use Bootstrap for common layout, spacing, alignment, and utility styling.
- Use custom CSS only for brand-specific or design-specific details.
- Match the provided desktop and mobile mockups instead of falling back to generic Bootstrap styling.
- Keep the implementation lightweight and easy to open directly in a browser.
- **Navigation buttons:** Do not add internal padding to navbar/menu buttons unless the user explicitly asks for it. If the Figma header looks off, fix sizing, width, line-height, or surrounding layout first, but keep button padding at `0` by default.

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

## Project Detail Page System (details.html)

- **Data-Driven Rendering:** Uses `projects-data.js` to dynamically generate content.
- **Content Blocks:** Supports a flexible `content` array with multiple block types:
  - `single`: Full-width image.
  - `row`: Multi-column images (use `gap: "0"` for seamless grids).
  - `text` / `titled-text`: Structured typographic sections.
  - `grid`: Flexible image/HTML grids.
- **Custom Project Renderers:** Some projects use specialized render functions (e.g., `renderTuwProject`, `renderLogosProject`) for unique layout requirements.

### Project Specific Patterns

- **Project 5 (TUW):** 
  - Uses CSS `background-image` with `url()` for product panels instead of `<img>` tags to ensure pixel-perfect alignment and centering.
  - Desktop panels use `display: flex` with `align-items: stretch` to force equal heights between design and real-product panels.
- **Project 6 (DLK):** 
  - Extends the content block system with custom types: `dlk-body` (A-D sections), `dlk-team-logo` (split layout with overlays), `dlk-merch` (dark background products), and `dlk-illustration` (fixed 3-col square grid).
  - Handles string-based `team` metadata in addition to object-array formats.

## HTML / CSS / JS Conventions

- Keep HTML semantic and accessible.
- Use simple DOM scripting for interactions.
- Add `aria-label` values where helpful.
- Avoid unnecessary abstractions.
- Keep the code easy for another agent or human to continue.
- **Gap Handling:** When rendering `gap` in rows, check `block.gap != null` to allow `0` as a valid value.

## Expectations For Future Changes

- Extend the current visual language instead of redesigning the site by default.
- Preserve the homepage and detail page behaviors unless a redesign is requested.
- Keep desktop and mobile parity with the mockups.
- Update this file when new rules, pages, or major rendering structures are established.

## Suggested Workflow

1. Check the relevant mockup in `../Design png/`.
2. Copy any needed runtime asset into `./assets/`.
3. Reuse Bootstrap where it fits.
4. Add custom CSS only for unique visual details in `details.html`.
5. Verify both desktop and mobile behavior after changes.
6. Update this guide if the working rules change.

## Avoid

- Do not rely on external design folders at runtime.
- Do not casually rename or move the original design files.
- Do not replace the chosen fonts with defaults unless the user asks.
- Do not add a build system without explicit approval.
- Do not assume missing design details carelessly; stay close to the references.
- **Do not repeat previous images as placeholders** just because the specific asset isn't originally present in the local directory; fetch the exact asset from Figma instead.
- **Do not use fixed heights for dynamic content columns** unless synchronization is required (like in TUW). Prefer flex/grid stretching.

