---
title: 13B-MSP Engine Running Data
permalink: /ProjectPages/RX8/enginedata/
description: >
  Logged oil pressure, oil temperature and OMP behaviour from a running
  Series 1 13B-MSP — including a reconstructed stock oil metering map
  from idle to 9,500 RPM.
---

This page publishes baseline data I logged from a running Series 1 13B-MSP during my [EnduraOMP project](/ProjectPages/EnduraOMP/). As far as I'm aware, no published dataset existed linking the Renesis OMP's commanded position to actual oil delivery, so this was measured from scratch. It's shared here as a reference for anyone tuning, diagnosing, or designing around the stock lubrication system.

## How the Data Was Gathered

Oil delivery can't be measured directly on a running engine — putting a flow meter or restriction into the live OMP circuit risks starving the engine and wiping out the apex seals. The measurement was therefore split into two stages:

1. **On-engine logging.** Oil pressure (external transducer in the oil filter gallery) and oil temperature (thermocouple alongside it) were logged continuously through an ESP32 data acquisition system, time-synchronised with OBD data streamed over Bluetooth. The ECU's commanded OMP stepper position (`MOP_POS`) isn't available through standard OBD-II PIDs, but can be read through manufacturer-specific parameters using Forscan. Steady-state holds were captured at 2,000 / 3,000 / 5,000 / 7,000 / 8,000 / 9,000 / 9,500 RPM after warming to ~70 °C oil temperature.

2. **Bench flow characterisation.** The stock OMP was then mounted on a bench rig and driven with an ESP32 and DRV8825 stepper driver at the same commanded positions logged in stage 1. At each position the pump ran for a fixed 30 s interval and the delivered oil volume was measured, giving flow rate in ml/min.

Combining the two stages reconstructs the effective relationship between engine speed, commanded OMP position, and oil delivery — without ever putting the engine at risk.

## Operating Envelope

Across the full running test, the engine and lubrication system covered the following envelope:

| Parameter | Range observed |
|:----------|:---------------|
| Engine speed | ~709 – 9,480 RPM |
| Oil temperature | 18.1 – 108.8 °C |
| Oil pressure | 1.16 – 4.88 bar |

The headline finding: **oil pressure is not governed by RPM alone — thermal state has a strong influence.** Pressure rises with engine speed but falls as oil temperature rises, which shows up clearly when comparing idle states:

| Condition | RPM (avg) | Oil temp (avg) | Oil pressure (avg) |
|:----------|----------:|---------------:|-------------------:|
| Cold fast idle | ~1,290 | 36.5 °C | 3.38 bar |
| Hot idle (fully warm) | ~820 | 104.9 °C | 1.22 bar |

Same engine, same idle — nearly a 3× difference in oil pressure purely from thermal state.

At higher speeds, pressure rises but approaches a bounded upper range rather than climbing indefinitely:

| Condition | Mean oil pressure |
|:----------|------------------:|
| Steady cruise (~3,000 RPM) | ~3.39 bar |
| Medium-load acceleration | ~4.08 bar |
| Upper high-load sweep | ~4.75 bar |
| Observed peak | < 4.9 bar |

## Stock OMP Metering Map

The reconstructed stock control schedule shows a progressive — not linear — increase in metering with engine speed:

| Engine speed | Commanded step (approx.) | Derived oil delivery (approx.) |
|-------------:|-------------------------:|-------------------------------:|
| 1,000 RPM | step 3 | 0.15 ml/min |
| 3,000 RPM | step 9 | 0.62 ml/min |
| 6,000 RPM | step 24 | 2.25 ml/min |
| 9,500 RPM | step 47 | 6.46 ml/min |

Mid-range delivery stays modest, then ramps steeply toward the top of the rev range. For context on what these "steps" physically mean — the stepper motor changing the pump's effective plunger stroke — see [how the OMP works](/ProjectPages/RX8/OMP/how-it-works/).

## Combustion Signals (Benchmark Only)

Lambda, fuel trims and pre-cat oxygen sensor data were logged alongside, primarily as a benchmark for later lubricant comparisons. Behaviour matched expectations: rich operation with high HC/CO at cold start and early fast idle, stabilising close to λ = 1.0 at hot idle and steady cruise, then enriching again under high load.

## Caveats

- The bench flow stage measured **relative** delivery at each commanded position — absolute system back-pressure was not replicated, so treat the ml/min figures as a well-grounded characterisation of the stock schedule's shape and scale, not a calibration-grade absolute map.
- Data is from one healthy Series 1 engine. Worn pumps, different oils and different sensor placements will shift the numbers.
- Step commands were read via Forscan's enhanced PIDs (`MOP_POS`); standard OBD-II readers will not show this parameter.

*This dataset fed directly into the design requirements for [EnduraOMP](/ProjectPages/EnduraOMP/), my MEng project replacing the stock metering system with a closed-loop electronic one.*
