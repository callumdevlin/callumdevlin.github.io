---
layout: default
title: MP1 — Modular Breathing Apparatus Stowage
---

[View the MP1 Advertisment Pack](/ProjectPages/E1/MP1%20Advertisement%20Pack.pdf)

# MP1 — Modular Breathing Apparatus (BA) Stowage

A universal, **modular** stowage system for SCBA/BA kits designed with Emergency One (E1).  
The MP1 replaces bespoke, one-off fixtures with a configurable assembly that fits **single cylinders and twin-pack systems** while meeting ergonomics and crash-load requirements.

## Design Envelope & Constraints

- **Cab integration envelope:** **256 mm (W) × 735 mm (H) × 275 mm (D)**, derived from E1 cab CAD (“green zone”) so installation is drop-in compatible. Targeting the cab envelope allows easy adaptation for rear lockers as well. *See the cab “green zone” CAD in Figure 1.* 

- **Use context:** tight cab clearances; operation in full PPE (low dexterity/visibility); rapid egress; valve access while docked. **Shallow depth is the controlling constraint**; width/height are more forgiving.:contentReference[oaicite:2]{index=2}

- **Crash requirement:** withstand **10 g** with a ~**20 kg** cylinder (≈**1962 N** equivalent load in tests).

## System Architecture (what’s in the design)

- **Back plate & sliding front panels** — structural spine that bolts to E1’s seat frame; two **sliding panels** set the clamping width for single or twin-pack kits.

- **Side-clamping, hands-free mechanism** — user pushes the BA into the dock; the **push plate** retracts and **pair of curved clamping arms** wrap the cylinder(s); a **Southco rotary latch** locks the arms. **Torsion springs** reset the mechanism open.

- **Vertical restraints** — **spigot** at the base carries static weight; **top stopper** (L-bracket + bumper) prevents upward “bounce” over rough terrain.

- **Release & override** — **seat-integrated pull handle** connected by cable for quick release; manual access to the latch for emergency override is preserved. Controls are **colour-coded red** for visibility in the cab.

### Locking & Release
- **Locking:** **Southco R4 rotary latch** + matching catch — automotive-grade, stress-tested component; the hook mounts to rear of the push plate.
- **Release:** **seat pull-handle** (cable) for fast, gross-motor actuation in PPE; **manual override** access retained per client safety requirement.

### Bottle Restraints (Vertical Control)
- **Bottom spigot:** carries static weight; bracketed to the back plate.  
- **Top stopper:** L-bracket + elastomer bumper; captures the crown of the cylinder to stop upward movement.

## Materials & Finish

- **Structure:** **3 mm mild steel sheet** (E1 standard stock) — balances strength, cost, and manufacturability on E1’s **laser + brake-press** lines.
- **Fasteners & springs:** stainless fasteners; torsion springs sized for repeatability and reset force margins.  
- **Bumpers:** nylon/rubber stoppers at contact points to control impact/wear.  
- **Finish:** **powder coat**; **red** for user-actuated parts (handle, moving arms) to increase discoverability in dark cabs.

## Structural Performance (FEA highlights)

**Global requirement:** survive **10 g** crash events and daily operational shocks.

- **Back plate (V4.0):**  
  Max stress ≈ **398.8 MPa** (< UTS 724 MPa); peak **deflection ~0.26 mm**. V4 bends cut peak stress by **≈29.7%** vs flat plate.

- **Main body assembly:**  
  Max stress ≈ **1.533×10⁸ N/m²** at slide-to-back-plate interface; **deflection ~0.075 mm**; welds at pivot/latch brackets remain elastic.

- **Top stopper & spigot:**  
  Stopper max stress ≈ **3.94×10⁷ N/m²**, deflection ~**0.5 mm** under bump; spigot max stress ≈ **1.98×10⁶ N/m²**, deflection ~**0.0087 mm** under static weight — **ample margin**.

- **Clamping arms:**  
  Max stress ≈ **1.46×10⁸ N/m²** at inner curve; tip **deflection ~0.93 mm** under half-side load (**981 N**), acceptable with latch engagement and dual link bars.

### Fatigue Life (S-N based)
- **Main body:** with operational stress ≈ **1.533×10⁸ N/m²** and daily cyclic events (top/bottom hits, braking pulls), life **exceeds 15 years**; stresses stay below **~327.5 MPa** endurance limit (assumed for alloy steel).
- **Clamping mechanism:** ~**21,915 cycles** (4 open/close per day × 15 yrs) → **> life target**, only sub-millimetre tip deformation expected; no critical fatigue hot-spots.

## Manufacturing & Assembly (DfMA)

1. **Laser cut** all steel parts from 4 mm sheet; nests yield efficient material use.  
2. **Brake-press bends** on back plate, push plate, and stopper bracket (controlled radii to avoid cracking).  
3. **MIG weld** pivot mounts, latch brackets, and link connectors (QA for penetration/position).  
4. **Powder coat** for corrosion/wear resistance and part identification.  
5. **Final assembly:** build main body + clamping module on the back plate; fit springs, latch, cable; set sliding panels to kit width; pin via **pilot holes** to prevent drift. 

## Human Factors

- **Gross-motor release** (seat handle) avoids fine motor actions in PPE.  
- **Valve access** preserved for in-vehicle checks.  
- **Vertical orientation** avoids “submarining” under crash loads.  
- **Shallow depth** prioritised for cab comfort; red touch-points improve discoverability.

## Integration & Naming

The product integrates with E1’s existing seat mounts and naming convention: **MP1 (Modular Pack 1)**, complementing SP1/SP2. Sliding panels + spigot allow **single or twin-pack** kits without bespoke re-engineering, improving standardisation across fleets. 