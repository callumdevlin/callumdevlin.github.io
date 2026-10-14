---
title: 13B-MSP Engine Removal and Rebuild Notes
crumb: Engine removal and rebuild
permalink: /ProjectPages/RX8/engine-removal-and-rebuild/
section: rx8
nav_order: 4
applies: 13B-MSP six-port (Series 1), Mazda engine "Type A" (all UK cars). Clearances and torques follow Mazda's October 2008 13B-MSP engine manual.
reviewed: 2026-10-14
description: >
  Top-lift removal, Renesis teardown, inspection, clearances, assembly, first start
  and running-in notes.
---

These notes follow Mazda's engine manual for the figures and the build order, and my own experience for the removal. Mazda's procedure takes the engine, gearbox and crossmember out downward as one unit; the top lift below is my own practice.

Mazda's engine manual divides the engine into "Type A" and "Type B". Type B is a 2009 model-year US-VIN engine with a second (upper) oil pan and a sealed oil pump. Everything else, including a 2005 UK car, is Type A, and the figures here are Type A.

## Before removal

I normally remove the engine alone through the top, leaving the Y16M-D gearbox in the car. Mazda gives no engine mass. The figures I could find range from about 112 kg for a bare engine without accessories or fluids up to about 138 kg, so I use roughly 120 kg as a planning figure only. If you are sizing a crane, leveller or straps, work to the top of that range, or weigh the engine. Check the crane's capacity at the boom's full working reach, not its retracted headline capacity, and use a load leveller. Put the engine stand beside or ahead of the car so the suspended engine does not have to travel across the workshop.

Before the engine goes on a stand, loosen the fasteners that need the flywheel lock or very high torque: the front pulley lockbolt (254-294 N·m) and the oil-pump sprocket nut. Do not loosen either without the proper holding tool. Leave the flywheel fitted until those are done, because the lock works through the flywheel's ring gear.

## Top-lift removal

{% include figure.html src="/Images/rx8-engine-lift.jpg" alt="A rotary engine hanging from a workshop crane on orange lifting straps beside a grey RX-8 with its bonnet open" caption="An engine coming out of an RX-8 through the top, hanging from a crane on lifting straps." class="fig-medium" %}

### Ordered disconnect checklist

1. Record radio/security settings if relevant, open the windows, remove the bonnet with an assistant, and disconnect the battery negative then positive terminals.
2. Remove the strut brace, engine cover, airbox, intake duct, airflow-meter connector and resonator/VFAD ducting needed for crane access.
3. Depressurise the fuel system. Drain engine oil and coolant; remove the radiator drain access panel. Recover refrigerant only if the A/C circuit genuinely must be opened.
4. Remove the radiator, electric fan/shroud assembly and upper joining hoses. Cap the transmission-cooler stubs only on an automatic car.
5. Disconnect and label the radiator hoses, the rear heater feed/return, expansion/degas hoses and both throttle-body coolant hoses. Tie them outside the lift path.
6. Disconnect the fuel feed quick connector at the rail, cap both sides, then disconnect the purge/EVAP and brake-booster/vacuum hoses.
7. Label the four coil leads **L/F, T/F, L/R, T/R** and unplug the coil pack. Disconnect the engine-earth straps.
8. Disconnect the engine harness at the chosen break points. Account for the throttle body, six injectors, four coils, eccentric-shaft sensor, ECT sensor, knock sensor, OMP stepper and position switch, oil-pressure switch, alternator and starter. Mazda's intake-air page also lists the AIR, SSV and VDI solenoids on every engine, plus the VFAD solenoid and APV motor on the high-power engine. Photograph clip and earth locations before releasing the loom.
9. Disconnect the secondary-air pipe/valve connections and remaining intake/vacuum brackets. Remove the upper and lower intake manifolds where clearance makes the top lift easier; cover every open port.
10. Unplug the oxygen-sensor wiring from its body-side clips. Unbolt the exhaust manifold/catalyst connection and its braces, then support the exhaust. Do not let it hang from the sensor wiring.
11. Unbolt the A/C compressor and tie it securely to the body without opening its hoses. Remove or tie aside any remaining belt-driven accessory and brackets that obstruct the lift. This car has electric power steering, not an engine-driven pump.
12. Disconnect the oil-cooler hoses at their engine-side joints and cap them immediately. Mazda describes a retaining clip with three projections at the oil-hose joint it covers, so expect to fit a new clip; note any banjo bolts and their washer order on your own car. Expect the hoses to hold oil after the sump has drained.
13. Remove the starter. Support the gearbox with a broad padded jack, remove the clutch slave cylinder from the bellhousing and tie it aside without opening the hydraulic line.
14. Remove the accessible bellhousing bolts, brackets and inspection covers. Mark each bolt length and position; check twice for the upper bolts and dowel-area brackets hidden behind the engine.
15. Attach the crane to rated engine lift eyes, fit the leveller and take only the engine's weight. Slightly loosen the engine-side mount fasteners, remove both mounts from the chassis, then remove the remaining mount brackets once the engine floats.
16. Remove the final bellhousing bolts. Adjust crane and gearbox heights until the joint opens squarely; pull the engine forward until the input shaft clears the clutch. Never draw the joint apart with wedges against the mating faces.
17. Raise a few centimetres at a time, changing leveller angle as needed. Stop after every movement and check the firewall heater hoses, oil lines, wiring behind the engine, exhaust studs, sump/crossmember and clutch/input shaft.
18. Move the free engine directly to the prepared stand. Fit correctly graded stand bolts with enough thread engagement and do not rest the engine on the sump or an oil-seal face.

Tie every disconnected hose and loom away from the lift path. The usual snags are a hidden rear earth, upper bellhousing bolt, clipped oxygen-sensor loom, oil-cooler hose, heater hose or A/C bracket. From practical experience my first top lift took about six hours and a familiar repeat about two. Those are planning observations, not labour times.

When the engine goes back in, Mazda's installation procedure includes steps that this top-lift method doesn't cover, including a PCM procedure after an engine replacement (a series of brake-pedal presses with the ignition on). Read the manual's installation page for the exact wording before you finish.
{:.note}

## Preparing for dismantling

- Photograph every side of the dressed engine and mark front/rear orientation.
- Remove the gearbox and clutch. Leave the flywheel/counterweight in place until the pulley lockbolt and oil-pump sprocket nut are off (see below).
- Strip the intake, throttle body, fuel rails/injectors, exhaust manifold, coils/leads, air-system hardware, wiring loom and remaining brackets.
- Blank every oil, coolant, fuel and intake opening. Degrease the exterior before opening the housing stack.
- Set out separate trays for front and rear rotors, each divided into faces A, B and C. Label stationary gears and return every reused seal to its original groove.

Never place a rotor directly on an oil-seal face. Photograph spring, notch and side-piece orientation before moving it.

## Disassembly order

This follows the sequence in Mazda's 13B-MSP engine manual in outline. Keep the manual's numbered figures open for bolt sequences and SST placement; where my wording and the manual differ, the manual wins.

### External housings and lubrication parts

1. Remove the oil filter, rear and front engine hangers and ECT sensor.
2. Remove the water-pump pulley/body, thermostat cover and thermostat.
3. Remove the oil pan, oil-pan baffle/clip, oil-level sensor and oil strainer. Do not lever against an aluminium sealing face. (A Type B engine also has an upper pan; Type A does not.)
4. Remove the OMP and keep all four pipes/nozzle positions labelled. Cap the small drillings immediately.
5. Lock the eccentric shaft through the flywheel with the specified tool, then remove the front pulley lockbolt and pulley. The bolt is very tight, so do this before any insecure stand work.
6. Remove the oil-pump bypass plug carefully: its valve and spring are loaded. Remove the front cover without driving a tool into its sealing face.
7. Remove the oil-pressure-regulator plug, spring and valve; keep the order distinct from the bypass valve.
8. Mark the metering-oil-pump drive-gear orientation. With the flywheel still locked, unstake and remove the oil-pump sprocket nut and lock washer, then the sprocket, chain, OMP drive gear, oil-pump gear and pump body/shaft components.
9. Remove the balance weight, thrust plate, thrust needle bearing and spacer. Keep the lettered end-float spacer identified.
10. A Type A oil pump can be dismantled for inspection (inner/outer rotors and shaft). A Type B pump is sealed and replaced as an assembly.

### Housing stack

1. Lock the flywheel with the SST. Remove its locknut and the flywheel/counterweight. Do not shock-load the eccentric shaft.
2. Loosen the tension bolts in Mazda's figure order, in two or three passes, then remove them and keep the seal washers accounted for.
3. Lift the rear housing with a small rotating/wiggling motion to break the oil film. Do not drive wedges between sealing faces. A side/corner seal may remain attached: return it to its labelled position immediately.
4. Remove the rear oil seal, rear stationary gear and the pressure regulator (Type A), then the rear dowel.
5. Lift the rear rotor housing vertically while controlling all three apex assemblies so they cannot fall. Mark housing orientation and width-measurement positions.
6. Lift the rear rotor from the eccentric shaft. Mazda's rotor note has you take the side piece, apex, corner and side seals and springs from the rotor's upper face into the SST tray first, then break the oil film and lift the rotor, then remove the seals from the lower face. Return every seal to its matching rear A/B/C position.
7. Remove the front dowel. With an assistant supporting the eccentric shaft upward by roughly 30 mm, lift and rotate the intermediate housing just enough to clear the shaft. Do not scrape the bearing/journal or lever on the seal track.
8. Remove the front rotor housing in the same controlled way.
9. Remove the eccentric shaft and its oil-jet plug, spring and ball. Keep them in order.
10. Lift the front rotor and empty its seals into the labelled front A/B/C tray, then remove the front plate, needle bearing, thrust plate and front stationary gear. Keep both stationary gears labelled and do not interchange them. Remove the front housing.

## Cleaning and inspection

### Rotor housings

- Chrome flaking or chipping, chatter marks, scoring and seal-track damage
- Water-jacket corrosion and cracks around ports/dowel areas
- Width at the Mazda measuring positions and maximum width variation

### Side and intermediate housings

- Flatness/distortion on a verified reference surface
- Stepped wear, inner/outer oil-seal tracks and side-seal tracks
- Port-edge damage, corrosion and cracking

### Rotors and seals

- Apex- and side-seal groove clearance, damage and carbon packing
- Corner-seal bores, oil-seal grooves and rotor-bearing bore
- Heat/carbon damage and cracks, especially between grooves and combustion recesses
- Seal height, spring free height, free movement and matched position

### Eccentric shaft, bearings and oil pump

- Journal diameter/finish, shaft runout and thrust surfaces
- Main- and rotor-bearing oil clearances, end play and oil passages
- Pump body, tip and side clearances (Type A); scoring or embedded debris

### Iron lapping (my practice, not Mazda's)

Mazda gives no lapping allowance. Past its wear or distortion limit its instruction is to replace the housing. What follows is how I would approach a borderline housing, not a Mazda procedure.

Measure flatness and wear before deciding to lap. Use a known-flat reference plate, a suitable abrasive/carrier and controlled figure-eight strokes. Rotate the housing regularly so hand pressure cannot create taper; protect port edges rather than rolling over them. Clean and measure repeatedly, recording material removed. A uniform scratch pattern does not prove flatness. Afterwards, remove every trace of abrasive from the surface, grooves and oil passages.

## Factory clearances

The standard and service-limit figures are from Mazda's October 2008 engine manual. A maximum is a rejection limit, not a machining target, and a dash means Mazda gives no figure.

<div style="overflow-x: auto;" markdown="1">

| Measurement | Mazda standard / nominal | Service limit |
| --- | ---: | ---: |
| Side-housing distortion | — | 0.04 mm max |
| Vertical side-housing wear | — | 0.10 mm max |
| Inner oil-seal-path wear | — | 0.01 mm max |
| Outer oil-seal-path wear | — | 0.10 mm max |
| Stepped-path wear | — | 0.02 mm max |
| Rotor-housing width difference | — | 0.06 mm max |
| Rotor-to-side-housing clearance | 0.05-0.19 mm | 0.05 mm min |
| Rotor round projection | 0.12-0.18 mm | 0.10 mm min |
| Apex-groove clearance (see note) | 0.042-0.101 mm | 0.15 mm max |
| Apex-seal height | 5.3 mm nominal | 4.3 mm min |
| Long apex-spring height | 5.4 mm nominal | 3.5 mm min |
| Combined reused side-seal end clearance | — | 0.40 mm max |
| Cut-off-seal height | 3.95 mm nominal | 3.80 mm min |
| Oil-seal contact width | — | 0.50 mm max |
| Oil-seal projection | — | 0.50 mm min |
| Rotor-bearing oil clearance | 0.06-0.08 mm | 0.10 mm max |
| Main-bearing clearance, without stopper | 0.045-0.085 mm | 0.10 mm max |
| Main-bearing clearance, with stopper | 0.055-0.075 mm | 0.10 mm max |
| Eccentric-shaft runout | 0.02 mm | 0.06 mm max |
| Eccentric-shaft end play | 0.04-0.09 mm | — (Mazda gives none) |
| Type A oil-pump body clearance | 0.20-0.25 mm | 0.30 mm max |
| Type A oil-pump tip clearance | 0.03-0.12 mm | 0.15 mm max |
| Type A oil-pump side clearance | 0.03-0.125 mm | 0.15 mm max |

</div>

Apex-groove clearance: Mazda's October 2008 engine manual gives two different standard ranges, 0.042-0.101 mm in the rotor-inspection procedure and 0.042-0.077 mm in the technical-data table. Both give 0.15 mm as the maximum. If your reading falls between 0.077 and 0.101 mm, record both ranges and treat 0.077 mm as the conservative standard.

End play: Mazda gives a standard of 0.04-0.09 mm and no separate maximum, so change the spacer to bring the measured value into that range rather than working to a limit. The lettered spacers run A to E at 7.985, 8.005, 8.025, 8.045 and 8.065 mm. A letter alone does not prove assembled end play. New side seals are selected by groove rank rather than treated like reused seals.

## Rotor-seal packing

Use the applicable Mazda orientation drawings while the parts are in hand. A simplified sketch cannot safely show every handed spring and notch.

1. Fit the inner and outer oil-seal springs in their specified directions.
2. Fit new oil-seal O-rings without twist, then install the oil seals over them. Use petroleum jelly only at the manual's retention points and confirm free axial movement.
3. Fit the cut-off-seal springs and seals, checking direction, projection and free return.
4. On the front-facing side of the rotor only, fit each side-seal spring and its matched/ranked side seal in the original A/B/C groove, then the corner springs, plugs and corner seals. Align each corner-seal notch with its apex groove and confirm the adjacent side seal moves freely.
5. Place the packed rotor on the correct front or intermediate housing with its protected face downward, engaging the eccentric-shaft journal without disturbing the oil seals.
6. Fit the long and short apex springs, apex side pieces and main apex seals. The long spring must engage the side-piece stop. Mazda has a bonding note for the apex seal and side piece; follow it. The side piece must not sit beneath the next housing.
7. Hold the apex assemblies inward while lowering the correctly oriented rotor housing over the rotor. Stop if force is required.
8. Fit the rear-facing side and corner seals once the rotor is in its housing, checking the corner-seal groove alignment with the SST. Recheck all exposed seals, spring return and apex movement before adding the next iron.
9. Fit new inner/outer water-jacket seals to clean grooves, untwisted, immediately before closing each housing joint. Mazda's text on lubricating the water-seal rubber is itself inconsistent (petroleum jelly in one place, no oil or grease in another), so check both notes.

Mazda's caution is to assemble only the side and corner seals on the engine-front side while the rotor is not yet in its housing. Photograph each completed layer and account for every tray position.

## Reassembly order

This is Mazda's order for a Type A engine.

1. Place the clean front housing on its fixture. Fit the labelled front stationary gear, thrust plate (chamfer towards the gear), needle bearing and plate.
2. Lubricate and fit the front rotor, the oil-jet ball, spring and plug, and the eccentric shaft. Check that the shaft turns smoothly.
3. Fit the front rotor housing on its dowels with new water seals, controlling all apex pieces. Rotate the shaft by hand.
4. Lower the intermediate housing squarely while supporting/positioning the shaft as specified. Confirm dowel engagement and turn the shaft again.
5. Fit the packed rear rotor, the rear rotor housing and the rear dowel.
6. Fit the rear pressure regulator (Type A), the rear stationary gear and the rear oil seal, engaging the stationary gear with the rotor's internal gear as the housing goes on, then the rear housing. Check free rotation after each layer.
7. Oil the tension-bolt threads and fit new seal washers. Tighten in the figure sequence over two or three passes to **31.4-39.2 N·m**, checking shaft rotation between passes.
8. Fit the flywheel/counterweight and torque its locknut to **392-490 N·m** with the specified lock and socket. Lock the shaft for everything that follows.
9. Fit the end-float spacer, needle bearing, thrust plate, balance weight, oil-pump parts (Type A or sealed Type B), OMP drive gear, chain and sprocket. Use a new sprocket lock washer and torque the nut to **31.4-46.1 N·m**, then bend the washer over.
10. Fit the bypass and pressure-regulator valves, springs and plugs to their correct bores. Fit the front cover with its seal and torque its bolts to **18.6-25.5 N·m**.
11. Fit the pulley components. Oil the lockbolt threads, fit a new O-ring, put silicone sealant on the seating face, and torque the bolt to **254-294 N·m** with the shaft locked.
12. Measure end play now, with everything above fitted. The standard is 0.04-0.09 mm. Change the spacer only from the measured result.
13. Apply the specified sealant bead to the clean oil pan and fit it within five minutes. Torque the pan bolts to **8.8-11.8 N·m** in sequence.
14. Refit the OMP, labelled lines/nozzles, water pump, thermostat, sensors, hangers, fuel/intake/exhaust components and ancillaries. Prime every opened oil path rather than relying on dry cranking.

See the [full torque page](/ProjectPages/RX8/torquespecs/) for related fasteners.

## Priming and first start

### Priming

1. Fill the engine with the planned running-in oil and fit a new filter.
2. Fill the separate Sohn reservoir, prime its supply hose and OMP inlet, and verify that the line remains air-free.
3. Fill and bleed the [cooling system](/ProjectPages/RX8/cooling/); confirm gearbox oil if it was disturbed.
4. Inspect every fuel joint, earth, starter lead, coolant/oil hose and blanking cap.
5. Positively disable fuel and ignition and crank in short intervals with starter cooling time. Disconnecting the eccentric-shaft sensor does both; Mazda uses it for the compression test.
6. Confirm a credible rise on the oil-pressure gauge and inspect for leaks between cranking intervals. Re-enable fuel and ignition only after the pressure path is established.

Full-throttle clear-flood mode can inhibit injection, but positive circuit isolation is preferable for a planned first start.

### First start

> Once the rebuilt engine starts, allow it enough time to warm and stabilise rather than switching it off after only a few seconds, as a very short initial run can leave a fresh rotary difficult to restart.

> Shut it down at once if there is no oil pressure, a major leak, uncontrolled temperature rise or abnormal mechanical noise.

Monitor oil pressure, coolant temperature, charging voltage, smoke, leaks and fan operation. Assembly oil and premix can create heavy initial smoke, but it should reduce. Fine initial material may appear in the first oil/filter; large flakes, bearing material, coolant contamination or continuing heavy debris are not normal. Open and inspect the first filter where practical.

## Running-in and oil changes

This is the procedure used for this engine, not a Mazda universal schedule.

| Mileage | Oil-change procedure |
| ---: | --- |
| 0-100 miles | Initial oil and filter |
| 100-2,000 miles | Approximately every 500 miles |
| Beyond 2,000 miles | Approximately every 3,000-5,000 miles |

Compression started relatively low and rose gradually over roughly the first 1,000 miles. Log raw and 250-rpm-corrected compression (see [compression testing](/ProjectPages/RX8/compression-testing/)), oil and Sohn consumption, coolant level and filter findings at each useful checkpoint.

## References

- Mazda 13B-MSP engine workshop manual, October 2008 (part 1773-1U-03C): sections 00-00-12 (engine type), 01-10 (disassembly, inspection, assembly) and 01-50 (technical data). [PDF via the foxed.ca mirror](https://www.foxed.ca/rx7manual/manuals/renesis%20rotary%20engine%20workshop%20manual.pdf), accessed 14 October 2026.
- Mazda RX-8 2003 workshop manual (European edition), [engine removal/installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011002000W04.html), [compression inspection](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011002000W03.html), [intake-air system](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE011301005W05.html).
- Engine mass: no Mazda figure. Secondary figures (about 112 kg bare, about 138 kg with accessories) are from Wikipedia's Mazda Wankel engine article and a 2003 forum post, neither with a primary source.
