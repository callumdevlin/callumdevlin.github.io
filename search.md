---
layout: notebook
title: Search
permalink: /search/
description: Search the project write-ups, the RX-8 notebook and the Rocket League notes.
toc: false
search: false
sitemap: false
---

<div id="site-search" class="site-search" data-index="{{ '/search.json' | relative_url }}">
  <form class="site-search-form" role="search" action="{{ '/search/' | relative_url }}" method="get">
    <label class="sr-only" for="site-search-q">Search the site</label>
    <input id="site-search-q" type="search" name="q" placeholder="e.g. torque, P1688, hose, aerial" autocomplete="off" spellcheck="false">
    <button type="submit">Search</button>
  </form>
  <p class="site-search-status" role="status" aria-live="polite"></p>
  <ul class="site-search-results"></ul>
</div>

<noscript>
Search needs JavaScript. Without it, browse from the lists instead:
the [projects](/ProjectPages/), the [RX-8 notebook](/ProjectPages/RX8/) and the [Rocket League notes](/ProjectPages/rlbot/).
</noscript>

Every word must appear on the page. Put a phrase in double quotes to match it exactly. Part numbers match with or without dashes, so `N3H1-15-185` and `N3H1 15 185` both work.
