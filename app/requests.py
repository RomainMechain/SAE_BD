from app import db
from app.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from datetime import datetime
from unidecode import unidecode
from pytz import timezone

def add_instrument(nom, description) :
    """Ajoute un instrument dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    id = session.query(INSTRUMENT).count() + 1
    instrument = INSTRUMENT(nomInstrument=nom, descriptionInstrument=description, idInstrument=id)
    session.add(instrument)
    session.commit()
    session.close()
    print("Instrument ajouté")

def get_all_instruments() :
    """Retourne tous les instruments de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    instruments = session.query(INSTRUMENT).all()
    session.close()
    return instruments

def get_user_by_email(email) :
    """Retourne l'utilisateur correspondant à l'email
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    user = session.query(UTILISATEUR).filter(UTILISATEUR.emailUtilisateur==email).first()
    session.close()
    return user

def email_exists(email) :
    """Retourne True si l'email existe dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    user = session.query(UTILISATEUR).filter(UTILISATEUR.emailUtilisateur==email).first()
    session.close()
    return user != None

def add_user(nom, prenom, email, mdp, telephone) :
    """Ajoute un utilisateur dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    id = session.query(UTILISATEUR).count() + 1
    user = UTILISATEUR(idUtilisateur=id, nomUtilisateur=nom, prenomUtilisateur=prenom, emailUtilisateur=email, mdpUtilisateur=mdp, numTelUtilisateur=telephone, idTypeUtilisateur=1)
    session.add(user)
    session.commit()
    session.close()
    print("Utilisateur ajouté")

def add_user_type(id, nom) :
    """Ajoute un type d'utilisateur dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    type = TYPEUTILISATEUR(idTypeUtilisateur=id, nomTypeUtilisateur=nom)
    session.add(type)
    session.commit()
    session.close()
    print("Type d'utilisateur ajouté")

def initialise_user_type() :
    """Initialise le type de tous les utilisateurs à "Membre"
    """
    add_user_type(1, "Membre")
    add_user_type(2, "Administrateur")
    add_user_type(3, "Participant")

def get_user_by_id(id) :
    """Retourne l'utilisateur correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    user = session.query(UTILISATEUR).filter(UTILISATEUR.idUtilisateur==id).first()
    session.close()
    return user

def get_all_event() :
    """Retourne tous les évènements de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    events = session.query(EVENEMENT).all()
    session.close()
    return events

def get_all_type_event() :
    """Retourne tous les types d'évènements de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    types = session.query(TYPEEVENEMENT).all()
    session.close()
    return types

def get_event_by_type(id) :
    """Retourne tous les évènements du type id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    events = session.query(EVENEMENT).filter(EVENEMENT.idTypeEvenement==id).all()
    session.close()
    return events

def order_events(lst_events) :
    """Retourne les évènements de la liste lst_events triés par date croissante
    """
    return sorted(lst_events, key=lambda event: event.heureEvenement)

def get_event_by_name(name) :
    """Retourne tous les évènements dont le nom contient name
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    events = session.query(EVENEMENT).filter(EVENEMENT.nomEvenement.ilike("%" + name + "%")).all()
    session.close()
    return events

def create_dico_event(id_event) :
    """Retourne un dictionnaire avec les informations necessaire pour l'affichage de la page d'un evenement
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    event = session.query(EVENEMENT).filter(EVENEMENT.idEvenement==id_event).first()
    type_evenement = session.query(TYPEEVENEMENT).filter(TYPEEVENEMENT.idTypeEvenement==event.idTypeEvenement).first()
    lieu = session.query(LIEU).filter(LIEU.idLieu==event.idLieu).first()
    groupe = session.query(GROUPE).filter(GROUPE.idGroupe==event.idGroupe).first()
    dico = {}
    dico["event"] = event
    dico["type_evenement"] = type_evenement
    dico["lieu"] = lieu
    dico["groupe"] = groupe
    return dico

def get_instrument_by_groupe(id_groupe) :
    """Retourne tous les instruments du groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    all_instruments = session.query(t_JOUE).filter_by(idGroupe=id_groupe).all()
    instruments = []
    for instrument in all_instruments :
        instruments.append(session.query(INSTRUMENT).filter_by(idInstrument=instrument.idInstrument).first())
    session.close()
    return instruments

def get_artiste_by_groupe(id_groupe) :
    """Retourne tous les artistes du groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    all_artistes = session.query(t_FAIT_PARTIE).filter_by(idGroupe=id_groupe).all()
    artistes = []
    for artiste in all_artistes :
        artistes.append(session.query(ARTISTE).filter_by(idArtiste=artiste.idArtiste).first())
    session.close()
    return artistes

def get_type_musique_by_groupe(id_groupe) :
    """Retourne tous les types de musique du groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    all_types = session.query(t_CHANTE).filter_by(idGroupe=id_groupe).all()
    types = []
    for type in all_types :
        types.append(session.query(TYPEMUSIQUE).filter_by(idTypeMusique=type.idTypeMusique).first())
    session.close()
    return types

def create_dico_groupe(id_groupe) :
    """Retourne un dictionnaire avec les informations necessaire pour l'affichage de la page d'un groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    groupe = session.query(GROUPE).filter(GROUPE.idGroupe==id_groupe).first()
    instruments = get_instrument_by_groupe(id_groupe)
    artistes = get_artiste_by_groupe(id_groupe)
    types_musique = get_type_musique_by_groupe(id_groupe)
    evenements = session.query(EVENEMENT).filter(EVENEMENT.idGroupe==id_groupe).all()
    dico = {}
    dico["groupe"] = groupe
    dico["instruments"] = instruments
    dico["artistes"] = artistes
    dico["types_musique"] = types_musique
    dico["evenements"] = evenements
    return dico

def groupe_is_favori(id_groupe, id_utilisateur) :
    """Retourne True si le groupe id_groupe est un favori de l'utilisateur id_utilisateur
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    favori = session.query(t_EST_FAVORIE).filter_by(idGroupe=id_groupe, idUtilisateur=id_utilisateur).first()
    session.close()
    return favori != None

def add_favori_db(id_groupe, id_utilisateur) :
    """Ajoute le groupe id_groupe aux favoris de l'utilisateur id_utilisateur
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_EST_FAVORIE.insert().values(idGroupe=id_groupe, idUtilisateur=id_utilisateur))
    session.commit()
    session.close()

def remove_favori_db(id_groupe, id_utilisateur) :
    """Retire le groupe id_groupe des favoris de l'utilisateur id_utilisateur
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_EST_FAVORIE.delete().where(t_EST_FAVORIE.c.idGroupe==id_groupe).where(t_EST_FAVORIE.c.idUtilisateur==id_utilisateur))
    session.commit()
    session.close()

def get_artiste_by_id(id_artiste) :
    """Retourne l'artiste correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    artiste = session.query(ARTISTE).filter(ARTISTE.idArtiste==id_artiste).first()
    session.close()
    return artiste