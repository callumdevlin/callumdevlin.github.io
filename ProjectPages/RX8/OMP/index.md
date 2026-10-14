---
title: Mazda RX-8 S1 Oil Metering Pump Guide
crumb: Series 1 OMP guide
permalink: /ProjectPages/RX8/OMP/
section: omp
nav_order: 0
applies: Series 1 RX-8 (2003-2008) factory electronic oil metering pump. Not the Series 2 system.
reviewed: 2026-10-14
description: >
  A practical guide to the Series 1 RX-8 oil metering pump: how it works, how
  to diagnose it, how to remove and refit it, and the nozzles, premix and
  clean-oil feed around it.
related:
  - /ProjectPages/RX8/enginedata/
  - /ProjectPages/RX8/sohn-adapter/
  - /ProjectPages/EnduraOMP/
---

The Series 1 RX-8 meters small, controlled amounts of oil into the rotary engine to lubricate the seals and housings. The part that does it is the oil metering pump, usually shortened to OMP; Mazda's manual calls it the metering oil pump.

This guide covers the Series 1 system only. The Series 2/R3 system is reported to have three nozzles per rotor and a different pump with its own codes, and an electric replacement is a different system again. Where Mazda gives a figure I quote it and link the page, and I say so where something comes from owner reports. Confirm connector diagrams and part numbers for your exact model year before relying on them.

## The guide {#start-here}

- [How the OMP works](/ProjectPages/RX8/OMP/how-it-works/): the pump, the stepper, the start-up sequence and the control logic.
- [Diagnostics and testing](/ProjectPages/RX8/OMP/testing/): fault codes, symptoms and tests for a suspect pump.
- [Removal, installation and servicing](/ProjectPages/RX8/OMP/servicing/): taking the pump off, refitting it and what to replace.
- [Nozzles, premix and clean oil feed](/ProjectPages/RX8/OMP/nozzles-premix/): checking the nozzles, and what premix or a separate oil supply changes.
- [OMP Lab](/ProjectPages/RX8/OMP/lab/): an interactive model of the start-up checks, faults and commanded step.

## The system at a glance

| | |
| :--- | :--- |
| Pump | Engine-driven pumping, with a stepper motor that sets the stroke |
| Oil nozzles | Two per rotor, tilted towards the side housing |
| Control | The PCM commands the stepper in steps and re-establishes zero at every engine start by reversing 60 steps |
| Feedback | One on/off position switch. There is no continuous position sensor |
| If it faults | Fail-safe: the stepper is fixed at step 7 and the engine is restricted |
| Fault codes | P1686, P1687 and P1688 |
