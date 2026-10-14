---
title: RX-8 PCM Terminals, Relays and Fault Codes
crumb: PCM terminals and codes
permalink: /ProjectPages/RX8/terminals-and-codes/
section: rx8
nav_order: 13
applies: Series 1 RX-8 (2003-2008). Definitions are from Mazda's 2003 workshop manual.
reviewed: 2026-10-14
description: >
  The PCM terminals, connector pins, relays and fault codes used in these notes, in
  one lookup.
---

Entries are from Mazda's 2003 workshop manual (linked under Sources). This is a lookup, not a wiring diagram: it doesn't show connector orientation, so identify the connector and pin on Mazda's diagram for your car.

## PCM terminals

| Terminal | Circuit | What Mazda says | Where it's used |
| --- | --- | --- | --- |
| `5X` | Cooling fan relay No. 1 control | Pulled to 1.0 V or less when the fans are operating, battery voltage otherwise | [Manual fan switch](/ProjectPages/RX8/cooling/manual-fan-switch/) |
| `5AD` | Cooling fan high-speed control (relays No. 2 and No. 3) | 1.0 V or less when running at high speed, battery voltage otherwise | [Manual fan switch](/ProjectPages/RX8/cooling/manual-fan-switch/) |
| `2W` | OMP stepper coil No. 1 | Energised in the stepping sequence | [How the OMP works](/ProjectPages/RX8/OMP/how-it-works/#how-the-stepper-is-driven) |
| `2AB` | OMP stepper coil No. 2 | As above | As above |
| `2V` | OMP stepper coil No. 3 | As above | As above |
| `2Y` | OMP stepper coil No. 4 | As above | As above |
| `2N` | OMP position-switch signal | At idle, 1.0 V or less except at the maximum position, where it reads battery voltage | [OMP diagnostics](/ProjectPages/RX8/OMP/testing/#switch-check-at-the-pcm) |
| `1U` | OMP switch ground (sensor ground) | Continuity to switch terminal C | [OMP diagnostics](/ProjectPages/RX8/OMP/testing/#pump-connections) |
| `2AA` | Ignition coil trigger, leading front (L/F) | | [Coils and leads](/ProjectPages/RX8/fuel-ignition-and-starting/#coils-and-leads) |
| `2AD` | Ignition coil trigger, trailing front (T/F) | | As above |
| `2Z` | Ignition coil trigger, leading rear (L/R) | | As above |
| `2AC` | Ignition coil trigger, trailing rear (T/R) | | As above |

## OMP connector pins

| Connector | Pin | Goes to |
| --- | --- | --- |
| 6-pin (stepper) | C and D | Supply from the main relay (battery voltage with ignition on) |
| 6-pin | E | PCM `2W` (coil No. 1) |
| 6-pin | F | PCM `2AB` (coil No. 2) |
| 6-pin | A | PCM `2V` (coil No. 3) |
| 6-pin | B | PCM `2Y` (coil No. 4) |
| 3-pin (switch) | A | PCM `2N` |
| 3-pin (switch) | C | PCM `1U` |

## Relays

| Relay | Job | Notes |
| --- | --- | --- |
| Cooling fan relay No. 1 | Both fans low; also needed for high | Terminal A fed from the main relay, terminal E to PCM `5X` |
| Cooling fan relays No. 2 and No. 3 | With No. 1, both fans high | Separate terminal-E wires joined into the `5AD` wire |
| Fuel pump relay | Pump power | Engine-compartment relay |
| Fuel pump speed-control relay | Bypasses the pump resistor at high demand or cranking | Command with the `FPRR` PID |

Mazda's relay-layout figure is a left-hand-drive one and numbers fan relay No. 1 as position 16, No. 2 as 19 and No. 3 as 13. Positions on a UK right-hand-drive car may differ.

## Fault codes used in these notes

| Code | Mazda's title | See |
| --- | --- | --- |
| `P0480` | Cooling fan No. 1 control circuit problem (relay No. 1, `5X`) | [Manual fan switch](/ProjectPages/RX8/cooling/manual-fan-switch/#p0480-and-p0481) |
| `P0481` | Cooling fan No. 2 control circuit problem (relays No. 2 and No. 3, `5AD`) | As above |
| `P1686` | Metering oil pump control circuit, low flow side problem | [OMP diagnostics](/ProjectPages/RX8/OMP/testing/#fault-codes) |
| `P1687` | Metering oil pump control circuit, high flow side problem | As above |
| `P1688` | Metering oil pump control circuit, initial check problem | As above |

## Scan-tool values (PIDs)

| PID | Meaning |
| --- | --- |
| `MOP_POS` | The PCM's current OMP step count. Read with a Mazda-capable tool such as Forscan; standard OBD-II readers won't show it |
| `MOP_SW` | State of the OMP position switch. Mazda describes it changing from on to off at 53 steps or over |
| `FPRR` | Fuel-pump speed-control relay command |

## Sources

Mazda RX-8 2003 workshop manual (European edition), via the foxed.ca mirror, accessed 14 October 2026: [PCM terminal inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014018880W02.html), [OMP control operation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T38.html), [DTC P0480](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200400W07.html), [DTC P0481](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200400W08.html), [DTC P1686](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010201600W01.html), [P1687](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010201600W02.html), [P1688](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010201600W03.html), [fuel-pump speed-control operation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014000140T26.html) and [relay locations](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE092167730W01.html). The ignition-coil terminals are from Mazda's US-style RX-8 service manual PCM terminal table.
