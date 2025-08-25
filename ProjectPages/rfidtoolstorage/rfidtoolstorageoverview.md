---
layout: default
title: ToolSync — Digital Tracking Toolbox
---
The inspiration for my 4th-year project came from a challenge I frequently encounter: managing tools efficiently. Whether during my workday at a Van Conversion company or in my own workspace, I’ve noticed how much time and effort can be wasted searching for misplaced tools in cluttered or poorly designed storage systems.

This project aims to tackle that problem by designing an innovative tool storage solution. My goal is to create a system that not only organizes tools effectively but also improves accessibility and minimises downtime, offering a practical solution for professionals and hobbyists alike.

ToolSync is a smart toolbox designed to reduce lost time and misplaced tools.  
It pairs a heavy-duty tool chest with digital tracking and a Raspberry Pi–powered touchscreen interface.  
A passive HF RFID reader manages check-in/out, while small BLE tags (*SyncTags*) attached to each tool can flash or beep when a tool goes missing.

## Electrical Architecture
**Power strategy.** The toolbox takes **230 V mains** as primary input and **bypasses a two-gang socket** (mains-only) so users can power tools without adding an inverter. A **230 V→5 V step-down** feeds and charges the low-voltage subsystem and onboard battery. This reduces conversion losses and cost/complexity.

**Connectors & serviceability.** A standard **C13 inlet** is used for input. All 5 V peripherals terminate to **quick-release 4-pin modular connectors**; a universal 4-pin pattern is reused (blanking unused pins) to reduce variation and speed maintenance.

**Cooling.** The Pi runs close to thermal limits under memory/output load, so a dedicated **DC fan** prevents throttling and stabilizes operation. Keep CPU < 85 °C per Raspberry Pi guidance.

**Power budget & runtime.**  
Peak draw (Pi, display, LEDs, TX module, USB) sums to **≈33.15 W**; typical/idle usage is ~**11.08 W**, yielding **~13.9 h** on the 12 V/5 V 12 800 mAh pack. Calculations and tables are documented in Stage 2.

**Safety & noise.** A **7.5 A fuse** (matched to 16 AWG wiring) is placed directly after the battery; a **battery isolator** prevents parasitic drain. The metal frame is **chassis-grounded**; I²C noise is mitigated with secure terminations and stable harnessing.

## Software & UI Design (on-device)
**Platform & comms.** A Raspberry Pi handles **RFID scanning (PN532)**, **JSON** data storage, and a **CustomTkinter** GUI over **I²C**, chosen for low wiring complexity and GPIO headroom.

**GUI layout.** A sidebar navigates drawers; the main panel renders tool tiles (e.g., “10 mm Spanner”) with **status dots**—green = available, red = missing—plus panels for editing tools and account/system settings.

**Data model.** Each user has a local JSON file keyed by drawer (`D1…D7`), with `uid` (SyncTag/ RFID) and `status` (1/0). Example structure is included in the Stage 2 report.

**Real-time updates.** A background **thread** continuously scans for RFID tags, then **inverts the tool’s status** and **refreshes** the UI so the overview stays live as items are added/removed/scanned.

**RFID parsing.** The PN532 returns hex bytes; a custom **hex→decimal UID** parser normalizes inconsistent tag formats and edge cases before lookup.

**Boot behaviour.** A systemd service (`tool_sync.service`) autostarts the UI after boot to make the box a single, appliance-like system.

## SyncTag (miniature PCB on tools)
**Component selection.** The tag integrates a **BK3432 BLE module**, **RFID receiver**, **buzzer** (80 dB) and **LED** with MOSFET switching, chosen for size, audibility, and low power.

**Power choice.** After evaluating miniature cells, the design standardizes on a **CR1025 (≈30 mAh)** for the best size-to-life trade-off and easy replacement.

**Protection & signalling.** The PCB includes **diodes for backflow protection** to isolate BLE/RFID interrupts and protect sensitive components from transients.

## Design for Service & Manufacture
- **Modular harnessing** with repeated 4-pin connectors reduces SKU sprawl and field repair time.
- **Grounded steel chassis** and protected runs minimize failures in harsh shop environments. 
- **Tool-level UX**: instant visual status and one-scan add/remove flows reduce drawer-diving and data entry.

## Tech Stack
- **Hardware:** Raspberry Pi, PN532 RFID, C13 mains inlet, 230→5 V converter, DC fan, modular 4-pin harness, 12 V/5 V 12 800 mAh battery.
- **Firmware/Software:** Python (CustomTkinter UI), systemd service, JSON data store, threaded PN532 polling, UID normalization.
- **SyncTag PCB:** BK3432 BLE, RFID RX, LED+buzzer via MOSFET, CR1025 coin cell, protective diodes.
