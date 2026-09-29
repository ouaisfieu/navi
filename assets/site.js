/* navi — scripts légers (thème, menu, vidéos, recherche). Aucun traceur. */
(function () {
  var root = document.documentElement;

  // Thème : sombre par défaut, choix mémorisé si possible
  var tb = document.querySelector('.theme-btn');
  if (tb) tb.addEventListener('click', function () {
    var next = root.dataset.theme === 'light' ? 'dark' : 'light';
    root.dataset.theme = next;
    try { localStorage.setItem('navi-theme', next); } catch (e) {}
  });

  // Menu mobile
  var mb = document.querySelector('.menu-btn'), nav = document.getElementById('nav-principale');
  if (mb && nav) mb.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    mb.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Vidéos YouTube : façade légère, lecteur chargé au clic (youtube-nocookie)
  document.querySelectorAll('.yt').forEach(function (el) {
    var btn = el.querySelector('.yt-play');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + el.dataset.id + '?autoplay=1&rel=0';
      f.title = el.dataset.title || 'Vidéo YouTube';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      f.allowFullscreen = true;
      f.loading = 'lazy';
      f.referrerPolicy = 'strict-origin-when-cross-origin';
      el.innerHTML = '';
      el.appendChild(f);
    });
  });

  // Recherche plein texte côté client
  var box = document.getElementById('q'), out = document.getElementById('results');
  if (!box || !out) return;
  var base = document.body.dataset.base || '../';
  var data = null;
  function norm(s) { return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function snippet(text, terms) {
    var n = norm(text), pos = -1;
    for (var i = 0; i < terms.length && pos < 0; i++) pos = n.indexOf(terms[i]);
    var start = Math.max(0, pos - 80), s = text.substr(start, 240);
    s = esc((start ? '… ' : '') + s + ' …');
    terms.forEach(function (t) {
      if (t.length < 3) return;
      s = s.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi'), '<mark>$1</mark>');
    });
    return s;
  }
  function run() {
    var q = box.value.trim();
    var terms = norm(q).split(/\s+/).filter(function (t) { return t.length > 1; });
    if (!terms.length) { out.innerHTML = ''; return; }
    var res = data.map(function (d) {
      var t = norm(d.t), dd = norm(d.d), k = norm(d.k), x = norm(d.x), score = 0;
      for (var i = 0; i < terms.length; i++) {
        var w = terms[i], hit = 0;
        if (t.indexOf(w) >= 0) hit += 10;
        if (k.indexOf(w) >= 0) hit += 6;
        if (dd.indexOf(w) >= 0) hit += 4;
        var c = x.split(w).length - 1; hit += Math.min(c, 8);
        if (!hit) return null;
        score += hit;
      }
      return { d: d, s: score };
    }).filter(Boolean).sort(function (a, b) { return b.s - a.s; }).slice(0, 30);
    out.innerHTML = res.length ? res.map(function (r) {
      return '<li><span class="badge badge-res">' + esc(r.d.s || 'navi') + '</span> <a href="' + base + r.d.u + '">' + esc(r.d.t) + '</a><p>' + snippet(r.d.x || r.d.d, norm(q).split(/\s+/)) + '</p></li>';
    }).join('') : '<li>Aucun résultat pour « ' + esc(q) + ' ». Essayez un autre terme (ex. Euroclear, fédéralisme, SIPRI).</li>';
    document.getElementById('count').textContent = res.length + ' résultat' + (res.length > 1 ? 's' : '');
  }
  fetch(base + 'assets/search-index.json').then(function (r) { return r.json(); }).then(function (j) {
    data = j;
    var p = new URLSearchParams(location.search).get('q');
    if (p) { box.value = p; run(); }
    box.addEventListener('input', run);
  });
  var form = document.getElementById('search-form');
  if (form) form.addEventListener('submit', function (e) { e.preventDefault(); run(); history.replaceState(null, '', '?q=' + encodeURIComponent(box.value)); });
})();
