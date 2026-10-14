---
title: RX-8 OMP Lab
permalink: /ProjectPages/RX8/OMP/lab/
type: lab
section: omp
nav_order: 5
toc: false
description: >
  An interactive version of the Series 1 RX-8 oil metering pump: how engine speed,
  load and coolant temperature set the commanded step, and how the start-up checks,
  switch faults and a jammed mechanism play out.
---

This is the companion to the [Series 1 OMP guide](/ProjectPages/RX8/OMP/). It models the stock pump only.

Two things to keep in mind while you use it. The commanded-step tables come from a community-decoded six-port ROM, and I haven't confirmed that they match my own ECU. The oil-delivery figures are a derived estimate, not a measurement. At step 47 and 9,500 rpm the lab's estimate is about 23 mL/min, against roughly 6.5 mL/min from my own rough, unvalidated figures ([logged data](/ProjectPages/RX8/enginedata/)). I haven't settled which is closer; a controlled bench run would. The lab lists its sources and evidence classes under *Model notes and sources*.

{% include lab-embed.html path="/tools/rx8-omp/" source="rx8-omp-lab" title="RX-8 OMP Lab: interactive oil metering pump teaching tool" height=2600 small=3700 %}
