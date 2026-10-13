---
title: RX-8 Acceleration Lab
permalink: /ProjectPages/RX8/acceleration-lab/
description: >
  Interactive gearing, road-speed and full-throttle acceleration lab for a 2005
  UK Series 1 RX-8 (231 PS six-speed or 192 PS five-speed).
---

{% comment %}
  The lab itself is a static app copied to tools/rx8-acceleration/ (the contents of
  its dist/ folder). This page only embeds it in an iframe, and is kept almost empty
  on purpose.

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

Companion to the [drivetrain notes](/ProjectPages/RX8/drivetrain/). It runs in your browser: nothing is uploaded or stored. <a class="no-push-state" href="{{ acc_tool_url }}" target="_blank" rel="noopener">Open it full page &rarr;</a>

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
.acc-embed-wrap { width: 100%; margin: 0 0 2rem; }
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
