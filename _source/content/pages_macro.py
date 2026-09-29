from h import L, kpis, bars, table, callout, levels

W = "https://fr.wikipedia.org/wiki/"
WD = "https://www.wikidata.org/wiki/"
S = "macro"

PAGES = [
{
 "slug": "monde/", "section": S, "kind": "hub",
 "title": "Macro : le système-monde en 2026",
 "h1": "Macro : le système-monde en 2026",
 "desc": "Vue d'ensemble de l'échelle macro : polycrise, ordre multipolaire, conflits, réarmement, fragmentation géoéconomique, recul démocratique, limites planétaires et risques technologiques.",
 "lede": "L'échelle macro observe les grandes structures : rapports de puissance entre États et blocs, flux financiers et commerciaux, trajectoires climatiques et technologiques. En 2026, un mot les résume : fragmentation.",
 "keywords": ["géopolitique mondiale 2026", "polycrise", "ordre multipolaire", "système international"],
 "about": [("Relations internationales", W + "Relations_internationales"), ("Géopolitique", W + "G%C3%A9opolitique")],
 "body": f"""
<p>L'ordre international né de la fin de la Guerre froide — hégémonie occidentale, expansion de la démocratie libérale, multilatéralisme structuré — se défait. Le Forum économique mondial parle d'une « ère de la compétition », la Conférence de Munich d'une « politique de la boule de démolition », l'IFRI d'un « nouvel échiquier ». Ces formules décrivent une même réalité : les crises ne s'additionnent plus, elles s'entretiennent.</p>
{kpis([("68 %", "des experts du WEF anticipent un ordre mondial fragmenté d'ici dix ans"), ("2 887 Md$", "de dépenses militaires mondiales en 2025 (SIPRI)"), ("74 %", "de la population mondiale vit en autocratie (V-Dem 2026)"), ("7 / 9", "limites planétaires franchies (PIK, 2025)")])}
<h2>Comment lire cette rubrique</h2>
<p>Chaque dossier part d'une dynamique mondiale, puis indique ses répercussions aux échelles inférieures : l'Europe et les États (échelle {L("meso/", "méso")}), puis les sociétés et les territoires (échelle {L("micro/", "micro")}). Les liens vers la {L("belgique/", "Belgique")} montrent comment un petit pays très ouvert encaisse — ou amplifie — ces chocs.</p>
{levels("Rivalité sino-américaine, réarmement, dédollarisation partielle, dépassement des limites planétaires.", "Réponses de l'UE et de l'OTAN, politiques des États moyens comme la Belgique, rôle des régions.", "Prix de l'énergie et de l'alimentation, emploi, sentiment d'insécurité, confiance dans les institutions.")}
<p>Pour commencer : {L("monde/polycrise/", "la polycrise, grille de lecture")}, puis {L("monde/ordre-multipolaire/", "le nouvel ordre multipolaire")}.</p>
""",
},
{
 "slug": "monde/polycrise/", "section": S,
 "title": "La polycrise : comprendre l'enchevêtrement des crises mondiales",
 "h1": "La polycrise, grille de lecture du monde en 2026",
 "desc": "Définition de la polycrise (Cascade Institute), modèles d'impacts croisés, rapports WEF 2026 et Munich 2026 : pourquoi les crises mondiales se renforcent mutuellement.",
 "lede": "Une polycrise n'est pas une accumulation de problèmes : c'est un système où chaque crise modifie les autres. Comprendre ces boucles est la condition pour agir à la bonne échelle.",
 "keywords": ["polycrise", "Cascade Institute", "Global Risks Report 2026", "Munich Security Report 2026", "risques systémiques"],
 "about": [("Polycrise", W + "Polycrise"), ("Risque systémique", W + "Risque_syst%C3%A9mique")],
 "level_label": "Macro",
 "body": f"""
<h2>Une définition précise</h2>
<p>Le <strong>Cascade Institute</strong> définit la polycrise comme l'enchevêtrement causal de crises multiples au sein de systèmes mondiaux interdépendants, produisant des boucles de rétroaction et des effets en cascade. La différence avec une simple « période difficile » est structurelle : une crise énergétique renchérit l'alimentation, qui alimente l'instabilité politique, qui fragilise la coopération climatique, qui aggrave à son tour les chocs agricoles.</p>
<p>Le <em>Polycrisis Core Model</em>, construit par analyse d'impacts croisés à partir de plus de 1 800 jugements d'experts, explore plus de quatre millions de futurs possibles d'ici 2040. Il montre que le système converge vers un petit nombre d'« attracteurs » stables : onze scénarios, dont la plupart relèvent du déclin illibéral ou du chaos (l'attracteur surnommé « Mad Max »). Un attracteur « Hope » existe, mais son bassin est étroit et dépend d'interventions rapides, notamment la préservation des institutions démocratiques.</p>
{callout("<p>Le modèle ne prédit pas l'avenir : il indique quelles combinaisons de facteurs se stabilisent. Sa leçon principale est politique — les institutions démocratiques sont un facteur de résilience, pas un luxe.</p>", "lilac", "À retenir")}
<h2>Ce que disent les grands rapports de 2026</h2>
<h3>Forum économique mondial — Global Risks Report 2026</h3>
<ul>
<li>La <strong>confrontation géoéconomique</strong> est le risque le plus susceptible de déclencher une crise mondiale en 2026 (18 % des experts), devant les conflits armés interétatiques (14 %).</li>
<li>La <strong>désinformation</strong> figure au deuxième rang des risques à court terme.</li>
<li>Les <strong>conséquences indésirables de l'IA</strong> connaissent la plus forte progression : du 30<sup>e</sup> rang à deux ans au 5<sup>e</sup> rang à dix ans.</li>
<li>À dix ans, les risques environnementaux dominent : événements extrêmes, perte de biodiversité, bouleversement des écosystèmes.</li>
</ul>
<h3>Conférence de Munich — « Under Destruction »</h3>
<p>Le rapport 2026 décrit une « politique de la boule de démolition » : des puissances historiquement garantes de l'ordre, au premier rang desquelles les États-Unis, démantèlent institutions multilatérales, libre-échange et alliances au profit d'arrangements <em>ad hoc</em> et d'un protectionnisme coercitif. Il souligne aussi une crise de confiance : dans presque tous les pays du G7 sondés, seule une petite minorité pense que les politiques actuelles amélioreront le sort des générations futures.</p>
<h3>IFRI — RAMSES 2026, « Un nouvel échiquier »</h3>
<p>L'institut français interroge la gouvernabilité d'un monde où la « mondialisation heureuse » a cédé la place à une course à la puissance, avec des puissances moyennes qui imposent leurs normes régionales.</p>
<h2>Les cinq boucles principales</h2>
{table(["Boucle", "Mécanisme", "Dossier"], [
 ("Dette ↔ climat", "Les États surendettés ne financent pas l'adaptation ; les catastrophes creusent la dette.", L("monde/geoeconomie/", "Géoéconomie")),
 ("Désinformation ↔ polarisation", "L'IA générative industrialise le faux ; la polarisation empêche le consensus minimal.", L("monde/democratie/", "Démocratie")),
 ("Réarmement ↔ budgets sociaux", "Les hausses militaires évincent dépenses sociales et climatiques.", L("monde/rearmement-nucleaire/", "Réarmement")),
 ("Minerais ↔ transition", "La transition dépend de chaînes dominées par la Chine, qui les utilise comme levier.", L("monde/geoeconomie/", "Géoéconomie")),
 ("Technologie ↔ sécurité", "IA, biologie de synthèse et quantique abaissent le coût de la destruction.", L("monde/technologies/", "Technologies")),
], "Boucles de rétroaction de la polycrise")}
<h2>Un monde « perdant-perdant »</h2>
<p>La Conférence de Munich parle d'un paradigme <em>lose-lose</em> : les gouvernements privilégient des gains relatifs de court terme, quitte à réduire le gâteau commun. Chaque acteur y gagne peut-être une position ; tous y perdent en sécurité et en prospérité.</p>
{levels("Les boucles se jouent entre grandes puissances, marchés et écosystèmes.", "L'UE tente de bâtir une « autonomie stratégique » ; la Belgique arbitre entre réarmement, désendettement et transition.", "Les ménages ressentent la polycrise par les prix, l'emploi et l'anxiété face à l'avenir.")}
<h2>Et la Belgique ?</h2>
<p>Petite économie ouverte (commerce extérieur supérieur à 150 % du PIB), hôte de l'UE et de l'OTAN, la Belgique concentre plusieurs de ces boucles sur son territoire : {L("meso/euroclear-avoirs-russes/", "Euroclear et les avoirs russes")}, {L("belgique/finances-publiques/", "procédure pour déficit excessif")} face au réarmement, {L("micro/narcotrafic-anvers/", "narcotrafic au port d'Anvers")}.</p>
""",
 "sources": [("Cascade Institute — Polycrisis", "https://cascadeinstitute.org/polycrisis/"),
             ("WEF — Global Risks Report 2026", "https://www.weforum.org/publications/global-risks-report-2026/"),
             ("Munich Security Report 2026 — Under Destruction", "https://securityconference.org/en/msc-kick-off/"),
             ("IFRI — RAMSES 2026. Un nouvel échiquier", "https://www.ifri.org/fr/sommaires-presentation-de-ledition/ramses/ramses-2026-un-nouvel-echiquier"),
             ("Cambridge — Understanding polycrisis", "https://www.cambridge.org/core/journals/global-sustainability")],
 "related": ["monde/ordre-multipolaire/", "monde/climat-limites-planetaires/", "meso/union-europeenne/"],
},
{
 "slug": "monde/ordre-multipolaire/", "section": S,
 "title": "Ordre multipolaire, axe CRINK, BRICS et dédollarisation en 2026",
 "h1": "Le nouvel ordre multipolaire : CRINK, BRICS et limites de la dédollarisation",
 "desc": "Consolidation Chine-Russie-Iran-Corée du Nord, sommet BRICS de New Delhi 2026, mBridge et part du dollar dans les réserves : ce qui change vraiment dans l'ordre mondial.",
 "lede": "Le monde n'est pas en train de basculer d'un hégémon à un autre. Il se fragmente en blocs, en alignements opportunistes et en « plomberies » financières parallèles.",
 "keywords": ["CRINK", "BRICS 2026", "dédollarisation", "mBridge", "multipolarité", "Sud global"],
 "about": [("BRICS", W + "BRICS"), ("Chine", WD + "Q148", "Country"), ("Russie", WD + "Q159", "Country"), ("Iran", WD + "Q794", "Country"), ("Corée du Nord", WD + "Q423", "Country")],
 "level_label": "Macro",
 "body": f"""
<h2>Un ordre fragmenté</h2>
<p>Selon le Forum économique mondial, 68 % des experts voient la décennie à venir sous le signe d'un ordre fragmenté ; seuls 6 % croient encore à un ordre unipolaire fondé sur des règles. La multipolarité n'est pas un équilibre stable entre pôles : c'est un paysage contesté, où la confrontation remplace la coopération et où chaque puissance moyenne négocie au cas par cas.</p>
<h2>L'axe « CRINK »</h2>
<p>Les analystes américains désignent par l'acronyme CRINK l'alignement entre <strong>Chine, Russie, Iran et Corée du Nord</strong>. Il ne s'agit pas d'une alliance formelle, mais d'un faisceau d'intérêts communs : contourner les sanctions et l'hégémonie occidentale.</p>
<ul>
<li>La Chine absorbe environ <strong>90 % des exportations de brut iranien</strong>, assurant à Téhéran des revenus vitaux.</li>
<li>Des registres douaniers (janvier 2025 – juin 2026) montrent des livraisons chinoises au ministère iranien de la Défense : traceurs GPS, moteurs électriques, composants électroniques, perchlorate de sodium (précurseur de propergol).</li>
<li>La compagnie Mahan Air, sous sanctions américaines, atteignait environ <strong>39 vols cargo hebdomadaires</strong> depuis la Chine en septembre 2026.</li>
</ul>
<p>Washington fait face à un dilemme : ménager la relation commerciale avec Pékin (les sommets bilatéraux se poursuivent) tout en dénonçant son rôle dans l'armement iranien.</p>
<h2>L'expansion des BRICS</h2>
<p>Après l'adhésion de l'Iran, de l'Égypte, de l'Éthiopie, de l'Arabie saoudite et des Émirats arabes unis, puis de l'Indonésie, les BRICS pèsent environ 40 % du PIB mondial et la moitié de la population. Le <strong>18<sup>e</sup> sommet</strong>, à New Delhi en septembre 2026, a adopté une déclaration de 140 paragraphes soutenant des systèmes de paiement interopérables en monnaies locales et la plateforme <em>mBridge</em>.</p>
<h3>mBridge et « l'immunité de plomberie »</h3>
<p>Développée sous l'égide de la Banque des règlements internationaux avec les banques centrales de Chine, de Thaïlande, des Émirats, de Hong Kong et d'Arabie saoudite, mBridge permet des règlements transfrontaliers instantanés en monnaies numériques de banque centrale. Plus de 55 milliards de dollars y auraient transité, dont l'essentiel en e-CNY. L'unité « BRICS Unit » (40 % or, 60 % panier de devises) reste un projet pilote.</p>
<h2>Le dollar reste central</h2>
{bars("Part du dollar américain dans quelques indicateurs clés (2026)", [("Transactions de change mondiales", 90, "≈ 90 %"), ("Réserves de change mondiales (FMI, T1 2026)", 57.13, "57,13 %"), ("Messages de paiement SWIFT", 51, "≈ 51 %"), ("CIPS chinois, en % des volumes SWIFT", 3, "< 3 %")], maxv=100, note="Sources : FMI (COFER), analyses Modern Diplomacy 2026. Le dernier indicateur mesure le poids du système chinois, pas du dollar.")}
<p>La dédollarisation est donc <strong>lente et incrémentale</strong> : il s'agit moins de remplacer le dollar que de se prémunir contre le gel d'avoirs — une leçon tirée du gel des réserves russes, dont une large part se trouve en Belgique chez {L("meso/euroclear-avoirs-russes/", "Euroclear")}.</p>
<h2>Les États charnières</h2>
<p>Le phénomène le plus disruptif est la stratégie des puissances moyennes — Indonésie, Émirats, Inde — qui rejoignent les BRICS tout en courtisant l'OCDE. Elles extraient des avantages des deux systèmes et réduisent l'efficacité des sanctions occidentales comme instrument de dissuasion.</p>
{levels("Bipolarisation sino-américaine atténuée par des alignements souples.", "L'UE, première puissance commerciale, dépend du dollar et de l'ouverture ; la Belgique vit de cette ouverture.", "Les diasporas, les entreprises exportatrices et les épargnants subissent les effets des sanctions et des taux de change.")}
""",
 "sources": [("WEF — Global Risks Report 2026, key findings", "https://www.weforum.org/publications/global-risks-report-2026/in-full/global-risks-report-2026-key-findings/"),
             ("BRI — Project mBridge", "https://www.bis.org/project/mbridge"),
             ("Modern Diplomacy — BRICS de-dollarization: settlement data vs rhetoric (2026)", "https://moderndiplomacy.eu/2026/09/01/brics-de-dollarization-settlement-data-vs-rhetoric/"),
             ("CSIS — Geopolitics and Foreign Policy", "https://www.csis.org/geopolitics-foreign-policy"),
             ("Times of India — How China helped arm Iran (2026)", "https://timesofindia.indiatimes.com/world/middle-east/how-china-helped-arm-iran-before-trump-rolled-out-the-red-carpet-for-xi/articleshow/134455086.cms")],
 "related": ["monde/geoeconomie/", "meso/euroclear-avoirs-russes/", "monde/conflits-2026/"],
},
{
 "slug": "monde/conflits-2026/", "section": S,
 "title": "Les 10 conflits majeurs de 2026 : Ukraine, Gaza, Soudan, Sahel…",
 "h1": "Les dix lignes de front de 2026",
 "desc": "Ukraine, Israël-Palestine, Iran et Houthis, Syrie, Corne de l'Afrique, Sahel, Venezuela, Soudan, Myanmar, Afghanistan-Pakistan : panorama des conflits majeurs de 2026.",
 "lede": "L'International Crisis Group recense dix conflits qui définissent l'instabilité de 2026. Plusieurs concernent directement l'Europe et la Belgique, par la sécurité, l'énergie, la migration ou le droit international.",
 "keywords": ["conflits 2026", "guerre en Ukraine", "Gaza", "Soudan", "Sahel", "International Crisis Group"],
 "about": [("Guerre russo-ukrainienne", W + "Invasion_de_l%27Ukraine_par_la_Russie"), ("Ukraine", WD + "Q212", "Country"), ("Soudan", WD + "Q1049", "Country")],
 "level_label": "Macro",
 "body": f"""
<h2>Europe orientale</h2>
<h3>1. Ukraine</h3>
<p>La guerre de position se poursuit à l'avantage démographique de la Russie. L'Ukraine a perdu au printemps 2025 son implantation dans la région russe de Koursk ; l'armée russe progresse vers Pokrovsk, Siversk et Koupiansk. Kiev souffre d'un réseau électrique dévasté, de désertions et de tensions politiques (départ du chef de cabinet Andriy Yermak). Une trêve pascale de 32 heures (11-13 avril 2026) n'a pas tenu. Fin septembre 2026, Moscou se dit prête à négocier mais refuse tout cessez-le-feu préalable.</p>
{callout("<p>La Belgique est concernée à trois titres : ses militaires sur le flanc est de l'OTAN, les avoirs russes gelés chez Euroclear, et le coût énergétique du conflit. Voir " + L("meso/otan-defense/", "Défense et OTAN") + " et " + L("meso/euroclear-avoirs-russes/", "Euroclear") + ".</p>", "lilac", "Lien avec la Belgique")}
<h2>Moyen-Orient</h2>
<h3>2. Israël-Palestine</h3>
<p>Après les opérations de 2024-2025, la bande de Gaza est en ruines. Un « vilain cessez-le-feu » laisse une administration résiduelle du Hamas, tandis qu'Israël contrôle les points névralgiques et entrave la reconstruction. La Belgique est intervenue devant la Cour internationale de Justice (voir {L("meso/moyen-orient-droit-international/", "droit international")}).</p>
<h3>3. Iran, Houthis et États-Unis</h3>
<p>Le conflit a débordé en échanges de frappes directes entre Israël et l'Iran. Les États-Unis ont déployé une armada pour frapper les Houthis au Yémen et protéger le détroit de Bab el-Mandeb, par lequel transite une part décisive du commerce Europe-Asie.</p>
<h3>4. Syrie</h3>
<p>Sous la présidence d'Ahmed al-Sharaa, Damas cherche le retrait des bases étrangères. Washington a rapidement allégé ses sanctions, redessinant l'architecture diplomatique du Levant. La Belgique a nommé un ambassadeur dédié à la Syrie, basé à Beyrouth.</p>
<h2>Afrique</h2>
<h3>5. Corne de l'Afrique</h3>
<p>Le Premier ministre éthiopien Abiy Ahmed revendique un accès souverain à la mer Rouge, ce que l'Érythrée considère comme un <em>casus belli</em>. L'alliance forgée contre le Tigré s'est dissoute après l'accord de Pretoria (2022).</p>
<h3>6. Sahel</h3>
<p>L'Alliance des États du Sahel (Mali, Burkina Faso, Niger), soutenue par l'Africa Corps russe, ne parvient pas à contenir le JNIM lié à Al-Qaïda, qui impose un blocus partiel autour de Bamako. La Belgique a fermé son poste diplomatique à Bamako.</p>
<h3>8. Soudan</h3>
<p>La guerre civile continue ; les Forces de soutien rapide (RSF) mènent des campagnes de nettoyage ethnique au Darfour, épicentre d'une crise humanitaire majeure.</p>
<p>À ces conflits s'ajoute l'est de la <strong>RDC</strong>, où le M23 soutenu par le Rwanda contrôle des territoires miniers — un dossier central pour la diplomatie belge ({L("meso/afrique-grands-lacs/", "Grands Lacs")}).</p>
<h2>Amériques et Asie</h2>
<h3>7. Venezuela</h3>
<p>Fin 2025, les États-Unis ont instauré un blocus naval de fait dans les Caraïbes, saisissant des pétroliers sous sanctions. La ligne dure du secrétaire d'État Marco Rubio accroît le risque d'escalade.</p>
<h3>9. Myanmar</h3>
<p>Contestée par une myriade de groupes armés ethniques, la junte survit grâce au soutien logistique et économique de Pékin.</p>
<h3>10. Afghanistan-Pakistan</h3>
<p>Les affrontements frontaliers s'intensifient ; les puissances du Golfe et la Turquie tentent une médiation.</p>
{table(["Conflit", "Enjeu principal pour l'Europe", "Canal d'impact en Belgique"], [
 ("Ukraine", "Sécurité du continent, énergie", "Défense, Euroclear, prix"),
 ("Israël-Palestine", "Droit international, cohésion sociale", "CIJ, exportations d'armes, mobilisations"),
 ("Iran / mer Rouge", "Routes commerciales", "Port d'Anvers-Bruges, coûts logistiques"),
 ("Sahel", "Terrorisme, migration", "Réseau diplomatique, asile"),
 ("RDC / Grands Lacs", "Minerais critiques", "Diplomatie, diaspora, Umicore"),
], "Lecture européenne et belge des conflits")}
""",
 "sources": [("International Crisis Group — 10 Conflicts to Watch in 2026", "https://www.crisisgroup.org/cmt/global/10-conflicts-watch-2026"),
             ("Wikipédia — 2026 Russo-Ukrainian truce", "https://en.wikipedia.org/wiki/2026_Russo-Ukrainian_truce"),
             ("La Libre — La Russie favorable à des négociations mais refuse le cessez-le-feu (12/09/2026)", "https://www.lalibre.be/international/europe/guerre-ukraine-russie/2026/09/12/guerre-en-ukraine-la-russie-se-dit-favorable-a-des-negociations-mais-refuse-le-cessez-le-feu-26MJ3XOQBZAFRFIA6Y7JHV54BM/"),
             ("CFR — Global Conflict Tracker, RDC", "https://www.cfr.org/global-conflict-tracker/conflict/violence-democratic-republic-congo"),
             ("Breaking Defense — Syria looks to end foreign military presence (2026)", "https://breakingdefense.com/2026/09/syria-looks-to-end-foreign-military-presence-have-sovereignty-over-all-bases-president/")],
 "related": ["monde/rearmement-nucleaire/", "meso/afrique-grands-lacs/", "meso/moyen-orient-droit-international/"],
},
{
 "slug": "monde/rearmement-nucleaire/", "section": S,
 "title": "Réarmement mondial et risque nucléaire : chiffres SIPRI 2026",
 "h1": "Réarmement mondial et retour du risque nucléaire",
 "desc": "Dépenses militaires record (2 887 milliards $ en 2025), objectif OTAN de 5 % du PIB, arsenaux nucléaires 2026, fin de New START et militarisation de l'espace.",
 "lede": "Onzième année consécutive de hausse : le « dividende de la paix » est terminé. L'Europe réarme au rythme le plus rapide depuis 1953, et le contrôle des armements nucléaires s'effondre.",
 "keywords": ["SIPRI 2026", "dépenses militaires", "armes nucléaires", "New START", "OTAN 5 %", "ASAT"],
 "about": [("Stockholm International Peace Research Institute", W + "Institut_international_de_recherche_sur_la_paix_de_Stockholm", "Organization"), ("Arme nucléaire", W + "Arme_nucl%C3%A9aire")],
 "level_label": "Macro",
 "body": f"""
<h2>Des dépenses militaires record</h2>
<p>Selon le SIPRI (avril 2026), les dépenses militaires mondiales ont atteint <strong>2 887 milliards de dollars en 2025</strong>, soit +2,9 % en termes réels et 2,5 % du PIB mondial, le fardeau le plus lourd depuis 2009. En dix ans, la hausse atteint 41 %, soit environ 352 dollars par être humain.</p>
{bars("Dépenses militaires 2025, en milliards de dollars (SIPRI)", [("États-Unis", 954), ("Chine (est.)", 336), ("Russie (est.)", 190), ("Allemagne", 114), ("Inde", 92.1, "92,1"), ("Royaume-Uni", 89), ("Ukraine", 84.1, "84,1"), ("Arabie saoudite", 83.2, "83,2")], note="Source : SIPRI, Trends in World Military Expenditure 2025 (avril 2026). L'Ukraine consacre environ 40 % de son PIB à sa défense.")}
<h3>L'Europe, nouveau moteur</h3>
<p>Les dépenses européennes ont bondi de <strong>14 %</strong> en un an, la plus forte hausse depuis 1953. L'Allemagne (+24 %, 2,3 % du PIB) franchit les 2 % pour la première fois depuis 1990 et devient le quatrième exportateur d'armes mondial. En juin 2025, l'OTAN a fixé un nouvel objectif de <strong>5 % du PIB d'ici 2035</strong> (dont une part pour la résilience et les infrastructures). Les 32 alliés représentent 55 % des dépenses mondiales.</p>
<p>En Asie, la hausse atteint 8,1 % ; le Japon consacre 1,4 % de son PIB à la défense, un niveau inédit depuis 1958.</p>
{callout("<p>Les règles budgétaires européennes accordent jusqu'en 2028 une « clause dérogatoire nationale » permettant d'exclure jusqu'à 1,5 % du PIB de dépenses de défense. À son expiration, la consolidation risque de se faire au détriment du social et du climat. En Belgique, cette tension est aiguë : voir " + L("belgique/finances-publiques/", "finances publiques") + ".</p>", "warn", "Le dilemme budgétaire")}
<h2>Les arsenaux nucléaires en 2026</h2>
<p>Le nombre total de têtes (12 187) baisse légèrement grâce au démantèlement d'ogives anciennes, mais le nombre de têtes <strong>déployées</strong> augmente. En janvier 2026, 9 745 têtes figuraient dans les stocks militaires, dont environ 4 012 déployées et près de 2 200 en alerte opérationnelle élevée.</p>
{table(["Puissance", "Têtes déployées", "Stock militaire", "Dynamique"], [
 ("Russie", "1 796", "4 400", "+78 déployées, plus haut niveau depuis 2017"),
 ("États-Unis", "1 770", "3 700", "Stable, modernisation des vecteurs"),
 ("France", "280", "290", "Doctrine de stricte suffisance"),
 ("Royaume-Uni", "120", "225", "Plafond relevé à 260"),
 ("Chine", "34", "620", "Croissance la plus rapide, nouveaux silos"),
 ("Inde", "12", "190", "Premières patrouilles de SNLE armés"),
 ("Pakistan", "0", "170", "Têtes non montées en temps de paix"),
 ("Israël", "0", "90", "Ambiguïté stratégique"),
 ("Corée du Nord", "0", "≈ 60", "Matière fissile pour ≈ 90"),
], "Forces nucléaires mondiales, janvier 2026 (SIPRI)")}
<p>Le traité <strong>New START</strong> a expiré en février 2026 sans successeur : pour la première fois depuis des décennies, aucun plafond juridique ne limite les arsenaux stratégiques russe et américain.</p>
<p>La Belgique participe au <strong>partage nucléaire de l'OTAN</strong> : la base de Kleine-Brogel accueillerait des bombes américaines B61. Le choix du F-35 est lié à cette mission. Voir {L("meso/otan-defense/", "la défense belge")}.</p>
<h2>L'espace, nouveau champ de bataille</h2>
<p>L'OTAN reconnaît l'espace comme domaine opérationnel. Au-delà des missiles antisatellites (Chine 2007, puis Inde et Russie), les puissances développent des satellites « de proximité », des lasers d'éblouissement et du brouillage. La Russie développerait une arme antisatellite à charge nucléaire ; le satellite chinois SJ-21 a démontré sa capacité à remorquer un autre satellite. Washington prépare le bouclier « Golden Dome ». Les essais passés ont laissé 6 904 débris recensés, menaçant d'un syndrome de Kessler.</p>
<p>En Belgique, le centre <strong>ESEC de l'ESA à Redu</strong> abrite le centre de cybersécurité spatiale européen, qui protège Galileo, Copernicus et IRIS² ({L("meso/niches-strategiques/", "niches stratégiques")}).</p>
""",
 "sources": [("SIPRI — Trends in World Military Expenditure, 2025", "https://www.sipri.org/sites/default/files/2026-04/2604_milex_2025.pdf"),
             ("SIPRI Yearbook 2026 — World nuclear forces", "https://www.sipri.org/yearbook/2026/08"),
             ("SIPRI — Communiqué, dépenses militaires 2026", "https://www.sipri.org/media/press-release/2026/global-military-spending-rise-continues-european-and-asian-expenditures-surge"),
             ("Secure World Foundation — Global Counterspace Capabilities 2026", "https://www.swfound.org/publications-and-reports/2026-global-counterspace-capabilities-report"),
             ("Parlement européen — Implications budgétaires des dépenses de défense (2026)", "https://www.europarl.europa.eu/RegData/etudes/STUD/2026/784024/ECTI_STU(2026)784024_EN.pdf")],
 "related": ["meso/otan-defense/", "monde/infrastructures-critiques/", "belgique/finances-publiques/"],
},
{
 "slug": "monde/geoeconomie/", "section": S,
 "title": "Géoéconomie 2026 : minerais critiques, dette du Sud, croissance, alimentation",
 "h1": "Géoéconomie : minerais critiques, dette et croissance en berne",
 "desc": "Contrôles chinois sur les terres rares, croissance mondiale 2026 (FMI, Banque mondiale), crise de la dette des pays en développement, échec du Cadre commun du G20, indice FAO.",
 "lede": "L'interdépendance économique, hier gage de paix, est devenue une arme. Les minerais, la dette et l'alimentation sont les nouveaux leviers de puissance.",
 "keywords": ["terres rares", "minerais critiques", "dette souveraine", "Cadre commun G20", "FMI 2026", "indice FAO"],
 "about": [("Terres rares", W + "Terre_rare"), ("Dette publique", W + "Dette_publique"), ("Fonds monétaire international", W + "Fonds_mon%C3%A9taire_international", "Organization")],
 "level_label": "Macro",
 "body": f"""
<h2>La guerre des minerais critiques</h2>
<p>La Chine contrôle environ 60 % de la production mondiale de terres rares, mais surtout <strong>90 % du raffinage</strong> et 94 % de la fabrication d'aimants. En avril 2025, en réponse aux droits de douane américains, Pékin a soumis à licence sept terres rares lourdes (dysprosium, terbium, yttrium, lutécium…). Le prix du dysprosium a été multiplié par six en Europe par rapport au marché chinois ; des constructeurs ont dû ralentir leurs cadences.</p>
{table(["Vague", "Éléments visés", "Usages", "Effet mesuré"], [
 ("Avril 2025", "Dy, Tb, Lu, Y, Gd", "Aimants haute température, radars, armes", "Délais 60-120 jours, flambée des prix"),
 ("Octobre 2025", "Ho, Er, Tm, Eu, Yb", "Optique, alliages", "Suspendue jusqu'au 10 novembre 2026"),
 ("Janvier 2026", "Argent, tungstène, antimoine", "Munitions, électronique, solaire", "Tungstène : +175 % de prix"),
 ("Extraterritorialité", "Règle des 0,1 %", "Tout produit fini contenant des terres rares chinoises", "Droit de regard de Pékin sur la production mondiale"),
], "Les contrôles chinois à l'exportation (2025-2026)")}
<p>Selon un économiste de la BCE, plus de 80 % des grandes entreprises européennes se trouvent à moins de trois intermédiaires d'un producteur chinois de terres rares. L'UE répond par le <em>Critical Raw Materials Act</em> et l'initiative RESourceEU. La Belgique y apporte une compétence rare : le recyclage des métaux par {L("meso/niches-strategiques/", "Umicore")}.</p>
<h2>Une croissance mondiale sous plafond</h2>
{bars("Prévisions de croissance 2026 (FMI, mise à jour mi-2026)", [("Inde", 6.5, "6,5 %"), ("Chine", 4.6, "4,6 %"), ("Afrique subsaharienne", 3.7, "3,7 %"), ("Monde", 3.1, "3,1 %"), ("États-Unis", 2.1, "2,1 %"), ("Zone euro", 1.3, "1,3 %"), ("Belgique (BFP)", 1.1, "1,1 %")], unit=" %", note="Sources : FMI, World Economic Outlook 2026 ; Bureau fédéral du Plan pour la Belgique. La Banque mondiale, avec une autre méthode (taux de change de marché), prévoit 2,5 %.")}
<p>La relation favorable où les taux d'intérêt restaient inférieurs à la croissance (<em>r &lt; g</em>) est révolue. La dette publique mondiale reste historiquement haute, alors que s'ajoutent les besoins du réarmement et de l'adaptation climatique.</p>
<h2>La dette étrangle le Sud global</h2>
<p>Entre 2022 et 2024, les pays en développement ont versé <strong>741 milliards de dollars de plus</strong> en service de la dette qu'ils n'ont reçu en nouveaux financements — le plus grand écart depuis cinquante ans. Fin 2025, près d'un quart d'entre eux avaient un revenu par habitant inférieur à celui de 2019. Environ 88 millions de jeunes vivent dans des pays cumulant faibles revenus et risque de défaut.</p>
<h3>L'échec du Cadre commun</h3>
<p>Lancé par le G20 en 2020 pour coordonner créanciers publics, Chine et créanciers privés, le Cadre commun n'a été utilisé que par le Tchad, la Zambie, le Ghana et l'Éthiopie, au terme de négociations interminables. C'est un problème classique d'action collective (Mancur Olson) : chaque créancier espère que les autres assumeront la décote. La Banque mondiale étudie des options contraignantes : lois de New York ou de Londres limitant les créanciers récalcitrants, devoir de bonne foi, clauses d'action collective.</p>
<h2>Alimentation : l'indice FAO remonte</h2>
<p>En août 2026, l'indice FAO des prix alimentaires atteignait <strong>133,3 points</strong> (+1,9 % sur un mois), tiré par le blé, le maïs et le sucre : météo défavorable, perturbations en mer Noire et en mer Rouge, engrais chers. Pour les pays dont la monnaie a chuté face au dollar, le coût réel des importations explose — un accélérateur direct d'instabilité politique.</p>
{levels("Arsenalisation des chaînes de valeur et bifurcation financière.", "L'Europe cherche des approvisionnements « amis » ; la Belgique mise sur la circularité et la diplomatie minière.", "Prix du panier, emplois industriels, coût des voitures électriques et des panneaux solaires.")}
""",
 "sources": [("Parlement européen (EPRS) — China's rare-earth export restrictions", "https://www.europarl.europa.eu/thinktank/en/document/EPRS_ATA(2025)779220"),
             ("CSIS — Rare Earth Export Restrictions One Year Later", "https://www.csis.org/analysis/rare-earth-export-restrictions-one-year-later"),
             ("FMI — World Economic Outlook, avril 2026", "https://www.imf.org/-/media/files/publications/weo/2026/april/english/text.pdf"),
             ("Banque mondiale — Global Economic Prospects", "https://www.worldbank.org/en/publication/global-economic-prospects"),
             ("Center for Global Development — A Modified Common Framework", "https://www.cgdev.org/blog/modified-common-framework-restructuring-sovereign-debt"),
             ("FAO — Food Price Index", "https://www.fao.org/worldfoodsituation/foodpricesindex/en/")],
 "related": ["meso/niches-strategiques/", "monde/ordre-multipolaire/", "belgique/economie/"],
},
{
 "slug": "monde/democratie/", "section": S,
 "title": "Recul démocratique 2026 : rapport V-Dem, désinformation, élections",
 "h1": "Le grand renversement démocratique",
 "desc": "Rapport V-Dem 2026 : 74 % de l'humanité en autocratie, déclassement des États-Unis, désinformation par l'IA, et les élections clés de 2026 (États-Unis, Hongrie, Brésil, Bangladesh).",
 "lede": "Les acquis démocratiques engrangés depuis 1974 sont presque effacés. Le recul touche désormais le cœur du monde occidental.",
 "keywords": ["V-Dem 2026", "autocratisation", "démocratie libérale", "désinformation", "élections 2026"],
 "about": [("Démocratie", W + "D%C3%A9mocratie"), ("Autocratie", W + "Autocratie")],
 "level_label": "Macro",
 "body": f"""
<h2>Le constat de V-Dem</h2>
<p>Le rapport 2026 de l'institut V-Dem (université de Göteborg), intitulé <em>Unraveling the Democratic Era?</em>, parle d'un « grand renversement » : le niveau de démocratie vécu par le citoyen moyen est revenu à celui de 1978.</p>
{kpis([("74 %", "de la population mondiale vit en autocratie (≈ 6 milliards)"), ("7 %", "vit en démocratie libérale (17 % au début des années 2000)"), ("44", "pays en voie d'autocratisation, dont 5 membres de l'UE"), ("33", "pays où la torture politique progresse")])}
<p>La population en « autocratie fermée » (28 %) dépasse désormais celle vivant en démocratie (26 %). Les outils de l'autocratisation sont récurrents : censure des médias (73 % des gouvernements concernés), répression de la société civile (68 %), affaiblissement des juges et des parlements.</p>
<h2>Le déclassement des États-Unis</h2>
<p>Fait marquant : selon V-Dem, les États-Unis perdent pour la première fois en cinquante ans leur statut de démocratie libérale. L'institut décrit l'« agrandissement de l'exécutif » le plus rapide de l'histoire américaine moderne : les contraintes législatives sur la présidence ont perdu un tiers de leur valeur, les indicateurs d'égalité devant la loi seraient revenus aux niveaux de 1965. Ces évaluations relèvent de la méthodologie de V-Dem (codage par experts) et sont contestées par une partie de la classe politique américaine.</p>
<p>En Europe, l'Italie, la Slovaquie, la Slovénie, la Croatie et le Royaume-Uni figurent parmi les pays classés « en autocratisation ».</p>
<h2>Désinformation et fracture cognitive</h2>
<p>Les modèles de langage ont industrialisé la production de faux contenus à coût marginal quasi nul. Le WEF classe la désinformation au 2<sup>e</sup> rang des risques à court terme. Elle forme une boucle avec la polarisation : moins de confiance dans les faits, moins de consensus possible sur le climat, les pandémies ou la dette. Les démocraties se retrouvent paralysées de l'intérieur, tandis que les autocraties contrôlent leur récit.</p>
<h2>Les élections clés de 2026</h2>
<p>Plus de 40 pays et 1,6 milliard d'habitants votent en 2026.</p>
{table(["Pays", "Date", "Enjeu"], [
 ("Bangladesh", "Février", "Premier scrutin compétitif depuis la chute de Sheikh Hasina ; gouvernement intérimaire de Muhammad Yunus"),
 ("Hongrie", "Avril", "Viktor Orbán défié par Péter Magyar (Tisza)"),
 ("Brésil", "Octobre", "Survie de la gauche au pouvoir dans une société très polarisée"),
 ("États-Unis", "Novembre", "Élections de mi-mandat, juge de paix de l'agenda de Donald Trump"),
], "Scrutins à fort impact géopolitique")}
<h2>Et en Belgique ?</h2>
<p>La Belgique reste une démocratie consolidée (16<sup>e</sup> à l'indice de perception de la corruption), mais elle n'échappe ni à la polarisation (percée du Vlaams Belang), ni aux menaces hybrides. Les enquêtes montrent pourtant que Flamands et francophones partagent l'essentiel de leurs valeurs : le clivage est d'abord politique et médiatique ({L("micro/identites/", "identités")}).</p>
{levels("Basculement autoritaire de grandes puissances, affaiblissement des normes.", "L'UE, communauté de droit, affronte des gouvernements illibéraux en son sein.", "Confiance dans les institutions, exposition aux réseaux sociaux, engagement associatif.")}
""",
 "sources": [("V-Dem — Democracy Report 2026", "https://www.v-dem.net/documents/75/V-Dem_Institute_Democracy_Report_2026_lowres.pdf"),
             ("WEF — Global Risks Report 2026", "https://reports.weforum.org/docs/WEF_Global_Risks_Report_2026.pdf"),
             ("CFR — Ten Elections to Watch in 2026", "https://www.cfr.org/articles/ten-elections-watch-2026"),
             ("Chatham House — US midterm elections 2026", "https://www.chathamhouse.org/events/all/standard-event/us-midterm-elections-2026-what-happens-next")],
 "related": ["micro/identites/", "belgique/elections-2024/", "monde/technologies/"],
},
{
 "slug": "monde/climat-limites-planetaires/", "section": S,
 "title": "Climat et limites planétaires 2026 : 7 limites sur 9 franchies",
 "h1": "Climat : sept limites planétaires sur neuf franchies",
 "desc": "Planetary Health Check 2025, acidification des océans, budget carbone pour 1,5 °C, AMOC, pergélisol, géo-ingénierie solaire et migrations climatiques.",
 "lede": "2024 a dépassé 1,5 °C de réchauffement ; 2025 est restée à 1,43 °C malgré La Niña. L'acidification des océans vient de rejoindre la zone de danger.",
 "keywords": ["limites planétaires", "acidification des océans", "budget carbone", "1,5 °C", "géo-ingénierie", "AMOC"],
 "about": [("Changement climatique", WD + "Q125928"), ("Limites planétaires", W + "Limites_plan%C3%A9taires")],
 "level_label": "Macro",
 "body": f"""
<h2>Le bilan de santé planétaire</h2>
<p>Le <em>Planetary Health Check 2025</em> (Institut de Potsdam et Stockholm Resilience Centre) constate que <strong>sept des neuf limites planétaires</strong> sont franchies. La nouveauté : l'acidification des océans. Le pH de surface a baissé d'environ 0,1 unité depuis l'ère préindustrielle, soit 30 à 40 % d'acidité en plus ; la saturation en aragonite (2,84 Ω) est passée sous le seuil de 2,86 Ω, menaçant coraux et ptéropodes à la base de la chaîne alimentaire.</p>
{table(["Limite", "État", "Indicateur"], [
 ("Changement climatique", "Franchie (risque élevé)", "CO₂ ≈ 423-426 ppm (limite sûre 350)"),
 ("Intégrité de la biosphère", "Franchie (risque élevé)", "Extinctions > 100 E/MSY (limite < 10)"),
 ("Entités nouvelles", "Franchie", "> 350 000 substances synthétiques"),
 ("Flux biogéochimiques", "Franchie (risque élevé)", "Azote : 165 Tg/an (limite 62)"),
 ("Usage des sols", "Franchie", "59 % du couvert forestier originel (limite 75 %)"),
 ("Eau douce", "Franchie", "Eau bleue 22,6 %, eau verte 22 % (limite ≈ 12,5 %)"),
 ("Acidification des océans", "Franchie (nouveau)", "Aragonite 2,84 Ω (limite 2,86)"),
 ("Couche d'ozone", "Zone sûre", "Restauration grâce au protocole de Montréal"),
 ("Aérosols", "Zone sûre", "0,063 (limite 0,1)"),
], "Les neuf limites planétaires (évaluation 2025)")}
<h2>Le budget carbone s'épuise</h2>
<p>Début 2025, il restait environ <strong>130 milliards de tonnes de CO₂</strong> pour avoir une chance sur deux de rester sous 1,5 °C. Au rythme actuel (40 à 42 Gt par an), il sera épuisé avant la fin de 2029. Pour une probabilité de 83 %, le budget tombe à 30 Gt — consommé dès 2026. La concentration atteint environ 425,7 ppm, 52 % au-dessus du niveau préindustriel.</p>
<h2>Points de bascule</h2>
<ul>
<li><strong>Pergélisol</strong> : son dégel pourrait libérer 200 à 300 Gt d'équivalent CO₂ supplémentaires ce siècle.</li>
<li><strong>AMOC</strong> : la circulation méridienne de retournement de l'Atlantique montre des signes de ralentissement ; un basculement bouleverserait le climat de l'hémisphère nord, Belgique comprise.</li>
</ul>
<h2>La tentation de la géo-ingénierie</h2>
<p>Face à l'échec de l'atténuation, la modification du rayonnement solaire (injection d'aérosols stratosphériques) gagne en crédibilité ; une entreprise privée, Stardust Solutions, a levé 75 millions de dollars. Le PNUE rappelle qu'elle ne traite ni la cause ni l'acidification, et qu'elle pourrait perturber les moussons. Sans traité, un déploiement unilatéral pourrait déclencher des conflits, et la simple promesse d'un « thermostat » retarde la réduction des émissions (aléa moral).</p>
<h2>Déplacements climatiques</h2>
<p>Le rapport <em>Groundswell</em> de la Banque mondiale estime que jusqu'à 216 millions de personnes pourraient migrer à l'intérieur de leur pays d'ici 2050. Les régions les plus touchées — Afrique subsaharienne, Asie du Sud, Amérique latine — sont aussi celles que la dette empêche d'investir dans l'adaptation.</p>
<h2>La Belgique face au climat</h2>
<p>La Commission européenne juge le plan énergie-climat belge insuffisant, et le marché carbone ETS2 inquiète pour le pouvoir d'achat. Voir {L("belgique/energie-climat/", "énergie et climat en Belgique")}.</p>
{levels("Dépassement des limites, budget carbone épuisé, points de bascule.", "Politiques européennes (Pacte vert, ETS2) et plans nationaux ; en Belgique, compétence éclatée entre quatre gouvernements.", "Inondations (Vesdre 2021), canicules, coût du chauffage, qualité de l'air.")}
""",
 "sources": [("Stockholm Resilience Centre — Seven of nine planetary boundaries now breached", "https://www.stockholmresilience.org/news--events/general-news/2025-09-24-seven-of-nine-planetary-boundaries-now-breached.html"),
             ("OMM — Earth's climate swings increasingly out of balance", "https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance"),
             ("Université de Leeds — Three years left of carbon budget for 1.5°C", "https://climate.leeds.ac.uk/news/scientists-find-three-years-left-of-remaining-carbon-budget-for-1-5c/"),
             ("PNUE — Solar Radiation Modification", "https://www.unep.org/resources/emerging-issues/solar-radiation-modification-no-substitute-real-climate-action"),
             ("Banque mondiale — Groundswell", "https://www.worldbank.org/en/news/press-release/2021/09/13/climate-change-could-force-216-million-people-to-migrate-within-their-own-countries-by-2050"),
             ("Carbon Brief — AMOC explainer", "https://interactive.carbonbrief.org/amoc-explainer/index.html")],
 "related": ["belgique/energie-climat/", "monde/polycrise/", "monde/geoeconomie/"],
},
{
 "slug": "monde/technologies/", "section": S,
 "title": "IA, biosécurité et menace quantique : les risques technologiques de 2026",
 "h1": "Technologies de rupture : IA, biosécurité et « Q-Day »",
 "desc": "International AI Safety Report 2026, cadres de sécurité des laboratoires d'IA, convergence IA-biologie, cryptographie post-quantique (FIPS 203-205) et stratégie « Harvest now, decrypt later ».",
 "lede": "La convergence de l'IA, de la biologie de synthèse et du calcul quantique abaisse les barrières d'accès à la destruction massive. La régulation court derrière.",
 "keywords": ["intelligence artificielle", "AI Safety Report 2026", "biosécurité", "cryptographie post-quantique", "Q-Day", "AI Act"],
 "about": [("Intelligence artificielle", WD + "Q11660"), ("Cryptographie post-quantique", W + "Cryptographie_post-quantique")],
 "level_label": "Macro",
 "body": f"""
<h2>L'IA de frontière avance plus vite que ses garde-fous</h2>
<p>L'<em>International AI Safety Report 2026</em>, rédigé par une centaine d'experts sous la direction de Yoshua Bengio, constate que les capacités des modèles de pointe progressent plus vite que la mise en place et l'efficacité des garde-fous. L'AI Act européen et les premières lois californiennes peinent à suivre.</p>
<p>Les laboratoires (Anthropic, Google DeepMind, OpenAI…) publient des <strong>cadres de sécurité</strong> fondés sur des seuils de capacités qui déclenchent des niveaux de protection renforcés. Des chercheurs relèvent toutefois leur hétérogénéité, qui complique les audits indépendants. Les inquiétudes portent sur l'autonomie d'agents capables de tromper leurs superviseurs, de mener des cyberattaques ou d'accélérer la recherche en IA, ainsi que sur le vol des poids des modèles.</p>
{callout("<p>Ce site est rédigé par Claude, un modèle d'Anthropic, l'un des laboratoires cités. Nous le signalons par transparence ; les constats ci-dessus proviennent de rapports indépendants.</p>", "lilac", "Transparence")}
<h2>La convergence IA-biologie</h2>
<p>Les grands modèles de langage abaissent surtout la barrière de l'information ; les <strong>outils de conception biologique</strong> dopés à l'IA relèvent le plafond de ce que des acteurs sophistiqués pourraient concevoir. En 2022, l'expérience Urbina a montré qu'un modèle détourné générait 40 000 molécules toxiques candidates en six heures. Les listes d'agents pathogènes réglementés deviennent insuffisantes face à des séquences synthétiques inédites ; les laboratoires automatisés pilotables à distance érodent la dernière barrière, celle du savoir-faire pratique.</p>
<p>La réponse multilatérale est lente : les négociations sur l'annexe « accès aux pathogènes et partage des avantages » (PABS) de l'Accord de l'OMS sur les pandémies achoppent sur le clivage Nord-Sud.</p>
<h2>Le « Q-Day » et la cryptographie post-quantique</h2>
<p>Un ordinateur quantique suffisamment puissant pourrait casser RSA et les courbes elliptiques, qui protègent la banque, les télécoms et les communications militaires. Plusieurs analystes placent ce risque vers 2030. Mais la menace est déjà active : des adversaires collectent aujourd'hui des données chiffrées pour les déchiffrer demain (<em>Harvest now, decrypt later</em>).</p>
{kpis([("2024", "Normes NIST FIPS 203, 204 et 205 (ML-KEM, ML-DSA, SLH-DSA)"), ("≈ 2030", "Horizon estimé d'un ordinateur quantique cryptographiquement pertinent"), ("5 %", "des organisations avaient déployé du chiffrement post-quantique début 2026"), ("> 80 %", "déclarent leurs bibliothèques cryptographiques non prêtes")])}
<h2>Implications pour la Belgique</h2>
<p>La Belgique héberge des infrastructures sensibles — {L("meso/euroclear-avoirs-russes/", "Euroclear")}, SWIFT (siège à La Hulpe), l'OTAN, le centre de cybersécurité spatiale de Redu — et l'{L("meso/niches-strategiques/", "imec")}, au cœur de la course aux puces. Le Centre pour la cybersécurité (CCB) pilote la mise en œuvre de la directive NIS2 ({L("micro/securite-cyber/", "sécurité et cyber")}).</p>
""",
 "sources": [("International AI Safety Report 2026 (arXiv)", "https://arxiv.org/abs/2602.21012"),
             ("Anthropic — Responsible Scaling Policy", "https://www.anthropic.com/responsible-scaling-policy"),
             ("Google DeepMind — Frontier Safety Framework", "https://deepmind.google/blog/introducing-the-frontier-safety-framework/"),
             ("OMS — Négociations PABS (18/09/2026)", "https://www.who.int/news/item/18-09-2026-member-states-advance-negotiations-on-pathogen-access-and-benefit-sharing-ahead-of-un-general-assembly-meeting-on-pandemics"),
             ("Cloud Security Alliance — Q-Day clock", "https://labs.cloudsecurityalliance.org/research/strategic-post-quantum-cryptography-migration-enterprise-roa/"),
             ("PwC — Preparing for Q-Day", "https://www.pwc.com/gx/en/issues/cybersecurity/preparing-for-q-day.html")],
 "related": ["monde/infrastructures-critiques/", "meso/niches-strategiques/", "micro/securite-cyber/"],
},
{
 "slug": "monde/infrastructures-critiques/", "section": S,
 "title": "Câbles sous-marins et infrastructures critiques : la zone grise",
 "h1": "Câbles sous-marins et infrastructures critiques : le front de la zone grise",
 "desc": "99 % des données intercontinentales passent par des câbles sous-marins. Pannes, sabotages, flottes fantômes, Baltic Sentry : la vulnérabilité des infrastructures en 2026.",
 "lede": "L'économie numérique, l'IA et la finance reposent sur quelques centaines de câbles posés au fond des mers. Leur protection est devenue une question de sécurité nationale.",
 "keywords": ["câbles sous-marins", "infrastructures critiques", "zone grise", "Baltic Sentry", "guerre hybride"],
 "about": [("Câble sous-marin", W + "C%C3%A2ble_sous-marin"), ("Guerre hybride", W + "Guerre_hybride")],
 "level_label": "Macro",
 "body": f"""
<h2>Une dépendance invisible</h2>
<p>Les câbles sous-marins transportent environ <strong>99 % des données intercontinentales</strong>. Les transferts massifs entre centres de données qui alimentent l'IA les rendent encore plus critiques. Or les pannes se multiplient, accidentelles ou non.</p>
{kpis([("99 %", "des données intercontinentales passent par des câbles"), ("13", "pays africains coupés en mars 2024 (4 câbles sectionnés)"), ("590 M$", "de pertes estimées pour le seul Nigeria"), ("3,5 Md$", "de coût pour le Golfe lors des coupures en mer Rouge (2025)")])}
<h2>Accidents et sabotages</h2>
<p>Selon une commission du Parlement britannique (septembre 2025), 70 à 80 % des incidents restent accidentels (ancres, chalutiers). Mais les 20 à 30 % restants incluent des actions de « zone grise », menées par des flottes fantômes de navires sous faux pavillon. Les points d'atterrage et la concentration des liaisons vers quelques centres de données constituent des points de défaillance uniques.</p>
<h3>Des signaux qualitatifs inquiétants</h3>
<p>L'analyste maritime Windward a suivi 34 081 épisodes de navires évoluant à très faible vitesse près des tracés de câbles au deuxième trimestre 2026. Si le volume global baisse, les événements impliquant des navires chinois à risque de pêche illégale ont bondi de 80,6 %, et le temps de stationnement moyen des navires de service iraniens a doublé (23,3 heures) : des missions de repérage plus ciblées.</p>
<h2>Les réponses</h2>
<ul>
<li><strong>OTAN</strong> : pérennisation de l'opération <em>Baltic Sentry</em> lancée en janvier 2025.</li>
<li><strong>UE</strong> : plan d'action sur la sécurité et la résilience des câbles sous-marins.</li>
<li><strong>Royaume-Uni</strong> : <em>Subsea Cables Act</em>.</li>
<li>Limite : en haute mer, la compétence juridique rend l'arrestation de navires suspects très difficile.</li>
</ul>
<h2>La mer du Nord belge</h2>
<p>La Belgique est directement concernée : parcs éoliens offshore, gazoducs, câbles vers le Royaume-Uni, future {L("belgique/energie-climat/", "île énergétique Princesse Élisabeth")}. Sa marine, intégrée à celle des Pays-Bas (BeNeSam), est spécialisée dans la guerre des mines, compétence utile pour la surveillance des fonds marins ({L("meso/otan-defense/", "défense")}).</p>
{levels("Câbles, satellites et réseaux électriques deviennent des cibles de la guerre hybride.", "OTAN et UE coordonnent surveillance et résilience ; la Belgique protège la mer du Nord.", "Une coupure se traduit par des paiements bloqués, des services en ligne indisponibles, des hausses de prix.")}
""",
 "sources": [("Parlement britannique — Subsea telecommunications cables: resilience and crisis", "https://publications.parliament.uk/pa/jt5901/jtselect/jtnatsec/723/report.html"),
             ("Windward — Q2 2026 Undersea Cables Risk Report", "https://windward.ai/knowledge-base/q2-2026-undersea-cables-risk-report/"),
             ("Tech Policy Press — The UN's AI Agenda Must Prioritize Undersea Cables", "https://www.techpolicy.press/the-uns-ai-agenda-must-prioritize-undersea-cables/"),
             ("Commission européenne — Sécurité des câbles sous-marins", "https://ec.europa.eu/newsroom/cipr/items/884566/")],
 "related": ["monde/technologies/", "belgique/energie-climat/", "meso/otan-defense/"],
},
]
