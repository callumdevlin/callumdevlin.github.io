---
title: How the RX-8 Renesis OMP Works
crumb: How the OMP works
permalink: /ProjectPages/RX8/OMP/how-it-works/
type: explainer
section: omp
nav_order: 1
applies: Series 1 RX-8 (2003-2008). Mazda figures are from the 2003 manual; later PCM calibrations may differ.
reviewed: 2026-10-14
description: >
  How the Series 1 RX-8 oil metering pump delivers oil: the engine-driven
  pumping, stepper-motor stroke control, what the PCM does at start-up, while
  running and at shut-down, the position switch, and the fail-safe.
---

The Series 1 RX-8 meters oil into the engine with a pump that is driven by the engine and adjusted by a stepper motor. The PCM decides how much oil each stroke should deliver; the engine decides how often the pump strokes. This page explains the parts, the logic and the fail-safe, using Mazda's own wording wherever it exists.

In brief:

- Engine rotation drives the pumping, so delivery rises and falls with engine speed.
- The stepper motor sets the stroke (how much oil per pumping event). The PCM commands it in steps.
- The PCM can't read the stepper's position directly. It re-establishes zero at every engine start, and the only feedback is a single position switch that gives one yes/no signal.
- If the PCM decides the stepper or switch has failed, it falls back to a fixed step (step 7) and restricts the engine.

Want to see it working rather than read about it? The [RX-8 OMP Lab](/ProjectPages/RX8/OMP/lab/) lets you move engine speed and replay the start-up checks.

## What's in the pump

[Mazda's sectional view](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html) labels these parts:

| Part | What it does |
| :--- | :--- |
| Stepping motor | Turns the control pin when the PCM energises coils No.1 to No.4 |
| Control pin | Sets the effective plunger stroke |
| Plunger, differential plunger and sub-plunger | The pumping elements |
| Driving worm | Moves the plungers. It is driven by the eccentric shaft through a driven gear |
| Positioning switch | On/off feedback to the PCM about the stepper's position |
| Oil inlet and oil outlets | Oil in from the engine; metered oil out through pipes to the nozzles |

Outside the pump, the system also has the oil pipes (with their banjo/connector bolts), the oil nozzles and a small air hose with a one-way check valve. The [nozzles page](/ProjectPages/RX8/OMP/nozzles-premix/) covers those.

## How oil is delivered

Two things happen at once:

1. The engine drives the pumping. The eccentric shaft turns the driven gear, which turns the driving worm, which moves the plunger and differential plunger. More engine speed means more pumping events.
2. The PCM sets the stroke. The PCM sends pulses to the stepper motor; the motor rotates the control pin; the control pin changes the plunger stroke. A bigger stroke delivers more oil per event.

> Stepper position → control pin → plunger stroke → oil per pumping event

The stepper does not pump oil itself. If the engine isn't turning, nothing is pumped whatever the step is.

The metered oil goes through the outlet pipes to two nozzles per rotor, tilted towards the side housing. Mazda says this was done to improve lubrication of the side housing and side seals, which matters because the Renesis breathes through side exhaust ports. [Mazda's construction page](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html) says the pulse signal is set by engine rotation, coolant temperature and the amount of intake air.

## What the PCM does, and when

The control logic, from [Mazda's control page](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T38.html):

| When | What happens |
| :--- | :--- |
| Ignition ON, engine stopped | Current to the stepper coils is cut to save battery. |
| Engine start (about 500 rpm) | Initial set: the PCM reverses the stepper 60 steps and detects the 0-step position. That becomes the reference for regular drive. This happens at every start. |
| After initial set, when the conditions are met | Monitor (position check): the PCM rotates the stepper 60 steps clockwise from step 0 and counts steps until the position switch turns on. It expects this above step 52. If it doesn't, the PCM decides there is a stepping-motor malfunction and activates fail-safe. |
| Running | Regular drive: the PCM works out a target step from engine rotation, coolant temperature and intake air amount (Mazda's wording), then steps the motor towards it. A step number below the target is increased (more stroke, more oil); one above it is reduced. |
| Ignition OFF | The PCM sets the target to step 0 and ends control once the actual step reaches 0. |

Mazda lists two conditions for the monitor: "ignition switch at ON for the 12th time" and "when the battery terminals are connected". It doesn't say which one, or both, is required, so don't treat the monitor as something that runs at every start. The initial set does run at every start.

The block diagram on the [same page set](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T37.html) shows the PCM's inputs as the ECT sensor, IAT sensor, BARO sensor, eccentric shaft position sensor, the metering oil pump switch and the ignition switch.

### How the stepper is driven

The motor has four coils. For each step the PCM energises two of them, and the pattern repeats every four steps. Because the PCM only sends pulses, its idea of the position is a count, not a measurement.

| Step | Coils energised | PCM terminals |
| :--- | :--- | :--- |
| 0 (and 4, 8, ...) | No.1 and No.4 | 2W and 2Y |
| 1 (and 5, 9, ...) | No.1 and No.2 | 2W and 2AB |
| 2 (and 6, 10, ...) | No.2 and No.3 | 2AB and 2V |
| 3 (and 7, 11, ...) | No.3 and No.4 | 2V and 2Y |

(Coil No.1 is on PCM terminal 2W, No.2 on 2AB, No.3 on 2V and No.4 on 2Y.) You can read the PCM's current step with the MOP_POS PID.

## The position switch

The switch is not a position sensor. It gives the PCM one yes/no signal that changes near the top of the stepper's travel, so the PCM can prove the motor really moved. It can't say where the motor is anywhere else, and it can't say how much oil is being delivered. The PCM has no flow sensing at all, so a blocked pipe or nozzle sets no code.

Mazda describes the switch in several places that look contradictory until you read them together:

| Mazda document | What it says |
| :--- | :--- |
| Workshop manual, control operation | The position switch "is on above step 52". |
| 2004 RX-8 Service Highlights | The switch turns on when the stepping motor is at step 52 or more. |
| Workshop manual, operation check (scan tool) | Move the motor with MOP_POS, and MOP_SW should change from on to off at 53 steps or over. |
| Workshop manual, inspection and PCM terminals | With the engine stopped, resistance across the switch (terminals A-C) should be 400 Ω or less. At idle, PCM terminal 2N sits at 1.0 V or less except when the pump is commanded to its maximum position, where it reads battery voltage. |

Mazda's wording varies by one step (above 52, 52 or more, 53 or over), so treat the change as happening between steps 52 and 53.

Read together, those figures fit a switch whose contact conducts at low steps and opens at about step 52 or 53. The PCM's input then goes high (battery voltage) above that point, which is the "on" in the control page, while the scan-tool MOP_SW shows the opposite sense. Mazda doesn't spell this out, though its PCM terminal table does list the MOP_SW PID as On while the initial set function is running, which fits. It is still my reading of its figures, and it means that at rest the switch should read a low resistance, not an open circuit. Owners who have measured switches report tens to about a hundred ohms in the conducting region, and much more (over 1,000 Ω) on a failed one.

This is why a faulty switch, or its wiring, makes a healthy pump look dead, and why [Mazda's diagnostic order](/ProjectPages/RX8/OMP/testing/) checks connectors, wiring and the switch before replacing the pump.

## Fail-safe

When the monitor finds the stepper or switch faulty, the PCM goes into fail-safe. Mazda describes two parts of it:

- Metering: the control pin is held at minimum stroke, so the oil supply is proportional to engine rotation only. The control page gives this as the stepper fixed at step 7.
- Engine restriction: if the engine needs more oil than that minimum, the PCM restricts fuel injection and holds back engine speed to protect the seals. The control page says the PCM fixes the fuel-injection pulse width (at engine start the table says regular control, otherwise 4.50 ms plus ineffective injection time with the throttle open more than 13%, or 2.65 ms plus ineffective time) and fixes the ignition timing at 4.88 degrees CA. Mazda's table shows that one value for both the leading and trailing plugs.

Normal driving is possible if the engine's oil need is within the minimum discharge. Mazda doesn't publish an rpm limit. One 2005 [RX8Club thread](https://www.rx8club.com/series-i-tech-garage-22/mop-dtc-p1686-dtc-p1687-dtc-p1688-limp-mode-58119/) reports cars held to about 3,000 to 3,300 rpm, so treat that as experience, not specification. See [diagnostics](/ProjectPages/RX8/OMP/testing/#symptoms).

## PCM updates that changed the oil quantity

Mazda North America issued two PCM calibration updates that touched the oil metering. Emission Recall Campaign 4206F came in 2006 and concerned an oil-injection metering system that "may be inaccurate". The cars it covered and the exact change aren't clear from the text available. Technical Service Bulletin 01-014/08 (2004 to 2008 cars, issued 14 March 2008 and revised on the 17th) is about lack of power and low idle in hot weather. It blames poor sealing from carbon on the rotor housing, caused by lack of metering oil at start-up or insufficient ignition timing in high ambient temperature. The fix is a revised PCM calibration that increases the metering oil amount during engine start and recalibrates the hot-weather ignition timing. The bulletin text is on a [manual mirror](https://workshop-manuals.com/mazda/rx8/2rtr-1.3l/powertrain_management/emission_control_systems/catalytic_converter/component_information/technical_service_bulletins/customer_interest/0101408/mar/08/engine_controls_lack_of_engine_power/). I haven't found a UK or European equivalent, so if you're buying a car or chasing carbon problems, ask Mazda UK which calibration it has.

## Inside the pump (community teardown)

This section is from owners' teardowns, not Mazda. One RX8Club teardown describes the stepper driving a geared cam; moving the cam changes how far the cam followers travel, which changes how the brass sleeves move relative to the pistons. Oil enters when sleeve holes line up with pressurised engine-oil passages and is pushed to the exit holes as the sleeve turns.

A later contributor described two compound pistons, one small and one large, each with two pumping faces. The diameters quoted were:

| Piston | Small diameter | Large diameter |
| :--- | ---: | ---: |
| Small | 1.82 mm | 2.58 mm |
| Large | 3.84 mm | 5.43 mm |

The same thread gives a maximum stroke of about 1.5 mm and a minimum of about 0.5 mm. One contributor's best guess, from a calculated graph rather than a measurement, is that the larger piston starts to contribute at around step 21. Treat these as useful community figures, not Mazda data.

## Sources

- Mazda workshop manual, [OMP construction](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html), [control operation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T38.html), [control block diagram](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T37.html), [PIDs](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200102T05.html) and [operation inspection](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html).
- Mazda 2004 RX-8 [Service Highlights](https://www.manualslib.com/manual/804935/Mazda-Rx-8-2004.html?page=173) (switch wording).
- RX8Club: [OMP output and modification thread](https://www.rx8club.com/series-i-tech-garage-22/omp-oil-metering-pump-output-modification-268559/) (teardown geometry).

