---
title: RX-8 Fuel, Ignition and Starting Reference
crumb: Fuel, ignition and starting
permalink: /ProjectPages/RX8/fuel-ignition-and-starting/
type: reference
section: rx8
nav_order: 7
applies: Series 1 RX-8 (2003-2008), six-port 13B-MSP. The coil kit, fuel pump and starter sections describe modifications on my car.
reviewed: 2026-10-14
description: >
  Spark plugs, D585 coils, staged injectors, fuel pressure, KEMSO pump installation
  and starting checks.
---

## Spark plugs

| Position | Plug | Gap | Torque |
| --- | --- | ---: | ---: |
| Leading | Mazda's European list: NGK RE8A-L, or RE7A-L (hotter). My car appears to have RE7C-L, which is not in Mazda's list | 1.05-1.15 mm | 12.8-17.7 N·m |
| Trailing | NGK RE9B-T | 1.05-1.15 mm | 12.8-17.7 N·m |

Mazda's replacement limit is a gap of 1.5 mm on a leading plug and 1.4 mm on a trailing plug. Don't bend the iridium electrodes to adjust the gap. A lower NGK heat-range number is hotter; it does not mean a stronger spark.

Viewed from the left side of the engine, the upper ports are trailing and the lower ports are leading, as I've recorded it. The front rotor is nearest the radiator and the rear rotor nearest the bulkhead. Mazda also colour-codes plugs and leads by position, so check its spark-plug removal page against what you find.

```text
front     T/F     T/R     rear
          L/F     L/R
```

Label the four leads before removal and keep leading and trailing plugs separate. Wet fuel/oil suggests flooding or weak ignition; dry black carbon suggests fouling or rich short-running; blistering, glazed insulation or eroded electrodes suggest excess heat. Compare all four under the same recent operating conditions: one freshly flooded plug does not prove a mechanical fault.

## Coils and leads

The factory system has four individually triggered coils with built-in igniters: L/F, T/F, L/R and T/R. The PCM trigger outputs are `2AA`, `2AD`, `2Z` and `2AC` respectively. I've recorded coil terminal A as the trigger, B as ground and C as battery supply. Mazda's pages give only the letters and the test conditions, so confirm the functions on the wiring diagram before back-probing.

This car uses a Rotary Revs four-coil D585-format kit with its bracket, Magnecor leads and wiring adaptor. Mount the bracket rigidly, keep its earth and the engine/body earths clean, seat every adaptor latch, and protect the coils and leads from exhaust heat. Route each lead by position, not by whichever cable reaches.

For a misfire:

1. Read stored and pending DTCs before clearing anything.
2. Check battery voltage at the coil supply while cranking and running. Voltage drop matters more than an unloaded reading.
3. Measure earth voltage drop between the coil bracket/ground and battery negative under load.
4. Inspect connector pin fit, heat damage and arcing tracks. Mazda's reference for a factory plug lead is 1.0-4.0 kΩ at 20 °C, and for a plug 3.0-7.5 kΩ at 25 °C.
5. Inspect the plug, then substitute one known-good coil/lead while keeping the labelled route.

Unburnt fuel can overheat the catalyst quickly, so do not continue a sustained misfire. D585 coils are not a licence to invent dwell: use the supplier's documented adaptor and tune strategy for the actual coil electronics.

## Six-injector arrangement

| Stage | Front rotor | Rear rotor | Use |
| --- | --- | --- | --- |
| Primary 1 | FP1 | RP1 | Low fuel demand |
| Secondary | FS | RS | Added as demand rises |
| Primary 2 | FP2 | RP2 | High-power engine only. Mazda's test shows these inactive at idle and active from about 6,250 rpm |

Factory resistance is approximately 13.8 Ω at 20 °C. Standard OEM-flow injectors suit the unmodified ECU calibration because the commanded pulse width and staged transitions assume the original flow characteristics. Replacing all six with OEM units does not establish that they are flow-matched.

Relieve pressure, disconnect the battery and label every connector before removing the rails. Pull each rail squarely so an injector is not side-loaded. Replace the upper O-rings and lower grommets/seals, lubricate them with clean fuel or the manual-approved lubricant, and never push a dry O-ring into the rail. After refitting, command the pump or crank with ignition disabled, inspect every injector/rail joint, then repeat the leak check with the engine running.

Rich trims, fuel smell, difficult hot starts and a rapid residual-pressure loss can indicate leakage. Lean trims or a weak high-load rotor can indicate restriction or staging/wiring faults; compare commanded stage, injector resistance and pressure before replacing parts.

## Fuel pressure and pump control

Connect a suitable tee and pressure gauge at the engine-bay quick-release fuel-feed connector. Use the correct fuel-line SST/adaptors and contain released fuel. Mazda's test is with the engine stopped, the ignition on, and the pump run by grounding the F/P terminal of the check connector. It is not a running-pressure figure.

| Test | Mazda reference |
| --- | ---: |
| Fuel-line pressure (ignition on, engine stopped, pump run via F/P) | 375-450 kPa / 3.75-4.50 bar / 54.4-65.2 psi |
| Residual pressure five minutes after the pump stops | At least 200 kPa / 2.0 bar / 29 psi |
| Fuel-pump resistor at 20 °C | 0.304-0.336 Ω |
| Pump supply voltage at terminal B, ignition on, F/P grounded (resistor in circuit) | 3.76-5.28 V |

The fuel-pump and fuel-pump-speed-control relays are in the engine compartment. At low demand the speed relay is off and pump current passes through a resistor, so the pump runs on reduced voltage. At high demand or cranking the PCM energises the speed relay, bypassing the resistor so the pump sees battery supply. Listen for the pump-frequency change while commanding `FPRR` with a capable scan tool.

## KEMSO 10910 installation

| Published item | KEMSO value |
| --- | ---: |
| SKU | 10910 |
| Nominal flow | 340 L/h |
| Flow condition | 43 psi at 13.5 V |
| Published pressure range | 43-90 psi |
| Body diameter | Approximately 38 mm |

KEMSO's listing makes no Series 1 or Series 2 fitment statement. The 340 L/h figure is a bench point, not in-car delivery at all voltage and pressure states. The RX-8 deliberately runs the pump at reduced voltage at low demand, so validate pressure in both relay states.

Mazda's rules for opening the module, from its fuel-pump unit removal page: drain the tank to half full or less on the gauge first, because above about three quarters the fuel level is above the pump flange. The lock ring is tightened with the Mazda SST: one full turn by hand, then a further 50-140° to a torque of 80-135 N·m. If that torque isn't reached, replace the cap or retainer. Mazda's leak check afterwards is to start from standstill, or brake five or six times at low speed, and look for leaks.
{:.note}

1. Record baseline fuel-line pressure, residual pressure and the fuel-level indication. Relieve pressure, disconnect the battery, ventilate the area and remove the rear seat and the pump service cover. Drain the tank as above.
2. Clean the outside of the module before opening it. Mark the lock-ring/module orientation and photograph the sender arm, cup, strainer and wiring.
3. Lift the module without bending the sender arm. Drain it into an approved container and compare the KEMSO body, outlet and polarity with the original pump.
4. Fit the strainer at the bottom of the reservoir cup in the same low orientation, clear of the cup wall and the sender sweep.
5. Use only hose rated for continuous submerged in-tank fuel service, and fuel-injection clamps. General external fuel hose can delaminate when its outer surface is submerged.
6. Confirm connector polarity, terminal retention and insulation. Secure the pump without point-loading its body or outlet and make sure the hose cannot kink as the module closes.
7. Move the sender through its full travel and check clearance to the pump, retaining clip, strainer, wires and hose. Verify the reservoir-cup fill and jet-pump passages stay unobstructed.
8. Fit a sound module seal, return the module to its orientation marks and tighten the lock ring by Mazda's method above. Reconnect, command the pump and check for vapour and liquid leaks before refitting the cover.
9. Recheck the fuel-level indication, running pressure, five-minute residual pressure, connector temperature and pressure in both low and high pump states.

### PA11 retaining clip

The custom MJF clip locates the 38 mm KEMSO body in the factory module. It is printed in PA11-HP.

> A prototype clip was left immersed in fuel for three weeks. After removal, it retained its apparent structural stiffness and no visible residue was observed in the fuel. This was a useful preliminary compatibility check, but it was not a complete long-term qualification test.

That observation did not measure swelling, mass change, creep or lifetime. On service, inspect contact stress, cracks, softening, wire/outlet damage and sender/cup clearance. A future check should add dimensional and pull testing, vibration/shock exposure and longer-term inspection in the identified pump fuel.

## Starter and cranking

The original manual-transmission starter is a 1.4 kW coaxial-reduction unit, and Mazda's no-load reference is no more than 90 A at 11 V. This car has an uprated replacement starter.

For slow or hot cranking:

1. Measure rested battery voltage, voltage at the battery during cranking and actual rotary cranking rpm.
2. Measure the positive drop from battery positive to starter B+ while cranking, then the earth drop from the starter housing/engine to battery negative. A poor cable or earth can leave a new starter slow.
3. Check terminal tightness, engine/body earth straps and heat damage near the exhaust.
4. Compare hot and cold rpm and current. High current with low rpm points toward the starter or mechanical drag; low current with excessive voltage drop points toward the supply path.
5. Interpret hot-start behaviour alongside compression, flooding and fuel residual pressure rather than treating starter speed as the only cause.

Cranking rpm directly affects rotary compression pressure, which is why every [compression test](/ProjectPages/RX8/compression-testing/) must record it.

## References

Mazda RX-8 2003 workshop manual (European edition), via the foxed.ca mirror, accessed 14 October 2026:

- [Spark-plug inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011801009W05.html) and [removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011801009W04.html)
- [Fuel-system location index](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011401006W01.html) and [fuel line pressure inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011401006W05.html)
- [Fuel-pump unit removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011413350W01.html), [inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011413350W02.html) and [resistor inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011413350W04.html)
- [Fuel-pump speed-control operation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T26.html)

Vendors: [KEMSO 10910 product page](https://www.kemsoracing.com/products/kemso-fuel-pump-for-mazda-rx8) and the [Rotary Revs D585 kit page](https://rotaryrevs.com/garage/product/rotary-revs-d585-ignition-coil-kit/).
