---
title: 13B-MSP Engine Running Data
crumb: Engine running data
permalink: /ProjectPages/RX8/enginedata/
type: data
section: rx8
nav_order: 10
applies: One healthy Series 1 13B-MSP (231 PS). Logged during my EnduraOMP project; the PCM calibration level of the car was not recorded.
description: >
  Logged oil pressure, oil temperature and OMP behaviour from a running Series 1
  13B-MSP, including a rough reconstruction of the stock oil delivery from idle
  to 9,500 rpm.
related:
  - /ProjectPages/EnduraOMP/
  - /ProjectPages/RX8/OMP/how-it-works/
  - /ProjectPages/RX8/OMP/lab/
---

This page publishes baseline data I logged from a running Series 1 13B-MSP during my [EnduraOMP project](/ProjectPages/EnduraOMP/). I didn't find a measured dataset linking the Renesis OMP's commanded position to oil delivery (a calculated graph exists in an RX8Club thread), so I measured what I could. It's shared as a starting point for anyone tuning, diagnosing or designing around the stock lubrication system, with its limits stated plainly.

The pressure and temperature logs and the commanded steps are measurements. The oil-delivery figures are a rough reconstruction and are **unvalidated**. They are total flow for all four outlets, and the [OMP Lab](/ProjectPages/RX8/OMP/lab/)'s derived estimate is about 3.6 times higher at the top of the range. Neither has been checked against a controlled bench run.
{:.note}

## How the data was gathered

Oil delivery can't be measured directly on a running engine: putting a flow meter or restriction into the live OMP circuit risks starving the engine and wiping out the apex seals. The measurement was therefore split into two stages.

1. **On-engine logging.** Oil pressure (an external transducer in the oil filter gallery) and oil temperature (a thermocouple alongside it) were logged continuously through an ESP32 data-acquisition system, time-synchronised with OBD data streamed over Bluetooth. The ECU's commanded OMP stepper position (`MOP_POS`) isn't available through standard OBD-II PIDs, but can be read as a manufacturer-specific parameter with Forscan. Steady-state holds were captured at 2,000 / 3,000 / 5,000 / 7,000 / 8,000 / 9,000 / 9,500 rpm after warming to about 70 °C oil temperature.
2. **Bench flow characterisation.** The stock OMP was mounted on a bench rig and driven with an ESP32 and DRV8825 stepper driver at the commanded positions logged in stage 1. At each position the pump ran for a fixed 30 s interval and the delivered oil volume was measured, giving a flow rate in mL/min.

Combining the two stages gives an effective relationship between engine speed, commanded OMP position and oil delivery without putting the engine at risk.

## Operating envelope

Across the full running test, the engine and lubrication system covered this envelope:

| Parameter | Range observed |
|:----------|:---------------|
| Engine speed | about 709 to 9,480 rpm |
| Oil temperature | 18.1 to 108.8 °C |
| Oil pressure | 1.16 to 4.88 bar |

The headline finding is that **oil pressure is not governed by engine speed alone; thermal state has a strong influence.** Pressure rises with engine speed but falls as the oil warms. The two idle states show the size of the effect, though they are at different engine speeds, so the table doesn't isolate temperature on its own:

| Condition | RPM (avg) | Oil temp (avg) | Oil pressure (avg) |
|:----------|----------:|---------------:|-------------------:|
| Cold fast idle | about 1,290 | 36.5 °C | 3.38 bar |
| Hot idle (fully warm) | about 820 | 104.9 °C | 1.22 bar |

That is a factor of about 2.8 (3.38 against 1.22 bar). At higher speeds pressure rises but approaches a bounded upper range rather than climbing indefinitely:

| Condition | Mean oil pressure |
|:----------|------------------:|
| Steady cruise (about 3,000 rpm) | about 3.39 bar |
| Medium-load acceleration | about 4.08 bar |
| Upper high-load sweep | about 4.75 bar |
| Observed peak | below 4.9 bar |

The steady-cruise figure sits close to Mazda's reference of 350 kPa at 3,000 rpm with the oil at 100 °C ([quick reference](/ProjectPages/RX8/quick-reference/)). These pressures were taken in the oil-filter gallery, which is not the pressure at the OMP's inlet. A racer quoted second-hand in an RX8Club thread saw only 18 to 20 psi hot at idle at the pump feed.

## Stock OMP metering map

The commanded steps are the logged `MOP_POS` values. The delivery column is a rough reconstruction from the bench stage. It is total flow for all four outlets and is not validated:

| Engine speed | Commanded step (approx.) | Rough delivery (approx., all four outlets) |
|-------------:|-------------------------:|-------------------------------------------:|
| 1,000 rpm | step 3 | 0.15 mL/min |
| 3,000 rpm | step 9 | 0.62 mL/min |
| 6,000 rpm | step 24 | 2.25 mL/min |
| 9,500 rpm | step 47 | 6.46 mL/min |

The shape holds up: delivery per 1,000 rpm of engine speed rises from about 0.15 mL/min at step 3 to about 0.68 at step 47, so it increases progressively rather than linearly. Mid-range delivery stays modest, then ramps steeply towards the top of the rev range. That is qualitatively consistent with the 2018 RX8Club analysis of the pump's geometry, which is itself a calculation. For what a "step" physically means (the stepper changing the pump's effective plunger stroke), see [how the OMP works](/ProjectPages/RX8/OMP/how-it-works/).

**Where the numbers disagree.** At step 47 and 9,500 rpm the OMP Lab's derived estimate is about 23.4 mL/min, against 6.46 mL/min here. The two agree well at low steps and diverge at high ones. A forum poster argues the geometry calculation behind the lab is about twice too high, and my own figures may be unreliable at high steps, or both. A controlled bench run at fixed steps and speeds would settle it.
{:.note}

## Combustion signals (benchmark only)

Lambda, fuel trims and pre-cat oxygen sensor data were logged alongside, mainly as a benchmark for later lubricant comparisons. Behaviour matched expectations: rich operation with high HC/CO at cold start and early fast idle, stabilising close to λ = 1.0 at hot idle and steady cruise, then enriching again under high load.

## Limits of this data

- The bench stage measured **relative** delivery at each commanded position. System back-pressure was not replicated, so treat the mL/min figures as indicating the shape and rough scale of the stock schedule, not as a calibration-grade absolute map.
- The data is from one healthy Series 1 engine. Worn pumps, different oils and different sensor placements will shift the numbers.
- `MOP_POS` was read through Forscan's enhanced PIDs; standard OBD-II readers won't show it.

I haven't yet written down several details that affect how far the delivery figures can be trusted: what drove the pump on the bench and at what speed, how such small volumes were measured, the oil's inlet pressure and temperature, and the car's PCM calibration level (Mazda changed the start-up metering in some US calibrations). Until those are recorded, read the delivery column as a rough guide.
{:.note}

*This dataset fed into the design requirements for [EnduraOMP](/ProjectPages/EnduraOMP/), my MEng project replacing the stock metering system with a controlled electronic one.*
