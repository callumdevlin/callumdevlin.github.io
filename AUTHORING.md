# Adding to this site

Jekyll with the Hydejack v9.2.1 theme (free edition), built by GitHub Pages straight from the branch. Pages are plain Markdown. This file is excluded from the published site.

## Preview

GitHub builds with Jekyll 3.10 and the `github-pages` gem. To preview the same thing locally, install Ruby 3.2 and `gem install github-pages`, then run `jekyll serve` from the repository root (the remote theme needs network access; set `JEKYLL_ENV=production` for a production-style build). The `Gemfile` in the repository is older than this setup, so don't rely on `bundle exec` until it is refreshed.

## Where working files go

Scratch notes, research, screenshots and one-off helper scripts live in `_maintenance/`. That folder is git-ignored (`.gitignore`) and excluded from the build (`_config.yml`), so nothing in it is committed or published. Don't force-add it. Anything the site needs to build, such as images, data files and the labs, belongs in the tracked folders.

## A new page

Put a `.md` file under `ProjectPages/`. It gets the `notebook` layout and is added to search automatically. Front matter, all optional except `title`:

```yaml
---
title: Page title                  # also the H1
crumb: Short label                 # breadcrumbs and Previous/Next
permalink: /ProjectPages/RX8/new-page/
description: One-sentence introduction shown under the title and used for SEO.
applies: Series 1 RX-8 (2003-2008) # short applicability note under the title
status: wip                        # shows "Work in progress"; leave out otherwise
reviewed: 2026-10-14               # only if you re-checked the content against its sources
section: rlbot                     # Previous/Next group (_data/sections.yml); only sequence groups use it
nav_order: 3
related: [/ProjectPages/RX8/torquespecs/]   # short "See also" line at the bottom
toc: false                         # the collapsed "On this page" list appears on pages with five or more H2s
---
```

Keep URLs stable. If a page must move, add a redirect rather than breaking the old address. If you shorten a heading, keep the old anchor with `## New heading {#old-anchor}`.

## Writing

British English, first person for my own work, "we" for group work. Put the answer first, keep paragraphs short, and put a limitation next to the result it affects rather than in a page-wide caveat. Cite near the claim; for Mazda figures give the manual section and the mirror link. `{:.note}` after a paragraph makes a callout; use it sparingly. Maths is `$$ ... $$` (MathJax); code goes in fenced blocks with a language.

## Images and figures

Put the original in `Images/` and never edit or delete originals. For smaller WebP versions, add them to `Images/optimised/` as `name-<width>.webp` and list the width, height and variants for the original in `_data/images.yml`; an image with no entry still works, it just loads the original. Then use the include, which keeps the image's own aspect ratio and links it to the original:

```liquid
{% include figure.html src="/Images/name.png" alt="What it shows" caption="Short caption." %}
```

Options: `eager=true` for the first image on a page, `class="fig-narrow"` or `"fig-medium"` for small images, `full="..."` to link a different original, and `fulllink=true` to add a "Full-size image" link to the caption for plots and drawings with small print. Side-by-side images go in `<div class="fig-grid" markdown="0"> ... </div>`. Say in the caption when an image is a render or a synthetic graph. The Projects page lists projects with `{% include project-row.html ... %}`.

## Labs

The two labs are built bundles in `tools/rx8-omp/` and `tools/rx8-acceleration/`. Their source (TypeScript, with Vitest tests) lives outside this repository in `RX8 Drive Train Web Tool`. To change one, edit and test it there, rebuild, and copy the new `dist/` over the folder here. The host pages use `{% include lab-embed.html ... %}`.

## Search

`/search/` reads `/search.json`, generated from every page with `search: true` (all of `ProjectPages/`, plus About). Pages with `published: false`, the maintenance folder and this file never appear in it.
