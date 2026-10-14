# Progress and testing record

Branch: `portfolio-overhaul` (from `master` at b24977a, clean tree). Nothing merged, pushed, committed or deployed: all changes are uncommitted in the working tree for review. To review: `git status`, `git diff master`. To discard everything: `git checkout master` then `git clean -fd` (this deletes the new untracked files too, so only do it if you are sure).

## Baseline (inspected 2026-10-14)

**Deployment.** No `.github/` folder: GitHub Pages builds the branch itself. The live site reports `Jekyll v3.10.0` and `Hydejack v9.2.1`. `_config.yml` used `remote_theme: hydecorp/hydejack@v9`, a moving **branch**; the `v9.2.1` tag exists, so the theme is now pinned to it.

**Stale local files (pre-existing, left alone).** `Gemfile.lock` pins Jekyll 4.3.2 plus `jekyll-theme-hydejack` 9.1.6 for `x64-mingw-ucrt` and does not list the `github-pages` gem `Gemfile` asks for. `_config.yml` had no `theme:` and did not list `jekyll-remote-theme`, so a plain local `jekyll build` would render without the theme; production is unaffected. `jekyll-remote-theme` is now listed so local and production builds match.

**Theme edition.** Hydejack v9.2.1 *free*. Present: layouts `about, blog, default, home, list, page, plain, post, redirect, not-found`; hooks `_includes/my-head.html`, `my-body.html`, `my-scripts.html`, `_sass/my-style.scss`, `my-inline.scss`, `my-variables.scss`; `_data/variables.yml` for widths. **Not in the free edition:** a search UI, dark mode (no `prefers-color-scheme` rules in the compiled CSS), project/resume/grid layouts.

**Layout fault (live site, 1600 px).** `main` was 864 px wide at x=400, leaving about 336 px empty on the right. The theme centres content in the viewport from 104rem up and reserves the gutters for its own contents box, so `no_third_column`/`no_toc` could not remove it. Fixed with widths in `_data/variables.yml` and a contents rail inside the column.

**Pre-existing defects.** Two broken images (`fuel-pump-module.svg`, `ppf-datum.svg`, deleted in commit 64fd7e4 but still referenced); five 1.6-2.1 MB PNGs with no image dimensions; the vertical scrollbar on display maths; breadcrumb contrast 4.48:1; unattributed throttle graph; hero image described as showing debug lines (it doesn't). None of these was introduced by this work.

**Labs.** `tools/rx8-omp/` and `tools/rx8-acceleration/` are Vite builds. Their sources and Vitest suites are outside this repo in `..\..\RX8 Drive Train Web Tool\` (read-only evidence). Node is not installed, so the labs were not rebuilt and no lab calculation was changed.

## Tooling used

| Tool | State |
| --- | --- |
| Ruby 3.2.11 + DevKit, `github-pages` gem (Jekyll 3.10.0) | installed with permission; `%LOCALAPPDATA%\jb` and `C:\Ruby32-x64` |
| Python 3.12 + venvs (PyMuPDF/Pillow) | scratchpad and `C:\cc-py` (short path needed for Pillow) |
| Browser pane | used for DOM measurement, layout, search, push-state and lab checks. It does not render frames while hidden, so animations and `requestAnimationFrame` handlers only advance when a screenshot forces a frame |
| Claude in Chrome | not used |
| Node / Vitest | not available |

## Batches

| Batch | Scope | Status |
| --- | --- | --- |
| 0 | Inventory, baseline, records, tooling | done |
| 1 | Shared layout, navigation, search, homepage, About, 404 | done |
| 2 | Case studies (MP1, ToolSync, EnduraOMP), projects index | done |
| 3 | RX-8 corrections and research (19 existing pages revised, 1 new lookup page) | done |
| 4 | Rocket League (7 existing pages revised, 3 new, tests, charts) | done |
| 5 | Integrated testing, image optimisation, polish, handover | done, see below |

## Tests actually run

- **Production-style build** (Jekyll 3.10.0, `JEKYLL_ENV=production`, remote theme v9.2.1): exit 0, about 20-35 s, repeatedly.
- **`check_site.py` on the build:** 40 HTML files, **0 problems**: no broken internal link/anchor/asset (exact-case checked), no heading jumps, one `h1` per page, no duplicate titles, no empty alt text, no leaked maintenance/draft/source files, no unreferenced oversized images. External URLs: see below.
- **Overflow at five widths (375, 768, 1280, 1600, 2560 px)** on all 38 content pages, measured in the browser: no horizontal overflow anywhere.
- **Rail:** sticks at 24 px (needed an `overflow: clip` fix because the theme clips `<hy-push-state>`); scroll-spy highlights the right section when frames render.
- **Search:** part numbers with and without punctuation (`N3H1-15-185` and `N3H1 15 185`), phrases, multi-word, misses, URL `?q=` update.
- **In-site navigation, back/forward:** no reload, content/title/maths/rail re-initialise, MathJax renders 0 errors, lab host pages size their iframes. Direct load and a deep link (`#coolant-hose-register`) checked.
- **Labs:** both load inside their host pages and report their height; the OMP Lab chart renders.
- **Contrast:** body 12.6:1, links 12.6:1, meta/rail 5.7:1, status tag colours 6:1 or better, breadcrumbs now 5.7:1.
- **Table keyboard access:** overflowing tables get `tabindex=0`, `role=region` and a name.
- **Rocket League maths:** `tools/rlbot_maths_tests.py`, 34 tests, all pass: aerial formula (printed form misses by about 1,500 uu, corrected form by under 0.001 uu), `ang_to` failure cases, turning radius table, time-to-distance, arc-then-line geometry (by driving the path), ETA estimator, pursuit simulation, handedness, team-aware defence.
- **Not tested here:** dark mode (not in this theme edition), print rendering (CSS written, not printed), screen-reader behaviour beyond markup inspection, real phones, Windows contrast modes. The static server used for the browser checks serves a plain 404 rather than GitHub's `404.html`.

## External links

`check_site.py --external` requested every distinct external URL in the build (140 including the site's own canonical URLs, 102 third-party after the checker was taught to resolve its own). **128 returned a success or redirect.** The failures, with the cause investigated:

| URL | Result | What it means |
| --- | --- | --- |
| callumdevlin.github.io new pages (5) | 404 | Canonical URLs of pages that aren't deployed yet. Expected; the checker now resolves these locally. |
| renewablelube.com product page | 403 | Cloudflare challenge; a browser opens it. Not bypassed. |
| rotaryrevs.com D585 page | TLS error | Certificate for another host (stackcp.com). Reported on the page as unopenable. |
| linkedin.com/in/callumdev | 999 | LinkedIn rejects scripted requests. Link kept (it is on the account list already). |
| manualslib.com (2004 Service Highlights p.173) | 403 | Bot protection; the research agent read it through a fetch tool. |
| raspberrypi.com documentation | 403 to the script | Opened and read through a fetch tool (the thermal figures on the ToolSync page come from it). |
| rx8ownersclub.co.uk (2 threads) | timeout | Slow or blocking; both were read by the research agent. |

None is a dead source that needs replacing. Other sources the research could not open (charm.li, enginebuildermag.com, racingbeat.com, several parts catalogues) are stated on the pages where a claim depends on them.

## Next steps (for a later session)

1. Fill the blank measurements and answer the questions in `owner-input.md`.
2. Add photographs (prototype, jack points, hose routes, PPF datum, fuel-pump module) and re-run `optimise_images.py`.
3. Decide on the MP1 back-plate load question and update the page if the FEA is re-run.
4. If a Node environment is installed, add Vitest checks for any change to the labs and re-publish `dist/`.
5. Consider self-hosting the two Google Fonts (privacy) and a `Gemfile`/`Gemfile.lock` refresh for local builds.
