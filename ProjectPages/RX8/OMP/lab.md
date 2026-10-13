---
title: RX-8 OMP Lab
permalink: /ProjectPages/RX8/OMP/lab/
description: >
  An interactive companion to my Series 1 OMP guide: see how engine speed,
  load and coolant temperature change the commanded step, and replay the
  start-up checks and switch faults.
---

{% comment %}
  The lab itself is a static app copied to tools/rx8-omp/ (the contents of its
  dist/ folder). This page only embeds it in an iframe.

  Configure here:
    omp_tool_path    where the built lab lives (with trailing slash)
    omp_height       fallback iframe height on wide screens, in px
    omp_height_small fallback iframe height on narrow screens (< 700 px wide), in px

  The lab (opened with ?embed=1) reports its own content height to this page, and
  the iframe's onload handler below uses that to fit the iframe exactly. The two
  heights above are only the starting size and the fallback if that doesn't happen.
  The message exchange is same-origin only, which holds because the lab is served
  from this same site.
{% endcomment %}
{% assign omp_tool_path = '/tools/rx8-omp/' %}
{% assign omp_height = 2600 %}
{% assign omp_height_small = 3700 %}
{% assign omp_tool_url = omp_tool_path | relative_url %}

I built this as an interactive companion to my [Series 1 OMP guide](/ProjectPages/RX8/OMP/). It runs entirely in your browser: there's no account, nothing is uploaded and nothing is stored.

It covers the stock Series 1 oil metering pump only, not the Series 2 system or an electric replacement, and it's modelled on a 2005 UK Series 1 (231 PS, six-port, manual).

> **Reference calibration / provisional model.** I use community-decoded six-port ROM data for the reference step tables. I haven't verified an exact match to my 2005 UK ECU, so these illustrate the control behaviour rather than reproduce my car's calibration exactly. The oil-delivery figures are my own estimates from published teardown geometry, not measurements, and the start-up timings are illustrative.
{:.note}

<p class="omp-open"><a class="no-push-state" href="{{ omp_tool_url }}" target="_blank" rel="noopener">Open the lab in a new tab &rarr;</a></p>

{::nomarkdown}
<div class="omp-embed-wrap" style="--omp-height: {{ omp_height }}px; --omp-height-small: {{ omp_height_small }}px;">
<iframe id="omp-lab-frame" class="omp-embed" src="{{ omp_tool_url }}?embed=1" title="RX-8 OMP Lab: interactive oil metering pump teaching tool" loading="lazy" onload="var w = window, f = this;
if (!w.ompLabFit) {
  w.ompLabFit = true;
  w.addEventListener('message', function (e) {
    var d = e.data, fr = document.getElementById('omp-lab-frame');
    if (!fr || !d || e.source !== fr.contentWindow || e.origin !== w.location.origin) return;
    if (d.source !== 'rx8-omp-lab' || d.type !== 'height') return;
    var px = Math.max(200, Math.min(20000, Math.round(Number(d.height))));
    if (!isNaN(px)) fr.style.height = (px + 2) + 'px';
  });
}
f.contentWindow.postMessage({ source: 'rx8-omp-lab', type: 'request-height' }, w.location.origin);"></iframe>
</div>
<noscript><p>The lab needs JavaScript. You can still <a href="{{ omp_tool_url }}">open it directly</a>.</p></noscript>
<style>
.omp-open { margin: 0 0 1rem; font-weight: 600; }
.omp-embed-wrap { width: 100%; margin: 0 0 2rem; }
.omp-embed {
  display: block;
  width: 100%;
  height: var(--omp-height, 2600px);
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 6px;
  background: #fff;
}
@media (max-width: 700px) {
  .omp-embed { height: var(--omp-height-small, 3700px); }
}
</style>
{:/nomarkdown}

## What to try

- **Explore OMP.** Drag the engine speed slider (700 to 9,000 rpm) and switch between a warm engine under light load, a warm engine under high load and a cold example. The graph keeps its full curve and only the marker moves, so you can see that the same RPM can ask for quite different steps. The cold example is higher because of the coolant-temperature minimum, not because of engine speed.
- **Startup & checks.** Pick an example and press play. The stepper homes to zero with 60 reverse commands, and then, only when a position check is due, sweeps towards step 60 while the binary switch changes to On. Try the three switch-feedback faults and the jammed mechanism, and compare what the controller thinks with where the mechanism actually is.

## What it's meant to show

1. Engine rotation drives the pumping.
2. The stepper adjusts the stroke.
3. Oil demand depends on operating conditions, not RPM alone.
4. Startup establishes a position reference, and sometimes a separate position check.
5. The positioning switch is binary: it can't tell you how much oil is flowing.
6. A fault can leave the controller's idea of the position different from the physical position.

The mechanical background is in [how the OMP works](/ProjectPages/RX8/OMP/how-it-works/).

## What's documented, decoded and estimated

- **Documented:** how the pump is built and controlled, the start-up homing and position check, the fault-code conditions and the electrical values come from Mazda's service information.
- **Decoded:** the reference commanded-step tables are community-decoded ROM data, used as published.
- **My own formula:** the way those tables are combined into one commanded step is a provisional formula of mine, because the factory logic isn't published.
- **Estimated:** oil delivery is calculated from published teardown geometry. I don't infer it from the step tables, because they describe a different quantity, and it isn't a measurement.
- **Illustrative:** the start-up timings, diagnostic windows, switch threshold and operating-condition presets are teaching values.

The lab's own *Model notes and sources* section lists every source and the ROM details. The approximate step and flow figures I logged on my own engine, on the [engine running data](/ProjectPages/RX8/enginedata/) page, are a relative characterisation rather than a calibrated map, so I haven't used them to set any of the lab's defaults.

## Related Pages

- [Series 1 OMP guide](/ProjectPages/RX8/OMP/): the full set of OMP pages.
- [How the OMP works](/ProjectPages/RX8/OMP/how-it-works/): drive, stroke control, initial-set and monitoring.
- [Diagnostics & testing](/ProjectPages/RX8/OMP/testing/): practical checks and fault codes.
- [13B-MSP engine running data](/ProjectPages/RX8/enginedata/): my logged oil pressure, temperature and OMP data.
- [EnduraOMP](/ProjectPages/EnduraOMP/): my MEng project, a closed-loop replacement for this system.
