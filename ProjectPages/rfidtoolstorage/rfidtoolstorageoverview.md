---
title: ToolSync, a Digital Tracking Toolbox
crumb: ToolSync
permalink: /ProjectPages/rfidtoolstorage/
reviewed: 2026-10-14
description: >
  My fourth-year BEng project: a tool chest that tracks its contents with RFID and a
  Raspberry Pi touchscreen, with BLE and NFC tags that flash to find a missing tool,
  built as a working scaled prototype with a KiCad design for the tag.
---

The idea for my fourth-year BEng project came from a problem I run into constantly: managing tools. At work, at a van conversion company, and in my own workshop, I've seen how much time goes on hunting for tools in cluttered or poorly organised storage.

ToolSync is my answer: a toolbox that tracks what's in it. It pairs a heavy-duty tool chest with a Raspberry Pi touchscreen. A passive HF RFID reader handles check-in and check-out, and small BLE tags (SyncTags) on the tools are designed to flash when one goes missing, so the box doesn't just tell you something has gone, it helps you find it.

## Research and concept

I started with a survey, interviews and shadowing, and looked at how people actually store and lose tools. Concept generation and a controlled convergence matrix narrowed a wide set of ideas to the digital tracking toolbox, which a focus group and a product champion then reviewed.

## Design development

### The toolbox

The full-size design is a welded box-section steel frame with laser-cut 3 mm aluminium drawers and side panels, heavy-duty drawer runners and castors, LED lighting and a work surface on top. A key lock latches every drawer at once through a cam and a connecting bar. The plastic parts are designed as injection-moulded ABS. I checked the drawer forces and the force to turn the lock by calculation, and the screen angle and handle heights against anthropometric data.

### Electrical architecture

The toolbox takes 230 V mains through a standard C13 inlet. The mains also feeds a two-gang socket, so tools can be powered from the box without an inverter. A 230 V to 5 V converter feeds the low-voltage subsystem and charges the onboard battery.

Serviceability drove the wiring. Every 5 V peripheral ends in a quick-release 4-pin connector, reusing one pin pattern throughout with the unused pins blanked, so there is less variation, fewer spares and faster maintenance. A small DC fan keeps the Raspberry Pi clear of the 85 °C limit Raspberry Pi gives for its processors.

#### Power budget

Peak draw across the Pi, display, LEDs, transmitter module and USB comes to roughly 33 W, and typical use is around 11 W. Taking the 12,800 mAh pack as a 12 V battery, that is 153.6 Wh, which gives about 4.6 hours at peak and about 14 hours at 11 W away from mains. These are calculated from the pack's rating, so a real runtime will be lower.

#### Protection

A 7.5 A fuse matched to the 16 AWG wiring sits directly after the battery, a battery isolator prevents drain in storage, the steel frame is chassis-grounded, and I²C noise is managed through secure terminations and stable harness routing.

### Software and interface

A Raspberry Pi handles RFID scanning through a PN532 module over I²C, stores data locally in JSON, and runs a touchscreen GUI built with CustomTkinter. I²C was chosen for its low wiring complexity and the GPIO headroom it leaves.

The interface is built around how someone uses a toolbox. A sidebar moves between drawers, and the main panel shows tool tiles ("10 mm Spanner" and so on), each with a status dot: green for available, red for missing. Further panels handle adding and editing tools and the account and system settings.

Each user has a local JSON file keyed by drawer (`D1` to `D7`), storing each tool's tag `uid` and a simple in/out `status`. A background thread polls the RFID reader continuously. When a tagged tool is scanned it inverts that tool's status and refreshes the UI, so the overview stays live as items come and go. The PN532 returns raw hex bytes, and real tags turned out to be inconsistent in format, so a custom hex-to-decimal UID parser normalises tags and edge cases before lookup. A systemd service (`tool_sync.service`) starts the UI at boot, so it behaves like an appliance rather than a computer.

### SyncTag, the tool-mounted PCB

The SyncTag is a miniature PCB that lives on each tool, drawn in KiCad 9. A TI CC2340R52 Bluetooth chip with a chip antenna sits on a four-layer main board, and a separate NFC flex carries an NXP NT3H2111, so the toolbox's reader can identify the tool with no battery in the tag. The alert is a red LED that flashes when the toolbox asks for the tool, and the power is a replaceable CR1025 coin cell (about 30 mAh) with reverse-battery protection. There is no buzzer in this revision, because a coin cell cannot supply one. The cell sets the size, so the tag comes to about 28.0 × 11.5 × 7.3 mm outside.

The modelled battery life is about 1.7 to 2.1 years for a typical workshop pattern, because the tag only advertises slowly while the tool is in the box. KiCad's electrical and design rule checks report no errors on either board, but nothing has been built or measured and there is no tag firmware, so the battery life, range and antenna performance are all estimates.

The full write-up, with the schematic, antenna design, power model and what is still unverified, is on its own page: [SyncTag, the tool tag's circuit board](/ProjectPages/rfidtoolstorage/synctag-pcb/).

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

The project met its aims apart from the full-scale prototype. The working prototype demonstrates check-in and check-out, the tag casing and the locking mechanism. The full-size toolbox exists as a design, and so does the tag's circuit board, which has passed software design checks but has not been built.

## Further development

The next steps are refining the manufacturing processes, building and testing the Bluetooth tag so it can flash (and revisiting a buzzer), building a full-scale model, and trying a larger display.

## References

- Raspberry Pi, [thermal limits and throttling](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html), accessed 14 October 2026.
