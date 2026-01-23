---
layout: default
title: Mazda 13B-MSP
---
Links:
- [Torque Specifications]({% link ProjectPages/13BMSP/torquespecs.md %})
- [Engine Running Data]({% link ProjectPages/13BMSP/enginedata.md %})

## Introduction

I created this page to document my experiences with the 13B-MSP engine, share the knowledge I’ve gained, and help others who may be working on their own projects.
What sets the Renesis apart over previous variants is its improved efficiency and emissions compared to earlier rotary engines. It achieves this by relocating the exhaust ports to the side housings, reducing overlap between intake and exhaust cycles. This results in a more refined engine that still delivers the exhilarating experience rotary fans love.

## Teardown Findings & Diagnostics

- **Rear stationary gear bearing** was *burned out*; heat damage had **scored the eccentric shaft** out of spec.  
- **Rotor bearings** were also heat-affected; **copper shavings** found in the oil pan indicated severe bearing material loss.  
- **Rotor & seal organisation:** marked **rotors front/back**, then labelled corners **A–B–C** on one face and **X–Y–Z** on the other.  
  - **Side-seal pairing:** installed in a rotation pattern (**A→B, B→C, C→A**) to avoid putting a worn edge back into its original groove.  
  - Marked each **corner, side, and apex** to keep wear patterns traceable through cleaning and reassembly.
- **Housings:** small **chips on the exhaust edge**—acceptable since **no compression sealing** occurs there. Edges deburred; sealing surfaces intact.  
- **Irons (side housings):** slight **side-seal markings** noted but **still within spec**.  
- **Coolant jackets:** generally clean; **one jacket** showed **sand/corrosion build-up**—fully flushed/cleaned before reassembly.

## Cleaning & Carbon Removal

- **Carbon soak:** **kerosene** used to dissolve heavy carbon deposits (rotor crowns, exhaust edges, combustion surfaces).  
- **Residue wash:** followed with an **engine degreaser** to strip oily film and kerosene residue, then compressed-air dry and immediate light oiling on bare metal to prevent flash rust.  
- **Care points:** no abrasive pads on chrome surfaces; plastic or wooden scrapers only on sealing areas.

## Parts & Vendors (placeholders to fill)

| Component                          | Spec / Notes                                | Manufacturer / Source |
|-----------------------------------|---------------------------------------------|-----------------------|
| Full rebuild kit                  | Gaskets, O-rings, seals                     | *(-)*            |
| Apex seals                        | 2- or 3-piece, street reliability           | *(-)*            |
| Side seals + springs              | Clearance matched to irons                   | *(-)*            |
| Corner seals + springs            | Matched to apex/side setup                  | *(-)*            |
| Rotor bearings                    | New                                          | *(-)*            |
| Stationary gear bearings (front/rear) | New; rear failure replaced                | *(-)*            |
| Eccentric shaft                   | Polish or replace (depending on spec)       | *(-)*            |
| Front pulley                      | **HVAC delete** path                          | *(-)*            |
| Sohn adapter kit + lines          | OMP to premix reservoir                     | *(-)*            |
| Water Pump & hoses                | New; correct temp rating                    | *(-)*            |

## Rebuild Process (highlights)

1. **Inspection & Measurement**  
   - Checked rotor housing chrome (slight chipping), corner radii, and port edges.  
   - Verified **side-seal and apex-seal clearances**; set target cold clearances for hot stability.  
   - Measured **e-shaft endplay** and checked thrust surfaces.  
2. **Prep**  
   - Deburred seal grooves; flushed **oil and coolant galleries** thoroughly.  
   - Replaced all bearings; verified oil passage cleanliness.  
3. **Assembly**  
   - New **apex/side/corner seals** and oil control rings; new gaskets throughout.  
   - Followed factory torque sequence; checked rotor-to-housing drag at multiple clock positions.  
   - Used **Vaseline** on coolant seals to keep them in the housing during assembly, this stops them getting pinched.
4. **Pre-start**  
   - **Primed oil system** (plugs out/fuel off) and confirmed pressure.  
   - Pressure-tested and vacuum-filled coolant; bled thoroughly.

## Custom Modifications & Why

- **Custom Oil Control/Relief Regulator** — revised spring/seating elevates and stabilises **hot oil pressure** without over-pressurising seals.  
- **Front Pulley + AC Delete** — reduces belt length & idlers → **less friction**, cleaner layout, easier service.  
- **Sohn Adapters** — routes OMP to premix reservoir for **cleaner burn** and more consistent apex/side seal lubrication.  
- **Oil Pressure/Flow Tuning** — small idle increase plus regulator adjustment yield steadier hot idle pressure.  
- **Cooling Strategy** — fresh thermostat, good bleed, and smarter fan triggers to clamp temperature drift.

## Challenges & Tips

- **Bearing debris (copper) management:** pull and inspect oil jets and galleries; replace **all** compromised bearings.  
- **Side-seal clearancing:** don’t rush; repeated measure-fit-measure cycles pay off in idle quality and hot sealing.  
- **Coolant air pockets:** vacuum fill, heat-soak with heater on, cool, re-bleed—repeat until stable.  
- **Leak control:** correct sealant amounts on front cover/OMP; re-check after first heat cycles.
- **Organisation beats speed:** the A/B/C & X/Y/Z corner scheme keeps parts traceable and prevents mismatch.  
- **Thermal control = longevity:** cooling stability and steady oil pressure mattered more than any single performance mod.  
- **Prime first, fire later:** proper priming protects fresh surfaces and gives a trustworthy baseline pressure.