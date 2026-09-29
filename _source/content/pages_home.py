from h import L, kpis, callout, video, levels
from pages_ressources import VIDEOS, video_ld

BASE = "https://ouaisfieu.github.io/navi/"

HOME_BODY = f"""
<form class="home-search" action="recherche/" method="get" role="search">
 <label class="sr" for="hq" style="position:absolute;left:-9999px">Rechercher sur navi</label>
 <input id="hq" name="q" type="search" placeholder="Rechercher : Euroclear, fédéralisme, SIPRI, indexation…" autocomplete="off">
 <button class="btn" type="submit">Rechercher</button>
</form>

<h2>Trois échelles, un même monde</h2>
<div class="home-levels">
 <a class="lvl" href="@/monde/"><span class="badge badge-macro">Macro</span><h3>Le système-monde</h3><p>Polycrise, ordre multipolaire, dix conflits majeurs, réarmement record, recul démocratique, limites planétaires, IA et quantique.</p></a>
 <a class="lvl" href="@/meso/"><span class="badge badge-meso">Méso</span><h3>L'Europe et la Belgique dans le monde</h3><p>UE, OTAN, diplomatie fédérale, Euroclear, imec, Grands Lacs, droit international, soft power.</p></a>
 <a class="lvl" href="@/micro/"><span class="badge badge-micro">Micro</span><h3>Société et territoires</h3><p>Pouvoir d'achat, emploi, école, pensions, identités, narcotrafic, cybersécurité, communes.</p></a>
 <a class="lvl" href="@/belgique/"><span class="badge badge-be">Focus</span><h3>La Belgique en 2026</h3><p>Fédéralisme, élections 2024, coalition Arizona, finances publiques, économie, énergie, Bruxelles.</p></a>
</div>

{kpis([("2 887 Md$", "dépenses militaires mondiales en 2025"), ("74 %", "de l'humanité en autocratie"), ("7 / 9", "limites planétaires franchies"), ("107,4 %", "dette publique belge / PIB (2025)"), ("≈ 210 Md€", "d'avoirs russes gelés à Bruxelles"), ("613 j", "de blocage à Bruxelles")])}

<h2>Pourquoi la Belgique ?</h2>
<p>Petit pays de 11,9 millions d'habitants, la Belgique concentre sur son territoire presque toutes les lignes de faille du monde contemporain : sièges de l'Union européenne et de l'OTAN, avoirs russes gelés chez {L("meso/euroclear-avoirs-russes/", "Euroclear")}, recherche mondiale sur les puces à l'{L("meso/niches-strategiques/", "imec")}, port d'Anvers devenu porte d'entrée de la cocaïne, {L("belgique/federalisme/", "fédéralisme")} à six parlements, {L("belgique/finances-publiques/", "procédure pour déficit excessif")} et réarmement accéléré. C'est un laboratoire idéal pour observer comment les forces mondiales atterrissent dans une société.</p>
{levels("Ce qui se joue entre puissances, marchés et écosystèmes.", "Ce que les institutions — UE, OTAN, État fédéral, Régions — en font.", "Ce que les citoyens vivent : salaires, emploi, école, sécurité, confiance.")}

<h2>Par où commencer ?</h2>
<ul>
<li>{L("monde/polycrise/", "La polycrise, grille de lecture du monde en 2026")}</li>
<li>{L("belgique/gouvernements/", "Qui gouverne la Belgique ?")}</li>
<li>{L("meso/euroclear-avoirs-russes/", "Euroclear et les avoirs russes : le dilemme belge")}</li>
<li>{L("micro/pouvoir-d-achat/", "L'indexation en centimes expliquée")}</li>
<li>{L("ressources/chiffres-cles/", "Tous les chiffres clés")} · {L("ressources/glossaire/", "Glossaire")} · {L("ressources/chronologie/", "Chronologie")}</li>
</ul>

<h2>En vidéo</h2>
<div class="video-grid">
{"".join(video(v, n, d) for v, n, d in VIDEOS)}
</div>

{callout("<p>Textes rédigés par Claude, modèle d'IA d'Anthropic, à partir de dossiers de recherche et de sources publiques citées en bas de chaque page. Éditeur anonyme. État des connaissances : fin septembre 2026. " + L("a-propos/", "Méthode et transparence") + ".</p>", "lilac", "Qui écrit ?")}
"""

PAGES = [
{
 "slug": "", "kind": "home",
 "title": "navi — Géosociopolitique mondiale macro, méso, micro · focus Belgique",
 "h1": "Comprendre le monde, de la planète à la commune",
 "desc": "Encyclopédie ouverte de la géosociopolitique mondiale en 2026 aux échelles macro, méso et micro, avec un focus sur la Belgique : conflits, économie, démocratie, climat, institutions, société.",
 "lede": "navi relie les grandes forces qui recomposent le monde en 2026 à ce qu'elles changent en Europe, en Belgique et dans la vie quotidienne.",
 "keywords": ["géosociopolitique", "géopolitique 2026", "Belgique", "macro méso micro", "encyclopédie"],
 "about": [("Géopolitique", "https://fr.wikipedia.org/wiki/G%C3%A9opolitique"), ("Belgique", "https://www.wikidata.org/wiki/Q31", "Country")],
 "body": HOME_BODY,
 "ld_extra": [video_ld(v, n, d, "") for v, n, d in VIDEOS],
},
{
 "slug": "a-propos/", "kind": "about",
 "title": "À propos, méthode et transparence",
 "h1": "À propos de navi",
 "desc": "Qui écrit navi, comment les contenus sont produits et vérifiés, licence, limites et contact.",
 "lede": "navi est une encyclopédie indépendante et gratuite. Voici comment elle est faite.",
 "keywords": ["à propos", "méthode", "transparence", "IA"],
 "body": f"""
<h2 id="auteur">L'auteur : Claude</h2>
<p>Les textes de navi sont rédigés par <strong>Claude</strong>, un modèle d'intelligence artificielle développé par <a href="https://www.anthropic.com" rel="noopener">Anthropic</a>. L'éditeur du site a choisi de rester anonyme ; il a défini le projet, fourni des dossiers de recherche et décide de la publication.</p>
<h2 id="methode">Méthode</h2>
<ol>
<li><strong>Dossiers de base</strong> : cinq rapports de recherche sur la situation géopolitique mondiale en 2026, le panorama des menaces, la Belgique dans l'ordre mondial et la géosociopolitique belge.</li>
<li><strong>Recherche complémentaire</strong> : vérification et actualisation de points clés (gouvernement bruxellois, population, négociations en Ukraine, mobilisations sociales) à partir de sources publiques en septembre 2026.</li>
<li><strong>Croisement</strong> : les chiffres divergents entre sources sont signalés ou attribués (« selon… »). Les évaluations contestées (par exemple les classements de V-Dem) sont présentées comme telles.</li>
<li><strong>Structure multi-échelle</strong> : chaque dossier situe son sujet aux niveaux macro, méso et micro.</li>
</ol>
<h2 id="limites">Limites</h2>
<ul>
<li>Un modèle d'IA peut commettre des erreurs : vérifiez les chiffres importants auprès des sources primaires citées.</li>
<li>Certaines sources des dossiers de base sont secondaires (presse, synthèses) ; les sources officielles sont privilégiées quand elles existent.</li>
<li>Les données évoluent : l'état des connaissances est celui de fin septembre 2026.</li>
</ul>
<h2 id="neutralite">Neutralité</h2>
<p>navi n'est affilié à aucun parti, gouvernement ou groupe d'intérêt. Sur les sujets disputés, le site présente les arguments des différentes parties et attribue les jugements à leurs auteurs.</p>
<h2 id="licence">Licence</h2>
<p>Les textes sont publiés sous licence <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" rel="license noopener">Creative Commons BY-SA 4.0</a>. Les vidéos intégrées restent la propriété de leurs auteurs.</p>
<h2 id="vie-privee">Vie privée</h2>
<p>Aucun traceur, aucun cookie publicitaire, aucune mesure d'audience. Les polices sont chargées depuis Google Fonts. Les vidéos YouTube ne se chargent qu'au clic, depuis le domaine youtube-nocookie.com. Le choix de thème (clair/sombre) est mémorisé localement dans votre navigateur.</p>
<h2 id="technique">Technique</h2>
<p>Site statique en HTML pur (approche JAMstack), hébergé sur GitHub Pages. Données structurées schema.org en JSON-LD sur chaque page (Article, CollectionPage, BreadcrumbList, DefinedTermSet, FAQPage, VideoObject), plan du site XML, flux Atom, recherche plein texte côté client, accessibilité (navigation clavier, contrastes, lien d'évitement).</p>
""",
},
{
 "slug": "recherche/", "kind": "search",
 "title": "Recherche",
 "h1": "Rechercher sur navi",
 "desc": "Recherche plein texte dans tous les dossiers de navi.",
 "lede": "Tapez un mot-clé : un pays, une institution, un concept.",
 "robots": "noindex, follow",
 "body": """
<form id="search-form" class="search-box" role="search">
 <label for="q" style="position:absolute;left:-9999px">Terme recherché</label>
 <input id="q" name="q" type="search" placeholder="Ex. Euroclear, tronc commun, New START…" autocomplete="off" autofocus>
 <button class="btn" type="submit">Chercher</button>
</form>
<p id="count" class="small" aria-live="polite"></p>
<ol id="results" class="results"></ol>
<noscript><p>La recherche nécessite JavaScript. Consultez le <a href="@/plan-du-site/">plan du site</a>.</p></noscript>
""",
},
{
 "slug": "plan-du-site/", "kind": "sitemap",
 "title": "Plan du site",
 "h1": "Plan du site",
 "desc": "Toutes les pages de navi, par rubrique.",
 "body": "",
},
{
 "slug": "404", "kind": "notfound",
 "title": "Page introuvable",
 "h1": "Page introuvable",
 "desc": "Cette page n'existe pas ou a été déplacée.",
 "robots": "noindex, follow",
 "body": '<p>Cette page n\'existe pas ou a été déplacée. Essayez la <a href="/navi/recherche/">recherche</a> ou revenez à l\'<a href="/navi/">accueil</a>.</p>',
},
]
