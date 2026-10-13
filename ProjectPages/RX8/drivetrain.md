---
title: RX-8 Y16M-D Gearbox, PPF and Super-LSD
permalink: /ProjectPages/RX8/drivetrain/
description: >
  Six-speed ratios, oil service, Power Plant Frame alignment and Super-LSD operation,
  plus an interactive gearing and acceleration lab.
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

The Y16M-D (Aisin AZ6) is a fully synchronised six-speed; first, second and third use triple-cone synchronisers.

## Oil service

| Unit | Oil | Capacity | Drain/fill torque |
| --- | --- | ---: | ---: |
| Y16M-D gearbox | SAE 75W-90, API GL-4 or GL-5 | Approximately 1.75 L | 27–48 Nm, new washers |
| Rear differential | API GL-5; SAE 90, 80W-90 or 75W-90 | Approximately 1.2–1.4 L | 39.2–53.9 Nm, new washers |

Keep the car level. On each unit the filler plug is high in the side of the casing and the drain is at its lowest service point. **Remove the filler first** so a seized filler cannot leave an empty unit. Drain, clean the magnetic plug where fitted, install the drain with a new washer, then fill through the side opening until oil is near the lower brim. Let excess settle to a slow drip before fitting the filler with a new washer.

## Acceleration Lab

{% comment %}
  The lab is a static app copied to tools/rx8-acceleration/ (the contents of its
  dist/ folder). This section only embeds it in an iframe.

  Configure here:
    acc_tool_path    where the built lab lives (with trailing slash)
    acc_height       fallback iframe height on wide screens, in px
    acc_height_small fallback iframe height on narrow screens (< 700 px wide), in px

  The lab (opened with ?embed=1) reports its own content height to this page, and
  the iframe's onload handler below uses that to fit the iframe exactly. The two
  heights above are only the starting size and the fallback if that doesn't happen.
  The message exchange is same-origin only, which holds because the lab is served
  from this same site.
{% endcomment %}
{% assign acc_tool_path = '/tools/rx8-acceleration/' %}
{% assign acc_height = 2800 %}
{% assign acc_height_small = 4200 %}
{% assign acc_tool_url = acc_tool_path | relative_url %}

I used to list calculated road speeds and shift drops here as fixed tables and graphs. This interactive lab replaces them. It starts from the six-speed ratios and 225/45R18 tyres above, and it runs entirely in your browser: nothing is uploaded or stored.

- **Gearing** shows engine rpm against road speed in each gear, with the redline and the shift points.
- **Acceleration** shows wheel force against drag and rolling resistance for a full-throttle pull.
- **Run comparison** compares shifting at a fixed rpm with shifting where the next gear accelerates harder, and replays the run.

It opens on the 231 PS six-speed car, and the configuration selector also has the 192 PS five-speed.

<p class="acc-open"><a class="no-push-state" href="{{ acc_tool_url }}" target="_blank" rel="noopener">Open the lab in a new tab &rarr;</a></p>

{::nomarkdown}
<div class="acc-embed-wrap" style="--acc-height: {{ acc_height }}px; --acc-height-small: {{ acc_height_small }}px;">
<iframe id="acceleration-lab-frame" class="acc-embed" src="{{ acc_tool_url }}?embed=1" title="RX-8 Acceleration Lab: interactive gearing, acceleration and shift-strategy tool" loading="lazy" onload="var w = window, f = this;
if (!w.accLabFit) {
  w.accLabFit = true;
  w.addEventListener('message', function (e) {
    var d = e.data, fr = document.getElementById('acceleration-lab-frame');
    if (!fr || !d || e.source !== fr.contentWindow || e.origin !== w.location.origin) return;
    if (d.source !== 'rx8-acceleration-lab' || d.type !== 'height') return;
    var px = Math.max(200, Math.min(20000, Math.round(Number(d.height))));
    if (!isNaN(px)) fr.style.height = (px + 2) + 'px';
  });
}
f.contentWindow.postMessage({ source: 'rx8-acceleration-lab', type: 'request-height' }, w.location.origin);"></iframe>
</div>
<noscript><p>The lab needs JavaScript. You can still <a href="{{ acc_tool_url }}">open it directly</a>.</p></noscript>
<style>
.acc-open { margin: 0 0 1rem; font-weight: 600; }
.acc-embed-wrap { width: 100%; margin: 0 0 1.5rem; }
.acc-embed {
  display: block;
  width: 100%;
  height: var(--acc-height, 2800px);
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 6px;
  background: #fff;
}
@media (max-width: 700px) {
  .acc-embed { height: var(--acc-height-small, 4200px); }
}
</style>
{:/nomarkdown}

> **How far to trust it.** It is a simplified one-dimensional model: full throttle, level road, still air, and rotational inertia left out, which makes acceleration slightly optimistic. Each car's engine torque curve is illustrative: only the published peak-torque and peak-power points are anchored to Mazda's figures, and I haven't tuned the model to reproduce Mazda's 0-62 mph time or top speed. The rolling radius is 0.97 times the unloaded tyre radius (an editable assumption), so its road speeds sit about 3% below the nominal-diameter figures I used to list here.
{:.note}

After an upshift the engine speed becomes `rpm before × next ratio ÷ current ratio`, ignoring tyre growth, slip and the road-speed loss during the shift.

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

