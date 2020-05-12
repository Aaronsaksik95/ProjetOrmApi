phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 12, 2020 at 01:19 PM
-- Server version: 5.7.26
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `projetApiOrm`
--

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

CREATE TABLE `article` (
  `id` int(11) NOT NULL,
  `image_article` text NOT NULL,
  `auteur_article` varchar(50) DEFAULT NULL,
  `title_article` text NOT NULL,
  `desc_article` text NOT NULL,
  `content_article` text NOT NULL,
  `date_article` date DEFAULT NULL,
  `source_article` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `article`
--

INSERT INTO `article` (`id`, `image_article`, `auteur_article`, `title_article`, `desc_article`, `content_article`, `date_article`, `source_article`) VALUES
(81, 'https://img.20mn.fr/Azps07_KS_SJKPxxdUM2mQ/648x360_olivier-veran-ministre-sante.jpg', NULL, 'Coronavirus EN DIRECT : Olivier Véran appelle les Français à ne pas « tout gâcher » après des images de regroupement', 'Coronavirus / Covid 19 live : suivez les dernières avancées concernant la propagation du coronavirus en France et son confinement', '8h35 : Vers une réouverture progressive des musées\r\nAlors que les grands musées rongent leur frein, la réouverture des petits musées et monuments est désormais possible. Mais elle sannonce progressive, beaucoup visant début juin, fixé aussi par lexécutif pour… [+714 chars]', '2020-05-12', 'Google News (France)'),
(82, 'https://img.20mn.fr/IMaEqcVeRp2gbADNmndNZA/648x360_restez-chez-mantra-13e-jour-confinement-france.jpg', 'M.P. avec AFP', 'Coronavirus en Nouvelle-Aquitaine : Que sait-on des deux clusters identifiés en Dordogne et dans la Vienne ?', 'Deux foyers de coronavirus ont été identifiés en Nouvelle-Aquitaine ces derniers jours, en Dordogne et dans la Vienne', '« Restez chez vous », le mantra au 13e jour de confinement en France. NICOLAS MESSYASZ/SIPA\r\nNeuf personnes positives au Covid-19, à lEglise-Neuve-de-Vergt en Dordogne. Quatre, parmi les proches des membres de la direction du Collège de Chauvigny, dans la Vie… [+5515 chars]', '2020-05-12', 'Google News (France)'),
(83, 'https://i.ytimg.com/vi/fyzKV9nhcz0/maxresdefault.jpg', NULL, 'Le canal Saint-Martin à Paris évacué par la police, l\'alcool désormais interdit', 'Au premier jour du déconfinement, le 11 mai, les Parisiens se sont rués le long du canal Saint-Martin, lieu prisé pour les apéritifs. Aux alentours de 19h30,...', 'Au premier jour du déconfinement, le 11 mai, les Parisiens se sont rués le long du canal Saint-Martin, lieu prisé pour les apéritifs. Aux alentours de 19h30,...', '2020-05-12', 'Google News (France)'),
(84, 'https://www.bfmtv.com/i/0/0/1aa/a87071ed285fc384087f70188ec3a.jpeg', 'BFMTV', 'Qui sont les 1% des Français les plus riches?', 'Dans une étude parue ce mardi, l\'Insee dévoile le profil des 1% des ménages les plus riches. Ces derniers vivent essentiellement en Ile-de-France et dans les départements frontaliers. Tandis que leurs ressources se composent davantage de revenus issus d\'activ…', 'Dans une étude parue ce mardi, l\'Insee dévoile le profil des 1% des ménages les plus riches. Ces derniers vivent essentiellement en Ile-de-France et dans les départements frontaliers. Tandis que leurs ressources se composent davantage de revenus issus d\'activ… [+18 chars]', '2020-05-12', 'Google News (France)'),
(85, 'https://img-0.journaldunet.com/_mLV3WuykuXarGxR2PWLNOhXm5Y=/540x/smart/9bd3f7c241ee405789ce657ddb164e77/ccmcms-jdn/15606773.jpg', 'Justine Gay', 'Attestation 100 km : téléchargez ou générez la déclaration...', '[ATTESTATION 100 KILOMETRES] La nouvelle attestation, à présenter au format papier ou numérique pour parcourir plus de 100 kilomètres hors de son département de résidence, est disponible. Voici les liens pour télécharger le PDF ou générer le QR code sur son s…', 'DECLARATION DE DEPLACEMENT\r\nEN DEHORS DE SON DEPARTEMENT ET\r\n A PLUS DE 100 KM DE SA RESIDENCE\r\nEn application des mesures générales prises pour faire face\r\nà l\'épidémie de covid-19 dans le cadre de l\'état d\'urgence sanitaire\r\n<table><tr><td>PERSONNE CONCERNE… [+2448 chars]', '2020-05-12', 'Google News (France)'),
(86, 'https://images.sudouest.fr/2020/05/12/5eba67bd66a4bde473411511/golden/rentree-scolaire-post.jpg', 'Sud Ouest', 'Déconfinement à Bordeaux : dans les écoles, rentrée en bon ordre pour les élèves', 'Seuls les élèves de grande section, de CP et de CM2 sont accueillis dans un premier temps depuis ce mardi 12 mai. Pour la récré, ce sera sous le préau pour les uns, dans la cour pour les autres. Sans se toucher.', 'Les 105 écoles maternelles et primaires de Bordeaux ont fait leur rentrée post-confinement ce mardi matin à part Condorcet et Flornoy où les équipes pédagogiques ont préféré attendre jeudi. \r\n&gt;&gt; A lire aussi : Déconfinement : ce mardi, nouvelle journée … [+2059 chars]', '2020-05-12', 'Google News (France)'),
(87, 'https://cdn-media.rtl.fr/online/image/2020/0415/7800401622_valerie-pecresse-le-30-juin-2018.jpg', NULL, 'Coronavirus : Valérie Pécresse \"redoute une génération sacrifiée\"', 'INVITÉE RTL - La présidente de l\'Île-de-France demande un plan de relance pour les entreprises \"avant l\'été\".', '\"Il faut une mobilisation générale pour la jeunesse\". Valérie Pécresse lance un appel à l\'antenne de RTL ce mardi 12 mai. La présidente de la région Île-de-France \"redoute une génération sacrifiée\". \r\n\"Aujourd\'hui, les entreprises ont mis une bonne partie de … [+1162 chars]', '2020-05-12', 'Google News (France)'),
(88, 'https://arc-anglerfish-eu-central-1-prod-leparisien.s3.amazonaws.com/public/MECFCR57RNURHDUAV74SDGPHMY.jpg', NULL, 'DIRECT. Coronavirus : des plages de la Côte d’Azur pourraient rouvrir ce week-end', 'Le gouvernement entend poursuivre la levée progressive du confinement, qui a débuté lundi avec la reprise de l’activité de nombreux commerce', '&gt; L\'essentiel\r\n&gt; Suivez les événements de la journée en direct :\r\n12h55. Pas de dépistage pour les athlètes des Jeux militaires. La secrétaire d\'Etat aux Armées Geneviève Darrieussecq, interrogée lors d\'une audition au Sénat, estime que dépister les ath… [+18922 chars]', '2020-05-12', 'Google News (France)'),
(89, 'https://img.lemde.fr/2020/05/11/208/0/2500/1250/1440/720/60/0/bea9b70_XwriVjvMS0rj31AEDBkaR3Zp.jpg', 'Denis Cosnard', 'A Paris, un début de déconfinement presque en douceur et sans cohue dans les transports', 'Lundi 11 mai, l’activité a repris progressivement en Ile-de-France. Sans embouteillages dans les rues ni cohue généralisée dans les transports en commun.', 'Dans le métro, à Paris, le 11 mai. CAMILLE MILLERAND POUR « LE MONDE »\r\nCe lundi 11 mai, Carole est sortie tôt de chez elle. Plus question de faire des grasses matinées. Le salon de coiffure dans lequel elle travaille, rue dAvron (20e arrondissement), rouvre … [+2631 chars]', '2020-05-11', 'Google News (France)'),
(90, 'https://www.bfmtv.com/i/0/0/94c/dd7ddad4478cdad5b4c56c09a4645.png', 'BFMTV', 'Feu vert du gouvernement pour l\'installation des conseils municipaux élus au 1er tour', 'Un conseil municipal a été élu au complet au premier tour dans plus de 30.000 communes, sur un total d\'environ 35.000.', 'Un conseil municipal a été élu au complet au premier tour dans plus de 30.000 communes, sur un total d\'environ 35.000.', '2020-05-12', 'Google News (France)'),
(91, 'https://www.francetvinfo.fr/image/75rzjcfrp-5402/1500/843/21500351.jpg', NULL, 'Déconfinement : un syndicat de médecins met en garde contre \"le risque de revenir en arrière\" après les rassemblements au canal Saint-Martin à Paris', '<ol><li>Déconfinement : un syndicat de médecins met en garde contre \"le risque de revenir en arrière\" après les ras...  franceinfo\r\n</li><li>Paris : après l\'évacuation du canal Saint-Martin, Castaner hausse le ton  Le Point\r\n</li><li>Déconfinement : l\'alcool …', '\"Si on veut se retrouver un petit peu sur l\'espace public, au moins portons un masque\", insiste Jacques Battistoni du syndicat MG France, après que le préfet de Paris a pris une mesure d\'interdiction de consommation d\'alcool sur les berges motivée par des fêt… [+2722 chars]', '2020-05-12', 'Google News (France)'),
(92, 'https://www.francetvinfo.fr/image/75rziql9m-3031/1500/843/21498505.jpg', NULL, '\"J\'ai l\'impression de tout flinguer en retournant au bureau\" : à l\'heure du déconfinement, ces salariés veulent rester en télétravail', '<ol><li>\"J\'ai l\'impression de tout flinguer en retournant au bureau\" : à l\'heure du déconfinement, ces salariés veu...  franceinfo\r\n</li><li>Déconfinement : « Pas de raison que l’Etat continue à payer l\'intégralité des salaires » en chômage partiel,…  20 Minu…', 'Continuer d\'exercer son activité professionnelle à domicile : c\'est le souhait de certains travailleurs, malgré la sortie progressive du confinement entamée lundi et l\'opposition de leur employeur.\r\nIls y vont à reculons. Pour des dizaines de millions de Fran… [+8099 chars]', '2020-05-12', 'Google News (France)'),
(93, 'https://www.numerama.com/content/uploads/2020/05/car-1149997_1920.jpg', 'Marcus Dupont-Besnard', 'Attestation de déplacement à plus de 100 km sur smartphone : comment l’utiliser et où la télécharger', 'Il faut se munir d’une attestation pour dépasser un rayon de plus de 100km autour de chez vous. Elle est disponible au format numérique.', 'Il faut se munir dune attestation pour dépasser un rayon de plus de 100km autour de chez vous. Elle est disponible au format numérique.\r\nDurant cette première phase de déconfinement lancée le 11 mai 2020, sortir de chez soi est de nouveau autorisé. Il ny a do… [+5610 chars]', '2020-05-12', 'Google News (France)'),
(94, 'https://medias.liberation.fr/photo/1312800-xx.jpg?modified_at=1589266639&amp;picto=fb&amp;ratio_x=191&amp;ratio_y=100&amp;width=1080', 'Marie Piquemal', '«Mon inspectrice voulait absolument que j’accueille des enfants dès ce matin, j\'ai dû batailler»', 'Les directeurs d\'école se retrouvent à nouveau en première ligne, avec la lourde tâche d\'orchestrer un retour en classe en respectant les consignes sanitaires. A tour de rôle, trois directeurs d\'école racontent cette folle semaine, chaque matin dans «Libé». E…', 'Toute la semaine, Libération donne la parole à des directeurs décole, en première ligne pour orchestrer le retour à lécole, en mettant en uvre un protocole sanitaire très strict. A tour de rôle, de bon matin dans Libé, trois directeurs décole livrent donc leu… [+3087 chars]', '2020-05-12', 'Google News (France)'),
(95, 'https://www.bfmtv.com/i/0/0/6eb/e002f4d24e5a10a0c3244c4f445be.jpeg', 'BFMTV', 'Bac 2020: Blanquer appelle les lycéens de première à « réviser leurs textes » pour l\'oral de français', 'Le ministre de l\'Éducation nationale a affirmé que l\'épreuve était pour l\'heure toujours maintenue.', 'Le ministre de l\'Éducation nationale a affirmé que l\'épreuve était pour l\'heure toujours maintenue.', '2020-05-11', 'Google News (France)'),
(96, 'https://img.20mn.fr/0_Z2DwgLQ-OJHEVEnAB5uA/648x360_bureau-vote-france-15-mars-2020-elections-municipales.jpg', '20 Minutes avec AFP', 'Municipales 2020 : Feu vert du gouvernement à l’installation des conseils municipaux élus au 1er tour', 'Sur 35.000 communes, 30.000 conseils municipaux ont été élus dès le premier tour des élections le 15 mars dernier', 'Un bureau de vote en France, le 15 mars 2020 pour les élections municipales. SEBASTIEN COURDJI/SIPA\r\nSuite à lavis du conseil scientifique, le gouvernement a donné son feu à linstallation des 30.000 conseils municipaux élus dès le premier tour \r\ndes élections… [+718 chars]', '2020-05-12', 'Google News (France)'),
(97, 'https://images.ladepeche.fr/api/v1/images/view/5eba82c23e454663f8457985/large/image.jpg?v=1', 'Cyril Brioulet', 'Attestation pour les déplacements de plus de 100 km : ce que vous devez savoir avant de l\'utiliser', 'Le ministère de l\'Intérieur a mis en ligne lundi soir la nouvelle attestation à utiliser pour les déplacements de plus de 100 km. Qui peut l\'utiliser, sous quelles conditions, où la télécharger ? La Dépêche vous répond.', 'l\'essentiel\r\n Le ministère de l\'Intérieur a mis en ligne lundi soir la nouvelle attestation à utiliser pour les déplacements de plus de 100 km. Qui peut l\'utiliser, sous quelles conditions, où la télécharger ? La Dépêche vous répond.\r\n Ne l\'appelez plus attes… [+3188 chars]', '2020-05-12', 'Google News (France)'),
(98, 'https://arc-anglerfish-eu-central-1-prod-leparisien.s3.amazonaws.com/public/RRZSCMWETBI2OLU54JD356MOTY.jpg', NULL, 'Paris : Hidalgo veut «ouvrir à la promenade les parcs et les jardins», Véran refuse', 'La maire de la capitale proposait que le port du masque y soit obligatoire.  Le ministre de la Santé lui a finalement opposé une fin de non-', 'Il s\'agit de l\'une des deux rares différences, sur le papier, entre les départements classés rouge et ceux en vert. Dans les premiers, les parcs et les jardins doivent rester fermés lors de la première phase du déconfinement ayant débuté le 11 mai.\r\nAnne Hida… [+2596 chars]', '2020-05-12', 'Google News (France)'),
(99, 'https://img.lemde.fr/2020/05/12/423/0/5381/2684/1440/720/60/0/9194e85_1R78UuCNOWiU_WVtJe6u8ICQ.jpg', NULL, 'Coronavirus dans le monde : les Etats-Unis dénombrent plus de 80 000 morts', 'Alors que les assouplissements se multiplient, la crainte d’une deuxième vague reste entière en Europe comme aux Etats-Unis, où le coronavirus touche désormais directement la Maison Blanche.', 'Un homme prend sa pause dans le quartier financier de New York, le 11 mai. SPENCER PLATT / AFP\r\nLa pandémie due au coronavirus a fait au moins 286 122 morts dans le monde depuis son apparition en décembre en Chine, selon un bilan établi par lAgence France-Pre… [+7636 chars]', '2020-05-12', 'Google News (France)'),
(100, 'https://photos.lci.fr/images/613/344/paris-nuit-254558-0@1x.jpeg', 'La rédaction de LCI', 'Odeur de soufre en Île-de-France : les analyses ne permettent pas de lever le mystère', 'RESULTATS - Les très nombreux internautes d’Île-de-France qui ont témoigné sur les réseaux sociaux dans la nuit de dimanche à lundi après avoir senti une drôle d’odeur de soufre vont être déçus : les prélèvements d’air effectués n’expliquent pas cette odeur, …', 'Une odeur, de soufre ou d’œuf pourri selon les témoignages, et des questions. Les analyses effectuées après qu’une mystérieuse odeur a été ressentie en Ile-de-France dans la nuit du dimanche 10 au lundi 11 mai n’ont pas permis d’apporter de réponse. La préfec… [+2253 chars]', '2020-05-12', 'Google News (France)'),
(101, 'https://i.f1g.fr/media/cms/orig/2020/05/11/97d3b417c13aa85756b91bb57a76abbca5ad68d5fd4fd3bb6e5b8eddecaa198f.jpeg', 'Claudia Cohen', 'Déconfinement : «On ne va pas choisir entre la santé et l\'emploi, il faut les deux», affirme Pénicaud', 'La ministre du Travail a précisé qu\'une disposition du projet de loi d\'urgence assouplissait les possibilités de renouvellement ou de prolongation des contrats courts pour les entreprises.', '«On ne va pas choisir entre la santé et l\'emploi, il faut les deux», a martelé Muriel Pénicaud ce matin. Invitée sur LCI, la ministre du Travail a envoyé des signaux clairs : il faut reprendre le chemin du travail pour «sauver l\'emploi à terme». Après près de… [+4500 chars]', '2020-05-11', 'Google News (France)'),
(102, 'https://images.sudouest.fr/2020/05/10/5eb90bb666a4bd42244114fd/golden/en-dordogne-un-cluster.jpg', 'Sud Ouest', 'Coronavirus en Nouvelle-Aquitaine : le point sur ces clusters en Dordogne et dans la Vienne', 'Deux foyers de coronavirus identifiés en Nouvelle-Aquitaine ces derniers jours, en Dordogne et dans la Vienne, n\'ont pas donné lieu à de nouveaux cas positifs dimanche malgré des dizaines de tests. Les autorités ont toutefois redoublé les appels à la vigilanc…', 'Deux foyers de coronavirus identifiés en Nouvelle-Aquitaine ces derniers jours, en Dordogne et dans la Vienne, n’ont pas donné lieu à de nouveaux cas positifs dimanche malgré des dizaines de tests, ont indiqué les autorités de santé, profitant de ces mini-clu… [+3280 chars]', '2020-05-11', 'Google News (France)');

-- --------------------------------------------------------

--
-- Table structure for table `commentaire`
--

CREATE TABLE `commentaire` (
  `id` int(11) NOT NULL,
  `content_com` text NOT NULL,
  `date_com` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(4, 'aaron99', 'azerty');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `commentaire`
--
ALTER TABLE `commentaire`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `article`
--
ALTER TABLE `article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `commentaire`
--
ALTER TABLE `commentaire`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
