# Information only the author can supply

Nothing here has been estimated. Until you supply it, the public pages leave the field blank or say it is unrecorded.

## RX-8 car records (the short version is also in `ProjectPages/RX8/_research-todo.md`)

- Every coolant hose end diameter, spigot OD and centreline length measured on the car (the blank "My measurement" cells in the cooling hose table); the exact RHD heater-hose part numbers (H09-H11), which no catalogue I could open lists.
- Actual rebuilt-engine measurements from the build sheets (blank "My measurement" column on the engine page).
- Exact fitted starter part number and rating; exact Prosport gauge and R-Spec sender models.
- As-installed manual fan-switch wiring: wire colours, where it taps in, which relay-socket pins (photos). Whether the relay layout on your RHD car matches the left-hand-drive figure (positions 16, 19, 13).
- Sohn adapter: material, seal specification, dimensions, reservoir capacity (CAD/build records), reservoir position and head above the pump, hose bore and length, and whether you checked delivery at high rpm.
- Fuel-pump retaining clip CAD dimensions and longer-duration inspection results.
- Photographs: jack/support points, cooling drain, hose routes, PPF datum (dimension A), fuel-pump module, Sohn installation.
- The leading spark plug actually fitted (the notebook says RE7C-L is "probable"): a photo of a removed plug or the receipt.
- Wheel-nut socket size (the old "17 mm" looked wrong for M12 × 1.5; the column was removed); tyre pressure from the door placard; whether your tank figure of 61 L comes from the UK handbook.
- **Engine measurements to date:** your PCM calibration level and whether the car had the 4206F / TSB 01-014/08 reflash.
- `Images/RX8-JackPoints.jpg`: who drew it, or where it came from, so it can be credited correctly.

## Bench data (enginedata page)

The page now states these as open. Answers would let the delivery figures be trusted more, or replaced:

- What drove the pump's plunger (drive worm) on the bench, at what speed, and how that speed mapped to engine rpm for each table row.
- Whether mL/min is total for all four outlets (the OMP Lab's notes say total) or per outlet; how such small volumes were measured (0.15 mL/min over 30 s is 0.075 mL); resolution, repeats and uncertainty.
- Oil grade, temperature and inlet pressure on the bench; what "back-pressure not replicated" meant in practice.
- How the 1,000 rpm and 6,000 rpm rows were obtained when they aren't in the list of logged holds.
- Dyno, road or free-revving for the steady-state holds; load, coolant and intake temperature; duration of each hold; transducer range and calibration; whether pressure was before or after the filter.
- The sump oil used and its condition.

## MP1 (Group 12 IGP)

- Which parts of the design and analysis you personally did.
- The FEA reports: the back-plate load is recorded as 2,000 kgf (19.6 kN) against the 1,962 N basis. Deliberate conservative case or entry error? And the material model (the plots mark a 620 MPa yield, an alloy-steel value; the sheet is mild steel). Where the 398.8 MPa peak sits.
- Sheet thickness (3 mm in the original page, 4 mm in the operations manual) and the true overall dimensions (manual: 583 × 260 × 230 mm, labelled W × H × D).
- Whether any physical test was done, and whether E1 adopted the design.
- Permission to name the other three team members on the page (they are on the manual cover, already published).

## ToolSync

- What was built and tested: toolbox, SyncTag PCB, battery runtime, which Pi model, thermal logging.
- Photographs or CAD of the finished box and tag; whether the BEng report/folio can be linked.

## EnduraOMP

- Photographs of the built prototype (every image on the page is a CAD render).
- Numbers for the hydrocarbon comparison (units, run conditions), and the duration and pressure of the oil/coolant cross-leakage test.
- Whether the design report can be linked.

## Rocket League bot

- Whether the offset-approach, arc-line path, time estimator and aerial maths exist in a branch not in the public repository, and what each co-developer wrote. (The public snapshot cannot run as committed because `behaviours.py` is missing.)
- Confirm Daniel McMurray is happy to be named (the repository README already names him).
- `Images/rlbot-hero.jpg`: confirm it is your own screenshot. `Images/v_agraph.JPG` (a throttle-acceleration graph of unknown origin) is no longer used; if you want it back, say where it came from.
