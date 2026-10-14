---
title: "EnduraOMP: Controlled Lubrication for Rotary Engines"
crumb: EnduraOMP
permalink: /ProjectPages/EnduraOMP/
image: /Images/optimised/enduraomp-engine-1-1200.webp
reviewed: 2026-10-14
description: >
  My MEng individual project: an electronically controlled oil metering system for
  rotary engines, built as a machined prototype.
related:
  - /ProjectPages/RX8/enginedata/
  - /ProjectPages/RX8/OMP/
---

{% include figure.html src="/Images/enduraomp-engine-1.webp" alt="CAD render of the EnduraOMP pump, in green and black, mounted on the side of a Mazda 13B-MSP rotary engine with a clear oil line running to the engine" caption="The EnduraOMP pump on the 13B-MSP, replacing the stock oil metering pump on the OEM interface. Render." eager=true %}

EnduraOMP is my MEng individual project at the University of Strathclyde: a lubrication system for rotary (Wankel) engines built around an electronically controlled gear pump, a dedicated clean-oil tank and a dashboard oil-level gauge. The project ran from problem research through to a machined and assembled prototype of the pump, tank and gauge.

## The problem

Rotary engines are compact, smooth and power-dense, which is why they keep coming back, from Mazda's MX-30 R-EV range extender to UAV propulsion and generator sets. But they have never shaken their reputation for being short-lived, and the causes are closely linked:

- Seal wear and compression loss. Apex, side and corner seals slide at high speed against the housings and wear down, costing compression and power.
- Oil consumption and carbon build-up. Oil is deliberately burned in the chambers, and conventional crankcase oils leave ash deposits that foul plugs and stick seals.
- Thermal distortion. Large temperature differences across the housings distort sealing surfaces and accelerate the cycle.

Through teardown work, user research with rotary specialists and benchmarking, I identified internal lubrication as the place where an intervention would do the most good. It drives seal wear, deposits and thermal behaviour directly, yet the stock system gives the user no visibility and limited control.

## The stock system's delivery {#building-the-evidence-first}

Mazda doesn't publish how much oil the stock pump delivers, and I haven't measured it. For sizing I worked to an assumed schedule rising from about 0.15 mL/min at idle to about 6.5 mL/min at 9,500 rpm. How I log a running engine, and what the commanded pump step read, is in my [13B-MSP engine data notes](/ProjectPages/RX8/enginedata/).

## Design development {#the-design}

### The pump

The pump is an external gear pump driven by a 12 V brushed DC gearmotor. It delivers a repeatable volume per revolution and is controlled by PWM, so delivery isn't slaved to engine speed. A first concept ran the oil through a central gear pump surrounded by coolant channels, but it proved impractical to seal and machine. After four iterations I settled on a sectioned housing, much as a rotary engine is built up in layers, so coolant channels surround the pump cavity to warm the oil on a cold start while the oil and coolant loops stay sealed from each other. A flow simulation showed continuous coolant flow around the pump with no stagnant regions and a temperature drop of about 10 K across the path.

The housing and coolant plate are CNC-machined 6063 aluminium, chosen from a materials screening for corrosion resistance and machinable sealing faces. Brass slide plates act as sacrificial wear faces, the covers are 3D-printed ASA, and NBR perimeter gaskets replaced the individual O-rings of the first design to cut the number of leak paths. Two O-rings remain, in grooves on the coolant plate. The pump mounts on the original oil pump interface through an aluminium bracket that also blanks off the old oil galleries. I settled the 30° upward angle of the mount with clay models, because it gave the clearest access to the bolts and hoses.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/enduraomp-pump.webp" alt="Render of the EnduraOMP pump unit: a dark grey body with two oil ports at one end and a green anodised mid-section" caption="The pump unit. Render." %}
{% include figure.html src="/Images/enduraomp-pump-internals.webp" alt="Render of the pump with its cover off, showing the ESP32 control board and its connectors fixed to the motor end" caption="The same assembly with the control board exposed. Render." %}
</div>

{% include figure.html src="/Images/enduraomp-pump-section.jpg" alt="Transparent render of the pump in section: the gear set at the centre inside a green coolant jacket, the motor and control electronics to the right" caption="Section render: the gear set sits at the core, wrapped by the coolant jacket." class="fig-medium" %}

### Control

<span id="what-i-was-aiming-for"></span>The control board is an ESP32 PCB built into the pump body. The idea is that a calibrated map, not a fixed mechanical relationship, sets the flow from engine speed and condition: higher flow for cold starts, stable low flow at hot idle and scaled delivery under high load. The architecture reads engine speed, oil temperature, oil pressure and tank level. The prototype firmware is a simpler feed-forward map from engine speed, taken from tachometer pulses, with corrections for cranking, high load and hot running. It also runs a short priming event at ignition and has a limp mode for critically low oil and a fault state for implausible sensor readings. I haven't tested those responses on an engine.

The same hardware is meant to suit automotive, generator and UAV duty, with only the calibration maps and protective actions changing. I have only worked with the 13B-MSP.

### Tank and gauge

The tank is a dedicated 1 L external reservoir, so the engine injects clean, purpose-chosen oil rather than drawing from the sump. I chose Renewable Lubricants' Bio-Rotary, an ashless, ester-based oil made for rotary engines, because ash from crankcase oil is a major source of deposits. A float-type resistive sender low in the tank warns of low oil before the pump can ingest air, a mesh filter sits in the filler neck, and mirrored outlet ports let the same tank serve either side of an installation.

<div class="fig-grid" markdown="0">
{% include figure.html src="/Images/enduraomp-tank.webp" alt="Render of a polished aluminium oil tank with a screw cap, mounting studs on one side and a hose barb at the bottom" caption="The oil reservoir. Render." %}
{% include figure.html src="/Images/enduraomp-tank-xray.webp" alt="Cutaway render of the tank showing the oil level and a float-type level sender inside" caption="Cutaway: a float-type level sender feeds the gauge. Render." %}
</div>

The gauge is a separate dashboard module with a 12-segment LED bar, driven by an LM3914 from a PWM signal and zoned green, amber and red. I chose an analogue bar driver over a digitally addressed display so the indicator depends as little as possible on firmware. Rotary ownership normally means careful dipstick checks, and this puts the oil level where you can see it.

{% include figure.html src="/Images/enduraomp-gauge-lit.webp" alt="Render of a round dashboard gauge with an LED bar showing the oil level" caption="The LED bar gauge: oil level at a glance, no dipstick. Render." class="fig-narrow" %}

## Prototyping {#prototype-and-bench-testing}

The boards were manufactured by JLCPCB and hand-assembled. The pump housing, coolant plate and slide plates were CNC-machined externally and anodised, gaskets were cut by hand from 1 mm NBR sheet, and the remaining parts were printed in ASA. An early translucent 3D-printed gear pump had already checked that the gears meshed and the gasket sealed. The tank is an existing tank modified to take the level sender, with a machined cap, and the gauge base is laser-cut steel that bends to fit different mounting surfaces.

For the one-off pump I controlled only the functionally important features tightly and left the rest at ±0.1 mm, biasing the slide plates slightly undersize and the housing slightly oversize so that it would go together. That choice cost efficiency later.

## Testing

I tested the prototype subsystem by subsystem.

- Electronics. The motor control board ran the motor smoothly across the PWM range. The gauge board had its data-connector ground missing from the regulator ground, which I fixed with a jumper, and its bar was jittery until I averaged the PWM signal over a longer window. Both fixes are planned for the next board revision.
- Engine fitment. The pump mounted on the OEM pump interface with practical hose and tool access, and the original seal sealed against the engine. This was a fitment check.
- Fluid. The coolant loop flowed smoothly with no external leaks, and the pump moved oil from the tank through the circuit. I didn't measure the volume, and the flow was less consistent than intended, most likely from internal leakage across the slide-plate interfaces. There was no leakage between the oil and coolant loops.

{% include figure.html src="/Images/enduraomp-engine-2.webp" alt="CAD render of the EnduraOMP pump on the 13B-MSP seen from the other side, with the pulley and the coolant and oil lines visible" caption="The fitment from the other side. Render." class="fig-medium" %}

## Outcome

The tests showed that the design can be built, assembled, mounted on the engine, controlled and fluid-tested at prototype level. The installed system is estimated at about 1.9 kg including 860 g of oil in a full tank, against about 2.9 kg for the stock pump and its drive, a saving of about 1 kg. A design-stage costing came to about £330 a unit to manufacture. I also took the concept back to rotary specialists, vehicle mechanics and an engineer. They were broadly positive about the dedicated tank and the visible oil level, and raised the same practical points as the tests: tolerance control in the pump, positive gasket location and electrical grounding.

The pump hasn't yet run on an engine as a complete system, so there is no durability result. What the project shows is that treating rotary lubrication as a controlled, testable, user-visible subsystem is a buildable route to a more reliable rotary engine.

## Further development {#limitations-and-next-steps}

The main next step is an instrumented on-engine test of the pump, to assess flow, thermal behaviour, transient response and fault handling under real load. Tighter control of the slide-plate faces would improve volumetric efficiency, and the electronics need a larger ground pour and better filtering. After that come a direct ECU interface so engine signals can be used without extra sensing, fault logging, and calibration maps for automotive, generator and UAV duty.
