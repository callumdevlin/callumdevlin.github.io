/*
 * Site behaviour that is layered on top of plain HTML (nothing here is needed to read a page).
 *
 *  - tables that overflow become keyboard-scrollable regions
 *  - the contents rail highlights the section being read
 *  - lab iframes size themselves to the lab's own height
 *  - search page (/search/)
 *  - Hydejack's page-transition animation is switched off for visitors who ask for reduced motion
 *
 * Hydejack swaps <main> in place when you follow a link (push-state), so scripts must not
 * assume a full page load. Everything runs through init(), which is idempotent: it is called
 * on first load and again after every in-site navigation, and each piece marks the elements
 * it has already handled.
 */
(function () {
  'use strict';
  if (window.__siteJs) return;
  window.__siteJs = true;

  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');

  // ------------------------------------------------------------------ tables
  function enhanceTables() {
    var tables = document.querySelectorAll('main table:not(.rouge-table)');
    for (var i = 0; i < tables.length; i++) {
      var t = tables[i];
      var scrolls = t.scrollWidth > t.clientWidth + 1;
      if (scrolls) {
        if (!t.hasAttribute('tabindex')) {
          t.setAttribute('tabindex', '0');
          t.setAttribute('role', 'region');
          var h = t.previousElementSibling;
          while (h && !/^H[1-6]$/.test(h.tagName)) h = h.previousElementSibling;
          var name = 'Table';
          if (h) {                                   // the heading text without the theme's "Permalink" anchor
            var clone = h.cloneNode(true), pl = clone.querySelectorAll('.permalink, [class*="permalink"]');
            for (var k = 0; k < pl.length; k++) pl[k].remove();
            name = clone.textContent.replace(/\s+/g, ' ').trim() + ': table';
          }
          t.setAttribute('aria-label', name + ' (scrolls sideways)');
        }
      } else if (t.getAttribute('role') === 'region' && t.hasAttribute('data-nb-scroll')) {
        t.removeAttribute('tabindex');
        t.removeAttribute('role');
        t.removeAttribute('aria-label');
      }
      if (scrolls) t.setAttribute('data-nb-scroll', '1');
    }
  }

  // ------------------------------------------------------------------ contents rail scroll-spy
  // Marks the last heading that has scrolled past the top of the viewport. A plain scroll check
  // (throttled to one per frame) rather than IntersectionObserver, whose callbacks do not fire
  // when a jump leaves no heading changing state.
  var spy = { byId: {}, heads: [], current: null, ticking: false };

  function spyUpdate() {
    if (!spy.heads.length) return;
    var pick = null;
    for (var i = 0; i < spy.heads.length; i++) {
      if (spy.heads[i].getBoundingClientRect().top <= 140) pick = spy.heads[i].id; else break;
    }
    if (pick === spy.current) return;
    spy.current = pick;
    for (var k in spy.byId) {
      if (k === pick) { spy.byId[k].classList.add('is-current'); spy.byId[k].setAttribute('aria-current', 'location'); }
      else { spy.byId[k].classList.remove('is-current'); spy.byId[k].removeAttribute('aria-current'); }
    }
  }

  function contentsSpy() {
    spy.byId = {}; spy.heads = []; spy.current = null;
    var links = document.querySelectorAll('.nb-rail .nb-toc a[href^="#"]');
    for (var i = 0; i < links.length; i++) {
      var id = decodeURIComponent(links[i].getAttribute('href').slice(1));
      var el = document.getElementById(id);
      if (el) { spy.byId[id] = links[i]; spy.heads.push(el); }
    }
    spyUpdate();
  }

  window.addEventListener('scroll', function () {
    if (spy.ticking || !spy.heads.length) return;
    spy.ticking = true;
    window.requestAnimationFrame(function () { spy.ticking = false; spyUpdate(); });
  }, { passive: true });

  // ------------------------------------------------------------------ labs (iframes)
  function labFrames() { return document.querySelectorAll('iframe[data-lab-source]'); }

  function requestHeight(frame) {
    try {
      frame.contentWindow.postMessage({ source: frame.getAttribute('data-lab-source'), type: 'request-height' }, window.location.origin);
    } catch (e) { /* cross-origin or not ready: the fallback height stays */ }
  }

  function initLabs() {
    var frames = labFrames();
    for (var i = 0; i < frames.length; i++) {
      (function (f) {
        if (f.getAttribute('data-nb-lab') === '1') return;
        f.setAttribute('data-nb-lab', '1');
        f.addEventListener('load', function () { requestHeight(f); });
        try {
          if (f.contentDocument && f.contentDocument.readyState === 'complete') requestHeight(f);
        } catch (e) { /* ignore */ }
      })(frames[i]);
    }
  }

  window.addEventListener('message', function (e) {
    if (e.origin !== window.location.origin) return;
    var d = e.data;
    if (!d || d.type !== 'height') return;
    var frames = labFrames();
    for (var i = 0; i < frames.length; i++) {
      var f = frames[i];
      if (e.source !== f.contentWindow || d.source !== f.getAttribute('data-lab-source')) continue;
      var px = Math.max(200, Math.min(20000, Math.round(Number(d.height))));
      if (!isNaN(px)) f.style.height = (px + 2) + 'px';
    }
  });

  // ------------------------------------------------------------------ search
  var searchIndex = null;      // parsed JSON, once
  var searchIndexPromise = null;

  function loadIndex(url) {
    if (searchIndex) return Promise.resolve(searchIndex);
    if (!searchIndexPromise) {
      searchIndexPromise = fetch(url, { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(function (docs) {
          docs.forEach(function (d) {
            d._title = (d.t || '').toLowerCase();
            d._desc = (d.d || '').toLowerCase();
            d._heads = (d.h || []).filter(function (h) { return h[0]; }).map(function (h) { return { id: h[0], text: h[1], low: h[1].toLowerCase() }; });
            d._body = (d.b || '').toLowerCase();
            d._compact = null;
          });
          searchIndex = docs;
          return docs;
        });
      searchIndexPromise.catch(function () { searchIndexPromise = null; });
    }
    return searchIndexPromise;
  }

  function compact(s) { return s.replace(/[^a-z0-9]/g, ''); }
  function esc(s) { return s.replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  // Terms are separated by spaces; "double quotes" keep a phrase together.
  function parseQuery(q) {
    var terms = [], re = /"([^"]+)"|(\S+)/g, m;
    while ((m = re.exec(q.toLowerCase()))) { var t = (m[1] || m[2]).trim(); if (t) terms.push(t); }
    return terms;
  }

  function termHits(doc, t) {
    // 1 = plain substring somewhere, 2 = only found ignoring punctuation (part numbers: n3h1-15-185 / n3h1 15 185)
    var c = compact(t);
    var inTitle = doc._title.indexOf(t) !== -1, inDesc = doc._desc.indexOf(t) !== -1;
    var inHead = false, hi;
    for (hi = 0; hi < doc._heads.length; hi++) if (doc._heads[hi].low.indexOf(t) !== -1) { inHead = true; break; }
    var bodyAt = doc._body.indexOf(t), mode = 1;
    if (!inTitle && !inDesc && !inHead && bodyAt === -1 && c.length >= 4) {
      if (doc._compact === null) doc._compact = compact(doc._title + ' ' + doc._desc + ' ' + doc._body);
      if (doc._compact.indexOf(c) !== -1) { mode = 2; }
      else return null;
    } else if (!inTitle && !inDesc && !inHead && bodyAt === -1) return null;
    var count = 0;
    if (bodyAt !== -1) { var p = 0; while (count < 8 && (p = doc._body.indexOf(t, p)) !== -1) { count++; p += t.length; } }
    return { title: inTitle, desc: inDesc, head: inHead, count: count, mode: mode };
  }

  function search(docs, q) {
    var terms = parseQuery(q);
    if (!terms.length) return [];
    var out = [];
    docs.forEach(function (d) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var h = termHits(d, terms[i]);
        if (!h) return;                       // every term must be present
        score += (h.title ? 12 : 0) + (h.head ? 6 : 0) + (h.desc ? 3 : 0) + Math.min(h.count, 5) + (h.mode === 2 ? 1 : 2);
      }
      out.push({ doc: d, score: score, terms: terms });
    });
    out.sort(function (a, b) { return b.score - a.score || a.doc.t.localeCompare(b.doc.t); });
    return out;
  }

  function highlight(text, terms) {
    var parts = terms.map(function (t) { return escRe(esc(t)); }).filter(Boolean).sort(function (a, b) { return b.length - a.length; });
    var html = esc(text);
    if (!parts.length) return html;
    return html.replace(new RegExp('(' + parts.join('|') + ')', 'gi'), '<mark>$1</mark>');
  }

  function snippet(doc, terms) {
    var body = doc.b || '', low = doc._body, at = -1, hit = '';
    terms.forEach(function (t) { var i = low.indexOf(t); if (i !== -1 && (at === -1 || i < at)) { at = i; hit = t; } });
    if (at === -1) return highlight((doc.d || '').slice(0, 200), terms);
    var start = Math.max(0, at - 70), end = Math.min(body.length, at + hit.length + 130);
    return (start > 0 ? '… ' : '') + highlight(body.slice(start, end), terms) + (end < body.length ? ' …' : '');
  }

  function renderResults(root, results, q) {
    var list = root.querySelector('.site-search-results'), status = root.querySelector('.site-search-status');
    list.innerHTML = '';
    if (!q.trim()) { status.textContent = ''; return; }
    status.textContent = results.length
      ? results.length + (results.length === 1 ? ' page matches' : ' pages match') + ' “' + q.trim() + '”.'
      : 'Nothing found for “' + q.trim() + '”. Try fewer or shorter words, or a part number without punctuation.';
    results.slice(0, 40).forEach(function (r) {
      var d = r.doc, li = document.createElement('li');
      var heads = [];
      d._heads.forEach(function (h) {
        if (heads.length < 3 && r.terms.some(function (t) { return h.low.indexOf(t) !== -1; })) heads.push(h);
      });
      li.innerHTML =
        '<p class="site-search-title"><a href="' + esc(d.u) + '">' + highlight(d.t, r.terms) + '</a></p>' +
        '<p class="site-search-where">' + esc(d.k || '') + '</p>' +
        '<p class="site-search-snippet">' + snippet(d, r.terms) + '</p>' +
        (heads.length ? '<p class="site-search-sections">In: ' + heads.map(function (h) {
          return '<a href="' + esc(d.u) + '#' + esc(h.id) + '">' + highlight(h.text, r.terms) + '</a>';
        }).join(' · ') + '</p>' : '');
      list.appendChild(li);
    });
  }

  function initSearch() {
    var root = document.getElementById('site-search');
    if (!root || root.getAttribute('data-nb-search') === '1') return;
    root.setAttribute('data-nb-search', '1');
    var input = root.querySelector('input[type="search"]'), form = root.querySelector('form');
    var url = root.getAttribute('data-index');
    var status = root.querySelector('.site-search-status');
    status.textContent = 'Loading the search index…';

    function run() {
      var q = input.value;
      loadIndex(url).then(function (docs) { renderResults(root, search(docs, q), q); })
        .catch(function () { status.textContent = 'The search index could not be loaded. Use the menu to browse instead.'; });
      try {
        var u = new URL(window.location.href);
        if (q.trim()) u.searchParams.set('q', q.trim()); else u.searchParams.delete('q');
        window.history.replaceState(window.history.state, '', u.pathname + u.search + u.hash);
      } catch (e) { /* ignore */ }
    }
    var timer = null;
    input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(run, 120); });
    form.addEventListener('submit', function (e) { e.preventDefault(); run(); });

    var initial = '';
    try { initial = new URL(window.location.href).searchParams.get('q') || ''; } catch (e) { /* ignore */ }
    input.value = initial;
    loadIndex(url).then(function () { status.textContent = ''; if (initial) run(); })
      .catch(function () { status.textContent = 'The search index could not be loaded. Use the menu to browse instead.'; });
    input.focus({ preventScroll: true });
  }

  // ------------------------------------------------------------------ wiring
  function init() {
    enhanceTables();
    contentsSpy();
    initLabs();
    initSearch();
  }

  function setMotion() {
    var ps = document.getElementById('_pushState');
    if (ps && reduceMotion && reduceMotion.matches) ps.setAttribute('duration', '0');
  }

  var resizeTimer = null;
  window.addEventListener('resize', function () { clearTimeout(resizeTimer); resizeTimer = setTimeout(enhanceTables, 200); });

  function boot() {
    setMotion();
    init();
    var ps = document.getElementById('_pushState');
    if (ps) {
      ps.addEventListener('hy-push-state-load', init);
      ps.addEventListener('hy-push-state-after', init);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
