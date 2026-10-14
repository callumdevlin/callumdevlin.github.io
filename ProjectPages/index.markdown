---
title: Projects
permalink: /ProjectPages/
type: index
toc: false
description: >
  Engineering projects, two technical notebooks and the interactive labs, with
  what was built, what was analysed and what was only designed kept distinct.
---

A mix of university, industry and personal work. Each project page covers the problem, the decisions behind the design and what was built and tested, and says plainly where the evidence stops.

## Engineering projects

<ul class="cards">
<li>{% include card.html href="/ProjectPages/EnduraOMP/" kicker="MEng individual project" title="EnduraOMP: controlled lubrication for rotary engines" text="An electronically controlled oil metering pump with its own tank and gauge, designed from logged data on a running 13B-MSP and built as a machined, bench-tested prototype." img="/Images/enduraomp-engine-1.webp" alt="CAD render of the EnduraOMP pump mounted on a Mazda 13B-MSP engine" %}</li>
<li>{% include card.html href="/ProjectPages/E1/" kicker="Industrial group project" title="MP1: breathing-apparatus stowage" text="A push-to-stow cradle for fire-appliance crew cabs, designed with Emergency One. An adjustable mechanism for single and twin-pack cylinders, checked with FEA against a 10 g requirement but not crash-tested." img="/Images/BA_Stowage_20.png" alt="Render of the MP1 stowage cradle holding a breathing-apparatus cylinder" contain=true %}</li>
<li>{% include card.html href="/ProjectPages/rfidtoolstorage/" kicker="BEng project" title="ToolSync: a toolbox that knows what is in it" text="RFID check-in and check-out, BLE tags that can flash and beep to find a missing tool, and a Raspberry Pi touchscreen." %}</li>
</ul>

## Notebooks

<ul class="cards">
<li>{% include card.html href="/ProjectPages/RX8/" kicker="Reference" title="Mazda RX-8 workshop notebook" text="Specifications, procedures, measured engine data and a guide to the factory oil metering pump for a Series 1 car. Mazda's figures, my measurements and open questions are kept apart." img="/Images/RX8-JackPoints.jpg" alt="Underside diagram of the RX-8 showing jack and support points" contain=true %}</li>
<li>{% include card.html href="/ProjectPages/rlbot/" kicker="Maths and code" title="Rocket League bot notes" text="The vectors, ground and aerial motion, steering and shot alignment behind a hard-coded Python bot, with worked examples and tests." img="/Images/rlbot-hero.jpg" alt="A Rocket League match with the bot's debug lines drawn in-game" %}</li>
</ul>

## Interactive labs

Small in-browser tools. They run locally and nothing is uploaded or stored.

<ul class="cards">
<li>{% include card.html href="/ProjectPages/RX8/OMP/lab/" kicker="Interactive lab" title="RX-8 OMP Lab" text="The stock Series 1 oil metering pump in action: how speed, load and coolant temperature set the commanded step, and how the start-up checks, switch faults and a jammed mechanism play out." %}</li>
<li>{% include card.html href="/ProjectPages/RX8/acceleration-lab/" kicker="Interactive lab" title="RX-8 Acceleration Lab" text="Gearing, road speed and full-throttle acceleration for the 231 PS six-speed and 192 PS five-speed RX-8, with shift-strategy comparison and replay." %}</li>
</ul>
