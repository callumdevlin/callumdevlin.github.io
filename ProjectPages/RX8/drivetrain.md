---
title: RX-8 Y16M-D Gearbox, PPF and Super-LSD
permalink: /ProjectPages/RX8/drivetrain/
description: >
  Six-speed ratios, oil service, calculated road speed, Power Plant Frame alignment and Super-LSD operation.
---

## Gearbox ratios

| Gear | Ratio |
| --- | ---: |
| 1st | 3.760 |
| 2nd | 2.269 |
| 3rd | 1.645 |
| 4th | 1.187 |
| 5th | 1.000 |
| 6th | 0.843 |
| Reverse | 3.564 |
| Final drive | 4.444 |

The Y16M-D is a fully synchronised six-speed; first, second and third use triple-cone synchronisers.

## Oil service

| Unit | Oil | Capacity | Drain/fill torque |
| --- | --- | ---: | ---: |
| Y16M-D gearbox | SAE 75W-90, API GL-4 or GL-5 | Approximately 1.75 L | 27–48 Nm, new washers |
| Rear differential | API GL-5; SAE 90, 80W-90 or 75W-90 | Approximately 1.2–1.4 L | 39.2–53.9 Nm, new washers |

Keep the car level. On each unit the filler plug is high in the side of the casing and the drain is at its lowest service point. **Remove the filler first** so a seized filler cannot leave an empty unit. Drain, clean the magnetic plug where fitted, install the drain with a new washer, then fill through the side opening until oil is near the lower brim. Let excess settle to a slow drip before fitting the filler with a new washer.

## Calculated road speeds

These figures use a nominal 225/45R18 diameter of 659.7 mm, not loaded rolling radius.

| Gear | mph per 1,000 rpm | km/h per 1,000 rpm |
| --- | ---: | ---: |
| 1st | 4.63 | 7.44 |
| 2nd | 7.66 | 12.33 |
| 3rd | 10.57 | 17.01 |
| 4th | 14.65 | 23.58 |
| 5th | 17.39 | 27.98 |
| 6th | 20.62 | 33.19 |

<div style="overflow-x:auto">

| Gear | 30 mph | 40 mph | 50 mph | 60 mph | 70 mph |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1st | 6,488 | 8,650 | >9,500 | >9,500 | >9,500 |
| 2nd | 3,915 | 5,220 | 6,525 | 7,830 | 9,135 |
| 3rd | 2,838 | 3,784 | 4,731 | 5,677 | 6,623 |
| 4th | 2,048 | 2,731 | 3,413 | 4,096 | 4,779 |
| 5th | 1,725 | 2,301 | 2,876 | 3,451 | 4,026 |
| 6th | 1,455 | 1,939 | 2,424 | 2,909 | 3,394 |

</div>

![Calculated Y16M-D road-speed curves for 225/45R18 tyres](/assets/rx8/generated/gear-speed-curves.svg)

| Shift | From 8,500 rpm | From 9,000 rpm | From 9,500 rpm |
| --- | ---: | ---: | ---: |
| 1st → 2nd | 5,129 | 5,431 | 5,733 |
| 2nd → 3rd | 6,162 | 6,525 | 6,887 |
| 3rd → 4th | 6,133 | 6,494 | 6,855 |
| 4th → 5th | 7,161 | 7,582 | 8,003 |
| 5th → 6th | 7,166 | 7,587 | 8,008 |

![Calculated RPM after each Y16M-D upshift](/assets/rx8/generated/shift-rpm-drop.svg)

`rpm after = rpm before × next ratio / current ratio`. Real tyre growth, slip and road-speed loss during the shift are not included.

## Power Plant Frame

The PPF rigidly relates gearbox and differential. Its height sets the driveline axis; an incorrect setting can preload mounts, alter propshaft alignment and create vibration or noise.

### Removal

1. Support the gearbox securely with a transmission jack.
2. Remove the exhaust/tunnel components needed to expose the PPF and mark the propshaft flange before removal where applicable.
3. Support the differential if its mounting is also being loosened.
4. Loosen and remove the PPF fasteners in a controlled sequence, then lower the frame without allowing the gearbox or differential to rotate on their mounts.

### Installation and height setting

1. Fit the PPF and temporarily tighten its nuts in Mazda's numbered order.
2. Tighten rear nut No. 1 only until the PPF is fully seated into the differential.
3. Refit the heat shield, exhaust-manifold stay, exhaust, silencer and front tunnel member—the datum member must be installed before adjustment.
4. Raise the **front/transmission end** of the PPF with the transmission jack until dimension A is **48.4–56.4 mm**.
5. Tighten rear differential fasteners Nos. 1 and 2 to **126–154 Nm**, then No. 3 to **74.5–93.2 Nm**, following the manual's numbered pattern.
6. Tighten the front/transmission-side nuts to **126–154 Nm**.
7. Remove the jack and remeasure dimension A; readjust if it is outside 48.4–56.4 mm.

![Side-view PPF diagram showing the exact dimension-A surfaces](/assets/rx8/generated/ppf-datum.svg)

Dimension A is vertical distance from the **lower surface of the PPF** to the **lower surface of the installed front tunnel member** at Mazda's illustrated front datum. It is not measured to the floorpan, exhaust shield or an arbitrary bolt head.

## Super-LSD

The factory Super-LSD is a torque-sensing geared differential, with a nominal torque-bias ratio of **2.0** and initial torque of **49 Nm**. It permits the normal left/right speed difference in a corner while biasing torque toward the tyre with more usable reaction. It is not a clutch-plate unit and needs neither clutch-pack servicing nor friction modifier.

When one wheel has almost no reaction torque—ice or a wheel off the ground—a torque-biasing differential cannot multiply useful torque from zero. Gentle brake/traction-control intervention can provide reaction, but tyres and safe recovery take priority.

For noise, first check equal tyre size/pressure, differential level/leaks, mounts, driveshafts and propshaft joints. A load/coast whine suggests gear or bearing setup; a speed-related rumble can be a bearing or tyre; normal low-speed differentiation is not itself a fault. Do not dismantle the internal gear case as routine service.

## References

- [Mazda Y16M-D specifications](https://www.foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE050001030T05.html)
- [Mazda Y16M-D oil replacement](https://charm.li/Mazda/RX-8%2005%2F2003%20-%2003%2F2008%20%28d932-1a-22c_ver30%29/esicont/srvc/html/id051107247900.html)
- [Mazda transmission/PPF installation](https://foxed.ca/rx7manual/2003mazdarx8/esicont/en/srvc/html/BHE051101025W07.html)
- [Mazda differential oil replacement](https://charm.li/Mazda/RX-8%2005%2F2003%20-%2003%2F2008%20%28d932-1a-22c_ver30%29/esicont/srvc/html/id031400800200.html)

