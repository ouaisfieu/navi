from h import L, kpis, bars, table, callout, video, esc

W = "https://fr.wikipedia.org/wiki/"
S = "ressources"
BASE = "https://ouaisfieu.github.io/navi/"

VIDEOS = [
    ("sMV9qZBg5Ds", "Vidéo complémentaire n° 1", "Première vidéo sélectionnée pour approfondir la géosociopolitique contemporaine."),
    ("R1MYxVzdZ6o", "Vidéo complémentaire n° 2", "Seconde vidéo sélectionnée pour approfondir les enjeux abordés sur navi."),
]


def video_ld(vid, name, desc, page):
    return {"@type": "VideoObject", "@id": BASE + page + "#video-" + vid, "name": name, "description": desc,
            "thumbnailUrl": [f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"],
            "embedUrl": f"https://www.youtube-nocookie.com/embed/{vid}",
            "contentUrl": f"https://www.youtube.com/watch?v={vid}", "inLanguage": "fr"}


GLOSS = [
 ("Accord de coopération", "Convention entre l'État fédéral et/ou des entités fédérées pour gérer ensemble une compétence partagée. Outil central du fédéralisme belge.", "belgique/federalisme/"),
 ("Arizona (coalition)", "Gouvernement fédéral belge formé le 3 février 2025 autour de Bart De Wever : N-VA, MR, Les Engagés, Vooruit, CD&V. Nom tiré des couleurs du drapeau de l'Arizona.", "belgique/gouvernements/"),
 ("ASAT", "Arme antisatellite : missile, satellite « tueur », laser ou brouillage visant à neutraliser des satellites.", "monde/rearmement-nucleaire/"),
 ("Autocratisation", "Processus de dégradation des institutions démocratiques (V-Dem) : concentration du pouvoir exécutif, atteintes aux médias, aux juges et à la société civile.", "monde/democratie/"),
 ("BeNeSam", "Coopération navale belgo-néerlandaise : états-majors fusionnés sous l'« Amiral Benelux », répartition des spécialités.", "meso/otan-defense/"),
 ("Boule de neige (effet)", "Situation où le taux d'intérêt moyen sur la dette dépasse la croissance nominale : la dette augmente mécaniquement.", "belgique/finances-publiques/"),
 ("BRICS", "Groupe de pays émergents (Brésil, Russie, Inde, Chine, Afrique du Sud) élargi depuis 2024 à l'Égypte, l'Éthiopie, l'Iran, les Émirats, l'Arabie saoudite, l'Indonésie…", "monde/ordre-multipolaire/"),
 ("Budget carbone", "Quantité de CO₂ encore émissible pour rester sous un seuil de réchauffement avec une probabilité donnée.", "monde/climat-limites-planetaires/"),
 ("CaMo", "Capacité motorisée : partenariat stratégique franco-belge pour l'armée de terre (Griffon, Jaguar, doctrine commune).", "meso/otan-defense/"),
 ("Clause dérogatoire nationale", "Flexibilité des règles budgétaires de l'UE (2025-2028) permettant d'exclure une partie des dépenses de défense des objectifs de déficit.", "meso/union-europeenne/"),
 ("Communauté", "En Belgique, entité fédérée compétente pour les matières liées aux personnes : enseignement, culture, aide aux personnes. Il y en a trois.", "belgique/federalisme/"),
 ("Confédéralisme", "Projet porté par la N-VA : les entités fédérées deviennent le centre de gravité et ne délèguent au niveau belge que ce qu'elles choisissent.", "belgique/federalisme/"),
 ("Cordon sanitaire", "Accord entre partis belges pour ne pas gouverner avec l'extrême droite (Vlaams Belang) ; il existe aussi un cordon médiatique côté francophone.", "belgique/elections-2024/"),
 ("CRINK", "Acronyme désignant l'alignement Chine-Russie-Iran-Corée du Nord.", "monde/ordre-multipolaire/"),
 ("Dédollarisation", "Réduction de la dépendance au dollar américain dans les échanges, les réserves et les paiements.", "monde/ordre-multipolaire/"),
 ("Euroclear", "Dépositaire central de titres basé à Bruxelles, où sont immobilisés environ 210 milliards d'euros d'avoirs de la Banque centrale russe.", "meso/euroclear-avoirs-russes/"),
 ("ETS2", "Second système européen d'échange de quotas d'émission, couvrant chauffage et transport routier.", "belgique/energie-climat/"),
 ("Fédération Wallonie-Bruxelles (FWB)", "Nom usuel de la Communauté française de Belgique.", "micro/ecole/"),
 ("Géoéconomie", "Usage d'instruments économiques (commerce, finance, technologie, matières premières) à des fins de puissance.", "monde/geoeconomie/"),
 ("In foro interno, in foro externo", "Principe selon lequel une entité fédérée compétente en interne l'est aussi sur la scène internationale, y compris pour conclure des traités.", "meso/diplomatie-belge/"),
 ("Indexation en centimes", "Plafonnement temporaire de l'indexation belge : la part du salaire au-delà de 4 000 € bruts n'est plus indexée pendant deux cycles.", "micro/pouvoir-d-achat/"),
 ("Limites planétaires", "Neuf processus biophysiques dont le franchissement menace la stabilité du système Terre ; sept sont dépassés.", "monde/climat-limites-planetaires/"),
 ("Loi spéciale de financement (LSF)", "Loi de 1989 qui organise le financement des Régions et Communautés.", "belgique/finances-publiques/"),
 ("mBridge", "Plateforme de règlements transfrontaliers en monnaies numériques de banques centrales, née sous l'égide de la BRI.", "monde/ordre-multipolaire/"),
 ("NIS2", "Directive européenne sur la cybersécurité des entités essentielles et importantes.", "micro/securite-cyber/"),
 ("Norme salariale", "Marge maximale d'évolution des salaires en Belgique, fixée par la loi de 1996 ; 0 % pour 2025-2026.", "micro/pouvoir-d-achat/"),
 ("Partage nucléaire", "Dispositif de l'OTAN où des alliés non nucléaires hébergent des armes américaines et entraînent des avions pour les emporter.", "meso/otan-defense/"),
 ("Polycrise", "Enchevêtrement causal de crises au sein de systèmes interdépendants, avec boucles de rétroaction.", "monde/polycrise/"),
 ("Procédure pour déficit excessif (PDE)", "Procédure de l'UE visant un État dont le déficit dépasse 3 % du PIB ; ouverte contre la Belgique en juillet 2024.", "belgique/finances-publiques/"),
 ("Q-Day", "Jour hypothétique où un ordinateur quantique pourra casser la cryptographie à clé publique actuelle.", "monde/technologies/"),
 ("Région", "En Belgique, entité fédérée territoriale : Flandre, Wallonie, Bruxelles-Capitale.", "belgique/federalisme/"),
 ("Soft power", "Capacité d'influence par l'attraction (culture, valeurs, réputation) plutôt que par la contrainte.", "meso/soft-power/"),
 ("Team Belgium", "Coordination des acteurs fédéraux et régionaux de la diplomatie économique belge.", "meso/diplomatie-belge/"),
 ("Zone grise", "Actions hostiles sous le seuil du conflit armé : sabotage déniable, désinformation, pressions économiques.", "monde/infrastructures-critiques/"),
]


def gloss_body():
    letters = sorted({g[0][0].upper() for g in GLOSS})
    out = ['<nav class="alpha" aria-label="Index alphabétique">' + "".join(f'<a href="#lettre-{l}">{l}</a>' for l in letters) + "</nav>"]
    out.append('<dl class="gloss">')
    cur = None
    from build_helpers import slug as _s  # type: ignore
    for term, d, link in GLOSS:
        l0 = term[0].upper()
        anchor = f' data-letter="{l0}"' if l0 != cur else ""
        extra = f'<span id="lettre-{l0}"></span>' if l0 != cur else ""
        cur = l0
        out.append(f'<dt id="{_s(term)}"{anchor}>{extra}{esc(term)}</dt><dd>{esc(d)} {L(link, "En savoir plus")}.</dd>')
    out.append("</dl>")
    return "\n".join(out)


def gloss_ld():
    from build_helpers import slug as _s  # type: ignore
    return {"@type": "DefinedTermSet", "@id": BASE + "ressources/glossaire/#termes", "name": "Glossaire de navi",
            "inLanguage": "fr-BE",
            "hasDefinedTerm": [{"@type": "DefinedTerm", "@id": BASE + "ressources/glossaire/#" + _s(t), "name": t, "description": d,
                                "inDefinedTermSet": BASE + "ressources/glossaire/#termes", "url": BASE + link} for t, d, link in GLOSS]}


CHRONO = [
 ("1830", "Indépendance de la Belgique."),
 ("1949", "La Belgique, membre fondateur de l'OTAN."),
 ("1957", "Traités de Rome : la Belgique fonde la CEE."),
 ("1967", "Le siège de l'OTAN s'installe à Bruxelles, le SHAPE à Mons."),
 ("1970", "Première réforme de l'État."),
 ("1993", "Quatrième réforme : la Belgique devient un État fédéral."),
 ("1994", "Suspension du service militaire obligatoire."),
 ("1996", "Intégration des marines belge et néerlandaise (BeNeSam)."),
 ("2003", "Loi de sortie du nucléaire ; licences d'armes régionalisées."),
 ("2010-2011", "Crise politique de 541 jours sans gouvernement fédéral de plein exercice."),
 ("2012-2014", "Sixième réforme de l'État."),
 ("2016", "Attentats de Bruxelles (22 mars) ; blocage wallon du CETA."),
 ("2017", "Budget de la défense au plus bas : 0,88 % du PIB."),
 ("2019", "Entrée en vigueur du partenariat CaMo avec la France."),
 ("24 février 2022", "Invasion à grande échelle de l'Ukraine par la Russie ; gel des avoirs russes chez Euroclear."),
 ("2022", "Plan STAR pour la défense."),
 ("1ᵉʳ semestre 2024", "Présidence belge du Conseil de l'UE."),
 ("9 juin 2024", "« Méga-scrutin » : élections européennes, fédérales et régionales."),
 ("Juillet 2024", "Gouvernements wallon (Dolimont), FWB (Degryse) et germanophone (Paasch III) ; ouverture d'une procédure pour déficit excessif (26 juillet)."),
 ("Septembre 2024", "Gouvernement flamand Diependaele."),
 ("13 octobre 2024", "Élections communales et provinciales ; majorité absolue du Vlaams Belang à Ninove."),
 ("3 février 2025", "Prestation de serment du gouvernement De Wever (Arizona)."),
 ("Avril 2025", "Contrôles chinois sur sept terres rares lourdes."),
 ("Juin 2025", "Sommet de l'OTAN : objectif de 5 % du PIB d'ici 2035."),
 ("2025", "Accord État-ENGIE : Doel 4 et Tihange 3 prolongés jusqu'en 2035."),
 ("Octobre 2025", "Validation de la mise à jour du plan national énergie-climat."),
 ("Novembre 2025", "La Chambre adopte la loi de programmation militaire 2026-2034."),
 ("Décembre 2025", "La Belgique intervient devant la CIJ dans l'affaire Afrique du Sud c. Israël."),
 ("Février 2026", "Expiration du traité New START ; gouvernement bruxellois Dilliès après 613 jours (14 février)."),
 ("Mars 2026", "Arrêt de la cour d'appel de Bruxelles sur les transferts d'armes vers Israël."),
 ("Avril 2026", "Trêve pascale russo-ukrainienne de 32 heures, non respectée ; rapport SIPRI sur les dépenses militaires."),
 ("30 mai 2026", "Loi-programme instaurant l'« indexation en centimes »."),
 ("Juin 2026", "Statbel : 11 867 634 habitants au 1ᵉʳ janvier 2026."),
 ("Rentrée 2026", "Déploiement du tronc commun dans le secondaire en FWB."),
 ("Septembre 2026", "Sommet des BRICS à New Delhi ; rétablissement des relations belgo-rwandaises ; Egmont Policy Brief 415 sur les semi-conducteurs."),
 ("12 octobre 2026", "Journée de grève annoncée dans les services publics (CGSP)."),
 ("10 novembre 2026", "Fin de la suspension d'une partie des contrôles chinois sur les terres rares."),
 ("Novembre 2026", "Élections de mi-mandat aux États-Unis."),
]


FAQ = [
 ("Qu'est-ce que la géosociopolitique ?", "C'est l'étude croisée des rapports de puissance entre États (géopolitique), des structures sociales et des dynamiques politiques internes. Elle relie ce qui se passe entre les nations à ce qui se passe dans les sociétés."),
 ("Que signifient macro, méso et micro ?", "Macro : le système mondial (grandes puissances, flux, climat). Méso : les échelons intermédiaires (Union européenne, OTAN, États, Régions). Micro : les sociétés, territoires et individus (revenus, emploi, école, sécurité)."),
 ("Qui gouverne la Belgique en 2026 ?", "Au fédéral, la coalition Arizona dirigée par Bart De Wever (N-VA) depuis le 3 février 2025. Les Régions et Communautés ont leurs propres gouvernements ; à Bruxelles, Boris Dilliès (MR) depuis février 2026."),
 ("Pourquoi la Belgique est-elle sous procédure pour déficit excessif ?", "Parce que son déficit public dépasse nettement 3 % du PIB (5,4 % en 2025) et que sa dette dépasse 100 % du PIB. La procédure a été ouverte par le Conseil de l'UE le 26 juillet 2024."),
 ("Pourquoi la Belgique refuse-t-elle de confisquer les avoirs russes gelés chez Euroclear ?", "Parce qu'une confiscation violerait l'immunité des États, exposerait la Belgique à des poursuites et à des représailles, et pourrait fragiliser la confiance dans l'euro. Elle exige un partage des risques au niveau européen."),
 ("Combien la Belgique dépense-t-elle pour sa défense ?", "Elle vise au moins 2 % du PIB dès 2025-2026, contre 0,88 % en 2017. La Vision stratégique 2026-2034 prévoit 34 milliards d'euros d'investissements."),
 ("Qu'est-ce que l'indexation en centimes ?", "Un plafonnement temporaire de l'indexation automatique des salaires : à partir de juin 2026, la part du salaire brut au-delà de 4 000 € par mois n'est pas indexée, pendant deux cycles."),
 ("Qui a écrit ce site ?", "Les textes sont rédigés par Claude, un modèle d'intelligence artificielle d'Anthropic, à partir de dossiers de recherche et de sources publiques citées. L'éditeur du site reste anonyme."),
 ("Les informations sont-elles à jour ?", "L'état des connaissances est celui de fin septembre 2026. Les chiffres proviennent des sources citées en bas de chaque page ; ils peuvent être révisés par leurs producteurs."),
]


def faq_ld():
    return {"@type": "FAQPage", "@id": BASE + "ressources/faq/#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}


PAGES = [
{
 "slug": "ressources/", "section": S, "kind": "hub",
 "title": "Ressources : glossaire, chronologie, chiffres, vidéos, sources",
 "h1": "Ressources",
 "desc": "Outils de référence de navi : glossaire, chronologie 1830-2026, chiffres clés, vidéos, FAQ et bibliographie complète.",
 "lede": "Les outils pour naviguer : définitions, repères chronologiques, données, vidéos et sources.",
 "keywords": ["glossaire géopolitique", "chronologie Belgique", "chiffres clés Belgique"],
 "body": "<p>Toutes les ressources sont reliées aux dossiers thématiques. Utilisez aussi la <a href=\"@/recherche/\">recherche plein texte</a>.</p>",
},
{
 "slug": "ressources/glossaire/", "section": S, "kind": "glossary",
 "title": "Glossaire de la géosociopolitique et de la Belgique",
 "h1": "Glossaire",
 "desc": "Définitions claires de 34 notions clés : polycrise, fédéralisme, confédéralisme, LSF, PDE, CaMo, Euroclear, ETS2, NIS2, budget carbone, zone grise…",
 "lede": "Les mots pour comprendre le monde et la Belgique en 2026.",
 "keywords": ["glossaire", "définitions", "vocabulaire politique belge", "vocabulaire géopolitique"],
 "body": "__GLOSS__",
 "ld_extra": "__GLOSS_LD__",
},
{
 "slug": "ressources/chronologie/", "section": S, "kind": "timeline",
 "title": "Chronologie : la Belgique et le monde, 1830-2026",
 "h1": "Chronologie : la Belgique et le monde",
 "desc": "Les dates clés de la Belgique fédérale et de son insertion internationale, de 1830 aux échéances de fin 2026.",
 "lede": "De l'indépendance aux échéances de l'automne 2026.",
 "keywords": ["chronologie Belgique", "dates clés", "histoire politique belge"],
 "body": '<ol class="timeline">' + "".join(f"<li><time>{d}</time>{t}</li>" for d, t in CHRONO) + "</ol>",
},
{
 "slug": "ressources/chiffres-cles/", "section": S, "kind": "article",
 "title": "Chiffres clés : la Belgique et le monde en 2026",
 "h1": "Chiffres clés 2026",
 "desc": "Tableau de bord : population, dette, déficit, emploi, défense, énergie pour la Belgique ; dépenses militaires, démocratie, climat, croissance pour le monde.",
 "lede": "Les données essentielles, avec leurs sources. Les pages thématiques les mettent en contexte.",
 "keywords": ["chiffres clés Belgique 2026", "statistiques Belgique", "données géopolitiques"],
 "about": [("Belgique", "https://www.wikidata.org/wiki/Q31", "Country")],
 "body": f"""
<h2>Belgique</h2>
{kpis([("11 867 634", "habitants au 1ᵉʳ janvier 2026 (Statbel)"), ("+1,1 %", "croissance du PIB attendue en 2026 (BFP)"), ("−5,0 %", "déficit public projeté en 2026"), ("109,8 %", "dette publique projetée fin 2026"), ("72,8 %", "taux d'emploi 20-64 ans"), ("≈ 153 %", "ouverture commerciale (2025)"), ("2 %", "du PIB : objectif défense 2025-2026"), ("266,5 Mt", "trafic du port d'Anvers-Bruges en 2025 (−4,1 %)")])}
{table(["Indicateur", "Valeur", "Source"], [
 ("Population", "11 867 634 (1ᵉʳ janvier 2026)", "Statbel"),
 ("Taux d'emploi Flandre / Wallonie / Bruxelles", "77,3 % / 67,6 % / 64,7 %", "Statbel"),
 ("Dette 2025", "107,4 % du PIB (≈ 690,7 Md€)", "BNB, BFP"),
 ("Coût du vieillissement", "25,7 % du PIB (2025) → 27,2 % (2050)", "Comité d'étude sur le vieillissement"),
 ("Bruxellois en difficulté financière", "49 %", "BX1 / enquête 2026"),
 ("Avoirs russes immobilisés chez Euroclear", "≈ 210 Md€", "Parlement européen, Euroclear"),
 ("Investissements défense 2026-2034", "34 Md€", "Vision stratégique"),
 ("Projets d'IDE 2025", "185 (−11 %)", "EY"),
 ("Soft power", "20ᵉ mondial", "Brand Finance 2026"),
], "Belgique : tableau de bord")}
<h2>Monde</h2>
{table(["Indicateur", "Valeur", "Source"], [
 ("Dépenses militaires mondiales 2025", "2 887 Md$ (2,5 % du PIB mondial)", "SIPRI"),
 ("Têtes nucléaires (stocks militaires)", "9 745, dont ≈ 4 012 déployées", "SIPRI, janvier 2026"),
 ("Croissance mondiale 2026", "3,1 % (FMI) ; 2,5 % (Banque mondiale)", "FMI, Banque mondiale"),
 ("Part du dollar dans les réserves", "57,13 % (T1 2026)", "FMI COFER"),
 ("Population en autocratie", "74 %", "V-Dem 2026"),
 ("Limites planétaires franchies", "7 sur 9", "PIK / SRC 2025"),
 ("Concentration de CO₂", "≈ 425,7 ppm", "Global Carbon Budget"),
 ("Indice FAO des prix alimentaires", "133,3 (août 2026)", "FAO"),
 ("Données intercontinentales via câbles", "≈ 99 %", "Plusieurs sources"),
], "Monde : tableau de bord")}
""",
 "sources": [("Statbel — 11 867 634 habitants au 1er janvier 2026", "https://statbel.fgov.be/fr/nouvelles/la-belgique-comptait-11867634-habitants-au-1er-janvier-2026"),
             ("Bureau fédéral du Plan", "https://www.plan.be/fr"),
             ("SIPRI Yearbook 2026", "https://www.sipri.org/yearbook/2026/08"),
             ("V-Dem — Democracy Report 2026", "https://www.v-dem.net/documents/75/V-Dem_Institute_Democracy_Report_2026_lowres.pdf")],
 "related": ["belgique/finances-publiques/", "monde/rearmement-nucleaire/", "micro/emploi-territoires/"],
},
{
 "slug": "ressources/videos/", "section": S, "kind": "videos",
 "title": "Vidéos : comprendre la géosociopolitique",
 "h1": "Vidéos",
 "desc": "Vidéos sélectionnées pour approfondir la géosociopolitique mondiale et belge, intégrées en mode respectueux de la vie privée.",
 "lede": "Deux vidéos pour prolonger la lecture. Le lecteur YouTube ne se charge qu'au clic (domaine youtube-nocookie).",
 "keywords": ["vidéos géopolitique", "comprendre la géopolitique", "Belgique vidéo"],
 "body": '<div class="video-grid">' + "".join(video(v, n, d) for v, n, d in VIDEOS) + "</div>"
         + "<p class=\"small\">Aucun cookie YouTube n'est déposé avant que vous lanciez la lecture.</p>",
 "ld_extra": [video_ld(v, n, d, "ressources/videos/") for v, n, d in VIDEOS],
},
{
 "slug": "ressources/faq/", "section": S, "kind": "faq",
 "title": "FAQ : questions fréquentes sur la Belgique et la géopolitique",
 "h1": "Questions fréquentes",
 "desc": "Réponses courtes aux questions les plus posées : échelles macro-méso-micro, gouvernement belge, déficit, Euroclear, défense, indexation, auteur du site.",
 "lede": "Des réponses courtes, avec des liens pour aller plus loin.",
 "keywords": ["FAQ", "questions Belgique", "géosociopolitique définition"],
 "body": "".join(f"<h2>{esc(q)}</h2><p>{esc(a)}</p>" for q, a in FAQ),
 "ld_extra": "__FAQ_LD__",
},
{
 "slug": "ressources/sources/", "section": S, "kind": "bibliography",
 "title": "Sources et bibliographie",
 "h1": "Sources et bibliographie",
 "desc": "Toutes les sources citées sur navi, classées par rubrique : institutions internationales, statistiques officielles belges, centres de recherche, presse.",
 "lede": "La liste complète des sources citées dans les dossiers, regroupées par rubrique.",
 "keywords": ["sources", "bibliographie", "références"],
 "body": "__BIBLIO__",
},
]

for _p in PAGES:
    if _p["body"] == "__GLOSS__":
        _p["body"] = gloss_body()
    if _p.get("ld_extra") == "__GLOSS_LD__":
        _p["ld_extra"] = [gloss_ld()]
    if _p.get("ld_extra") == "__FAQ_LD__":
        _p["ld_extra"] = [faq_ld()]
