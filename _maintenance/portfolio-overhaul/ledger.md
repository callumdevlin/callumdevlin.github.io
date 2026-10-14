# Research and corrections ledger

One row per consequential claim or correction. **Evidence** says what was actually opened and read; "I opened it" means I read the underlying page myself, "report" means a research agent did and its report is in `research/`. All source access dates are **2026-10-14** unless stated. Evidence of what the author did (project history) is kept apart from evidence that an engineering statement is correct.

Verdicts: CORRECTED (page changed to the source), QUALIFIED (claim kept, wording narrowed), OPEN (unresolved, with a way to verify), OWNER (needs the author's data).

The three RX-8 reports hold roughly 190 claim-level verdicts (`research/rx8-core.md`, `rx8-engine-cooling.md`, `rx8-omp.md`); this ledger records the ones that changed the site. Mazda figures are from the 2003 European (UK/LHD-labelled) workshop manual mirror at foxed.ca, not a 2005 UK RHD edition; running changes may differ.

## Case studies

| ID | Page / claim | Evidence | Applicability | Action | Unresolved / how to verify |
| --- | --- | --- | --- | --- | --- |
| C-001 | MP1 "crash-rated", "verified structure" | Page's own basis: FEA at 1,962 N (10 g × ~20 kg). Operations manual p.3/8 gives a 35 kg maximum. No test report or certification in repo. | Group 12 IGP | QUALIFIED: FEA check against E1's 10 g requirement; "crash-rated"/"verified" removed | A physical test would be needed to claim more |
| C-002 | MP1 "below UTS 724 MPa" with 3 mm mild steel | 724 MPa is an alloy-steel value. The FEA plot marks a 620 MPa yield (I opened BA-FEA-2.JPG), also an alloy-steel value | MP1 | QUALIFIED | FEA material data (OWNER) |
| C-003 | MP1 thickness 3 mm vs 4 mm | Operations manual p.8 says 4 mm | MP1 | OPEN, shown on page | Build drawings |
| C-004 | MP1 envelope 256×735×275 vs manual 583×260×230 (W×H×D) | Manual labels look transposed; 260 mm would exceed 256 mm | MP1 | OPEN, shown on page | Drawing |
| C-005 | MP1 "universal" | Ad pack: "fits most UK and European BA cylinder configurations"; manual 150-250 mm width, 450-500 mm height | MP1 | CORRECTED: "adjustable" | Cylinder models |
| C-006 | MP1 authorship | Manual cover credits four students | MP1 | CORRECTED ("we") | Personal contribution (OWNER) |
| C-007 | MP1 fatigue | 21,915 = 4 × 365.25 × 15 ✓. The stresses quoted are 10 g crash stresses, endurance limit an alloy-steel assumption | MP1 | QUALIFIED | |
| C-008 | ToolSync 13.9 h runtime | 12.8 Ah × 12 V = 153.6 Wh ÷ 11 W = 13.96 h; ideal, ignores converter loss, usable capacity, sag | Pack voltage assumed 12 V | QUALIFIED (calculated best case) | Measured runtime (OWNER) |
| C-009 | ToolSync Pi "below 85 °C prevents throttling" | Raspberry Pi docs (I opened): 85 °C limit on all models; Pi 4 throttles progressively from 80 °C; Pi 3B+ soft limit 60 °C | Pi model unrecorded | CORRECTED | Which Pi (OWNER) |
| C-010 | ToolSync built vs designed | No report or photos supplied | ToolSync | QUALIFIED; page says build/test status isn't itemised | OWNER |
| C-011 | EnduraOMP "closed-loop" | Page describes sensor inputs driving a calibrated flow map; no flow measurement of delivered oil | MEng | CORRECTED to "electronically controlled" | Report/design record |
| C-012 | MP1 back-plate load | BA-FEA-1.JPG (I opened it): applied force −2,000 kgf, reaction resultant 19,613.2 N, ten times the 1,962 N basis | MP1 | QUALIFIED, stated on page (stress is at that load; not re-run) | Owner to say if deliberate or an entry error |
| C-013 | MP1 clamp-arm load | BA-FEA-3.JPG: 1,000 N normal force (page said 981 N). Results 146.1 MPa and 0.927 mm match the page | MP1 | CORRECTED to 1,000 N | |
| C-014 | MP1 FEA plots carry the "SolidWorks Educational Product, instructional use only" watermark | BA-FEA-2/4.JPG | MP1 | Noted in caption | |
| C-015 | EnduraOMP images | I opened all of them: every one is a CAD render | MEng | CORRECTED: captioned as renders; note says no photos of the prototype yet | Prototype photos (OWNER) |
| C-016 | EnduraOMP oil comparison | Bio-ester oil via external feed vs 10W-30 baseline: tests the oil and feed, not the pump; no numbers on page | MEng | QUALIFIED | Numbers (OWNER) |
| C-017 | EnduraOMP stock delivery map | Delivery figures are the same rough, total-flow, unvalidated numbers the OMP Lab's CALIBRATION notes describe; the lab's derived estimate is 23.4 mL/min at step 47 / 9,500 rpm against 6.46 | | QUALIFIED on EnduraOMP, enginedata, OMP Lab pages | Controlled bench run |

## RX-8 corrections

| ID | Page / claim | Evidence | Action |
| --- | --- | --- | --- |
| R-001 | Oil pressure 500 kPa "high-power" | Mazda oil pressure inspection (I opened): 350 kPa at 3,000 rpm, oil 100 °C, no standard/high split; relief valve 441-490 kPa. My own logged cruise pressure (~3.4 bar) agrees. | CORRECTED to 350 kPa |
| R-002 | Pulley lockbolt 300-340 N·m | Mazda engine assembly (I opened): 254-294 N·m, oil on threads, silicone on the seat | CORRECTED |
| R-003 | Flywheel locknut "red Loctite", 54 mm | Report: Mazda EC manual says silicone sealant on the threads; no Loctite, no size | CORRECTED; size dropped |
| R-004 | Oil pan "upper block" 18.6-25.5 N·m | Report (engine manual 00-00-12, 01-10-4): upper pan is Type B only (2009 MY US VIN); a 2005 UK car is Type A, single pan 8.8-11.8 | CORRECTED |
| R-005 | Apex-groove clearance "older vs revised" | Report: the Oct 2008 manual prints 0.042-0.101 (01-10-16) and 0.042-0.077 (01-50-1) | CORRECTED: conflict shown |
| R-006 | End-play maximum 0.10 mm | Report: Mazda gives 0.04-0.09 only | CORRECTED (maximum removed) |
| R-007 | Reassembly order | Report: spacer, regulator/gear/seal, flywheel and end-play measurement were out of Mazda's order | CORRECTED: page follows Mazda's order |
| R-008 | Brake fluid "DOT 3" | Mazda air bleeding (I opened): European/UK spec DOT3 or DOT4 | CORRECTED |
| R-009 | Differential oil 80W-90/75W-90 | Mazda differential oil (I opened): SAE 90 only, GL-5, 1.2-1.4 L | CORRECTED |
| R-010 | Steering rack bolts 88 N·m; tie-rod nut rows | Report: 74.4-104.8; Mazda's own pages disagree on the tie-rod locknut (37.0-49.0 vs 68.6-98.0) | CORRECTED; conflict shown |
| R-011 | Fuel pressure "running" | Report: Mazda test is engine stopped, ignition on, pump run via F/P | CORRECTED |
| R-012 | Front disc 323 mm "high-power" | Report: Mazda keys 303/323 mm to standard/sport suspension | CORRECTED |
| R-013 | Super-LSD "bias 2.0, initial torque 49 N·m", "no friction modifier" | Report: not in any page opened; manual says only "low torque bias ratio" | CORRECTED: removed |
| R-014 | Engine mass ~120 kg | Report: Mazda gives none; secondary figures 112-138 kg | QUALIFIED |
| R-015 | Fan page | Report: after-cooling runs fans with ignition off; P0480/P0481 are continuous monitors, MIL does not light; relays 2/3 terminal-E wires join at 5AD; motor currents are a bench test | CORRECTED |
| R-016 | Hose register | Report: part numbers from Atkins/Mazdatrix; one connecting pipe N3H2-15-190; H07/H08 feed/return reversed (forum moderators); RHD heater hoses H09-H11 unresolved; dimensions only Dayco 72615/71766, Gates 23059, UK used-hose ODs | CORRECTED; dimensions blank where unsourced |
| R-017 | OMP fail-safe | Report: one 4.88° CA value for leading and trailing; injection has an "at engine start: regular control" row; "charging efficiency" is not Mazda's wording | CORRECTED |
| R-018 | OMP owner-thread claims | Report: "30° after refit" was a deliberate full-travel move; "trained technician" was "for training"; 3,000-3,500 rpm confirmed only as 3,000-3,300; 1,132 Ω fix was "5 miles so far"; sump-rise claim unsupported | CORRECTED / softened |
| R-019 | TSB 01-014/08 and recall 4206F | Report: TSB is a lack-of-power/hot-weather bulletin (14/17 March 2008) with two possible causes; 4206F letter not opened | CORRECTED / QUALIFIED |
| R-020 | Premix table | Arithmetic ✓ except 50 L high rate 195.3 mL (page said 196); vendor page blocked; Mazdatrix and ARD copies differ; Racing Beat dose ≈1:77; UK club ratios are my conversions | CORRECTED / QUALIFIED |
| R-021 | KEMSO module | Report: Mazda's rules (drain to half, lock-ring method 50-140° and 80-135 N·m, leak check) were missing; D585 vendor page unopenable (TLS) | CORRECTED / QUALIFIED |
| R-022 | Torque page sizes, stopper screw, upper-pan row | Socket sizes not Mazda's (wheel nut 17 mm looked wrong); stopper screw 3.2-4.7 confirmed in the Oct 2008 engine manual | Sizes removed; stopper kept |
| R-023 | enginedata | "Same idle" wrong (1,290 vs 820 rpm); ratio 2.77; 1,000/6,000 rpm rows not in the hold list; pressure was taken in the filter gallery, not at the pump inlet | CORRECTED; method gaps stated |
| R-024 | Chassis | Mazda bleed order is master cylinder first and last, furthest caliper first; the LR-RR-LF-RF wheel order is my inference | QUALIFIED |

## Rocket League

| ID | Page / claim | Evidence | Action |
| --- | --- | --- | --- |
| L-001 | Aerial formula `2/(T-dt)^2 (P - x0 - v0 dt - 1/2 g dt^2 z)` | Derived and simulated (`tools/rlbot_maths_tests.py`): the printed form misses by 1,490+ uu; `2/(T-t_b)^2 (P - x0 - v0 T - 1/2 g T^2 z)` lands within 0.001 uu. Agrees with Mish's aerial_hit write-up | CORRECTED |
| L-002 | "Minimum radius near the cap is on the order of a kilometre" | RLUtilities curvature table: 1,136 uu = 11.4 m; 145 uu = 1.45 m at rest | CORRECTED |
| L-003 | `ang_to` "returns 0 to π" | Raises on zero vectors and on cos = 1.0000000000000002 (about one in five exactly parallel random pairs in my test); unsigned | CORRECTED |
| L-004 | Bot implements offset point, arc-line, estimator, aerials | Report: none of it is in the public repo; `behaviours` module missing; template classes credited to RLBotPythonExample (MIT); README credits two developers | CORRECTED: labelled illustrative, "we", credit added |
| L-005 | Ground page units line and gravity sign | accelerations are uu/s²; along-facing gravity term is −g(f·z) | CORRECTED |
| L-006 | Ball radius 92.75 | Older docs/template 92.75; current docs/RocketSim 91.25 | Both stated |
| L-007 | Framework version | PyPI `rlbot` 1.x = RLBot v4; v5 pre-release, different API | Stated on index and overview |
| L-008 | Hero image alt text | Image is an in-game screenshot with no debug lines | CORRECTED |
| L-009 | Unattributed throttle graph | Provenance unknown | Replaced by `assets/rlbot/throttle-acceleration.svg` drawn from the tested constants |
| L-010 | Pursuit and ETA numbers | Independently re-simulated; match the agent's figures exactly | Used |

## Site / configuration

| ID | Item | Evidence | Action |
| --- | --- | --- | --- |
| S-001 | `remote_theme` tracks branch `v9` | `git ls-remote`: `v9` is a branch; tag `v9.2.1` exists; live site renders 9.2.1 | Pinned to `@v9.2.1` |
| S-002 | Search not in Hydejack free | No search include in the v9.2.1 source | Built a small client-side search |
| S-003 | Empty right gutter | Measured on the live site; theme centres content and reserves the gutters for its own contents box | Fixed with the documented `_data/variables.yml` widths plus a contents rail |
| S-004 | Dark mode | The free edition's compiled CSS has no `prefers-color-scheme` rules | Not available; not claimed |
| S-005 | Breadcrumb contrast | Theme grey #777 is 4.48:1 on white | Darkened to #666 (5.7:1) |
| S-006 | Stray scrollbar on display maths | MathJax's hidden accessibility copy inflates the theme's overflow box | Hidden with one CSS rule |
| S-007 | `jekyll-feed` | No posts, so the feed was empty | Removed from plugins |
| S-008 | Stale `Gemfile.lock` | Locks Jekyll 4.3.2 + hydejack 9.1.6 and lacks `github-pages` | Left untouched (production uses GitHub's builder); noted |
