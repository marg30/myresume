/* ==========================================================================
   Blue Hour sky
   Draws the pixel-art twilight scene behind the introduction: a dithered
   gradient sky, twinkling stars, a crescent moon, drifting clouds and a city
   whose windows switch on one by one. Move the pointer for a little parallax,
   click the sky for a shooting star.

   Colors come from the CSS variables of the active theme (--sky-1 ... --win),
   so changing a theme in main.css changes the scene too.
   ========================================================================== */
(function () {
  'use strict';

  var canvas = document.getElementById('sky');
  if (!canvas || !canvas.getContext) return;

  var ctx = canvas.getContext('2d');
  var hero = canvas.parentNode;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var PX = 4;                       // CSS pixels per scene pixel
  var FRAME = 1000 / 12;            // 12 frames per second, like an old console
  var BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]];

  var W = 0, H = 0;
  var skyLayer, farLayer, nearLayer, moon;
  var stars = [], clouds = [], windows = [];
  var col = {}, showStars = true, showWindows = true;
  var shoot = null;
  var pointer = 0, parallax = 0;
  var t0 = performance.now(), lastFrame = 0, onScreen = true, raf = 0;

  /* ----- helpers ----- */
  function cssVar(name, fallback) {
    var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return v || fallback;
  }
  function rgb(hex) {
    hex = String(hex).replace('#', '');
    if (hex.length === 3) hex = hex.replace(/./g, '$&$&');
    var n = parseInt(hex, 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
  }
  function str(c) { return 'rgb(' + c[0] + ',' + c[1] + ',' + c[2] + ')'; }
  function mix(a, b, t) {
    return [Math.round(a[0] + (b[0] - a[0]) * t), Math.round(a[1] + (b[1] - a[1]) * t), Math.round(a[2] + (b[2] - a[2]) * t)];
  }
  function seeded(seed) {
    var a = seed >>> 0;
    return function () {
      a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function layer(w, h) {
    var c = document.createElement('canvas');
    c.width = w; c.height = h;
    var g = c.getContext('2d');
    return { canvas: c, g: g };
  }
  function skyAt(t) {
    var stops = [0, 0.45, 0.78, 1], cs = [col.s1, col.s2, col.s3, col.s4];
    for (var i = 1; i < stops.length; i++) {
      if (t <= stops[i]) return mix(cs[i - 1], cs[i], (t - stops[i - 1]) / (stops[i] - stops[i - 1]));
    }
    return cs[3];
  }

  /* ----- scene construction ----- */
  function readColors() {
    col.s1 = rgb(cssVar('--sky-1', '#0A0F3A'));
    col.s2 = rgb(cssVar('--sky-2', '#2B3C9E'));
    col.s3 = rgb(cssVar('--sky-3', '#6477E0'));
    col.s4 = rgb(cssVar('--sky-4', '#F5A8C8'));
    col.cloud = rgb(cssVar('--cloud', '#8FA2F0'));
    col.cloud2 = rgb(cssVar('--cloud-2', '#F2A6C9'));
    col.moon = rgb(cssVar('--moon', '#FFF2C4'));
    col.city = rgb(cssVar('--city', '#0A0E2E'));
    col.city2 = rgb(cssVar('--city-2', '#1C2670'));
    col.win = rgb(cssVar('--win', '#FFD98A'));
    col.star = rgb(cssVar('--star', '#FFFFFF'));
    showStars = cssVar('--stars', '1') !== '0';
    showWindows = cssVar('--windows', '1') !== '0';
  }

  function buildSky() {
    skyLayer = layer(W, H);
    var img = skyLayer.g.createImageData(W, H), d = img.data, N = 18;
    for (var y = 0; y < H; y++) {
      var v = (y / Math.max(1, H - 1)) * N, band = Math.floor(v), frac = v - band;
      for (var x = 0; x < W; x++) {
        var b = band + (frac > (BAYER[y & 3][x & 3] + 0.5) / 16 ? 1 : 0);
        var c = skyAt(Math.min(1, b / N)), i = (y * W + x) * 4;
        d[i] = c[0]; d[i + 1] = c[1]; d[i + 2] = c[2]; d[i + 3] = 255;
      }
    }
    skyLayer.g.putImageData(img, 0, 0);
  }

  function buildCity(rand) {
    farLayer = layer(W, H);
    nearLayer = layer(W, H);
    windows = [];

    function skyline(L, color, minH, maxH, minW, maxW, withWindows) {
      var g = L.g, x = -2;
      g.fillStyle = str(color);
      while (x < W) {
        var w = minW + Math.floor(rand() * (maxW - minW + 1));
        var h = Math.floor(H * (minH + rand() * (maxH - minH)));
        if (rand() < 0.14) h += Math.floor(H * 0.1);              // an occasional tower
        g.fillRect(x, H - h, w, h);
        if (rand() < 0.5 && w > 6) g.fillRect(x + 2, H - h - 2, w - 4, 2);   // stepped roof
        if (rand() < 0.16) g.fillRect(x + Math.floor(w / 2), H - h - 6, 1, 6); // antenna
        if (withWindows) {
          for (var wx = x + 1; wx < x + w - 1; wx += 3) {
            for (var wy = H - h + 3; wy < H - 2; wy += 4) {
              if (rand() < 0.55) windows.push({ x: wx, y: wy, delay: 0.6 + rand() * 9, flip: false });
            }
          }
        }
        x += w + (rand() < 0.3 ? 1 : 0);
      }
    }
    skyline(farLayer, col.city2, 0.13, 0.26, 4, 9, false);
    skyline(nearLayer, col.city, 0.07, 0.17, 7, 15, true);
  }

  function buildMoon() {
    var R = Math.max(6, Math.min(11, Math.round(H * 0.055)));
    var size = Math.ceil(R * 6);
    moon = layer(size, size);
    moon.R = R; moon.size = size;
    var img = moon.g.createImageData(size, size), d = img.data, c = size / 2;
    for (var y = 0; y < size; y++) {
      for (var x = 0; x < size; x++) {
        var dx = x - c + 0.5, dy = y - c + 0.5, dist = Math.sqrt(dx * dx + dy * dy), i = (y * size + x) * 4;
        var cx = dx - R * 0.5, cy = dy + R * 0.2, cut = Math.sqrt(cx * cx + cy * cy) < R * 0.92;
        if (dist <= R && !cut) {
          d[i] = col.moon[0]; d[i + 1] = col.moon[1]; d[i + 2] = col.moon[2]; d[i + 3] = 255;
        } else if (dist < R * 2.4) {
          var glow = Math.pow(1 - dist / (R * 2.4), 2) * 0.5;
          if (glow > (BAYER[y & 3][x & 3] + 0.5) / 16 * 0.55) {
            d[i] = col.moon[0]; d[i + 1] = col.moon[1]; d[i + 2] = col.moon[2]; d[i + 3] = 60;
          }
        }
      }
    }
    moon.g.putImageData(img, 0, 0);
  }

  function cloudSprite(w, rows) {
    var L = layer(w, rows * 2 + 1), g = L.g;
    for (var r = 0; r < rows; r++) {
      var inset = Math.floor((rows - 1 - r) * 2.5) + (r === 0 ? 3 : 0);
      g.fillStyle = r === rows - 1 ? str(col.cloud2) : str(col.cloud);
      g.fillRect(inset, r * 2, Math.max(2, w - inset * 2), 2);
    }
    L.w = w; L.h = rows * 2;
    return L;
  }

  function build() {
    var r = hero.getBoundingClientRect();
    W = Math.max(48, Math.ceil(r.width / PX));
    H = Math.max(48, Math.ceil(r.height / PX));
    canvas.width = W; canvas.height = H;
    readColors();

    var rand = seeded(20201026);
    buildSky();
    buildCity(rand);
    buildMoon();

    stars = [];
    var count = Math.round((W * H) / 700);
    for (var i = 0; i < count; i++) {
      stars.push({ x: Math.floor(rand() * W), y: Math.floor(rand() * H * 0.6), big: rand() < 0.16, phase: rand() * 8, speed: 0.4 + rand() * 1.2 });
    }
    clouds = [];
    for (var k = 0; k < 5; k++) {
      var w = 18 + Math.floor(rand() * 22);
      clouds.push({ sprite: cloudSprite(w, 3 + Math.floor(rand() * 2)), x: rand() * (W + 40) - 20, y: Math.floor(H * (0.26 + rand() * 0.34)), v: 1.2 + rand() * 2.4, depth: 0.6 + rand() * 0.8 });
    }
    draw(0);
  }

  /* ----- drawing ----- */
  function draw(t) {
    ctx.clearRect(0, 0, W, H);
    ctx.drawImage(skyLayer.canvas, 0, 0);

    if (showStars) {
      ctx.fillStyle = str(col.star);
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i], state = reduce ? 0 : Math.floor(t * s.speed + s.phase) % 4;
        if (state === 3) continue;
        ctx.globalAlpha = state === 2 ? 0.4 : 1;
        ctx.fillRect(s.x, s.y, 1, 1);
        if (s.big && state < 2) {
          ctx.fillRect(s.x - 1, s.y, 1, 1); ctx.fillRect(s.x + 1, s.y, 1, 1);
          ctx.fillRect(s.x, s.y - 1, 1, 1); ctx.fillRect(s.x, s.y + 1, 1, 1);
        }
      }
      ctx.globalAlpha = 1;
    }

    var mx = Math.round(W * 0.8 - moon.size / 2 + parallax * 1.5);
    var my = Math.round(Math.max(moon.R * 2.4, H * 0.2) - moon.size / 2);
    ctx.drawImage(moon.canvas, mx, my);

    ctx.globalAlpha = showStars ? 0.5 : 0.9;
    for (var c = 0; c < clouds.length; c++) {
      var cl = clouds[c];
      var cx = Math.round(((cl.x + (reduce ? 0 : t * cl.v)) % (W + cl.sprite.w + 20)) - cl.sprite.w + parallax * 3 * cl.depth);
      ctx.drawImage(cl.sprite.canvas, cx, cl.y);
    }
    ctx.globalAlpha = 1;

    ctx.drawImage(farLayer.canvas, 0, 0);
    ctx.drawImage(nearLayer.canvas, 0, 0);

    if (showWindows) {
      ctx.fillStyle = str(col.win);
      for (var w = 0; w < windows.length; w++) {
        var win = windows[w];
        var lit = reduce ? win.delay < 5.5 : t > win.delay;
        if (lit && !win.flip) ctx.fillRect(win.x, win.y, 1, 2);
      }
    }

    if (shoot) {
      for (var k = 0; k < 9; k++) {
        ctx.globalAlpha = Math.max(0, 1 - k / 9);
        ctx.fillStyle = str(col.star);
        ctx.fillRect(Math.round(shoot.x - shoot.vx * k * 0.35), Math.round(shoot.y - shoot.vy * k * 0.35), 1, 1);
      }
      ctx.globalAlpha = 1;
    }
  }

  /* ----- animation loop ----- */
  function tick(now) {
    raf = 0;
    if (!onScreen || document.hidden) return;
    if (now - lastFrame >= FRAME) {
      lastFrame = now;
      var t = (now - t0) / 1000;
      parallax += (pointer - parallax) * 0.12;

      if (shoot) {
        shoot.x += shoot.vx; shoot.y += shoot.vy; shoot.life--;
        if (shoot.life <= 0 || shoot.x < -10 || shoot.x > W + 10 || shoot.y > H) shoot = null;
      } else if (Math.random() < 0.004) {
        launch(Math.random() * W, Math.random() * H * 0.3);
      }
      if (windows.length && Math.random() < 0.35) {
        var one = windows[Math.floor(Math.random() * windows.length)];
        if (t > 10 && Math.random() < 0.5) one.flip = !one.flip;
      }
      draw(t);
    }
    schedule();
  }
  function schedule() { if (!raf) raf = requestAnimationFrame(tick); }
  function launch(x, y) {
    var dir = Math.random() < 0.5 ? -1 : 1;
    shoot = { x: x, y: y, vx: dir * (1.6 + Math.random()), vy: 0.9 + Math.random() * 0.5, life: 40 };
  }

  /* ----- events ----- */
  var resizeTimer;
  function rebuild() { clearTimeout(resizeTimer); resizeTimer = setTimeout(build, 120); }

  window.addEventListener('resize', rebuild);
  document.addEventListener('themechange', function () { build(); });
  if (window.ResizeObserver) new ResizeObserver(rebuild).observe(hero);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(rebuild);

  if (!reduce) {
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      pointer = ((e.clientX - r.left) / r.width - 0.5) * 2;
    });
    hero.addEventListener('pointerdown', function (e) {
      if (e.target.closest && e.target.closest('a, button, input')) return;
      var r = hero.getBoundingClientRect();
      launch((e.clientX - r.left) / PX, (e.clientY - r.top) / PX);
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        onScreen = entries[0].isIntersecting;
        if (onScreen) schedule();
      }).observe(hero);
    }
    document.addEventListener('visibilitychange', function () { if (!document.hidden) schedule(); });
  }

  build();
  if (!reduce) schedule();
}());
