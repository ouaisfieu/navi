from h import L, kpis, bars, table, callout, levels

W = "https://fr.wikipedia.org/wiki/"
WD = "https://www.wikidata.org/wiki/"
S = "meso"
BE = ("Belgique", WD + "Q31", "Country")

PAGES = [
{
 "slug": "meso/", "section": S, "kind": "hub",
 "title": "Méso : l'Europe et la Belgique dans l'ordre mondial",
 "h1": "Méso : l'Europe et la Belgique dans l'ordre mondial",
 "desc": "L'échelle intermédiaire : Union européenne, OTAN, diplomatie belge, Euroclear, niches technologiques, Afrique des Grands Lacs, droit international et soft power.",
 "lede": "Entre les forces mondiales et le quotidien, il y a les institutions qui traduisent, amortissent ou amplifient : l'Union européenne, l'OTAN, les États et leurs diplomaties. La Belgique en est un laboratoire.",
 "keywords": ["Belgique dans le monde", "politique étrangère belge", "Union européenne", "OTAN"],
 "about": [BE, ("Union européenne", WD + "Q458", "Organization"), ("OTAN", WD + "Q7184", "Organization")],
 "body": f"""
<p>La Belgique pèse aujourd'hui 0,43 % du PIB mondial (contre environ 1 % il y a un demi-siècle) et moins de 0,32 % des dépenses militaires. Elle n'est qu'une voix sur 193 à l'ONU, 32 à l'OTAN, 27 dans l'UE. Pourtant, elle abrite sur son sol les sièges de l'UE et de l'OTAN, le SHAPE, Euroclear, SWIFT et l'imec : une « salle des machines » de l'autonomie stratégique européenne.</p>
{kpis([("0,43 %", "part de la Belgique dans le PIB mondial (FMI, 2024)"), ("> 60", "organisations internationales à Bruxelles"), ("≈ 210 Md€", "d'avoirs de la Banque centrale russe gelés chez Euroclear"), ("20ᵉ", "au Global Soft Power Index 2026")])}
<h2>Le fil rouge : du multilatéralisme confortable au réalisme</h2>
<p>Pendant trois décennies, la Belgique a délégué une grande partie de sa politique extérieure à l'UE et misé sur le soft power. Depuis 2022, et plus nettement avec le gouvernement De Wever (2025), elle opère un « réétalonnage » : réarmement, contrôle migratoire, diplomatie économique, défense ferme du droit international.</p>
""",
},
{
 "slug": "meso/union-europeenne/", "section": S,
 "title": "La Belgique et l'Union européenne : capitale, règles budgétaires, influence",
 "h1": "La Belgique et l'Union européenne",
 "desc": "Bruxelles capitale de l'UE, procédure pour déficit excessif, clause dérogatoire défense, cadre financier 2028-2034, Benelux : la relation entre la Belgique et l'Europe en 2026.",
 "lede": "Pays fondateur, hôte des institutions, la Belgique a fait de l'Europe un projet fédérateur au-dessus de ses divisions internes. En 2026, l'Europe est aussi son créancier de rigueur.",
 "keywords": ["Belgique Union européenne", "procédure déficit excessif Belgique", "Bruxelles capitale européenne", "Benelux", "cadre financier pluriannuel"],
 "about": [BE, ("Union européenne", WD + "Q458", "Organization"), ("Benelux", W + "Benelux", "Organization")],
 "level_label": "Méso",
 "body": f"""
<h2>Bruxelles, capitale de fait de l'Europe</h2>
<p>Commission, Conseil, une partie du Parlement européen, service diplomatique de l'UE, OTAN, SHAPE à Mons : la Belgique mène une <strong>politique d'État hôte</strong> qui fait de Bruxelles le foyer de plus de soixante organisations internationales et d'environ 40 000 fonctionnaires internationaux. Cette fonction apporte prestige, emplois et influence ; elle a aussi un coût pour la Région bruxelloise (sécurité, infrastructures), sans recettes fiscales proportionnelles ({L("belgique/bruxelles/", "le paradoxe bruxellois")}).</p>
<h2>L'Europe comme projet fédérateur</h2>
<p>Dans les années 1990, la Belgique a délégué une grande partie de ses responsabilités géopolitiques à l'UE ; la construction européenne servait de projet supranational commun à un pays traversé de tensions communautaires. L'Institut Egmont juge que cette délégation a atrophié l'appareil diplomatique national ({L("meso/diplomatie-belge/", "diplomatie belge")}).</p>
<h2>La discipline budgétaire européenne</h2>
<p>Le 26 juillet 2024, le Conseil de l'UE a ouvert une <strong>procédure pour déficit excessif</strong> contre la Belgique. Son plan budgétaire et structurel à moyen terme limite la croissance des dépenses primaires nettes à 2,5 % en 2026 et 2027. Le déficit atteignait 5,4 % du PIB en 2025, la dette 107,4 %.</p>
{callout("<p>La « clause dérogatoire nationale » (2025-2028) permet d'exclure jusqu'à 1,5 % du PIB de dépenses de défense des objectifs de réduction du déficit. La Belgique l'utilise pour son réarmement, mais son expiration rendra les arbitrages plus durs.</p>", "warn", "Défense et règles budgétaires")}
<p>Détails : {L("belgique/finances-publiques/", "finances publiques belges")}.</p>
<h2>Le prochain budget européen</h2>
<p>Le cadre financier pluriannuel 2028-2034 en préparation renforce nettement les programmes industriels de défense (EDIP, mobilité militaire). L'institut Bruegel plaide pour que plus de flexibilité s'accompagne de plus de contrôle démocratique. Pour la Belgique, dont l'industrie de défense se consolide (John Cockerill, FN Herstal, Thales Belgium), l'enjeu est aussi économique.</p>
<h2>Le Benelux, laboratoire du « minilatéralisme »</h2>
<p>Belgique, Pays-Bas et Luxembourg coordonnent leurs positions en amont des sommets européens, ce qui amplifie leur poids. La coopération va loin : marines intégrées (BeNeSam), police du ciel commune, traité de police Benelux permettant le partage de bases de données et des enquêtes transfrontalières, utile contre le narcotrafic ({L("micro/narcotrafic-anvers/", "Anvers")}).</p>
<h2>La présidence belge de 2024</h2>
<p>Au premier semestre 2024, la Belgique a présidé le Conseil de l'UE, avec l'appui d'un programme de l'Institut Egmont — dernière grande démonstration de son savoir-faire de médiateur avant l'alternance politique.</p>
{levels("L'UE cherche une autonomie stratégique entre États-Unis et Chine.", "La Belgique, hôte et contributrice, est soumise à la surveillance budgétaire européenne.", "Les Bruxellois vivent l'Europe au quotidien : emplois, loyers, sécurité, multilinguisme.")}
""",
 "sources": [("Conseil de l'UE — Procédure concernant les déficits excessifs", "https://www.consilium.europa.eu/fr/policies/excessive-deficit-procedure/"),
             ("Trésor (FR) — Situation économique et financière de la Belgique", "https://www.tresor.economie.gouv.fr/Pays/BE/situation-economique-et-financiere-de-la-belgique"),
             ("Bruegel — Defence in the 2028-2034 EU budget", "https://www.bruegel.org/analysis/more-flexibility-needs-greater-accountability-defence-2028-2034-eu-budget"),
             ("SPF Affaires étrangères — Politique d'État hôte", "http://diplomatie.belgium.be/en/policy/interministerial-committee-host-nation-policy/short-history"),
             ("Benelux — Coopération sécuritaire transfrontalière", "https://www.benelux.int/en/post/belgian-and-dutch-limburg-strengthen-cross-border-security/")],
 "related": ["belgique/finances-publiques/", "meso/diplomatie-belge/", "belgique/bruxelles/"],
},
{
 "slug": "meso/otan-defense/", "section": S,
 "title": "Défense belge et OTAN : réarmement, CaMo, F-35, BeNeSam",
 "h1": "La défense belge : du passager clandestin au laboratoire européen",
 "desc": "Budget de défense belge, Vision stratégique 2026-2034 (34 Md€), partenariat CaMo avec la France, BeNeSam avec les Pays-Bas, F-35 et partage nucléaire, flanc est, Groenland.",
 "lede": "Tombée à 0,88 % du PIB en 2017, la défense belge vise désormais 2 % et au-delà. Faute de taille critique, la Belgique mise sur l'intégration avec ses voisins.",
 "keywords": ["défense belge", "OTAN Belgique", "CaMo", "BeNeSam", "F-35 Belgique", "Kleine-Brogel", "Theo Francken"],
 "about": [BE, ("OTAN", WD + "Q7184", "Organization"), ("Composante Terre", W + "Composante_Terre"), ("Partage nucléaire", W + "Partage_nucl%C3%A9aire")],
 "level_label": "Méso",
 "body": f"""
<h2>Trente ans de désarmement</h2>
<p>Après la Guerre froide, la Belgique a suspendu la conscription (1994) et laissé fondre son budget militaire jusqu'à <strong>0,88 % du PIB en 2017</strong>. Elle a acquis la réputation de « passager clandestin » de l'OTAN — illustrée en 2016, quand l'armée a dû emprunter des équipements balistiques aux Américains pour ses patrouilles après les attentats de Bruxelles.</p>
<h2>Le rattrapage</h2>
<p>Le plan <strong>STAR</strong> (2022) a amorcé la remontée. Le gouvernement De Wever s'est engagé à atteindre 2 % du PIB ; la <strong>loi de programmation militaire 2026-2034</strong>, adoptée par la Chambre en novembre 2025, et la <strong>Vision stratégique</strong> du ministre Theo Francken prévoient 34 milliards d'euros d'investissements.</p>
{kpis([("0,88 %", "du PIB en 2017, point bas historique"), ("2 %", "objectif OTAN minimal visé dès 2025-2026"), ("34 Md€", "Vision stratégique 2026-2034"), ("3,7 Md€", "sur dix ans pour l'innovation de défense")])}
<p>Au programme : reconstitution des stocks de munitions, défense antiaérienne, escadrons de F-35 supplémentaires, troisième frégate, drones. En incluant les dépenses de sécurité au sens large, certaines estimations situent l'effort réel autour de 3,4 à 3,5 % du PIB en 2026 — une comptabilité discutée. Le Bureau du Plan souligne qu'atteindre ces niveaux impliquera des arbitrages avec les dépenses sociales.</p>
<h2>CaMo : l'armée de terre franco-belge</h2>
<p>Entré en vigueur en 2019, le partenariat <strong>Capacité motorisée</strong> avec la France va au-delà de l'achat de matériel : doctrine, formation, logistique et systèmes d'information (bulle SCORPION) sont partagés, afin qu'une unité belge s'insère « plug and play » dans une brigade française. La Cour des comptes estime le coût total à 14,4 milliards d'euros sur 25 ans.</p>
{table(["Phase", "Matériels", "Industrie belge"], [
 ("CaMo 1", "382 Griffon, 60 Jaguar (livraisons 2025-2026)", "Assemblage final en Belgique"),
 ("CaMo 2", "29 CAESAR MkII, mortiers embarqués, jusqu'à 123 Serval et 92 Griffon supplémentaires", "Tourelleaux téléopérés FN Herstal"),
 ("Soutien LS²", "Maintenance du parc motorisé", "John Cockerill, FN Herstal, Thales Belgium"),
], "Le programme CaMo")}
<h2>BeNeSam : une marine binationale</h2>
<p>Depuis 1996, les états-majors belge et néerlandais sont fusionnés sous l'« Amiral Benelux » à Den Helder. La Belgique pilote la guerre des mines (école OTAN Eguermin à Ostende), les Pays-Bas les frégates. Les deux pays achètent ensemble des frégates anti-sous-marines et des chasseurs de mines, et alternent la police du ciel au-dessus du Benelux.</p>
<h2>Le F-35 et Kleine-Brogel</h2>
<p>La Belgique participe au <strong>partage nucléaire</strong> de l'OTAN : la base de Kleine-Brogel abriterait des bombes américaines B61 (estimées entre 10 et 20). Le choix du F-35 (environ 4 milliards d'euros pour 34 appareils) s'explique en grande partie par sa certification pour la nouvelle B61-12. Des analystes de l'IFRI et du GRIP parlent d'une « illusion » de protection et d'une dépendance technologique accrue ; des mouvements pacifistes demandent le retrait de ces armes. La Belgique participe par ailleurs comme observatrice aux réunions du traité d'interdiction des armes nucléaires.</p>
<h2>Sur le terrain</h2>
<ul>
<li><strong>Flanc est</strong> : des centaines de militaires en Roumanie (groupement tactique sous commandement français) et en Lituanie.</li>
<li><strong>Police du ciel</strong> : rotations de F-16 au-dessus des pays baltes et de l'Islande.</li>
<li><strong>Arctique</strong> : déploiement au Groenland dans le cadre de la mission OTAN « Arctic Sentry », sur fond de tensions avec Washington au sujet de ce territoire danois.</li>
</ul>
<h2>Cyber et espace</h2>
<p>Un <em>Cyber Command</em> a été créé au sein de la Défense. Le Conseil national de sécurité se réunit sur les menaces hybrides. À Redu, l'ESEC de l'Agence spatiale européenne héberge le centre de cybersécurité spatiale qui protège Galileo, Copernicus et IRIS².</p>
{levels("Réarmement mondial, fin de New START, pression américaine sur les alliés.", "Intégration binationale (France, Pays-Bas) et européenne ; industrie de défense qui se consolide.", "Recrutement, emplois industriels en Wallonie, débat sur le coût social du réarmement.")}
""",
 "sources": [("Egmont — Re-Empowering Belgian Foreign Policy (Policy Brief 354)", "https://egmontinstitute.be/re-empowering-belgian-foreign-policy/"),
             ("Cabinet Francken — Loi de programmation militaire 2026-2034", "https://francken.belgium.be/fr/actualites/la-chambre-approuve-la-loi-de-programmation-militaire-2026-2034"),
             ("Cour des comptes — Rééquipement de la capacité motorisée", "https://www.ccrek.be/sites/default/files/Docs/2025_16_ReequipementDefense.pdf"),
             ("Ministère des Armées (FR) — 5 choses à savoir sur CaMo", "http://www.defense.gouv.fr/terre/5-choses-savoir/5-choses-savoir-partenariat-camo"),
             ("IFRI — Les F-35 belges et l'illusion de protection nucléaire", "https://www.ifri.org/fr/presse-contenus-repris-sur-le-site/les-f-35-belges-au-coeur-dune-illusion-de-protection-nucleaire"),
             ("GRIP — Faut-il acheter le F-35 pour le partage nucléaire ?", "https://www.grip.org/faut-il-acheter-le-f-35-pour-participer-au-partage-nucleaire-dans-lotan-2/"),
             ("Défense belge — Missions sur le flanc est", "https://www.mil.be/en/our-missions/missions-on-the-eastern-flank-of-europe/")],
 "related": ["monde/rearmement-nucleaire/", "belgique/finances-publiques/", "meso/union-europeenne/"],
},
{
 "slug": "meso/diplomatie-belge/", "section": S,
 "title": "Diplomatie belge : fédéralisme, Team Belgium, réseau d'ambassades",
 "h1": "La diplomatie belge à l'épreuve du fédéralisme",
 "desc": "Principe in foro interno, in foro externo, crise du CETA, Team Belgium, fermetures et ouvertures de postes, Institut Egmont, Francophonie et Benelux.",
 "lede": "La Belgique est l'un des rares États où les régions et communautés concluent elles-mêmes des traités. Une richesse démocratique, et un risque de paralysie.",
 "keywords": ["diplomatie belge", "in foro interno in foro externo", "CETA Wallonie", "Team Belgium", "Maxime Prévot", "Institut Egmont"],
 "about": [BE, ("Service public fédéral Affaires étrangères", W + "Service_public_f%C3%A9d%C3%A9ral_Affaires_%C3%A9trang%C3%A8res", "GovernmentOrganization"), ("Maxime Prévot", W + "Maxime_Pr%C3%A9vot", "Person")],
 "level_label": "Méso",
 "body": f"""
<h2>In foro interno, in foro externo</h2>
<p>En vertu de l'article 167 de la Constitution, les Régions et Communautés sont compétentes pour conclure des traités dans les matières qui relèvent de leurs compétences internes : commerce extérieur, environnement, agriculture, enseignement, culture. Le SPF Affaires étrangères est devenu un coordinateur, gardant surtout les affaires consulaires, la sécurité et les relations interétatiques.</p>
<p>La coordination passe par la Conférence interministérielle de politique étrangère et la structure <strong>Coormulti</strong> (2003). Celle-ci ne se serait réunie que trois fois entre 2018 et 2023, y compris sur des sujets comme la stratégie envers la Chine.</p>
<h2>La leçon du CETA</h2>
<p>En 2016, le Parlement wallon a temporairement bloqué la signature de l'accord commercial UE-Canada. Le blocage a abouti à des garanties sur le règlement des différends et les normes environnementales ; en 2024, la Wallonie affichait un excédent commercial de 64,8 millions d'euros avec le Canada. Mais l'épisode a montré qu'aucun gouvernement fédéral ne peut engager seul le pays sur un traité « mixte ». Le Pacte mondial pour les migrations (2018) a produit une crise comparable.</p>
<h2>Faire plus avec moins</h2>
<p>Entre 2013 et 2024, le budget de la diplomatie (hors coopération au développement, qui dépasse 1,25 milliard d'euros) a perdu plus d'un quart de son pouvoir d'achat. Le réseau est passé de 131 postes en 2006 à 115. En 2024-2025, le SPF a engagé sa révision la plus profonde en quinze ans : huit fermetures, une vingtaine de postes renforcés, un pool de « diplomates volants ».</p>
{table(["Zone", "Décisions", "Logique"], [
 ("Balkans occidentaux", "Ouverture à Tirana, fermeture à Sarajevo", "Élargissement de l'UE, migrations"),
 ("Moyen-Orient", "Ambassadeur pour la Syrie (basé à Beyrouth), fermeture à Koweït", "Reconstruction, réfugiés"),
 ("Afrique subsaharienne", "Fermetures à Bamako, Maputo, Conakry", "Recul européen au Sahel"),
 ("Amérique latine, Asie", "Fermetures à La Havane, Rio, Guangzhou", "Concentration sur Brasilia et Pékin"),
], "La refonte du réseau diplomatique (2025-2027)")}
<h2>Team Belgium et diplomatie économique</h2>
<p>L'approche « Team Belgium » réunit agences fédérales (Enabel, BIO, Finexpo) et régionales (AWEX, Flanders Investment &amp; Trade, hub.brussels). Les missions économiques princières en sont la vitrine : au Brésil, près de 400 participants et 39 accords signés.</p>
<h2>Le réétalonnage Prévot</h2>
<p>Le ministre des Affaires étrangères Maxime Prévot (Les Engagés) revendique une diplomatie qui allie « fermeté sur les principes et réalisme sur le terrain » : plus de bilatéral, sécurisation des approvisionnements, conditionnalité migratoire de l'aide au développement, défense du droit international. Deux exemples : la {L("meso/afrique-grands-lacs/", "réconciliation avec le Rwanda")} et l'{L("meso/moyen-orient-droit-international/", "intervention devant la CIJ")}.</p>
<h2>Les relais d'influence</h2>
<ul>
<li><strong>Institut Egmont</strong> : fondé en 1947 par Paul van Zeeland, principal centre de réflexion en relations internationales.</li>
<li><strong>Francophonie</strong> : la Belgique siège à l'OIF à deux titres (État fédéral et Fédération Wallonie-Bruxelles), une tribune précieuse en Afrique.</li>
<li><strong>Benelux</strong> : coordination en amont des Conseils européens.</li>
</ul>
{levels("Multipolarité, compétition pour l'influence en Afrique.", "Diplomatie en réseau entre fédéral, Régions et Communautés.", "Diasporas, entreprises exportatrices, ONG et universités comme acteurs de la politique extérieure.")}
""",
 "sources": [("Egmont — Re-Empowering Belgian Foreign Policy", "https://egmontinstitute.be/re-empowering-belgian-foreign-policy/"),
             ("Cahiers ISPOLE — Belgium's foreign policy amid federalization (2025)", "https://shs.cairn.info/revue-cahiers-ispole-2025-1-page-3?lang=en"),
             ("SPF Affaires étrangères — Révision du réseau diplomatique", "https://diplomatie.belgium.be/fr/politique/themes-politiques/sous-la-loupe/une-revision-du-reseau-diplomatique-pour-mieux-defendre-les-interets-belges"),
             ("SPF Affaires étrangères — Rapport annuel 2024", "https://diplomatie.belgium.be/sites/default/files/2025-06/Rapport_annuel_SPF_2024.pdf"),
             ("Justice-en-ligne — La ratification du CETA", "https://www.justice-en-ligne.be/La-ratification-du-CETA-lorsque-la"),
             ("Brussels Times — How Maxime Prévot is changing Belgium's tune", "https://www.brusselstimes.com/1851921/how-maxime-prevot-is-changing-belgiums-tune-on-the-world-stage")],
 "related": ["belgique/federalisme/", "meso/afrique-grands-lacs/", "meso/soft-power/"],
},
{
 "slug": "meso/euroclear-avoirs-russes/", "section": S,
 "title": "Euroclear et les avoirs russes gelés : le dilemme belge",
 "h1": "Euroclear et les avoirs russes gelés : le dilemme belge",
 "desc": "Environ 210 milliards d'euros d'avoirs de la Banque centrale russe sont immobilisés chez Euroclear à Bruxelles. Bénéfices exceptionnels, prêt du G7, refus belge de la confiscation.",
 "lede": "Une chambre de compensation discrète de Bruxelles se retrouve au cœur de la plus grande opération de gel d'avoirs souverains de l'histoire. La Belgique y joue sa stabilité financière.",
 "keywords": ["Euroclear", "avoirs russes gelés", "prêt de réparation Ukraine", "windfall profits", "immunité des États"],
 "about": [("Euroclear", W + "Euroclear", "Organization"), BE, ("Banque centrale de la fédération de Russie", W + "Banque_centrale_de_Russie", "Organization")],
 "level_label": "Méso",
 "body": f"""
<h2>Ce qu'est Euroclear</h2>
<p>Institution privée de droit belge, Euroclear est un dépositaire central de titres : il conserve environ <strong>42 500 milliards d'euros</strong> de titres et traite des centaines de millions de transactions par an. C'est une pièce de la « plomberie » financière mondiale, peu connue du grand public.</p>
<h2>Le gel</h2>
<p>Depuis les sanctions européennes de 2022, environ <strong>210 milliards d'euros</strong> d'avoirs de la Banque centrale de Russie sont immobilisés dans ses livres. Coupons et remboursements ne pouvant être versés, les liquidités s'accumulent et sont réinvesties. Avec la remontée des taux, elles ont produit des bénéfices exceptionnels : 4,4 milliards d'euros en 2023, plus de 6 milliards en 2024, 2,3 milliards au seul premier semestre 2026.</p>
{kpis([("≈ 210 Md€", "d'avoirs russes immobilisés"), ("42 500 Md€", "de titres conservés par Euroclear"), ("99,7 %", "des bénéfices nets exceptionnels transférés à l'UE"), ("50 Md$", "prêt du G7 à l'Ukraine adossé à ces revenus")])}
<h2>Le compromis des bénéfices</h2>
<p>Sur la base de l'article 215 du TFUE, l'UE oblige Euroclear à reverser l'essentiel des bénéfices exceptionnels nets : 90 % à la Facilité européenne pour la paix (armement de l'Ukraine) et 10 % à la reconstruction. Ces flux garantissent le prêt de 50 milliards de dollars décidé par le G7. En 2023, l'impôt des sociétés sur ces bénéfices a rapporté 1,085 milliard d'euros au Trésor belge, ce qui a valu à Bruxelles des critiques de ses alliés.</p>
<h2>Pourquoi la Belgique refuse la confiscation</h2>
<ol>
<li><strong>Le droit</strong> : confisquer des avoirs de banque centrale violerait l'immunité souveraine des États et exposerait la Belgique à des poursuites, notamment au titre du traité bilatéral d'investissement belgo-luxembourgeois avec l'URSS/Russie.</li>
<li><strong>Le risque systémique</strong> : la BCE avertit qu'une confiscation unilatérale saperait la confiance des pays tiers (Chine, Golfe) et le statut de l'euro comme monnaie de réserve.</li>
<li><strong>L'asymétrie</strong> : les États-Unis détiennent quelque 5 milliards de dollars d'avoirs russes, l'Europe plus de 190 milliards ; les entreprises européennes ont encore environ 90 milliards d'actifs en Russie exposés à des représailles.</li>
</ol>
<p>La Belgique exige donc une <strong>mutualisation des risques</strong> au niveau européen (et du G7) avant tout pas supplémentaire, comme un « prêt de réparation » adossé au capital.</p>
<h2>La contre-offensive russe</h2>
<p>La Banque centrale russe a engagé des procédures, réclamant quelque 200 milliards d'euros devant ses tribunaux et menaçant de saisir les actifs occidentaux restants en Russie. En septembre 2026, elle poursuivait l'UE devant la justice européenne. L'UE a adopté un instrument protégeant les entités qui appliquent les sanctions contre ces jugements extraterritoriaux.</p>
{callout("<p>Le dossier Euroclear montre la « géoéconomie » à l'état pur : un petit pays, par la localisation d'une infrastructure, détient un levier stratégique… et en porte le risque.</p>", "lilac", "Pourquoi c'est important")}
{levels("Arsenalisation de la finance, réaction du Sud global (dédollarisation).", "Négociation UE-G7 sur le partage des risques ; la Belgique en position de veto de fait.", "Recettes fiscales belges, emplois financiers à Bruxelles, stabilité de l'épargne.")}
""",
 "sources": [("Parlement européen — EU sanctions and Russia's frozen assets (2025)", "https://www.europarl.europa.eu/RegData/etudes/STUD/2025/754487/EXPO_STU(2025)754487_EN.pdf"),
             ("Bruegel — How to harvest the windfall profits from Russian assets", "https://www.bruegel.org/analysis/how-harvest-windfall-profits-russian-assets-europe"),
             ("MR — Guerre en Ukraine : avoirs russes et Euroclear", "https://www.mr.be/argumentaires/guerre-en-ukraine-avoirs-russes-et-euroclear/"),
             ("Le Club des juristes — Prêt de réparations adossé aux avoirs russes", "https://www.leclubdesjuristes.com/international/lunion-europeenne-face-au-defi-dun-pret-de-reparations-a-lukraine-adosse-aux-avoirs-russes-12274/"),
             ("Ukrainska Pravda — Russian Central Bank sues EU (17/09/2026)", "https://www.pravda.com.ua/eng/news/2026/09/17/8053978/")],
 "related": ["monde/ordre-multipolaire/", "meso/union-europeenne/", "monde/conflits-2026/"],
},
{
 "slug": "meso/niches-strategiques/", "section": S,
 "title": "Les niches stratégiques belges : imec, biopharma, Umicore, île énergétique",
 "h1": "Les niches stratégiques de la Belgique",
 "desc": "imec et les semi-conducteurs sous 2 nm, « Biopharma Valley », recyclage des métaux critiques par Umicore, île énergétique Princesse Élisabeth : les goulets d'étranglement que contrôle la Belgique.",
 "lede": "Trop petite pour peser par la masse, la Belgique pèse par des nœuds : quelques infrastructures et savoir-faire sans lesquels l'autonomie stratégique européenne serait impossible.",
 "keywords": ["imec", "semi-conducteurs Belgique", "biopharma Belgique", "Umicore", "île Princesse Elisabeth", "Chips Act"],
 "about": [("imec", W + "Imec", "Organization"), ("Umicore", W + "Umicore", "Organization"), ("Île Princesse-Élisabeth", W + "%C3%8Ele_Princesse-%C3%89lisabeth", "Place")],
 "level_label": "Méso",
 "body": f"""
<h2>imec : le laboratoire des puces du monde</h2>
<p>Installé à Louvain (Leuven), l'<strong>imec</strong> est le principal centre mondial de recherche pré-concurrentielle en microélectronique. Il travaille avec ASML, TSMC, Intel ou Rapidus sur des gravures de 2 nanomètres et en deçà. Dans le cadre du <em>Chips Act</em> européen, il coordonne la ligne pilote <strong>NanoIC</strong>, qui accélère le passage du laboratoire à la production.</p>
<p>La rivalité sino-américaine l'a rattrapé : sous la pression des règles d'exportation américaines, l'imec a fortement réduit en 2024 ses collaborations avec des institutions chinoises. L'Institut Egmont (Policy Brief 415, septembre 2026) souligne les fragilités de l'écosystème belge : beaucoup de PME de conception, pas de fonderie de masse, des coûts de production européens 15 à 30 % supérieurs à l'Asie. Il plaide pour exploiter le <em>Chips Act 2.0</em> et des niches comme la photonique (université de Gand).</p>
<h2>La « Biopharma Valley »</h2>
<p>La Belgique concentre production de vaccins, thérapies géniques et essais cliniques. Le secteur y investit environ <strong>5,3 milliards d'euros par an en R&amp;D</strong>, près d'un dixième de l'effort européen. En Wallonie, le pôle BioWin fédère un écosystème qui pèse 6,2 % de l'économie régionale ; la Région a débloqué 81 millions d'euros pour les médicaments de thérapie innovante.</p>
{callout("<p>Les fédérations sectorielles (essenscia, pharma.be) signalent en 2025-2026 plus de 1 500 emplois perdus en chimie-pharma et un recul des exportations d'environ 5 %, entre l'attractivité américaine et la concurrence chinoise sur les principes actifs.</p>", "warn", "Signaux d'alerte")}
<h2>Umicore et les métaux critiques</h2>
<p>Face au quasi-monopole chinois du raffinage, la Belgique mise sur la circularité : <strong>Umicore</strong> (Hoboken, Olen) récupère plus de 95 % des métaux des batteries lithium-ion. La diplomatie belge promeut aussi, en RDC (70 % du cobalt mondial), des partenariats respectant des normes sociales et environnementales et favorisant le raffinage local, en alternative à l'emprise chinoise (70 à 80 % du cuivre et du cobalt congolais).</p>
<h2>L'île énergétique Princesse Élisabeth</h2>
<p>À 45 km des côtes, le gestionnaire de réseau <strong>Elia</strong> construit la première île énergétique artificielle au monde : 23 caissons de béton, 3,5 GW d'éolien offshore raccordés, interconnexions prévues vers le Royaume-Uni (Nautilus) et le Danemark (TritonLink). Le projet, soutenu par la BEI, a vu ses coûts dériver de plus de 1,3 milliard d'euros. Il s'inscrit dans la déclaration d'Ostende : 120 GW d'éolien en mer du Nord en 2030, 300 GW en 2050.</p>
{table(["Niche", "Acteur", "Enjeu géopolitique"], [
 ("Microélectronique", "imec (Louvain)", "Recherche sous 2 nm, cœur du Chips Act"),
 ("Santé", "Biopharma Valley, BioWin", "Souveraineté sanitaire européenne"),
 ("Métaux critiques", "Umicore", "Recyclage face au monopole chinois"),
 ("Énergie", "Elia, Jan De Nul, DEME", "Hub électrique de la mer du Nord"),
 ("Finance", "Euroclear, SWIFT", "Plomberie financière mondiale"),
 ("Espace", "ESEC Redu", "Cybersécurité des constellations européennes"),
], "Les nœuds belges de l'autonomie stratégique européenne")}
{levels("Guerre des puces, des minerais et de l'énergie.", "Politique industrielle européenne (Chips Act, CRMA, REPowerEU) et politiques régionales.", "Emplois très qualifiés à Louvain, Gosselies, Hoboken ; formation et attractivité des universités.")}
""",
 "sources": [("Egmont — Strengthening Belgium's Semiconductor Ecosystem (Policy Brief 415)", "https://egmontinstitute.be/app/uploads/2026/09/Foulon_De-Decker_Policy_Brief_415_vFinal.pdf?type=pdf"),
             ("Représentation de la Commission — L'Europe investit dans l'imec (2026)", "https://belgium.representation.ec.europa.eu/actualites-et-evenements/actualites/leurope-investit-des-milliards-dans-linnovation-en-matiere-de-semi-conducteurs-limec-de-louvain-2026-02-09_fr"),
             ("essenscia — La chimie et la pharma belges à un tournant", "https://www.essenscia.be/fr/la-chimie-et-la-pharma-belges-a-un-tournant-perte-demplois-exportations-en-recul-et-investissements-en-berne/"),
             ("Belgium.be — Biopharma, un secteur clé", "https://openforbusiness.belgium.be/fr/innovation/biopharma-un-secteur-cle-en-belgique"),
             ("SPF Affaires étrangères — Durabilité dans l'exploitation minière (Lubumbashi)", "https://diplomatie.belgium.be/fr/politique/themes-politiques/sous-la-loupe/des-reseaux-au-service-de-la-durabilite-dans-le-secteur-de-lexploitation-miniere-et-des-matieres-premieres-critiques-lubumbashi"),
             ("Jan De Nul — Princess Elisabeth Island", "https://www.jandenul.com/projects/princess-elisabeth-island-belgium"),
             ("BEI — La Belgique construit la première île énergétique", "https://www.eib.org/fr/stories/offshore-wind-energy-island-belgium")],
 "related": ["monde/geoeconomie/", "belgique/economie/", "belgique/energie-climat/"],
},
{
 "slug": "meso/afrique-grands-lacs/", "section": S,
 "title": "La Belgique, la RDC et le Rwanda : politique africaine en 2026",
 "h1": "La Belgique et les Grands Lacs : RDC, Rwanda, minerais",
 "desc": "Rupture puis rétablissement des relations belgo-rwandaises (2026), conflit du M23 dans l'est de la RDC, minerais critiques et poids du passé colonial.",
 "lede": "L'Afrique centrale reste pour la Belgique une priorité historique et émotionnelle. En 2026, elle y pratique une diplomatie plus transactionnelle.",
 "keywords": ["Belgique Rwanda 2026", "RDC M23", "Grands Lacs", "politique africaine Belgique", "cobalt RDC"],
 "about": [("République démocratique du Congo", WD + "Q974", "Country"), ("Rwanda", WD + "Q1037", "Country"), ("Mouvement du 23 mars", W + "Mouvement_du_23_mars", "Organization")],
 "level_label": "Méso",
 "body": f"""
<h2>Un lien singulier</h2>
<p>Ancienne puissance coloniale du Congo, du Rwanda et du Burundi, la Belgique entretient avec la région des Grands Lacs des relations chargées d'histoire, d'importantes diasporas et des intérêts économiques, dont l'accès aux minerais critiques. Le travail de mémoire sur la période coloniale reste un sujet politique et sociétal en Belgique.</p>
<h2>Le conflit dans l'est de la RDC</h2>
<p>Le groupe rebelle <strong>M23</strong>, soutenu par Kigali selon les Nations unies et de nombreux États, s'est emparé de territoires clés des Kivu, riches en minerais. D'autres groupes (FDLR, ADF affiliées à l'État islamique) commettent aussi des atrocités contre les civils. La Belgique a fermement condamné l'ingérence rwandaise.</p>
<h2>Rupture et réconciliation</h2>
<p>La condamnation belge a provoqué une rupture diplomatique de dix-huit mois : fermeture de l'ambassade rwandaise à Bruxelles, coopération suspendue. En <strong>septembre 2026</strong>, sous médiation du Qatar, les deux pays ont rétabli leurs relations. Le ministre Maxime Prévot assure que cela ne signifie pas l'abandon des principes : soutien à l'intégrité territoriale et à la souveraineté de la RDC, pression maintenue au sein du Groupe de contact international sur les Grands Lacs.</p>
{callout("<p>Rétablir un canal direct permet de peser sur Kigali, de débloquer la coopération et de faciliter la vie de la diaspora rwandaise en Belgique. Le risque : que le pragmatisme soit perçu à Kinshasa comme un lâchage.</p>", "lilac", "Le pari du réalisme")}
<h2>La bataille des minerais</h2>
<p>La RDC produit environ 70 % du cobalt mondial et une part importante du germanium. La Chine y contrôle 70 à 80 % du marché du cuivre et du cobalt. La « Team Belgium » (diplomates, Enabel, entreprises) promeut lors d'événements comme la <em>DRC Mining Week</em> de Lubumbashi des partenariats fondés sur des normes ESG et le raffinage local. L'enjeu rejoint la stratégie européenne sur les matières premières critiques ({L("meso/niches-strategiques/", "Umicore")}).</p>
<h2>Au-delà des Grands Lacs</h2>
<p>La Belgique réduit sa présence au Sahel (fermeture de Bamako) face au recul de l'influence européenne et à l'arrivée de l'Africa Corps russe. Elle mise sur la Francophonie, où elle dispose de deux sièges, pour maintenir son influence culturelle et universitaire.</p>
{levels("Compétition sino-occidentale pour les minerais, recul européen au Sahel.", "Diplomatie belge bilatérale, médiation qatarie, Groupe de contact international.", "Diasporas congolaise et rwandaise en Belgique, mémoire coloniale, consommateurs de smartphones et de batteries.")}
""",
 "sources": [("Brussels Times — Belgium and Rwanda restore diplomatic relations", "https://www.brusselstimes.com/belgium/2329118/belgium-and-rwanda-restore-diplomatic-relations"),
             ("Anadolu — Belgium announces resumption of relations with Rwanda", "https://www.aa.com.tr/en/europe/belgium-announces-resumption-of-diplomatic-relations-with-rwanda/4065671"),
             ("SPF Affaires étrangères — International Contact Group for the Great Lakes", "https://diplomatie.belgium.be/en/news/international-contact-group-great-lakes-icg"),
             ("CFR — Conflict in the DRC", "https://www.cfr.org/global-conflict-tracker/conflict/violence-democratic-republic-congo"),
             ("SPF Affaires étrangères — DRC Mining Week, Lubumbashi", "https://diplomatie.belgium.be/fr/politique/themes-politiques/sous-la-loupe/des-reseaux-au-service-de-la-durabilite-dans-le-secteur-de-lexploitation-miniere-et-des-matieres-premieres-critiques-lubumbashi")],
 "related": ["meso/diplomatie-belge/", "monde/conflits-2026/", "meso/niches-strategiques/"],
},
{
 "slug": "meso/moyen-orient-droit-international/", "section": S,
 "title": "La Belgique, Gaza et le droit international : CIJ, CPI, exportations d'armes",
 "h1": "La Belgique et le droit international : CIJ, CPI et Gaza",
 "desc": "Intervention belge devant la CIJ (décembre 2025), soutien à la CPI face aux sanctions américaines, arrêt de la cour d'appel de Bruxelles sur les exportations d'armes (mars 2026).",
 "lede": "Pour échapper au reproche du « deux poids, deux mesures », la Belgique se pose en défenseur des juridictions internationales. Cette posture est aussi dictée par ses propres tribunaux.",
 "keywords": ["Belgique CIJ", "Cour pénale internationale", "Gaza droit international", "exportations d'armes Israël Belgique", "génocide Convention"],
 "about": [("Cour internationale de justice", W + "Cour_internationale_de_justice", "Organization"), ("Cour pénale internationale", W + "Cour_p%C3%A9nale_internationale", "Organization"), BE],
 "level_label": "Méso",
 "body": f"""
<h2>Deux cours, deux logiques</h2>
<p>La <strong>Cour internationale de justice</strong> (CIJ, organe de l'ONU) tranche les différends entre États. La <strong>Cour pénale internationale</strong> (CPI) juge la responsabilité individuelle pour génocide, crimes contre l'humanité et crimes de guerre. La Belgique soutient les deux.</p>
<h2>Défendre la CPI</h2>
<p>Lorsque le procureur de la CPI a demandé des mandats d'arrêt contre des dirigeants du Hamas ainsi que contre le Premier ministre et le ministre de la Défense israéliens, la Chambre des représentants américaine a menacé la Cour de sanctions. Membre du Bureau de l'Assemblée des États parties (2024-2026), la Belgique a coordonné avec la Slovénie, le Chili, la Jordanie et le Sénégal une déclaration de soutien signée par <strong>93 des 124 États parties</strong>.</p>
<h2>L'intervention devant la CIJ</h2>
<p>En <strong>décembre 2025</strong>, la Belgique a déposé une déclaration d'intervention (article 63 du Statut) dans l'affaire introduite par l'Afrique du Sud contre Israël au titre de la Convention sur le génocide. Son argumentaire souligne que des opérations militaires en apparence légitimes peuvent coïncider avec une intention génocidaire, et que des violations systématiques du droit humanitaire peuvent en constituer des indices. La Belgique avait déjà plaidé dans l'avis consultatif sur l'illégalité de l'occupation des territoires palestiniens.</p>
<h2>La pression des tribunaux belges</h2>
<p>En <strong>mars 2026</strong>, la cour d'appel de Bruxelles a rendu un arrêt jugeant que l'État belge avait manqué à son obligation de prévention en ne bloquant pas certains transits d'armes et de biens à double usage vers Israël. Le gouvernement doit désormais justifier rigoureusement chaque licence, ce qui met en tension intérêts industriels de défense et impératifs éthiques. Des ONG et collectifs citoyens multiplient les actions en justice.</p>
{callout("<p>Depuis 2003, l'octroi des licences d'exportation, d'importation et de transit d'armes relève des Régions (surtout la Wallonie, qui abrite FN Herstal et John Cockerill), alors que la politique étrangère et les obligations internationales engagent l'État fédéral : encore une illustration du fédéralisme belge en politique extérieure.</p>", "lilac", "Qui décide ?")}
<h2>Une position d'ensemble</h2>
<p>La Belgique conditionne son soutien à la reconstruction de Gaza à la viabilité d'une solution à deux États et au renforcement de la gouvernance palestinienne. Elle combine ainsi alignement euro-atlantique sur la sécurité et autonomie juridique sur le droit humanitaire.</p>
{levels("Érosion de l'ordre juridique international, accusations de double standard.", "Diplomatie juridique belge, coordination avec des États du Sud.", "Mobilisations citoyennes, clivages politiques internes, recours devant les tribunaux.")}
""",
 "sources": [("SPF Affaires étrangères — Soutien à une CPI indépendante", "https://diplomatie.belgium.be/fr/politique/themes-politiques/sous-la-loupe/la-belgique-soutien-indefectible-dune-cour-penale-internationale-independante-et-impartiale"),
             ("ONU (UNISPAL) — La Belgique dépose une déclaration d'intervention (23/12/2025)", "https://www.un.org/unispal/document/belgium-files-a-declaration-ic-23dec25/"),
             ("EJIL:Talk! — Brussels Court of Appeal, 16 March 2026", "https://www.ejiltalk.org/domestic-courts-and-the-states-obligation-to-prevent-genocide-and-serious-violations-of-ihl-the-brussels-court-of-appeals-interlocutory-judgment-of-16-march-2026/"),
             ("ULB — La guerre de Gaza et le droit international", "https://cdi.ulb.ac.be/la-guerre-de-gaza-et-le-droit-international/"),
             ("JusticeInfo — Justice pour Gaza : qui fait quoi ?", "https://www.justiceinfo.net/fr/151717-justice-pour-gaza-qui-fait-quoi.html")],
 "related": ["monde/conflits-2026/", "meso/diplomatie-belge/", "monde/democratie/"],
},
{
 "slug": "meso/soft-power/", "section": S,
 "title": "Soft power belge : réputation, classements et image internationale",
 "h1": "Le soft power belge : réputation forte, voix discrète",
 "desc": "Global Soft Power Index 2026 (20e), réputation, paix, bonheur, universités, politique d'État hôte : forces et limites de l'image internationale de la Belgique.",
 "lede": "La Belgique inspire confiance plus qu'elle n'impressionne. Son influence est celle d'un médiateur : efficace dans les coulisses, souvent inaudible sur la grande scène.",
 "keywords": ["soft power Belgique", "Global Soft Power Index 2026", "image de la Belgique", "nation branding"],
 "about": [BE, ("Soft power", W + "Soft_power")],
 "level_label": "Méso",
 "body": f"""
<h2>Les classements</h2>
{table(["Classement", "Rang de la Belgique"], [
 ("Global Soft Power Index 2026 (Brand Finance, 193 pays)", "20ᵉ"),
 ("Sous-indice « Réputation » (Brand Finance)", "Parmi les tout premiers"),
 ("Global Peace Index 2024", "16ᵉ"),
 ("World Happiness Report 2024", "16ᵉ"),
 ("Indice de perception de la corruption 2023", "16ᵉ"),
 ("KU Leuven, World University Rankings 2024", "45ᵉ université mondiale"),
], "La Belgique dans les indices internationaux")}
<h2>Les sources de l'influence</h2>
<ul>
<li><strong>La fonction d'hôte</strong> : UE, OTAN, plus de soixante organisations internationales, une diplomatie multilatérale dense.</li>
<li><strong>La qualité de vie et le modèle social</strong>, reconnus par les indices de bonheur et de paix.</li>
<li><strong>Les universités</strong> (KU Leuven, UGent, UCLouvain, ULB, ULiège…) et la recherche ({L("meso/niches-strategiques/", "imec, biopharma")}).</li>
<li><strong>La culture</strong> : bande dessinée, gastronomie, festivals, architecture Art nouveau, et une scène artistique bilingue.</li>
<li><strong>La Francophonie</strong> et les liens avec l'Afrique centrale.</li>
</ul>
<h2>Les freins</h2>
<p>Les observateurs citent la complexité institutionnelle et la lenteur de formation des gouvernements (541 jours en 2010-2011, 613 jours à Bruxelles en 2024-2026), le narcotrafic à Anvers qui écorne l'image de sécurité, et une identité nationale peu projetée. Contrairement à la France (puissance culturelle) ou à l'Allemagne (puissance commerciale), la Belgique agit en facilitateur.</p>
{callout("<p>La discrétion peut être un atout : un pays sans ambition hégémonique est un médiateur crédible. Encore faut-il des moyens diplomatiques pour transformer la réputation en influence.</p>", "lilac", "Analyse")}
""",
 "sources": [("Brand Finance — Global Soft Power Index 2026", "https://brandfinance.com/insights/global-soft-power-index-2026-executive-summary"),
             ("Place Brand Observer — Belgium country performance", "https://placebrandobserver.com/belgium-country-performance-brand-strength-reputation/"),
             ("Monocle — Soft Power Survey", "https://monocle.com/affairs/soft-power-survey-annual-ranking/")],
 "related": ["meso/diplomatie-belge/", "belgique/bruxelles/", "micro/identites/"],
},
]
