---
title: How the RX-8 Renesis OMP Works
crumb: How the OMP works
permalink: /ProjectPages/RX8/OMP/how-it-works/
section: omp
nav_order: 1
applies: Series 1 RX-8 (2003-2008). Mazda figures are from the 2003 manual; later PCM calibrations may differ.
reviewed: 2026-10-14
description: >
  How the Series 1 RX-8 oil metering pump delivers oil: engine-driven pumping, stepper
  stroke control, what the PCM does at start-up, running and shut-down, the position
  switch, and the fail-safe.
---

The pump is driven by the engine and adjusted by a stepper motor. The engine decides how often the pump strokes; the PCM decides how much oil each stroke delivers.

- Engine rotation drives the pumping, so delivery rises and falls with engine speed.
- The stepper sets the stroke (oil per pumping event). The PCM commands it in steps.
- The PCM can't read the stepper's position. It re-establishes zero at every engine start, and its only feedback is one yes/no position switch.
- If the PCM decides the stepper or switch has failed, it falls back to a fixed step (step 7) and restricts the engine.

To see it working, the [RX-8 OMP Lab](/ProjectPages/RX8/OMP/lab/) lets you move engine speed and replay the start-up checks.

## What's in the pump

From [Mazda's sectional view](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html):

| Part | What it does |
| :--- | :--- |
| Stepping motor | Turns the control pin when the PCM energises coils No.1 to No.4 |
| Control pin | Sets the effective plunger stroke |
| Plunger, differential plunger, sub-plunger | The pumping elements |
| Driving worm | Moves the plungers; driven by the eccentric shaft through a driven gear |
| Positioning switch | On/off feedback to the PCM about the stepper's position |
| Oil inlet and outlets | Oil in from the engine; metered oil out through pipes to the nozzles |

Outside the pump are the oil pipes (with banjo/connector bolts), the nozzles, and a small air hose with a one-way check valve; see the [nozzles page](/ProjectPages/RX8/OMP/nozzles-premix/).

## How oil is delivered

1. **The engine drives the pumping.** The eccentric shaft turns the driven gear, then the driving worm, which moves the plungers. More rpm means more pumping events.
2. **The PCM sets the stroke.** Pulses turn the stepper, the stepper turns the control pin, and the pin changes the plunger stroke. A bigger stroke delivers more oil per event.

> Stepper position → control pin → plunger stroke → oil per pumping event

The stepper doesn't pump. If the engine isn't turning, nothing is pumped whatever the step.

Metered oil goes through the outlet pipes to two nozzles per rotor, tilted towards the side housing to lubricate the side housing and side seals, which matters because the Renesis breathes through side exhaust ports. Per Mazda, the pulse signal is set by engine rotation, coolant temperature and intake air amount.

## What the PCM does, and when

From [Mazda's control page](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T38.html):

| When | What happens |
| :--- | :--- |
| Ignition ON, engine stopped | Stepper coil current is cut to save battery. |
| Engine start (about 500 rpm) | **Initial set:** the PCM reverses the stepper 60 steps and detects the 0-step position, which becomes the reference. Happens at every start. |
| After initial set, when conditions are met | **Monitor:** the PCM turns the stepper 60 steps clockwise from step 0 and counts steps until the position switch turns on, expecting above step 52. If not, it decides the stepping motor has malfunctioned and goes to fail-safe. |
| Running | **Regular drive:** the PCM works out a target step from engine rotation, coolant temperature and intake air amount, then steps towards it. Below target: more stroke, more oil. Above: less. |
| Ignition OFF | Target goes to step 0 and control ends when the actual step reaches 0. |

Mazda lists two conditions for the monitor, "ignition switch at ON for the 12th time" and "when the battery terminals are connected", without saying which, or both, is required. Don't treat the monitor as running at every start; the initial set does.

Per [Mazda's block diagram](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T37.html), the PCM's inputs are the ECT, IAT and BARO sensors, the eccentric shaft position sensor, the pump switch and the ignition switch.

### How the stepper is driven

The motor has four coils. For each step the PCM energises two, and the pattern repeats every four steps. The PCM only sends pulses, so its idea of position is a count, not a measurement. Read it with the MOP_POS PID.

| Step | Coils energised | PCM terminals |
| :--- | :--- | :--- |
| 0 (and 4, 8, ...) | No.1 and No.4 | 2W and 2Y |
| 1 (and 5, 9, ...) | No.1 and No.2 | 2W and 2AB |
| 2 (and 6, 10, ...) | No.2 and No.3 | 2AB and 2V |
| 3 (and 7, 11, ...) | No.3 and No.4 | 2V and 2Y |

Coil No.1 is on PCM terminal 2W, No.2 on 2AB, No.3 on 2V and No.4 on 2Y.

## The position switch

It isn't a position sensor. It gives one yes/no signal near the top of the stepper's travel so the PCM can prove the motor really moved. It can't say where the motor is elsewhere or how much oil is delivered. The PCM has no flow sensing, so a blocked pipe or nozzle sets no code.

Mazda's descriptions look contradictory until read together:

| Mazda document | What it says |
| :--- | :--- |
| Workshop manual, control operation | The switch "is on above step 52". |
| 2004 RX-8 Service Highlights | The switch turns on when the stepping motor is at step 52 or more. |
| Workshop manual, operation check (scan tool) | Move the motor with MOP_POS; MOP_SW should change from on to off at 53 steps or over. |
| Workshop manual, inspection and PCM terminals | Engine stopped, resistance across the switch (A-C) should be 400 Ω or less. At idle, PCM terminal 2N sits at 1.0 V or less except when the pump is commanded to maximum, where it reads battery voltage. |

The wording varies by one step (above 52, 52 or more, 53 or over), so treat the change as happening between steps 52 and 53.

My reading of those figures: the contact conducts at low steps and opens at about step 52 or 53. The PCM input then goes high above that point (the "on" in the control page), while the scan-tool MOP_SW shows the opposite sense. Mazda doesn't spell this out, though its terminal table lists the MOP_SW PID as On while the initial set runs, which fits. It means a good switch reads low resistance at rest, not open circuit. Owners report tens to about a hundred ohms in the conducting region and over 1,000 Ω on a failed one.

That is why a faulty switch or its wiring makes a healthy pump look dead, and why [Mazda's diagnostic order](/ProjectPages/RX8/OMP/testing/) checks connectors, wiring and the switch before the pump.

## Fail-safe

When the monitor finds the stepper or switch faulty, the PCM goes to fail-safe:

- **Metering:** the control pin is held at minimum stroke, so oil supply follows engine rotation only. The control page gives this as the stepper fixed at step 7.
- **Engine restriction:** if the engine needs more oil than that minimum, the PCM restricts fuel injection and holds back engine speed to protect the seals. It fixes the injection pulse width (at engine start, regular control; otherwise 4.50 ms plus ineffective injection time with the throttle open more than 13%, or 2.65 ms plus ineffective time) and the ignition timing at 4.88° CA. Mazda's table shows that one value for both leading and trailing plugs.

Normal driving is possible if the engine's oil need is within the minimum discharge. Mazda publishes no rpm limit. One 2005 [RX8Club thread](https://www.rx8club.com/series-i-tech-garage-22/mop-dtc-p1686-dtc-p1687-dtc-p1688-limp-mode-58119/) reports cars held to about 3,000-3,300 rpm; treat that as experience. See [diagnostics](/ProjectPages/RX8/OMP/testing/#symptoms).

## PCM updates that changed the oil quantity

Mazda North America issued two PCM calibration updates touching oil metering:

- **Emission Recall Campaign 4206F (2006):** concerned an oil-injection metering system that "may be inaccurate". The cars covered and the exact change aren't clear from the text available.
- **Technical Service Bulletin 01-014/08** (2004-2008 cars, issued 14 March 2008, revised the 17th): lack of power and low idle in hot weather, blamed on poor sealing from carbon on the rotor housing, caused by lack of metering oil at start-up or insufficient ignition timing in high ambient temperature. The fix is a revised PCM calibration that increases metering oil during engine start and recalibrates hot-weather ignition timing. The text is on a [manual mirror](https://workshop-manuals.com/mazda/rx8/2rtr-1.3l/powertrain_management/emission_control_systems/catalytic_converter/component_information/technical_service_bulletins/customer_interest/0101408/mar/08/engine_controls_lack_of_engine_power/).

I haven't found a UK or European equivalent, so when buying a car or chasing carbon problems, ask Mazda UK which calibration it has.

## Inside the pump (community teardown)

From owners' teardowns, not Mazda. One RX8Club teardown describes the stepper driving a geared cam; moving the cam changes how far the cam followers travel, and so how the brass sleeves move relative to the pistons. Oil enters when sleeve holes line up with pressurised engine-oil passages and is pushed to the exit holes as the sleeve turns.

A later contributor described two compound pistons, each with two pumping faces:

| Piston | Small diameter | Large diameter |
| :--- | ---: | ---: |
| Small | 1.82 mm | 2.58 mm |
| Large | 3.84 mm | 5.43 mm |

The same thread gives a maximum stroke of about 1.5 mm and a minimum of about 0.5 mm, and one contributor's guess, from a calculated graph, is that the larger piston starts to contribute around step 21. Treat these as community figures, not Mazda data.

## Sources

- Mazda workshop manual: [OMP construction](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html), [control operation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T38.html), [control block diagram](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T37.html), [PIDs](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200102T05.html) and [operation inspection](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html).
- Mazda 2004 RX-8 [Service Highlights](https://www.manualslib.com/manual/804935/Mazda-Rx-8-2004.html?page=173) (switch wording).
- RX8Club: [OMP output and modification thread](https://www.rx8club.com/series-i-tech-garage-22/omp-oil-metering-pump-output-modification-268559/) (teardown geometry).
