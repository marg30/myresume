/* ==========================================================================
   Blue Hour Portfolio · interactions
   - pixel-art section icons
   - theme switcher (remembers your choice)
   - section navigation highlight
   - slide-in of content blocks
   - project filter (click a skill or a technology)
   - pixel thumbnails for projects without a screenshot
   - "copy email" button
   The page is fully readable without any of this.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  var body = document.body;

  /* ---------- 1. Pixel icons (8 x 8 bitmaps) ---------- */
  var ICONS = {
    user: ['..####..', '.######.', '.######.', '..####..', '...##...', '.######.', '########', '########'],
    briefcase: ['..####..', '..#..#..', '########', '#......#', '########', '#..##..#', '#......#', '########'],
    laptop: ['.######.', '.#....#.', '.#....#.', '.#....#.', '.######.', '########', '#......#', '########'],
    bolt: ['....##..', '...##...', '..##....', '.######.', '...##...', '..##....', '.##.....', '.#......'],
    cap: ['...##...', '..####..', '.######.', '########', '..#..#..', '..#..#..', '..####..', '........'],
    globe: ['..####..', '.#.##.#.', '#..##..#', '########', '#..##..#', '.#.##.#.', '..####..', '........'],
    flask: ['..####..', '...##...', '...##...', '..####..', '.##..##.', '#.####.#', '########', '.######.'],
    mail: ['########', '##....##', '#.#..#.#', '#..##..#', '#......#', '#......#', '########', '........'],
    moon: ['..####..', '.###....', '###.....', '###.....', '###.....', '.###....', '..####..', '........']
  };

  function pixelIcon(name) {
    var rows = ICONS[name];
    if (!rows) return null;
    var d = '';
    rows.forEach(function (row, y) {
      var x = 0;
      while (x < row.length) {
        if (row.charAt(x) === '#') {
          var start = x;
          while (x < row.length && row.charAt(x) === '#') x++;
          d += 'M' + start + ' ' + y + 'h' + (x - start) + 'v1h-' + (x - start) + 'z';
        } else x++;
      }
    });
    return '<svg viewBox="0 0 8 8" shape-rendering="crispEdges" fill="currentColor" focusable="false"><path d="' + d + '"/></svg>';
  }
  $$('.pix').forEach(function (el) {
    var svg = pixelIcon(el.getAttribute('data-pix'));
    if (svg) el.innerHTML = svg;
  });

  /* ---------- 2. Themes ---------- */
  var swatches = $$('[data-theme-set]');
  function currentTheme() { return root.getAttribute('data-theme'); }
  function markTheme() {
    swatches.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-theme-set') === currentTheme())); });
  }
  swatches.forEach(function (b) {
    b.addEventListener('click', function () {
      root.setAttribute('data-theme', b.getAttribute('data-theme-set'));
      try { localStorage.setItem('pf-theme', b.getAttribute('data-theme-set')); } catch (e) {}
      markTheme();
      document.dispatchEvent(new Event('themechange'));
      drawThumbs();
    });
  });
  markTheme();

  /* ---------- 3. Navigation highlight ---------- */
  var navLinks = $$('[data-nav]');
  if ('IntersectionObserver' in window && navLinks.length) {
    var sections = navLinks.map(function (a) { return document.getElementById(a.getAttribute('data-nav')); }).filter(Boolean);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        navLinks.forEach(function (a) {
          var on = a.getAttribute('data-nav') === en.target.id;
          a.classList.toggle('is-active', on);
          if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    sections.forEach(function (s) { io.observe(s); });
  }

  /* ---------- 4. Slide-in on scroll ---------- */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); ro.unobserve(en.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -4% 0px' });
    reveals.forEach(function (el) { ro.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- 5. Project filter ---------- */
  var cards = $$('.project');
  var filtersBox = $('#filters');
  var countBox = $('#count');
  var active = '';

  function labelFor(key) {
    var el = $('[data-filter="' + key + '"]');
    return el ? el.textContent.trim().replace(/×\d+$/, '').trim() : key;
  }

  function applyFilter(key) {
    active = key === active ? '' : key;
    var shown = 0;
    cards.forEach(function (c) {
      var match = !active || c.getAttribute('data-tags').split('|').indexOf(active) > -1;
      var wasHidden = c.hidden;
      c.hidden = !match;
      if (match) {
        shown++;
        c.classList.add('in');
        if (wasHidden) { c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); }
      }
    });
    $$('[data-filter]').forEach(function (b) {
      var key2 = b.getAttribute('data-filter');
      b.setAttribute('aria-pressed', String(!!active && key2 === active));
    });
    $$('.chip[data-all]').forEach(function (b) { b.setAttribute('aria-pressed', String(!active)); });
    if (countBox) {
      countBox.hidden = !active;
      countBox.textContent = active ? body.getAttribute('data-showing') + ' ' + shown + ' ' + body.getAttribute('data-of') + ' ' + cards.length + ' ' + body.getAttribute('data-projects') + ' · ' + labelFor(active) : '';
    }
  }

  if (cards.length && filtersBox) {
    var tally = {};
    $$('.project [data-filter]').forEach(function (b) {
      var k = b.getAttribute('data-filter');
      if (!tally[k]) tally[k] = { n: 0, label: b.textContent.trim() };
      tally[k].n++;
    });
    var keys = Object.keys(tally).sort(function (a, b) { return tally[b].n - tally[a].n || a.localeCompare(b); });

    filtersBox.setAttribute('role', 'group');
    filtersBox.setAttribute('aria-label', body.getAttribute('data-filter-label'));
    var all = document.createElement('button');
    all.type = 'button'; all.className = 'chip'; all.setAttribute('data-all', ''); all.setAttribute('aria-pressed', 'true');
    all.textContent = body.getAttribute('data-all');
    all.addEventListener('click', function () { active = 'x'; applyFilter('x'); });
    filtersBox.appendChild(all);
    keys.forEach(function (k) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'chip'; b.setAttribute('data-filter', k); b.setAttribute('aria-pressed', 'false');
      b.textContent = tally[k].label;
      filtersBox.appendChild(b);
    });
    filtersBox.hidden = false;
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('[data-filter]') : null;
    if (!b) return;
    var inSkills = !!b.closest('.skill-group');
    applyFilter(b.getAttribute('data-filter'));
    if (inSkills && active) {
      var target = document.getElementById('projects');
      if (target) target.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    }
  });

  /* ---------- 6. Pixel thumbnails ---------- */
  function hash(s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  function rng(a) {
    return function () {
      a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function cv(name, fb) { var v = getComputedStyle(root).getPropertyValue(name).trim(); return v || fb; }
  function rgb(hex) { hex = hex.replace('#', ''); if (hex.length === 3) hex = hex.replace(/./g, '$&$&'); var n = parseInt(hex, 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; }
  function mix(a, b, t) { return 'rgb(' + [0, 1, 2].map(function (i) { return Math.round(a[i] + (b[i] - a[i]) * t); }).join(',') + ')'; }

  function drawThumbs() {
    var s1 = rgb(cv('--sky-1', '#0A0F3A')), s2 = rgb(cv('--sky-2', '#2B3C9E')), s4 = rgb(cv('--sky-4', '#F5A8C8'));
    var city = cv('--city', '#0A0E2E'), city2 = cv('--city-2', '#1C2670'), win = cv('--win', '#FFD98A');
    var moon = cv('--moon', '#FFF2C4'), star = cv('--star', '#FFFFFF'), showStars = cv('--stars', '1') !== '0';
    $$('.thumb-canvas').forEach(function (c) {
      var w = c.width = 64, h = c.height = 28, g = c.getContext('2d');
      var seed = hash(c.getAttribute('data-seed') || 'x'), r = rng(seed), motif = seed % 4;
      var bands = 7;
      for (var i = 0; i < bands; i++) {
        var t = i / (bands - 1);
        g.fillStyle = t < 0.6 ? mix(s1, s2, t / 0.6) : mix(s2, s4, (t - 0.6) / 0.4);
        g.fillRect(0, Math.round(i * h / bands), w, Math.ceil(h / bands) + 1);
      }
      if (showStars) { g.fillStyle = star; for (var k = 0; k < 14; k++) g.fillRect(Math.floor(r() * w), Math.floor(r() * h * 0.5), 1, 1); }
      g.fillStyle = moon;
      var mx = 6 + Math.floor(r() * (w - 18)), my = 3 + Math.floor(r() * 5);
      g.fillRect(mx + 1, my, 4, 1); g.fillRect(mx, my + 1, 6, 4); g.fillRect(mx + 1, my + 5, 4, 1);
      if (motif === 0 || motif === 3) {            // skyline
        for (var x = 0; x < w;) {
          var bw = 4 + Math.floor(r() * 7), bh = 5 + Math.floor(r() * 12);
          g.fillStyle = city; g.fillRect(x, h - bh, bw, bh);
          g.fillStyle = win;
          for (var wy = h - bh + 2; wy < h - 1; wy += 3) for (var wx = x + 1; wx < x + bw - 1; wx += 2) if (r() < 0.4) g.fillRect(wx, wy, 1, 1);
          x += bw;
        }
      } else if (motif === 1) {                      // hills
        [city2, city].forEach(function (colr, n) {
          g.fillStyle = colr;
          for (var x2 = 0; x2 < w; x2++) {
            var hh = Math.round(5 + n * 3 + Math.sin(x2 / (6 + n * 3) + seed % 7) * 3 + r());
            g.fillRect(x2, h - hh, 1, hh);
          }
        });
      } else {                                       // sea with moon trail
        g.fillStyle = city2; g.fillRect(0, h - 10, w, 10);
        g.fillStyle = moon;
        for (var yy = h - 9; yy < h; yy += 2) g.fillRect(mx + 2 + Math.floor(r() * 3) - 1, yy, 2 + Math.floor(r() * 3), 1);
        g.fillStyle = city; g.fillRect(0, h - 3, w, 3);
      }
    });
  }
  drawThumbs();

  /* Skill logos that fail to load are simply removed */
  $$('img.devicon').forEach(function (img) { img.addEventListener('error', function () { img.remove(); }); });

  /* ---------- 7. Copy email ---------- */
  var copyBtn = $('#copy-mail');
  if (copyBtn) {
    var label = $('.copy-label', copyBtn), original = label ? label.textContent : '';
    function done() {
      if (!label) return;
      label.textContent = body.getAttribute('data-copied');
      setTimeout(function () { label.textContent = original; }, 1800);
    }
    function fallback(text) {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch (e) {}
      document.body.removeChild(ta);
    }
    copyBtn.addEventListener('click', function () {
      var text = copyBtn.getAttribute('data-email');
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () { fallback(text); });
      else fallback(text);
    });
  }
}());
