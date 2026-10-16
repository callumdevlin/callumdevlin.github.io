---
title: Custom RX-8 Sohn Adapter and Separate OMP Oil Supply
crumb: Sohn adapter
permalink: /ProjectPages/RX8/sohn-adapter/
section: rx8
nav_order: 9
status: wip
applies: My own build on a Series 1 RX-8.
reviewed: 2026-10-14
description: >
  A front-cover adapter that lets the factory oil metering pump draw from a separate
  reservoir, with fitting, priming and premix doses.
---

The adapter lets the factory Series 1 oil metering pump (OMP) draw clean two-stroke oil from its own reservoir instead of engine oil. The pump, its drive and control, and the four metering pipes and nozzles all stay factory.

## Oil path

| | Path |
| --- | --- |
| Factory | Sump → front-cover drilling → OMP → four pipes/nozzles → engine |
| Modified | Vented reservoir → oil-resistant hose → adapter → OMP → four pipes/nozzles → engine |

{% include figure.html src="/assets/rx8/generated/sohn-oil-path.svg" alt="Block diagram comparing the factory oil path, from the sump through the front cover to the OMP and four nozzles, with the modified path from a vented reservoir through the adapter to the same OMP and nozzles" caption="The factory and modified oil paths. A schematic of the arrangement, not a drawing of the adapter." class="fig-medium" %}

The adapter sits between the front cover and the OMP. It closes the original sump-oil feed and gives the pump a separate inlet.

## Components {#component-record}

- Pump and control: factory Series 1 electronic OMP and PCM strategy.
- Delivery: the four factory metering pipes and nozzles.
- Oil: Renewable Lubricants Bio-Rotary Racing Premix.
- Adapter drawings, material and seal details, and reservoir capacity: not published yet.

## Fitting

1. Work clean and cap the open front-cover and pump ports straight away. Take the OMP off without pulling it sideways against its drive.
2. Check both faces and the pump drive, and seat the adapter seals in their grooves. Never use the bolts to pull a misaligned drive into place.
3. Mount the OMP square on the adapter and check the drive turns and seats before tightening.
4. Mount the vented reservoir upright, with the level visible, away from exhaust heat and belts. It must keep feeding under braking and cornering.
5. Run the supply hose downhill where you can, with no high loops that trap air. Use oil-compatible hose with retained fittings, protect it at edges and hot spots, keep it visible enough to spot bubbles, and avoid ties that flatten the bore or a tight bend at the adapter.

The pump draws from the reservoir, so a low tank may not keep up. One owner thread reports a gravity feed that was only just enough at low to moderate load and not enough at high rpm, and a flyer quoted in it asks for the tank level to stay at least 6 inches above the pump. I haven't tested this on my build, so check delivery at high rpm.
{:.note}

## Priming and checks

1. Fill the reservoir and loosen the lowest suitable connection until bubble-free oil reaches the adapter, then secure it.
2. Prime the OMP inlet and metering circuit. Mazda gives no priming procedure, so this is my practice. Don't count on the pump purging a long dry hose during a first start.
3. Check all four metering lines are on their labelled nozzles and the nozzles hold vacuum, using the [factory test](/ProjectPages/RX8/OMP/nozzles-premix/#testing-a-nozzle).
4. With fuel and ignition disabled, crank in short bursts and watch for bubbles or a falling oil column.
5. Start only once engine oil pressure and the separate OMP supply are established. Inspect everything cold, hot and after the first drive.
6. Mark the reservoir level and log distance, fuel added and oil used. A repeatable level fall is the practical whole-system check; a level that doesn't move, or falls fast, needs investigating.

Likely faults: empty or unvented reservoir, loose fitting, air leak, heat or chafe damage, incompatible hose, failed adapter seal, mis-seated drive, blocked line or nozzle, lost prime. The factory has no low-level warning for the separate tank.

## Premix {#bio-rotary-oil-and-premix}

I run Bio-Rotary Racing Premix in the reservoir and can also dose it into the fuel. The vendor only describes adding it to fuel; reservoir use is my own practice. Premix supplements the OMP's delivery and doesn't fix a failed pump or a blocked nozzle.

For a naturally aspirated petrol daily driver I worked to **0.25 to 0.50 US fl oz per US gallon**, the wording on Mazdatrix's copy of the product text. Another retailer's copy gives only the lower figure (1 oz per 4 US gallons), so check the vendor's live page. Higher rates are given for alcohol fuels and for track use of modified or boosted engines.

Conversions use 1 US fl oz = 29.5735 mL and 1 US gal = 3.78541 L:

| Petrol added | 0.25 oz/gal: 1.95 mL/L (about 1:512) | 0.50 oz/gal: 3.91 mL/L (about 1:256) |
| ---: | ---: | ---: |
| 10 L | 20 mL | 39 mL |
| 20 L | 39 mL | 78 mL |
| 30 L | 59 mL | 117 mL |
| 40 L | 78 mL | 156 mL |
| 50 L | 98 mL | 195 mL |

Some retailers use 1 oz = 30 mL (about 1:500), so a bottle chart can differ from this table by a few per cent. Work from the litres you actually add, don't mix up US and imperial gallons, and more oil isn't always better.

## References {#related-references}

- Product text as copied by [Mazdatrix](https://mazdatrix.com/product/renewable-lubricants-bio-rotary-racing-premix/) and [ARD Importing](https://www.ardimporting.co.nz/products/bio-rotary-racing-premix), accessed 14 October 2026; the vendor's page is [Renewable Lubricants](https://renewablelube.com/products/bio-rotary-racing-premix).
- The factory pump and nozzles: [Series 1 OMP guide](/ProjectPages/RX8/OMP/) and [nozzles and clean-oil feed](/ProjectPages/RX8/OMP/nozzles-premix/).
