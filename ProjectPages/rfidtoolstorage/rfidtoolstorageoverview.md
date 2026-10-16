---
title: ToolSync, a Digital Tracking Toolbox
crumb: ToolSync
permalink: /ProjectPages/rfidtoolstorage/
reviewed: 2026-10-16
image: /Images/optimised/synctag-pcb-render-1200.webp
description: >
  My fourth-year BEng project: a tool chest that tracks its contents with RFID, and
  SyncTags, small BLE and NFC tags that flash to find a missing tool. A scaled prototype
  was built, and the tag's electronics are designed in KiCad.
---

The idea for my fourth-year BEng project came from a problem I run into constantly: managing tools. At work, at a van conversion company, and in my own workshop, I've seen how much time goes on hunting for tools in cluttered or poorly organised storage.

ToolSync is my answer: a toolbox that tracks what's in it. A heavy-duty tool chest with a Raspberry Pi touchscreen and a passive HF RFID reader handles check-in and check-out. Small tags on the tools, the SyncTags, carry the tool's identity and flash when the toolbox asks for that tool, so the box doesn't just tell you something has gone, it helps you find it. I built a working scaled prototype of the toolbox, and I designed the SyncTag's electronics in KiCad 9 (it is not built yet, see [the SyncTag](#the-synctag)).

## Research and concept

I started with a survey, interviews and shadowing, and looked at how people actually store and lose tools. Concept generation and a controlled convergence matrix narrowed a wide set of ideas to the digital tracking toolbox, which a focus group and a product champion then reviewed.

## The toolbox

The full-size design is a welded box-section steel frame with laser-cut 3 mm aluminium drawers and side panels, heavy-duty drawer runners and castors, LED lighting and a work surface on top. A key lock latches every drawer at once through a cam and a connecting bar. The plastic parts are designed as injection-moulded ABS. I checked the drawer forces and the force to turn the lock by calculation, and the screen angle and handle heights against anthropometric data.

The box runs from 230 V mains through a C13 inlet, with a converter feeding the Raspberry Pi, the touchscreen and an onboard battery, and a two-gang socket so tools can be powered from the box. Every 5 V peripheral ends in the same quick-release 4-pin connector, which keeps the wiring simple to service.

A Raspberry Pi reads tags through a PN532 module over I²C and runs a touchscreen interface built with CustomTkinter. A sidebar moves between drawers, and each tool is a tile with a green dot for available or a red one for missing. Each tool's tag ID and in/out status are kept in a local JSON file keyed by drawer (`D1` to `D7`). Scanning a tagged tool flips its status and refreshes the screen, and a systemd service starts the program at boot, so the box behaves like an appliance rather than a computer.

## The SyncTag

The SyncTag is the small tag that sits on each tool. Its electronics are two boards drawn in KiCad 9: a 26.4 × 10.1 mm four-layer main board with a Bluetooth Low Energy (BLE) chip, antenna and coin cell, and a separate NFC antenna flex. KiCad's own electrical and design rule checks report no errors on either board. **Nothing has been built, powered or measured, and no tag firmware exists yet**, so every performance figure in this section is a data-sheet number or a model, and I say which.

{% include figure.html src="/Images/synctag-pcb-render.png" alt="Angled 3D render of a long thin green circuit board with a black square chip in the middle, small capacitors, five pads along the left edge, a red LED and a cream chip antenna at the right-hand end" caption="The SyncTag main board, rendered from the KiCad design. The part bodies are placeholder shapes, not manufacturer models." eager=true %}

### What the tag has to do

- **Be read with no battery.** The toolbox's RFID reader checks tools in and out, so the tool's identity has to be readable even when the tag's cell is flat.
- **Be found.** When a tool is missing, the toolbox sends a Bluetooth command and the tag flashes.
- **Run from a replaceable coin cell** for as long as it can, since nobody will want to open a tool tag often.
- **Stay small enough to stick on a tool.** The cell sets the size: a CR1025 is 10.0 mm across, so the board is 10.1 mm wide and the tag comes to about 28.0 × 11.5 × 7.3 mm outside.

### The design

| Block | Choice | Why |
| --- | --- | --- |
| Identity | NXP NT3H2111 (NTAG I²C plus) on its own two-layer flex with a 13.56 MHz coil and a ferrite sheet | powered by the reader's field, so the toolbox can always read it; its output pin and I²C port let the main chip learn it was scanned |
| Bluetooth chip | TI CC2340R52 (Cortex-M0+, BLE 5.4, about 0.7 µA standby, built-in DC/DC) | low standby current, and a documented reference design for the antenna filter and crystal |
| Antenna | Johanson 2450AT18D0100001E chip antenna at the board edge, TI's reference harmonic filter and two unfitted tuning slots | small enough for the board, with a manufacturer-recommended layout |
| Alert | one red LED behind the diffuser | a coin cell cannot supply the roughly 15 mA of a magnetic buzzer, and a piezo needs about 2 mm more height |
| Cell | CR1025 (30 mAh) in a Keystone 3030 retainer on the underside, with a P-FET against a reversed cell | replaceable and as small as a coin cell gets |
| Clocks | 48 MHz crystal; 32 kHz from the chip's internal oscillator | a 32 kHz crystal did not fit |
| Programming | five SWD and test pads | to program and debug the first boards |

The nominal height of the stack is 6.86 mm and the worst case 7.23 mm, against a 7.0 mm target, so a prototype enclosure has to confirm it.

{% include figure.html src="/Images/synctag-block-diagram.png" alt="Block diagram: cell and reverse-battery protection feed the CC2340R52 chip in the centre, which connects to the RF filter and chip antenna, an indicator LED, programming pads and the NFC flex, which talks to the ToolSync toolbox" caption="Block diagram of the SyncTag." fulllink=true %}

#### Why NFC identity is a separate passive part

If the Bluetooth chip pretended to be the NFC tag itself, the tool's identity would vanish whenever the cell went flat, and the toolbox would stop seeing it. The NT3H2111 is powered by the reader's field, so the toolbox's PN532 can always read the tool's ID with no battery. Its output pin and I²C port still let the main chip learn that it was scanned and read or write a short record, such as whether the tool is in or out.

{% include figure.html src="/Images/synctag-schematic.png" alt="KiCad schematic sheet with seven boxed sections: power, supply decoupling, the CC2340R52 chip, a crystal, the RF filter and antenna, the NFC flex connector, an LED and the programming pads" caption="The main-board schematic, exported from KiCad." fulllink=true %}

### Power and battery life

The modelled life depends mostly on how the tag advertises. A tag that advertises every 5 s so it can be found lasts about 0.84 years in a typical workshop pattern. If it only sends a slow beacon while the tool is in the box, which the NFC check-in tells it, and advertises quickly only while the tool is out, the same pattern gives about 1.9 years. The floor with no radio use at all is about 2.8 years at 10 °C.

| Usage pattern | Modelled life (state-aware schedule) |
| --- | --- |
| Typical workshop (tool checked out 5 % of the time) | about 1.7 to 2.1 years |
| Cold garage, heavy find use | about 0.5 to 0.7 years |

{% include figure.html src="/Images/synctag-battery-life.png" alt="Two charts: bars of estimated cell life for four usage patterns with a state-aware schedule roughly doubling life, and a line of life against advertising interval rising from about 0.1 to 2.2 years" caption="Left: life by usage pattern, fixed adverts against the state-aware schedule. Right: life against a fixed advertising interval for the typical pattern. Model output." fulllink=true %}

This is a model. The advertising current, the usable fraction of the cell and the temperature factors are my assumptions, and the range only varies the advertising charge. The bigger unknown is the cell itself: Panasonic does not publish the CR1025's internal resistance, and below about 136 Ω the supply would sag under the chip's 1.71 V minimum during a transmit burst with the LED on. That could end the tag's life earlier than the table says, so it needs measuring at 0 °C and 20 °C.

### Antennas

**Bluetooth (2.4 GHz).** The chip antenna sits at the east end of the board with a 4 × 6 mm area on every layer kept free of copper, as the manufacturer requires. The feed is a 0.20 mm grounded coplanar line over a solid ground plane, with no vias, through TI's reference filter and a DC block. For an assumed 0.10 mm dielectric a quasi-static calculation gives 48.5 to 50.1 Ω, depending on the material. It is sensitive: 0.01 mm of dielectric height moves it about 2.5 Ω, and I have not yet confirmed the fabricator's stack-up. Two tuning capacitor slots are left empty because the manufacturer says the matching values depend on the board. The 72 % efficiency in Johanson's data sheet is for their own 40 × 20 mm test board, **not for this tag**. A small ground area, a cell close to the antenna and a metal tool are all known to detune a chip antenna, so I expect this one to do worse. I have not measured it.

**NFC (13.56 MHz).** The coil is on the flex: two layers of six turns, 0.15 mm track and gap, 9.5 × 8.5 mm outside, with a ferrite sheet behind it to shield the coil from the metal underneath. A partial-inductance model gives about 1.7 µH, with an uncertainty of about 10 %. With the NT3H2111's input capacitance that resonates near 16.6 MHz in free air, so a trim capacitor slot lets me pull it down toward 13.56 MHz on the real assembly. I do not claim a read distance. A coil this small against a ferrite and a metal tool will probably have a short range, and only a reader can say how short.

{% include figure.html src="/Images/synctag-flex-render.png" alt="Angled 3D render of a green flex circuit with a small chip and capacitors at the left, a five-finger tail and a square spiral coil on the right" caption="The NFC flex: the spiral coil on the right, the NT3H2111 and its parts on the left, and the five fingers at the far left that solder to the main board. Render." class="fig-medium" %}

### The layout

The main board has four layers at 0.8 mm. The second layer is a solid ground plane that serves as the reference under the RF feed. Tracks and gaps are 0.10 mm, the vias are 0.20 mm drills, and the 0.20 mm RF line has its own rule set.

I placed the parts that are fixed by the physics first: the antenna and its keep-out at the end, the RF chain in signal order along one edge, the crystal under the chip and the cell retainer on the underside. I wrote scripts to place and route the rest. Routing took several rounds. At first four connections would never route. Making the board bigger on its own did not fix it; what worked was keeping clear zones for the RF feed and the crystal, and then testing small placement changes with the real router in the loop until every connection was made. The board ended up at 26.4 mm long where the first attempt was 23.4 mm. KiCad's checker, not my router, is the judge of the result.

{% include figure.html src="/Images/synctag-assembly.png" alt="Two flat drawings: the main board top side with labelled parts, five test pads, the hatched antenna keep-out and the antenna, and below it the NFC flex with its chip, passives and square coil outline" caption="Assembly drawing of both boards from the design files: reference designators, the three unfitted tuning slots (C14, C15 and C21) and the antenna keep-out." fulllink=true %}

## Prototyping

I planned a full-scale prototype, but at the start of Stage 2 I judged that a full-size box wasn't feasible in the time, and built a scaled-down proof of concept instead.

- The toolbox prototype uses a pre-made miniature toolbox with the real electronics: a Raspberry Pi, the RFID module and a display, managing two drawers. Tool detection, data storage and the interface run as they would in the full design. I left Bluetooth out because the tag's circuit board was not ready to build, although the software is structured to accept it.
- The SyncTag casing is a 1:1 TPU print. Trying wall thicknesses from 1.0 to 3.5 mm showed that 2.5 mm protects the electronics and still bends to stick to a flat tool surface. An RFID sticker inside the casing stands in for the tag electronics, which let tools be checked in and out as designed. The tags read without interference against tools, the toolbox and other metal. The finished tag is a rigid board of about 28.0 × 11.5 × 7.3 mm, so its casing would be rigid and larger than this print, which tested the stick-on idea and the wall thickness.
- The locking mechanism is a 1:1 plywood model, CNC-cut with a technician's help. It showed the cam lifting the latch hooks together and worked without changes.
- A scaled handle prototype went to a group of tradesmen. They found the shape comfortable but the bare edge hard to grip with greasy hands, so the design gained a rubber trim.

## Evaluation

I lent the prototype, with SyncTags and a working electronics housing, to a friend, who used it on a car job and found check-in and check-out useful for keeping track of tools and for tidying up. I also showed the prototype to focus groups at a van conversion company and a bodyshop. The response was positive, and the main suggestion was a larger screen for reading at a distance.

A costing for the full-size toolbox came to about £391 to manufacture, excluding the tags, whose cost depends on the final bill of materials, which I have not totalled.

## Outcome

The project met its aims apart from the full-scale prototype. The working prototype demonstrates check-in and check-out, the tag casing and the locking mechanism. The full-size toolbox exists as a design, and so does the SyncTag's circuit board, which has passed software design checks but has not been built.

## Further development

The next steps are building and testing the SyncTag so it can flash on command (and revisiting a buzzer), building a full-scale model, refining the manufacturing processes, and trying a larger display.
