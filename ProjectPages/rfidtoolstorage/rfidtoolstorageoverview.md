---
title: ToolSync, a Digital Tracking Toolbox
crumb: ToolSync
permalink: /ProjectPages/rfidtoolstorage/
reviewed: 2026-10-16
image: /Images/optimised/synctag-pcb-render-1200.webp
description: >
  My fourth-year BEng project: a toolbox that knows which tools are in it, and SyncTags,
  small tags that flash to help find a missing one.
---

ToolSync is a toolbox that knows what is in it. The idea came from a problem I run into constantly: you put a tool down mid-job, someone moves it, and ten minutes later you are hunting for it. ToolSync checks every tool in and out, shows what is missing on a touchscreen, and can make a missing tool's tag flash so you can find it.

## How it works

1. **Check out.** Every tool carries a small tag, the SyncTag. Hold a tool up to the reader and the toolbox logs it as out; hold it up again and it is back in. The tag is read by NFC, so this works even with no battery in the tag.
2. **See what is missing.** The touchscreen shows each drawer, with a tile for every tool and a green or red dot for in or out.
3. **Find it.** Press find on a missing tool and the toolbox sends a Bluetooth message. That tool's tag flashes.

Two radios do two jobs. NFC (13.56 MHz) handles identity: it has a short range, suits a metal toolbox better than UHF RFID, and needs no power in the tag. Bluetooth Low Energy (2.4 GHz) handles finding, which needs longer range and a little power.

## The toolbox

The toolbox is a tool chest with seven drawers and a single key that locks every drawer at once: the key turns a cam, which lifts a connecting bar, which moves a hook behind each drawer in step. A Raspberry Pi touchscreen and the NFC reader sit on top, and the box runs from mains with a socket to power tools. I checked the drawer forces, the force to turn the lock and the screen angle by calculation.

Inside, the Raspberry Pi reads the tags through a PN532 reader and keeps each tool's tag ID and in/out status against its drawer. Scanning a tool flips its status and the screen updates straight away. The program starts at boot, so the box behaves like an appliance rather than a computer.

## The SyncTag

The SyncTag is the small tag on each tool: a 26.4 × 10.1 mm four-layer main board with a Bluetooth chip, a chip antenna and a replaceable CR1025 coin cell, plus a separate NFC flex that carries the coil. Both boards are designed in KiCad 9 and pass its electrical and design rule checks with no errors. The tag measures about 28 × 11.5 × 7.3 mm outside.

{% include figure.html src="/Images/synctag-pcb-render.png" alt="Angled 3D render of a long thin green circuit board with a black square chip in the middle, small capacitors, five pads along the left edge, a red LED and a cream chip antenna at the right-hand end" caption="The SyncTag main board, rendered from the KiCad design. The part bodies are placeholder shapes." eager=true %}

### How the tag is put together

- **Identity on its own NFC flex.** An NXP NT3H2111 with a 13.56 MHz coil and a ferrite sheet. It is powered by the reader's field, and its output pin tells the main chip when the tag has been scanned.
- **Bluetooth.** A TI CC2340R52 with a Johanson chip antenna at the end of the board. It draws about 0.7 µA asleep.
- **Alert.** A red LED behind a diffuser. There is no buzzer: a coin cell cannot supply the current one needs.
- **Power.** A CR1025 in a retainer on the underside, so the cell can be changed, with a P-FET that blocks a reversed cell.

{% include figure.html src="/Images/synctag-block-diagram.png" alt="Block diagram: cell and reverse-battery protection feed the CC2340R52 chip in the centre, which connects to the RF filter and chip antenna, an indicator LED, programming pads and the NFC flex, which talks to the ToolSync toolbox" caption="Block diagram of the SyncTag." fulllink=true %}

#### Why identity is a separate passive part

If the Bluetooth chip pretended to be the NFC tag itself, the tool's identity would vanish whenever the cell went flat and the toolbox would stop seeing it. Putting the identity on the NT3H2111 means the toolbox can always read the tool, whatever state the battery is in. The chip's I²C port still lets the main chip read or write a short record, such as whether the tool is in or out.

{% include figure.html src="/Images/synctag-schematic.png" alt="KiCad schematic sheet with seven boxed sections: power, supply decoupling, the CC2340R52 chip, a crystal, the RF filter and antenna, the NFC flex connector, an LED and the programming pads" caption="The main-board schematic, exported from KiCad." fulllink=true %}

### Making a coin cell last

A CR1025 holds about 30 mAh, so the tag has to spend almost all its time asleep. The main cost is advertising, the Bluetooth beacons that let the toolbox find the tag. A tag that advertises every 5 s lasts an estimated 0.84 years in a typical workshop pattern. The tag does not need to do that while it is in the box, because the NFC check-in already tells it so. It sends a slow beacon while in the box and advertises quickly only while the tool is out. The same pattern then gives an estimated 1.7 to 2.1 years, and the floor with no radio use at all is about 2.8 years.

{% include figure.html src="/Images/synctag-battery-life.png" alt="Two charts: bars of estimated cell life for four usage patterns with a state-aware schedule roughly doubling life, and a line of life against advertising interval rising from about 0.1 to 2.2 years" caption="Left: estimated life by usage pattern, fixed adverts against the in-box and out-of-box schedule. Right: estimated life against a fixed advertising interval for the typical pattern." fulllink=true %}

### Antennas

**Bluetooth.** The chip antenna sits at the end of the board with an area on every layer kept free of copper, as the manufacturer requires. The signal reaches it along a 0.20 mm coplanar line over a solid ground plane, which a calculation puts at about 50 Ω, through TI's reference filter. Two empty capacitor slots let the match be tuned to the real board.

**NFC.** The coil is on the flex: two layers of six turns, 9.5 × 8.5 mm, about 1.7 µH from a partial-inductance model, with a ferrite sheet behind it to shield it from the metal underneath. A trim capacitor slot lets it be tuned to 13.56 MHz.

{% include figure.html src="/Images/synctag-flex-render.png" alt="Angled 3D render of a green flex circuit with a small chip and capacitors at the left, a five-finger tail and a square spiral coil on the right" caption="The NFC flex: the spiral coil on the right, the NT3H2111 and its parts on the left, and the five fingers at the far left that solder to the main board." class="fig-medium" %}

### The layout

The main board has four layers, with the second a solid ground plane under the RF feed. The parts fixed by the physics went down first: the antenna and its keep-out at one end, the RF chain in signal order along one edge, the crystal under the chip and the cell retainer on the underside. I wrote scripts to place and route the rest, testing small placement changes with the real router in the loop until every connection was made, and used KiCad's own checker to judge the result.

{% include figure.html src="/Images/synctag-assembly.png" alt="Two flat drawings: the main board top side with labelled parts, five test pads, the hatched antenna keep-out and the antenna, and below it the NFC flex with its chip, passives and square coil outline" caption="Assembly drawing of both boards: reference designators, the three unfitted tuning slots (C14, C15 and C21) and the antenna keep-out." fulllink=true %}
