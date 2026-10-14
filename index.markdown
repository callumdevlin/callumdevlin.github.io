---
layout: landing
title: Callum Devlin
description: >-
  I'm a mechatronics engineer from Glasgow. At work I design and integrate the
  mechanics of phased-array antenna and RF hardware for satellite communications.
  In my own time I like hands-on automotive, electronics and software projects.
search: true
---

## Selected projects

<ul class="proj-list">
{% include project-row.html href="/ProjectPages/EnduraOMP/" title="EnduraOMP: controlled lubrication for rotary engines" text="An electronically controlled oil metering pump, designed from logged engine data and built as a machined bench prototype." img="/Images/enduraomp-engine-1.webp" %}
{% include project-row.html href="/ProjectPages/E1/" title="MP1: breathing-apparatus stowage" text="A push-to-stow cradle for fire-appliance crew cabs, developed with Emergency One and built as a 1:1 steel prototype." img="/Images/BA_Stowage_20.png" %}
{% include project-row.html href="/ProjectPages/rfidtoolstorage/" title="ToolSync: a toolbox that knows what is in it" text="RFID check-in and check-out, with small tags designed to flash and beep to help find a missing tool." %}
</ul>

## Notebooks

- The [RX-8 workshop notebook](/ProjectPages/RX8/) covers specifications, procedures and engine data for a Series 1 Mazda RX-8.
- The [Rocket League bot notes](/ProjectPages/rlbot/) cover the vectors, steering and path planning behind a hard-coded Python bot.
- The [complete project list](/ProjectPages/) has everything else.

## Search {#looking-for-something-specific}

<form class="site-search site-search-form" role="search" action="{{ '/search/' | relative_url }}" method="get">
<label class="sr-only" for="home-search-q">Search the site</label>
<input id="home-search-q" type="search" name="q" placeholder="e.g. torque, P1688, hose, aerial" autocomplete="off">
<button type="submit">Search</button>
</form>
