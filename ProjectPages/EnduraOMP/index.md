---
title: "EnduraOMP: Controlled Lubrication for Rotary Engines"
crumb: EnduraOMP
permalink: /ProjectPages/EnduraOMP/
type: case-study
image: /Images/optimised/enduraomp-engine-1-1200.webp
description: >
  My MEng individual project: an electronically controlled oil metering system for
  rotary engines, from logged data on a running engine to a machined, bench-tested
  prototype.
related:
  - /ProjectPages/RX8/enginedata/
  - /ProjectPages/RX8/OMP/
  - /ProjectPages/RX8/sohn-adapter/
---

{% include figure.html src="/Images/enduraomp-engine-1.webp" alt="CAD render of the EnduraOMP pump, in green and black, mounted on the side of a Mazda 13B-MSP rotary engine with a clear oil line running to the engine" caption="The EnduraOMP pump on the 13B-MSP, replacing the stock oil metering pump on the OEM interface. The images on this page are CAD renders of the design." eager=true %}

**EnduraOMP** is my MEng individual project at the University of Strathclyde: a reliability-focused lubrication system for rotary (Wankel) engines, built around an electronically controlled gear pump, a dedicated clean-oil supply, and onboard sensing and diagnostics. The project ran from problem research through to a machined, assembled and bench-tested prototype.

I haven't added photographs of the built prototype to this page yet, so every image here is a render of the design. What was built and tested is described in [Prototype and bench testing](#prototype-and-bench-testing), along with what wasn't.
{:.note}

## The problem

Rotary engines are compact, smooth and power-dense, which is why they keep coming back, from Mazda's MX-30 R-EV range extender to UAV propulsion and generator sets. But they have never shaken their reputation for being short-lived, and the causes are closely linked:

- **Seal wear and compression loss.** Apex, side and corner seals slide at high speed against the housings and wear down, costing compression and power.
- **Oil consumption and carbon build-up.** Oil is deliberately burned in the chambers, and conventional crankcase oils leave ash deposits that foul plugs and stick seals.
- **Thermal distortion.** Large temperature differences across the housings distort sealing surfaces and accelerate the cycle.

Through teardown work, user research with rotary specialists and benchmarking, I identified **internal lubrication as the place where an intervention would do the most good**. It drives seal wear, deposits and thermal behaviour directly, yet the stock system gives the user no visibility and limited control.

## Building the evidence first

Rather than jumping to a concept, I generated a baseline dataset from a running Mazda 13B-MSP. I didn't find a measured dataset linking the stock oil metering pump's commanded position to the oil it delivers.

The approach had two stages. First, I logged the live engine's ECU-commanded OMP position against RPM, oil pressure and oil temperature, without touching the oil circuit. Then I bench-drove the stock pump at those same commanded positions and measured the flow. Together they gave a rough reconstruction of the stock metering schedule: from about 0.15 mL/min at idle to about 6.5 mL/min at 9,500 RPM, and a clear dependence of oil pressure on temperature as well as engine speed.

The pressures and commanded steps are measurements. The delivery figures are rough and unvalidated, and the derived estimate in my [OMP Lab](/ProjectPages/RX8/OMP/lab/) puts the top of the range about 3.6 times higher, so I treat them as the scale of the problem rather than a calibration. The full results and their limits are in my [13B-MSP engine data notes](/ProjectPages/RX8/enginedata/).

## The design

EnduraOMP replaces the stock mechanically driven metering pump with an **electronically controlled lubrication system** of four subsystems.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/enduraomp-pump.webp" alt="Render of the EnduraOMP pump unit: a dark grey body with two oil ports at one end and a green anodised mid-section" caption="The pump unit." %}
{% include figure.html src="/Images/enduraomp-pump-internals.webp" alt="Render of the pump with its cover off, showing the ESP32 control board and its connectors fixed to the motor end" caption="The same assembly with the integrated ESP32 control board exposed." %}
</div>

**The pump** is an external gear pump driven by a 12 V brushless DC motor. It delivers a repeatable volume per revolution and is controlled by PWM rather than being slaved to engine speed. The housing is built up in sections, much as a rotary engine is built up in layers, so coolant channels surround the pump cavity to warm the oil on a cold start while the oil and coolant loops stay sealed from each other. The housing is CNC-machined, anodised 6061 aluminium.

{% include figure.html src="/Images/enduraomp-pump-section.jpg" alt="Transparent render of the pump in section: the gear set at the centre inside a green coolant jacket, the motor and control electronics to the right" caption="Section render: the gear set sits at the core, wrapped by the coolant-conditioning jacket." class="fig-medium" %}

**The control board** is an ESP32-based PCB built into the pump body. It is designed to read engine speed, oil temperature, oil pressure and tank level, and to meter oil to suit the operating condition: higher flow for cold starts, stable low flow at hot idle and scaled delivery under high load. USB-C on the board is for programming and data access.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/enduraomp-tank.webp" alt="Render of a polished aluminium oil tank with a screw cap, mounting studs on one side and a hose barb at the bottom" caption="The dedicated oil reservoir." %}
{% include figure.html src="/Images/enduraomp-tank-xray.webp" alt="Cutaway render of the tank showing the oil level and a float-type level sender inside" caption="Cutaway: a float-type level sender feeds the gauge." %}
</div>

**The tank** is a dedicated external reservoir, so the engine injects clean, purpose-chosen oil rather than drawing from the sump. That allows ashless, ester-based two-stroke oils that leave less ash than crankcase oil, and it means the condition of the sump oil no longer decides what gets burned in the chambers.

{% include figure.html src="/Images/enduraomp-gauge-lit.webp" alt="Render of a round dashboard gauge with an LED bar showing the oil level" caption="The LED bar gauge: oil level at a glance, no dipstick." class="fig-narrow" %}

**The gauge** is a dashboard LED bar driven from the tank's level sender, so the injection oil level is always in front of the driver. Rotary ownership normally means careful dipstick checks. This puts that information where you can see it.

## What I was aiming for

Existing reliability products each tackle one piece of the problem: premix kits, clean-oil feed adapters, upgraded seals. The core idea of EnduraOMP is that **lubrication should be a controlled, observable, serviceable subsystem**, not a hidden one:

- **Not tied to engine speed.** A calibrated flow map replaces the fixed mechanical relationship, so delivery can follow the operating condition, including a cold-start priming strategy. The map sets the flow from engine speed and condition; nothing in the design measures the delivered flow itself, so I describe it as electronically controlled rather than closed-loop.
- **Fault-aware by design.** The design is meant to detect low oil, pressure faults, sensor failure and pump failure, with responses that depend on the application (warn and derate for a UAV, controlled shutdown for a generator) and loggable diagnostics. I haven't tested these responses on an engine.
- **One architecture, in intent.** The same hardware is meant to suit automotive, generator and UAV duty, with only the calibration maps and protective actions changing. I have only worked with the 13B-MSP.
- **Visible to the user.** The tank and gauge turn oil management from guesswork into a glance.

## Prototype and bench testing

This didn't stay in CAD. The boards were manufactured by JLCPCB and hand-assembled. The housing, coolant plate and slide plates were CNC-machined and anodised, gaskets were cut from NBR sheet, and the remaining hardware was 3D printed in ASA. Testing was staged, subsystem by subsystem.

- **Electronics.** The motor control board ran the brushless pump motor smoothly across the full PWM range first time. The gauge board needed a grounding fix and extra PWM smoothing before the LED bar read steadily. That is exactly what staged bench testing is for, and both fixes are in the next board revision.
- **Engine fitment.** The pump assembly mounted directly to the 13B-MSP on the OEM OMP interface and sealed against the original engine geometry, with practical hose and tool access. This was a fitment check.
- **Fluid testing.** The coolant loop flowed cleanly with no external leaks, and the pump circulated oil and produced measurable flow. I saw no cross-leakage between the oil and coolant loops, which supports the sectioned sealing architecture. I haven't recorded the test duration or pressures here, so that isn't a long-term seal result.
- **On-engine oil comparison.** I ran the engine on the chosen ashless bio-ester oil through an external feed and compared it with the earlier 10W-30 baseline under the same warm-up and rev pattern. The hydrocarbon emissions trace improved clearly. That was one qualitative comparison of the oil and feed method, not a test of the EnduraOMP pump, and I haven't put numbers on it here.

{% include figure.html src="/Images/enduraomp-engine-2.webp" alt="CAD render of the EnduraOMP pump on the 13B-MSP seen from the other side, with the pulley and the coolant and oil lines visible" caption="The fitment from the other side. Render." class="fig-medium" %}

## Limitations and next steps

The prototype's deliberately relaxed machining tolerances, chosen so a one-off assembly would go together, cost volumetric efficiency through internal leakage at the slide-plate interfaces. The next iteration is about tighter control of those faces, not a new layout. The electronics need a stronger ground pour and hardware-level signal filtering. And the big one is a full instrumented on-engine test campaign to validate flow behaviour, thermal interaction and fault handling under real load.

The project doesn't claim production readiness. What it shows is that treating rotary lubrication as a controlled, testable, user-visible subsystem is a credible and buildable route to a more reliable rotary engine.

*Curious about the stock system this replaces? My [RX-8 OMP guide](/ProjectPages/RX8/OMP/) covers how Mazda's metering pump works, how to diagnose it and how to service it.*
