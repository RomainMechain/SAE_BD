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