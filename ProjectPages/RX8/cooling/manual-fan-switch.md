---
title: RX-8 Manual Cooling Fan Switch Wiring
crumb: Manual fan switch
permalink: /ProjectPages/RX8/cooling/manual-fan-switch/
type: wiring
section: rx8
nav_order: 6
applies: Series 1 RX-8 (2003-2008). Circuit descriptions are from Mazda's 2003 workshop manual.
reviewed: 2026-10-14
description: >
  Manual low- and high-speed cooling-fan override for the Series 1 RX-8 that keeps
  normal PCM control, and what it does to the PCM's fan-circuit monitoring.
related:
  - /ProjectPages/RX8/cooling/
---

This is an explanatory note, not a verified installation guide. The circuits come from Mazda's manual, and relay and connector positions haven't been confirmed on a UK right-hand-drive car.

The cooling fans can start automatically, and also after the engine is switched off (see below). Disconnect the battery while making connections and keep clear of the blades whenever the system is live.
{:.note}

## Factory fan operation

| Fan mode | Relay No. 1 | Relay No. 2 | Relay No. 3 | PCM control |
| --- | --- | --- | --- | --- |
| Off | Off | Off | Off | none |
| Low | On | Off | Off | `5X` |
| High | On | On | On | `5X` + `5AD` |

Relay No. 1 alone runs both fans at low speed. High speed needs relay No. 1 and relays No. 2 and No. 3. The PCM controls relay No. 1 through output `5X`, and relays No. 2 and No. 3 together through `5AD`. Mazda's diagnosis pages show relay No. 1's terminal A fed with battery voltage through the main relay and its terminal E running to the PCM at `5X`. Relays No. 2 and No. 3 each have their own terminal E, joined into the single `5AD` wire.

These are low-side drivers: the PCM energises each relay coil by pulling its control wire to ground. A manual request should therefore reproduce that ground through an added, isolated relay contact. It must not feed the fan motors or Mazda's control wires from a dashboard switch.

| Condition | Factory fan state |
| --- | --- |
| Coolant below the low threshold, no A/C request | Off |
| 97 °C or above | Both fans low |
| 101 °C or above | Both fans high |
| Cooling from high | High releases at 98 °C or below |
| Cooling from low | Low releases at 94 °C or below |
| Coolant sensor (ECT) failure | High-speed fail-safe |
| Ignition off, hot engine bay | "After-cooling": high speed can run with the key out |

The [cooling page](/ProjectPages/RX8/cooling/#fan-logic-and-checks) has the temperature and hysteresis graph.

## The idea

{% include figure.html src="/assets/rx8/diagrams/manual-fan-override-concept.svg" alt="Schematic: the PCM outputs 5X and 5AD go to the E terminals of the fan relays; an added normally-open contact on each wire can connect it to ground" caption="The idea in one picture: an added normally-open contact in parallel with the PCM's own ground path, one on `5X` and one on `5AD`. An explanatory schematic only, not a wiring diagram." %}

## Manual LOW-speed switch

The LOW switch manually energises cooling-fan relay No. 1. Its factory control path is:

```text
relay No. 1 coil → relay terminal E → PCM 5X → ground when requested
```

Leave the original PCM connection intact and add a parallel ground path. With the LOW switch off, the added contact is open and the PCM runs the fans normally. With it on, the contact grounds the relay No. 1 control wire, the relay energises and both fans run at low speed.

**Added control circuit:**

```text
ignition-switched 12 V → small fuse → LOW dashboard switch → added relay coil → ground
```

**Isolated contact:**

```text
relay No. 1 terminal E / PCM 5X wire → added normally-open contact → ground
```

For a conventional numbered automotive relay, a typical arrangement is:

| Added relay terminal | Connection |
| --- | --- |
| 85 | Coil ground |
| 86 | Fused switched input from the LOW switch |
| 30 | Ground |
| 87 | Relay No. 1 terminal E / `5X` wire |

Check the pin diagram printed on the actual relay; numbering is not a substitute for identifying its coil and normally-open contact. The fuse is only for the added coil, so a small one suits a standard relay; check your relay's coil current.

**Do not apply 12 V to the Mazda relay control wire or PCM `5X`. Do not cut the factory PCM connection.**

## Manual HIGH-speed switch

Grounding `5AD` alone does **not** request the full high-speed state. On Mazda's diagnosis, a fan No. 2 that runs with fan No. 1 off points to relay No. 3 stuck closed or a short to ground on `5AD`, so `5AD` on its own runs only fan No. 2. High speed needs both circuits grounded:

- `5X` energises relay No. 1.
- `5AD` energises relays No. 2 and No. 3.
- All three factory relays must be active for both fans to run high.

Don't join `5X` and `5AD`: they are separate PCM-controlled circuits. Use two electrically isolated normally-open contacts operated by the same HIGH switch.

Relays No. 2 and No. 3 have separate terminal-E wires that join into `5AD`. The added ground has to go on the common `5AD` wire, not on one relay's terminal E, or only one fan will go to high.
{:.note}

**HIGH switch control circuit:**

```text
ignition-switched 12 V → small fuse → HIGH dashboard switch
→ added relay A coil and added relay B coil → ground
```

**Separate isolated contacts:**

```text
relay A: 5X / relay No. 1 control wire → normally-open contact → ground
relay B: 5AD / relay No. 2 and No. 3 control wire → normally-open contact → ground
```

With the HIGH switch off, both added contacts are open and the PCM controls the fans as it always did. With it on, relay A grounds `5X`, relay B grounds `5AD`, all three factory relays energise and both fans run at high speed. A suitable dual-pole normally-open relay can do both grounding jobs, but two ordinary automotive relays are easier to identify, source and test.

Mazda's relay-layout figure is a left-hand-drive one and numbers relay No. 1 as position 16, No. 2 as 19 and No. 3 as 13. Positions on a UK right-hand-drive car may differ, so locate the relays by their function and connector before splicing.

## LOW and HIGH switches together

| LOW switch | HIGH switch | Result |
| --- | --- | --- |
| Off | Off | Automatic PCM control |
| On | Off | Both fans low |
| Off | On | Both fans high |
| On | On | Both fans high |

The LOW circuit grounds `5X` only. The HIGH circuit already includes the low-speed relay, so it grounds `5X` and `5AD` through separate contacts. Never let the HIGH switch ground only `5AD`.

### Optional AUTO / LOW / HIGH selector

| Selector position | `5X` manual request | `5AD` manual request | Result |
| --- | --- | --- | --- |
| AUTO | None | None | Factory control |
| LOW | Grounded | None | Both fans low |
| HIGH | Grounded | Grounded | Both fans high |

A three-position selector is a tidy alternative to two switches. It must not have a position that disables automatic control: the PCM connections stay intact in AUTO, LOW and HIGH. If the LOW and HIGH positions share a relay, add a diode so the LOW position cannot feed back into the HIGH relay's coil. That is my own electrical design note, not something from Mazda.

## P0480 and P0481

The PCM monitors the voltage on both fan-relay control wires. Mazda titles `P0480` "cooling fan No. 1 control circuit" (relay No. 1, `5X`) and `P0481` "cooling fan No. 2 control circuit" (relays No. 2 and No. 3, `5AD`). Both are continuous monitors: the PCM sets the fault when the wire is low while it is commanding the relay off. Mazda publishes no debounce time, and the warning lamp does not light for these codes.

So, when the manual switch grounds a circuit the PCM wants off, expect a pending code, and possibly a stored one. Mazda's own key-on test requires these codes not to be present, so scan for pending and stored codes after testing. Don't disable the monitoring.

## Cautions

- Cooling fans can start automatically, and with the ignition off after a hot shutdown. Keep clear of the blades.
- Do not run fan-motor current through a dashboard switch.
- Do not apply 12 V to `5X` or `5AD`.
- Do not join `5X` and `5AD`.
- Do not cut or remove either factory PCM control connection.
- Do not create a manual mode that prevents automatic high-speed or fail-safe operation.
- Verify relay terminals against Mazda's diagram and your car before splicing.

## References

Mazda RX-8 2003 workshop manual (European edition), via the foxed.ca mirror, accessed 14 October 2026:

- [Cooling fan control system inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html)
- [PCM terminal inspection: 5X and 5AD](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014018880W02.html)
- [DTC P0480: relay No. 1 / 5X](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200400W07.html)
- [DTC P0481: relays No. 2 and No. 3 / 5AD](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200400W08.html)
- [Relay locations](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE092167730W01.html)
