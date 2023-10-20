INSERT INTO SPECTATEUR (idSpectateur, nomSpectateur, prenomSpectateur, mdpSpectateur, numTelSpectateur, emailSpectateur)
VALUES
(1, 'John Doe', 'John', 'password123', '0123456789', 'john.doe@example.com'),
(2, 'Jane Doe', 'Jane', 'password456', '9876543210', 'jane.doe@example.com');

INSERT INTO TYPE_BILLET (idBillet, nomBillet, caracteristiqueBillet, prixBillet)
VALUES
(1, 'Billet standard', 'Billet pour accéder à l événement', 10),
(2, 'Billet VIP', 'Billet pour accéder à l événement avec des avantages supplémentaires', 20);

INSERT INTO EST_INSCRIT (idSpectateur, idBillet, dateInscription)
VALUES
(1, 1, '2023-10-20'),
(2, 2, '2023-10-20');

INSERT INTO TYPE_EVENEMENT (idTypeEvenement, nomTypeEvenement, caracteristiqueTypeEvenement)
VALUES
(1, 'Concert', 'Événement musical'),
(2, 'Festival', 'Événement musical de grande envergure');

INSERT INTO LIEU (idLieu, nomLieu, adresse)
VALUES
(1, 'Salle de concert', '123 Main Street'),
(2, 'Parc des expositions', '456 Elm Street');

INSERT INTO GROUPE (idGroupe, nomGroupe, descriptionGroupe, photoGroupe, lienReseauxGroupe, lienVideoGroupe)
VALUES
(1, 'AC/DC', 'Groupe de rock australien', 'https://example.com/acdc.jpg', 'https://example.com/acdc-reseaux-sociaux', 'https://example.com/acdc-video');

INSERT INTO EVENEMENT (idEvenement, dateEvenement, heureEvenement, dureeEvenement, dureeMontageEvenement, dureeDemontageEvenement, idGroupe, idTypeEvenement, idLieu)
VALUES
(1, '2023-11-04', '20:00:00', 120, 60, 30, 1, 1, 1);

INSERT INTO EST_FAVORIE (idSpectateur, idGroupe)
VALUES
(1, 1),
(2, 1);

INSERT INTO PRE_INSCRIT (idSpectateur, idEvenement)
VALUES
(1, 1),
(2, 1);

INSERT INTO ARTISTE (idArtiste, nomArtiste)
VALUES
(1, 'Angus Young'),
(2, 'Brian Johnson');

INSERT INTO FAIT_PARTIE (idGroupe, idArtiste)
VALUES
(1, 1),
(1, 2);

INSERT INTO INSTRUMENT (idInstrument, nomInstrument, descriptionInstrument)
VALUES
(1, 'Guitare électrique', 'Instrument à cordes pincées'),
(2, 'Batterie', 'Instrument de percussion'),
(3, 'Basse électrique', 'Instrument à cordes frottées');

INSERT INTO JOUE (idGroupe, idInstrument)
VALUES
(1, 1),
(1, 2),
(1, 3);

INSERT INTO HEBERGEMENT (idHebergement, nomHebergementHebergement, descriptionHebergement)
VALUES
(1, 'Hôtel Ibis', 'Hôtel 3 étoiles situé à proximité de la salle de concert'),
(2, 'Hôtel Mercure', 'Hôtel 4 étoiles situé dans le centre-ville');

INSERT INTO A_RESERVE (idArtiste, idHebergement, dateAReserve, dureeHebergement)
VALUES
(1, 1, '2023-11-03', 2),
(2, 2, '2023-11-03', 2);

INSERT INTO TYPE_MUSIQUE (idTypeMusique, nomTypeMusique, caracteristiqueTypeMusique)
VALUES
(1, 'Rock', 'Genre de musique populaire caractérisé par un rythme soutenu et des guitares électriques'),
(2, 'Pop', 'Genre de musique populaire caractérisée par des mélodies simples et accrocheuses');