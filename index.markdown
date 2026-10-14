---
layout: landing
title: Callum Devlin
description: >-
  I'm a mechatronics engineer from Glasgow with a product design engineering
  background. I like projects where the mechanics, electronics and software all
  have to agree: a rotary-engine oil pump, firefighter breathing-apparatus
  stowage, a smart toolbox.
search: true
---

This site has my project write-ups and two notebooks that grew out of my own projects: a workshop reference for a Series 1 Mazda RX-8, and the maths behind a Rocket League bot. Each page says what was measured, what was calculated and what is still an open question.

## Selected projects

<ul class="cards">
<li>{% include card.html href="/ProjectPages/EnduraOMP/" kicker="MEng individual project" title="EnduraOMP: controlled lubrication for rotary engines" text="An electronically controlled oil metering pump with its own oil tank and gauge, designed from logged data on a running 13B-MSP and built as a machined, bench-tested prototype." img="/Images/enduraomp-engine-1.webp" alt="The EnduraOMP pump mounted on a Mazda 13B-MSP engine" %}</li>
<li>{% include card.html href="/ProjectPages/E1/" kicker="Industrial group project" title="MP1: breathing-apparatus stowage" text="A push-to-stow cradle for fire-appliance crew cabs, designed with Emergency One: mechanism, FEA load cases and a fabrication plan." img="/Images/BA_Stowage_20.png" alt="Render of the MP1 breathing-apparatus stowage cradle" contain=true %}</li>
<li>{% include card.html href="/ProjectPages/rfidtoolstorage/" kicker="BEng project" title="ToolSync: a toolbox that knows what is in it" text="RFID check-in and check-out, BLE tags that flash and beep to find a missing tool, and a Raspberry Pi touchscreen." %}</li>
</ul>

## Notebooks

<ul class="cards">
<li>{% include card.html href="/ProjectPages/RX8/" kicker="Reference" title="Mazda RX-8 workshop notebook" text="Specifications, procedures, measured engine data and a guide to the factory oil metering pump, for a Series 1 car." img="/Images/RX8-JackPoints.jpg" alt="Underside diagram of the RX-8 showing jack and support points" contain=true %}</li>
<li>{% include card.html href="/ProjectPages/rlbot/" kicker="Maths and code" title="Rocket League bot notes" text="Vectors, ground and aerial motion and shot alignment for a hard-coded Python bot." img="/Images/rlbot-hero.jpg" alt="A Rocket League match with the bot's debug lines drawn in-game" %}</li>
</ul>

## Interactive labs

<ul class="cards">
<li>{% include card.html href="/ProjectPages/RX8/OMP/lab/" kicker="Interactive lab" title="RX-8 OMP Lab" text="Step through the start-up checks of the factory oil metering pump and see how speed, load and temperature set the commanded step." %}</li>
<li>{% include card.html href="/ProjectPages/RX8/acceleration-lab/" kicker="Interactive lab" title="RX-8 Acceleration Lab" text="Gearing, road speed and full-throttle acceleration for the six-speed and five-speed RX-8, with shift-strategy comparison." %}</li>
</ul>

## Looking for something specific?

<form class="site-search site-search-form" role="search" action="{{ '/search/' | relative_url }}" method="get">
<label class="sr-only" for="home-search-q">Search the site</label>
<input id="home-search-q" type="search" name="q" placeholder="e.g. torque, P1688, hose, aerial" autocomplete="off">
<button type="submit">Search</button>
</form>

Or go straight to the [RX-8 quick reference](/ProjectPages/RX8/quick-reference/), the [torque table](/ProjectPages/RX8/torquespecs/) or the [list of all projects](/ProjectPages/).
