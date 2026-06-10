---
title: RX-8 OMP Diagnostics & Testing
permalink: /ProjectPages/RX8/OMP/testing/
description: >
  Practical diagnostics for the Series 1 RX-8 oil metering pump — symptoms,
  fault codes P1684–P1688, electrical inspections, nozzle testing and
  line clogging checks.
---

This page covers practical checks for diagnosing Series 1 OMP problems, from first warning signs through to component-level electrical tests. It assumes you've read [how the OMP works](/ProjectPages/RX8/OMP/how-it-works/) — the diagnostics make far more sense once you understand the initial-set and monitoring functions the PCM runs at every start.

> **Why this matters:** the OMP is the engine's lifeline. An engine run with a genuinely failed OMP and no premix can destroy its seals quickly. Take OMP-related warning lights seriously, and if in doubt, add premix to the fuel as a safety net while you diagnose. Verify all electrical specifications and connector pinouts against the workshop manual for your model year.
{:.note}

## Warning Signs & Symptoms

- **Check engine light with an OMP fault code** — see the table below. The most common real-world presentation.
- **Limp mode** — when the PCM detects a stepping motor or position switch failure it activates fail-safe: the metering control is fixed at a minimum stroke (step 7), and the PCM restricts fuel injection and suppresses engine speed to protect the seals. If your RX-8 suddenly won't rev past roughly 3,000 RPM with an OMP code stored, this is what's happening.
- **Oil consumption suddenly stops.** A standard RX-8 *should* use oil. If you stop topping up and the level isn't moving over a normal interval, treat it as a red flag, not a bonus.
- **Oil weeping around the pump body or pipe unions** on the front cover.

## Fault Codes

The Series 1 OMP-related DTCs:

| DTC | Relates to | What it means in practice |
|:----|:-----------|:--------------------------|
| P1684 | Metering oil pump position sensor circuit | The PCM can't reconcile the position switch signal with where it believes the stepper is — wiring, connector, switch or (rarely) pump fault. |
| P1685 | Stepping motor circuit | Fault detected in one of the stepper motor's coil circuits or its driver path. The four codes correspond to the motor's separate windings/circuits. |
| P1686 | Stepping motor circuit | As above. |
| P1687 | Stepping motor circuit | As above. |
| P1688 | Stepping motor circuit | As above. |

Any of P1685–P1688 (and usually P1684/P1686 in practice) will put the car into the fail-safe behaviour described above. Exact code definitions can vary slightly between sources — confirm against the DTC table in the workshop manual for your model year.

**The "confused switch" case.** Genuine mechanical pump failure is rare. Far more often the PCM has lost its position reference — for example after codes were cleared mid-fault, a battery disconnect at the wrong moment, or a sticking position switch — and the monitoring function then fails its check even though the pump itself is healthy. Before condemning a pump, work through the electrical checks below; many "failed" OMPs are recovered by re-establishing a valid zero reference and a working switch signal.

## Pre-Diagnostic Checks

Work cheap-to-expensive:

1. **Oil level and condition.** Low or badly degraded oil affects the whole system. Top up and note consumption rate.
2. **Read codes before clearing anything.** Note freeze-frame data if your reader supports it. Clearing codes does not fix the fault and can complicate the PCM's position learning.
3. **Visual inspection.** With the intake tract removed for access, inspect the OMP connector for backed-out pins, corrosion and chafed wiring along the loom — the wiring is a more common culprit than the pump.
4. **Listen for the initial-set.** At each engine start the PCM reverses the stepper 60 steps to find its zero reference. A healthy system performs this routine every start.

## Electrical Inspections

Disconnect the OMP connector for resistance checks; all checks against the workshop manual's specified values and pinout for your model year.

**Stepper motor coil resistance.** The stepping motor uses four coils (No.1–No.4). Measure resistance across each winding pair at the connector. You're looking for four consistent, in-spec readings — an open circuit (infinite) or short (near zero) on any winding confirms a motor/wiring fault and explains a P1685–P1688 code. Also measure from each terminal to the pump body: there should be no continuity to ground.

**Position switch.** The switch detects the fully-open region — it turns on when the stepper is at step 52 or more, and the PCM uses it after the initial-set to verify the motor genuinely moves (rotating 60 steps and expecting the switch to trip above step 52). Check switch continuity at the connector: with the pump at rest (step 0) the switch should be open; if you can drive the pump (or with it removed, rotate the mechanism to the fully-open position), it should close. A switch that's stuck open mimics a dead stepper to the PCM.

**Supply and signal voltage.** With the connector reconnected and ignition ON (engine off), back-probe the connector and verify supply per the manual's PCM terminal voltage tables. Note the PCM cuts current to the stepper coils when ignition is ON but the engine is stopped, so don't condemn the circuit just because the coils are unpowered at key-on.

**Live data.** With Forscan or a WDS-equivalent, monitor the `MOP POS` PID while running. It should sit low at idle and climb progressively with RPM — my logged stock map ([full data here](/ProjectPages/RX8/enginedata/)) ran from about step 3 at 1,000 RPM to step 47 at 9,500 RPM. A commanded value that never moves, or jumps erratically, points at the control side rather than the hydraulics.

## Oil Nozzle & Check Valve Testing

Each rotor has two oil nozzles with one-way check valves preventing reverse flow on the air-hose side. With a nozzle removed:

- It should **hold vacuum** applied from the air bleed side (a hand vacuum pump is ideal). A nozzle that won't hold vacuum has a failed check valve and can let oil be drawn the wrong way or air-lock the line.
- Oil should pass freely in the delivery direction. A blocked nozzle starves that injection point even with a perfect pump.

Full removal and inspection details are on the [nozzles page](/ProjectPages/RX8/OMP/nozzles-premix/).

## Leakage & Clogging Checks

- **Banjo unions:** check each connector bolt at the pump outlets and nozzle ends for weeping. The sealing washers are single-use — leaks here are usually reused washers, not cracked fittings.
- **Pipe clogging:** with the lines disconnected at both ends, gently blow through each pipe — they should flow freely. The connector bolts themselves have small internal drillings that can varnish up on neglected engines; clean with solvent and soft wire, never by drilling.
- **Supply side:** confirm oil is actually reaching the pump inlet from the engine's oil system (or from the external reservoir on converted cars).

## Recording Your Results

It's worth logging results as you go — it turns a frustrating intermittent fault into a pattern:

| Check | Spec / expected | Measured | Pass? |
|:------|:----------------|:---------|:------|
| DTCs present | none | | |
| Stepper coil 1–4 resistance | per manual, four consistent readings | | |
| Coil-to-body continuity | none | | |
| Position switch @ rest | open | | |
| Position switch @ full open | closed | | |
| Initial-set audible at start | yes | | |
| `MOP POS` rises with RPM | progressive | | |
| Nozzles hold vacuum | yes | | |
| Pipes flow freely | yes | | |

If everything above passes but codes persist, the remaining suspects are the loom between connector and PCM, and the PCM itself — in that order of likelihood.

*Next: [removal, installation and servicing](/ProjectPages/RX8/OMP/servicing/).*
