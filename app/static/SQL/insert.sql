INSERT INTO SPECTATEUR (idSpectateur, nomSpectateur, prenomSpectateur, mdpSpectateur, numTelSpectateur, emailSpectateur) VALUES (1, 'Dupont', 'Jean', 'mdp123', '0612345678', 'jean.dupont@gmail.com');
INSERT INTO SPECTATEUR (idSpectateur, nomSpectateur, prenomSpectateur, mdpSpectateur, numTelSpectateur, emailSpectateur) VALUES (2, 'Martin', 'Pierre', 'mdp456', '0687654321', 'pierre.martin@gmail.com');
INSERT INTO SPECTATEUR (idSpectateur, nomSpectateur, prenomSpectateur, mdpSpectateur, numTelSpectateur, emailSpectateur) VALUES (3, 'Durant', 'Sophie', 'mdp789', '0698765432', 'sophie.durant@gmail.com');

INSERT INTO TYPE_BILLET (idBillet, nomBillet, caracteristiqueBillet, prixBillet, nbJoursBillet) VALUES (1, 'Billet 1 jour', 'Donne accès à l evenement pendant 1 jour', 10, 1);
INSERT INTO TYPE_BILLET (idBillet, nomBillet, caracteristiqueBillet, prixBillet, nbJoursBillet) VALUES (2, 'Billet VIP', 'Donne accès à l evenemnt pendant 3 jours', 25, 3);
INSERT INTO TYPE_BILLET (idBillet, nomBillet, caracteristiqueBillet, prixBillet, nbJoursBillet) VALUES (3, 'Billet Premium', 'Acces à l evenemnt pour 5 jours', 35, 5);

INSERT INTO EST_INSCRIT (idSpectateur, idBillet, dateInscription) VALUES (1, 1, '2023-10-21');
INSERT INTO EST_INSCRIT (idSpectateur, idBillet, dateInscription) VALUES (2, 2, '2023-10-21');
INSERT INTO EST_INSCRIT (idSpectateur, idBillet, dateInscription) VALUES (3, 3, '2023-10-21');

INSERT INTO TYPE_EVENEMENT (idTypeEvenement, nomTypeEvenement, caracteristiqueTypeEvenement,estGratuitTypeEvenement) VALUES (1, 'Concert', 'Événement musical',false);
INSERT INTO TYPE_EVENEMENT (idTypeEvenement, nomTypeEvenement, caracteristiqueTypeEvenement,estGratuitTypeEvenement) VALUES (2, 'Festival', 'Événement musical de grande envergure',false);
INSERT INTO TYPE_EVENEMENT (idTypeEvenement, nomTypeEvenement, caracteristiqueTypeEvenement,estGratuitTypeEvenement) VALUES (3, 'Spectacle', 'Événement artistique',true);

INSERT INTO LIEU (idLieu, nomLieu, adresse, capactiteLieu) VALUES (1, 'La Cigale', '12 Rue de Rochechouart, 75009 Paris',200);
INSERT INTO LIEU (idLieu, nomLieu, adresse, capactiteLieu) VALUES (2, 'Olympia', '28 Boulevard des Capucines, 75009 Paris',2000);
INSERT INTO LIEU (idLieu, nomLieu, adresse, capactiteLieu) VALUES (3, 'Zénith de Paris', '211 Avenue Jean Jaurès, 75019 Paris',20000);

INSERT INTO GROUPE (idGroupe, nomGroupe, descriptionGroupe, photoGroupe, lienReseauxGroupe, lienVideoGroupe) VALUES
(1, 'Indochine', 'Groupe de rock français', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Indochine_logo.svg/220px-Indochine_logo.svg.png', 'https://www.facebook.com/indochineofficiel', 'https://www.youtube.com/channel/UC-5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6'),
(2, 'Vianney', 'Auteur-compositeur-interprète français', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Vianney_2022.jpg/220px-Vianney_2022.jpg', 'https://www.facebook.com/vianneyofficiel', 'https://www.youtube.com/channel/UC-5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6'),
(3, 'louloucopter', 'Auteur français', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Vianney_2022.jpg/220px-Vianney_2022.jpg', 'https://www.facebook.com/vianneyofficiel', 'https://www.youtube.com/channel/UC-5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6Q5g73-c6');

INSERT INTO EVENEMENT (idEvenement,nomEvenement, dateEvenement, heureEvenement, dureeEvenement, dureeMontageEvenement, dureeDemontageEvenement, idGroupe, idTypeEvenement, idLieu)
VALUES (1, "nom 1",'2023-10-21', '2023-10-21 12:00:00', 120, 60, 60, 1, 1, 1);
INSERT INTO EVENEMENT (idEvenement, nomEvenement, dateEvenement, heureEvenement, dureeEvenement, dureeMontageEvenement, dureeDemontageEvenement, idGroupe, idTypeEvenement, idLieu)
VALUES (2, "nom2", '2023-10-22', '2023-10-22 14:00:00', 180, 90, 90, 2, 2, 2);
INSERT INTO EVENEMENT (idEvenement, nomEvenement, dateEvenement, heureEvenement, dureeEvenement, dureeMontageEvenement, dureeDemontageEvenement, idGroupe, idTypeEvenement, idLieu)
VALUES (3, "Nom 3", '2023-10-23', '2023-10-23 16:00:00', 240, 120, 120, 3, 3, 3);

INSERT INTO EST_FAVORIE (idSpectateur, idGroupe) VALUES
(1, 1),
(2, 2),
(3, 2);

INSERT INTO PRE_INSCRIT (idSpectateur, idEvenement) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO ARTISTE (idArtiste, nomArtiste)
VALUES (1,'Led Zeppelin'),
      (2,'The Beatles'),
      (3,'Pink Floyd'),
      (4,'The Rolling Stones'),
      (5,'Queen'),
      (6,'Michael Jackson'),
      (7,'Beyoncé'),
      (8,'Adele'),
      (9,'Ed Sheeran');

INSERT INTO FAIT_PARTIE (idGroupe, idArtiste) VALUES
(1, 1),
(2, 2);

INSERT INTO INSTRUMENT (idInstrument, nomInstrument, descriptionInstrument)
VALUES
(1, 'Guitare', 'Instrument à cordes pincées'),
(2, 'Piano', 'Instrument à clavier'),
(3, 'Batterie', 'Instrument à percussion'),
(4, 'Violon', 'Instrument à cordes frottées'),
(5, 'Saxophone', 'Instrument à vent'),
(6, 'Flûte', 'Instrument à vent'),
(7, 'Trombone', 'Instrument à vent'),
(8, 'Trompette', 'Instrument à vent'),
(9, 'Contrebasse', 'Instrument à cordes frottées');

INSERT INTO JOUE (idGroupe, idInstrument) VALUES
(1, 1),
(2, 2),
(1, 3);

INSERT INTO HEBERGEMENT (idHebergement, capacite, nomHebergement, descriptionHebergement)
VALUES
(1,2, 'Hôtel', 'Établissement offrant des chambres meublées à louer, généralement pour de courtes durées.'),
(2,4, 'Appartement', 'Logement indépendant situé dans un immeuble.'),
(3,6, 'Maison', 'Habitation individuelle.'),
(4,8, 'Camping', 'Terrain aménagé pour accueillir des campeurs.'),
(5,10, 'Gîte', 'Maison rurale meublée et équipée, louée à la semaine ou au mois.'),
(6,12, 'Chambre d hôtes', 'Chambre meublée chez un particulier, louée à la nuitée.'),
(7,14, 'Auberge de jeunesse', 'Établissement offrant des hébergements collectifs à bas prix.'),
(8,16, 'Village vacances', 'Ensemble de logements situés dans un même lieu, offrant des services et des animations.'),
(9,18, 'Résidence de tourisme', 'Ensemble de logements meublés et équipés, situés dans un même lieu, offrant des services hôteliers.');


INSERT INTO A_RESERVE (idGroupe, idHebergement, dateAReserve, dureeHebergement) VALUES
(1, 1, '2023-10-21', 2),
(2, 2, '2023-10-22', 3);

INSERT INTO TYPE_MUSIQUE (idTypeMusique, nomTypeMusique, caracteristiqueTypeMusique)
VALUES
(1, 'Rock', 'Musique caractérisée par des guitares électriques, des batteries et des basses.'),
(2, 'Pop', 'Musique populaire caractérisée par des mélodies simples et des paroles faciles à retenir.'),
(3, 'Classique', 'Musique caractérisée par des harmonies complexes et des instruments à cordes.'),
(4, 'Jazz', 'Musique caractérisée par des improvisations et des rythmes syncopés.'),
(5, 'Reggae', 'Musique caractérisée par des rythmes lents et des paroles engagées.'),
(6, 'Hip-hop', 'Musique caractérisée par des paroles rythmées et des samples.'),
(7, 'Electro', 'Musique caractérisée par des rythmes électroniques et des synthétiseurs.'),
(8, 'Rap', 'Musique caractérisée par des paroles rythmées et des rimes.'),
(9, 'Country', 'Musique caractérisée par des guitares acoustiques, des banjos et des mandolines.');

INSERT INTO CHANTE (idGroupe, idTypeMusique) VALUES
(1, 1),
(2, 2);

INSERT INTO PAIRE_MUSIQUE (musique1, musique2)
VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 1);