---
title: RX-8 Oil Nozzles, Premix & Clean Oil Feed
crumb: Nozzles, premix and clean oil
permalink: /ProjectPages/RX8/OMP/nozzles-premix/
type: reference
section: omp
nav_order: 4
applies: Series 1 RX-8 (2003-2008). Mazda's figures are from the 2003 manual; premix and clean-oil figures are owner and vendor reports.
reviewed: 2026-10-14
description: >
  The system around the Series 1 RX-8 OMP: how the oil nozzles and their air
  hose work, Mazda's test for them, what premix does and doesn't do, and clean
  oil feed conversions such as the Sohn adapter.
---

Metered oil only protects the engine if the pipes, nozzles and the oil itself are right. This page covers the delivery end of the system, then the two big aftermarket topics: premix and clean oil feed. Mazda's figures are marked as Mazda's; everything else is owner or specialist experience.

In brief:

- Each rotor has two nozzles, each with a one-way check valve and an air connection. A failed or blocked nozzle sets no code.
- Mazda's nozzle test is a vacuum hold test: at least 66.5 kPa applied, and a drop of 2.66 kPa or more in a minute means replace it.
- Mazda doesn't recommend or forbid premix. Premix supplements the OMP; it doesn't repair it.
- A clean oil feed trades better oil chemistry for a tank you must watch yourself: nothing warns you when it runs empty.

## Oil nozzles

The Series 1 Renesis has two oil nozzles per rotor. Mazda says they are tilted towards the side housing so oil is injected directly onto it, which improves lubrication of the side housing and side seals, important because the Renesis breathes through side exhaust ports.

### The air hose and check valve

Each nozzle has a one-way check valve and a small air hose. Per [Mazda's construction page](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html), the nozzle receives barometric pressure through the air hose so that engine vacuum can't be applied to the oil inlet, and the check valve stops oil flowing back towards the air hose when the engine is under positive pressure.

That air feed matters. Engine Builder magazine (2011) reported a Mazda bulletin about a 2009-style air intake hose supplied by mistake for some 2004 to 2008 cars (from 8 January 2008). It blocks the barometric feed to the nozzle, so engine vacuum acts on the nozzle instead and more oil is drawn in than the pump meters, which raises oil consumption. The correct hose for those cars was given as N3H1-13-221E. The date and part number come from a second-hand summary of that article, so check the part and its current number with a dealer before relying on them. If a car uses far more oil than expected, check which air intake hose is fitted.

### Testing a nozzle

Mazda's test, with the nozzle removed:

1. Apply a vacuum of 66.5 kPa (0.68 kgf/cm², 9.65 psi) or more to port A with a vacuum pump.
2. It must hold. If it drops 2.66 kPa (0.027 kgf/cm², 0.39 psi) or more in one minute, replace the nozzle.

Also check the oil pipes, nozzles and the pump's connector bolts for clogging, and look for leaks at the pump-to-cover mating surface and the pipe connections with the engine idling. Nothing here sets a code: the PCM has no flow sensing, so the pump and PCM carry on happily pushing oil at a dead end.

Owners who vacuum-tested their nozzles report that several failed, sometimes all four, so the test is worth doing whenever you have access. ([Example thread](https://www.rx8club.com/series-i-tech-garage-22/leaking-oil-injectors-234791/).)

> Don't drill nozzles or bolts to clear them. The orifice size is part of the metering. Mazda's remedy for a nozzle that fails the vacuum test is to replace it. If you clean any part, test it under vacuum again afterwards: owners warn that compressed air can force a check valve open, and some advise against solvents.
{:.note}

### Removing a nozzle

Mazda's procedure: engine cold; remove the engine cover, battery cover, negative battery cable, battery, battery box and tray, and the upper and lower extension manifold. Then remove, in order: air hose, oil nozzle, washer, oil pipe (housing side), washer. Install in reverse, start the engine, check for leaks and check the oil level. Mazda gives no torque values on that page. ([Mazda: oil nozzle removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W02.html).)

### Pipes

The pipes and their connector bolts have small internal drillings that can varnish up. Old pipes also go brittle and shrink with heat; owners report the factory pipes lasting around 100,000 miles. Check them whenever access is open. Diagnostic checks are on the [diagnostics page](/ProjectPages/RX8/OMP/testing/).

## Premix

"Premix" means adding two-stroke oil to the fuel, so a little lubricant arrives with the fuel charge.

What Mazda says: the 2004 RX-8 owner's manual (US edition, [Print 6, January 2004](https://www.mazdausa.com/siteassets/pdf/owners-optimized/2004/rx8/2004-rx-8-owners-manual.pdf)) states that the engine "consumes a small amount of engine oil due to its structural design", that oil consumption "depends on engine speed and engine load" and is higher under extreme driving, and that Mazda recommends checking the oil level at every second fuel filling. It gives no figure for normal consumption. It also says never to add fuel-system additives, but it doesn't mention two-stroke oil, so it doesn't explicitly cover premix. No Mazda document I have seen recommends or forbids premix, and I know of no source for the common claim that premix voids the warranty.

An owner quoted a 2004 Mazda Customer Assistance reply ([thread](https://www.rx8club.com/rx-8-discussion-3/sucks-mazda-says-1-qt-oil-consumed-600-miles-43191/)) calling 1 quart per 600 miles the warranty's normal consumption; owners read that as a limit, not a typical figure. It is a single pasted email and unverified, and another print of the 2004 manual has a shorter oil note without the "second fuel filling" sentence. Typical owner reports are far lower, roughly 1 quart per 1,500 to 3,000 miles, with hard use much higher. Those are anecdotes, not specifications.

What owners and specialists report (community figures, not manufacturer guidance):

| Source | Quantity |
| :--- | :--- |
| Main RX8Club [premix thread](https://www.rx8club.com/series-i-tech-garage-22/gas-oil-premix-thread-99636/) | Typical posts run from about 1:160 to 1:800, and richer mixes also appear. One 2004 post suggests 1:600 to 1:800 if the OMP is still working, because a fixed ratio is more oil than most driving needs |
| UK RX-8 Owners Club [guide](https://www.rx8ownersclub.co.uk/forum/viewtopic.php?t=50814) | Start with 125 ml per full tank, up to 300 ml per tank for hard driving or track days. The thread gives no ratio or tank size; my conversion for a 61 L tank is about 1:490 and 1:200 |
| RX8 Help [premix page](http://www.rx8help.com/premix.html) | About 1 oz per 2 gallons, and some use 1 oz per 3 or 4. The page doesn't say US or imperial; in US units that is about 1:256, 1:384 and 1:512. Calculate from the fuel added, not the tank size |

Where these sources name an oil standard they lean towards a two-stroke oil to JASO FC or FD. The UK club names FC (good) and FD (best), and RX8 Help and the RX8Club opening post are doubtful about TC-W3 oils, though no single source says all of that. Racing Beat reported adding 10 oz of Royal Purple two-stroke oil to 6 US gallons of fuel during RX-8 race development. That is about 1:77, roughly three times the richest rate on the product I use, and it gained an average of 1.7 hp, with the cost of the oil and a greater tendency to foul plugs as the downsides. It is a race note from a reprint, not road advice, and the gain shouldn't be assumed at a leaner ratio.

This car uses Renewable Lubricants Bio-Rotary Racing Premix; the [Sohn-adapter and premix page](/ProjectPages/RX8/sohn-adapter/#bio-rotary-oil-and-premix) converts the product's published application range. If you premix, measure the fuel actually added and record the dose instead of relying on a nominal tank quantity.

| In favour | Against |
| :--- | :--- |
| Adds lubrication through the intake charge, reaching the apex seal path | Oil in the fuel fouls spark plugs more easily |
| A margin if the OMP under-delivers | Some owners stop premixing before emissions tests; the effect on the catalyst is anecdotal |
| Purpose-made two-stroke oil is formulated to burn cleanly | A fixed ratio is too much oil for most driving, and it can't reach the engine on a closed-throttle lift-off, when fuel is cut |

There is no measured data on catalyst or oxygen-sensor effects, only owner anecdotes.

What premix doesn't do:

- It isn't targeted. The OMP nozzles inject oil deliberately towards the side housings; premix arrives with the charge. They complement each other and aren't interchangeable.
- It doesn't repair a failed OMP or clear a code. The PCM's fail-safe stays active, and the controlled, condition-dependent metering is still gone. Running on premix alone with a dead metering system is a risk decision, not a fix.
- Deleting or unplugging the OMP with the stock PCM gives fail-safe in owner reports, so they don't recommend it on a road car. (One owner said the car ran normally with the pump removed but its connectors still plugged in, so the unplugged connector seems to be the trigger.) Race builds that remove it use an aftermarket ECU and treat premix as the oil supply, which is a different situation.

## Clean oil feed (Sohn-style adapters)

The stock system meters engine sump oil, so whatever crankcase oil you run is what gets burned. Crankcase oils carry metallic detergent and anti-wear additives that leave sulphated ash when burned.

A clean oil feed conversion (the Sohn adapter being the best known) sits between the engine and the OMP, closes the sump-oil feed and gives the pump a hose connection to a separate reservoir of two-stroke oil. The stock pump, control and nozzles keep working as designed; only the oil being metered changes. It is for Series 1 cars only. The fitted system here uses my [custom Sohn adapter](/ProjectPages/RX8/sohn-adapter/).

The benefits:

- The engine burns oil formulated for total-loss use, which reduces ash deposits.
- The sump oil is only a bearing lubricant, so its grade no longer has to be a compromise.
- Owners disagree about how much difference it makes, and there is no controlled data.

The trade-offs and obligations:

- You are the low-oil warning system. The stock system can't run the metering circuit dry, because the sump feeds it. With a separate tank, an empty tank means no injection oil at all and no warning: the PCM still sees a pump that moves normally and sets no code.
- Priming and air. The line must be primed, and air can take a while to clear. Many owners premix the first tank.
- Hose and fittings. Soft tubing has hardened and cracked in service. Use oil-resistant, heat-resistant hose with retained fittings, route it so it can't chafe or trap air, and vent the tank properly (a filtered breather).
- Check the sump level. One owner reported a rising, fuel-smelling sump level after fitting an adapter, and the replies pointed to fuel dilution rather than the added oil. Watch for it without assuming the cause.
- More fittings means more places to leak or let air in; inspect them as part of routine maintenance.

This trade-off, better oil chemistry in exchange for you carrying responsibility for the tank, is what my MEng project explored: [EnduraOMP](/ProjectPages/EnduraOMP/) combines a dedicated clean-oil reservoir with electronic metering, level sensing and a driver-visible gauge, so the system watches the tank instead of relying on the owner's memory.

## Maintenance after any change

- Check oil consumption (or reservoir consumption) regularly. It is the only whole-system proof of delivery.
- Vacuum-test the nozzles and inspect unions at service intervals.
- Keep premix discipline consistent if you rely on it.
- After any line work, prime and leak-check as you would after [pump servicing](/ProjectPages/RX8/OMP/servicing/).

## Sources

- Mazda workshop manual: [OMP construction](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html), [OMP inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W03.html), [oil nozzle removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W02.html).
- [Engine Builder magazine: air intake hose bulletin](https://www.enginebuildermag.com/2011/06/high-oil-consumption-due-to-wrong-air-intake-hose-on-some-mazda-rx-8-engines/) (summary only).
- Mazda USA, [2004 RX-8 owner's manual](https://www.mazdausa.com/siteassets/pdf/owners-optimized/2004/rx8/2004-rx-8-owners-manual.pdf) (Print 6, January 2004), for the oil-consumption and fuel-additive wording.
- Racing Beat's oil-injection note, as [reprinted in 2011](https://mickaircraft.com/ACRE/ACRE201104/messages/20110405-RX-8%20Oil%20injection%20questions%20and%20thoughts-7823124.html).
- UK RX-8 Owners Club, [Oil 101 for newbies](https://www.rx8ownersclub.co.uk/forum/viewtopic.php?t=50814); [RX8 Help premix page](http://www.rx8help.com/premix.html).
- RX8Club threads on [premix](https://www.rx8club.com/series-i-tech-garage-22/gas-oil-premix-thread-99636/), [Sohn adapters](https://www.rx8club.com/series-i-tech-garage-22/richard-sohn-omp-mop-adapter-102271/) and [removing the OMP](https://www.rx8club.com/series-i-tech-garage-22/oil-metering-pump-elimination-223879/).
