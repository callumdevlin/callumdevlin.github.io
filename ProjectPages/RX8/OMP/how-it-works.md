---
title: How the RX-8 Renesis OMP Works
permalink: /ProjectPages/RX8/OMP/how-it-works/
description: >
  How the Series 1 RX-8 oil metering pump delivers oil — the mechanical drive,
  stepper-motor stroke control, the PCM's initial-set and monitoring functions,
  and what's physically inside the pump.
---

The RX-8 Renesis was designed around side exhaust ports rather than the peripheral exhaust layout used on earlier Mazda rotaries, and this changed how Mazda approached oil injection.

Mazda states that the Renesis uses two oil nozzles per rotor to improve lubrication in the side housing and side seal area. These nozzles are tilted so that oil is injected directly towards the side housings.

The stock system meters **engine oil**: oil is drawn from the engine's oil system, metered by the OMP, sent through the pipes and injected into the engine. After injection this oil is not recovered — it is burned as part of combustion, which is why regular oil level checking is part of normal RX-8 ownership.

## Main Components of the OMP System

The Series 1 OMP system breaks down into the following parts. [Mazda's sectional view](https://www.manualslib.com/manual/804935/Mazda-Rx-8-2004.html?page=58) of the Series 1 pump identifies the positioning switch, control pin, plunger, driving worm, oil inlet, oil outlet, stepping motor, differential plunger and sub-plunger.

| Component | Function |
| :--- | :--- |
| Metering oil pump body | Houses the internal metering and pumping mechanism |
| Stepping motor | Moves the control mechanism according to PCM commands |
| Control pin | Changes the effective plunger stroke |
| Plunger and differential plunger | Mechanical pumping elements |
| Driving worm | Drives the oil discharging mechanism |
| Driven gear | Transfers drive from the eccentric shaft to the pump mechanism |
| Positioning switch | Allows the PCM to monitor OMP position |
| Oil inlet | Supplies oil into the pump |
| Oil outlets | Send metered oil towards the oil nozzles |
| Connector bolts / banjo fittings | Join oil pipes to the OMP outlets |
| Oil pipes | Carry oil from the pump to the nozzles |
| Oil nozzles | Inject oil towards the side housing area |
| One-way check valve | Prevents unwanted reverse flow in the nozzle/air hose side |
| PCM | Calculates and controls the required OMP position |

## How the Pump Is Driven Mechanically

Although the OMP is electronically controlled, the pumping action itself is mechanical.

Mazda describes the oil discharging mechanism as consisting of the plunger and differential plunger, driven by the driving worm — which is itself driven by the eccentric shaft through a driven gear. So the pump has two things happening at once:

1. **Mechanical rotation from the engine.** The eccentric shaft drives the pump mechanism, so as engine speed increases, the pumping events increase. This gives a base relationship between engine speed and oil delivery.
2. **Electronic stroke control from the PCM.** The PCM commands the stepping motor, the stepping motor changes the control pin position, and the control pin changes the plunger stroke. More stroke means more oil per pumping event; less stroke means less.

This combination is why the pump can deliver different amounts of oil at different operating conditions.

## How the PCM Controls Oil Delivery

The PCM calculates the required oil delivery and converts it into a stepping motor step number. Mazda's control description states that the PCM calculates the optimum amount of oil delivery as a step number by determining engine operating conditions from its input signals, then sends an operation signal to the stepping motor inside the pump.

The relevant inputs in the OMP control block diagram are:

| Input | Why it matters |
| :--- | :--- |
| ECT sensor | Engine coolant temperature affects oiling requirements and warm-up behaviour |
| IAT sensor | Intake air temperature helps define operating condition |
| BARO sensor | Barometric pressure affects load/air calculation |
| Eccentric shaft position sensor | Provides engine speed/position information |
| Metering oil pump switch | Used for OMP position monitoring |
| Ignition switch | Used for start, stop and initialisation logic |

The PCM changes the plunger stroke by controlling the stepping motor's rotation amount — the step number. The stepping motor uses coils No.1 to No.4 according to the commanded step, and the current step number can be checked using the WDS data monitor PID `MOP POS` (also accessible via Forscan — see my [logged engine data](/ProjectPages/RX8/enginedata/) for real values across the rev range).

## Stepper Motor and Plunger Stroke Control

A stepper motor moves in small increments, which means the PCM can command a specific *position* rather than only switching the pump on or off. As a simplified rule:

- Low step number = smaller plunger stroke = less oil
- High step number = larger plunger stroke = more oil

Note this is **not** the same as the electric motor pumping the oil directly. The stepper motor sets the stroke; the engine-driven internal mechanism still provides the repeating pumping action. The chain of control is:

> Stepper motor position → control pin position → allowed plunger stroke → oil volume per pump event

Mazda's regular drive function describes this directly: if the actual step number is less than the target, the PCM increases the step number, increasing plunger stroke and oil delivery; if it is larger than target, the PCM lowers it, reducing delivery.

## Initial-Set Function

At engine start, the PCM needs a known OMP reference position. Mazda's initial-set function reverses the stepping motor 60 steps at engine start and detects the 0-step position, which then becomes the reference for regular drive operation.

This matters because a stepper motor counts movement from a known reference — if the PCM doesn't know where the OMP is, it can't confidently command the correct amount of oil. The sequence is:

> Engine start → PCM reverses stepper 60 steps → 0-step reference detected → regular drive control begins

The OMP is therefore not a passive fitting; it is actively re-referenced every time the engine starts.

## OMP Position Switch & Monitor Function

Mazda describes the positioning switch as detecting the fully-open region of the stepping motor: it turns on when the motor is at **step 52 or more**.

The monitor function runs after the initial-set: the PCM rotates the stepping motor 60 steps clockwise from the 0-step position and counts steps until the switch turns on, expecting it above step 52. If the on-position is not detected above step 52, the PCM determines a stepping motor malfunction and activates fail-safe.

So the switch is not a continuous position sensor like a throttle position sensor — it's a reference/confirmation device that proves the pump has actually moved to the expected region. This distinction matters enormously for diagnosis: a faulty *switch* makes a healthy *pump* look dead. See [diagnostics & testing](/ProjectPages/RX8/OMP/testing/).

Two further details from Mazda's description: after the ignition is switched off, the PCM commands the target step to 0 and ends metering control once it's reached — so the pump is actively returned to a known state rather than left wherever it stopped. And with ignition ON but the engine stopped, current to the stepper coils is cut to save battery.

## Internal Metering Mechanism

Community teardowns add useful detail to Mazda's description. One RX8Club teardown describes the stepper motor driving a geared cam regulated by the position sensor; moving the cam lets the cam followers travel further, changing how the brass pump sleeves move relative to the pump pistons. Oil enters when sleeve holes align with pressurised engine oil passages, and is pumped to the exit holes as the sleeve rotates into alignment.

That discussion initially described the Series 1 OMP as having four pumping sections — two smaller, two larger — with the small pump contributing sooner and the larger adding delivery as commanded output increases. A later contributor refined the dimensional interpretation: the pump has **two compound pistons**, one small and one large, each with two pumping faces — one at the small-diameter end and one formed by the shoulder between the small and large diameters. The measured diameters given were:

| Pump element | Small diameter | Large diameter |
| :--- | ---: | ---: |
| Small compound piston | 1.82 mm | 2.58 mm |
| Large compound piston | 3.84 mm | 5.43 mm |

The large-to-small diameter ratio is approximately 1.41 for both pistons — which matters because it lets the shoulder area pump a similar volume to the smaller face area.

## Fail-Safe Behaviour

Mazda describes the fail-safe function as operating when a failure is detected in the stepping motor or positioning switch. When fail-safe operates, the PCM holds the control pin at the **minimum stroke position**, so oil supply becomes proportional to engine rotation alone and the minimum oil amount for each engine speed is supplied.

If the engine would require more oil than that minimum discharge, the PCM restricts fuel injection and suppresses engine speed increase, preventing seizure of the internal seals. The control-system fail-safe description adds that the PCM controls fuel injection time, ignition timing and the stepper target to protect the engine, with metering oil pump control fixed at **step 7** in fail-safe — the "limp mode" RX-8 owners know, typically capping the engine around 3,000 RPM.

*Next: [diagnostics & testing](/ProjectPages/RX8/OMP/testing/), including the fault codes that trigger this fail-safe.*
