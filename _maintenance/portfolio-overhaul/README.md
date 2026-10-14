# Portfolio overhaul: maintenance records

These files exist to finish and hand over the overhaul reliably. They are **not published**: `_maintenance/` is listed under `exclude:` in `_config.yml` (and Jekyll skips underscore folders anyway). Run `python _maintenance/portfolio-overhaul/tools/check_site.py _site` after a build to confirm nothing from this folder leaked into the output.

| File | Purpose |
| --- | --- |
| [progress.md](progress.md) | Baseline, completed batches, tests actually run, exact next steps. |
| [inventory.md](inventory.md) | Every authored page: URL, type, WIP status, and separate content / fact-check / visual review status. |
| [ledger.md](ledger.md) | Research and corrections ledger: claim, evidence, applicability, correction, open questions, access date. |
| [owner-input.md](owner-input.md) | Things only Callum can supply (measurements, part numbers, photos, build status). Blank means unrecorded. |
| [research/](research/) | The fact-check reports (RX-8 core, engine and cooling, OMP) and the Rocket League research record, with the evidence each correction rests on. |
| `tools/` | `build.ps1` (production-style build), `check_site.py` (links, anchors, headings, leaks, external URLs), `optimise_images.py` (WebP variants + `_data/images.yml`), `rlbot_maths_tests.py` (the Rocket League worked examples), `make_rlbot_charts.py` (draws the two RL charts). |

## Status vocabulary

- `todo`: not reviewed yet.
- `done`: reviewed and edited.
- `unchanged`: reviewed, no change needed.
- `wip-kept`: marked work in progress by the author; scope and maturity deliberately left as they were, only clear factual or presentation errors fixed.
- `blocked`: cannot be verified with the evidence available (reason given).

"Fact-checked" is only ever set after the underlying source was opened and read. Working links are not evidence.

## Local build (not part of the repository)

The machine had no Ruby. A scratch environment was set up in `%LOCALAPPDATA%\jb` (Ruby 3.2 + the `github-pages` gem, so Jekyll 3.10, matching the live build). The repository `Gemfile` and `Gemfile.lock` are untouched; see progress.md for the exact commands. Delete `%LOCALAPPDATA%\jb` and `C:\Ruby32-x64` to remove it.
