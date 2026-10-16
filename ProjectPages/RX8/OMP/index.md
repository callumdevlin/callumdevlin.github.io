---
title: Mazda RX-8 S1 Oil Metering Pump Guide
crumb: Series 1 OMP guide
permalink: /ProjectPages/RX8/OMP/
section: omp
nav_order: 0
applies: Series 1 RX-8 (2003-2008) factory electronic oil metering pump. Not the Series 2 system.
reviewed: 2026-10-14
description: >
  A practical guide to the Series 1 RX-8 oil metering pump: how it works, how to
  diagnose it, how to remove and refit it, and the nozzles, premix and clean-oil feed
  around it.
related:
  - /ProjectPages/RX8/enginedata/
  - /ProjectPages/RX8/sohn-adapter/
  - /ProjectPages/EnduraOMP/
---

The Series 1 RX-8 meters small, controlled amounts of oil into the engine to lubricate the seals and housings. Mazda's manual calls the part the metering oil pump; I use OMP.

This guide covers the Series 1 system only. The Series 2/R3 system is reported to have three nozzles per rotor and a different pump with its own codes, and an electric replacement is a different system again. Mazda's figures are quoted with a link; owner reports are marked. Confirm connector diagrams and part numbers for your model year.

## The guide {#start-here}

- [How the OMP works](/ProjectPages/RX8/OMP/how-it-works/): the pump, stepper, start-up sequence and control logic.
- [Diagnostics and testing](/ProjectPages/RX8/OMP/testing/): fault codes, symptoms and tests.
- [Removal, installation and servicing](/ProjectPages/RX8/OMP/servicing/): taking the pump off, refitting it and what to replace.
- [Nozzles, premix and clean oil feed](/ProjectPages/RX8/OMP/nozzles-premix/): nozzle checks, and what premix or a separate oil supply changes.
- [OMP Lab](/ProjectPages/RX8/OMP/lab/): an interactive model of the start-up checks, faults and commanded step.

## The system at a glance

| | |
| :--- | :--- |
| Pump | Engine-driven pumping, with a stepper motor that sets the stroke |
| Oil nozzles | Two per rotor, tilted towards the side housing |
| Control | The PCM commands the stepper in steps and re-establishes zero at every start by reversing 60 steps |
| Feedback | One on/off position switch; no continuous position sensor |
| If it faults | Fail-safe: stepper fixed at step 7, engine restricted |
| Fault codes | P1686, P1687, P1688 |
