insert into HEBERGEMENT values (1, 1, 'rock', 'Hébergement pour les groupes de rock');
insert into ARTISTE values (1, 'Muse');
insert into ARTISTE values (2, 'Coldplay');
insert into GROUPE values (1, 'Groupe1', 'Groupe de rock', "photo", "lien", "lien");
insert into GROUPE values (2, 'Groupe2', 'Groupe de rock', "photo", "lien", "lien");
insert into GROUPE VALUES (3, 'Groupe3', 'Groupe de rock', "photo", "lien", "lien");
insert into FAIT_PARTIE values (1, 1);
insert into FAIT_PARTIE values (1, 2);
insert into A_RESERVE values (1, 1, '2019-01-01', 5); -- Declanche le trigger maxCapaciteHebergement
insert into A_RESERVE values (2, 1, '2019-01-03', 5);
insert into A_RESERVE values (3, 1, '2019-01-05', 5); -- Declanche le trigger conflitDateReservation
insert into LIEU values(1,"Lieu 1","3 rue de l'algérie",0);
insert into LIEU values(2,"Lieu 2","3 rue de l'algérie",79);
insert into TYPE_EVENEMENT values(1,"type 1","Type 1", false);
insert into EVENEMENT values(1,'2023-10-21','2023-10-21 12:00:00',100,100,100,1,1,1);
insert into EVENEMENT values(2,'2023-11-21','2023-11-21 12:00:00',100,100,100,1,1,2);
INSERT INTO SPECTATEUR VALUES (1, 'Dupont', 'Jean', 'mdp123', '0612345678', 'jean.dupont@gmail.com');
insert into PRE_INSCRIT values(1,1); -- Declanche le trigger maxCapaciteLieu
insert into PRE_INSCRIT values(1,2); -- Declanche le trigger inscriptionEvenement
insert into EVENEMENT values(3,"2023-10-21",'2023-10-21 12:00:00',100,100,100,1,1,1) -- Declanche le trigger conflitDateGroupeEvenement
