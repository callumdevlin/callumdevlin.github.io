---
title: SyncTag, designing the tag's circuit board
crumb: SyncTag PCB
permalink: /ProjectPages/rfidtoolstorage/synctag-pcb/
reviewed: 2026-10-16
image: /Images/optimised/synctag-pcb-render-1200.webp
description: >
  The electronics of the ToolSync tag, designed in KiCad 9: a BLE and NFC board with a
  coin cell, what I changed from my first concept and why, and what is still only a
  model.
---

I have designed the electronics of the SyncTag, the small tag that sits on each tool in [ToolSync](/ProjectPages/rfidtoolstorage/). It is two boards drawn in KiCad 9: a 26.4 × 10.1 mm four-layer main board with a Bluetooth Low Energy (BLE) chip, antenna and coin cell, and a separate NFC antenna flex. KiCad's own electrical and design rule checks report no errors on either. **Nothing has been built, powered or measured, and no tag firmware exists yet**, so every performance figure below is a data-sheet number or a model, and I say which.

{% include figure.html src="/Images/synctag-pcb-render.png" alt="Angled 3D render of a long thin green circuit board with a black square chip in the middle, small capacitors, five pads along the left edge, a red LED and a cream chip antenna at the right-hand end" caption="The main board, rendered from the KiCad design. The part bodies are placeholder shapes, not manufacturer models." eager=true %}

## Why I redesigned the tag

My BEng report described the tag as an NTAG213 for identity, a BK3432 Bluetooth chip, a 5 mm LED, a buzzer and a coin cell in a 25 × 10 × 7 mm casing, but it only existed as a schematic. When I checked it against data sheets and dimensions, several things did not hold:

- **The cell does not fit.** A CR1025 is 10.0 mm across, which cannot go in a 9 mm cavity or a 10 mm wide casing, however thin the walls.
- **The alert parts do not fit either.** The 5 mm LED and the 12 × 9.5 mm buzzer need more height than a cavity 3.7 to 4.5 mm tall allows.
- **A coin cell cannot run that buzzer.** A magnetic buzzer draws about 15 mA, and I could not find the buzzer part named in the report as written. The nearest real family is a 9 × 9 mm piezo with a last-time-buy notice.
- **The 694-day battery figure was only the sleep current.** It is the cell capacity divided by the BLE chip's 1.8 µA sleep draw, which leaves out advertising, the fact that a coin cell never delivers its full rating, and temperature. A tag that can be found over Bluetooth has to advertise.
- **The BK3432 is thinly documented.** There is no reference antenna design or certification, so I would be guessing at the matching network.
- **A plain NTAG213 has no output pin,** but the schematic assumed it could signal the Bluetooth chip when scanned.

## What I designed instead

| Block | First concept | Rev A design |
| --- | --- | --- |
| Identity | NTAG213 | NXP NT3H2111 (NTAG I²C plus) on its own two-layer flex with a 13.56 MHz coil and a ferrite sheet |
| Bluetooth chip | BK3432 | TI CC2340R52 (Cortex-M0+, BLE 5.4, about 0.7 µA standby, built-in DC/DC) |
| Antenna | not defined | Johanson 2450AT18D0100001E chip antenna at the board edge, TI's reference harmonic filter and two unfitted tuning slots |
| Alert | LED and buzzer | one red LED behind the diffuser; **no buzzer in Rev A** |
| Cell | 15 mAh cell (no standard part found) | CR1025 (30 mAh) in a Keystone 3030 retainer on the underside, with a P-FET against a reversed cell |
| Clocks | not defined | 48 MHz crystal; 32 kHz from the chip's internal oscillator |
| Programming | none | five SWD and test pads |
| Size | 25 × 10 × 7 mm | about 28.0 × 11.5 × 7.3 mm outside |

The cell and the stack of parts above it are why the tag grows: the nominal stack is 6.86 mm and the worst case 7.23 mm, against a 7.0 mm target, so a prototype enclosure has to confirm it.

{% include figure.html src="/Images/synctag-block-diagram.png" alt="Block diagram: cell and reverse-battery protection feed the CC2340R52 chip in the centre, which connects to the RF filter and chip antenna, an indicator LED, programming pads and the NFC flex, which talks to the ToolSync toolbox" caption="Block diagram of Rev A." fulllink=true %}

### Why NFC identity is a separate passive part

If the Bluetooth chip pretended to be the NFC tag itself, the tool's identity would vanish whenever the cell went flat, and the toolbox would stop seeing it. The NT3H2111 is powered by the reader's field, so the toolbox's PN532 can always read the tool's ID with no battery. Its output pin and I²C port still let the main chip learn that it was scanned and read or write a short record, such as whether the tool is in or out.

{% include figure.html src="/Images/synctag-schematic.png" alt="KiCad schematic sheet with seven boxed sections: power, supply decoupling, the CC2340R52 chip, a crystal, the RF filter and antenna, the NFC flex connector, an LED and the programming pads" caption="The main-board schematic, exported from KiCad." fulllink=true %}

## Power and battery life

The modelled life depends mostly on how the tag advertises. A tag that advertises every 5 s so it can be found lasts about 0.84 years in a typical workshop pattern. If it only sends a slow beacon while the tool is in the box, which the NFC check-in tells it, and advertises quickly only while the tool is out, the same pattern gives about 1.9 years. The floor with no radio use at all is about 2.8 years at 10 °C.

| Usage pattern | Modelled life (state-aware schedule) |
| --- | --- |
| Typical workshop (tool checked out 5 % of the time) | about 1.7 to 2.1 years |
| Cold garage, heavy find use | about 0.5 to 0.7 years |

{% include figure.html src="/Images/synctag-battery-life.png" alt="Two charts: bars of estimated cell life for four usage patterns with a state-aware schedule roughly doubling life, and a line of life against advertising interval rising from about 0.1 to 2.2 years" caption="Left: life by usage pattern, fixed adverts against the state-aware schedule. Right: life against a fixed advertising interval for the typical pattern. Model output." fulllink=true %}

This is a model. The advertising current, the usable fraction of the cell and the temperature factors are my assumptions, and the range only varies the advertising charge. The bigger unknown is the cell itself: Panasonic does not publish the CR1025's internal resistance, and below about 136 Ω the supply would sag under the chip's 1.71 V minimum during a transmit burst with the LED on. That could end the tag's life earlier than the table says, so it needs measuring at 0 °C and 20 °C.

## Antennas

**Bluetooth (2.4 GHz).** The chip antenna sits at the east end of the board with a 4 × 6 mm area on every layer kept free of copper, as the manufacturer requires. The feed is a 0.20 mm grounded coplanar line over a solid ground plane, with no vias, through TI's reference filter and a DC block. For an assumed 0.10 mm dielectric a quasi-static calculation gives 48.5 to 50.1 Ω, depending on the material. It is sensitive: 0.01 mm of dielectric height moves it about 2.5 Ω, and I have not yet confirmed the fabricator's stack-up. Two tuning capacitor slots are left empty because the manufacturer says the matching values depend on the board. The 72 % efficiency in Johanson's data sheet is for their own 40 × 20 mm test board, **not for this tag**. A small ground area, a cell close to the antenna and a metal tool are all known to detune a chip antenna, so I expect this one to do worse. I have not measured it.

**NFC (13.56 MHz).** The coil is on the flex: two layers of six turns, 0.15 mm track and gap, 9.5 × 8.5 mm outside, with a ferrite sheet behind it to shield the coil from the metal underneath. A partial-inductance model gives about 1.7 µH, with an uncertainty of about 10 %. With the NT3H2111's input capacitance that resonates near 16.6 MHz in free air, so a trim capacitor slot lets me pull it down toward 13.56 MHz on the real assembly. I do not claim a read distance. A coil this small against a ferrite and a metal tool will probably have a short range, and only a reader can say how short.

{% include figure.html src="/Images/synctag-flex-render.png" alt="Angled 3D render of a green flex circuit with a small chip and capacitors at the left, a five-finger tail and a square spiral coil on the right" caption="The NFC flex: the spiral coil on the right, the NT3H2111 and its parts on the left, and the five fingers at the far left that solder to the main board. Render." class="fig-medium" %}

## The layout

The main board has four layers at 0.8 mm. The second layer is a solid ground plane that serves as the reference under the RF feed. Tracks and gaps are 0.10 mm, the vias are 0.20 mm drills, and the 0.20 mm RF line has its own rule set. These are near the limit of a standard board service, so I would confirm them with a fabricator before ordering.

I placed the parts that are fixed by the physics first: the antenna and its keep-out at the end, the RF chain in signal order along one edge, the crystal under the chip and the cell retainer on the underside. I wrote scripts to place and route the rest. Routing took several rounds. At first four connections would never route. Making the board bigger on its own did not fix it; what worked was keeping clear zones for the RF feed and the crystal, and then testing small placement changes with the real router in the loop until every connection was made. The board ended up at 26.4 mm long where the first attempt was 23.4 mm, and I did not retry the shorter lengths with the final method, so part of that growth may be a limit of my scripts. KiCad's checker, not my router, is the judge of the result.

{% include figure.html src="/Images/synctag-assembly.png" alt="Two flat drawings: the main board top side with labelled parts, five test pads, the hatched antenna keep-out and the antenna, and below it the NFC flex with its chip, passives and square coil outline" caption="Assembly drawing of both boards from the design files: reference designators, the three unfitted tuning slots (C14, C15 and C21) and the antenna keep-out." fulllink=true %}

## What has been checked, and what has not

All of these were run in software on 16 October 2026 against the design as generated:

| Check | Result |
| --- | --- |
| KiCad 9.0.7 electrical rules check, both schematics, no exclusions | 0 violations on each |
| Design rules check with schematic parity, main board | 0 errors, 0 unconnected items, 0 parity differences; 15 warnings, all about the footprint copy differing from the library copy because I moved the silkscreen to the fabrication layer |
| Design rules check with schematic parity, NFC flex | the same, with 7 such warnings |
| Host-side byte layout of the tag's messages | 6 unit tests pass, which proves the encoder and decoder agree with each other and nothing about the radio |
| Stack height, battery model, line impedance, coil inductance | calculated; models, not measurements |

I turned off no checks and added no exclusions to get those results. Still to do:

- **A layout review.** The board was placed and routed by my scripts and has not had a proper human review. I am going through it by hand in KiCad. For example, a few vias sit inside pads of their own net, which the checker allows but which can wick solder away, so I am moving those.
- **Parts.** On 16 October 2026 at DigiKey UK the CC2340R52, the 0201-size 100 nF and 1 µF capacitors and the P-FET showed no stock, one filter inductor is obsolete and the crystal is sold only on a 3,000-piece reel. I could not open other UK distributors, so the design may not be buildable in small numbers until that is resolved.
- **Firmware.** There is a written architecture (the states, timers, the advertising format and how the toolbox finds a tag), but nothing has been compiled or run.
- **Everything physical:** build and bring up the boards, measure the current in each state, the cell's voltage under load, whether the NFC field really wakes the chip, the Bluetooth range and the NFC read distance, and tune the matching on the real assembly and on a metal tool.
- **No sound.** The tag can only flash in this revision. A piezo needs about 2 mm more height, so I would choose one before the enclosure is fixed.

## What I would do next

1. Finish the layout review and re-run the checks.
2. Resolve the part availability, then order a few boards and the flex.
3. Write and test the firmware, starting with current measurement in each state.
4. Measure the cell under load, the NFC wake-up, and the antenna and read range, then adjust the tuning parts.
5. Put the revised tag into the casing and the toolbox, and decide on a buzzer for Rev B.
