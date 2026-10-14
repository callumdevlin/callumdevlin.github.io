---
title: RX-8 OMP Lab
permalink: /ProjectPages/RX8/OMP/lab/
section: omp
nav_order: 5
toc: false
description: >
  An interactive version of the Series 1 RX-8 oil metering pump: how engine speed,
  load and coolant temperature set the commanded step, and how the start-up checks,
  switch faults and a jammed mechanism play out.
---

This is the companion to the [Series 1 OMP guide](/ProjectPages/RX8/OMP/). It models the stock pump only. The commanded-step tables come from a community-decoded six-port ROM that I haven't confirmed against my own ECU, and the oil-delivery figures are a derived estimate rather than a measurement. The lab lists its sources under *Model notes and sources*.

{% include lab-embed.html path="/tools/rx8-omp/" source="rx8-omp-lab" title="RX-8 OMP Lab: interactive oil metering pump teaching tool" height=2600 small=3700 %}
