drop table PAIRE_MUSIQUE;
drop table CHANTE;
drop table TYPE_MUSIQUE;
drop table A_RESERVE;
drop table HEBERGEMENT;
drop table JOUE;
drop table INSTRUMENT;
drop table FAIT_PARTIE;
drop table ARTISTE;
drop table PRE_INSCRIT;
drop table EST_FAVORIE;
drop table EVENEMENT;
drop table GROUPE;
drop table LIEU;
drop table TYPE_EVENEMENT;
drop table EST_INSCRIT;
drop table TYPE_BILLET;
drop table UTILISATEUR;
drop table TYPE_UTILISATEUR;


create table TYPE_UTILISATEUR (
    idTypeUtilisateur int(10),
    nomTypeUtilisateur varchar(50),
    constraint PKtype_utilisateur PRIMARY KEY (idTypeUtilisateur)
);

create table UTILISATEUR (
    idUtilisateur int(10),
    nomUtilisateur varchar(50),
    prenomUtilisateur varchar(50),
    mdpUtilisateur varchar(50),
    numTelUtilisateur varchar(50),
    emailUtilisateur varchar(50),
    idTypeUtilisateur int(10),
    constraint PKUtilisateur PRIMARY KEY (idUtilisateur),
    constraint FKUtilisateur_type_utilisateur FOREIGN KEY (idTypeUtilisateur) references TYPE_UTILISATEUR(idTypeUtilisateur)
);

create table TYPE_BILLET (
    idBillet int(10),
    nomBillet varchar(50),
    caracteristiqueBillet varchar(100),
    prixBillet int(10),
    nbJoursBillet int(10),
    constraint PKtype_billet PRIMARY KEY (idBillet)
);

create table EST_INSCRIT (
    idUtilisateur int(10),
    idBillet int(10),
    dateInscription date,
    constraint PKest_inscrit PRIMARY KEY (idUtilisateur, idBillet),
    constraint FKest_inscrit_Utilisateur FOREIGN KEY (idUtilisateur) references UTILISATEUR(idUtilisateur),
    constraint FKest_inscrit_type_billet FOREIGN KEY (idBillet) references TYPE_BILLET(idBillet)
);

create table TYPE_EVENEMENT (
    idTypeEvenement int(10),
    nomTypeEvenement varchar(50),
    caracteristiqueTypeEvenement varchar(100),
    estGratuitTypeEvenement boolean,
    constraint PKtype_evenement PRIMARY KEY (idTypeEvenement)
);

create table LIEU (
    idLieu int(10),
    nomLieu varchar(50),
    adresse varchar(50),
    capactiteLieu int(10),
    constraint PKlieu PRIMARY KEY (idLieu)
);

create table GROUPE (
    idGroupe int(10),
    nomGroupe varchar(50),
    descriptionGroupe varchar(100),
    photoGroupe varchar(500),
    lienReseauxGroupe varchar(500),
    lienVideoGroupe varchar(500),
    constraint PKgroupe PRIMARY KEY (idGroupe)
);

create table EVENEMENT (
    idEvenement int(10),
    nomEvenement varchar(50),
    dateEvenement date,
    heureEvenement date,
    dureeEvenement int(10),
    dureeMontageEvenement int(10),
    dureeDemontageEvenement int(10),
    idGroupe int(10),
    idTypeEvenement int(10),
    idLieu int(10),
    constraint PKevenement PRIMARY KEY (idEvenement),
    constraint FKevenement_groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe),
    constraint FKevenement_typeEvenement FOREIGN KEY (idTypeEvenement) references TYPE_EVENEMENT(idTypeEvenement),
    constraint FKevenement_lieu FOREIGN KEY (idLieu) references LIEU(idLieu)
);

create table EST_FAVORIE (
    idUtilisateur int(10),
    idGroupe int(10),
    constraint PKestFavorie PRIMARY KEY (idUtilisateur, idGroupe),
    constraint FKestFavorie_Utilisateur FOREIGN KEY (idUtilisateur) references UTILISATEUR(idUtilisateur),
    constraint FKestFavorie_groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe)
);

create table PRE_INSCRIT (
    idUtilisateur int(10),
    idEvenement int(10),
    constraint PKpreInscrit PRIMARY KEY (idUtilisateur,idEvenement),
    constraint FKpreInscrit_Utilisateur FOREIGN KEY (idUtilisateur) references UTILISATEUR(idUtilisateur),
    constraint FKpreInscrit_Evenement FOREIGN KEY (idEvenement) references EVENEMENT(idEvenement)
); 

create table ARTISTE (
    idArtiste int(10),
    nomArtiste varchar(50),
    constraint PKartiste PRIMARY KEY (idArtiste)
);

create table FAIT_PARTIE (
    idGroupe int(10),
    idArtiste int(10),
    constraint PKfaitParte PRIMARY KEY (idGroupe, idArtiste),
    constraint FKfaitPartie_groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe),
    constraint FKfaitPartie_artiste FOREIGN KEY (idArtiste) references ARTISTE(idArtiste)
);

create table INSTRUMENT (
    idInstrument int(10) PRIMARY KEY,
    nomInstrument varchar(50),
    descriptionInstrument varchar(200)
);

create table JOUE(
    idGroupe int(10),
    idInstrument int(10),
    constraint PKjoue PRIMARY KEY (idGroupe,idInstrument),
    constraint FKjoue_groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe),
    constraint FKjoue_instrument FOREIGN KEY (idInstrument) references INSTRUMENT(idInstrument)
);

create table HEBERGEMENT(
    idHebergement int(10),
    capacite int(10),
    nomHebergement varchar(50),
    descriptionHebergement varchar(200),
    constraint PKhebergement PRIMARY KEY (idHebergement)
);

create table A_RESERVE(
    idGroupe int(10),
    idHebergement int(10),
    dateAReserve date,
    dureeHebergement int(10),
    constraint PKaReserve PRIMARY KEY (idGroupe, idHebergement, dateAReserve),
    constraint FKaReserve_Groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe),
    constraint FKaReserve_Hebergement FOREIGN KEY (idHebergement) references HEBERGEMENT(idHebergement)
);

create table TYPE_MUSIQUE(
    idTypeMusique int(10),
    nomTypeMusique varchar(50),
    caracteristiqueTypeMusique varchar(200),
    constraint PKtypeMusique PRIMARY KEY (idTypeMusique)
);

create table CHANTE(
    idGroupe int(10),
    idTypeMusique int(10),
    constraint PKchante PRIMARY KEY (idGroupe,idTypeMusique),
    constraint FKchante_Groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe),
    constraint FKchante_TypeMusique FOREIGN KEY (idTypeMusique) references TYPE_MUSIQUE(idTypeMusique)
);

create table PAIRE_MUSIQUE(
    musique1 int(10),
    musique2 int(10),
    constraint PKmusique PRIMARY KEY (musique1,musique2),
    constraint FKmusique1_typeMusique FOREIGN KEY (musique1) references TYPE_MUSIQUE(idTypeMusique),
    constraint FKmusique2_typeMusique FOREIGN KEY (musique2) references TYPE_MUSIQUE(idTypeMusique)
);

DROP FUNCTION getNbArtisteGroupe;
DROP FUNCTION getNomTypeEvenement;
DROP FUNCTION EvenementEstGratuit;
DROP FUNCTION aBilletDate;

DELIMITER |

-- Fonction qui permet de récupérer le nombre d'artiste d'un groupe
create function getNbArtisteGroupe(idG int(10)) returns int(10) 
READS SQL DATA
DETERMINISTIC
begin
    declare nbArtiste int(10);
    select count(*) into nbArtiste from FAIT_PARTIE where idGroupe = idG;
    return nbArtiste;
end|
DELIMITER ;

DELIMITER |

-- Fonction qui permet de récupérer le nom d'un type d'événement en fonction de son id
CREATE function getNomTypeEvenement(idE int(10)) returns varchar(50)
READS SQL DATA
DETERMINISTIC
begin
    declare nomTypeE varchar(50);
    select nomTypeEvenement into nomTypeE from TYPE_EVENEMENT natural join EVENEMENT where idTypeEvenement = idE;
    return nomTypeE;
end|

DELIMITER ;

DELIMITER |

-- Fonction qui permet de récupérer si un événement est gratuit ou non en fonction de son id

CREATE Function EvenementEstGratuit(idE int(10)) returns boolean
READS SQL DATA
DETERMINISTIC
begin
    declare estG boolean;
    select estGratuitTypeEvenement into estG from TYPE_EVENEMENT natural join EVENEMENT where idEvenement = idE;
    return estG;
end|

DELIMITER ;

DELIMITER |

-- Fonction qui indique si un Utilisateur a déjà un billet pour une date donnée
CREATE function aBilletDate(idS int(10), dateE date) returns boolean
READS SQL DATA
DETERMINISTIC
BEGIN
    declare idB int(10);
    declare dateB date;
    declare nbJoursB int(10);
    declare fini boolean default false;
    declare lesBillets cursor for 
        select idBillet, dateInscription from EST_INSCRIT where idUtilisateur = idS;
    declare continue handler for not found set fini = true;
    open lesBillets;
    while not fini do
        fetch lesBillets into idB, dateB;
        if not fini then
            SELECT nbJoursBillet into nbJoursB from TYPE_BILLET where idBillet = idB;
            if dateE BETWEEN dateB AND DATE_ADD(dateB, INTERVAL nbJoursB DAY) then
                return true;
            end if;
        end if;
    end while;
    close lesBillets;
    return false;
end|

DELIMITER ;
DELIMITER |

-- Trigger qui permet de vérifier que le nombre d'artiste est inférieur à la capacité de l'hébergement
create trigger maxCapacite BEFORE INSERT ON A_RESERVE for each row
begin
    declare nbArtiste int(10);
    declare capa int(10);
    select getNbArtisteGroupe(new.idGroupe) into nbArtiste;
    select capacite into capa from HEBERGEMENT where idHebergement = new.idHebergement;
    if (nbArtiste > capa) then
        signal sqlstate '45000' set message_text = 'Le nombre d''artiste est supérieur à la capacité de l''hébergement';
    end if;
end|

DELIMITER ;

DELIMITER |

-- Trigger qui permet de ne pas vendre plus de billet en pré-inscirption qu'il n'y a de place dans le lieu de l'événement
create trigger maxCapaciteLieu BEFORE INSERT ON PRE_INSCRIT for each row
begin
    declare capa int(10);
    declare nbPreInscris int(10);
    select capactiteLieu into capa from LIEU natural join EVENEMENT where idEvenement = new.idEvenement;
    select count(idUtilisateur) into nbPreInscris from PRE_INSCRIT where idEvenement = new.idEvenement;
    if (nbPreInscris >= capa) then
        signal sqlstate '45000' set message_text = 'Le nombre d Utilisateur se préinscrivant à cet événement est supérieur à la capacité du lieu';
    end if;
end|
DELIMITER ;

DELIMITER |

-- Trigger qui permet de vérifier qu'il n'y a pas de conflit de date entre deux réservations
CREATE trigger conflitDateReservation BEFORE INSERT ON A_RESERVE for each row
begin 
    declare nombreReservation int(10);
    SELECT COUNT(*) INTO nombreReservation
    FROM A_RESERVE
    WHERE idHebergement = NEW.idHebergement
    AND (
        (NEW.dateAReserve BETWEEN dateAReserve AND DATE_ADD(dateAReserve, INTERVAL dureeHebergement DAY))
        OR (DATE_ADD(NEW.dateAReserve, INTERVAL NEW.dureeHebergement DAY) BETWEEN dateAReserve AND DATE_ADD(dateAReserve, INTERVAL dureeHebergement DAY))
    );
    if nombreReservation > 0 then
        signal sqlstate '45000' set message_text = 'Il y a un conflit de date avec une autre réservation';
    end if;
end|

DELIMITER ;

DELIMITER |

-- trigger qui verifie que l Utilisateur peut s'inscrire à un événement, soit il est gratuit soit il a un billet pour cette date
CREATE Trigger inscriptionEvenement BEFORE INSERT ON PRE_INSCRIT for each row
begin 
    DECLARE evnementGratuit boolean;
    DECLARE dateE date;
    select EvenementEstGratuit(new.idEvenement) into evnementGratuit;
    SELECT dateEvenement into dateE from EVENEMENT where idEvenement = new.idEvenement;
    if (evnementGratuit = false) then
        if (aBilletDate(new.idUtilisateur, dateE) = false) then
            signal sqlstate '45000' set message_text = 'L Utilisateur n''a pas de billet pour cette date';
        end if;
    end if;
end|

CREATE TRIGGER conflitDateGroupeEvenement BEFORE INSERT ON EVENEMENT FOR EACH ROW
BEGIN
    DECLARE finEvenement DATE;
    DECLARE nombreErreur INT;

    SET finEvenement = DATE_ADD(NEW.dateEvenement, INTERVAL NEW.dureeEvenement MINUTE);

    SELECT COUNT(idEvenement) INTO nombreErreur FROM EVENEMENT e WHERE idGroupe = NEW.idGroupe
    AND (
        (NEW.dateEvenement BETWEEN e.dateEvenement AND DATE_ADD(e.dateEvenement, INTERVAL e.dureeEvenement MINUTE))
        OR (NEW.dateEvenement BETWEEN e.dateEvenement AND DATE_ADD(e.dateEvenement, INTERVAL e.dureeEvenement MINUTE))
    );
    
    IF nombreErreur > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ce groupe participe déjà à un événement se chevauchant dans le temps';
    END IF;
END|

DELIMITER ;