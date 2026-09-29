# navi — Géosociopolitique mondiale, focus Belgique

Site statique en HTML pur (JAMstack, aucune étape de build nécessaire pour le déployer).
Textes rédigés par Claude (IA, Anthropic) · éditeur anonyme · licence CC BY-SA 4.0.

## Déployer sur GitHub Pages
1. Copier le contenu de ce dossier à la racine du dépôt `ouaisfieu/navi` (branche `main`).
2. Settings → Pages → Source : « Deploy from a branch » → `main` / `/ (root)`.
3. Le site sera servi à https://ouaisfieu.github.io/navi/ (URL canonique utilisée partout).
   Si tu utilises un domaine personnalisé, remplacer `https://ouaisfieu.github.io/navi/` et `/navi/`
   dans les fichiers (ou modifier `BASE` dans `_source/build.py` et régénérer).

## Contenu
- 48 pages : accueil, 4 rubriques (Macro, Méso, Belgique, Micro) + Ressources, 34 dossiers,
  glossaire, chronologie, chiffres clés, vidéos, FAQ, bibliographie, recherche, plan du site, 404.
- SEO : balises title/description/canonical, Open Graph, Twitter Cards, sitemap.xml, robots.txt, flux Atom.
- Web sémantique : JSON-LD schema.org sur chaque page (WebSite + SearchAction, Organization, Person,
  Article, CollectionPage/ItemList, BreadcrumbList, DefinedTermSet, FAQPage, VideoObject), liens sameAs Wikidata/Wikipédia.
- Mode sombre par défaut (bouton pour le mode clair, choix mémorisé), vidéos YouTube en mode nocookie chargées au clic.

## À compléter
- Titres exacts des deux vidéos YouTube (actuellement « Vidéo complémentaire n° 1/2 ») :
  `_source/content/pages_ressources.py` → `VIDEOS`, puis `python3 _source/build.py`.

## Mettre à jour (optionnel)
Le dossier `_source/` contient le générateur Python (sans dépendance) qui a produit ce HTML.
`cd _source && python3 build.py` régénère le site dans `_source/dist/` ; copier ensuite ce contenu à la racine.
