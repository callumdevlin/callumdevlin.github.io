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

This page covers how I log a running Series 1 13B-MSP and what the logs show about the oil metering pump. It started as part of my [EnduraOMP project](/ProjectPages/EnduraOMP/). Mazda doesn't publish the stock pump's oil delivery and I haven't measured it, so there is no delivery map here.

## Logging set-up

An ESP32 reads engine speed from a Bluetooth OBD-II adapter (PID `0x0C`) and logs two analogue inputs, an oil pressure transducer and an oil temperature sensor, to a CSV file at about 5 Hz. Standard OBD-II readers don't expose the pump's commanded position (`MOP_POS`). Forscan can read it as an enhanced PID, along with coolant temperature, lambda and fuel trims, and it logs at roughly 100 samples a second.

The ESP32 stores raw ADC counts, so the pressure and temperature channels need the transducers' calibrations applied before they mean anything. I haven't published figures from them.

## What the commanded step read

I have two Forscan logs from a warm engine. One runs for 111 s from idle (about 800 rpm) to 2,480 rpm with coolant at 80 to 83 °C. The other runs for 60 s up to 4,520 rpm with coolant at 86 to 88 °C. In both, `MOP_POS` read 7 throughout, at every engine speed.

Step 7 is the step Mazda gives for the pump's fail-safe, where the stepper is fixed at step 7. These logs don't show whether the ECU was in fail-safe or the PID was simply reporting a constant. They stop at 4,520 rpm, so they say nothing about the pump's schedule above that.

## What Mazda publishes

| Item | Figure | Source |
| --- | --- | --- |
| Oil pressure at 3,000 rpm, oil at 100 °C | 350 kPa (3.5 bar) | Workshop manual, oil pressure inspection |
| Oil pump relief valve opens | 441 to 490 kPa | Workshop manual |
| OMP stepper at start-up | Reverses 60 steps to find zero | Control operation page |
| OMP position switch changes | Between steps 52 and 53 | Control operation page and Service Highlights |
| OMP fail-safe | Stepper fixed at step 7 | Control operation page |

The [OMP guide](/ProjectPages/RX8/OMP/how-it-works/) explains how these fit together, and the [OMP Lab](/ProjectPages/RX8/OMP/lab/) lets you step through the control logic.
