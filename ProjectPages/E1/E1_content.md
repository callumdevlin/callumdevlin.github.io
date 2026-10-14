---
title: MP1, Breathing-Apparatus Stowage
crumb: MP1 stowage
permalink: /ProjectPages/E1/
type: case-study
image: /Images/optimised/BA_Stowage_18-1200.webp
reviewed: 2026-10-14
description: >
  A push-to-stow cradle for breathing-apparatus cylinders in fire-appliance crew
  cabs, designed with Emergency One as a group project and checked with FEA against
  their 10 g requirement.
---

{% include figure.html src="/Images/BA_Stowage_18.png" alt="Render of three MP1 stowage stations mounted in a crew-cab seat bank, each holding a yellow breathing-apparatus cylinder" caption="Three MP1 stations in a crew-cab seat bank. Render." eager=true %}

MP1 is a stowage cradle for breathing-apparatus (BA) cylinders in the crew cab of a fire appliance. We designed it with Emergency One (E1) as a four-person industrial group project. One adjustable assembly replaces bespoke fixtures and holds either a single cylinder or a twin pack. It is meant to clamp when you push the cylinder in and to let go when you pull a handle in the seat.

This was a design and analysis project at university. I worked on it as one of four, so "we" below means the group. The design was checked by FEA against E1's crash requirement. It hasn't been crash-tested or certified, and I say where the evidence stops in [what the analysis shows](#what-the-analysis-does-and-doesnt-show).

## The brief

E1 needed a BA stowage solution that could:

- fit the existing cab integration space without rework to the vehicle structure
- support single and twin-pack formats without a unique bracket for each customer
- work with gloved hands in low visibility
- meet a **10 g crash requirement** for a cylinder of about 20 kg, which is a load of about 1,962 N (20 kg × 9.81 m/s² × 10)

Operating in full PPE means reduced dexterity and limited visibility, and the cylinder has to stay accessible for rapid egress and valve checks while docked.

## The space it has to fit

The envelope came from E1's cab CAD, where the allowable volume behind the seat is the green zone below. It is **256 mm wide, 735 mm high and 275 mm deep**. Taking it directly from the cab model meant the design could be installed without redesigning the cab, and the same logic should carry over to rear lockers. Depth is the controlling constraint, because of cab comfort and clearance around the seat and controls.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/GreenZone2.JPG" alt="CAD of a crew-cab seat bank with a green translucent volume marking the space available for one stowage station" caption="The green volume is the space available behind the seat for one station, from E1's cab CAD." %}
{% include figure.html src="/Images/GreenZone1.JPG" alt="CAD of a seated figure in the crew cab with the green stowage envelope behind the seat" caption="The same envelope seen from the side, with a seated figure for scale." %}
</div>

## How it works for the firefighter

The motion is a single push to stow:

1. Push the cylinder down into the dock. This is a gross-motor action.
2. The push plate retracts and guides the cylinder into position.
3. Curved side arms wrap around the cylinder and clamp it.
4. A rotary latch locks the mechanism.
5. A pull handle built into the seat releases the latch for quick removal.

The red parts are the ones the user touches, so they're easy to find in a dark cab. Direct access to the latch is kept as a manual override, as the client required.

## How it's built

### Back plate and sliding panels

The back plate bolts into E1's seat frame and is the primary load path. Two sliding front panels set the effective clamping width, so one backbone fits single and twin-pack formats. The panels can be pinned through pilot holes to stop them drifting.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/BA_Stowage_8.png" alt="Front view of the empty MP1 bracket: a dark back plate with two red sliding side panels, curved clamping arms and a lower spigot bracket" caption="The empty bracket from the front: back plate, red sliding panels and the spigot bracket at the bottom." %}
{% include figure.html src="/Images/Instruction-3.JPG" alt="Line drawing of the back plate with a red double-headed arrow between the two sliding panels, showing they move sideways" caption="The sliding panels move sideways on slots to set the clamping width." %}
</div>

### Clamping mechanism

The push plate is the input surface during stowage. A pair of curved arms clamps the cylinder from the sides, and torsion springs reset the mechanism to open after release so it always presents ready to stow. The aim was for clamp loads to be reacted into the back plate and seat frame rather than into plastics or trim.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/BA_Stowage_3.png" alt="Render of the MP1 mechanism from above: red back plate and sliding panels, curved black clamp arms and the spigot bracket at the base" caption="The mechanism without a cylinder, seen from above." %}
{% include figure.html src="/Images/BA_Stowage_6.png" alt="Close-up render of the clamp arm pivots, linkage bars and spring on the red sliding panel" caption="Close-up of the arm pivots, link bars and spring." %}
{% include figure.html src="/Images/Instruction-1.JPG" alt="Line drawing of the back plate with red arrows showing the curved clamp arms swinging inward when a cylinder is pushed in" caption="Clamping: pushing the cylinder in swings the arms around it." %}
</div>

### Locking and release

We chose a Southco R4 rotary latch with its matching catch, as an established automotive-grade part for repeated cycles and vibration. Release is a seat pull handle and cable, designed for gross-motor operation in PPE. Manual override access is kept so the mechanism is still serviceable if the cable fails, which was a client requirement.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/Instruction-4.JPG" alt="Sketch of a cylinder base beside a seat cushion, with a red arrow showing the pull handle lifting" caption="The seat-integrated pull handle lifts to release." %}
{% include figure.html src="/Images/Instruction-5.JPG" alt="Sketch of the latch with the release cable attachment circled in red and an arrow showing the cable pulling down" caption="The cable attachment at the latch (circled). Pulling the cable releases it." %}
</div>

### Vertical restraint

Side clamping controls lateral movement, but vehicle motion also gives vertical events from bumps, kerbs and braking pitch. The design uses two vertical controls. A bottom spigot carries the static weight and locates the cylinder base, and its height can be adjusted. A top stopper, made from an L-bracket with an elastomer bumper, prevents upward bounce and keeps the cylinder crown captured.

{% include figure.html src="/Images/Instruction-2.JPG" alt="Line drawing of the spigot bracket at the bottom of the back plate, with a red arrow showing it adjusts upward on slotted holes" caption="The spigot bracket adjusts in height on slotted holes." class="fig-medium" %}

### Materials and finish

- **Structure:** mild steel sheet, which is E1's standard stock and suits their in-house laser and brake-press capability. The sheet thickness is 3 mm on this page's earlier version and 4 mm in the operations manual, and I haven't resolved which is right (see the open items below).
- **Fasteners and springs:** stainless fasteners and torsion springs sized for reliable reset.
- **Contact surfaces:** nylon and rubber at wear points to reduce noise, impact and abrasion.
- **Finish:** powder coat, with red for user-actuated and moving parts.

## What the analysis does and doesn't show

We ran linear static FEA in SolidWorks on the main components, against the 10 g, 20 kg basis (1,962 N). The results are below, with what I can and can't tell from the saved reports.

| Component | Applied load | Peak von Mises stress | Peak displacement | Notes |
| --- | --- | ---: | ---: | --- |
| Back plate (V4.0) | See the note below | 398.8 MPa | 0.26 mm | Added formed bends cut the peak stress by about 30% against a flat plate |
| Main body, slide-to-back-plate interface | Not in the saved reports | 153.3 MPa | 0.075 mm | Weld areas around the pivot and latch brackets stay elastic |
| Clamping arms | 1,000 N (report) | 146 MPa | 0.93 mm at the tip | Peak at the inner curve |
| Top stopper | Not in the saved reports | 39.4 MPa | 0.5 mm | Bump event; some controlled compliance is intended |
| Spigot | Not in the saved reports | 1.98 MPa | 0.0087 mm | Static weight; intentionally stiff |

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/BA-FEA-2.JPG" alt="SolidWorks results for the back plate: a von Mises stress plot with a maximum of 3.988e8 N per square metre and a displacement plot with a maximum of 0.2647 mm" caption="Back plate results: peak von Mises stress 398.8 MPa and peak displacement 0.265 mm. The plots carry SolidWorks' educational-licence watermark." class="fig-narrow" %}
{% include figure.html src="/Images/BA-FEA-4.JPG" alt="SolidWorks results for the clamping arms: a stress plot with a maximum of 1.461e8 N per square metre and a displacement plot with a maximum of 0.9274 mm at the arm tips" caption="Clamping arm results: peak stress 146 MPa and 0.93 mm tip displacement for a 1,000 N load." class="fig-narrow" %}
</div>

These are indicative results, for four reasons:

- **The back-plate load.** The report records the load as −2,000 kgf, which is about 19.6 kN and ten times the 1,962 N used as the design basis. It may have been a deliberate conservative case or an entry error. I don't know which, so the 398.8 MPa is the stress at that applied load, not at the design load. Because the analysis is linear, the stress at 1,962 N would be about a tenth of it if the plate was loaded ten times too hard, but I haven't re-run it. The clamp-arm study used 1,000 N (the page used to say 981 N).
- **The material.** The stress plots mark a yield strength of about 620 MPa, which is an alloy-steel value, and the page's earlier "below UTS 724 MPa" is also an alloy-steel figure. The sheet we specified is mild steel, which typically yields at a few hundred MPa less. The results would need re-running with the actual material data.
- **Peak stresses.** A peak at a fixing or a corner is often a modelling artefact, and the saved reports don't show how the peaks were treated.
- **No test.** Nothing was physically tested. "Meets 10 g" isn't something this analysis can claim. It checks the design against a stated requirement.

**Fatigue.** The fatigue argument was a simple S–N check assuming four stow and release cycles a day for 15 years, which is 21,915 cycles (4 × 365.25 × 15). The stress values quoted are crash-load stresses rather than stresses in everyday service, and the endurance limit of about 327.5 MPa was an alloy-steel assumption, so it is a plausibility argument and not a fatigue analysis.

## Making it

The design was shaped to fit E1's existing fabrication workflow and to avoid special processes:

1. **Laser cut** the sheet components, nested for material efficiency.
2. **Brake press** the bends on the back plate, push plate and stopper bracket, with controlled radii.
3. **MIG weld** the pivot mounts, latch brackets and link connectors, with attention to bracket alignment.
4. **Powder coat** for corrosion resistance, durability and the red visual coding.
5. **Assemble**: arms, latch, springs, cable and sliders, set the width and pin it through the pilot holes.

## What it gives E1, and what it doesn't

The design is meant to standardise BA stowage across customer formats, reduce bespoke engineering and simplify quoting and build variance. It also aims to improve usability with gross-motor operation and clear touch points. It follows E1's naming as MP1 (Modular Pack 1), alongside their SP1 and SP2.

What it doesn't have: physical crash or fatigue testing, any certification, or evidence that E1 adopted it. The advertisement pack and operations manual we wrote for the project are in the links below. They are project documents. The advertisement pack's price and the manual's 12-month warranty are part of that exercise and aren't evidence of a commercial product.

## Open items

Where the project documents disagree, I've left it visible rather than choose.

- **Sheet thickness:** 3 mm on this page (from the original write-up) against 4 mm in the operations manual.
- **Size:** the cab envelope above is 256 × 735 × 275 mm. The manual lists the finished unit as 583 × 260 × 230 mm, labelled width × height × depth. Those labels look transposed (583 mm is probably the vertical size), and if 260 mm is the width it is 4 mm over the 256 mm cab width.
- **Load rating:** the manual gives a 35 kg maximum bottle weight, while the analysis basis is about 20 kg.
- **Cylinder compatibility:** the advertisement pack says it fits "most UK and European BA cylinder configurations". The manual gives a clamping width range of 150-250 mm and a height range of 450-500 mm. Which cylinder models that covers isn't recorded here.

## Documents

- [MP1 Operations Manual](/ProjectPages/E1/MP1%20Operations%20Manual.pdf) (PDF, 8 pages; credits the group of four on the cover)
- [MP1 Advertisement Pack](/ProjectPages/E1/MP1%20Advertisement%20Pack.pdf) (PDF, 6 pages)
