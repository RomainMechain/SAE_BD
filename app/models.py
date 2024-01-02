from app import db
from typing import List, Optional

from sqlalchemy import Column, Date, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = db.Model
metadata = Base.metadata


class ARTISTE(Base):
    __tablename__ = 'ARTISTE'

    idArtiste = mapped_column(Integer, primary_key=True)
    nomArtiste = mapped_column(String(50))

    GROUPE: Mapped['GROUPE'] = relationship('GROUPE', secondary='FAIT_PARTIE', back_populates='ARTISTE_')


class GROUPE(Base):
    __tablename__ = 'GROUPE'

    idGroupe = mapped_column(Integer, primary_key=True)
    nomGroupe = mapped_column(String(50))
    descriptionGroupe = mapped_column(String(100))
    photoGroupe = mapped_column(String(500))
    lienReseauxGroupe = mapped_column(String(500))
    lienVideoGroupe = mapped_column(String(500))

    ARTISTE_: Mapped['ARTISTE'] = relationship('ARTISTE', secondary='FAIT_PARTIE', back_populates='GROUPE')
    TYPE_MUSIQUE: Mapped['TYPEMUSIQUE'] = relationship('TYPEMUSIQUE', secondary='CHANTE', back_populates='GROUPE_')
    SPECTATEUR: Mapped['SPECTATEUR'] = relationship('SPECTATEUR', secondary='EST_FAVORIE', back_populates='GROUPE_')
    INSTRUMENT: Mapped['INSTRUMENT'] = relationship('INSTRUMENT', secondary='JOUE', back_populates='GROUPE_')
    A_RESERVE: Mapped[List['ARESERVE']] = relationship('ARESERVE', uselist=True, back_populates='GROUPE_')
    EVENEMENT: Mapped[List['EVENEMENT']] = relationship('EVENEMENT', uselist=True, back_populates='GROUPE_')


class HEBERGEMENT(Base):
    __tablename__ = 'HEBERGEMENT'

    idHebergement = mapped_column(Integer, primary_key=True)
    capacite = mapped_column(Integer)
    nomHebergement = mapped_column(String(50))
    descriptionHebergement = mapped_column(String(200))

    A_RESERVE: Mapped[List['ARESERVE']] = relationship('ARESERVE', uselist=True, back_populates='HEBERGEMENT_')


class INSTRUMENT(Base):
    __tablename__ = 'INSTRUMENT'

    idInstrument = mapped_column(Integer, primary_key=True)
    nomInstrument = mapped_column(String(50))
    descriptionInstrument = mapped_column(String(200))

    GROUPE_: Mapped['GROUPE'] = relationship('GROUPE', secondary='JOUE', back_populates='INSTRUMENT')


class LIEU(Base):
    __tablename__ = 'LIEU'

    idLieu = mapped_column(Integer, primary_key=True)
    nomLieu = mapped_column(String(50))
    adresse = mapped_column(String(50))
    capactiteLieu = mapped_column(Integer)

    EVENEMENT: Mapped[List['EVENEMENT']] = relationship('EVENEMENT', uselist=True, back_populates='LIEU_')


class SPECTATEUR(Base):
    __tablename__ = 'SPECTATEUR'

    idSpectateur = mapped_column(Integer, primary_key=True)
    nomSpectateur = mapped_column(String(50))
    prenomSpectateur = mapped_column(String(50))
    mdpSpectateur = mapped_column(String(50))
    numTelSpectateur = mapped_column(String(50))
    emailSpectateur = mapped_column(String(50))

    GROUPE_: Mapped['GROUPE'] = relationship('GROUPE', secondary='EST_FAVORIE', back_populates='SPECTATEUR')
    EST_INSCRIT: Mapped[List['ESTINSCRIT']] = relationship('ESTINSCRIT', uselist=True, back_populates='SPECTATEUR_')
    EVENEMENT: Mapped['EVENEMENT'] = relationship('EVENEMENT', secondary='PRE_INSCRIT', back_populates='SPECTATEUR_')


class TYPEBILLET(Base):
    __tablename__ = 'TYPE_BILLET'

    idBillet = mapped_column(Integer, primary_key=True)
    nomBillet = mapped_column(String(50))
    caracteristiqueBillet = mapped_column(String(100))
    prixBillet = mapped_column(Integer)
    nbJoursBillet = mapped_column(Integer)

    EST_INSCRIT: Mapped[List['ESTINSCRIT']] = relationship('ESTINSCRIT', uselist=True, back_populates='TYPE_BILLET')


class TYPEEVENEMENT(Base):
    __tablename__ = 'TYPE_EVENEMENT'

    idTypeEvenement = mapped_column(Integer, primary_key=True)
    nomTypeEvenement = mapped_column(String(50))
    caracteristiqueTypeEvenement = mapped_column(String(100))
    estGratuitTypeEvenement = mapped_column(INTEGER(11))

    EVENEMENT: Mapped[List['EVENEMENT']] = relationship('EVENEMENT', uselist=True, back_populates='TYPE_EVENEMENT')


class TYPEMUSIQUE(Base):
    __tablename__ = 'TYPE_MUSIQUE'

    idTypeMusique = mapped_column(Integer, primary_key=True)
    nomTypeMusique = mapped_column(String(50))
    caracteristiqueTypeMusique = mapped_column(String(200))

    GROUPE_: Mapped['GROUPE'] = relationship('GROUPE', secondary='CHANTE', back_populates='TYPE_MUSIQUE')
    TYPE_MUSIQUE: Mapped['TYPEMUSIQUE'] = relationship('TYPEMUSIQUE', secondary='PAIRE_MUSIQUE', primaryjoin=lambda: TYPEMUSIQUE.idTypeMusique == t_PAIRE_MUSIQUE.c.musique1, secondaryjoin=lambda: TYPEMUSIQUE.idTypeMusique == t_PAIRE_MUSIQUE.c.musique2, back_populates='TYPE_MUSIQUE_')
    TYPE_MUSIQUE_: Mapped['TYPEMUSIQUE'] = relationship('TYPEMUSIQUE', secondary='PAIRE_MUSIQUE', primaryjoin=lambda: TYPEMUSIQUE.idTypeMusique == t_PAIRE_MUSIQUE.c.musique2, secondaryjoin=lambda: TYPEMUSIQUE.idTypeMusique == t_PAIRE_MUSIQUE.c.musique1, back_populates='TYPE_MUSIQUE')


class ARESERVE(Base):
    __tablename__ = 'A_RESERVE'
    __table_args__ = (
        ForeignKeyConstraint(['idGroupe'], ['GROUPE.idGroupe'], name='FKaReserve_Groupe'),
        ForeignKeyConstraint(['idHebergement'], ['HEBERGEMENT.idHebergement'], name='FKaReserve_Hebergement'),
        Index('FKaReserve_Hebergement', 'idHebergement')
    )

    idGroupe = mapped_column(Integer, primary_key=True, nullable=False)
    idHebergement = mapped_column(Integer, primary_key=True, nullable=False)
    dateAReserve = mapped_column(Date, primary_key=True, nullable=False)
    dureeHebergement = mapped_column(Integer)

    GROUPE_: Mapped['GROUPE'] = relationship('GROUPE', back_populates='A_RESERVE')
    HEBERGEMENT_: Mapped['HEBERGEMENT'] = relationship('HEBERGEMENT', back_populates='A_RESERVE')


t_CHANTE = Table(
    'CHANTE', metadata,
    Column('idGroupe', Integer, primary_key=True, nullable=False),
    Column('idTypeMusique', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['idGroupe'], ['GROUPE.idGroupe'], name='FKchante_Groupe'),
    ForeignKeyConstraint(['idTypeMusique'], ['TYPE_MUSIQUE.idTypeMusique'], name='FKchante_TypeMusique'),
    Index('FKchante_TypeMusique', 'idTypeMusique')
)


t_EST_FAVORIE = Table(
    'EST_FAVORIE', metadata,
    Column('idSpectateur', Integer, primary_key=True, nullable=False),
    Column('idGroupe', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['idGroupe'], ['GROUPE.idGroupe'], name='FKestFavorie_groupe'),
    ForeignKeyConstraint(['idSpectateur'], ['SPECTATEUR.idSpectateur'], name='FKestFavorie_spectateur'),
    Index('FKestFavorie_groupe', 'idGroupe')
)


class ESTINSCRIT(Base):
    __tablename__ = 'EST_INSCRIT'
    __table_args__ = (
        ForeignKeyConstraint(['idBillet'], ['TYPE_BILLET.idBillet'], name='FKest_inscrit_type_billet'),
        ForeignKeyConstraint(['idSpectateur'], ['SPECTATEUR.idSpectateur'], name='FKest_inscrit_spectateur'),
        Index('FKest_inscrit_type_billet', 'idBillet')
    )

    idSpectateur = mapped_column(Integer, primary_key=True, nullable=False)
    idBillet = mapped_column(Integer, primary_key=True, nullable=False)
    dateInscription = mapped_column(Date)

    TYPE_BILLET: Mapped['TYPEBILLET'] = relationship('TYPEBILLET', back_populates='EST_INSCRIT')
    SPECTATEUR_: Mapped['SPECTATEUR'] = relationship('SPECTATEUR', back_populates='EST_INSCRIT')


class EVENEMENT(Base):
    __tablename__ = 'EVENEMENT'
    __table_args__ = (
        ForeignKeyConstraint(['idGroupe'], ['GROUPE.idGroupe'], name='FKevenement_groupe'),
        ForeignKeyConstraint(['idLieu'], ['LIEU.idLieu'], name='FKevenement_lieu'),
        ForeignKeyConstraint(['idTypeEvenement'], ['TYPE_EVENEMENT.idTypeEvenement'], name='FKevenement_typeEvenement'),
        Index('FKevenement_groupe', 'idGroupe'),
        Index('FKevenement_lieu', 'idLieu'),
        Index('FKevenement_typeEvenement', 'idTypeEvenement')
    )

    idEvenement = mapped_column(Integer, primary_key=True)
    nomEvenement = mapped_column(String(50))
    dateEvenement = mapped_column(Date)
    heureEvenement = mapped_column(Date)
    dureeEvenement = mapped_column(Integer)
    dureeMontageEvenement = mapped_column(Integer)
    dureeDemontageEvenement = mapped_column(Integer)
    idGroupe = mapped_column(Integer)
    idTypeEvenement = mapped_column(Integer)
    idLieu = mapped_column(Integer)

    GROUPE_: Mapped[Optional['GROUPE']] = relationship('GROUPE', back_populates='EVENEMENT')
    LIEU_: Mapped[Optional['LIEU']] = relationship('LIEU', back_populates='EVENEMENT')
    TYPE_EVENEMENT: Mapped[Optional['TYPEEVENEMENT']] = relationship('TYPEEVENEMENT', back_populates='EVENEMENT')
    SPECTATEUR_: Mapped['SPECTATEUR'] = relationship('SPECTATEUR', secondary='PRE_INSCRIT', back_populates='EVENEMENT')


t_FAIT_PARTIE = Table(
    'FAIT_PARTIE', metadata,
    Column('idGroupe', Integer, primary_key=True, nullable=False),
    Column('idArtiste', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['idArtiste'], ['ARTISTE.idArtiste'], name='FKfaitPartie_artiste'),
    ForeignKeyConstraint(['idGroupe'], ['GROUPE.idGroupe'], name='FKfaitPartie_groupe'),
    Index('FKfaitPartie_artiste', 'idArtiste')
)


t_JOUE = Table(
    'JOUE', metadata,
    Column('idGroupe', Integer, primary_key=True, nullable=False),
    Column('idInstrument', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['idGroupe'], ['GROUPE.idGroupe'], name='FKjoue_groupe'),
    ForeignKeyConstraint(['idInstrument'], ['INSTRUMENT.idInstrument'], name='FKjoue_instrument'),
    Index('FKjoue_instrument', 'idInstrument')
)


t_PAIRE_MUSIQUE = Table(
    'PAIRE_MUSIQUE', metadata,
    Column('musique1', Integer, primary_key=True, nullable=False),
    Column('musique2', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['musique1'], ['TYPE_MUSIQUE.idTypeMusique'], name='FKmusique1_typeMusique'),
    ForeignKeyConstraint(['musique2'], ['TYPE_MUSIQUE.idTypeMusique'], name='FKmusique2_typeMusique'),
    Index('FKmusique2_typeMusique', 'musique2')
)


t_PRE_INSCRIT = Table(
    'PRE_INSCRIT', metadata,
    Column('idSpectateur', Integer, primary_key=True, nullable=False),
    Column('idEvenement', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['idEvenement'], ['EVENEMENT.idEvenement'], name='FKpreInscrit_Evenement'),
    ForeignKeyConstraint(['idSpectateur'], ['SPECTATEUR.idSpectateur'], name='FKpreInscrit_spectateur'),
    Index('FKpreInscrit_Evenement', 'idEvenement')
)