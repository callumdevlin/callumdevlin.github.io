---
title: ToolSync — Digital Tracking Toolbox
permalink: /ProjectPages/rfidtoolstorage/
description: >
  My 4th-year BEng project — a smart toolbox combining RFID check-in/out,
  BLE locator tags and a Raspberry Pi touchscreen interface to stop tools
  going missing.
---

The inspiration for my 4th-year BEng project came from a challenge I run into constantly: managing tools efficiently. Whether during my workday at a van conversion company or in my own workspace, I've watched how much time and effort gets wasted hunting for misplaced tools in cluttered or poorly designed storage systems.

ToolSync is my answer: a smart toolbox designed to reduce lost time and misplaced tools. It pairs a heavy-duty tool chest with digital tracking and a Raspberry Pi–powered touchscreen interface. A passive HF RFID reader handles check-in and check-out, while small BLE tags (*SyncTags*) attached to each tool can flash and beep when a tool goes missing — so the box doesn't just tell you something's gone, it helps you find it.

## Electrical Architecture

The toolbox takes **230 V mains** as its primary input through a standard **C13 inlet**, and bypasses a two-gang socket so users can power their tools directly from the box without needing an inverter. A 230 V → 5 V step-down feeds and charges the low-voltage subsystem and onboard battery, which keeps conversion losses, cost and complexity down.

Serviceability drove the wiring strategy. Every 5 V peripheral terminates to quick-release **4-pin modular connectors**, reusing one universal pin pattern throughout (with unused pins blanked). One connector type means less variation, fewer spares, and faster maintenance when something needs swapping in the field.

The Raspberry Pi runs close to its thermal limits under sustained display and scanning load, so a dedicated DC fan keeps the CPU below the 85 °C Raspberry Pi guidance and prevents throttling mid-use.

On the power budget: peak draw across the Pi, display, LEDs, transmitter module and USB sums to roughly **33 W**, but typical idle usage sits around **11 W** — giving about **13.9 hours** of runtime from the 12 800 mAh battery pack when away from mains.

Safety is handled in layers: a **7.5 A fuse** (matched to the 16 AWG wiring) sits directly after the battery, a battery isolator prevents parasitic drain in storage, the steel frame is chassis-grounded, and I²C noise is managed through secure terminations and stable harness routing — this is a box destined for workshop environments, not a desk.

## Software & UI

A Raspberry Pi handles RFID scanning through a **PN532** module over I²C, local data storage in **JSON**, and a touchscreen GUI built with **CustomTkinter**. I²C was chosen for its low wiring complexity and the GPIO headroom it leaves for everything else.

The interface is built around how someone actually uses a toolbox: a sidebar navigates between drawers, and the main panel shows tool tiles — "10 mm Spanner" and so on — each with a status dot, green for available, red for missing. Further panels handle adding and editing tools and account/system settings.

Under the hood, each user has a local JSON file keyed by drawer (`D1`–`D7`), storing each tool's tag `uid` and a simple in/out `status`. A background **thread** continuously polls the RFID reader; when a tagged tool is scanned, it inverts that tool's status and refreshes the UI, so the overview stays live as items come and go. The PN532 returns raw hex bytes, and real-world tags turned out to be inconsistent in format — so a custom hex→decimal UID parser normalises tags and edge cases before lookup.

To make the whole thing feel like an appliance rather than a computer, a systemd service (`tool_sync.service`) autostarts the UI at boot — flip the switch and the toolbox is ready.

## SyncTag — the Tool-Mounted PCB

The SyncTag is a miniature PCB that lives on each tool. It integrates a **BK3432 BLE module**, an RFID receiver, an 80 dB buzzer and an LED, both switched through MOSFETs — chosen for size, audibility and low power. After evaluating miniature cells, I standardised on a **CR1025** coin cell (~30 mAh) as the best size-to-life trade-off with easy replacement. The board includes backflow-protection diodes to isolate the BLE and RFID interrupts and protect the more sensitive components from transients.

## Design for Service & Manufacture

A few principles carried through the whole build:

- **Modular harnessing** — the repeated 4-pin connector pattern cuts SKU sprawl and field repair time.
- **Built for the environment** — grounded steel chassis and protected cable runs to survive a working shop.
- **Tool-level UX** — instant visual status and one-scan add/remove flows replace drawer-diving and manual logs.

## Tech Stack

- **Hardware:** Raspberry Pi, PN532 RFID reader, C13 mains inlet, 230→5 V converter, DC cooling fan, modular 4-pin harness, 12 V/5 V 12 800 mAh battery.
- **Software:** Python (CustomTkinter UI), systemd autostart service, JSON data store, threaded PN532 polling, UID normalisation.
- **SyncTag PCB:** BK3432 BLE, RFID receiver, LED + buzzer via MOSFET switching, CR1025 coin cell, protective diodes.
