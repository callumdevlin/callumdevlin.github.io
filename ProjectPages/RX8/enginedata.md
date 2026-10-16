---
title: 13B-MSP Engine Running Data
crumb: Engine running data
permalink: /ProjectPages/RX8/enginedata/
section: rx8
nav_order: 10
applies: Series 1 RX-8 (2003-2008) 13B-MSP, 231 PS.
description: >
  How I log a running 13B-MSP, what the oil metering pump's commanded step read in my
  Forscan logs, and the lubrication figures Mazda publishes.
related:
  - /ProjectPages/EnduraOMP/
  - /ProjectPages/RX8/OMP/how-it-works/
---

How I log a running Series 1 13B-MSP, and what the logs show about the oil metering pump. It started as part of my [EnduraOMP project](/ProjectPages/EnduraOMP/). Mazda doesn't publish the stock pump's oil delivery and I haven't measured it, so there is no delivery map here.

## Logging set-up

- **ESP32:** reads engine speed from a Bluetooth OBD-II adapter (PID `0x0C`) and logs an oil pressure transducer and an oil temperature sensor to CSV at about 5 Hz. It stores raw ADC counts, so the transducer calibrations must be applied before the values mean anything. I haven't published figures from them.
- **Forscan:** standard OBD-II readers don't expose the pump's commanded position (`MOP_POS`), but Forscan reads it as an enhanced PID, along with coolant temperature, lambda and fuel trims, at roughly 100 samples a second.

## What the commanded step read

Two Forscan logs from a warm engine: 111 s from idle (about 800 rpm) to 2,480 rpm with coolant at 80-83 °C, and 60 s up to 4,520 rpm with coolant at 86-88 °C. In both, `MOP_POS` read 7 throughout, at every engine speed.

Step 7 is Mazda's fail-safe step. The logs don't show whether the ECU was in fail-safe or the PID was just reporting a constant, and they stop at 4,520 rpm, so they say nothing about the schedule above that.

## What Mazda publishes

| Item | Figure | Source |
| --- | --- | --- |
| Oil pressure at 3,000 rpm, oil at 100 °C | 350 kPa (3.5 bar) | Workshop manual, oil pressure inspection |
| Oil pump relief valve opens | 441 to 490 kPa | Workshop manual |
| OMP stepper at start-up | Reverses 60 steps to find zero | Control operation page |
| OMP position switch changes | Between steps 52 and 53 | Control operation page and Service Highlights |
| OMP fail-safe | Stepper fixed at step 7 | Control operation page |

The [OMP guide](/ProjectPages/RX8/OMP/how-it-works/) explains how these fit together, and the [OMP Lab](/ProjectPages/RX8/OMP/lab/) lets you step through the control logic.
