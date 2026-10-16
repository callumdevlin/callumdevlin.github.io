---
title: RX-8 Oil Nozzles, Premix & Clean Oil Feed
crumb: Nozzles, premix and clean oil
permalink: /ProjectPages/RX8/OMP/nozzles-premix/
section: omp
nav_order: 4
applies: Series 1 RX-8 (2003-2008). Mazda's figures are from the 2003 manual; premix and clean-oil figures are owner and vendor reports.
reviewed: 2026-10-14
description: >
  The Series 1 RX-8 oil nozzles and their air hose, Mazda's test, how much premix to run
  in different situations and which oils owners use, and clean oil feed conversions.
---

Metered oil only protects the engine if the pipes, nozzles and the oil itself are right. Mazda's figures are marked as Mazda's; everything else is owner or specialist experience.

- Each rotor has two nozzles, each with a one-way check valve and an air connection. A failed or blocked nozzle sets no code.
- Mazda's nozzle test is a vacuum hold: at least 66.5 kPa applied, and a drop of 2.66 kPa or more in a minute means replace it.
- Mazda neither recommends nor forbids premix. Premix supplements the OMP; it doesn't repair it.
- A clean oil feed gives better oil chemistry but a tank you must watch yourself: nothing warns you when it runs empty.

## Oil nozzles

The Series 1 Renesis has two nozzles per rotor, tilted towards the side housing so oil is injected directly onto it. That helps lubricate the side housing and side seals, which matters because the Renesis breathes through side exhaust ports.

### The air hose and check valve

Each nozzle has a check valve and a small air hose. Per [Mazda's construction page](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html), the nozzle gets barometric pressure through the hose so engine vacuum can't act on the oil inlet, and the check valve stops oil flowing back towards the hose under positive pressure.

Engine Builder magazine (2011) reported a Mazda bulletin about a 2009-style air intake hose supplied by mistake on some 2004-2008 cars (from 8 January 2008). It blocks the barometric feed, so engine vacuum draws in more oil than the pump meters and consumption rises. The correct hose was given as N3H1-13-221E. The date and part number come from a second-hand summary, so confirm the part with a dealer. If a car uses far more oil than expected, check which air intake hose is fitted.

### Testing a nozzle

Mazda's test, nozzle removed:

1. Apply a vacuum of 66.5 kPa (0.68 kgf/cm², 9.65 psi) or more to port A with a vacuum pump.
2. It must hold. A drop of 2.66 kPa (0.027 kgf/cm², 0.39 psi) or more in one minute means replace the nozzle.

Also check the oil pipes, nozzles and the pump's connector bolts for clogging, and look for leaks at the pump-to-cover face and pipe connections with the engine idling. None of this sets a code: the PCM has no flow sensing, so it keeps pushing oil at a dead end. Owners who vacuum-tested their nozzles report several failing, sometimes all four ([example thread](https://www.rx8club.com/series-i-tech-garage-22/leaking-oil-injectors-234791/)), so test whenever you have access.

Don't drill nozzles or bolts to clear them: the orifice size is part of the metering. Mazda's remedy for a failed nozzle is to replace it. If you clean a part, vacuum-test it again; owners warn that compressed air can force a check valve open, and some advise against solvents.
{:.note}

### Removing a nozzle

Mazda's procedure, engine cold: remove the engine cover, battery cover, negative cable, battery, battery box and tray, and the upper and lower extension manifold. Then remove in order: air hose, oil nozzle, washer, oil pipe (housing side), washer. Install in reverse, start the engine, check for leaks and check the oil level. Mazda gives no torque values on that page ([oil nozzle removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W02.html)).

### Pipes

The pipes and connector bolts have small internal drillings that can varnish up, and old pipes go brittle and shrink with heat. Owners report factory pipes lasting around 100,000 miles. Check them whenever access is open; see the [diagnostics page](/ProjectPages/RX8/OMP/testing/).

## Premix

"Premix" means adding two-stroke oil to the fuel so a little lubricant arrives with the charge. Mazda neither recommends nor forbids it. Everything on dose and brand below is vendor or community guidance, not Mazda data.

### How much to premix

Starting doses by scenario. The OMP keeps metering oil whatever you add, so more isn't better: too much fouls plugs and wastes oil.

| Scenario | US fl oz per US gal | Per 10 L of fuel | Per full 61 L tank | Where it comes from |
| :--- | :---: | :---: | :---: | :--- |
| Daily driver, naturally aspirated petrol, OMP working | 0.25-0.5 | 20-39 mL | 119-238 mL | Bio-Rotary vendor range. Idemitsu gives 0.5, Rotary Performance works out about 0.4 (4 oz per 10 gal), and the UK club starts at 125 mL a tank |
| Lightest use, OMP working | 0.16-0.21 (1:800-1:600) | 13-17 mL | 76-102 mL | One 2004 RX8Club poster; the stock OMP already supplies oil |
| Hard road driving or track day, petrol | 0.5-1 | 39-78 mL | 238-477 mL | Bio-Rotary vendor (track use). The UK club says up to 300 mL a tank (about 0.63) |
| Modified or boosted engine | 0.5-1 | 39-78 mL | 238-477 mL | Bio-Rotary vendor. A retailer note on Idemitsu mentions about 2 for boosted; that isn't on the maker's page |
| Alcohol fuel (E85, methanol) | 0.5-1 | 39-78 mL | 238-477 mL | Bio-Rotary vendor. Idemitsu's page says its premix is for gasoline engines only |
| OMP failed, disabled or removed | about 1 | 78 mL | 477 mL | A retailer note on Idemitsu. With the stock PCM an unplugged OMP gives fail-safe (owner reports), so this is for aftermarket-ECU builds or a get-home measure |

Notes on the table:

- **Aftermarket apex seals:** Bio-Rotary says it is "ok to up the mix ratio" and gives no figure.
- **First tank after a pump service or Sohn fit:** owners premix it as a margin while the circuit fills. Use the daily-driver row.
- **Race development:** Racing Beat reported 10 oz of Royal Purple two-stroke oil in 6 US gallons (about 1.7 oz per gal, 1:77) and a 1.7 hp average gain, with more plug fouling. A race note from a reprint, not road advice.
- **Maths:** 1 US fl oz = 29.5735 mL and 1 US gal = 3.78541 L, so 1 oz per gal is 7.8 mL per litre (about 1:128). Work from the litres you actually add, don't mix up US and imperial gallons, and expect bottle charts using 1 oz = 30 mL to differ by a few per cent.

### Premix oils the community uses

Choose a two-stroke oil rated JASO FC or FD (or ISO-L-EGD) and sold as safe to premix with petrol, not just for direct injection. Several brands claim FC or FD without a JASO certification mark. Traditional engine oil separates in the tank, and lawn-equipment two-stroke oils can contain dye that stains plastic parts. Most threads below are from 2004-2017 and are anecdotal.

| Oil | Pros | Cons |
| :--- | :--- | :--- |
| **Idemitsu Full Synthetic Rotary Engine Pre-Mix** (2206-042A) | Rotary-specific and the oil forums name most often. Maker's dose is 0.5 oz per gal, which owners round to about 8 oz a tank. Around $8 a bottle at Atkins | Hard to buy outside the US: Atkins doesn't ship abroad, and owners in Canada and Italy report it hard to find. Owners dispute its FC rating (the maker's sheet says it exceeds FC, but it isn't on the JASO list). Gasoline engines only |
| **Renewable Lubricants Bio-Rotary Racing Premix** (the one I use) | Rotary-specific, with doses for petrol, alcohol and track use. Vendor claims little smoke or smell and cleaner plugs | Those are vendor claims; it didn't turn up in the owner threads I read. About $29 a quart at Mazdatrix. The vendor describes fuel dosing only, not a reservoir |
| **Amsoil Saber Professional** | Full synthetic, low-smoke, and the alternative to Idemitsu that RX8Club posts name most often. Described by owners as catalyst-friendly and flexible on a catless car. Amsoil says it works up to 100:1 | Needs thorough mixing to disperse (one owner). Amsoil's own material covers small engines, not rotaries, and a forum post says neither Amsoil nor Idemitsu endorses it for the car (unverified) |
| **Motul 710 2T** | Ester synthetic, JASO FD and ISO-L-EGD, made for premix and oil injection. Motul says it is catalytic-converter and ethanol compatible. Named in the UK club guide; one RX8Club owner uses 6 oz a tank | Motul's own ratio is 25:1-50:1, far richer than rotary doses, so ignore it. About £22 a litre at one UK retailer (check the live price) |
| **Lucas 2-cycle (semi-synthetic)** | Cheap and easy to buy. Several RX8Club owners (2017) use about 6 oz a tank | Claims FC but owners found it isn't on the JASO list. Owners' advice is mostly "don't overthink it" |
| **Royal Purple 2-cycle** | Used by Racing Beat in race development. Some owners rate it | Expensive in quantity, and other owners call it marketing. Opinions are mixed |
| **Castrol TC-W3 (outboard)** | Cheap and ashless. Early adopters (2004) reported smoother idle | Outboard oil to the TC-W3 standard, not JASO. One poster calls it a weaker lubricant than JASO FC or ISO oils, and the original poster later stopped using it |

Also named in the UK club guide: Castrol Power 1 Racing 2T and Protek R. I found nothing more on either.

### What Mazda says

The 2004 US owner's manual ([Print 6, January 2004](https://www.mazdausa.com/siteassets/pdf/owners-optimized/2004/rx8/2004-rx-8-owners-manual.pdf)) says the engine "consumes a small amount of engine oil due to its structural design", that consumption "depends on engine speed and engine load" and is higher in extreme driving, and that you should check the oil level at every second fill-up. It gives no figure for normal consumption and says never to add fuel-system additives, but doesn't mention two-stroke oil. No Mazda document I've seen recommends or forbids premix, and I know of no source for the claim that it voids the warranty.

An owner quoted a 2004 Mazda Customer Assistance reply ([thread](https://www.rx8club.com/rx-8-discussion-3/sucks-mazda-says-1-qt-oil-consumed-600-miles-43191/)) calling 1 quart per 600 miles normal under warranty. It is one pasted email and unverified, and another print of the 2004 manual has a shorter oil note without the "second fill-up" sentence. Typical owner reports are far lower, roughly 1 quart per 1,500-3,000 miles, with hard use much higher. Anecdotes, not specifications.

### For and against

| In favour | Against |
| :--- | :--- |
| Adds lubrication through the intake charge, reaching the apex seal path | Oil in the fuel fouls plugs more easily |
| A margin if the OMP under-delivers | Some owners stop premixing before emissions tests; the catalyst effect is anecdotal |
| Purpose-made two-stroke oil is formulated to burn cleanly | A fixed ratio is too much oil for most driving, and it can't reach the engine on a closed-throttle lift-off, when fuel is cut |

There is no measured data on catalyst or oxygen-sensor effects, only owner anecdotes. The UK club guide also notes premix can marginally lower the petrol's octane, so consider premium unleaded.

Premix doesn't:

- **Target the oil.** The nozzles inject towards the side housings; premix arrives with the charge. They complement each other.
- **Repair a failed OMP or clear a code.** Fail-safe stays active and the controlled metering is still gone. Running on premix alone with a dead pump is a risk decision, not a fix.
- **Replace the OMP.** Unplugging or deleting it with the stock PCM gives fail-safe in owner reports, so they don't recommend it on a road car. (One owner said the car ran normally with the pump removed but its connectors plugged in, so the unplugged connector seems to be the trigger.) Race builds that remove it use an aftermarket ECU and treat premix as the oil supply.

I use Bio-Rotary in the reservoir as well as the fuel; see the [Sohn adapter page](/ProjectPages/RX8/sohn-adapter/#bio-rotary-oil-and-premix). Measure the fuel actually added and record the dose.

## Clean oil feed (Sohn-style adapters)

The stock system meters sump oil, so whatever crankcase oil you run gets burned. Crankcase oils carry metallic detergent and anti-wear additives that leave sulphated ash.

A clean oil feed conversion (the Sohn adapter is the best known) closes the sump-oil feed and gives the OMP a hose connection to a separate two-stroke oil reservoir. The stock pump, control and nozzles work as designed; only the oil changes. Series 1 only. The fitted system here is my [custom Sohn adapter](/ProjectPages/RX8/sohn-adapter/).

**Benefits**

- The engine burns oil formulated for total-loss use, which reduces ash deposits.
- Sump oil is only a bearing lubricant, so its grade needn't be a compromise.
- Owners disagree on how much difference it makes, and there is no controlled data.

**Trade-offs**

- **You are the low-oil warning.** The stock system can't run dry because the sump feeds it. With a separate tank, empty means no injection oil and no warning: the PCM still sees a pump moving normally and sets no code.
- **Priming and air.** The line must be primed and air can take a while to clear. Many owners premix the first tank.
- **Hose and fittings.** Soft tubing has hardened and cracked in service. Use oil- and heat-resistant hose with retained fittings, route it clear of chafe and air traps, and vent the tank with a filtered breather. More fittings mean more places to leak or let air in.
- **Check the sump level.** One owner saw a rising, fuel-smelling sump level after fitting an adapter; replies pointed to fuel dilution rather than the added oil. Watch for it without assuming the cause.

This trade-off, better oil in exchange for owning the tank, is what my MEng project explored: [EnduraOMP](/ProjectPages/EnduraOMP/) pairs a clean-oil reservoir with electronic metering, level sensing and a driver-visible gauge.

## Maintenance after any change

- Check oil (or reservoir) consumption regularly. It is the only whole-system proof of delivery.
- Vacuum-test the nozzles and inspect unions at service intervals.
- Keep premix dosing consistent if you rely on it.
- After any line work, prime and leak-check as after [pump servicing](/ProjectPages/RX8/OMP/servicing/).

## Sources

- Mazda workshop manual: [OMP construction](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011101008T07.html), [OMP inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W03.html), [oil nozzle removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011114100W02.html).
- [Engine Builder magazine: air intake hose bulletin](https://www.enginebuildermag.com/2011/06/high-oil-consumption-due-to-wrong-air-intake-hose-on-some-mazda-rx-8-engines/) (summary only).
- Mazda USA, [2004 RX-8 owner's manual](https://www.mazdausa.com/siteassets/pdf/owners-optimized/2004/rx8/2004-rx-8-owners-manual.pdf) (Print 6, January 2004), for the oil-consumption and fuel-additive wording.
- Racing Beat's oil-injection note, as [reprinted in 2011](https://mickaircraft.com/ACRE/ACRE201104/messages/20110405-RX-8%20Oil%20injection%20questions%20and%20thoughts-7823124.html).
- UK RX-8 Owners Club, [Oil 101 for newbies](https://www.rx8ownersclub.co.uk/forum/viewtopic.php?t=50814); [RX8 Help premix page](http://www.rx8help.com/premix.html).
- RX8Club threads, read 16 October 2026: [Gas/Oil Premix thread](https://www.rx8club.com/series-i-tech-garage-22/gas-oil-premix-thread-99636/), [Best premix combination](https://www.rx8club.com/series-i-tech-garage-22/best-premix-combination-need-advice-265337/), [Non-synthetic or synthetic 2-stroke oil?](https://www.rx8club.com/series-i-tech-garage-22/non-synthetic-synthetic-2-stroke-oil-133558/) and [Best engine oil and premix](https://www.rx8club.com/series-i-tech-garage-22/best-engine-oil-premix-rx8-rotor-engine-142534/); NoPistons, [Best oil for rotary running premix](https://www.nopistons.com/performance-mods-20/best-oil-rotary-running-premix-37997/).
- Dose and product pages: [Idemitsu Rotary Pre-Mix at Atkins Rotary](https://www.atkinsrotary.com/Oil-Lube-Sealing-Compound-Etc/Pre-Mix/Idemitsu-Full-Synthetic-Rotary-Engine-Pre-Mix-2206-042A.html), [Bio-Rotary at Mazdatrix](https://mazdatrix.com/product/renewable-lubricants-bio-rotary-racing-premix/), [Amsoil Saber Professional](https://www.amsoil.com/shop/by-product/motor-oil/2-stroke/saber-professional-synthetic-2-stroke-oil/), [Motul 710 2T](https://motul.com/en-AE/products/16400), a [retailer listing for the Idemitsu premix](https://www.desertcart.ma/products/115466870) (the no-pump and boosted notes) and Jalopnik, [Do rotary engines need premixed fuel?](https://jalopnik.com/1976617/do-rotary-engines-need-premixed-fuel/) (Rotary Performance's 4 oz per 10 gal).
- RX8Club threads on [Sohn adapters](https://www.rx8club.com/series-i-tech-garage-22/richard-sohn-omp-mop-adapter-102271/) and [removing the OMP](https://www.rx8club.com/series-i-tech-garage-22/oil-metering-pump-elimination-223879/).
