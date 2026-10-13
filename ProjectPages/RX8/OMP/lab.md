---
title: RX-8 OMP Lab
permalink: /ProjectPages/RX8/OMP/lab/
description: >
  Interactive demo of the Series 1 RX-8 oil metering pump: how engine speed,
  load and coolant temperature set the commanded step, and how the start-up
  checks and switch faults play out.
---

{% comment %}
  The lab itself is a static app copied to tools/rx8-omp/ (the contents of its
  dist/ folder). This page only embeds it in an iframe, and is kept almost empty
  on purpose.

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

Companion to the [Series 1 OMP guide](/ProjectPages/RX8/OMP/). It runs in your browser: nothing is uploaded or stored. <a class="no-push-state" href="{{ omp_tool_url }}" target="_blank" rel="noopener">Open it full page &rarr;</a>

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
