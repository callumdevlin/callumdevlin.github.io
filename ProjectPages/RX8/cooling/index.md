---
title: "RX-8 Cooling System: Hose Routing, Drain/Fill and Fan Control"
crumb: Cooling system
permalink: /ProjectPages/RX8/cooling/
type: reference
section: rx8
nav_order: 5
status: growing
applies: Series 1 RX-8 (2003-2008), 13B-MSP. Mazda figures are from the 2003 European manual; the hose part numbers are catalogue evidence and the RHD heater hoses are unresolved.
reviewed: 2026-10-14
description: >
  Coolant routing, a hose register with part numbers and the dimensions that
  have a real source, draining, filling, bleeding and fan control.
related:
  - /ProjectPages/RX8/cooling/manual-fan-switch/
  - /ProjectPages/RX8/quick-reference/
---

## Quick reference

| Item | Value |
| --- | --- |
| Total capacity | 9.8 L |
| Thermostat | Starts opening 80-84 °C; fully open at 95 °C; lift at least 8.5 mm |
| Cap valve-opening pressure | 73.3-103.3 kPa. Mazda's system leak test is 127 kPa for one minute |
| Fan low | On at 97 °C; off at 94 °C or below |
| Fan high | On at 101 °C; back to low at 98 °C or below |

All from Mazda's [engine specifications](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010002000T04.html) and [cooling fan control inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html).

## System layout

Mazda's flow chart shows the pump feeding the engine and the engine's coolant leaving through the thermostat to the top of a down-flow radiator. The radiator outlet, the heater return and the reserve-tank feed all join at the pump inlet. The top of the radiator and the engine bleed to the reserve tank, which has an orifice in its outlet hose, so keep that orifice if you replace the hose.

The throttle-body warming loop is not on Mazda's chart. From owner reports, coolant runs from the rear housing through the throttle body and back towards the pump inlet; I'd verify the direction by feel on a warming engine before relying on it.

## Coolant-hose register

Mazda's manual names the hoses only generically ("upper radiator hose", "lower radiator hose") and gives no part numbers, so the IDs H01-H11 are my own labels. The part numbers below come from parts catalogues (Atkins Rotary, Mazdatrix, mazdaparts.org, read 2026-10-14). They are good evidence for what a hose is called and what replaced it, but they are not a dimensional drawing, and catalogues are not always right about RHD cars.

| ID | Route | Mazda part no. (replaces) | Applicability notes | Status |
| --- | --- | --- | --- | :---: |
| H01 | Lower radiator outlet to the pump/thermostat-housing inlet | `N3H1-15-185B` (185, 185A) | 2004-2011. | <span class="tag tag-spec">Catalogue</span> |
| H02 | Radiator top to the connecting pipe (front upper hose) | `N3H1-15-186C` (186A, 186B) | 2004-2011. | <span class="tag tag-spec">Catalogue</span> |
| H03 | Connecting pipe to the engine-side outlet at the thermostat housing (rear upper hose) | `N3H2-15-186B` (186, 186A) | 2004-2011. The engine-side endpoint is from a retailer's wording, so check it. | <span class="tag tag-spec">Catalogue</span> |
| pipe | The single connecting pipe between H02 and H03 | `N3H2-15-190` | One pipe, not a front and a rear one. | <span class="tag tag-spec">Catalogue</span> |
| H04 | Radiator top bleed port to the reserve tank | `N3H1-15-184D` | 2004-2011. | <span class="tag tag-spec">Catalogue</span> |
| H05 | Thermostat housing to the reserve tank upper port | `N3H1-15-380A` (183A, 183B) | Early parts carried the 183 number, so "380" alone is incomplete. | <span class="tag tag-spec">Catalogue</span> |
| H06 | Reserve tank lower outlet to the lower thermostat housing | `N3H1-15-381C` (earlier), `N3H1-15-381D` (later) | Catalogues split the two at a US VIN (041201, December 2004). How that maps to a UK car's VIN is not established. | <span class="tag tag-open">Check by VIN</span> |
| H07 | Throttle body to the thermostat/pump-inlet side | `N3H1-13-692C` (692A, 692B) | 2004-2011. Flow direction: see the note below. | <span class="tag tag-spec">Catalogue</span> |
| H08 | Rear housing to the throttle body | `N3H1-13-691A` | 2004-2008 only; the catalogues list no later fitment. | <span class="tag tag-spec">Catalogue</span> |
| H09 | Rear housing to the heater, RHD | | No RHD part number found. LHD cars use `FE01-61-211` (2004-2008), which one catalogue marks "won't fit RHD". | <span class="tag tag-open">Unresolved</span> |
| H10 | Heater feed link, RHD | | No RHD number found. LHD `FE01-61-213`, marked "won't fit RHD". | <span class="tag tag-open">Unresolved</span> |
| H11 | Heater return to the pump, RHD | | No RHD number found. LHD `FE01-61-212D` ("won't fit RHD") or `FE01-61-24YC`/`24YD`; these differ by build date and carry a restrictor orifice. | <span class="tag tag-open">Unresolved</span> |

Direction of H07 and H08: I first wrote H07 as the feed and H08 as the return. Two forum moderators' descriptions point the other way (the top rear-housing port feeds the throttle body, which returns towards the pump inlet), so I've changed the routes above. It is moderate-confidence evidence from forum posts, so confirm on your car.
{:.note}

Left-hand-drive heater references such as `FE01-61-211/-213` do not establish the UK RHD hose shape. Owner reports say the RHD car differs in heater-core side, firewall connection and some heater hoses. Not every part number above has been matched to a UK VIN.

Aftermarket "18-hose" kits cover coolant and breather hoses together, and vendors don't publish the split. Some "18 pcs" listings are nine hoses plus eighteen clamps. Classify each hose by its endpoints before fitting it; do not connect a similarly sized vacuum or breather hose into the cooling circuit.

### Hose dimensions

A dimension only goes in the "Evidence" column if there is a source for it, and what kind of number it is matters: a catalogue's nominal inner diameter is not the outside diameter of the metal spigot it fits over, and a figure measured on an old hose is bigger than new because rubber stretches. Where I have no source the cell says so. Retailer fitment claims and kit photographs are not dimensional drawings.

| ID | Evidence found (and what kind of number it is) | Source | Status | My measurement: ends A / B, OD, centreline |
| --- | --- | --- | :---: | --- |
| H01 | Catalogue nominal ID 34.9 mm (1.375 in) at both ends, hose OD 45.2 mm (1.781 in), curved. Used UK 231 hose: about 44-46 mm OD (an owner's ball-park, measured on an installed hose) | Dayco 72615 listing; RX-8 Owners Club UK thread "Radiator Hose Size" (2019) | <span class="tag tag-estimate">Indicative</span> | <span class="fill"></span> |
| H02 | Catalogue nominal IDs 31.75 mm and 34.9 mm (dual-ID hose). Cross-references to this hose conflict between suppliers | Dayco 71766 listing | <span class="tag tag-estimate">Indicative</span> | <span class="fill"></span> |
| H03 | Catalogue nominal ID 33 mm at both ends, centreline length 295 mm, pre-shaped EPDM. The fitment text conflicts with Dayco's for 2008 | Gates 23059 listing | <span class="tag tag-estimate">Indicative</span> | <span class="fill"></span> |
| H04-H08 | No sourced dimension found. The Mazda clamp sizes in catalogues (5/8 in for H04 and H05, 1 in for H06, 9/16 in for H07 and H08) are only a rough cue to hose size | Atkins product pages | <span class="tag tag-open">None</span> | <span class="fill"></span> |
| H09-H11 | No sourced dimension or UK part number found | | <span class="tag tag-open">None</span> | <span class="fill"></span> |

Taken together, the independent hints for the three large radiator hoses (UK 44 mm and 46 mm OD, a 44.5 mm clamp label, Dayco's 45.2 mm OD) agree on about 44-46 mm OD and a nominal ID of 33-35 mm. A 38 mm "ID" quoted in some forum posts looks like an expanded used hose. None of this is a fitment instruction. Measure the spigots and the centreline on your car before ordering silicone hoses, which come in standard sizes that don't match 33-35 mm.

The blank measurement cells need a vernier caliper and a tape on the car, so they stay blank rather than being estimated.
{:.note}

## Draining the system

Mazda's coolant-replacement procedure drains only at the radiator drain plug. It doesn't say whether the engine has other drain points, and one parts retailer lists a centre cast-iron coolant plug (9951-01-000) as fitting the 13B-MSP, so look at your engine before assuming a radiator drain empties it. Either way, a radiator drain leaves coolant in the heater matrix, rear housing, upper joining pipe and throttle-body loop.

1. Let the engine cool completely and remove the centre splash shield/undertray for access.
2. Slowly remove the expansion-tank pressure cap.
3. Put a wide drain tray beneath the radiator's lower tank and open the radiator drain plug.
4. Let the expansion tank empty through the connected lower hose. Squeeze the main hoses gently to move retained pockets; do not use compressed air.
5. For a more complete drain, disconnect H01 at the lowest point after the radiator has stopped flowing, and catch the extra coolant rather than assuming the system is empty.
6. Inspect the drain plug and its seal (the plug on my car is plastic), then refit it hand-snug. Mazda publishes no torque or washer for it.
7. Reconnect H01 with its clamp returned behind the hose bead and refit the undertray after leak checks.

Measure what comes out. It will be less than the full 9.8 L, and the figure tells you how much to mix back in.

## Refilling and bleeding

Mazda's text: ethylene-glycol coolant, soft (demineralised) water, mixed for the climate. If your cap or filler neck is marked FL22 the coolant is premixed and should not be diluted. I could not open the Mazda bulletin for FL22, so check it against your cap marking.

1. Check that the drain plug and H01 are secure. Set the cabin temperature to full hot; heat output is a useful circulation check.
2. Fill the expansion tank slowly to **F**, pausing to squeeze H01, H02 and the accessible heater hoses. Let bubbles return before adding more. (The squeezing is my practice.)
3. Fit the pressure cap. Start the engine, inspect every disturbed joint and let it idle until warm.
4. Hold approximately **2,500 rpm for five minutes**, then **3,000 rpm for five minutes**, then return to idle. Mazda says to repeat these stages several times while you watch temperature.
5. Confirm the upper radiator hose becomes hot as the thermostat opens. Continue until temperature is stable and the cooling fans cycle; stop immediately for a rapid temperature rise or loss of cabin heat.
6. Shut down and let the engine cool completely. Never open the pressurised tank hot.
7. Top the cold level to **F** and repeat if it dropped. I also recheck after the first full drive and again the next morning.

Intermittent heater output points to air at the heater matrix/firewall hoses. A sudden level drop when the thermostat opens usually comes from the rear housing or bypass region. Persistent gurgling can remain in the upper joining pipe, throttle-body loop or the small bleed hoses; check those hoses for kinks before repeating the cycle.

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

The last row is easy to forget: the fans can start after you have switched off and walked away, so keep hands clear of them.
{:.note}

{% include figure.html src="/assets/rx8/generated/fan-temperature-logic.svg" alt="Chart of the cooling fan states against coolant temperature, showing the low and high thresholds and their hysteresis" caption="Fan thresholds and hysteresis, drawn from the table above. A schematic of Mazda's figures, not a measurement." class="fig-medium" %}

Mazda's motor-current references are a **bench test**: with a battery and ammeter connected directly to the motor connector at 12 V, fan No. 1 draws 8.9-11.9 A and fan No. 2 draws 4.0-7.0 A. They are not in-car low/high-speed circuit currents. If neither fan runs, check the fan fuses (general practice), relay No. 1, both motor connectors and grounds. If low is missing but high works, concentrate on relay No. 1 and the series/low-speed path. If only one fan runs, test that motor and its branch before blaming the PCM.

## Manual fan control

The Series 1 fan relays can also be requested manually while normal PCM control stays in place. The [manual fan switch note](/ProjectPages/RX8/cooling/manual-fan-switch/) covers low-speed and high-speed operation, two-switch and AUTO/LOW/HIGH arrangements, the PCM `5X` and `5AD` circuits and the `P0480`/`P0481` codes that result.

## References

- Mazda RX-8 2003 workshop manual (European edition), read 2026-10-14 through a third-party mirror: [cooling-system flow](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011201008T03.html), [engine coolant replacement](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011215001W04.html), [cooling fan control inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE010300103W31.html), [fan motor inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011215140W02.html), [relay location](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE092167730W01.html).
- Hose part numbers: [Atkins Rotary RX-8 coolant hoses](https://www.atkinsrotary.com/Coolant-System/Radiator-and-Coolant-Hoses/Rx8-Coolant-Hoses/), [Mazdatrix](https://mazdatrix.com/product-category/cooling-system/water-cooling-systems/hoses-and-pumps/), [mazdaparts.org](https://mazdaparts.org/mazda-rx8-radiator-hose.html).
- Hose dimensions: [Dayco 72615](https://partshawk.com/mazda-rx-8-lower-radiator-coolant-hose-dayco-72615.html), [Dayco 71766](https://partshawk.com/dayco-71766-radiator-coolant-hose.html), [Gates 23059](https://partshawk.com/mazda-rx-8-radiator-coolant-hose-gates-23059.html), [RX-8 Owners Club UK: Radiator Hose Size](https://www.rx8ownersclub.co.uk/forum/viewtopic.php?t=80569).
