---
title: RX-8 OMP Removal, Installation & Servicing
permalink: /ProjectPages/RX8/OMP/servicing/
description: >
  Removing and refitting the Series 1 RX-8 oil metering pump: Mazda's
  procedure, owner tips, the rebuild-or-replace decision, the position-switch
  setting and what to check at first start.
---

Mazda's removal and installation procedure is short, and it leaves out several things you will want: **torque values, priming, and how the position switch is set**. This page gives Mazda's steps first, then what owners add. Anything that comes from owners rather than Mazda is marked as such.

> **Diagnose first.** Many suspected pump failures turn out to be the connector, the wiring, water at the pump or the position switch. Work through [diagnostics & testing](/ProjectPages/RX8/OMP/testing/) before you spend money.
{:.note}

> **Caution:** the OMP is part of the engine's lubrication chain, so mistakes here can cost an engine. If any of this is outside your comfort zone, hand it to a rotary specialist.
{:.note}

## Before you start

| | |
| :--- | :--- |
| **Engine** | Cold. Mazda says to remove and install all the parts when the engine is cold. |
| **Battery** | Negative cable disconnected (this is part of Mazda's procedure). |
| **Tools** | Metric sockets and spanners, a torque wrench that is accurate at low values, line spanners for the unions, a pick set, lint-free rags, a parts tray, masking tape and a pen for labels. A hand vacuum pump is handy for checking the nozzles. |
| **Parts** | A new **flange O-ring** and a new **sealing washer on each banjo or connector bolt** you disturb. Fresh engine oil. Optionally, new nozzle washers. |
| **Time** | Owners report one to two hours. |

Part numbers for the O-ring and washers vary by supplier, so ask your parts supplier to match them to your car.

## Removal

**Mazda's procedure:**

1. Remove the engine cover and the battery cover.
2. Disconnect the negative battery cable.
3. Remove the battery, the battery box and the battery tray.
4. Remove, in this order: **connectors, washer, oil pipe (pump side), gasket, metering oil pump, O-ring.**

**What owners add:**

- Access is from the battery area and the passenger side. The pump is held by **three bolts** (reports say one 10 mm bolt on top and two underneath). Oil will spill.
- **Label each oil pipe** before you disturb it, so it goes back to the same port, and cap or tape every open connection straight away. A single fibre in the small drillings is a blockage.
- The **banjo bolts are hollow and snap easily**. Don't force them.
- Mark which pipe goes where, and note the pump's position as it comes out: the drive worm engages a gear in the front cover, so withdraw the pump square-on without prising it sideways.

## Inspect it

- **Connector and pins:** corrosion, backed-out pins, chafed wires. Water at the connector is a common finding.
- **Hose above the pump:** a weeping hose or pipe above the pump can drip onto it.
- **Drive worm:** it should turn freely by hand. Owners report this is normal.
- **Body and mating face:** cracks around the ears and unions; clean the front-cover face with no gasket fragments or scoring.
- **Pipes:** old pipes go **brittle and shrink with heat**. Owners report factory lines lasting around 100,000 miles, and one found shrunken lines with almost no flow on a vacuum test ([thread](https://www.rx8club.com/australia-new-zealand-forum-37/oil-metering-lines-beware-217377/)). Replace any that are hard or cracked.
- **Stepper and switch:** with the pump out, repeat the [coil and switch resistance checks](/ProjectPages/RX8/OMP/testing/#electrical-checks-and-mazdas-figures) (30.6 to 35.6 Ω per winding pair, and 400 Ω or less across the switch).

## Rebuild or replace?

Mazda supplies the pump as a **complete assembly**, and its manual's remedy for a bad stepper or switch is to replace the pump. I found no RX-8 internal rebuild kit. What can realistically be done:

- **Reseal it.** The flange O-ring and the banjo washers are sold separately, and leaks traced to the pump are usually the flange seal or the crush washers, not the body.
- **Clean and free it.** Some owners have opened pumps that were corroded or stiff, cleaned them and got them working again. It needs care and a note of how everything is timed together.
- **Replace it.** If the coils or switch are out of range, or the pump is stuck, replacement is the sensible route. A genuine new unit costs several hundred pounds. Used units are far cheaper, but owners report some arrive **mis-set** or with a worn switch, and some fail again soon after. Test the coils and the switch, and check the setting, before one goes near your engine.
- **The switch can't be bought on its own,** according to owners, so a bad switch means a new or used pump.

## Installation

Install in the reverse order of removal, with these notes:

1. Fit a **new O-ring and gasket**, lightly oiled.
2. Offer the pump up square and let the drive engage. It should seat without force; if it stands proud, the drive isn't engaged, so don't pull it down with the bolts.
3. **Torque:** Mazda's removal and installation page gives no torque values. Use the figures in the full workshop manual for your car, and keep the low values on the banjo and connector bolts low.
4. Reconnect each labelled pipe with **new washers**, then the connectors, then the battery and its fittings.

### Position switch setting

Mazda gives no procedure for setting the position switch, because it doesn't expect you to disturb it. Owners report that Mazda won't adjust it for that reason. The switch is held on the pump by two screws with slotted holes, giving a small range of adjustment (an owner measured about 30 degrees of travel in one direction), and a pump whose switch is set wrongly sets a code and goes into fail-safe. It matters if the switch has been removed or knocked, or if you fit a used pump.

What owners and RX8Club moderators do (this is **not** Mazda's procedure):

- **Switch still fitted:** loosen the two screws, nudge the switch a small amount, reset the PCM and see whether the code clears. If not, try the other direction. ([Thread](https://www.rx8club.com/series-i-trouble-shooting-95/need-help-resetting-oil-metering-pump-262411/).)
- **Switch removed, or starting from scratch:** a moderator's method is to check the connections first, then remove the switch and turn the pump's shaft **clockwise until it stops**, refit the switch, then turn it slightly **counter-clockwise until the slack is taken up** (about the middle of its adjustment range), reset the PCM and test. ([Thread](https://www.rx8club.com/series-i-trouble-shooting-95/omp-issues-245126/).) One owner in that thread tried it, didn't get it to work and fitted a new pump instead, so don't expect it to be a sure fix.

A wrongly set switch gives a code and fail-safe; I found no report of engine damage from it, and the switch looks like a check rather than a control. If a code returns within seconds of starting, the fault is real and still there.

## Priming, first start and checks

Mazda's installation step is: **start the engine, check for oil leaks at the areas you worked on, and check the engine oil level.** It gives no priming or bleeding procedure. These steps are my practice and owner advice:

1. **Prime the circuit.** Fill the metering lines with fresh oil as far as is practical when you connect them, so the pump doesn't start dry.
2. **Premix for the first tank.** Owners suggest adding two-stroke oil to the first tank of fuel as a margin while the circuit fills. There is more on premix on the [nozzles & premix page](/ProjectPages/RX8/OMP/nozzles-premix/).
3. **First start.** Start the engine and let it idle with no load. The PCM runs its **initial set** (reverse 60 steps to find zero) at every start. Because you disconnected the battery, it will also run its **position check** once the battery is connected, which is expected.
4. **Check for leaks** at every union and the pump flange, cold and again after warm-up.
5. **Verify control.** No codes should be set. With a scan tool, watch MOP_POS rise with engine speed ([expected values here](/ProjectPages/RX8/enginedata/)). Mazda's [PCM terminal 2N check](/ProjectPages/RX8/OMP/testing/#switch-check-at-the-pcm) is a quick electrical test of the switch circuit.
6. **Check the oil level and watch consumption** over the following weeks. Consumption is the end-to-end proof that the system is delivering, because the PCM can't detect a lack of flow.

## Sources

- Mazda workshop manual: [OMP removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W01.html), [oil nozzle removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W02.html), [OMP inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W03.html).
- RX8Club owner threads linked above.

*Next: [oil nozzles, premix and clean oil feed systems](/ProjectPages/RX8/OMP/nozzles-premix/).*
