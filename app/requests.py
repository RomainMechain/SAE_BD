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
    user = session.query(SPECTATEUR).filter(SPECTATEUR.emailSpectateur==email).first()
    session.close()
    return user

def email_exists(email) :
    """Retourne True si l'email existe dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    user = session.query(SPECTATEUR).filter(SPECTATEUR.emailSpectateur==email).first()
    session.close()
    return user != None

def add_user(nom, prenom, email, mdp, telephone) :
    """Ajoute un utilisateur dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    id = session.query(SPECTATEUR).count() + 1
    user = SPECTATEUR(idSpectateur=id, nomSpectateur=nom, prenomSpectateur=prenom, emailSpectateur=email, mdpSpectateur=mdp, numTelSpectateur=telephone)
    session.add(user)
    session.commit()
    session.close()
    print("Utilisateur ajouté")