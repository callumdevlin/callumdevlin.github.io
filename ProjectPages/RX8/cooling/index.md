---
title: "RX-8 Cooling System: Hose Routing, Drain/Fill and Fan Control"
crumb: Cooling system
permalink: /ProjectPages/RX8/cooling/
section: rx8
nav_order: 5
applies: Series 1 RX-8 (2003-2008), 13B-MSP. Mazda figures are from the 2003 European workshop manual.
reviewed: 2026-10-14
description: >
  Coolant routing, a hose register with part numbers and sizes, draining, filling,
  bleeding and fan control.
related:
  - /ProjectPages/RX8/cooling/manual-fan-switch/
---

## Quick reference

| Item | Value |
| --- | --- |
| Total capacity | 9.8 L |
| Thermostat | Starts opening 80-84 °C; fully open at 95 °C; lift at least 8.5 mm |
| Cap valve-opening pressure | 73.3-103.3 kPa. Mazda's system leak test is 127 kPa for one minute |
| Fan low | On at 97 °C; off at 94 °C or below |
| Fan high | On at 101 °C; back to low at 98 °C or below |

From Mazda's [engine specifications](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010002000T04.html) and [cooling fan control inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html).

## System layout

Per Mazda's flow chart, the pump feeds the engine and coolant leaves through the thermostat to the top of a down-flow radiator. The radiator outlet, heater return and reserve-tank feed all join at the pump inlet. The top of the radiator and the engine bleed to the reserve tank, whose outlet hose has an orifice, so keep it if you replace the hose.

The throttle-body warming loop isn't on Mazda's chart. Owners report coolant running from the rear housing through the throttle body and back towards the pump inlet. Confirm the direction by feel on a warming engine.

## Coolant-hose register

<span id="hose-dimensions"></span>Mazda names the hoses only generically and gives no part numbers, so H01-H11 are my own labels. Part numbers come from catalogues (Atkins Rotary, Mazdatrix, mazdaparts.org), which show what a hose is called and what replaced it but can be wrong for right-hand-drive cars. A blank means no size or part number found.

| ID | Route | Mazda part no. (replaces) | Size and fitment |
| --- | --- | --- | --- |
| H01 | Lower radiator outlet to the pump/thermostat-housing inlet | `N3H1-15-185B` (185, 185A) | 2004-2011. Nominal ID 34.9 mm (1.375 in) both ends, hose OD 45.2 mm (1.781 in), curved (Dayco 72615). A used UK 231 hose is reported at 44-46 mm OD. |
| H02 | Radiator top to the connecting pipe (front upper hose) | `N3H1-15-186C` (186A, 186B) | 2004-2011. Dual ID, 31.75 and 34.9 mm (Dayco 71766); supplier cross-references conflict. |
| H03 | Connecting pipe to the engine-side outlet at the thermostat housing (rear upper hose) | `N3H2-15-186B` (186, 186A) | 2004-2011. Nominal ID 33 mm both ends, centreline 295 mm, pre-shaped EPDM (Gates 23059); Dayco's fitment text differs for 2008. The engine-side endpoint is from a retailer's wording, so check it. |
| pipe | The single connecting pipe between H02 and H03 | `N3H2-15-190` | One pipe, not a front and a rear one. |
| H04 | Radiator top bleed port to the reserve tank | `N3H1-15-184D` | 2004-2011. Clamp 5/8 in. |
| H05 | Thermostat housing to the reserve tank upper port | `N3H1-15-380A` (183A, 183B) | Early parts carried the 183 number, so "380" alone is incomplete. Clamp 5/8 in. |
| H06 | Reserve tank lower outlet to the lower thermostat housing | `N3H1-15-381C` (earlier), `N3H1-15-381D` (later) | Catalogues split the two at a US VIN (041201, December 2004); how that maps to a UK VIN isn't established. Clamp 1 in. |
| H07 | Throttle body to the thermostat/pump-inlet side | `N3H1-13-692C` (692A, 692B) | 2004-2011. Clamp 9/16 in. |
| H08 | Rear housing to the throttle body | `N3H1-13-691A` | 2004-2008 only. Clamp 9/16 in. |
| H09 | Rear housing to the heater, RHD | | LHD cars use `FE01-61-211` (2004-2008), which one catalogue marks "won't fit RHD". |
| H10 | Heater feed link, RHD | | LHD `FE01-61-213`, marked "won't fit RHD". |
| H11 | Heater return to the pump, RHD | | LHD `FE01-61-212D` ("won't fit RHD") or `FE01-61-24YC`/`24YD`, which differ by build date and carry a restrictor orifice. |

Notes on sizes:

- Catalogue clamp sizes for H04-H08 are only a rough cue. The three large radiator hoses (H01-H03) point to about 44-46 mm OD and a nominal ID of 33-35 mm. A 38 mm ID in some forum posts looks like an expanded used hose.
- A catalogue ID is a nominal hose size, not the OD of the spigot it fits, and a used hose measures larger than a new one. Measure the spigots and centreline on your car before ordering silicone hoses, which come in standard sizes that don't match 33-35 mm.
- On H07 and H08, forum moderators describe the top rear-housing port feeding the throttle body, which returns towards the pump inlet. That is forum evidence, not Mazda's.
- LHD heater references don't establish the UK RHD hose shape: owners report the RHD car differs in heater-core side, firewall connection and some heater hoses. Not every part number here is matched to a UK VIN.
- Aftermarket "18-hose" kits cover coolant and breather hoses together, and the split isn't published. Some "18 pcs" listings are nine hoses plus eighteen clamps. Identify each hose by its endpoints, and never connect a similar vacuum or breather hose into the cooling circuit.

## Draining the system

Mazda's coolant-replacement procedure drains only at the radiator drain plug and doesn't say whether the engine has other drain points. One retailer lists a centre cast-iron coolant plug (9951-01-000) as fitting the 13B-MSP, so look at your engine. Either way, a radiator drain leaves coolant in the heater matrix, rear housing, upper joining pipe and throttle-body loop.

1. Let the engine cool completely and remove the centre splash shield/undertray.
2. Slowly remove the expansion-tank pressure cap.
3. Put a wide tray under the radiator's lower tank and open the drain plug.
4. Let the expansion tank empty through the connected lower hose. Squeeze the main hoses gently to move trapped pockets; don't use compressed air.
5. For a fuller drain, disconnect H01 at the lowest point once the radiator has stopped flowing, and catch the extra coolant.
6. Inspect the drain plug and seal (mine is plastic) and refit it hand-snug. Mazda publishes no torque or washer.
7. Reconnect H01 with its clamp behind the hose bead and refit the undertray after leak checks.

Measure what comes out. It will be less than the full 9.8 L, and tells you how much to mix back in.

## Refilling and bleeding

Mazda specifies ethylene-glycol coolant with soft (demineralised) water, mixed for the climate. If your cap or filler neck is marked FL22 the coolant is premixed and shouldn't be diluted.

1. Check the drain plug and H01 are secure. Set the cabin temperature to full hot; heat output is a useful circulation check.
2. Fill the expansion tank slowly to F, pausing to squeeze H01, H02 and the accessible heater hoses (my practice, not Mazda's). Let bubbles return before adding more.
3. Fit the cap, start the engine, check every disturbed joint and idle until warm.
4. Hold about 2,500 rpm for five minutes, then 3,000 rpm for five minutes, then idle. Mazda says to repeat these stages several times while you watch temperature.
5. Confirm the upper radiator hose gets hot as the thermostat opens. Continue until temperature is stable and the fans cycle. Stop at once for a rapid temperature rise or loss of cabin heat.
6. Shut down and let the engine cool completely. Never open the pressurised tank hot.
7. Top up the cold level to F and repeat if it dropped. I also recheck after the first full drive and the next morning.

Intermittent heater output means air at the heater matrix or firewall hoses. A sudden level drop when the thermostat opens usually comes from the rear housing or bypass area. Persistent gurgling can remain in the upper joining pipe, throttle-body loop or small bleed hoses; check those for kinks before repeating the cycle.

## Fan logic and checks

Mazda's thresholds are for the engine at idle with the A/C off.

| Coolant/command condition | Relays | Behaviour |
| --- | --- | --- |
| Below 97 °C, no A/C request | None | Both fans off |
| 97 °C or above, rising | No. 1 | Both fans low speed |
| 101 °C or above, rising | Nos. 1, 2 and 3 | Both fans high speed |
| Cooling from high | High until 98 °C or below; low until 94 °C or below | Hysteresis prevents rapid switching |
| A/C request | PCM selects low or high from refrigerant pressure | Temperature is not the only input |
| ECT circuit fault | Fail-safe request | Both fans high speed |
| Ignition off, hot engine bay | PCM "after-cooling" | Fans can run at high speed with the key out |

The last row is easy to forget: the fans can start after you've switched off and walked away, so keep hands clear.
{:.note}

{% include figure.html src="/assets/rx8/generated/fan-temperature-logic.svg" alt="Chart of the cooling fan states against coolant temperature, showing the low and high thresholds and their hysteresis" caption="Fan thresholds and hysteresis, drawn from the table above. A schematic of Mazda's figures, not a measurement." class="fig-medium" %}

Mazda's motor-current figures are a bench test: battery and ammeter direct to the motor connector at 12 V, fan No. 1 draws 8.9-11.9 A and fan No. 2 draws 4.0-7.0 A. They aren't in-car circuit currents.

- Neither fan runs: check the fan fuses, relay No. 1, both motor connectors and grounds.
- Low missing but high works: look at relay No. 1 and the series/low-speed path.
- Only one fan runs: test that motor and its branch before blaming the PCM.

## Manual fan control

The Series 1 fan relays can also be requested manually while normal PCM control stays in place. The [manual fan switch note](/ProjectPages/RX8/cooling/manual-fan-switch/) covers low and high operation, two-switch and AUTO/LOW/HIGH arrangements, the PCM `5X` and `5AD` circuits and the `P0480`/`P0481` codes.

## References

- Mazda RX-8 2003 workshop manual (European edition), via the foxed.ca mirror, accessed 14 October 2026: [cooling-system flow](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011201008T03.html), [engine coolant replacement](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011215001W04.html), [cooling fan control inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html), [fan motor inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011215140W02.html), [relay location](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE092167730W01.html).
- Hose part numbers: [Atkins Rotary RX-8 coolant hoses](https://www.atkinsrotary.com/Coolant-System/Radiator-and-Coolant-Hoses/Rx8-Coolant-Hoses/), [Mazdatrix](https://mazdatrix.com/product-category/cooling-system/water-cooling-systems/hoses-and-pumps/), [mazdaparts.org](https://mazdaparts.org/mazda-rx8-radiator-hose.html).
- Hose sizes: [Dayco 72615](https://partshawk.com/mazda-rx-8-lower-radiator-coolant-hose-dayco-72615.html), [Dayco 71766](https://partshawk.com/dayco-71766-radiator-coolant-hose.html), [Gates 23059](https://partshawk.com/mazda-rx-8-radiator-coolant-hose-gates-23059.html), [RX-8 Owners Club UK: Radiator Hose Size](https://www.rx8ownersclub.co.uk/forum/viewtopic.php?t=80569).
