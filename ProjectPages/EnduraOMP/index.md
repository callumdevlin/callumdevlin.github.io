---
title: EnduraOMP — Improving Rotary Engine Reliability
permalink: /ProjectPages/EnduraOMP/
image: /Images/enduraomp-engine-1.webp
description: >
  My MEng individual project — a closed-loop, electronically controlled oil
  metering system for rotary engines, taken from live engine testing through
  to a working machined prototype.
---

![EnduraOMP mounted on a 13B-MSP](/Images/enduraomp-engine-1.webp){:.lead loading="lazy"}

The EnduraOMP pump mounted on the 13B-MSP, replacing the stock oil metering pump on the OEM interface.
{:.figcaption}

**EnduraOMP** is my MEng individual project at the University of Strathclyde: a reliability-focused lubrication system for rotary (Wankel) engines, built around an electronically controlled gear pump, a dedicated clean-oil supply, and onboard sensing and diagnostics. The project ran from problem research through to a machined, assembled and bench-tested prototype.

## The Problem

Rotary engines are compact, smooth and power-dense — which is exactly why they keep coming back, from Mazda's MX-30 R-EV range extender to UAV propulsion and generator sets. But they've never shaken their reputation for being short-lived, and the root causes are tightly linked:

- **Seal wear and compression loss** — apex, side and corner seals slide at high speed against the housings and wear down, costing compression and power.
- **Oil consumption and carbon build-up** — oil is deliberately burned in the chambers, and conventional crankcase oils leave ash deposits that foul plugs and stick seals.
- **Thermal distortion** — large temperature differences across the housings distort sealing surfaces and accelerate the cycle.

Through teardown work, user research with rotary specialists, and benchmarking, I identified **internal lubrication as the highest-leverage intervention point**: it directly drives seal wear, deposits and thermal behaviour, yet the stock system offers the user no visibility and limited control.

## Building the Evidence First

Rather than jumping to a concept, I generated a baseline dataset from a running Mazda 13B-MSP — because no published data existed linking the stock oil metering pump's commanded position to actual oil delivery.

The approach had two stages: logging the live engine's ECU-commanded OMP position against RPM, oil pressure and oil temperature (without touching the oil circuit), then bench-driving the stock pump at those same commanded positions to measure real flow. Together they reconstructed the stock metering map — from roughly **0.15 ml/min at idle to 6.5 ml/min at 9,500 RPM** — and showed that oil pressure is strongly coupled to temperature, not just engine speed.

That dataset defined the operating envelope any replacement system has to satisfy. The full results are published in my [13B-MSP engine data notes](/ProjectPages/RX8/enginedata/).

## The Solution

EnduraOMP replaces the stock mechanically driven metering pump with a **closed-loop, electronically controlled lubrication system** made up of four subsystems:

![EnduraOMP pump unit](/Images/enduraomp-pump.webp){:width="450" loading="lazy"}
![Pump with control electronics exposed](/Images/enduraomp-pump-internals.webp){:width="450" loading="lazy"}

The pump unit, and the same assembly with the integrated ESP32 motor control board exposed.
{:.figcaption}

**The pump** — an external gear pump driven by a 12 V brushless DC motor, delivering a repeatable volume per revolution and controlled by PWM rather than being slaved to engine speed. The housing uses a sectioned architecture (inspired by how rotary engines themselves are built up in layers) so that coolant channels surround the pump cavity for cold-start oil warming, while the oil and coolant loops stay fully sealed from one another. The housing is CNC-machined, anodised 6061 aluminium.

![Pump section view showing internal gear set and coolant jacket](/Images/enduraomp-pump-section.jpg){:loading="lazy"}

Section view: the gear set sits at the core, wrapped by the coolant conditioning jacket.
{:.figcaption}

**The control board** — an ESP32-based PCB integrated into the pump body, reading engine speed, oil temperature, oil pressure and tank level, and metering oil to suit the operating condition: higher flow for cold starts, stable low flow at hot idle, and scaled delivery under high load. USB-C is on board for programming and data access.

![External oil tank](/Images/enduraomp-tank.webp){:width="450" loading="lazy"}
![Tank internals with float-type level sender](/Images/enduraomp-tank-xray.webp){:width="450" loading="lazy"}

The dedicated oil reservoir, with a float-type level sender feeding the gauge.
{:.figcaption}

**The tank** — a dedicated external reservoir so the engine injects clean, purpose-chosen oil rather than drawing from the sump. This enables ashless, ester-based two-stroke oils that burn cleanly instead of leaving deposits, and means sump oil condition no longer dictates what gets burned in the chambers.

![EnduraOMP oil level gauge](/Images/enduraomp-gauge-lit.webp){:width="420" loading="lazy"}

The LED bar gauge — oil level at a glance, no dipstick required.
{:.figcaption}

**The gauge** — a dashboard LED bar driven from the tank's level sender, giving the user constant visibility of injection oil level. Rotary ownership normally means religious dipstick checks; this puts that information in front of the driver.

## What Makes It Different

Existing reliability products each attack one piece of the problem — premix kits, clean-oil feed adapters, upgraded seals. EnduraOMP's core idea is that **lubrication should be a controlled, observable, serviceable subsystem**, not a hidden one:

- **Decoupled from engine speed** — a calibrated flow map replaces the fixed mechanical relationship, so delivery suits the actual operating condition, including a cold-start priming strategy.
- **Fault-aware by design** — low oil, pressure faults, sensor failure and pump failure are detected and handled, with application-dependent responses (warn and derate for a UAV, controlled shutdown for a generator) and loggable diagnostics.
- **One scalable architecture** — the same hardware suits automotive, generator and UAV duty cycles; only the calibration maps and protective actions change.
- **User-visible** — the tank and gauge turn oil management from guesswork into a glance.

## Prototype & Validation

This didn't stay in CAD. The boards were manufactured by JLCPCB and hand-assembled; the housing, coolant plate and slide plates were CNC-machined and anodised; gaskets were cut from NBR sheet, and the remaining hardware was 3D printed in ASA.

Testing was staged, subsystem by subsystem:

- **Electronics** — the motor control board ran the brushless pump motor smoothly across the full PWM range first time. The gauge board needed a grounding fix and extra PWM smoothing before the LED bar read steadily — exactly the kind of fault staged bench testing is for, and both fixes are now baked into the next board revision.
- **Engine fitment** — the pump assembly mounted directly to the 13B-MSP on the OEM OMP interface and sealed against the original engine geometry, with practical hose and tool access.
- **Fluid testing** — the coolant loop flowed cleanly with no external leaks, and the pump circulated oil and produced measurable flow. Most importantly, **there was zero cross-leakage between the oil and coolant loops**, validating the sectioned sealing architecture.
- **On-engine oil comparison** — running the engine on the selected ashless bio-ester oil through an external feed, against the earlier 10W-30 baseline under the same warm-up and rev pattern, showed a clear improvement in the hydrocarbon emissions trace.

## Honest Limitations & Next Steps

The prototype's deliberately relaxed machining tolerances (chosen to guarantee a one-off assembly would go together) cost volumetric efficiency through internal leakage at the slide-plate interfaces — so the next iteration is about tighter manufacturing control of those faces, not a new layout. The electronics need a stronger ground pour and hardware-level signal filtering. And the big one: a full, instrumented on-engine test campaign to validate flow behaviour, thermal interaction and fault handling under real load.

The project doesn't claim production readiness — what it demonstrates is that treating rotary lubrication as a controlled, testable, user-visible subsystem is a credible and buildable route to a more reliable rotary engine.

---

*Curious about the stock system this replaces? My [RX-8 OMP guide](/ProjectPages/RX8/OMP/) documents how Mazda's metering pump works, how to diagnose it, and how to service it.*
