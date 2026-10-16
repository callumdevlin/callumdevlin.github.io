---
title: RX-8 Fuel, Ignition and Starting Reference
crumb: Fuel, ignition and starting
permalink: /ProjectPages/RX8/fuel-ignition-and-starting/
section: rx8
nav_order: 7
applies: Series 1 RX-8 (2003-2008), six-port 13B-MSP. The coil kit, fuel pump and starter sections describe modifications on my car.
reviewed: 2026-10-14
description: >
  Spark plugs, D585 coils, staged injectors, fuel pressure and pump control, and
  starting checks.
---

## Spark plugs

| Position | Plug | Gap | Torque |
| --- | --- | ---: | ---: |
| Leading | NGK RE7C-L (NGK stock no. 6700) | 1.05-1.15 mm | 12.8-17.7 N·m |
| Trailing | NGK RE9B-T (NGK stock no. 6701) | 1.05-1.15 mm | 12.8-17.7 N·m |

Both are NGK Laser Iridium, sold as a set of four (two RE7C-L, two RE9B-T). What owners say:

- The RX8Club threads I read advise sticking with these rather than paying about twice as much for Denso, whose iridium plug is a colder heat range that suits racing more than road use.
- Some owners, mostly on track or in UK threads, fit the colder NGK RE8C-L in the leading position. The RE7C-L is one heat range hotter.
- Mazda's European manual page lists the leading plug under different codes (RE8A-L, RE7A-L), so check the code on the box against the two above.

Mazda's replacement limit is a gap of 1.5 mm leading and 1.4 mm trailing. Don't bend the iridium electrodes to set the gap. A lower NGK heat-range number is hotter, not a stronger spark.

Viewed from the left side of the engine, the upper ports are trailing and the lower ports leading, as I've recorded it. The front rotor is nearest the radiator. Mazda also colour-codes plugs and leads by position, so check its removal page against what you find.

```text
front     T/F     T/R     rear
          L/F     L/R
```

Label the four leads before removal and keep leading and trailing plugs apart. Wet fuel/oil suggests flooding or weak ignition; dry black carbon suggests fouling or rich short-running; blistering, glazed insulation or eroded electrodes suggest excess heat. Compare all four under the same recent conditions: one freshly flooded plug doesn't prove a mechanical fault.

## Coils and leads

The factory system has four individually triggered coils with built-in igniters: L/F, T/F, L/R and T/R. The PCM trigger outputs are `2AA`, `2AD`, `2Z` and `2AC` respectively. I've recorded coil terminal A as trigger, B as ground and C as battery supply. Mazda's pages give only the letters and test conditions, so confirm the functions on the wiring diagram before back-probing.

This car uses a Rotary Revs four-coil D585-format kit with its bracket, Magnecor leads and wiring adaptor. Mount the bracket rigidly, keep its earth and the engine/body earths clean, seat every adaptor latch, protect the coils and leads from exhaust heat, and route each lead by position.

For a misfire:

1. Read stored and pending DTCs before clearing anything.
2. Check battery voltage at the coil supply while cranking and running. Voltage drop matters more than an unloaded reading.
3. Measure earth voltage drop between the coil bracket/ground and battery negative under load.
4. Inspect connector pin fit, heat damage and arcing tracks. Mazda's reference is 1.0-4.0 kΩ at 20 °C for a factory plug lead and 3.0-7.5 kΩ at 25 °C for a plug.
5. Inspect the plug, then swap in one known-good coil/lead, keeping the labelled route.

Unburnt fuel can overheat the catalyst quickly, so don't continue a sustained misfire. D585 coils aren't a licence to invent dwell: use the supplier's documented adaptor and tune strategy for the actual coil electronics.

## Six-injector arrangement

| Stage | Front rotor | Rear rotor | Use |
| --- | --- | --- | --- |
| Primary 1 | FP1 | RP1 | Low fuel demand |
| Secondary | FS | RS | Added as demand rises |
| Primary 2 | FP2 | RP2 | High-power engine only. Mazda's test shows these inactive at idle and active from about 6,250 rpm |

Factory resistance is about 13.8 Ω at 20 °C. OEM-flow injectors suit the unmodified ECU calibration because the commanded pulse width and staged transitions assume the original flow. Replacing all six with OEM units doesn't mean they're flow-matched.

Refitting rails:

1. Relieve pressure, disconnect the battery and label every connector.
2. Pull each rail off squarely so no injector is side-loaded.
3. Replace the upper O-rings and lower grommets/seals. Lubricate with clean fuel or the manual-approved lubricant; never push a dry O-ring into the rail.
4. Refit, then command the pump or crank with ignition disabled and inspect every injector and rail joint. Repeat the leak check with the engine running.

Rich trims, fuel smell, difficult hot starts and rapid residual-pressure loss can indicate leakage. Lean trims or a weak high-load rotor can indicate restriction or staging/wiring faults; compare commanded stage, injector resistance and pressure before replacing parts.

## Fuel pressure and pump control

Connect a suitable tee and gauge at the engine-bay quick-release fuel-feed connector, using the correct fuel-line SST/adaptors and containing released fuel. Mazda's test has the engine stopped, ignition on, and the pump run by grounding the F/P terminal of the check connector. It isn't a running-pressure figure.

| Test | Mazda reference |
| --- | ---: |
| Fuel-line pressure (ignition on, engine stopped, pump run via F/P) | 375-450 kPa / 3.75-4.50 bar / 54.4-65.2 psi |
| Residual pressure five minutes after the pump stops | At least 200 kPa / 2.0 bar / 29 psi |
| Fuel-pump resistor at 20 °C | 0.304-0.336 Ω |
| Pump supply voltage at terminal B, ignition on, F/P grounded (resistor in circuit) | 3.76-5.28 V |

The fuel-pump and speed-control relays are in the engine compartment. At low demand the speed relay is off and pump current passes through a resistor, so the pump runs on reduced voltage. At high demand or cranking the PCM energises the speed relay, bypassing the resistor so the pump sees battery supply. Listen for the pump-frequency change while commanding `FPRR` with a capable scan tool.

My car runs an uprated KEMSO pump; its installation has [its own page](/ProjectPages/RX8/kemso-fuel-pump/).

## Starter and cranking

The original manual-transmission starter is a 1.4 kW coaxial-reduction unit, with a Mazda no-load reference of no more than 90 A at 11 V. This car has an uprated replacement starter.

For slow or hot cranking:

1. Measure rested battery voltage, battery voltage during cranking and actual cranking rpm.
2. Measure the positive drop from battery positive to starter B+ while cranking, then the earth drop from the starter housing/engine to battery negative. A poor cable or earth can leave a new starter slow.
3. Check terminal tightness, engine/body earth straps and heat damage near the exhaust.
4. Compare hot and cold rpm and current. High current with low rpm points to the starter or mechanical drag; low current with excessive voltage drop points to the supply path.
5. Read hot-start behaviour alongside compression, flooding and fuel residual pressure, not starter speed alone.

Cranking rpm directly affects rotary compression pressure, which is why every [compression test](/ProjectPages/RX8/compression-testing/) must record it.

## References

Mazda RX-8 2003 workshop manual (European edition), via the foxed.ca mirror, accessed 14 October 2026:

- [Spark-plug inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011801009W05.html) and [removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011801009W04.html)
- [Fuel-system location index](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011401006W01.html) and [fuel line pressure inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011401006W05.html)
- [Fuel-pump resistor inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011413350W04.html)
- [Fuel-pump speed-control operation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T26.html)

Owner threads on spark plugs, read 16 October 2026: [Best spark plugs](https://www.rx8club.com/rx-8-discussion-3/best-spark-plugs-229604/) and [Difference between RE8C-L and RE7C-L spark plugs](https://www.rx8club.com/series-i-tech-garage-22/difference-between-re8c-l-re7c-l-spark-plugs-269189/), both on RX8Club. The NGK stock numbers (6700 and 6701) are from the [Atkins Rotary plug set listing](https://www.atkinsrotary.com/04-11-Rx8-NGK-Spark-Plug-Set.html).

Vendor: the [Rotary Revs D585 kit page](https://rotaryrevs.com/garage/product/rotary-revs-d585-ignition-coil-kit/).
