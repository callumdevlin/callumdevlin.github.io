---
title: RX-8 OMP Removal, Installation & Servicing
crumb: OMP servicing
permalink: /ProjectPages/RX8/OMP/servicing/
section: omp
nav_order: 3
applies: Series 1 RX-8 (2003-2008) factory OMP. Mazda's steps are from the 2003 manual; owner advice is marked as such.
reviewed: 2026-10-14
description: >
  Removing and refitting the Series 1 RX-8 oil metering pump: Mazda's procedure, owner
  tips, rebuild or replace, the position-switch setting and first-start checks.
---

Mazda's procedure is short and leaves out torque values, priming and how the position switch is set. This page gives Mazda's steps first, then owner additions, marked as such. Many suspected pump failures turn out to be the connector, wiring, water or the switch, so do the [diagnostics](/ProjectPages/RX8/OMP/testing/) first.

The OMP is part of the engine's lubrication chain, so mistakes here can cost an engine. If any of this is outside your comfort zone, hand it to a rotary specialist.
{:.note}

## Before you start

| | |
| :--- | :--- |
| Engine | Cold (Mazda's requirement). |
| Battery | Negative cable disconnected (part of Mazda's procedure). |
| Tools | Metric sockets and spanners, a torque wrench accurate at low values, line spanners for the unions, picks, lint-free rags, a parts tray, tape and a pen for labels. A hand vacuum pump helps for the nozzles. |
| Parts | New flange O-ring and a new sealing washer for each banjo or connector bolt you disturb; fresh engine oil; optionally new nozzle washers. Part numbers vary by supplier, so have yours matched to the car. |
| Time | Owners report one to two hours. |

## Removal

Mazda's procedure:

1. Remove the engine cover and battery cover.
2. Disconnect the negative battery cable.
3. Remove the battery, battery box and battery tray.
4. Remove, in order: connectors, washer, oil pipe (pump side), gasket, metering oil pump, O-ring.

Owners add:

- Access is from the battery area and the passenger side. Three bolts hold the pump (reports say one on top, reached from above, and two underneath). Oil will spill.
- Label each oil pipe so it goes back to the same port, and cap every open connection at once. A single fibre in the small drillings is a blockage.
- The banjo bolts are hollow and snap easily. Don't force them.
- The drive worm engages a gear in the front cover, so withdraw the pump square-on without prising it sideways, and note its position as it comes out.

## Inspect it

- **Connector and pins:** corrosion, backed-out pins, chafed wires. Water at the connector is a common finding.
- **Hose above the pump:** a weeping hose or pipe can drip onto it.
- **Drive worm:** should turn freely by hand (owners say this is normal).
- **Body and mating face:** cracks around the ears and unions; front-cover face clean, with no gasket fragments or scoring.
- **Pipes:** old pipes go brittle and shrink with heat. Owners disagree on life: about 100,000 miles by one account, shrunken lines at about 65,000 by another, and one overheated car's lines gave almost no flow on a vacuum test ([thread](https://www.rx8club.com/australia-new-zealand-forum-37/oil-metering-lines-beware-217377/)). Replace any that are hard or cracked.
- **Stepper and switch:** repeat the [coil and switch resistance checks](/ProjectPages/RX8/OMP/testing/#electrical-checks-and-mazdas-figures) (30.6-35.6 Ω per winding pair, 400 Ω or less across the switch).

## Rebuild or replace?

Mazda supplies the pump complete, and its remedy for a bad stepper or switch is to replace the pump. I found no RX-8 internal rebuild kit. Realistically:

- **Reseal:** the flange O-ring and banjo washers are sold separately, and pump leaks are usually the flange seal or crush washers, not the body.
- **Clean and free:** some owners opened corroded or stiff pumps, cleaned them and got them working. It needs care and a note of how everything is timed together.
- **Replace:** if the coils or switch are out of range or the pump is stuck. A new genuine unit costs several hundred pounds. Used units are far cheaper, but owners report some arriving mis-set or with a worn switch, and some failing again soon. Test the coils and switch and check the setting before one goes near your engine.

The switch is part of the pump; Mazda's remedy for a bad switch is a new pump.

## Installation

Reverse of removal, with these notes:

1. Fit a new O-ring and gasket, lightly oiled.
2. Offer the pump up square and let the drive engage. It should seat without force. If it stands proud, the drive isn't engaged, so don't pull it down with the bolts.
3. Mazda's page gives no torque values. Use the figures in the full workshop manual, and keep the banjo and connector bolts low.
4. Reconnect each labelled pipe with new washers, then the connectors, then the battery and its fittings.

### Position switch setting

Mazda gives no setting procedure because it doesn't expect you to disturb the switch, and owners report Mazda won't adjust it. Two screws in slotted holes give a small range (one owner estimated about 30° of travel; others in the thread said 10-19°), and a wrongly set switch sets a code and fail-safe. It matters if the switch was removed or knocked, or if you fit a used pump.

What owners and an RX8Club moderator do (not Mazda's procedure):

- **Switch still fitted:** loosen the two screws, nudge the switch a little, reset the PCM and see if the code clears; if not, try the other way. Relayed second-hand and offered tentatively ([thread](https://www.rx8club.com/series-i-trouble-shooting-95/need-help-resetting-oil-metering-pump-262411/)).
- **Switch removed, or starting fresh:** the moderator's method is to check the connections, remove the switch, turn the pump's shaft clockwise until it stops, refit the switch, then turn it slightly anticlockwise until the slack is taken up (about mid-range), reset the PCM and test ([thread](https://www.rx8club.com/series-i-trouble-shooting-95/omp-issues-245126/)). One owner there tried this, it didn't work, and he fitted a new pump, so it isn't a sure fix.

A wrongly set switch gives a code and fail-safe, and I know of no report of engine damage from it; the switch looks like a check rather than a control. If a code returns within seconds of starting, the fault is real.

## Priming, first start and checks

Mazda's installation step is to start the engine, check for oil leaks where you worked and check the engine oil level. It gives no priming or bleeding procedure; these steps are my practice and owner advice:

1. **Prime:** fill the metering lines with fresh oil as far as practical when you connect them, so the pump doesn't start dry.
2. **Premix the first tank:** owners add two-stroke oil to the first tank as a margin while the circuit fills. See the [nozzles and premix page](/ProjectPages/RX8/OMP/nozzles-premix/).
3. **First start:** let it idle with no load. The PCM runs its initial set (reverse 60 steps to find zero) at every start; Mazda lists battery connection as a condition for the position check, so expect it after a battery disconnect.
4. **Leaks:** check every union and the pump flange, cold and again after warm-up.
5. **Control:** no codes should be set. With a scan tool, MOP_POS should rise with engine speed; a constant 7 is Mazda's fail-safe step. The [PCM terminal 2N check](/ProjectPages/RX8/OMP/testing/#switch-check-at-the-pcm) is a quick electrical test of the switch circuit.
6. **Consumption:** check the oil level and watch consumption over the following weeks. It is the end-to-end proof of delivery, because the PCM can't detect a lack of flow.

## Sources

- Mazda workshop manual: [OMP removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W01.html), [oil nozzle removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W02.html), [OMP inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W03.html).
- RX8Club owner threads linked above.
