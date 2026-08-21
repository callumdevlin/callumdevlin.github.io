---
title: RX-8 Manual Cooling Fan Switch Wiring
permalink: /ProjectPages/RX8/cooling/manual-fan-switch/
description: >
  Manual low- and high-speed cooling-fan override wiring for the Series 1 Mazda RX-8 while retaining normal PCM control.
---

This note applies to the Series 1/pre-facelift RX-8, primarily the 2005 UK RHD high-power 231 PS car.

> The cooling fans can start automatically. Disconnect the battery while making connections, and keep clear of the blades whenever the system is live.

## Factory fan operation

| Fan mode | Relay No. 1 | Relay No. 2 | Relay No. 3 | PCM control |
| --- | --- | --- | --- | --- |
| Off | Off | Off | Off | — |
| Low | On | Off | Off | `5X` |
| High | On | On | On | `5X` + `5AD` |

Cooling-fan relay No. 1 runs **both fans at low speed**. High speed requires relay No. 1 **and** relays No. 2 and No. 3. The PCM controls relay No. 1 through output `5X`, and controls relays No. 2 and No. 3 together through output `5AD`.

These are low-side drivers: the PCM energises each relay coil by pulling its control circuit to ground. A manual request should reproduce that ground request through added isolated relay contacts. It must not feed the fan motors or Mazda control circuits from the dashboard switch.

| Condition | Factory fan state |
| --- | --- |
| Below low threshold, no A/C request | Off |
| Approximately 97 °C | Both fans low |
| Approximately 101 °C | Both fans high |
| Cooling from high | High releases around 98 °C |
| Cooling from low | Low releases around 94 °C |
| ECT failure | High-speed fail-safe |

The [main cooling page](/ProjectPages/RX8/cooling/#fan-logic-and-checks) includes the temperature and hysteresis graph.

## Manual LOW-speed switch

The LOW switch manually energises cooling-fan relay No. 1. Its factory control path is:

```text
relay No. 1 coil → relay terminal E/control side → PCM 5X → ground when requested
```

Leave the original PCM connection intact and add a parallel ground path.

**LOW switch off:** the added contact is open and the PCM operates the fans normally.

**LOW switch on:** the added contact grounds the relay No. 1 control node, relay No. 1 energises and both fans run at low speed.

### Added control circuit

```text
ignition-switched 12 V → approximately 1 A fuse → LOW dashboard switch
→ added relay coil → ground
```

### Isolated contact

```text
relay No. 1 terminal E / PCM 5X control node
→ added normally-open contact → ground
```

For a conventional numbered automotive relay, a typical arrangement is:

| Added relay terminal | Connection |
| --- | --- |
| 85 | Coil ground |
| 86 | Fused switched input from the LOW switch |
| 30 | Ground |
| 87 | Relay No. 1 terminal-E / `5X` control node |

Check the pin diagram printed on the actual relay; numbering is not a substitute for identifying its coil and normally-open contact.

**Do not apply 12 V to the Mazda relay control node or PCM `5X` circuit. Do not cut the factory PCM connection.**

> **Diagram still to add:** Manual LOW-speed override. Show cooling-fan relay No. 1, its factory PCM `5X` connection, the added isolated relay contact to ground, dashboard switch, ignition-switched fused supply and added relay coil.
>
> Placeholder path: `/assets/rx8/diagrams/manual-fan-low-speed.svg`

## Manual HIGH-speed switch

Grounding `5AD` alone does **not** request the complete high-speed state. High speed requires both control circuits grounded:

- `5X` energises relay No. 1.
- `5AD` energises relays No. 2 and No. 3.
- All three factory relays must be active for both fans to run at high speed.

Do not directly connect `5X` and `5AD`; they are separate PCM-controlled circuits. Use two electrically isolated normally-open contacts operated by the same HIGH switch.

### HIGH switch control circuit

```text
ignition-switched 12 V → approximately 1 A fuse → HIGH dashboard switch
→ added relay A coil and added relay B coil → ground
```

### Separate isolated contacts

```text
relay A: 5X / relay No. 1 control node → NO contact → ground
relay B: 5AD / relay No. 2 and No. 3 control node → NO contact → ground
```

**HIGH switch off:** both added contacts are open and factory PCM control is unchanged.

**HIGH switch on:** relay A grounds `5X`, relay B independently grounds `5AD`, all three factory fan relays energise and both fans run at high speed.

A suitable dual-pole normally-open relay can provide the two isolated grounding functions, but two ordinary automotive relays are generally easier to identify, source and test.

> **Diagram still to add:** Manual HIGH-speed override. Show separate isolated ground contacts for the `5X` and `5AD` control circuits. Both contacts are operated by the same HIGH switch. The two PCM control circuits must remain electrically isolated.
>
> Placeholder path: `/assets/rx8/diagrams/manual-fan-high-speed.svg`

## LOW and HIGH switches together

| LOW switch | HIGH switch | Result |
| --- | --- | --- |
| Off | Off | Automatic PCM control |
| On | Off | Both fans low |
| Off | On | Both fans high |
| On | On | Both fans high |

The LOW circuit grounds `5X` only. The HIGH circuit already includes the low-speed relay requirement, so it grounds `5X` and `5AD` through separate contacts. Never make the HIGH switch ground only `5AD`.

### Optional AUTO / LOW / HIGH selector

| Selector position | `5X` manual request | `5AD` manual request | Result |
| --- | --- | --- | --- |
| AUTO | None | None | Factory control |
| LOW | Grounded | None | Both fans low |
| HIGH | Grounded | Grounded | Both fans high |

A three-position selector is a tidy alternative to two switches. It must not have a position that disables automatic control: the original PCM connections remain intact in AUTO, LOW and HIGH.


## P0480 and P0481

The PCM monitors the fan-relay control voltages in both commanded-on and commanded-off states. Manually grounding a circuit can therefore produce a low voltage when the PCM expected it to be inactive.

- `P0480`: cooling-fan relay No. 1 / low-speed control monitoring on `5X`.
- `P0481`: cooling-fan relays No. 2 and No. 3 / high-speed control monitoring on `5AD`.

Because the PCM monitors these circuits, manually grounding `5X` or `5AD` can potentially store `P0480` or `P0481` depending on when the PCM performs its diagnostic checks. Scan for pending and stored codes after testing. Do not disable the monitoring.

## Important cautions

- Cooling fans can start automatically; keep clear of the blades with the system live.
- Do not run fan-motor current through a dashboard switch.
- Do not apply 12 V to `5X` or `5AD`.
- Do not directly connect `5X` and `5AD` together.
- Do not cut or remove either factory PCM control connection.
- Do not create a manual mode that prevents automatic high-speed or fail-safe operation.
- Verify relay terminals against the Mazda diagram and the actual vehicle before splicing.

## References

- [Mazda cooling-fan control-system inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html)
- [Mazda PCM terminal inspection: 5X and 5AD](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE014018880W02.html)
- [Mazda DTC P0480: relay No. 1 / 5X](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200400W07.html)
- [Mazda DTC P0481: relays No. 2 and No. 3 / 5AD](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010200400W08.html)
- [Mazda relay locations](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE092167730W01.html)

