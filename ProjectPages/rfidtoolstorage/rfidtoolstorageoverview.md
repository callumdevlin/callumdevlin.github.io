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
**Power strategy.** The toolbox takes **230 V mains** as primary input and **bypasses a two-gang socket** (mains-only) so users can power tools without adding an inverter. A **230 V→5 V step-down** feeds and charges the low-voltage subsystem and onboard battery. This reduces conversion losses and cost/complexity. :contentReference[oaicite:5]{index=5}

**Connectors & serviceability.** A standard **C13 inlet** is used for input. All 5 V peripherals terminate to **quick-release 4-pin modular connectors**; a universal 4-pin pattern is reused (blanking unused pins) to reduce variation and speed maintenance. :contentReference[oaicite:6]{index=6}

**Cooling.** The Pi runs close to thermal limits under memory/output load, so a dedicated **DC fan** prevents throttling and stabilizes operation. Keep CPU < 85 °C per Raspberry Pi guidance. :contentReference[oaicite:7]{index=7}

**Power budget & runtime.**  
Peak draw (Pi, display, LEDs, TX module, USB) sums to **≈33.15 W**; typical/idle usage is ~**11.08 W**, yielding **~13.9 h** on the 12 V/5 V 12 800 mAh pack. Calculations and tables are documented in Stage 2. :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}

**Safety & noise.** A **7.5 A fuse** (matched to 16 AWG wiring) is placed directly after the battery; a **battery isolator** prevents parasitic drain. The metal frame is **chassis-grounded**; I²C noise is mitigated with secure terminations and stable harnessing. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

## Software & UI Design (on-device)
**Platform & comms.** A Raspberry Pi handles **RFID scanning (PN532)**, **JSON** data storage, and a **CustomTkinter** GUI over **I²C**, chosen for low wiring complexity and GPIO headroom. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

**GUI layout.** A sidebar navigates drawers; the main panel renders tool tiles (e.g., “10 mm Spanner”) with **status dots**—green = available, red = missing—plus panels for editing tools and account/system settings. :contentReference[oaicite:14]{index=14}

**Data model.** Each user has a local JSON file keyed by drawer (`D1…D7`), with `uid` (SyncTag/ RFID) and `status` (1/0). Example structure is included in the Stage 2 report. :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}

**Real-time updates.** A background **thread** continuously scans for RFID tags, then **inverts the tool’s status** and **refreshes** the UI so the overview stays live as items are added/removed/scanned. :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}

**RFID parsing.** The PN532 returns hex bytes; a custom **hex→decimal UID** parser normalizes inconsistent tag formats and edge cases before lookup. :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20}

**Boot behaviour.** A systemd service (`tool_sync.service`) autostarts the UI after boot to make the box a single, appliance-like system. :contentReference[oaicite:21]{index=21}

## SyncTag (miniature PCB on tools)
**Component selection.** The tag integrates a **BK3432 BLE module**, **RFID receiver**, **buzzer** (80 dB) and **LED** with MOSFET switching, chosen for size, audibility, and low power. :contentReference[oaicite:22]{index=22}

**Power choice.** After evaluating miniature cells, the design standardizes on a **CR1025 (≈30 mAh)** for the best size-to-life trade-off and easy replacement. :contentReference[oaicite:23]{index=23}

**Protection & signalling.** The PCB includes **diodes for backflow protection** to isolate BLE/RFID interrupts and protect sensitive components from transients. *(See Figure 2 on page ~59 for the schematic.)* :contentReference[oaicite:24]{index=24}

## Design for Service & Manufacture
- **Modular harnessing** with repeated 4-pin connectors reduces SKU sprawl and field repair time. :contentReference[oaicite:25]{index=25}
- **Grounded steel chassis** and protected runs minimize failures in harsh shop environments. :contentReference[oaicite:26]{index=26}
- **Tool-level UX**: instant visual status and one-scan add/remove flows reduce drawer-diving and data entry. :contentReference[oaicite:27]{index=27}

## Tech Stack
- **Hardware:** Raspberry Pi, PN532 RFID, C13 mains inlet, 230→5 V converter, DC fan, modular 4-pin harness, 12 V/5 V 12 800 mAh battery. :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29} :contentReference[oaicite:30]{index=30}  
- **Firmware/Software:** Python (CustomTkinter UI), systemd service, JSON data store, threaded PN532 polling, UID normalization. :contentReference[oaicite:31]{index=31} :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33} :contentReference[oaicite:34]{index=34}  
- **SyncTag PCB:** BK3432 BLE, RFID RX, LED+buzzer via MOSFET, CR1025 coin cell, protective diodes. :contentReference[oaicite:35]{index=35}
