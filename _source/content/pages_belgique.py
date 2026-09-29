from h import L, kpis, bars, table, callout, levels

W = "https://fr.wikipedia.org/wiki/"
WD = "https://www.wikidata.org/wiki/"
S = "belgique"
BE = ("Belgique", WD + "Q31", "Country")

PAGES = [
{
 "slug": "belgique/", "section": S, "kind": "hub",
 "title": "Belgique 2026 : institutions, politique, économie, énergie",
 "h1": "La Belgique en 2026 : un laboratoire de l'Europe",
 "desc": "Tout comprendre de la Belgique contemporaine : fédéralisme, élections de 2024, coalition Arizona, finances publiques, économie, énergie-climat et Bruxelles.",
 "lede": "11,87 millions d'habitants, trois Régions, trois Communautés, six parlements et un pays qui concentre, sur 30 688 km², presque toutes les tensions des démocraties européennes.",
 "keywords": ["Belgique 2026", "politique belge", "fédéralisme belge", "économie belge", "gouvernement De Wever"],
 "about": [BE],
 "body": f"""
{kpis([("11 867 634", "habitants au 1ᵉʳ janvier 2026 (Statbel)"), ("107,4 %", "dette publique / PIB en 2025"), ("72,8 %", "taux d'emploi des 20-64 ans (2026)"), ("613 jours", "sans gouvernement bruxellois de plein exercice (2024-2026)")])}
<h2>Repères essentiels</h2>
<ul>
<li><strong>Régime</strong> : monarchie constitutionnelle fédérale ; roi Philippe depuis 2013.</li>
<li><strong>Entités fédérées</strong> : Régions flamande, wallonne et de Bruxelles-Capitale ; Communautés flamande, française (Fédération Wallonie-Bruxelles) et germanophone.</li>
<li><strong>Langues officielles</strong> : néerlandais, français, allemand.</li>
<li><strong>Gouvernement fédéral</strong> : coalition « Arizona » dirigée par Bart De Wever (N-VA) depuis le 3 février 2025.</li>
<li><strong>Économie</strong> : très ouverte (commerce extérieur ≈ 150 % du PIB), port d'Anvers-Bruges, chimie-pharma, services.</li>
</ul>
<p>Pour l'insertion internationale du pays, voir la rubrique {L("meso/", "Méso")} ; pour le vécu social, la rubrique {L("micro/", "Micro")}.</p>
""",
},
{
 "slug": "belgique/federalisme/", "section": S,
 "title": "Le fédéralisme belge expliqué : six réformes de l'État, Régions et Communautés",
 "h1": "Le fédéralisme belge en six réformes",
 "desc": "De l'État unitaire à l'État fédéral (1970-2014) : Régions, Communautés, sixième réforme, confédéralisme, Communauté germanophone et « fédéralisme de réforme renforcé ».",
 "lede": "La Belgique n'a pas été conçue fédérale : elle l'est devenue, par couches successives, pour pacifier ses conflits linguistiques. Le résultat est un édifice unique, efficace pour éviter la rupture, lent pour décider.",
 "keywords": ["fédéralisme belge", "réformes de l'État", "Régions et Communautés", "confédéralisme", "Communauté germanophone", "sixième réforme de l'État"],
 "about": [BE, ("Réformes de l'État belge", W + "R%C3%A9formes_de_l%27%C3%89tat_belge"), ("Communauté germanophone de Belgique", W + "Communaut%C3%A9_germanophone_de_Belgique", "AdministrativeArea")],
 "level_label": "Méso",
 "body": f"""
<h2>Deux fédéralismes superposés</h2>
<p>La Belgique repose sur deux types d'entités fédérées qui se chevauchent :</p>
{table(["Type", "Entités", "Compétences typiques"], [
 ("Régions (territoire)", "Flandre, Wallonie, Bruxelles-Capitale", "Économie, emploi, aménagement du territoire, environnement, logement, mobilité, commerce extérieur"),
 ("Communautés (personnes)", "Flamande, française (FWB), germanophone", "Enseignement, culture, médias, aide aux personnes, une partie de la santé"),
 ("État fédéral", "—", "Justice, défense, police fédérale, sécurité sociale, fiscalité principale, politique monétaire (via l'UE), affaires étrangères"),
], "Qui fait quoi en Belgique ?")}
<p>En Flandre, Région et Communauté ont fusionné leurs institutions. Côté francophone, la Région wallonne et la Fédération Wallonie-Bruxelles restent distinctes, avec des transferts de compétences de la seconde vers la première et vers la Commission communautaire française (COCOF) à Bruxelles.</p>
<h2>Les six réformes de l'État</h2>
{table(["Réforme", "Années", "Apports principaux"], [
 ("1ʳᵉ", "1970", "Création des communautés culturelles, principe des Régions"),
 ("2ᵉ", "1980", "Institutions flamandes et wallonnes, Communautés compétentes pour les matières personnalisables"),
 ("3ᵉ", "1988-1989", "Enseignement aux Communautés, Région de Bruxelles-Capitale, loi spéciale de financement"),
 ("4ᵉ", "1993", "La Belgique devient un « État fédéral » (art. 1ᵉʳ de la Constitution), élection directe des parlements"),
 ("5ᵉ", "2001", "Agriculture, commerce extérieur, lois communales et provinciales aux Régions"),
 ("6ᵉ", "2012-2014", "Allocations familiales, emploi, une partie des soins de santé, mobilité ; réforme du Sénat et de la LSF"),
], "Chronologie de la fédéralisation")}
<h2>Frictions et débats</h2>
<p>Ce fédéralisme « de dissociation » produit des chevauchements et une coordination permanente (comités de concertation, conférences interministérielles, accords de coopération). Deux visions s'opposent :</p>
<ul>
<li>le <strong>fédéralisme coopératif</strong>, qui veut clarifier les compétences exclusives et renforcer la collaboration ;</li>
<li>le <strong>confédéralisme</strong> porté par la N-VA : Flandre et Wallonie quasi souveraines, ne déléguant qu'un minimum au niveau central. Le Vlaams Belang prône, lui, l'indépendance flamande.</li>
</ul>
<p>L'accord de gouvernement Arizona renonce provisoirement à une réforme constitutionnelle au profit d'un « fédéralisme de réforme renforcé » : plus de coopération, plus de responsabilité financière des entités.</p>
<h2>La Communauté germanophone, entité en émancipation</h2>
<p>Environ 80 000 habitants dans l'est du pays. Depuis des décennies, la Wallonie lui transfère des compétences (emploi, aménagement du territoire, logement). En 2024, son Parlement a adopté une résolution pour sortir de la province de Liège et se faire reconnaître comme entité fédérée à part entière, en vue d'une éventuelle septième réforme. Son gouvernement « Paasch III » (ProDG, CSP, PFF) s'est installé en juillet 2024.</p>
<h2>Le fédéralisme à l'international</h2>
<p>Les entités fédérées concluent leurs propres traités dans leurs domaines (principe <em>in foro interno, in foro externo</em>). Voir {L("meso/diplomatie-belge/", "diplomatie belge")} et l'épisode du CETA.</p>
{levels("La Belgique est citée comme modèle — ou contre-modèle — de gestion des sociétés plurinationales.", "Six parlements, des accords de coopération, une loi spéciale de financement qui structure les budgets.", "Les citoyens s'adressent à plusieurs niveaux pour l'école, l'emploi, les allocations familiales, la santé.")}
""",
 "sources": [("Wikipédia — Réformes de l'État belge", W + "R%C3%A9formes_de_l%27%C3%89tat_belge"),
             ("CRISP — Vocabulaire politique : Communauté germanophone", "https://www.vocabulairepolitique.be/communaute-germanophone/"),
             ("Bureau fédéral du Plan — La 6e réforme de l'État : soutenabilité budgétaire", "https://www.plan.be/fr/publications/la-6e-reforme-de-letat-enjeux-en-termes-de"),
             ("Belgium.be — Accord de gouvernement fédéral 2025-2029", "https://www.belgium.be/fr/publications/accord_de_gouvernement_du_gouvernement_federal_bart_de_wever"),
             ("21News — La Communauté germanophone va sortir de la province de Liège", "https://www.21news.be/la-communaute-germanophone-va-sortir-de-la-province-de-liege/")],
 "related": ["belgique/gouvernements/", "belgique/finances-publiques/", "meso/diplomatie-belge/"],
},
{
 "slug": "belgique/elections-2024/", "section": S,
 "title": "Élections belges de 2024 : résultats, analyse, carte politique",
 "h1": "Le « méga-scrutin » de 2024 et la nouvelle carte politique",
 "desc": "Résultats des élections fédérales, régionales et européennes du 9 juin 2024 et des communales d'octobre 2024 : N-VA, Vlaams Belang, MR, Les Engagés, recul du PS et d'Ecolo.",
 "lede": "Le 9 juin 2024, les Belges ont voté le même jour pour l'Europe, le fédéral et les Régions. Résultat : une victoire des droites au nord comme au sud, sous des formes très différentes.",
 "keywords": ["élections belges 2024", "résultats élections Belgique", "N-VA", "Vlaams Belang", "MR", "Les Engagés", "élections communales 2024"],
 "about": [("Élections législatives fédérales belges de 2024", W + "%C3%89lections_l%C3%A9gislatives_f%C3%A9d%C3%A9rales_belges_de_2024", "Event"), BE],
 "level_label": "Méso",
 "body": f"""
<h2>Résultats à la Chambre</h2>
{bars("Sièges à la Chambre des représentants (sur 150), élections du 9 juin 2024", [("N-VA", 24), ("Vlaams Belang", 20), ("MR", 20), ("PS", 16), ("PVDA-PTB", 15), ("Les Engagés", 14), ("Vooruit", 13), ("CD&amp;V", 11), ("Open VLD", 7), ("Groen", 6), ("Ecolo", 3), ("DéFI", 1)], note="Source : SPF Intérieur, résultats officiels. Les partis de la coalition Arizona (N-VA, MR, Les Engagés, Vooruit, CD&amp;V) totalisent 82 sièges.")}
{table(["Parti", "Orientation", "Voix (national)", "Dynamique"], [
 ("N-VA", "Nationalisme flamand, conservatisme", "16,71 %", "Reste premier parti"),
 ("Vlaams Belang", "Extrême droite, séparatisme", "13,77 %", "Forte progression"),
 ("MR", "Libéralisme", "10,26 %", "Percée en Wallonie et à Bruxelles"),
 ("PVDA-PTB", "Gauche radicale", "9,86 %", "Stagnation"),
 ("Vooruit", "Social-démocratie flamande", "8,11 %", "Légère hausse"),
 ("PS", "Social-démocratie francophone", "8,04 %", "Recul historique"),
 ("CD&amp;V", "Démocratie chrétienne flamande", "7,98 %", "Érosion"),
 ("Les Engagés", "Centre", "6,77 %", "Triplement des sièges"),
], "Principaux partis, scrutin fédéral 2024")}
<h2>En Flandre : la N-VA tient, le Vlaams Belang progresse</h2>
<p>Au Parlement flamand, le Vlaams Belang obtient 22,66 % et 31 sièges, mais la N-VA reste première avec 23,88 %, contrairement aux sondages. Le « cordon sanitaire » autour du VB est maintenu ; la N-VA forme un gouvernement flamand avec Vooruit et le CD&amp;V, dirigé par Matthias Diependaele. Aux communales d'octobre 2024, le VB décroche pour la première fois une majorité absolue, à Ninove.</p>
<h2>En Wallonie et à Bruxelles : la vague bleue et orange</h2>
<p>Au Parlement wallon, le MR s'impose avec 29,61 %, devant le PS (23,22 %) et Les Engagés (20,66 %). Ecolo s'effondre, le PTB stagne. Pour la première fois depuis des décennies, le PS est rejeté dans l'opposition à tous les niveaux sauf à Bruxelles.</p>
<h2>Des électorats moins éloignés qu'il n'y paraît</h2>
<p>Les enquêtes post-électorales (ISPO/KU Leuven) montrent que les priorités diffèrent — la migration domine l'agenda flamand, le pouvoir d'achat l'agenda wallon — mais que les valeurs socio-économiques des électeurs des deux côtés sont très proches. Voir {L("micro/identites/", "identités et clichés")}.</p>
{callout("<p>En Belgique, les partis sont organisés par communauté linguistique : un électeur wallon ne peut pas voter N-VA, un électeur flamand ne peut pas voter MR (sauf dans l'ancien arrondissement de Bruxelles-Hal-Vilvorde pour certaines listes). Le système fédéral assemble donc deux paysages politiques distincts.</p>", "lilac", "Particularité belge")}
""",
 "sources": [("SPF Intérieur — Résultats Chambre, 9 juin 2024", "https://resultatselection.belgium.be/fr/election-results/chambre-des-repr%C3%A9sentants/2024/royaume/251712"),
             ("SPF Intérieur — Résultats Parlement flamand 2024", "https://resultatselection.belgium.be/fr/election-results/parlement-flamand/2024/r%C3%A9gion/251714"),
             ("SPF Intérieur — Résultats Parlement wallon 2024", "https://resultatselection.belgium.be/fr/election-results/parlement-wallon/r%C3%A9gion/2024/253626"),
             ("Wikipédia — Vlaams Belang", W + "Vlaams_Belang"),
             ("DaarDaar — Flamands de droite et Wallons de gauche, vraiment ?", "https://daardaar.be/rubriques/societe/flamands-de-droite-et-wallons-de-gauche-vraiment-cette-etude-deconstruit-les-cliches/")],
 "related": ["belgique/gouvernements/", "micro/identites/", "micro/communes/"],
},
{
 "slug": "belgique/gouvernements/", "section": S,
 "title": "Gouvernements belges 2024-2026 : Arizona, Wallonie, Flandre, Bruxelles",
 "h1": "Qui gouverne la Belgique ? Les exécutifs 2024-2026",
 "desc": "La coalition fédérale Arizona de Bart De Wever, les gouvernements flamand, wallon, de la FWB et germanophone, et les 613 jours de blocage bruxellois jusqu'au gouvernement Dilliès.",
 "lede": "Des exécutifs formés en quelques semaines au sud, en plus de sept mois au fédéral, en plus d'un an et demi à Bruxelles : la Belgique de 2024-2026 illustre toutes les vitesses du compromis.",
 "keywords": ["coalition Arizona", "gouvernement De Wever", "gouvernement wallon Dolimont", "gouvernement Dilliès", "613 jours Bruxelles"],
 "about": [("Gouvernement De Wever", W + "Gouvernement_De_Wever", "GovernmentOrganization"), ("Bart De Wever", W + "Bart_De_Wever", "Person"), ("Gouvernement Dilliès", W + "Gouvernement_Dilli%C3%A8s", "GovernmentOrganization")],
 "level_label": "Méso",
 "body": f"""
<h2>Le fédéral : la coalition Arizona</h2>
<p>Après 239 jours de négociations, l'accord est conclu le 31 janvier 2025 et le gouvernement <strong>De Wever</strong> prête serment le 3 février 2025. Pour la première fois, un nationaliste flamand dirige le gouvernement fédéral. La coalition réunit N-VA (jaune), MR (bleu), Les Engagés et CD&amp;V (orange) et Vooruit (rouge) — les couleurs du drapeau de l'Arizona.</p>
{table(["Portefeuille", "Titulaire", "Parti"], [
 ("Premier ministre", "Bart De Wever", "N-VA"),
 ("Affaires étrangères", "Maxime Prévot", "Les Engagés"),
 ("Économie et Emploi", "David Clarinval", "MR"),
 ("Défense", "Theo Francken", "N-VA"),
 ("Finances", "Jan Jambon", "N-VA"),
 ("Budget", "Vincent Van Peteghem", "CD&amp;V"),
 ("Affaires sociales et Santé", "Frank Vandenbroucke", "Vooruit"),
 ("Fonction publique, Modernisation", "Vanessa Matz", "Les Engagés"),
], "Membres clés du gouvernement fédéral")}
<h3>Le programme</h3>
<p>L'accord de coalition, très détaillé, vise des économies de l'ordre de 23 milliards d'euros d'ici 2029, pour respecter les règles européennes et financer de nouvelles priorités (défense, sécurité). Principales mesures :</p>
<ul>
<li>réforme des {L("micro/vieillissement-pensions/", "pensions")} (bonus, accès à la pension anticipée resserré) ;</li>
<li>marché du travail : limitation dans le temps des allocations de chômage, évaluation des malades de longue durée après huit semaines, statut unique ouvrier-employé ;</li>
<li>{L("micro/pouvoir-d-achat/", "« indexation en centimes »")} au-delà de 4 000 € bruts ;</li>
<li>tax shift énergétique, taxe sur les comptes-titres doublée, contribution bancaire accrue ;</li>
<li>fusion de l'Office des étrangers, du CGRA et de Fedasil en un SPF Migration d'ici 2027 ;</li>
<li>réarmement ({L("meso/otan-defense/", "défense")}).</li>
</ul>
<p>Certains universitaires parlent de « néolibéralisme autoritaire » ; les syndicats multiplient grèves et manifestations. Une nouvelle journée d'action des services publics (CGSP) est annoncée pour le 12 octobre 2026, en pleine confection du budget.</p>
<h2>Les Régions et Communautés</h2>
{table(["Entité", "Chef de l'exécutif", "Coalition", "Installation"], [
 ("Région wallonne", "Adrien Dolimont (MR)", "MR – Les Engagés", "Juillet 2024"),
 ("Fédération Wallonie-Bruxelles", "Élisabeth Degryse (Les Engagés)", "MR – Les Engagés", "Juillet 2024"),
 ("Flandre (Région et Communauté)", "Matthias Diependaele (N-VA)", "N-VA – Vooruit – CD&amp;V", "Septembre 2024"),
 ("Communauté germanophone", "Oliver Paasch (ProDG)", "ProDG – CSP – PFF", "Juillet 2024"),
 ("Région de Bruxelles-Capitale", "Boris Dilliès (MR)", "MR, PS, Les Engagés, Groen, Anders, Vooruit, CD&amp;V", "Février 2026"),
], "Les gouvernements des entités fédérées")}
<h2>Bruxelles : 613 jours de blocage</h2>
<p>La loi spéciale exige à Bruxelles une majorité dans chacun des deux groupes linguistiques du Parlement. Côté francophone, le PS refusait toute alliance incluant la N-VA ; côté néerlandophone, Groen et Vooruit peinaient à former une majorité sans elle. Il a fallu 613 jours pour qu'un accord à sept partis aboutisse ; le gouvernement de <strong>Boris Dilliès</strong> (MR) a prêté serment le 14 février 2026 avec une feuille de route resserrée : retour à l'équilibre budgétaire, Plan régional de mobilité, lutte contre la criminalité. Voir {L("belgique/bruxelles/", "le dossier Bruxelles")}.</p>
{callout("<p>Des constitutionnalistes ont décrit Bruxelles, pendant ce blocage, comme une « pure confédération » : chaque groupe linguistique y dispose d'une autonomie totale dans la négociation.</p>", "lilac", "Un révélateur institutionnel")}
""",
 "sources": [("Wikipédia — Gouvernement De Wever", W + "Gouvernement_De_Wever"),
             ("Belgium.be — Accord de coalition fédérale 2025-2029 (PDF)", "https://www.belgium.be/sites/default/files/resources/publication/files/Accord_gouvernemental-Bart_De_Wever_fr.pdf"),
             ("VRT NWS — Le gouvernement bruxellois Dilliès prête serment (14/02/2026)", "https://www.vrt.be/vrtnws/fr/2026/02/14/le-nouveau-gouvernement-bruxellois-mene-par-le-ministre-preside/"),
             ("BX1 — Après 613 jours de blocage, un accord bruxellois", "https://bx1.be/categories/news/apres-613-jours-de-blocage-la-region-bruxelloise-tient-enfin-un-accord-de-gouvernement/"),
             ("Wallonie.be — Composition du gouvernement wallon 2024-2029", "https://www.wallonie.be/fr/actualites/composition-du-gouvernement-wallon-2024-2029"),
             ("La Libre — La CGSP appelle à la grève le 12 octobre (22/09/2026)", "https://www.lalibre.be/belgique/societe/2026/09/22/la-cgsp-appelle-a-la-greve-le-12-octobre-pour-peser-sur-les-choix-budgetaires-du-gouvernement-7JL7MNXDA5G2TE7V4M2O6YUFYI/")],
 "related": ["belgique/elections-2024/", "belgique/bruxelles/", "belgique/finances-publiques/"],
},
{
 "slug": "belgique/finances-publiques/", "section": S,
 "title": "Finances publiques belges : déficit, dette, effet boule de neige, LSF",
 "h1": "Finances publiques : la Belgique sous procédure pour déficit excessif",
 "desc": "Déficit de 5 % du PIB, dette vers 116 % en 2029, effet boule de neige selon la BNB, loi spéciale de financement, budget de la FWB, mesures fiscales de l'Arizona.",
 "lede": "La Belgique est l'un des pays les plus fragiles de la zone euro sur le plan budgétaire. La charge d'intérêts remonte, le vieillissement coûte, la défense aussi.",
 "keywords": ["déficit Belgique", "dette publique Belgique", "procédure déficit excessif", "effet boule de neige", "loi spéciale de financement", "budget FWB"],
 "about": [BE, ("Dette publique", W + "Dette_publique"), ("Banque nationale de Belgique", W + "Banque_nationale_de_Belgique", "Organization")],
 "level_label": "Méso",
 "body": f"""
<h2>Les chiffres</h2>
{table(["Indicateur", "2024", "2025", "2026 (proj.)", "2029 (politique inchangée)"], [
 ("Croissance du PIB réel", "+0,9 %", "+1,0 %", "+1,1 %", "+1,4 %"),
 ("Déficit public (% PIB)", "−4,5 %", "−5,4 %", "−5,0 %", "−5,8 % (−6,4 % en 2031)"),
 ("Dette publique (% PIB)", "104,7 %", "107,4 %", "109,8 %", "116,6 %"),
 ("Inflation", "2,8 %", "2,1 %", "1,3 %", "Pic à 2,4 % en 2027 (ETS2)"),
], "Trajectoire macro-budgétaire (BFP, BNB, Commission)")}
{bars("Dette publique belge, en % du PIB", [("2024", 104.7, "104,7 %"), ("2025", 107.4, "107,4 %"), ("2026 (projection)", 109.8, "109,8 %"), ("2029 (politique inchangée)", 116.6, "116,6 %")], maxv=120, note="Sources : Bureau fédéral du Plan, BNB, Commission européenne. Échelle de 0 à 120 %. En 2025, la dette représentait environ 690 milliards d'euros.")}
<h2>La procédure pour déficit excessif</h2>
<p>Ouverte le 26 juillet 2024 par le Conseil de l'UE, elle impose un plan budgétaire et structurel à moyen terme : la croissance des dépenses primaires nettes est plafonnée à 2,5 % en 2026 et 2027. Le gouverneur de la BNB, Pierre Wunsch, a chiffré à plus de 11 milliards d'euros l'effort nécessaire pour s'y conformer.</p>
<h2>L'effet boule de neige</h2>
<p>La BNB alerte : le taux d'intérêt implicite sur la dette remonte (de 1,8 % en 2023 vers près de 3 % à long terme) alors que la croissance nominale reste faible. Quand le taux dépasse la croissance, la dette augmente mécaniquement même sans nouveau déficit primaire. Les charges d'intérêt passeraient de 2,4 % du PIB en 2025 à 3,3 % en 2028.</p>
<h2>Qui porte la dette ?</h2>
<p>L'Entité I (fédéral et sécurité sociale) porte plus de 80 % de la dette totale, mais l'Entité II (Régions et Communautés) présente un risque élevé d'insoutenabilité à moyen terme. La dette de la Wallonie et de Bruxelles pourrait dépasser 300 % de leurs recettes propres.</p>
<h3>La loi spéciale de financement (LSF)</h3>
<p>Adoptée en 1989 et remaniée par la sixième réforme, la LSF finance les entités surtout par des dotations et une part d'impôt, avec des mécanismes de transition qui s'éteignent progressivement. Des compétences lourdes ont été transférées sans autonomie fiscale proportionnelle ; les entités se sont endettées. Pour la <strong>Fédération Wallonie-Bruxelles</strong>, dont la masse salariale enseignante absorbe l'essentiel du budget, le déficit 2026 est estimé à 1,6 milliard d'euros. Le Conseil supérieur des finances plaide pour davantage de leviers fiscaux régionaux — un argument que la N-VA reprend dans sa logique confédérale.</p>
<h2>Les choix de l'Arizona</h2>
<p>L'effort vise environ 60 % d'économies et 40 % de recettes :</p>
<ul>
<li>baisse des accises sur l'électricité, TVA sur le gaz, le mazout et le diesel portée progressivement de 6 % à 12 % ;</li>
<li>TVA sur pesticides et engrais de synthèse de 6 % à 21 % ;</li>
<li>taxe sur les comptes-titres doublée (0,30 % au-delà d'un million d'euros), contribution bancaire +150 millions, précompte mobilier relevé pour les sociétés de management ;</li>
<li>maîtrise des dépenses sociales, gel des recrutements publics, recours limité à la consultance.</li>
</ul>
{callout("<p>La hausse programmée des dépenses militaires (vers 2 % du PIB, avec la clause dérogatoire européenne) complique la réduction du déficit. Le Bureau du Plan prévient que la norme de défense imposera des arbitrages avec les dépenses sociales.</p>", "warn", "La tenaille : défense, vieillissement, dette")}
{levels("Fin de l'argent bon marché, taux réels positifs, réarmement européen.", "Règles budgétaires de l'UE, LSF, répartition de l'effort entre entités.", "Moins de services publics ou plus d'impôts : ce que chaque ménage paie et reçoit.")}
""",
 "sources": [("Bureau fédéral du Plan — Perspectives économiques 2025-2030", "https://www.plan.be/fr/publications/perspectives-economiques-2025-2030-pour-la"),
             ("BNB — Attention à la boule de neige !", "https://www.nbb.be/fr/actualites/blog/attention-la-boule-de-neige"),
             ("indicators.be — Dette publique", "https://www.indicators.be/fr/i/G17_DBT/Dette_publique_%28i84%29"),
             ("MFWB — Éléments-clés du budget annuel", "https://budget-finances.cfwb.be/budget-et-comptabilite/elements-cles-du-budget-annuel/"),
             ("UNamur — Le nouveau cadre budgétaire européen", "https://www.unamur.be/fr/media/6969"),
             ("Les Engagés — Accord fédéral : grandes orientations", "https://www.lesengages.be/actualite/accord-federal-les-grandes-orientations-pour-redresser-proteger-et-preparer-lavenir/")],
 "related": ["meso/union-europeenne/", "micro/vieillissement-pensions/", "belgique/bruxelles/"],
},
{
 "slug": "belgique/economie/", "section": S,
 "title": "Économie belge 2026 : port d'Anvers, industrie, investissements, compétitivité",
 "h1": "L'économie belge : un carrefour sous pression",
 "desc": "Ouverture commerciale, recul du port d'Anvers-Bruges en 2025, baisse des investissements étrangers, compétitivité, biopharma wallonne et désindustrialisation.",
 "lede": "Dépendante à plus de 150 % du commerce international, l'économie belge amplifie les chocs du monde. Deux visages se dessinent : une logistique lourde qui recule, une économie de la connaissance qui résiste.",
 "keywords": ["économie belge 2026", "port d'Anvers-Bruges", "investissements étrangers Belgique", "compétitivité", "biopharma Wallonie"],
 "about": [BE, ("Port d'Anvers-Bruges", W + "Port_d%27Anvers-Bruges", "Place")],
 "level_label": "Méso",
 "body": f"""
<h2>Une économie hyper-ouverte</h2>
<p>En 2025, la somme des exportations et importations atteignait environ 153 % du PIB. Cette ouverture est une force en période de croissance mondiale, une vulnérabilité en période de fragmentation. La croissance belge attendue pour 2026 est d'environ 1,1 %.</p>
<h2>Le port d'Anvers-Bruges recule</h2>
<p>Deuxième port d'Europe, Anvers-Bruges a vu son trafic baisser de <strong>4,1 %</strong> en 2025, à 266,5 millions de tonnes :</p>
<ul>
<li>vracs solides (charbon, engrais, sable) en chute de 12,1 % ;</li>
<li>vracs liquides en baisse, les nouvelles raffineries africaines réduisant les exportations de produits raffinés ;</li>
<li>moins d'acier européen en transit, pénalisé par le protectionnisme nord-américain ;</li>
<li>roulier en hausse de 3 %, porté par les voitures chinoises — la Chine a dépassé le Japon.</li>
</ul>
<p>Le port est aussi la principale porte d'entrée de la cocaïne en Europe ({L("micro/narcotrafic-anvers/", "narcotrafic")}).</p>
<h2>Attractivité en baisse</h2>
<p>Selon le baromètre EY 2026, les projets d'investissements directs étrangers ont reculé de 11 % en 2025 (185 projets), le plus bas niveau depuis une décennie. Coûts de l'énergie, coûts salariaux, complexité administrative et désindustrialisation européenne pèsent.</p>
<h2>La compétitivité et les salaires</h2>
<p>L'indexation automatique des salaires a protégé le pouvoir d'achat pendant la crise énergétique mais a pesé sur la compétitivité face aux pays voisins. Réponse : norme salariale de 0 % pour 2025-2026 et « indexation en centimes » ({L("micro/pouvoir-d-achat/", "détails")}).</p>
<h2>L'autre visage : la connaissance</h2>
<p>La chimie-pharma reste le premier moteur exportateur, et la Wallonie consolide un pôle biotech (BioWin) qui pèse 6,2 % de son économie et emploie des dizaines de milliers de personnes. L'imec à Louvain, les universités et les spin-offs incarnent la Belgique qui innove ({L("meso/niches-strategiques/", "niches stratégiques")}).</p>
{table(["Force", "Faiblesse"], [
 ("Position logistique centrale, port de rang mondial", "Dépendance aux flux mondiaux en recul"),
 ("Main-d'œuvre très qualifiée, universités", "Coûts salariaux et énergétiques élevés"),
 ("Biopharma, chimie, microélectronique", "Désindustrialisation de l'industrie lourde"),
 ("Institutions internationales à Bruxelles", "Complexité institutionnelle et fiscale"),
], "Forces et faiblesses de l'économie belge")}
""",
 "sources": [("Ports et Corridors — Port Anvers-Bruges : le trafic perd 4,1 % en 2025", "https://portsetcorridors.com/2026/port-anvers-bruges-le-trafic-perd-41-en-2025/"),
             ("EY — Baromètre de l'attractivité belge 2026", "https://www.ey.com/fr_be/insights/entrepreneurship/enseignements-majeurs-du-barometre-de-l-attractivite-belge-2026"),
             ("TheGlobalEconomy — Belgium trade openness", "https://www.theglobaleconomy.com/Belgium/trade_openness/"),
             ("Wallonia.be — L'écosystème wallon champion du biopharma", "https://www.wallonia.be/fr/actualites/bio-san-diego-lecosysteme-wallon-champion-du-biopharma"),
             ("Bureau fédéral du Plan — Budget économique 2026", "https://www.plan.be/fr/publications/budget-economique-2026-perspectives-economiques")],
 "related": ["meso/niches-strategiques/", "micro/emploi-territoires/", "monde/geoeconomie/"],
},
{
 "slug": "belgique/energie-climat/", "section": S,
 "title": "Énergie et climat en Belgique : nucléaire prolongé, PNEC, ETS2, éolien offshore",
 "h1": "Énergie et climat : le pragmatisme belge",
 "desc": "Prolongation de Doel 4 et Tihange 3 jusqu'en 2035, reprise des déchets nucléaires par l'État, plan national énergie-climat critiqué par la Commission, ETS2 et île énergétique.",
 "lede": "Ayant voté la sortie du nucléaire en 2003, la Belgique a dû prolonger deux réacteurs. Son plan climat, lui, souffre de l'éclatement des compétences entre quatre gouvernements.",
 "keywords": ["nucléaire Belgique", "Doel 4 Tihange 3", "PNEC Belgique", "ETS2", "île Princesse Elisabeth", "transition énergétique Belgique"],
 "about": [BE, ("Centrale nucléaire de Doel", W + "Centrale_nucl%C3%A9aire_de_Doel", "Place"), ("Centrale nucléaire de Tihange", W + "Centrale_nucl%C3%A9aire_de_Tihange", "Place")],
 "level_label": "Méso",
 "body": f"""
<h2>Le revirement nucléaire</h2>
<p>La loi de 2003 prévoyait la sortie du nucléaire en 2025. La crise énergétique de 2022 a rendu ce calendrier intenable. En 2025, l'État et ENGIE Electrabel ont conclu un accord exécutoire : <strong>Doel 4 et Tihange 3</strong> fonctionneront dix années supplémentaires, jusqu'en 2035, avec un redémarrage prévu en novembre 2025 sous contrôle de l'autorité de sûreté.</p>
<p>La contrepartie est lourde : l'État reprend la responsabilité de la gestion finale des déchets de haute activité, en échange d'un versement forfaitaire de 15 milliards d'euros par ENGIE. Une forme de nationalisation du passif nucléaire, qui transfère un risque de coût à long terme vers le contribuable.</p>
<h2>Le plan national énergie-climat (PNEC)</h2>
<p>Le PNEC 2021-2030 assemble le plan fédéral et ceux des trois Régions. Sa mise à jour a été validée avec un an de retard, en octobre 2025. L'évaluation de la Commission européenne, début 2026, est sévère :</p>
<ul>
<li>consommation d'énergie primaire projetée à 41,3 Mtep en 2030, contre un objectif de référence de 34 Mtep ;</li>
<li>renouvelables sous-dimensionnés, investissements peu chiffrés ;</li>
<li>absence d'analyse d'impact social de l'ETS2 pour la Flandre et Bruxelles.</li>
</ul>
<p>Fédéral et Régions se disputent en outre la répartition des recettes des enchères de CO₂.</p>
<h2>L'ETS2 et le pouvoir d'achat</h2>
<p>Le second marché européen du carbone, qui couvrira le chauffage et le transport routier, doit démarrer en 2027-2028. Le Bureau du Plan anticipe un pic d'inflation à 2,4 % en 2027 lié à la hausse des combustibles fossiles. Sans compensation ciblée, les ménages modestes, souvent mal isolés, seront les plus touchés ({L("micro/pouvoir-d-achat/", "pouvoir d'achat")}).</p>
<h2>La mer du Nord, centrale verte</h2>
<p>L'{L("meso/niches-strategiques/", "île énergétique Princesse Élisabeth")} doit raccorder 3,5 GW d'éolien offshore et interconnecter la Belgique au Royaume-Uni et au Danemark. Le tax shift fédéral (baisse des accises sur l'électricité, hausse de la TVA sur les fossiles) vise à favoriser l'électrification.</p>
{kpis([("2035", "fin prévue de Doel 4 et Tihange 3"), ("15 Md€", "versés par ENGIE contre la reprise des déchets"), ("41,3 Mtep", "consommation primaire projetée en 2030 (objectif 34)"), ("3,5 GW", "éolien raccordé à l'île énergétique")])}
""",
 "sources": [("SFEN — L'État belge et Engie scellent l'avenir de Tihange 3 et Doel 4", "https://www.sfen.org/rgn/belgique-etat-belge-engie-scellent-avenir-tihange-3-doel-4/"),
             ("SPF Économie — Prolongation de Doel 4 et Tihange 3", "https://economie.fgov.be/fr/themes/energie/sources-et-vecteurs-denergie/nucleaire/prolongation-de-la-duree-de"),
             ("Climat.be — Plan national énergie et climat", "https://climat.be/politique-climatique/belge/nationale/plan-national-energie-et-climat"),
             ("Climat.be — Mise à jour finale du PNEC 2025", "https://climat.be/actualites/2025/mise-a-jour-finale-du-plan-national-belge-en-matiere-denergie-et-de-climat-2025"),
             ("Renouvelle — Nationalisation du nucléaire : qui payera ?", "https://www.renouvelle.be/fr/nationalisation-du-nucleaire-en-belgique-qui-payera-et-combien/")],
 "related": ["monde/climat-limites-planetaires/", "meso/niches-strategiques/", "micro/pouvoir-d-achat/"],
},
{
 "slug": "belgique/bruxelles/", "section": S,
 "title": "Bruxelles, capitale paradoxale : richesse, pauvreté, dette, gouvernance",
 "h1": "Bruxelles, capitale paradoxale",
 "desc": "PIB élevé mais habitants appauvris, dette régionale passée de 6 à 15 milliards, navetteurs, 613 jours de blocage, fonction internationale : le paradoxe bruxellois expliqué.",
 "lede": "Bruxelles produit beaucoup de richesse, mais une grande partie échappe à ses habitants et à ses finances. En 2026, près d'un Bruxellois sur deux déclare des difficultés financières.",
 "keywords": ["Bruxelles", "paradoxe bruxellois", "dette Région bruxelloise", "pauvreté Bruxelles", "navetteurs", "gouvernement bruxellois"],
 "about": [("Région de Bruxelles-Capitale", WD + "Q240", "AdministrativeArea"), BE],
 "level_label": "Méso",
 "body": f"""
<h2>Le paradoxe</h2>
<p>La Région de Bruxelles-Capitale affiche l'un des PIB par habitant les plus élevés d'Europe, mais le revenu de ses habitants est inférieur à la moyenne belge. Explication : une grande partie des emplois est occupée par des navetteurs flamands et wallons, qui paient leur impôt des personnes physiques dans leur Région de résidence. Environ <strong>20 % de la masse salariale</strong> générée à Bruxelles est ainsi imposée ailleurs.</p>
{kpis([("49 %", "des Bruxellois déclarent des difficultés financières (2026)"), ("6 → 15 Md€", "dette régionale en sept ans"), ("64,7 %", "taux d'emploi à Bruxelles (contre 77,3 % en Flandre)"), ("613 jours", "de formation du gouvernement")])}
<h2>Une dette qui explose</h2>
<p>La dette régionale est passée d'environ 6 à 15 milliards d'euros en sept ans. Les causes avancées : sous-financement structurel, coûts de la fonction de capitale internationale (sécurité, mobilité, infrastructures), investissements dans le métro et le logement, et dépenses sociales. Le gouvernement Dilliès vise un retour progressif à l'équilibre.</p>
<h2>Une gouvernance complexe</h2>
<p>19 communes, une Région, trois commissions communautaires (COCOF, VGC, COCOM), des compétences fédérales, communautaires et régionales entremêlées, des majorités distinctes par groupe linguistique : Bruxelles cumule les niveaux. Le blocage de 2024-2026 en a été la démonstration ({L("belgique/gouvernements/", "gouvernements")}).</p>
<h2>Une ville-monde</h2>
<p>Classée deuxième ville la plus cosmopolite du monde par l'Organisation internationale pour les migrations (2015), Bruxelles accueille institutions européennes, OTAN, lobbys, médias et diplomates. Cette fonction internationale fait vivre l'économie locale mais tire aussi les prix du logement vers le haut.</p>
<h2>Sécurité</h2>
<p>La violence liée au narcotrafic touche certains quartiers (Anderlecht, Molenbeek) ; des fusillades répétées ont conduit à des plans d'action spécifiques. Voir {L("micro/narcotrafic-anvers/", "narcotrafic")}.</p>
{levels("Bruxelles, capitale de l'UE et de l'OTAN, est une vitrine mondiale.", "Une Région sous-financée prise entre Flandre et Wallonie, sous tutelle budgétaire de fait.", "Loyers élevés, chômage des jeunes, pauvreté infantile, mais aussi forte vitalité associative et culturelle.")}
""",
 "sources": [("Brussels Governance Monitor — Le paradoxe bruxellois", "https://governance.brussels/fr/comprendre/paradoxe-bruxellois"),
             ("BX1 — 49 % des Bruxellois en difficulté financière", "https://bx1.be/categories/news/bruxelles-decroche-un-triste-record-49-des-habitants-en-difficulte-financiere/"),
             ("La Libre — Boris Dilliès présente une feuille de route resserrée (23/02/2026)", "https://www.lalibre.be/belgique/politique-belge/2026/02/23/accord-bruxellois-boris-dillies-presente-une-feuille-de-route-resserree-au-parlement-regional-FNWLAAWHWBA3XDK47FD7DIYXAU/"),
             ("Revue Politique — Bruxelles n'est pas une confédération", "https://www.revuepolitique.be/bruxelles-nest-pas-une-confederation/"),
             ("Statbel — Emploi et chômage", "https://statbel.fgov.be/fr/themes/emploi-formation/marche-du-travail/emploi-et-chomage")],
 "related": ["belgique/gouvernements/", "micro/emploi-territoires/", "meso/union-europeenne/"],
},
]
