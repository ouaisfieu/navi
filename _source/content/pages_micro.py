from h import L, kpis, bars, table, callout, levels

W = "https://fr.wikipedia.org/wiki/"
WD = "https://www.wikidata.org/wiki/"
S = "micro"
BE = ("Belgique", WD + "Q31", "Country")

PAGES = [
{
 "slug": "micro/", "section": S, "kind": "hub",
 "title": "Micro : société, territoires et vécu en Belgique",
 "h1": "Micro : ce que la géopolitique fait au quotidien",
 "desc": "L'échelle micro : pouvoir d'achat et indexation, emploi par région, école, pensions, identités, narcotrafic, cybersécurité et vie communale en Belgique.",
 "lede": "Les grandes tendances finissent toujours quelque part : sur une fiche de paie, dans une classe, dans un quartier, dans un bureau de vote communal. L'échelle micro observe cet atterrissage.",
 "keywords": ["société belge", "pouvoir d'achat Belgique", "emploi Belgique", "école Belgique", "vivre en Belgique"],
 "about": [BE, ("Sociologie", W + "Sociologie")],
 "body": f"""
<p>La géosociopolitique ne se limite pas aux chancelleries. L'inflation énergétique née de la guerre en Ukraine se lit dans l'indexation des salaires ; la fragmentation commerciale dans le trafic du port d'Anvers et les emplois qui en dépendent ; la polarisation mondiale dans les résultats d'une commune comme Ninove.</p>
{levels("Chocs mondiaux : énergie, taux d'intérêt, conflits, climat.", "Politiques publiques qui les filtrent : indexation, sécurité sociale, compétences régionales.", "Vécu : revenus, emploi, école, santé, sécurité, sentiment d'appartenance.")}
""",
},
{
 "slug": "micro/pouvoir-d-achat/", "section": S,
 "title": "Pouvoir d'achat en Belgique : indexation en centimes, norme salariale 0 %",
 "h1": "Pouvoir d'achat : l'indexation en centimes et la norme à 0 %",
 "desc": "Comment fonctionne l'indexation automatique des salaires, ce que change « l'indexation en centimes » de 2026 au-delà de 4 000 € bruts, la norme salariale 2025-2026 et l'effet de l'ETS2.",
 "lede": "La Belgique est l'un des rares pays à indexer automatiquement salaires et allocations. En 2026, ce mécanisme emblématique est rogné pour les salaires les plus élevés.",
 "keywords": ["indexation des salaires", "indexation en centimes", "norme salariale 0 %", "pouvoir d'achat Belgique", "loi-programme 2026"],
 "about": [("Indexation des salaires en Belgique", W + "Indexation_des_salaires", "Thing"), BE],
 "level_label": "Micro",
 "body": f"""
<h2>L'indexation automatique</h2>
<p>En Belgique, salaires et allocations suivent l'évolution des prix (indice santé lissé), selon des mécanismes fixés par secteur (commissions paritaires). Défendue par les syndicats (CSC, FGTB), l'indexation a protégé les ménages pendant la crise énergétique de 2022, mais a renchéri le coût du travail par rapport aux pays voisins.</p>
<h2>La norme salariale à 0 %</h2>
<p>La loi de 1996 sur la compétitivité encadre l'évolution des salaires. Pour 2025-2026, la marge a été fixée à <strong>0 %</strong> : aucune hausse réelle au-delà de l'indexation et des augmentations barémiques.</p>
<h2>L'« indexation en centimes »</h2>
<p>Abroger l'indexation était une ligne rouge pour Vooruit. Le compromis, inscrit dans la <strong>loi-programme du 30 mai 2026</strong>, plafonne temporairement l'indexation :</p>
<ul>
<li>deux cycles, à partir de juin 2026 puis de janvier 2028 ;</li>
<li>la part du salaire brut mensuel au-delà de <strong>4 000 €</strong> (2 000 € pour les allocations de remplacement) n'est plus indexée, jusqu'à un différentiel cumulé de 2 % ;</li>
<li>l'employeur économise, mais reverse 50 % de ce gain via une cotisation spéciale de modération salariale.</li>
</ul>
{table(["Salaire brut mensuel", "Indexation classique (2 %)", "Avec plafond à 4 000 €", "Manque à gagner"], [
 ("3 000 €", "+60 €", "+60 €", "0 €"),
 ("4 000 €", "+80 €", "+80 €", "0 €"),
 ("5 000 €", "+100 €", "+80 €", "−20 €"),
 ("7 000 €", "+140 €", "+80 €", "−60 €"),
], "Exemple pour une indexation de 2 %")}
{callout("<p>Le dispositif est présenté comme touchant les « hauts salaires ». Il concerne aussi des profils qualifiés de la classe moyenne (ingénieurs, cadres, enseignants en fin de carrière dans certains cas), et, pour les allocations, un seuil plus bas.</p>", "lilac", "Qui est concerné ?")}
<h2>Les pressions à venir</h2>
<ul>
<li><strong>Énergie</strong> : la TVA sur le gaz et le mazout passe progressivement de 6 % à 12 % d'ici 2029, compensée par une baisse des accises sur l'électricité.</li>
<li><strong>ETS2</strong> : le nouveau marché carbone européen pourrait porter l'inflation à 2,4 % en 2027.</li>
<li><strong>Alimentation</strong> : l'indice FAO des prix alimentaires remonte (133,3 points en août 2026).</li>
</ul>
<h2>Bruxelles, point de tension</h2>
<p>En 2026, <strong>49 % des Bruxellois</strong> déclarent être en difficulté financière. Loyers élevés, chômage et faibles revenus s'y cumulent ({L("belgique/bruxelles/", "le paradoxe bruxellois")}).</p>
""",
 "sources": [("UCM — Modération salariale dès juin 2026 : la loi est votée", "https://www.ucm.be/actualites/moderation-salariale-des-juin-2026-la-loi-est-votee"),
             ("CSC — Index salaire", "https://www.lacsc.be/vos-droits/travailler-dans-le-secteur-prive/salaire/index-salaire"),
             ("SPF Emploi — Norme salariale", "https://emploi.belgique.be/fr/themes/remuneration/norme-salariale"),
             ("Deloitte Legal — L'indexation en centimes et la modération salariale", "https://www.deloittelegal.be/lg/en/blogs/la-nouvelle-indexation-en-centime-et-la-mod-ration-salariale.html"),
             ("BX1 — 49 % des Bruxellois en difficulté financière", "https://bx1.be/categories/news/bruxelles-decroche-un-triste-record-49-des-habitants-en-difficulte-financiere/")],
 "related": ["micro/emploi-territoires/", "belgique/energie-climat/", "belgique/finances-publiques/"],
},
{
 "slug": "micro/emploi-territoires/", "section": S,
 "title": "Emploi en Belgique 2026 : taux d'emploi par région, chômage, activation",
 "h1": "Emploi : trois Belgiques",
 "desc": "Taux d'emploi 2026 en Flandre, Wallonie et Bruxelles, écart selon la qualification, chômage des jeunes, objectif de 80 % et politique d'activation de l'Arizona.",
 "lede": "72,8 % de taux d'emploi en moyenne, mais 77,3 % en Flandre et 64,7 % à Bruxelles : la carte de l'emploi raconte une Belgique à plusieurs vitesses.",
 "keywords": ["taux d'emploi Belgique 2026", "chômage Wallonie", "emploi Bruxelles", "Forem VDAB Actiris", "activation"],
 "about": [BE, ("Chômage", W + "Ch%C3%B4mage")],
 "level_label": "Micro",
 "body": f"""
<h2>La carte de l'emploi</h2>
{bars("Taux d'emploi des 20-64 ans, 2026 (Statbel)", [("Flandre", 77.3, "77,3 %"), ("Belgique", 72.8, "72,8 %"), ("Wallonie", 67.6, "67,6 %"), ("Bruxelles-Capitale", 64.7, "64,7 %"), ("Objectif fédéral 2029", 80, "80 %")], maxv=100, note="Source : Statbel, enquête sur les forces de travail. Échelle de 0 à 100 %.")}
<p>L'objectif de 80 % d'ici 2029, inscrit dans l'accord de gouvernement, suppose des centaines de milliers d'emplois supplémentaires — surtout au sud et à Bruxelles.</p>
<h2>La qualification, premier facteur</h2>
{bars("Taux d'emploi selon le niveau d'instruction (Statbel)", [("Diplôme de l'enseignement supérieur", 85.4, "85,4 %"), ("Peu qualifiés", 46.4, "46,4 %")], maxv=100)}
<p>Près de 40 points séparent les diplômés du supérieur des personnes peu qualifiées. Une partie de l'écart régional s'explique par la structure des qualifications, la mobilité et la discrimination à l'embauche, documentée à Bruxelles.</p>
<h2>La Wallonie et ses jeunes</h2>
<p>L'IWEPS relève une détérioration en 2025 : le chômage administratif augmente de 9,6 % sur un an, et le taux de chômage des jeunes atteint 31,4 %.</p>
<h2>L'activation</h2>
<ul>
<li>allocations de chômage limitées dans le temps ;</li>
<li>chômeurs temporaires invités à s'inscrire rapidement auprès du Forem, du VDAB ou d'Actiris ;</li>
<li>évaluation du potentiel de travail des malades de longue durée après huit semaines, sanctions en cas de refus d'un trajet de réintégration ;</li>
<li>fin de la distinction ouvrier-employé (statut unique).</li>
</ul>
{callout("<p>Les partisans y voient un rattrapage nécessaire pour financer la sécurité sociale ; les syndicats et CPAS craignent un transfert de charges vers l'aide sociale communale. L'enjeu se joue au niveau local.</p>", "lilac", "Débat")}
""",
 "sources": [("Statbel — Emploi et chômage", "https://statbel.fgov.be/fr/themes/emploi-formation/marche-du-travail/emploi-et-chomage"),
             ("Statbel — Taux d'emploi 72,8 % (2026)", "https://statbel.fgov.be/fr/nouvelles/le-taux-demploi-se-stabilise-728-au-premier-trimestre-2026"),
             ("IWEPS — Évolution du chômage administratif en Wallonie", "https://www.iweps.be/indicateur-statistique/evolution-chomage-administratif/"),
             ("UCM — Mesures de l'Arizona pour les employeurs", "https://www.ucm.be/actualites/accord-du-gouvernement-federal-les-mesures-prevues-par-larizona-impactant-les-employeurs")],
 "related": ["micro/pouvoir-d-achat/", "belgique/economie/", "micro/ecole/"],
},
{
 "slug": "micro/ecole/", "section": S,
 "title": "École en Fédération Wallonie-Bruxelles : Pacte d'excellence et tronc commun",
 "h1": "L'école francophone et le Pacte pour un enseignement d'excellence",
 "desc": "Déploiement du tronc commun jusqu'à 15 ans dès la rentrée 2026, cinq heures de mathématiques, DAccE, inégalités PISA et arbitrages budgétaires de la FWB.",
 "lede": "L'avenir économique d'un pays se joue dans ses classes. L'école francophone, marquée par de fortes inégalités sociales, vit une réforme d'ampleur sous contrainte budgétaire.",
 "keywords": ["Pacte d'excellence", "tronc commun", "enseignement Fédération Wallonie-Bruxelles", "PISA Belgique", "DAccE"],
 "about": [("Fédération Wallonie-Bruxelles", W + "F%C3%A9d%C3%A9ration_Wallonie-Bruxelles", "GovernmentOrganization"), ("Pacte pour un enseignement d'excellence", W + "Pacte_pour_un_enseignement_d%27excellence")],
 "level_label": "Micro",
 "body": f"""
<h2>Le diagnostic</h2>
<p>Les enquêtes PISA épinglent régulièrement l'enseignement francophone pour la force du lien entre origine sociale et résultats, et pour l'orientation précoce qui cantonnait des élèves défavorisés dans des filières de relégation. L'enseignement relève des Communautés : la Flandre et la Communauté germanophone ont leurs propres systèmes.</p>
<h2>Le tronc commun</h2>
<p>Élément central du Pacte, le <strong>tronc commun</strong> garde tous les élèves dans un socle d'apprentissages unifié jusqu'à 15 ans (fin de la 3<sup>e</sup> secondaire). Il se déploie dans le secondaire à partir de la rentrée 2026 :</p>
<ul>
<li>suppression du premier degré différencié ;</li>
<li>cinq périodes de mathématiques au lieu de quatre, deux périodes de compétences numériques ;</li>
<li>Dossier d'accompagnement de l'élève (DAccE) qui suit les progrès et difficultés ;</li>
<li>co-interventions pédagogiques, recours accru aux logopèdes.</li>
</ul>
<h2>La contrainte budgétaire</h2>
<p>Avec un déficit de l'ordre de 1,6 milliard d'euros en 2026, la FWB, dirigée par une majorité MR-Les Engagés, a reporté certains dispositifs du Pacte et remanié le financement de la gratuité scolaire (par exemple, la gratuité des repas chauds a été retirée du budget de l'enseignement). Les enseignants ont mené plusieurs mouvements de grève contre les mesures d'économie et la réforme de leur statut.</p>
{callout("<p>L'école cristallise la tension entre ambition égalitaire et finances contraintes par la loi spéciale de financement : " + L("belgique/finances-publiques/", "voir les finances publiques") + ".</p>", "warn", "Lien avec les finances")}
""",
 "sources": [("FWB — Le tronc commun dans le secondaire", "https://pactepourunenseignementdexcellence.cfwb.be/mesures/le-tronc-commun-secondaire/"),
             ("Ligue de l'enseignement — Le tronc commun", "https://ligue-enseignement.be/education-enseignement/legislation/le-pacte-pour-un-enseignement-dexcellence-le-tronc-commun"),
             ("BX1 — La majorité MR-Engagés reporte des dispositifs du Pacte", "https://bx1.be/categories/news/la-majorite-mr-engages-reporte-plusieurs-dispositifs-du-pacte-dexcellence/"),
             ("Laïcité.be — Pacte d'excellence : évolution sans révolution", "https://www.laicite.be/magazine-article/pacte-dexcellence%E2%80%89-evolution-revolution/")],
 "related": ["micro/emploi-territoires/", "belgique/finances-publiques/", "belgique/federalisme/"],
},
{
 "slug": "micro/vieillissement-pensions/", "section": S,
 "title": "Vieillissement et réforme des pensions en Belgique (2026)",
 "h1": "Vieillissement et réforme des pensions",
 "desc": "Coût du vieillissement selon le Comité d'étude sur le vieillissement 2026, bonus pension, pension anticipée, pension minimum et assimilation des périodes de maladie.",
 "lede": "Le vieillissement est le « moteur silencieux » de la dégradation budgétaire belge. La réforme des pensions de 2026 veut allonger les carrières sans casser la solidarité.",
 "keywords": ["réforme des pensions 2026", "bonus pension", "vieillissement Belgique", "Comité d'étude sur le vieillissement", "pension anticipée"],
 "about": [BE, ("Retraite", W + "Retraite_(%C3%A9conomie)")],
 "level_label": "Micro",
 "body": f"""
<h2>Le coût du vieillissement</h2>
<p>Selon le rapport 2026 du Comité d'étude sur le vieillissement (Bureau du Plan), les dépenses sociales liées à l'âge (pensions, soins de santé, incapacité…) passeront de <strong>25,7 % du PIB en 2025 à 27,2 % en 2050</strong>. Ces 1,5 point de PIB supplémentaires pèsent sur la trajectoire de dette.</p>
<h2>La réforme</h2>
<p>Approuvée début 2026, elle combine incitants et restrictions :</p>
<ul>
<li>réintroduction d'un <strong>bonus pension</strong> pour ceux qui travaillent au-delà des conditions de départ ;</li>
<li>conditions d'accès à la pension anticipée resserrées ;</li>
<li>suppression progressive, à partir de 2027, de l'âge de mise à la retraite d'office pour certaines professions (officiers supérieurs) ;</li>
<li>les périodes de maladie restent assimilées à du travail pour les 5 000 jours requis pour la pension minimum garantie.</li>
</ul>
<p>L'âge légal de la pension passe de 65 à 66 ans en 2025, puis à 67 ans en 2030, conformément à une réforme antérieure.</p>
<h2>Les effets</h2>
<p>Le Comité conclut que ces mesures freinent la croissance des dépenses, au prix d'une baisse lente du niveau de vie relatif des futurs pensionnés par rapport aux actifs. Les syndicats dénoncent une pénalisation des carrières longues et pénibles, notamment des femmes aux carrières interrompues.</p>
{levels("Vieillissement de toute l'Europe, taux d'intérêt plus élevés.", "Règles budgétaires européennes, arbitrage entre défense et sécurité sociale.", "Âge de départ, montant de pension, choix de carrière et d'épargne.")}
""",
 "sources": [("Bureau fédéral du Plan — Comité d'étude sur le vieillissement, rapport 2026", "https://www.plan.be/fr/publications/comite-detude-sur-le-vieillissement-rapport-annuel-0"),
             ("Service fédéral des Pensions — Réforme des pensions 2025-2029", "https://www.sfpd.fgov.be/fr/changements/reforme-des-pensions")],
 "related": ["belgique/finances-publiques/", "micro/pouvoir-d-achat/", "micro/emploi-territoires/"],
},
{
 "slug": "micro/identites/", "section": S,
 "title": "Flamands, Wallons, Bruxellois : identités, clichés et sentiment national",
 "h1": "Identités belges : des clichés aux données",
 "desc": "Flamands de droite, Wallons de gauche ? Ce que disent les enquêtes ISPO/KU Leuven 2025-2026 sur les valeurs, les priorités électorales et le sentiment d'appartenance.",
 "lede": "Les discours politiques opposent souvent une Flandre travailleuse et conservatrice à une Wallonie assistée et de gauche. Les enquêtes racontent une autre histoire.",
 "keywords": ["identité belge", "Flamands Wallons", "clichés", "sentiment national", "ISPO KU Leuven"],
 "about": [BE, ("Communautés de Belgique", W + "Communaut%C3%A9s_de_Belgique")],
 "level_label": "Micro",
 "body": f"""
<h2>Ce que montrent les enquêtes</h2>
<p>Les études de l'ISPO (KU Leuven) de 2025-2026 comparent les attitudes des électeurs des deux côtés de la frontière linguistique. Sur la protection sociale, l'égalité ou même l'immigration, <strong>les positions sont très proches</strong>. Le clivage est d'abord politique et médiatique, pas sociétal.</p>
<h2>Ce qui diffère : l'agenda</h2>
<ul>
<li>En Flandre, la concurrence N-VA / Vlaams Belang a placé la <strong>migration</strong> en tête des priorités (citée par près d'un électeur sur quatre).</li>
<li>En Wallonie, la préoccupation centrale reste le <strong>pouvoir d'achat</strong> et l'inflation.</li>
</ul>
<p>Les partis étant organisés par communauté, chaque espace médiatique hiérarchise différemment les enjeux, ce qui produit des résultats électoraux divergents à partir de valeurs voisines ({L("belgique/elections-2024/", "élections 2024")}).</p>
<h2>Un sentiment national résilient</h2>
<p>Malgré la fédéralisation, le sentiment d'appartenance belge reste répandu, souvent combiné à une identité régionale. Bruxelles, où plus de la moitié des habitants a des origines étrangères, développe une identité métropolitaine propre, multilingue.</p>
{callout("<p>Des médias comme DaarDaar (traductions d'articles flamands en français) ou les collaborations entre VRT et RTBF tentent de réduire l'étanchéité des espaces publics.</p>", "lilac", "Passerelles")}
<h2>Pourquoi c'est géopolitique</h2>
<p>La cohésion interne conditionne la capacité d'un État à agir à l'extérieur : un pays dont l'avenir institutionnel est incertain négocie moins bien. Inversement, la réussite d'un compromis belge est souvent citée en exemple pour d'autres sociétés plurilingues.</p>
""",
 "sources": [("DaarDaar — Flamands de droite et Wallons de gauche, vraiment ?", "https://daardaar.be/rubriques/societe/flamands-de-droite-et-wallons-de-gauche-vraiment-cette-etude-deconstruit-les-cliches/"),
             ("Les Plats Pays — Belges ou Wallons et Flamands ?", "https://www.les-plats-pays.com/article/belges-ou-wallons-et-flamands-des-identites-sous-tension/"),
             ("Sciences humaines (FESeC) — Le confédéralisme", "https://fesec.scienceshumaines.be/critiquer-belgique-federale-le-confederalisme/")],
 "related": ["belgique/elections-2024/", "belgique/federalisme/", "monde/democratie/"],
},
{
 "slug": "micro/narcotrafic-anvers/", "section": S,
 "title": "Narcotrafic à Anvers et Bruxelles : la Belgique, « narco-État » ?",
 "h1": "Narcotrafic : Anvers, porte d'entrée de la cocaïne en Europe",
 "desc": "Saisies record au port d'Anvers, corruption, violence à Bruxelles, alerte des magistrats, screening de 16 678 travailleurs portuaires et traité de police Benelux.",
 "lede": "Le port qui fait la richesse de la Belgique est aussi la principale porte d'entrée de la cocaïne sud-américaine en Europe. Des magistrats alertent sur un risque de dérive vers un « narco-État ».",
 "keywords": ["narcotrafic Anvers", "cocaïne port d'Anvers", "narco-État Belgique", "fusillades Bruxelles", "criminalité organisée"],
 "about": [("Anvers", WD + "Q12892", "City"), ("Trafic de cocaïne", W + "Trafic_de_coca%C3%AFne")],
 "level_label": "Micro",
 "body": f"""
<h2>L'ampleur</h2>
<p>Les saisies de cocaïne à Anvers ont varié entre plusieurs dizaines et plus de cent tonnes par an. Les douanes estiment qu'elles ne représentent que 10 à 40 % des flux réels. À cela s'ajoutent l'héroïne de la route des Balkans et la production de drogues de synthèse exportées vers l'Asie et le reste de l'Europe.</p>
<h2>L'argent et la corruption</h2>
<p>Un kilo acheté quelques milliers d'euros en Amérique du Sud se revend autour de 30 000 euros en Europe. Ces marges permettent de corrompre dockers, transporteurs, agents publics, et d'installer une économie parallèle. Un juge d'instruction anversois a publiquement alerté en 2025 sur un risque de « narco-État », les institutions étant sous influence des trafiquants.</p>
<h2>La violence</h2>
<p>Règlements de comptes, explosions, enlèvements : la violence liée aux réseaux touche Anvers et Bruxelles, où le taux d'homicide atteint 3,19 pour 100 000 habitants, avec des fusillades concentrées dans certains quartiers d'Anderlecht et de Molenbeek.</p>
<h2>Les réponses</h2>
{kpis([("16 678", "travailleurs portuaires contrôlés en 2026"), ("≈ 320", "avis négatifs, écartés des postes sensibles"), ("10-40 %", "part estimée des flux réellement saisie"), ("3,19", "homicides / 100 000 hab. à Bruxelles")])}
<ul>
<li><strong>Screening</strong> de l'Autorité nationale de sécurité au port ;</li>
<li>renforcement de la police maritime et de la douane (scanners) ;</li>
<li><strong>Traité de police Benelux</strong> : bases de données partagées, enquêtes conjointes transfrontalières ;</li>
<li>coopération avec les pays d'origine (Colombie, Équateur) et l'alliance européenne des ports.</li>
</ul>
{levels("Routes mondiales de la cocaïne, conteneurisation, criminalité transnationale.", "Coopération Benelux et européenne ; capacités de la justice et de la police.", "Jeunes recrutés comme petites mains, habitants exposés à la violence, confiance dans les institutions.")}
""",
 "sources": [("Euractiv — Is Belgium becoming Europe's first narco state?", "https://www.euractiv.com/news/is-belgium-becoming-europes-first-narco-state/"),
             ("AML Intelligence — Antwerp judge warns of narco state (2025)", "https://www.amlintelligence.com/2025/10/insight-belgium-becoming-an-eu-narco-state-warns-antwerp-judge-as-city-institutions-fall-under-influence-of-traffickers/"),
             ("Anadolu — 300+ employees suspended at Belgian port", "https://www.aa.com.tr/en/europe/over-300-employees-suspended-at-belgian-port-after-failing-drug-security-checks/3801552"),
             ("Port of Antwerp-Bruges — Anti-drugs policy", "https://www.portofantwerpbruges.com/en/our-port/people-and-environment/safety/anti-drugs-policy"),
             ("Benelux — Coopération sécuritaire transfrontalière", "https://www.benelux.int/en/post/belgian-and-dutch-limburg-strengthen-cross-border-security/")],
 "related": ["belgique/economie/", "belgique/bruxelles/", "micro/securite-cyber/"],
},
{
 "slug": "micro/securite-cyber/", "section": S,
 "title": "Cybersécurité et menaces hybrides en Belgique : NIS2, CCB, résilience",
 "h1": "Cybersécurité et menaces hybrides : la résilience au quotidien",
 "desc": "Directive NIS2 et enregistrement de 2 410 organisations auprès du CCB, Centre de crise national, Conseil national de sécurité, désinformation et protection des infrastructures.",
 "lede": "Ports, hôpitaux, réseaux électriques, communes : la guerre hybride vise aussi les organisations ordinaires. La directive NIS2 oblige des milliers d'entre elles à se protéger.",
 "keywords": ["NIS2 Belgique", "Centre pour la cybersécurité Belgique", "menaces hybrides", "cyberattaque", "résilience"],
 "about": [("Centre pour la Cybersécurité Belgique", W + "Centre_pour_la_cybers%C3%A9curit%C3%A9_Belgique", "GovernmentOrganization"), ("Directive NIS2", W + "Directive_NIS_2")],
 "level_label": "Micro",
 "body": f"""
<h2>Les acteurs</h2>
<ul>
<li><strong>Centre pour la cybersécurité Belgique (CCB)</strong> : autorité nationale, pilote de NIS2, centre de réponse aux incidents (CERT.be).</li>
<li><strong>Centre de crise national (NCCN)</strong> : protection des infrastructures critiques, gestion de crise.</li>
<li><strong>Conseil national de sécurité</strong> : se réunit sur la recrudescence des menaces hybrides.</li>
<li><strong>Cyber Command</strong> de la Défense : opérations cyber et guerre de l'information.</li>
</ul>
<h2>NIS2 : un choc organisationnel</h2>
<p>La directive européenne NIS2 étend les obligations de cybersécurité à de nombreux secteurs (énergie, transports, santé, finance, eau, numérique, administrations…). Entre fin 2024 et début 2026, plus de <strong>2 410 organisations</strong> se sont enregistrées auprès du CCB, avec des exigences de gestion des risques, de notification d'incidents et des sanctions possibles.</p>
<h2>Menaces concrètes</h2>
<ul>
<li>rançongiciels contre hôpitaux, communes, entreprises ;</li>
<li>attaques par déni de service lors d'événements politiques ;</li>
<li>campagnes de désinformation, parfois dopées à l'IA ;</li>
<li>risques de sabotage d'infrastructures en mer du Nord ({L("monde/infrastructures-critiques/", "câbles et infrastructures")}).</li>
</ul>
{callout("<p>Le CCB propose des outils gratuits (Safeonweb) pour signaler les messages suspects : chaque citoyen est un maillon de la résilience collective.</p>", "info", "Au niveau individuel")}
<p>À plus long terme, la migration vers la cryptographie post-quantique concernera aussi les administrations et entreprises belges ({L("monde/technologies/", "technologies de rupture")}).</p>
""",
 "sources": [("Industrial Cyber — Belgium's CCB reports NIS2 registration surge (2 410 organisations)", "https://industrialcyber.co/regulation-standards-and-compliance/belgiums-ccb-reports-significant-registration-surge-under-nis2-as-2410-organizations-from-critical-sectors-enrolled/"),
             ("Centre de crise — Protection des infrastructures critiques", "http://crisiscenter.be/en/role-national-crisis-center/risk-assessment-and-protection-critical-infrastructures/protection"),
             ("BX1 — Le Conseil national de sécurité sur les menaces hybrides", "https://bx1.be/categories/news/le-conseil-national-de-securite-se-reunit-vendredi-sur-les-menaces-hybrides/"),
             ("SPF Affaires étrangères — Cybersécurité et réglementation internationale", "http://diplomatie.belgium.be/fr/politique/themes-politiques/sous-la-loupe/cybersecurite-la-necessite-dune-reglementation-internationale")],
 "related": ["monde/technologies/", "monde/infrastructures-critiques/", "meso/otan-defense/"],
},
{
 "slug": "micro/communes/", "section": S,
 "title": "Élections communales 2024 et pouvoir local en Belgique",
 "h1": "Le pouvoir local : communes, provinces et CPAS",
 "desc": "Plus de 560 communes, élections d'octobre 2024, première majorité absolue du Vlaams Belang à Ninove, rôle des CPAS, provinces et sortie annoncée de la Communauté germanophone de la province de Liège.",
 "lede": "C'est à l'échelon communal que la plupart des Belges rencontrent l'État : état civil, écoles, police locale, aide sociale. C'est aussi là que se testent les dynamiques politiques.",
 "keywords": ["élections communales 2024", "communes belges", "Ninove Vlaams Belang", "CPAS", "provinces"],
 "about": [BE, ("Commune de Belgique", W + "Commune_de_Belgique")],
 "level_label": "Micro",
 "body": f"""
<h2>L'architecture locale</h2>
<p>La Belgique compte un peu plus de 560 communes depuis les fusions volontaires en Flandre au 1<sup>er</sup> janvier 2025 (581 auparavant : 300 en Flandre, 262 en Wallonie, 19 à Bruxelles), dix provinces et un CPAS (centre public d'action sociale) par commune. Les pouvoirs locaux relèvent de la tutelle des Régions depuis 2001.</p>
<h2>Les élections d'octobre 2024</h2>
<ul>
<li>En Flandre, le vote n'est plus obligatoire pour les communales : la participation a nettement baissé.</li>
<li>Le Vlaams Belang obtient sa première majorité absolue, à <strong>Ninove</strong>, ce qui met le cordon sanitaire à l'épreuve localement.</li>
<li>En Wallonie, le MR et Les Engagés progressent, prolongeant la tendance de juin.</li>
<li>À Bruxelles, le PS reste fort dans plusieurs communes, tandis que des listes locales et le PTB s'affirment.</li>
</ul>
<h2>Le CPAS, amortisseur social</h2>
<p>La limitation des allocations de chômage dans le temps devrait faire basculer une partie des demandeurs vers le revenu d'intégration payé par les CPAS, avec un impact sur les finances communales, déjà tendues ({L("micro/emploi-territoires/", "emploi")}).</p>
<h2>Les provinces en question</h2>
<p>La Communauté germanophone veut sortir de la province de Liège ; la Wallonie réduit le rôle des provinces. À Bruxelles, il n'y a plus de province depuis 1995.</p>
{callout("<p>Le nombre exact de communes évolue avec les fusions volontaires en Flandre ; consultez Statbel ou l'Agence flamande de l'administration intérieure pour le chiffre à jour.</p>", "warn", "Chiffres mouvants")}
""",
 "sources": [("Wikipédia — Vlaams Belang", W + "Vlaams_Belang"),
             ("21News — La Communauté germanophone va sortir de la province de Liège", "https://www.21news.be/la-communaute-germanophone-va-sortir-de-la-province-de-liege/"),
             ("CRISP — Vocabulaire politique", "https://www.vocabulairepolitique.be/")],
 "related": ["belgique/elections-2024/", "belgique/federalisme/", "micro/identites/"],
},
]
