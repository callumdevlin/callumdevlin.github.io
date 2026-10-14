# Page inventory

Columns: **Content** = rewritten/edited for voice, structure and accuracy of wording. **Facts** = technical claims checked against sources that were actually opened (see ledger.md and research/). **Visual** = loaded in a browser and measured at 375, 768, 1280, 1600 and 2560 px (no horizontal overflow on any page); sampled by eye at desktop. See README.md for the status vocabulary.

Last updated: 2026-10-14, end of batch 5. 38 published pages (33 existing, all revised; 5 new: search, PCM terminals and codes, coordinates and units, steering, behaviours and testing), 2 lab apps (unchanged), 2 PDFs (unchanged) and one unpublished to-do file. Everything below has a recorded outcome.

Key to **Facts**: `checked` = sources opened and read, corrections applied; `partial` = checked, but named items remain OPEN or need the owner; `own data` = the author's measurements, checked for internal consistency only; `n/a` = no technical claims.

## Site pages

| Source | Output URL | Type | WIP | Content | Facts | Visual | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `index.markdown` | `/` | home | no | done | n/a | done | Rewritten: real images, cards, search box. No stats or slogans. |
| `about.markdown` | `/about/` | about | no | done | checked | done | Only facts already on the site; no new claims about employers, dates or qualifications. |
| `404.html` | `/404.html` | utility | no | done | n/a | done | Links back into the site. |
| `search.md`, `search.json` | `/search/`, `/search.json` | utility | no | done (new) | n/a | done | Client-side; indexes `search: true` pages only (all of ProjectPages plus About). |
| `ProjectPages/index.markdown` | `/ProjectPages/` | index | no | done | checked | done | "Crash-rated", "universal", "closed-loop" removed. |

## Engineering case studies

| Source | Output URL | Type | WIP | Content | Facts | Visual | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ProjectPages/E1/E1_content.md` | `/ProjectPages/E1/` | case study | no | done | partial | done | Group project ("we"). FEA results labelled indicative; load/material/thickness/size conflicts shown as open items (ledger C-001..C-007, C-012..C-014). |
| `ProjectPages/EnduraOMP/index.md` | `/ProjectPages/EnduraOMP/` | case study | no | done | partial | done | All images are CAD renders and are captioned as such; "closed-loop" and "validation" wording corrected; oil comparison described as a lubricant/feed comparison. |
| `ProjectPages/rfidtoolstorage/rfidtoolstorageoverview.md` | `/ProjectPages/rfidtoolstorage/` | case study | no | done | partial | done | Runtime marked as a calculated best case; Pi thermal limits corrected from Raspberry Pi docs. Build/test status unknown (owner-input.md). |
| `ProjectPages/E1/MP1 Operations Manual.pdf` | `/ProjectPages/E1/MP1%20Operations%20Manual.pdf` | download | no | n/a | historical | n/a | Unaltered. |
| `ProjectPages/E1/MP1 Advertisement Pack.pdf` | `/ProjectPages/E1/MP1%20Advertisement%20Pack.pdf` | download | no | n/a | historical | n/a | Unaltered. |

## RX-8 notebook

| Source | Output URL | Type | WIP | Content | Facts | Visual | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ProjectPages/RX8/index.md` | `/ProjectPages/RX8/` | index | growing | done | n/a | done | Added symptom finder and "still to fill in". |
| `ProjectPages/RX8/quick-reference.md` | `/ProjectPages/RX8/quick-reference/` | reference | growing | done | checked | done | Oil pressure 500 → 350 kPa; brake fluid DOT 3/4; diff oil SAE 90; fuel pressure condition; plug record. |
| `ProjectPages/RX8/torquespecs.md` | `/ProjectPages/RX8/torquespecs/` | reference | growing | done | checked | done | Rebuilt row by row: pulley bolt 254-294, rack bolts, oil pan Type A, decimals, thread conditions. Socket sizes removed (unverifiable). |
| `ProjectPages/RX8/terminals-and-codes.md` | `/ProjectPages/RX8/terminals-and-codes/` | reference | growing | done (new) | checked | done | Lookup built only from values verified on other pages. |
| `ProjectPages/RX8/enginedata.md` | `/ProjectPages/RX8/enginedata/` | measured data | no | done | own data | done | Confidence language aligned with the OMP Lab's notes; method gaps stated. |
| `ProjectPages/RX8/compression-testing.md` | `/ProjectPages/RX8/compression-testing/` | procedure | wip-kept (Devlin Rotary tester) | done | checked | done | |
| `ProjectPages/RX8/engine-removal-and-rebuild.md` | `/ProjectPages/RX8/engine-removal-and-rebuild/` | procedure | growing | done | checked | done | Reassembly reordered to Mazda's order; Type A vs B; apex-groove conflict; end-play maximum removed; top lift labelled as my practice. |
| `ProjectPages/RX8/cooling/index.md` | `/ProjectPages/RX8/cooling/` | reference | growing | done | partial | done | Hose register evidence-based; RHD heater hoses unresolved; dimensions blank where unsourced. |
| `ProjectPages/RX8/cooling/manual-fan-switch.md` | `/ProjectPages/RX8/cooling/manual-fan-switch/` | wiring note | growing | done | checked | done | New explanatory schematic (not an installation diagram); P0480/P0481 corrected; common 5AD wire; after-cooling. |
| `ProjectPages/RX8/fuel-ignition-and-starting.md` | `/ProjectPages/RX8/fuel-ignition-and-starting/` | reference | growing | done | partial | done | Broken image removed; Mazda module-removal rules added; D585/vendor page unverifiable. |
| `ProjectPages/RX8/drivetrain.md` | `/ProjectPages/RX8/drivetrain/` | reference | growing | done | checked | done | Broken image removed; Super-LSD figures removed (unsourced); calculated road-speed table added. |
| `ProjectPages/RX8/chassis.md` | `/ProjectPages/RX8/chassis/` | reference | growing | done | checked | done | Disc size tied to suspension; DOT 3/4; bleed order labelled as inference. Jack-point image source to confirm (owner-input.md). |
| `ProjectPages/RX8/sohn-adapter.md` | `/ProjectPages/RX8/sohn-adapter/` | own build | wip-kept | done | partial | done | Component record kept blank ("Not yet recorded"). Premix vendor text only via retailer copies. |
| `ProjectPages/RX8/acceleration-lab.md` | `/ProjectPages/RX8/acceleration-lab/` | lab host | no | done | n/a | done | Shared embed include; lab loads and sizes itself. |
| `ProjectPages/RX8/OMP/index.md` | `/ProjectPages/RX8/OMP/` | index | no | done | checked | done | |
| `ProjectPages/RX8/OMP/how-it-works.md` | `/ProjectPages/RX8/OMP/how-it-works/` | explainer | no | done | checked | done | Fail-safe timing/injection wording, TSB/recall wording, 3,000-3,300 rpm report. |
| `ProjectPages/RX8/OMP/testing.md` | `/ProjectPages/RX8/OMP/testing/` | procedure | no | done | checked | done | Owner-thread attributions corrected. |
| `ProjectPages/RX8/OMP/servicing.md` | `/ProjectPages/RX8/OMP/servicing/` | procedure | no | done | checked | done | |
| `ProjectPages/RX8/OMP/nozzles-premix.md` | `/ProjectPages/RX8/OMP/nozzles-premix/` | reference | no | done | partial | done | Engine Builder bulletin could not be opened (stated). |
| `ProjectPages/RX8/OMP/lab.md` | `/ProjectPages/RX8/OMP/lab/` | lab host | no | done | n/a | done | States the 23 vs 6.5 mL/min disagreement. |
| `ProjectPages/RX8/_research-todo.md` | (not published) | internal | n/a | updated | n/a | n/a | `published: false` and underscore name. |

## Rocket League notes

| Source | Output URL | Type | WIP | Content | Facts | Visual | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ProjectPages/rlbot/index.md` | `/ProjectPages/rlbot/` | index | growing | done | checked | done | States what the public repo contains and the RLBot version. |
| `ProjectPages/rlbot/overview.md` | `/ProjectPages/rlbot/overview/` | explainer | growing | done | checked | done | Group authorship; v4/v5; honest status. |
| `ProjectPages/rlbot/coordinates-and-units.md` | `/ProjectPages/rlbot/coordinates-and-units/` | maths | growing | done (new) | checked | done | Handedness verified by test. |
| `ProjectPages/rlbot/vectors.md` | `/ProjectPages/rlbot/vectors/` | maths | growing | done | checked | done | `ang_to` failure cases tested; template credited. |
| `ProjectPages/rlbot/steering.md` | `/ProjectPages/rlbot/steering/` | maths | growing | done (new) | checked | done | Pursuit simulation reproduced independently. |
| `ProjectPages/rlbot/ground-kinematics.md` | `/ProjectPages/rlbot/ground-kinematics/` | maths | growing | done | checked | done | Units and gravity sign fixed; own chart replaces unattributed graph. |
| `ProjectPages/rlbot/movingpath.md` | `/ProjectPages/rlbot/movingpath/` | analysis | wip-kept | done | checked | done | "Order of a kilometre" corrected (11 m); arc-line and estimator tested. |
| `ProjectPages/rlbot/aligning-shots.md` | `/ProjectPages/rlbot/aligning-shots/` | maths | wip-kept | done | checked | done | Labelled as design, not in public repo. |
| `ProjectPages/rlbot/aerial-kinematics.md` | `/ProjectPages/rlbot/aerial-kinematics/` | maths | wip-kept | done | checked | done | **Formula corrected** (verified numerically). |
| `ProjectPages/rlbot/behaviours-and-testing.md` | `/ProjectPages/rlbot/behaviours-and-testing/` | explainer | growing | done (new) | checked | done | |

## Interactive labs (built bundles)

| Source | Output URL | Type | WIP | Content | Facts | Visual | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tools/rx8-omp/` | `/tools/rx8-omp/` | lab | no | unchanged | cross-checked | done | Loads, sizes itself in the host page, chart renders. No change to calculations (sources are outside this repo and Node is not installed). |
| `tools/rx8-acceleration/` | `/tools/rx8-acceleration/` | lab | no | unchanged | cross-checked | done | As above. Checked in the lab's source (params.ts): the 231 PS six-speed uses the notebook's ratios, 4.444 final drive and 225/45R18 (0.32985 m radius = 659.7 mm diameter). |

## Assets

| Item | Outcome |
| --- | --- |
| `Images/*` (34 originals) | Untouched. `Images/optimised/` holds 69 WebP variants; `_data/images.yml` records dimensions. |
| Unreferenced images | `blackh.jpg`, `fullboard.JPG`, `greenglassC2da.png`, `magnet_schematic.jpg`, `timinglightschematic.jpg` (Arduino gauge/ECU schematics from the removed go-kart pages), `enduraomp-gauge.webp` left unused. Not deleted. |
| `assets/rx8/generated/*.svg` | 3 used (waveform, fan logic, Sohn path) and captioned as schematics or synthetic; `gear-speed-curves.svg` and `shift-rpm-drop.svg` unreferenced (numbers re-derived and correct). |
| `assets/rx8/diagrams/manual-fan-override-concept.svg` | New, explanatory only. |
| `assets/rlbot/*.svg` | New, drawn by `tools/make_rlbot_charts.py` from the tested constants. |
