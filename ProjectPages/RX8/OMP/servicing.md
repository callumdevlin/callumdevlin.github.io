---
title: RX-8 OMP Removal, Installation & Servicing
permalink: /ProjectPages/RX8/OMP/servicing/
description: >
  How to remove, inspect, reinstall and prime the Series 1 RX-8 oil metering
  pump — tools, seals, the rebuild-vs-replace decision, and first-start checks.
---

This page covers how to approach removing, inspecting and reinstalling the Series 1 OMP safely, and what can realistically be serviced versus what should be replaced. Diagnose first — see [diagnostics & testing](/ProjectPages/RX8/OMP/testing/) — because many suspected pump failures turn out to be the position switch or wiring, and that's a much cheaper fix.

> **Caution:** the OMP sits in the engine's lubrication chain, so mistakes here can cost an engine. Exact torque values, sequences and part numbers must come from the workshop manual for your model year — this page deliberately describes method, not numbers, where the manual is the proper authority. If any of this is outside your comfort zone, hand it to a rotary specialist.
{:.note}

## Before You Start

**Tools:** standard metric sockets and spanners, a torque wrench covering low ranges accurately, flare/line spanners for the pipe unions, a pick set, clean lint-free rags, a parts tray, and labels or masking tape for the oil lines. A hand vacuum pump is useful for checking the nozzles while you're in there.

**Parts to have on hand:**
- New sealing washers for every banjo/connector bolt you disturb — these are single-use.
- A new OMP-to-front-cover O-ring/gasket.
- Fresh engine oil for priming.
- Optional but sensible while access is open: new oil nozzle O-rings.

**Safety:** engine cold, battery negative disconnected (this also means the PCM will re-run its OMP learning afterwards — that's expected), and absolute cleanliness. The metering circuit moves millilitres per minute through small drillings; a single fibre of rag in the wrong place is a blockage.

## Access & Removal

1. **Get access.** The OMP mounts to the engine front cover. Remove the intake tract components in the way until you have clear sight of the pump body, its electrical connector, and the oil pipe unions.
2. **Label everything.** Before disturbing any line, label each oil pipe with its port. The pipes route metered oil to specific nozzles — crossing them up changes which injection point gets what.
3. **Disconnect electrics.** Release the OMP connector and inspect it while it's apart (pins, corrosion).
4. **Crack the unions.** Loosen the connector/banjo bolts at the pump outlets. Expect a small amount of oil; have rags ready. Cap or bag the open pipe ends immediately — cleanliness again.
5. **Unbolt the pump.** Remove the mounting fasteners and withdraw the pump squarely from the front cover. The pump is driven from the eccentric shaft through a driven gear — note how the drive engages as it comes out, and don't force anything. Recover the old O-ring/gasket and make sure no fragment stays behind on the mating face.

## Inspection Once It's Out

- **Drive gear:** inspect the driven gear teeth for wear, chipping or debris.
- **Rotation:** the mechanical pumping elements should turn without grinding or binding.
- **Body:** check for cracks, especially around the mounting ears and unions, and varnish build-up around the inlet.
- **Stepper & switch:** with the pump on the bench this is the easiest time to repeat the [coil resistance and position switch checks](/ProjectPages/RX8/OMP/testing/) — and, if your diagnosis pointed at a confused position reference, to manually return the mechanism to its proper rest position so the PCM's initial-set can re-learn from a sane starting point.
- **Mating face:** clean the front cover face carefully. No gasket fragments, no scoring.

## Rebuild or Replace?

Honest answer: the Series 1 OMP is not officially a serviceable item — Mazda supplies it as a unit, and no internal seal kit exists. What *can* realistically be done:

- **Clean and reseal externally** — unions, mating O-ring, external surfaces. This plus a switch/reference fix resolves a large share of "failed" pumps.
- **Stepper or switch faults** — these are the common genuine failures, and on a bench they're diagnosable with a multimeter. Some owners successfully transplant or repair these; it requires care and good documentation of how the mechanism times together.
- **Internal wear of the pumping elements** — teardowns show precision compound pistons and sleeves with very small clearances. If the metering internals themselves are worn or scored, replacement (new or known-good used, *bench-tested before fitting*) is the sensible route. If buying used, test the stepper coils and switch before it goes anywhere near your engine.

## Installation

1. Fit a **new** O-ring/gasket, lightly oiled.
2. Offer the pump up squarely, engaging the drive — it should seat without force. If it stands proud, the drive isn't engaged; don't pull it down with the bolts.
3. Torque the mounting fasteners to the manual's specification.
4. Reconnect each labelled oil pipe with **new sealing washers**, and torque the union bolts to spec — these are small fasteners with low torque values, and overtightening distorts the sealing faces.
5. Reconnect the electrical connector until it clicks.

## Priming, First Start & Verification

This is the part people skip, and it's the part that protects your seals.

1. **Prime the circuit.** The metering lines and pump should not start dry. Fill the lines with fresh oil as far as practical when connecting them.
2. **Cheap insurance:** add two-stroke premix to the fuel tank for the first tank after OMP work. It backstops the injection system while the circuit fully purges. (Background on premix is on the [nozzles & premix page](/ProjectPages/RX8/OMP/nozzles-premix/).)
3. **First start.** Reconnect the battery. At key-on/start the PCM runs its initial-set (reversing the stepper 60 steps to find zero) and then its monitor function. Start the engine and let it idle — no load, no revs.
4. **Check for leaks** at every union you disturbed, cold and again after warm-up.
5. **Verify control.** Confirm no DTCs are set, and ideally watch `MOP POS` in Forscan rise progressively with RPM ([expected values here](/ProjectPages/RX8/enginedata/)).
6. **Watch consumption.** Over the following weeks, confirm the engine is consuming oil at a normal rate. Consumption is the end-to-end proof the system is delivering.

*Next: [oil nozzles, premix and clean oil feed systems](/ProjectPages/RX8/OMP/nozzles-premix/).*
