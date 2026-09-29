#!/usr/bin/env python3
"""Générateur du site statique « navi ». Produit du HTML pur dans ./dist (aucune dépendance)."""
import json, os, re, shutil, sys, html
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "content"))
from h import esc  # noqa

BASE = "https://ouaisfieu.github.io/navi/"
SITE = "navi"
SITE_LONG = "navi — Géosociopolitique mondiale, focus Belgique"
TODAY = "2026-09-29"
PUBLISHED = "2026-09-29"
LANG = "fr-BE"
DIST = os.path.join(os.path.dirname(__file__), "dist")

SECTIONS = {
    "macro": {"name": "Macro · Monde", "short": "Macro", "slug": "monde/", "badge": "macro",
              "desc": "Le système-monde : ordre multipolaire, conflits, réarmement, économie, démocratie, climat, technologies."},
    "meso": {"name": "Méso · Europe & Belgique dans le monde", "short": "Méso", "slug": "meso/", "badge": "meso",
             "desc": "L'échelon intermédiaire : Union européenne, OTAN, diplomatie belge, niches stratégiques, partenariats régionaux."},
    "belgique": {"name": "Belgique · Institutions & économie", "short": "Belgique", "slug": "belgique/", "badge": "be",
                 "desc": "Le fédéralisme, les élections, les gouvernements, les finances publiques, l'économie, l'énergie et Bruxelles."},
    "micro": {"name": "Micro · Société & territoires", "short": "Micro", "slug": "micro/", "badge": "micro",
              "desc": "Le vécu : pouvoir d'achat, emploi, école, pensions, identités, sécurité, communes."},
    "ressources": {"name": "Ressources", "short": "Ressources", "slug": "ressources/", "badge": "res",
                   "desc": "Glossaire, chronologie, chiffres clés, vidéos, FAQ et bibliographie."},
}

AUTHOR = {
    "@type": "Person",
    "@id": BASE + "a-propos/#claude",
    "name": "Claude",
    "description": "Modèle d'intelligence artificielle développé par Anthropic, auteur des textes de ce site.",
    "url": BASE + "a-propos/",
    "affiliation": {"@type": "Organization", "name": "Anthropic", "url": "https://www.anthropic.com"},
    "sameAs": ["https://www.anthropic.com/claude"],
}
PUBLISHER = {
    "@type": "Organization",
    "@id": BASE + "#editeur",
    "name": "navi",
    "url": BASE,
    "logo": {"@type": "ImageObject", "url": BASE + "assets/logo.png", "width": 512, "height": 512},
}
LICENSE = "https://creativecommons.org/licenses/by-sa/4.0/deed.fr"

# ------------------------------------------------------------------ chargement du contenu
from pages_home import PAGES as P0          # noqa
from pages_macro import PAGES as P1         # noqa
from pages_meso import PAGES as P2          # noqa
from pages_belgique import PAGES as P3      # noqa
from pages_micro import PAGES as P4         # noqa
from pages_ressources import PAGES as P5    # noqa

PAGES = P0 + P1 + P2 + P3 + P4 + P5
BY_SLUG = {p["slug"]: p for p in PAGES}


def depth_prefix(slug):
    d = slug.count("/")
    return "../" * d if d else "./"


def strip_tags(s):
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def slugify(t):
    t = strip_tags(t).lower()
    rep = {"à": "a", "â": "a", "ä": "a", "é": "e", "è": "e", "ê": "e", "ë": "e", "î": "i", "ï": "i",
           "ô": "o", "ö": "o", "ù": "u", "û": "u", "ü": "u", "ç": "c", "œ": "oe", "’": "-", "'": "-"}
    for a, b in rep.items():
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:60]


def add_heading_ids(body):
    toc, seen = [], set()

    def rep(m):
        lvl, attrs, inner = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            hid = re.search(r'id="([^"]+)"', attrs).group(1)
        else:
            hid = slugify(inner)
            base, i = hid, 2
            while hid in seen:
                hid = f"{base}-{i}"; i += 1
            attrs = f' id="{hid}"' + attrs
        seen.add(hid)
        if lvl == "2":
            toc.append((hid, strip_tags(inner)))
        return f"<h{lvl}{attrs}>{inner}</h{lvl}>"

    body = re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", rep, body, flags=re.S)
    return body, toc


def reading_time(text):
    return max(1, round(len(text.split()) / 220))


def url_of(slug):
    return BASE + slug


# ------------------------------------------------------------------ schema.org
def breadcrumb_ld(p):
    items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE}]
    sec = SECTIONS.get(p.get("section"))
    if sec and p["slug"] != sec["slug"] and p["slug"]:
        items.append({"@type": "ListItem", "position": 2, "name": sec["name"], "item": url_of(sec["slug"])})
    if p["slug"]:
        items.append({"@type": "ListItem", "position": len(items) + 1, "name": p["h1"], "item": url_of(p["slug"])})
    return {"@type": "BreadcrumbList", "@id": url_of(p["slug"]) + "#fil", "itemListElement": items}


def about_ld(p):
    out = []
    for a in p.get("about", []):
        name, same = a[0], a[1] if len(a) > 1 else None
        typ = a[2] if len(a) > 2 else "Thing"
        d = {"@type": typ, "name": name}
        if same:
            d["sameAs"] = same if isinstance(same, list) else [same]
        out.append(d)
    return out


def page_ld(p, body_text, toc):
    url = url_of(p["slug"])
    website = {
        "@type": "WebSite", "@id": BASE + "#site", "url": BASE, "name": SITE, "alternateName": SITE_LONG,
        "description": "Encyclopédie ouverte de la géosociopolitique mondiale aux échelles macro, méso et micro, avec un focus sur la Belgique.",
        "inLanguage": LANG, "publisher": {"@id": BASE + "#editeur"},
        "potentialAction": {"@type": "SearchAction",
                            "target": {"@type": "EntryPoint", "urlTemplate": BASE + "recherche/?q={search_term_string}"},
                            "query-input": "required name=search_term_string"},
    }
    graph = [website, PUBLISHER, AUTHOR, breadcrumb_ld(p)]
    kind = p.get("kind", "article")
    common = {
        "@id": url + "#page", "url": url, "name": p["title"], "headline": p["h1"][:110],
        "description": p["desc"], "inLanguage": LANG, "isPartOf": {"@id": BASE + "#site"},
        "author": {"@id": AUTHOR["@id"]}, "publisher": {"@id": BASE + "#editeur"},
        "datePublished": PUBLISHED, "dateModified": p.get("updated", TODAY),
        "breadcrumb": {"@id": url + "#fil"}, "license": LICENSE,
        "image": BASE + "assets/og-image.png",
    }
    if p.get("about"):
        common["about"] = about_ld(p)
    if p.get("keywords"):
        common["keywords"] = ", ".join(p["keywords"])
    if kind in ("article",):
        art = {"@type": ["Article", "WebPage"] if False else "Article", **common,
               "mainEntityOfPage": url, "articleSection": SECTIONS.get(p.get("section"), {}).get("name", ""),
               "wordCount": len(body_text.split()), "timeRequired": f"PT{reading_time(body_text)}M",
               "educationalLevel": p.get("level_label", ""),
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".lede", "h1"]}}
        if p.get("sources"):
            art["citation"] = [{"@type": "CreativeWork", "name": t, "url": u} for t, u in p["sources"]]
        if toc:
            art["hasPart"] = [{"@type": "WebPageElement", "name": n, "url": f"{url}#{i}"} for i, n in toc]
        if not art["educationalLevel"]:
            del art["educationalLevel"]
        graph.append(art)
    elif kind in ("hub", "home"):
        cp = {"@type": "CollectionPage", **common}
        items = p.get("_children", [])
        if items:
            cp["mainEntity"] = {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": url_of(c["slug"]), "name": c["h1"]} for i, c in enumerate(items)]}
        graph.append(cp)
    elif kind == "about":
        graph.append({"@type": "AboutPage", **common, "mainEntity": {"@id": AUTHOR["@id"]}})
    elif kind == "search":
        graph.append({"@type": "SearchResultsPage", **common})
    elif kind == "sitemap":
        graph.append({"@type": "WebPage", **common})
    else:
        graph.append({"@type": "WebPage", **common})
    for extra in p.get("ld_extra", []):
        graph.append(extra)
    return {"@context": "https://schema.org", "@graph": graph}


# ------------------------------------------------------------------ gabarit
NAV = [("", "Accueil"), ("monde/", "Macro"), ("meso/", "Méso"), ("micro/", "Micro"),
       ("belgique/", "Belgique"), ("ressources/", "Ressources")]


def nav_html(p, pre):
    cur_sec = SECTIONS.get(p.get("section"), {}).get("slug")
    out = []
    for slug, label in NAV:
        active = (slug == p["slug"]) or (slug and slug == cur_sec)
        aria = ' aria-current="page"' if slug == p["slug"] else ""
        cls = ' class="active"' if active else ""
        out.append(f'<li><a href="{pre}{slug}"{cls}{aria}>{label}</a></li>')
    return "\n".join(out)


def crumbs_html(p, pre):
    if not p["slug"]:
        return ""
    parts = [f'<li><a href="{pre}">Accueil</a></li>']
    sec = SECTIONS.get(p.get("section"))
    if sec and p["slug"] != sec["slug"]:
        parts.append(f'<li><a href="{pre}{sec["slug"]}">{sec["name"]}</a></li>')
    parts.append(f'<li aria-current="page">{p["h1"]}</li>')
    return '<nav class="crumbs" aria-label="Fil d\'Ariane"><ol>' + "".join(parts) + "</ol></nav>"


def card(c, pre):
    sec = SECTIONS.get(c.get("section"), {})
    b = sec.get("badge", "res")
    return (f'<a class="card" href="{pre}{c["slug"]}"><span class="badge badge-{b}">{sec.get("short", "")}</span>'
            f'<h3>{c["h1"]}</h3><p>{c["desc"]}</p><span class="card-go" aria-hidden="true">Lire →</span></a>')


def render(p):
    pre = "/navi/" if p["slug"] == "404" else depth_prefix(p["slug"])
    body, toc = add_heading_ids(p.get("body", ""))
    body_text = strip_tags(body)
    kind = p.get("kind", "article")
    sec = SECTIONS.get(p.get("section"), {})
    badge = sec.get("badge", "res")

    # enfants des hubs
    children_html = ""
    if kind in ("hub",) and p.get("_children"):
        children_html = '<section class="cards" aria-label="Dossiers de la rubrique">' + "".join(card(c, pre) for c in p["_children"]) + "</section>"

    toc_html = ""
    if kind == "article" and len(toc) >= 3:
        toc_html = ('<nav class="toc" aria-label="Sommaire"><details open><summary>Sommaire</summary><ol>'
                    + "".join(f'<li><a href="#{i}">{esc(n)}</a></li>' for i, n in toc) + "</ol></details></nav>")

    meta_html = ""
    if kind in ("article", "hub", "about"):
        rt = reading_time(body_text)
        meta_html = (f'<p class="meta">Par <a href="{pre}a-propos/" rel="author">Claude</a> (IA, Anthropic) · '
                     f'<time datetime="{p.get("updated", TODAY)}">mis à jour le 29 septembre 2026</time> · '
                     f'{rt} min de lecture</p>')

    related_html = ""
    if p.get("related"):
        rel = [BY_SLUG[s] for s in p["related"] if s in BY_SLUG]
        related_html = '<section class="related" aria-labelledby="a-lire"><h2 id="a-lire">À lire aussi</h2><div class="cards cards-sm">' + "".join(card(c, pre) for c in rel) + "</div></section>"

    sources_html = ""
    if p.get("sources"):
        sources_html = ('<section class="sources" aria-labelledby="sources"><h2 id="sources">Sources principales</h2><ol>'
                        + "".join(f'<li><a href="{esc(u)}" rel="noopener external">{t}</a></li>' for t, u in p["sources"])
                        + '</ol><p class="small">Chiffres et faits croisés à partir des dossiers du projet et de recherches complémentaires ; '
                          f'voir la <a href="{pre}ressources/sources/">bibliographie complète</a> et la <a href="{pre}a-propos/#methode">méthode</a>.</p></section>')

    body = body.replace('href="@/', f'href="{pre}')
    ld = json.dumps(page_ld(p, body_text, toc), ensure_ascii=False, indent=1)
    canonical = url_of(p["slug"])
    title_full = p["title"] if p["slug"] == "" else f'{p["title"]} · {SITE}'
    robots = p.get("robots", "index, follow, max-image-preview:large, max-snippet:-1")
    kw = ", ".join(p.get("keywords", []))
    lede = f'<p class="lede">{p["lede"]}</p>' if p.get("lede") else ""
    hero_cls = " hero-home" if kind == "home" else ""
    level_badge = f'<span class="badge badge-{badge}">{sec.get("name", "")}</span>' if sec else ""

    return f"""<!doctype html>
<html lang="{LANG}" data-theme="dark" prefix="og: https://ogp.me/ns#">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title_full)}</title>
<meta name="description" content="{esc(p['desc'])}">
{f'<meta name="keywords" content="{esc(kw)}">' if kw else ''}
<meta name="author" content="Claude (Anthropic)">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="fr" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta name="theme-color" content="#0f1412" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#0f1412">
<meta name="color-scheme" content="dark light">
<meta property="og:type" content="{'website' if kind in ('home', 'hub') else 'article'}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="fr_BE">
<meta property="og:title" content="{esc(p['h1'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="navi — géosociopolitique mondiale, focus Belgique">
{f'<meta property="article:published_time" content="{PUBLISHED}"><meta property="article:modified_time" content="{p.get("updated", TODAY)}"><meta property="article:section" content="{esc(sec.get("name", ""))}">' if kind == 'article' else ''}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p['h1'])}">
<meta name="twitter:description" content="{esc(p['desc'])}">
<meta name="twitter:image" content="{BASE}assets/og-image.png">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}assets/logo.png">
<link rel="manifest" href="{pre}site.webmanifest">
<link rel="sitemap" type="application/xml" href="{pre}sitemap.xml">
<link rel="alternate" type="application/atom+xml" title="navi — mises à jour" href="{pre}feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{pre}assets/style.css">
<script>try{{var t=localStorage.getItem('navi-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<script type="application/ld+json">
{ld}
</script>
</head>
<body class="k-{kind}">
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
 <div class="wrap hdr">
  <a class="brand" href="{pre}" aria-label="navi, accueil"><img src="{pre}assets/favicon.svg" alt="" width="28" height="28"><span>navi</span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-principale">Menu</button>
  <nav id="nav-principale" class="nav" aria-label="Navigation principale"><ul>
{nav_html(p, pre)}
  </ul></nav>
  <div class="tools">
   <a class="icon-btn" href="{pre}recherche/" aria-label="Rechercher"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="m20 20-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
   <button class="icon-btn theme-btn" type="button" aria-label="Basculer le thème clair ou sombre"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z" fill="currentColor"/></svg></button>
  </div>
 </div>
</header>
<main id="contenu" class="wrap">
{crumbs_html(p, pre)}
<article class="page page-{kind}" >
<header class="page-head{hero_cls}">
{level_badge if kind != 'home' else ''}
<h1>{p['h1']}</h1>
{lede}
{meta_html}
</header>
{toc_html}
<div class="prose">
{body}
</div>
{children_html}
{sources_html}
{related_html}
</article>
</main>
<footer class="site-footer">
 <div class="wrap foot">
  <div>
   <p class="brand-foot"><img src="{pre}assets/favicon.svg" alt="" width="22" height="22"> navi</p>
   <p class="small">Encyclopédie indépendante de la géosociopolitique mondiale — échelles macro, méso et micro, focus Belgique. Textes rédigés par Claude (IA, Anthropic) à partir de sources publiques citées ; éditeur anonyme.</p>
   <p class="small">Contenus sous licence <a href="{LICENSE}" rel="license noopener">CC BY-SA 4.0</a>. État des connaissances : septembre 2026.</p>
  </div>
  <nav aria-label="Pied de page"><ul class="foot-links">
   <li><a href="{pre}monde/">Macro · Monde</a></li><li><a href="{pre}meso/">Méso · Europe</a></li>
   <li><a href="{pre}micro/">Micro · Société</a></li><li><a href="{pre}belgique/">Belgique</a></li>
   <li><a href="{pre}ressources/glossaire/">Glossaire</a></li><li><a href="{pre}ressources/chronologie/">Chronologie</a></li>
   <li><a href="{pre}ressources/sources/">Sources</a></li><li><a href="{pre}a-propos/">À propos &amp; méthode</a></li>
   <li><a href="{pre}plan-du-site/">Plan du site</a></li><li><a href="{pre}feed.xml">Flux Atom</a></li>
  </ul></nav>
 </div>
</footer>
<script src="{pre}assets/site.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------ sorties annexes
def write(path, content, mode="w"):
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, mode, encoding=None if "b" in mode else "utf-8") as f:
        f.write(content)


def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(os.path.dirname(__file__), "assets"), os.path.join(DIST, "assets"))

    # enfants des hubs
    order = {p["slug"]: i for i, p in enumerate(PAGES)}
    for p in PAGES:
        if p.get("kind") == "hub":
            sec = p["section"]
            p["_children"] = [c for c in PAGES if c.get("section") == sec and c["slug"] != p["slug"]
                              and c.get("kind") not in ("hub",) and not c.get("hidden")]
        if p.get("kind") == "home":
            p["_children"] = [BY_SLUG[s["slug"]] for s in SECTIONS.values()]

    # plan du site : rempli dynamiquement
    if "plan-du-site/" in BY_SLUG:
        sm = BY_SLUG["plan-du-site/"]
        parts = []
        for key, s in SECTIONS.items():
            items = [c for c in PAGES if c.get("section") == key]
            parts.append(f'<h2>{s["name"]}</h2><ul>' + "".join(f'<li><a href="@/{c["slug"]}">{c["h1"]}</a> — {c["desc"]}</li>' for c in items) + "</ul>")
        other = [c for c in PAGES if not c.get("section") and c["slug"] != "404"]
        parts.append("<h2>Autres pages</h2><ul>" + "".join(f'<li><a href="@/{c["slug"]}">{c["h1"]}</a></li>' for c in other) + "</ul>")
        sm["body"] = "\n".join(parts)

    if "ressources/sources/" in BY_SLUG:
        bib = BY_SLUG["ressources/sources/"]
        parts, seen = [], set()
        total = 0
        for key, s in SECTIONS.items():
            items = []
            for c in PAGES:
                if c.get("section") != key:
                    continue
                for t, u in c.get("sources", []):
                    if u in seen:
                        continue
                    seen.add(u); items.append((t, u, c))
            if items:
                total += len(items)
                parts.append(f'<h2>{s["name"]}</h2><ol>' + "".join(
                    f'<li><a href="{esc(u)}" rel="noopener external">{t}</a> <span class="small">— cité dans <a href="@/{c["slug"]}">{c["h1"]}</a></span></li>' for t, u, c in items) + "</ol>")
        bib["body"] = f"<p>{total} sources uniques, dédoublonnées. Les dossiers de recherche d'origine comptent plusieurs centaines de références supplémentaires.</p>" + "\n".join(parts)

    for p in PAGES:
        out = render(p)
        path = (p["slug"] + "index.html") if p["slug"] != "404" else "404.html"
        write(path, out)

    # sitemap
    urls = []
    for p in PAGES:
        if p.get("robots", "").startswith("noindex") or p["slug"] == "404":
            continue
        pr = "1.0" if p["slug"] == "" else ("0.8" if p.get("kind") == "hub" else "0.7")
        urls.append(f"<url><loc>{url_of(p['slug'])}</loc><lastmod>{p.get('updated', TODAY)}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    write(".nojekyll", "")

    # flux Atom
    entries = []
    for p in PAGES:
        if p.get("kind") != "article":
            continue
        entries.append(f"""<entry><title>{esc(p['h1'])}</title><link href="{url_of(p['slug'])}"/><id>{url_of(p['slug'])}</id>
<updated>{p.get('updated', TODAY)}T12:00:00+02:00</updated><summary>{esc(p['desc'])}</summary><author><name>Claude (Anthropic)</name></author></entry>""")
    write("feed.xml", f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="fr-BE">
<title>{SITE_LONG}</title><link href="{BASE}"/><link rel="self" href="{BASE}feed.xml"/><id>{BASE}</id>
<updated>{TODAY}T12:00:00+02:00</updated>
{chr(10).join(entries)}
</feed>
""")

    # index de recherche
    idx = []
    for p in PAGES:
        if p["slug"] in ("404", "recherche/"):
            continue
        body, _ = add_heading_ids(p.get("body", ""))
        idx.append({"u": p["slug"], "t": p["h1"], "d": p["desc"],
                    "s": SECTIONS.get(p.get("section"), {}).get("short", ""),
                    "k": " ".join(p.get("keywords", [])), "x": strip_tags(body)[:6000]})
    write("assets/search-index.json", json.dumps(idx, ensure_ascii=False))

    write("site.webmanifest", json.dumps({
        "name": SITE_LONG, "short_name": SITE, "lang": "fr-BE", "start_url": "./", "display": "standalone",
        "background_color": "#0f1412", "theme_color": "#0f1412",
        "icons": [{"src": "assets/logo.png", "sizes": "512x512", "type": "image/png"},
                  {"src": "assets/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, ensure_ascii=False, indent=1))
    print(f"{len(PAGES)} pages générées dans {DIST}")


if __name__ == "__main__":
    build()
