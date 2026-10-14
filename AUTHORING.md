# Adding to this site

Jekyll with the Hydejack v9.2.1 theme (free edition), published by GitHub Pages straight from the branch. Pages are plain Markdown. This file is excluded from the published site.

## Preview and check

The machine needs Ruby 3.2 (RubyInstaller with DevKit) and the `github-pages` gem, which gives the same Jekyll 3.10 that GitHub runs. The scripts in `_maintenance/portfolio-overhaul/tools/` set this up outside the repository:

```powershell
.\_maintenance\portfolio-overhaul\tools\build.ps1                                   # production-style build into %LOCALAPPDATA%\jb\_site
python -m http.server 4000 --directory "$env:LOCALAPPDATA\jb\_site"                 # look at it at http://localhost:4000
python _maintenance\portfolio-overhaul\tools\check_site.py "$env:LOCALAPPDATA\jb\_site"           # links, anchors, headings, leaks
python _maintenance\portfolio-overhaul\tools\check_site.py "$env:LOCALAPPDATA\jb\_site" --external  # also request every external URL
python _maintenance\portfolio-overhaul\tools\rlbot_maths_tests.py                   # Rocket League worked examples
```

`_maintenance/README.md` explains the other files there (inventory, ledger, owner-input list).

## A new page

Put a `.md` file under `ProjectPages/` (it gets the `notebook` layout and is added to search automatically) with front matter like:

```yaml
---
title: Page title                 # also the H1
crumb: Short label                # breadcrumbs and Previous/Next (optional)
permalink: /ProjectPages/RX8/new-page/
type: reference                   # case-study | reference | procedure | wiring | data | explainer | maths | lab | index
section: rx8                      # joins a Previous/Next group from _data/sections.yml (optional)
nav_order: 14                     # position in that group
status: growing                   # wip | growing (shows a label; leave out for finished pages)
applies: Series 1 RX-8 (2003-2008) # one line: what the page applies to
reviewed: 2026-10-14              # ONLY if you re-checked the technical content against sources
description: One-sentence summary shown under the title and used for SEO.
related: [/ProjectPages/RX8/torquespecs/]   # optional links shown at the bottom
toc: false                        # contents navigation is automatic for pages with 3+ H2 headings
---
```

Keep URLs stable. If a page must move, add a redirect rather than breaking the old address.

## Writing conventions

- British English, first person for my own work, "we" for group work. Say what was measured, what was calculated from stated inputs, what comes from a manufacturer and what is an estimate, and where a value is unknown leave it blank.
- Cite near the claim. For Mazda figures give the manual section and the mirror link. Do not set `reviewed:` for formatting changes.
- `{:.note}` after a paragraph makes a callout; use sparingly.
- Inline status tags for table cells: `<span class="tag tag-spec">Catalogue</span>` (also `tag-measured`, `tag-derived`, `tag-estimate`, `tag-open`). Always keep the words, never colour alone.
- Write-in cell for a value not measured yet: `<span class="fill"></span>`.
- Maths: `$$ ... $$` (MathJax). Code: fenced blocks with a language.

## Images and figures

1. Put the **original** in `Images/` (never edit or delete originals; they are the full-quality downloads).
2. Run `python _maintenance/portfolio-overhaul/tools/optimise_images.py` (needs Pillow). It writes WebP variants to `Images/optimised/` and the dimensions to `_data/images.yml`.
3. Use the include so the image is captioned, uncropped, responsive and linked to the original:

```liquid
{% include figure.html src="/Images/name.png" alt="What it shows" caption="Short caption." %}
```

Side-by-side images: wrap two or more includes in `<div class="fig-grid" markdown="0"> ... </div>`. Use `eager=true` for the first image on a page, `class="fig-narrow"` or `fig-medium` for small images. Say in the caption when an image is a render or a synthetic graph. Cards (home and project index) use `{% include card.html ... %}`.

## Labs

The two labs are built bundles in `tools/rx8-omp/` and `tools/rx8-acceleration/`. Their source (TypeScript, Vitest tests) lives outside this repository in `RX8 Drive Train Web Tool`. To change one, edit and test it there, rebuild, and copy the new `dist/` over the folder here. The host pages use `{% include lab-embed.html ... %}`.

## Search

`/search/` reads `/search.json`, generated from every page with `search: true` (all of `ProjectPages/`, plus About). Drafts (`published: false`), the maintenance folder and this file never appear in it.
