---
title: ToolSync, a Digital Tracking Toolbox
crumb: ToolSync
permalink: /ProjectPages/rfidtoolstorage/
type: case-study
description: >
  My fourth-year BEng project: a toolbox that combines RFID check-in and check-out,
  BLE tags that can flash and beep, and a Raspberry Pi touchscreen to stop tools
  going missing.
---

The idea for my fourth-year BEng project came from a problem I run into constantly: managing tools. At work, at a van conversion company, and in my own workshop, I've seen how much time goes on hunting for tools in cluttered or poorly organised storage.

ToolSync is my answer: a toolbox that tracks what's in it. It pairs a heavy-duty tool chest with a Raspberry Pi touchscreen. A passive HF RFID reader handles check-in and check-out, and small BLE tags (*SyncTags*) on the tools can flash and beep when one goes missing, so the box doesn't just tell you something has gone, it helps you find it.

This page describes the design and the software. It doesn't yet itemise which parts were built and bench-tested or give measured results, and I've labelled the figures that are calculations rather than measurements.
{:.note}

## Electrical architecture

The toolbox takes **230 V mains** through a standard **C13 inlet**. The mains also feeds a two-gang socket, so tools can be powered from the box without an inverter. A 230 V to 5 V converter feeds the low-voltage subsystem and charges the onboard battery, which keeps conversion losses, cost and complexity down.

Serviceability drove the wiring strategy. Every 5 V peripheral ends in a quick-release **4-pin modular connector**, reusing one pin pattern throughout with the unused pins blanked. One connector type means less variation, fewer spares and faster maintenance when something needs swapping in the field.

A Raspberry Pi runs warm under sustained display and scanning load, so a dedicated DC fan keeps it clear of its thermal limits. Raspberry Pi defines that limit as 85 °C on all models, and a Pi 4 starts to throttle progressively from 80 °C (a 3B+ has a 60 °C soft limit by default). I haven't recorded which model the box uses or logged its temperatures here.

### Power budget

Peak draw across the Pi, display, LEDs, transmitter module and USB comes to roughly **33 W**, and typical idle use is around **11 W**. Taking the 12,800 mAh pack as a 12 V battery, that is 153.6 Wh, which at 11 W is about **14 hours** of runtime away from mains. That is a calculated best case. It ignores converter losses, the usable fraction of the battery and voltage sag, so a real figure will be lower, and I haven't recorded a measured runtime.

### Protection

Safety is handled in layers: a **7.5 A fuse** matched to the 16 AWG wiring sits directly after the battery, a battery isolator prevents parasitic drain in storage, the steel frame is chassis-grounded, and I²C noise is managed through secure terminations and stable harness routing. This is a box for workshops, not a desk.

## Software and interface

A Raspberry Pi handles RFID scanning through a **PN532** module over I²C, stores data locally in **JSON**, and runs a touchscreen GUI built with **CustomTkinter**. I²C was chosen for its low wiring complexity and the GPIO headroom it leaves.

The interface is built around how someone uses a toolbox. A sidebar moves between drawers, and the main panel shows tool tiles ("10 mm Spanner" and so on), each with a status dot: green for available, red for missing. Further panels handle adding and editing tools and the account and system settings.

Each user has a local JSON file keyed by drawer (`D1` to `D7`), storing each tool's tag `uid` and a simple in/out `status`. A background **thread** polls the RFID reader continuously. When a tagged tool is scanned it inverts that tool's status and refreshes the UI, so the overview stays live as items come and go. The PN532 returns raw hex bytes, and real tags turned out to be inconsistent in format, so a custom hex-to-decimal UID parser normalises tags and edge cases before lookup.

To make it feel like an appliance rather than a computer, a systemd service (`tool_sync.service`) starts the UI at boot.

## SyncTag, the tool-mounted PCB

The SyncTag is a miniature PCB that lives on each tool. It integrates a **BK3432 BLE module**, an RFID receiver, an 80 dB buzzer and an LED, with the buzzer and LED switched through MOSFETs chosen for size, audibility and low power. After evaluating miniature cells I standardised on a **CR1025** coin cell (about 30 mAh) as the best size-to-life trade-off, with easy replacement. The board includes backflow-protection diodes to isolate the BLE and RFID interrupts and protect the more sensitive components from transients.

## Design for service and manufacture

A few principles ran through the whole design:

- **Modular harnessing:** the repeated 4-pin connector pattern cuts the number of part variants and field repair time.
- **Built for the environment:** a grounded steel chassis and protected cable runs to survive a working shop.
- **Tool-level interface:** instant visual status and one-scan add and remove flows replace drawer-diving and manual logs.

## Tech stack

- **Hardware:** Raspberry Pi, PN532 RFID reader, C13 mains inlet, 230 V to 5 V converter, DC cooling fan, modular 4-pin harness, 12 V / 5 V 12,800 mAh battery.
- **Software:** Python (CustomTkinter UI), systemd autostart service, JSON data store, threaded PN532 polling, UID normalisation.
- **SyncTag PCB:** BK3432 BLE, RFID receiver, LED and buzzer via MOSFET switching, CR1025 coin cell, protective diodes.

## References

- Raspberry Pi, [thermal limits and throttling](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html), read 2026-10-14.
