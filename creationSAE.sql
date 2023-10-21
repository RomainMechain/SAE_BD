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
drop table SPECTATEUR;

create table SPECTATEUR (
    idSpectateur int(10),
    nomSpectateur varchar(50),
    prenomSpectateur varchar(50),
    mdpSpectateur varchar(50),
    numTelSpectateur varchar(50),
    emailSpectateur varchar(50),
    constraint PKspectateur PRIMARY KEY (idSpectateur)
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
    idSpectateur int(10),
    idBillet int(10),
    dateInscription date,
    constraint PKest_inscrit PRIMARY KEY (idSpectateur, idBillet),
    constraint FKest_inscrit_spectateur FOREIGN KEY (idSpectateur) references SPECTATEUR(idSpectateur),
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
    photoGroupe varchar(200),
    lienReseauxGroupe varchar(200),
    lienVideoGroupe varchar(200),
    constraint PKgroupe PRIMARY KEY (idGroupe)
);

create table EVENEMENT (
    idEvenement int(10),
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
    idSpectateur int(10),
    idGroupe int(10),
    constraint PKestFavorie PRIMARY KEY (idSpectateur, idGroupe),
    constraint FKestFavorie_spectateur FOREIGN KEY (idSpectateur) references SPECTATEUR(idSpectateur),
    constraint FKestFavorie_groupe FOREIGN KEY (idGroupe) references GROUPE(idGroupe)
);

create table PRE_INSCRIT (
    idSpectateur int(10),
    idEvenement int(10),
    constraint PKpreInscrit PRIMARY KEY (idSpectateur,idEvenement),
    constraint FKpreInscrit_spectateur FOREIGN KEY (idSpectateur) references SPECTATEUR(idSpectateur),
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
    constraint PKaReserve PRIMARY KEY (idGroupe, idHebergement),
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
    declare nomTypeEvenement varchar(50);
    select nomTypeEvenement into nomTypeEvenement from TYPE_EVENEMENT where idTypeEvenement = idE;
    return nomTypeEvenement;
end|

DELIMITER ;

DELIMITER |

-- Fonction qui permet de récupérer si un événement est gratuit ou non en fonction de son id

CREATE Function EvenementEstGratuit(idE int(10)) returns boolean
READS SQL DATA
DETERMINISTIC
begin
    declare estG boolean;
    select estGratuit into estG from EVENEMENT where idEvenement = idE;
    return estG;
end|

DELIMITER ;

DELIMITER |

-- Fonction qui indique si un spectateur a déjà un billet pour une date donnée
CREATE function aBilletDate(idS int(10), dateE date) returns boolean
READS SQL DATA
DETERMINISTIC
BEGIN
    declare idB int(10);
    declare dateB date;
    declare nbJoursB int(10);
    declare fini boolean default false;
    declare lesBillets cursor for 
        select idBillet, dateInscription from EST_INSCRIT where idSpectateur = idS;
    declare continue handler for not found set fini = true;
    open lesBillets;
    while not fini do
        fetch lesBillets into idB;
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
    select count(idSpectateur) into nbPreInscris from PRE_INSCRIT where idEvenement = new.idEvenement;
    if (nbPreInscris >= capa) then
        signal sqlstate '45000' set message_text = 'Le nombre de spectateur se préinscrivant à cet événement est supérieur à la capacité du lieu';
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
