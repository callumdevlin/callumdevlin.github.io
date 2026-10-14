---
title: RX-8 OMP Diagnostics & Testing
crumb: OMP diagnostics
permalink: /ProjectPages/RX8/OMP/testing/
type: procedure
section: omp
nav_order: 2
applies: Series 1 RX-8 (2003-2008) factory OMP. Mazda's figures are from the 2003 manual.
reviewed: 2026-10-14
description: >
  Diagnosing the Series 1 RX-8 oil metering pump: symptoms, what codes
  P1686, P1687 and P1688 actually mean, Mazda's diagnostic order, the
  electrical and nozzle tests with Mazda's figures, and a result sheet.
---

Work from the cheap checks to the expensive ones. Mazda's own diagnostic flow does exactly that: connectors, power and wiring first, then the switch, and the pump itself only after those pass. An OMP fault code usually points to a connector, a wiring fault or the position switch rather than a worn-out pump, so read the codes and freeze-frame data and work through the [diagnostic order](#diagnostic-order) below before buying anything.

An engine run with a genuinely failed OMP and no premix can destroy its seals quickly. Take OMP warning lights seriously and, if in doubt, add premix to the fuel while you diagnose.
{:.note}

## Symptoms

| What you see | What it can mean |
| :--- | :--- |
| Check-engine light with P1686, P1687 or P1688 | The PCM's switch check failed. See the table below. |
| Engine feels restricted, won't rev freely | Fail-safe may be active (stepper fixed at step 7, injection and ignition fixed). Owners typically report being held to about 3,000 to 3,500 rpm. |
| Code only when hot, or after the car has sat | Often a corroded or stiff pump or connector (owners found coolant or water above the pump), or a marginal switch. |
| Oil level stops falling | Treat it as a warning, not a bonus: delivery may have stopped. The PCM has no flow sensing, so no code does not mean oil is flowing. |
| Oil weeping at the pump or pipe unions | Seal or washer problem. Check the pump-to-cover mating surface and the pipe connections. |
| Blue smoke | Oil is being burned: Mazda's smoke flow checks OMP control first, then compression, oil condition and pressure, then pipe and nozzle air or clogging. |

## Fault codes

Mazda's 2003 RX-8 manual has three OMP codes. All three are continuous monitors: the MIL comes on if the fault is seen in the first drive cycle, a pending code is set, freeze-frame data is recorded and the code is stored.

| Code | Mazda's title | What the PCM saw |
| :--- | :--- | :--- |
| P1686 | Metering oil pump control circuit, low flow side problem | The stepper was driven beyond the standard step, but the switch input stayed off. |
| P1687 | Metering oil pump control circuit, high flow side problem | The stepper was driven less than the standard step, but the switch input was on. |
| P1688 | Metering oil pump control circuit, initial check problem | The switch input was on during the stepper's initial check. |

All three share the same possible causes: the pump or its switch, a connector or terminal, an open or short to ground in the pump supply or coil wiring, or the PCM. P1686 adds an open in the switch wiring, and P1687 and P1688 add a short to ground on the switch wiring.

Some online code lists describe P1684 as a "position sensor circuit" fault and P1685 to P1688 as stepping-motor circuit faults, which people then read as four separate windings. That isn't what Mazda's 2003 RX-8 DTC table says. It lists only P1686, P1687 and P1688 for the metering oil pump, defined by switch state against stepper position, and each one's checks cover all four coil lines together, so a single code doesn't point at a single winding. Mazda's switch-inspection page mentions P1685 once in a caution, but there is no P1685 page or table entry. On Series 2 cars, owners report that P1684 and P1685 are pump oil-pressure codes, a different system.

## What goes wrong in practice

Mazda's flow lists every possible cause. Owner reports (RX8Club and similar, mostly from 2005 to 2022) suggest this order of likelihood. They are community experience, not Mazda data.

| Cause | What owners found |
| :--- | :--- |
| Water or coolant at the pump or its connector | A weeping hose or pipe above the pump drips onto it. Corroded, stiff internals and hot-start-only codes that cleared once cleaned and dried. See the [intermittent P1688 thread](https://www.rx8club.com/rx-8-discussion-3/oil-metering-intermittent-problem-266331/). |
| Position switch moved on the pump | One owner deliberately turned the switch to the end of its travel to get more oil flow (he estimated about 30 degrees; others in the thread estimated 10 to 19) and got an immediate code and limp mode. Backing it off by 5 to 10 degrees and resetting the ECU cleared it. See [MOP adjustments](https://www.rx8club.com/series-i-major-horsepower-upgrades-93/mop-adjustments-120276/) and the [servicing page](/ProjectPages/RX8/OMP/servicing/#position-switch-setting). |
| Worn or intermittent switch | A resistive track that wears or goes intermittent when hot. One switch measured 1,132 Ω against the 400 Ω limit and a used pump stopped the code, although the owner also suspected a harness short and had seen the same code with his old pump plugged in. His last report was "fixed for 5 miles so far" ([thread](https://www.rx8club.com/new-member-forum-197/p1688-limp-mode-please-help-272863/)). |
| Stuck mechanism | A stiff stepper freed with lubricant, after which the code cleared. |
| Harness and connector | A bare wire in the loom, salt or water in the 3-pin connector, no loom over it. |
| The pump itself | Replaced successfully in several cases, including units whose coils and switch read in spec. Used pumps sometimes fail again, or arrive mis-set. |
| The PCM | Last in Mazda's flow; no confirmed case appears in the owner reports. |

One poster, who said he did it "for training", reported that shorting two stepper coil wires produced all three codes at once ([thread](https://www.rx8club.com/series-i-tech-garage-22/mop-dtc-p1686-dtc-p1687-dtc-p1688-limp-mode-58119/)). That fits Mazda's logic: the codes describe the switch check, not which winding failed.

## Diagnostic order

This is Mazda's flow for P1686, P1687 and P1688, condensed. Do the steps in order and stop when you find the fault.

1. Record the freeze-frame data and check for related service information.
2. Inspect the pump connector for damaged, pulled-out or corroded pins.
3. Check the pump supply. Ignition on, engine off: voltage at pump terminals C and D (harness side) to body ground should be battery voltage (B+).
4. Check for shorts to ground. Ignition off: there should be no continuity from pump terminals A, E, B and F (harness side) to body ground.
5. Inspect the pump. Replace it if faulty.
6. Inspect the PCM connector.
7. Check for opens in the coil wiring. Ignition off: continuity between pump terminals A, E, B, F and PCM terminals 2V, 2W, 2Y, 2AB.
8. Inspect the switch connector.
9. Check the switch wiring. For P1686, check continuity from switch terminal A to PCM 2N and switch terminal C to PCM 1U (an open is the fault). For P1687 and P1688, check that switch terminal A is not shorted to ground.
10. Inspect the switch. If it is faulty, Mazda's remedy is to replace the pump (the switch is part of it).
11. Reconnect everything, clear the code, start the engine and see if it returns. Only if it does, replace the PCM. In owner reports a real fault tends to come straight back within seconds to a minute of starting (one reported about 15 seconds). That is experience, not Mazda. A code that returns only occasionally usually means a marginal connector, switch or water ingress, so go back to steps 2 to 10.
12. Do the after-repair procedure and check for other codes.

[Mazda: P1686](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010201600W01.html), [P1687](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010201600W02.html), [P1688](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010201600W03.html).

## Pump connections

| Connector | Terminal | Goes to |
| :--- | :--- | :--- |
| 6-pin (stepper) | C and D | Supply from the main relay (B+ with ignition on) |
| 6-pin | E | PCM 2W (coil No.1) |
| 6-pin | F | PCM 2AB (coil No.2) |
| 6-pin | A | PCM 2V (coil No.3) |
| 6-pin | B | PCM 2Y (coil No.4) |
| 3-pin (switch) | A | PCM 2N (switch signal) |
| 3-pin | C | PCM 1U (switch ground) |

## Electrical checks and Mazda's figures

All figures are at 20 °C. Disconnect the connector before measuring resistance.

| Check | How | Specification |
| :--- | :--- | :--- |
| Supply voltage | 6-pin connector, terminals C and D, ignition on | Battery voltage |
| Stepper winding resistance | 6-pin connector: D-B, D-F, C-A and C-E | 30.6 to 35.6 Ω each. Out of range: replace the pump. |
| Position switch resistance | Idle the engine, stop it, disconnect the 3-pin connector, measure A-C | 400 Ω or less. Out of range: replace the pump. At rest the switch should conduct, not read open. |

Mazda's diagnostic flow checks the harness side for shorts to ground (step 4 above). With the pump out, you can also check each winding terminal against the pump body, which should show no continuity; that check isn't in Mazda's inspection page.

### Switch check at the PCM

Mazda has a voltage check of the switch circuit at PCM terminal 2N, using the PCM's learning function:

1. Disconnect the negative battery terminal to clear the OMP control learning value, then reconnect.
2. Measure at PCM terminal 2N: ignition ON: 0 V; just after engine start: B+; idling after start: 0 V.
3. If the readings are wrong but the wiring is good, replace the pump.

Mazda says this inspection can't be done correctly if the stepper is faulty, so check that P1685, P1686, P1687 and P1688 are not stored first. It also gives wiring checks from switch terminal A to PCM 2N and C to PCM 1U (no open) and from A to ground and to the power supply (no short).

### Live data

With a scan tool that shows the PIDs (Mazda's procedure uses WDS), watch MOP_POS (the PCM's step count) and MOP_SW (the switch). Mazda's operation check moves the motor with MOP_POS and expects MOP_SW to change at 53 steps or over. If it changes, Mazda then sends you to the oil pipe (leaks or cracks between pump and nozzle), the nozzle (clogging) and the hose between the intake manifold and the nozzle (clogging, leaks, poor connection). If it doesn't change, check the motor and switch and replace the pump if faulty.

Your own scan tool may only let you read MOP_POS, not drive it. That's still useful: it should sit low at idle and climb with engine speed. My logged stock map ([full data here](/ProjectPages/RX8/enginedata/)) ran from about step 3 at 1,000 rpm to step 47 at 9,500 rpm.

## Oil nozzle checks

Each rotor has two nozzles. Mazda's test:

1. Remove the nozzle.
2. Apply a vacuum of 66.5 kPa (0.68 kgf/cm², 9.65 psi) or more to port A with a vacuum pump.
3. It must hold. If it drops 2.66 kPa (0.027 kgf/cm², 0.39 psi) or more in one minute, replace the nozzle.

Mazda's other two inspections are done on the running engine and on the parts: look for oil leaks at the pump-to-front-cover mating surface and where the oil pipe connects (engine at idle), and check the oil pipes, nozzles and the pump's connector bolts for clogging. Don't clear a blockage by drilling: the orifice size is part of the metering. More on the nozzles is on the [nozzles page](/ProjectPages/RX8/OMP/nozzles-premix/).

## Record your results

| Check | Expected | Measured | Pass? |
| :--- | :--- | :--- | :--- |
| Codes and freeze frame | none stored | | |
| Pump supply, terminals C and D (ignition on) | B+ | | |
| Windings D-B, D-F, C-A, C-E | 30.6 to 35.6 Ω each | | |
| Windings to ground (A, E, B, F) | no continuity | | |
| Switch A-C (engine idled then stopped) | 400 Ω or less | | |
| Switch wiring A to 2N, C to 1U | continuity | | |
| 2N after clearing learn value | 0 V / B+ / 0 V | | |
| MOP_POS climbs with rpm | progressive | | |
| Nozzles hold vacuum | drop under 2.66 kPa per minute | | |
| Pipes, connector bolts | not clogged | | |
| Leaks at pump and unions | none | | |

If everything passes but a code returns after clearing, Mazda's last step is the PCM.

