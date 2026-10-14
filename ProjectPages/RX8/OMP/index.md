---
title: Mazda RX-8 S1 Oil Metering Pump Guide
crumb: Series 1 OMP guide
permalink: /ProjectPages/RX8/OMP/
type: index
section: omp
nav_order: 0
applies: Series 1 RX-8 (2003-2008) factory electronic oil metering pump. Not the Series 2 system.
reviewed: 2026-10-14
description: >
  A practical guide to the Series 1 RX-8 oil metering pump: how it works, how
  to diagnose it, how to remove and refit it, and the nozzles, premix and
  clean-oil feed around it.
---

The Series 1 RX-8 meters small, controlled amounts of oil into the rotary engine to lubricate the seals and housings. The part that does it is the **oil metering pump**, usually shortened to **OMP**. Mazda's manual calls it the metering oil pump.

This guide covers the **Series 1 system only**: not the Series 2/R3 system, which owners and specialists report has three nozzles per rotor and a different pump with its own codes, and not an electric replacement.

Where Mazda gives a figure, I quote it and link the page, and I mark what comes from owner reports instead. Confirm connector diagrams and part numbers for your exact model year before you rely on anything here.
{:.note}

## Start here

| I want to... | Go to |
| :--- | :--- |
| Understand how the pump and its control work | [How the OMP works](/ProjectPages/RX8/OMP/how-it-works/) |
| Diagnose a fault code or a suspect pump | [Diagnostics & testing](/ProjectPages/RX8/OMP/testing/) |
| Remove, refit or replace the pump | [Removal, installation & servicing](/ProjectPages/RX8/OMP/servicing/) |
| Check the nozzles, or think about premix or a clean-oil feed | [Nozzles, premix & clean oil feed](/ProjectPages/RX8/OMP/nozzles-premix/) |
| Play with engine speed, the start-up checks and faults | [RX-8 OMP Lab](/ProjectPages/RX8/OMP/lab/) |

## The system at a glance

| | |
| :--- | :--- |
| **Pump** | Engine-driven pumping, with a stepper motor that sets the stroke |
| **Oil nozzles** | Two per rotor, tilted towards the side housing |
| **Control** | The PCM commands the stepper in steps. It re-establishes zero at every engine start by reversing 60 steps |
| **Feedback** | One on/off position switch. There is no continuous position sensor |
| **If it faults** | Fail-safe: the stepper is fixed at step 7 and the engine is restricted |
| **Fault codes** | P1686, P1687 and P1688 |

## Related pages

- [13B-MSP engine running data](/ProjectPages/RX8/enginedata/): my logged dataset, including a reconstructed stock OMP metering map from idle to 9,500 rpm.
- [Custom Sohn adapter](/ProjectPages/RX8/sohn-adapter/): my separate oil-supply adapter, which keeps the factory OMP and its control.
- [EnduraOMP](/ProjectPages/EnduraOMP/): my MEng project, a closed-loop electronic replacement for this system.
