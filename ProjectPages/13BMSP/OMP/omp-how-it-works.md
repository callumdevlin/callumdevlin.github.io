---
layout: default
title: "Mazda RX-8 S1 Renesis Oil Metering Pump Guide"
description: "A practical technical guide to the Series 1 Mazda RX-8 Renesis oil metering pump system, covering how it works, diagnostics, servicing, installation, oil nozzles, premix and clean oil feed systems."
permalink: /ProjectPages/13BMSP/OMPGuide/omp-guide.md
categories: [automotive, rotary-engines]
tags: [mazda-rx8, series-1-rx8, renesis, oil-metering-pump, omp, rotary-engine, maintenance]
sitemap: true
published: false
---

### How the RX-8 Renesis OMP works

The RX-8 Renesis was designed around side exhaust ports rather than the peripheral exhaust port layout used on some earlier Mazda rotary engines. This changed how Mazda approached oil injection.

Mazda states that the Renesis uses two oil nozzles per rotor to improve lubrication in the side housing and side seal area. These nozzles are tilted towards the side housing so oil is injected directly towards the side housing.

The stock system uses engine oil as the metered oil source. This oil is drawn from the engine oil system, metered by the OMP, sent through the pipes and injected into the engine.

After injection, this oil is not recovered. It is burned as part of combustion, which is why regular oil level checking is part of normal RX-8 ownership.

### Main Components of the OMP System
The Series 1 OMP system can be broken down into several smaller parts:
[Mazda’s sectional view:](https://www.manualslib.com/manual/804935/Mazda-Rx-8-2004.html?page=58) of the Series 1 pump identifies the positioning switch, control pin, plunger, driving worm, oil inlet, oil outlet, stepping motor, differential plunger and sub-plunger.


| Component                        | Function                                                       |
| -------------------------------- | -------------------------------------------------------------- |
| Metering oil pump body           | Houses the internal metering and pumping mechanism             |
| Stepping motor                   | Moves the control mechanism according to PCM commands          |
| Control pin                      | Changes the effective plunger stroke                           |
| Plunger and differential plunger | Mechanical pumping elements                                    |
| Driving worm                     | Drives the oil discharging mechanism                           |
| Driven gear                      | Transfers drive from the eccentric shaft to the pump mechanism |
| Positioning switch               | Allows the PCM to monitor OMP position                         |
| Oil inlet                        | Supplies oil into the pump                                     |
| Oil outlets                      | Send metered oil towards the oil nozzles                       |
| Connector bolts / banjo fittings | Join oil pipes to the OMP outlets                              |
| Oil pipes                        | Carry oil from the pump to the nozzles                         |
| Oil nozzles                      | Inject oil towards the side housing area                       |
| One-way check valve              | Prevents unwanted reverse flow in the nozzle/air hose side     |
| PCM                              | Calculates and controls the required OMP position              |


### How the Pump is Driven Mechanically
Although the OMP is electronically controlled, the pumping action is mechanical.

Mazda describes the oil discharging mechanism as consisting of the plunger and differential plunger, driven by the driving worm. The driving worm itself is driven by the eccentric shaft through a driven gear.

That means the pump has two different things happening at the same time:

1. Mechanical rotation from the engine
    - The eccentric shaft drives the pump mechanism.
    - As engine speed increases, the mechanical pumping events increase.
    - This gives a base relationship between engine speed and oil delivery.
2. Electronic stroke control from the PCM
    - The PCM commands the stepping motor.
    - The stepping motor changes the control pin position.
    - This changes the plunger stroke.
    - More stroke means more oil per pumping event.
    - Less stroke means less oil per pumping event.

This is why the pump can deliver different amounts of oil at different operating conditions.

### How the PCM Controls Oil Delivery

The PCM calculates the required oil delivery and converts it into a stepper motor step number.

Mazda’s control description states that the PCM calculates the optimum amount of oil delivery as a stepping motor step number by determining engine operating conditions from input signals, then sends an operation signal to the stepping motor inside the metering oil pump.

The service highlights list the following relevant inputs in the OMP control block diagram:

| Input                           | Why it matters                                                               |
| ------------------------------- | ---------------------------------------------------------------------------- |
| ECT sensor                      | Engine coolant temperature affects oiling requirements and warm-up behaviour |
| IAT sensor                      | Intake air temperature helps define operating condition                      |
| BARO sensor                     | Barometric pressure affects load/air calculation                             |
| Eccentric shaft position sensor | Provides engine speed/position information                                   |
| Metering oil pump switch        | Used for OMP position monitoring                                             |
| Ignition switch                 | Used for start, stop and initialisation logic                                |

Mazda also states that the PCM changes the plunger stroke by controlling the stepping motor rotation amount, or step number. The stepping motor uses coils No.1 to No.4 according to the commanded step number, and Mazda notes that the step number can be checked using the WDS data monitor PID MOP POS.

### Stepper Motor and Plunger Stroke Control

A stepper motor moves in small increments. This is useful because the PCM can command a specific position rather than only switching the pump on or off.

A simplified explanation is:
- Low step number  = smaller plunger stroke = less oil
- High step number = larger plunger stroke  = more oil

This is not the same as saying the electric motor directly pumps the oil. The stepper motor controls the stroke setting. The engine-driven internal mechanism still provides the repeating pumping action.

A useful way to think about it is:

Stepper motor position
        ↓
Control pin angle / position
        ↓
Allowed plunger stroke
        ↓
Oil volume per pump event

When the PCM wants more oil, it commands a position that increases plunger stroke. When the PCM wants less oil, it reduces the commanded stroke.

Mazda’s regular drive function explains this directly: if the actual step number is less than the target, the PCM increases the step number, increasing plunger stroke and oil delivery. If the actual step number is larger than target, the PCM lowers the step number, reducing plunger stroke and oil delivery.

### Initial-Set Function

At engine start, the PCM needs a known OMP reference position.

Mazda’s initial-set function reverses the stepping motor 60 steps at engine start and detects the 0-step position. This 0-step position then becomes the reference for regular drive operation.

This matters because a stepper motor normally counts movement from a known reference. If the PCM does not know where the OMP is, it cannot confidently command the correct amount of oil.

The basic sequence is:

Engine start
        ↓
PCM reverses stepper motor 60 steps
        ↓
0-step reference is detected
        ↓
PCM begins regular drive control

This is why the OMP is not just a passive oil fitting. It is actively managed every time the engine starts.

### OMP Position Sensor

Mazda describes this switch as detecting the fully open position of the stepping motor during the metering oil pump learning function. It turns on when the stepping motor is at step 52 or more.

The monitor function is used after the initial-set function. Mazda states that the PCM rotates the stepping motor 60 steps clockwise from the 0-step position, counts the step number until the position switch turns on, and expects the switch to be on above step 52. If the on-position is not detected above step 52, the PCM determines a stepping motor malfunction and activates fail-safe.

This means the switch is not used as a continuous position sensor in the same way as a throttle position sensor. It is more like a reference/confirmation device used to prove the pump has moved to the expected region.

Additionally, Mazda states that after the ignition switch is turned off, the PCM sets the target step to step 0. Once the actual step reaches 0, metering oil pump control ends.

Mazda also states that when the ignition is ON but the engine is stopped, current flow to the stepper motor coils is stopped to save battery consumption.

This means the OMP is actively returned to a known state rather than simply being left wherever it happened to be when the engine stopped.

### Internal Metering Mechanism

One RX8Club teardown describes the OMP as having a stepper motor that drives a geared cam regulated by a position sensor. The same post describes the stepper motor moving the cam, which lets the cam followers move further, changing how the brass pump sleeves move relative to the pump pistons. It also describes oil entering when sleeve holes align with pressurised engine oil holes, then being pumped to the exit holes as the sleeve rotates and aligns.

The RX8Club teardown discussion describes the Series 1 OMP as effectively having four pumping sections: two smaller and two larger. The post explains that the small pump begins contributing sooner, while the larger pump rotates/pumps faster and adds more oil delivery as commanded output increases.

Another RX8Club member later corrected and expanded the dimensional interpretation, describing the pump as having two compound pistons: one small and one large. Each piston has two pumping faces: one at the small-diameter end and one formed by the shoulder between the small and large diameters. The measured diameters given in that post were:

| Pump element          | Small diameter | Large diameter |
| --------------------- | -------------: | -------------: |
| Small compound piston |        1.82 mm |        2.58 mm |
| Large compound piston |        3.84 mm |        5.43 mm |

The same post notes that the large-to-small diameter ratio is approximately 1.41 for both pistons. This matters because the shoulder area can be arranged to pump a similar volume to the smaller face area.

### Fail-Safe Behaviour

Mazda describes the fail-safe function as operating when a failure is detected in the stepping motor or positioning switch. When fail-safe operates, the PCM keeps the control pin at the minimum stroke position, so oil supply is only proportional to engine rotation rate and the minimum oil amount for each engine speed is supplied.

Mazda also states that if the engine requires more oil than the minimum discharge, fuel injection is restricted, engine speed increase is suppressed, and seizure of the internal seals is prevented.

The control-system fail-safe page adds that when the monitor function determines the stepping motor is malfunctioning, the fail-safe controls fuel injection time, ignition timing and the target step for the stepping motor to protect the engine and prevent burning of engine seals. It also shows the metering oil pump control being fixed at step 7 in fail-safe.