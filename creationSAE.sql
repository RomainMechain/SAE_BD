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
    constraint PKtype_evenement PRIMARY KEY (idTypeEvenement)
);

create table LIEU (
    idLieu int(10),
    nomLieu varchar(50),
    adresse varchar(50),
    constraint PKlieu PRIMARY KEY (idLieu)
);

create table GROUPE (
    idGroupe int(10),
    nomGroupe varchar(50),
    descriptionGroupe varchar(100),
    photoGroupe varchar(100),
    lienReseauxGroupe varchar(100),
    lienVideoGroupe varchar(100),
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
    descriptionInstrument varchar2 (1000),
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
    nomInstrumentHebergement varchar(50),
    descriptionHebergement varchar2(1000),
    constraint PKhebergement PRIMARY KEY (idHebergement)
);

create table A_RESERVE(
    idArtiste int(10),
    idHebergement int(10),
    dateAReserve date,
    dureeHebergement int(10),
    constraint PKaReserve PRIMARY KEY (idArtiste, idHebergement),
    constraint FKaReserve_Artiste FOREIGN KEY (idArtiste) references ARTISTE(idArtiste),
    constraint FKaReserve_Hebergement FOREIGN KEY (idHebergement) references HEBERGEMENT(idHebergement)
);

create table TYPE_MUSIQUE(
    idTypeMusique int(10),
    nomTypeMusique varchar(50),
    caracteristiqueTypeMusique varchar(200),
    constraint PKtypeMusique PRIMARY KEY idTypeMusique,
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