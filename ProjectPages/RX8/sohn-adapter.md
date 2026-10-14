---
title: Custom RX-8 Sohn Adapter and Separate OMP Oil Supply
crumb: Sohn adapter
permalink: /ProjectPages/RX8/sohn-adapter/
type: reference
section: rx8
nav_order: 9
status: wip
applies: My own build on a Series 1 RX-8. The component record is deliberately left blank until I can fill it from the CAD and build records.
reviewed: 2026-10-14
description: >
  The custom front-cover adapter and separate reservoir oil path, with priming,
  checks and premix dose conversions.
related:
  - /ProjectPages/RX8/OMP/nozzles-premix/
  - /ProjectPages/RX8/enginedata/
  - /ProjectPages/EnduraOMP/
---

This adapter keeps the factory Series 1 electronic OMP and its four metering pipes and nozzles. It changes only the pump inlet: instead of drawing engine oil through the front cover, the OMP draws clean two-stroke oil from a dedicated reservoir.

## Oil paths

| Arrangement | Path |
| --- | --- |
| Factory | Engine sump → front-cover drilling → factory OMP → four pipes/nozzles → engine |
| Modified | Separate vented reservoir → oil-resistant supply hose → custom front-cover adapter → factory OMP → four pipes/nozzles → engine |

{% include figure.html src="/assets/rx8/generated/sohn-oil-path.svg" alt="Block diagram comparing the factory oil path, from the sump through the front cover to the OMP and four nozzles, with the modified path from a vented reservoir through the adapter to the same OMP and nozzles" caption="The factory and modified oil paths. A schematic of the arrangement, not a drawing of the adapter." class="fig-medium" %}

The machined/printed interface sits between the Series 1 front cover and the OMP, closes the original sump-oil feed and presents a separate inlet to the pump. The OMP stays in its factory location with its drive and electrical control unchanged.

## Component record

| Field | Record |
| --- | --- |
| Adapter material | Not yet recorded |
| Front-cover/OMP seal type | Not yet recorded |
| Interface and port dimensions | Not yet recorded |
| Reservoir capacity | Not yet recorded |
| Pump and control | Factory Series 1 electronic OMP and PCM strategy |
| Delivery | Four factory metering pipes and nozzles |
| Oil | Renewable Lubricants Bio-Rotary Racing Premix |

These fields stay blank until I fill them from the CAD and build records. A useful drawing of this part has to show the original front-cover feed closure, the new inlet, pump-drive clearance, sealing faces and fitting engagement, not a decorative outside view, so I'll add dimensioned CAD and a section render rather than a sketch.

## Installation and hose routing

1. Work cleanly and cap the open front-cover and pump ports immediately. Remove the OMP without pulling it sideways against its drive.
2. Inspect both interface faces and the pump drive. Fit the adapter seals in their intended grooves; do not use fasteners to pull a misaligned drive into place.
3. Mount the OMP squarely on the adapter and confirm the drive turns and seats as designed before tightening.
4. Mount the vented reservoir upright where its level can be checked, away from exhaust heat and moving belts. It must keep feeding under braking and cornering.
5. Route the supply continuously downhill where practical, without high loops that trap air. Use oil-compatible hose and positively retained fittings, and protect it at every edge and hot zone.
6. Keep the hose visible enough to inspect for bubbles. Avoid cable ties that flatten the bore and fittings that impose a tight bend at the adapter.

**Gravity head.** The pump draws from the reservoir, and a low tank may not keep up. One owner thread reports that a gravity feed was only just enough at low to moderate load and not enough at high rpm, and a flyer quoted second-hand in the same thread asks for the tank level to stay at least 6 inches above the pump. I haven't tested this on my own build, so check delivery at high rpm rather than assuming it.
{:.note}

## Priming and leak checks

1. Fill the reservoir and open or loosen the lowest suitable connection until bubble-free oil reaches the adapter, then secure it.
2. Prime the OMP inlet and metering circuit. Mazda gives no priming procedure, so this is my practice. Don't rely on the pump to purge a long dry hose during a running first start.
3. Confirm all four metering lines are connected to their labelled nozzles and that the nozzles hold vacuum, by the [factory test](/ProjectPages/RX8/OMP/nozzles-premix/#testing-a-nozzle).
4. With fuel and ignition disabled, crank in short intervals and watch the feed for persistent bubbles or loss of column.
5. Start only after engine oil pressure and the separate OMP supply are established. Inspect the reservoir, hose, adapter, OMP and four lines cold, hot and after the first drive.
6. Mark the reservoir level and log distance, fuel added and oil used. A repeatable level fall is the practical whole-system delivery check; an unexpectedly unchanged or rapidly falling level needs investigation.

Likely failure modes are an empty or unvented reservoir, a loose fitting, an air leak, heat or chafe damage, incompatible hose, a failed interface seal, a mis-seated drive, a blocked line or nozzle, or lost prime. There is no factory low-level warning for the separate tank.

## Bio-Rotary oil and premix

I use Bio-Rotary Racing Premix in the separate reservoir and can also dose it into the fuel. The vendor's guidance is for adding it to fuel; putting it in the reservoir is my own practice, not something the vendor describes. Premix supplements the targeted OMP delivery. It does not repair a failed pump or a blocked nozzle.

For a naturally aspirated petrol daily driver, the range I worked from is 0.25 to 0.50 US fl oz per US gallon. That is the wording on a retailer's copy of the product text (Mazdatrix). The vendor's own page blocked my request when I checked, and another retailer's copy gives a single lower figure (1 oz per 4 US gallons, the 0.25 end of the range), so check the live page before you rely on these numbers. Higher rates are given for alcohol fuels and for track use of modified or boosted engines.

The conversions use 1 US fl oz = 29.5735 mL and 1 US gal = 3.78541 L:

| Petrol added | 0.25 oz/gal: 1.95 mL/L (about 1:512) | 0.50 oz/gal: 3.91 mL/L (about 1:256) |
| ---: | ---: | ---: |
| 10 L | 20 mL | 39 mL |
| 20 L | 39 mL | 78 mL |
| 30 L | 59 mL | 117 mL |
| 40 L | 78 mL | 156 mL |
| 50 L | 98 mL | 195 mL |

Some retailers label metric doses using 1 oz = 30 mL, which gives about 1:500 rather than 1:512, so a bottle chart may differ from this table by a few per cent. Calculate from the actual litres dispensed, don't confuse US and imperial gallons, and don't assume more oil is always better.

## Related references

- [Series 1 OMP guide](/ProjectPages/RX8/OMP/)
- [OMP nozzles and clean-oil feed](/ProjectPages/RX8/OMP/nozzles-premix/)
- [Measured stock OMP behaviour](/ProjectPages/RX8/enginedata/)
- [EnduraOMP](/ProjectPages/EnduraOMP/)
- Product text as copied by [Mazdatrix](https://mazdatrix.com/product/renewable-lubricants-bio-rotary-racing-premix/) and [ARD Importing](https://www.ardimporting.co.nz/products/bio-rotary-racing-premix), read 2026-10-14; the vendor's own page is [Renewable Lubricants](https://renewablelube.com/products/bio-rotary-racing-premix).
