from app import db
from app.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError

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

def get_paire_musique(id_type_musique) :
    """Retourne une paire de musique correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    all_paires = session.query(t_PAIRE_MUSIQUE).filter_by(musique1=id_type_musique).all()
    paires = []
    for paire in all_paires :
        paires.append(session.query(TYPEMUSIQUE).filter_by(idTypeMusique=paire.musique2).first())
    session.close()
    return paires

def get_groupe_by_type_musique(id_type_musique) :
    """Retourne tous les groupes qui font de la musique du type id_type_musique
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    all_groupes = session.query(t_CHANTE).filter_by(idTypeMusique=id_type_musique).all()
    groupes = []
    for groupe in all_groupes :
        groupes.append(session.query(GROUPE).filter_by(idGroupe=groupe.idGroupe).first())
    session.close()
    return groupes

def get_type_musique_by_id(id_type_musique) :
    """Retourne le type de musique correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    type_musique = session.query(TYPEMUSIQUE).filter(TYPEMUSIQUE.idTypeMusique==id_type_musique).first()
    session.close()
    return type_musique

def get_lieu_by_id(id_lieu) :
    """Retourne le lieu correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    lieu = session.query(LIEU).filter(LIEU.idLieu==id_lieu).first()
    session.close()
    return lieu

def get_event_by_lieu(id_lieu) :
    """Retourne tous les évènements qui ont lieu au lieu id_lieu
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    events = session.query(EVENEMENT).filter(EVENEMENT.idLieu==id_lieu).all()
    session.close()
    return order_events(events)

def get_all_type_billet() :
    """Retourne tous les types de billets de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    types = session.query(TYPEBILLET).all()
    session.close()
    return types

def get_unique_event_days():
    """Retourne tous les jours uniques où il y a un événement
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    unique_days = session.query(func.date(EVENEMENT.heureEvenement)).all()
    unique_days = sorted(list(set(unique_days)))
    session.close()
    return [day[0] for day in unique_days]

def get_billet_by_id(id_billet) :
    """Retourne le billet correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    billet = session.query(TYPEBILLET).filter(TYPEBILLET.idBillet==id_billet).first()
    session.close()
    return billet

def buy_ticket(id_billet, id_utilisateur, date) :
    """Ajoute un billet à l'utilisateur id_utilisateur pour l'évènement id_billet
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    date = datetime.strptime(date, "%Y-%m-%d").date()
    achat = ESTINSCRIT(idBillet=id_billet, idUtilisateur=id_utilisateur, dateInscription=date)
    try:
        session.add(achat)
        session.commit()
        return True
    except SQLAlchemyError:
        session.rollback()
        return False
    finally:
        session.close()

def get_nb_pre_inscrits(id_event) :
    """Retourne le nombre de pré-inscrits à l'évènement id_event
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    nb_pre_inscrits = session.query(t_PRE_INSCRIT).filter(t_PRE_INSCRIT.c.idEvenement==id_event).count()
    session.close()
    return nb_pre_inscrits

def  est_pre_inscrit(id_event, id_utilisateur) :
    """Retourne True si l'utilisateur id_utilisateur est pré-inscrit à l'évènement id_event
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    pre_inscrit = session.query(t_PRE_INSCRIT).filter(t_PRE_INSCRIT.c.idEvenement==id_event).filter(t_PRE_INSCRIT.c.idUtilisateur==id_utilisateur).first()
    session.close()
    return pre_inscrit != None

def get_inscription_by_utilisateur(id_utilisateur) :
    """Retourne toutes les inscriptions de l'utilisateur id_utilisateur
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    inscriptions = session.query(ESTINSCRIT).filter(ESTINSCRIT.idUtilisateur==id_utilisateur).all()
    session.close()
    return inscriptions

def inscrit_pour_date(id_utilisateur, date) :
    """return True si l'utilisateur id_utilisateur a un billet valide la date date
    """
    inscriptions = get_inscription_by_utilisateur(id_utilisateur)
    for inscription in inscriptions :
        billet = get_billet_by_id(inscription.idBillet)
        # Convertit date en objet datetime.date
        date = date.date()
        # Vérifie si la date est comprise entre dateInscription et dateInscription + nbJoursBillet
        if inscription.dateInscription <= date <= (inscription.dateInscription + timedelta(days=billet.nbJoursBillet)):
            return True
    return False

def pre_inscription_possible(id_event, id_utilisateur):
    """Retourne True si l'utilisateur id_utilisateur peut se pré-inscrire à l'évènement dico_event
    """
    dico_event = create_dico_event(id_event)
    if get_nb_pre_inscrits(dico_event["event"].idEvenement) >= dico_event["lieu"].capactiteLieu :
        return False
    else :
        if dico_event["type_evenement"].estGratuitTypeEvenement :
            return True
        if inscrit_pour_date(id_utilisateur, dico_event["event"].heureEvenement) :
            return True
    return False

def pre_inscription_db(id_event, id_utilisateur) :
    """Ajoute une pré-inscription à l'utilisateur id_utilisateur pour l'évènement id_event
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_PRE_INSCRIT.insert().values(idEvenement=id_event, idUtilisateur=id_utilisateur))
    session.commit()
    session.close()
    print("Pré-inscription ajoutée")

def remove_pre_inscription_db(id_event, id_utilisateur) :
    """Retire la pré-inscription de l'utilisateur id_utilisateur pour l'évènement id_event
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_PRE_INSCRIT.delete().where(t_PRE_INSCRIT.c.idEvenement==id_event).where(t_PRE_INSCRIT.c.idUtilisateur==id_utilisateur))
    session.commit()
    session.close()
    print("Pré-inscription retirée")

def get_all_groupe() :
    """Retourne tous les groupes de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    groupes = session.query(GROUPE).all()
    session.close()
    return groupes

def get_groupe_by_nom(nom) :
    """Retourne tous les groupes dont le nom contient nom
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    groupes = session.query(GROUPE).filter(GROUPE.nomGroupe.ilike("%" + nom + "%")).all()
    session.close()
    return groupes

def get_groupe_favori(groupes,id_user) :
    """Retourne tous les groupes favoris de l'utilisateur id_user
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    groupes_favoris = []
    for groupe in groupes :
        if groupe_is_favori(groupe.idGroupe, id_user) :
            groupes_favoris.append(groupe)
    session.close()
    return groupes_favoris

def is_admin(id_user) :
    """Retourne True si l'utilisateur id_user est un administrateur
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    user = session.query(UTILISATEUR).filter(UTILISATEUR.idUtilisateur==id_user).first()
    session.close()
    return user.idTypeUtilisateur == 2

def add_artiste_bd(nom, description, photo) :
    """Ajoute un artiste dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    id = session.query(ARTISTE).count() + 1
    artiste = ARTISTE(idArtiste=id, nomArtiste=nom, descriptionArtiste=description, photoArtiste=photo)
    session.add(artiste)
    session.commit()
    session.close()
    return id

def get_all_lieu() :
    """Retourne tous les lieux de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    lieux = session.query(LIEU).all()
    session.close()
    return lieux

def get_datetime_debut_fin(date, duree, dureeMontage, dureeDemontage) : 
    date_debut = date - timedelta(hours=float(dureeMontage))
    date_fin = date + timedelta(hours=float(duree)) + timedelta(hours=float(dureeDemontage))
    print(date_debut, date_fin)
    return (date_debut, date_fin)

def get_datetime_debut_fin_by_evenement(id_event) :
    """Retourne un tuple avec la date de début et la date de fin de l'évènement id_event
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    event = session.query(EVENEMENT).filter(EVENEMENT.idEvenement==id_event).first()
    date = event.heureEvenement
    duree = event.dureeEvenement
    dureeMontage = event.dureeMontageEvenement
    dureeDemontage = event.dureeDemontageEvenement
    session.close()
    return get_datetime_debut_fin(date, duree, dureeMontage, dureeDemontage)

def get_event_by_lieu(id_lieu) :
    """Retourne tous les évènements qui ont lieu au lieu id_lieu
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    events = session.query(EVENEMENT).filter(EVENEMENT.idLieu==id_lieu).all()
    session.close()
    return order_events(events)

def is_enclosed(startA, endA, startB, endB):
    print("ENCLOSE", startA >= startB and endA <= endB)
    return startA >= startB and endA <= endB

def is_overlapping(startA, endA, startB, endB):
    print("OVERLAP", startA < endB and endA > startB)
    return startA < endB and endA > startB

def is_date_ok_for_lieu(date, duree, dureeMontage, dureeDemontage, id_lieu) :
    """Retourne True si la date est disponible pour le lieu id_lieu
    """
    date_debut, date_fin = get_datetime_debut_fin(date, duree, dureeMontage, dureeDemontage)
    events = get_event_by_lieu(id_lieu)
    for event in events :
        event_debut, event_fin = get_datetime_debut_fin_by_evenement(event.idEvenement)
        if is_overlapping(date_debut, date_fin, event_debut, event_fin) or is_overlapping(event_debut, event_fin, date_debut, date_fin) or is_enclosed(date_debut, date_fin, event_debut, event_fin) :
            return False
    return True

def get_event_by_groupe(id_groupe) :
    """Retourne tous les évènements du groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    events = session.query(EVENEMENT).filter(EVENEMENT.idGroupe==id_groupe).all()
    session.close()
    return order_events(events)

def is_date_ok_for_groupe(date, duree, dureeMontage, dureeDemontage, id_groupe) :
    """Retourne True si la date est disponible pour le groupe id_groupe
    """
    date_debut, date_fin = get_datetime_debut_fin(date, duree, dureeMontage, dureeDemontage)
    events = get_event_by_groupe(id_groupe)
    for event in events :
        event_debut, event_fin = get_datetime_debut_fin_by_evenement(event.idEvenement)
        if is_overlapping(date_debut, date_fin, event_debut, event_fin) or is_overlapping(event_debut, event_fin, date_debut, date_fin) or is_enclosed(date_debut, date_fin, event_debut, event_fin) :
            return False
    return True

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def add_event_db(nom, date, duree, dureeMontage, dureeDemontage, id_groupe, id_lieu, id_type_event) :
    """Ajoute un évènement dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    id = session.query(EVENEMENT).count() + 1
    event = EVENEMENT(idEvenement=id, nomEvenement=nom, heureEvenement=date, dureeEvenement=duree, dureeMontageEvenement=dureeMontage, dureeDemontageEvenement=dureeDemontage, idGroupe=id_groupe, idLieu=id_lieu, idTypeEvenement=id_type_event)
    session.add(event)
    session.commit()
    session.close()
    print("Evènement ajouté")
    return id

def get_all_artiste() :
    """Retourne tous les artistes de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    artistes = session.query(ARTISTE).all()
    session.close()
    return artistes

def get_all_type_musique() :
    """Retourne tous les types de musique de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    types_musique = session.query(TYPEMUSIQUE).all()
    session.close()
    return types_musique

def get_all_instrument() :
    """Retourne tous les instruments de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    instruments = session.query(INSTRUMENT).all()
    session.close()
    return instruments

def add_groupe_db(nom, description, lienReseaux, lienVideo, photo, artistes, instruments, types_musique) :
    """Ajoute un groupe dans la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    id = session.query(GROUPE).count() + 1
    groupe = GROUPE(idGroupe=id, nomGroupe=nom, descriptionGroupe=description, lienReseauxGroupe=lienReseaux, lienVideoGroupe=lienVideo, photoGroupe=photo)
    session.add(groupe)
    session.commit()
    session.close()
    print("Groupe ajouté")
    for artiste in artistes :
        add_artiste_groupe_db(id, artiste)
    for instrument in instruments :
        add_instrument_groupe_db(id, instrument)
    for type_musique in types_musique :
        add_type_musique_groupe_db(id, type_musique)
    return id

def add_artiste_groupe_db(id_groupe, id_artiste) :
    """Ajoute un artiste au groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_FAIT_PARTIE.insert().values(idGroupe=id_groupe, idArtiste=id_artiste))
    session.commit()
    session.close()
    print("Artiste ajouté au groupe")

def add_instrument_groupe_db(id_groupe, id_instrument) :
    """Ajoute un instrument au groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_JOUE.insert().values(idGroupe=id_groupe, idInstrument=id_instrument))
    session.commit()
    session.close()
    print("Instrument ajouté au groupe")

def add_type_musique_groupe_db(id_groupe, id_type_musique) :
    """Ajoute un type de musique au groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_CHANTE.insert().values(idGroupe=id_groupe, idTypeMusique=id_type_musique))
    session.commit()
    session.close()
    print("Type de musique ajouté au groupe")

def get_all_hebergement() :
    """Retourne tous les hébergements de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    hebergements = session.query(HEBERGEMENT).all()
    session.close()
    return hebergements

def get_groupe_by_id(id_groupe) :
    """Retourne le groupe correspondant à l'id
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    groupe = session.query(GROUPE).filter(GROUPE.idGroupe==id_groupe).first()
    session.close()
    return groupe

def create_dico_hebergement():
    Session = sessionmaker(bind=db.engine)
    session = Session()
    reservations = session.query(ARESERVE).all()
    res = {}
    for reservation in reservations:
        if reservation.idGroupe not in res:
            res[reservation.idGroupe] = []
        res[reservation.idGroupe].append({
            'nomHebergement': reservation.idHebergement, 
            'dateAReserve': reservation.dateAReserve,
            'dureeHebergement': reservation.dureeHebergement  
        })

    return res

def create_liste_hebergement(id_groupe):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = []
    reservations = session.query(ARESERVE).filter(ARESERVE.idGroupe==id_groupe).all()
    for reservation in reservations:
        res.append({
            'nomHebergement': session.query(HEBERGEMENT).filter(HEBERGEMENT.idHebergement==reservation.idHebergement).first().nomHebergement, 
            'dateAReserve': reservation.dateAReserve,
            'dureeHebergement': reservation.dureeHebergement  
        })
    return res

def is_date_ok_for_hebergement_groupe(date, duree, id_groupe) :
    """Retourne True si le groupe n'est pas déjà réservé à la date date pour une durée de duree jours
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    date_debut = date
    date_fin = date + timedelta(days=duree)
    reservations = session.query(ARESERVE).filter(ARESERVE.idGroupe==id_groupe).all()
    for reservation in reservations :
        if reservation.dateAReserve <= date_debut <= (reservation.dateAReserve + timedelta(days=reservation.dureeHebergement)) or reservation.dateAReserve <= date_fin <= (reservation.dateAReserve + timedelta(days=reservation.dureeHebergement)) :
            return False
    return True

def add_hebergement_db(id_hebergement, date, duree, id_groupe) :
    """Ajoute un hébergement pour le groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    areserve = ARESERVE(idHebergement=id_hebergement, idGroupe=id_groupe, dateAReserve=date, dureeHebergement=duree)
    session.add(areserve)
    session.commit()
    session.close()

def get_nb_artiste_by_groupe(id_groupe) :
    """Retourne le nombre d'artistes du groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    nb_artiste = session.query(t_FAIT_PARTIE).filter(t_FAIT_PARTIE.c.idGroupe==id_groupe).count()
    session.close()
    return nb_artiste

def get_groupe_areserver(id_hebergement,date) :
    """Retourne les groupes qui ont reservé l'hebergement id_hebergement à la date date
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    groupes = []
    reservations = session.query(ARESERVE).filter(ARESERVE.idHebergement==id_hebergement).filter(ARESERVE.dateAReserve==date).all()
    for reservation in reservations :
        groupes.append(session.query(GROUPE).filter(GROUPE.idGroupe==reservation.idGroupe).first())
    session.close()
    return groupes

def is_ok_capacite_hebergement_date(date, id_hebergement, id_groupe) :
    """Retourne True si l'hebergement id_hebergement a une capacité suffisante pour le groupe id_groupe
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    nb_artiste = get_nb_artiste_by_groupe(id_groupe)
    hebergement = session.query(HEBERGEMENT).filter(HEBERGEMENT.idHebergement==id_hebergement).first()
    nb_place = hebergement.capacite
    reservations = session.query(ARESERVE).filter(ARESERVE.idHebergement==id_hebergement).filter(ARESERVE.dateAReserve==date).all()
    for reservation in reservations :
        nb_place -= get_nb_artiste_by_groupe(reservation.idGroupe)
    session.close()
    return nb_place >= nb_artiste

def is_ok_capacite_hebergement(date, duree, idHebergement, id_groupe) :
    """Retourne True si l'hebergement id_hebergement a une capacité suffisante pour le groupe id_groupe pendant la durée duree
    """
    for i in range(duree) :
        if not is_ok_capacite_hebergement_date(date + timedelta(days=i), idHebergement, id_groupe) :
            return False
    return True

def get_liste_billet(id_utilisateur) :
    """Retourne la liste des billets de l'utilisateur id_utilisateur
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    res = []
    inscriptions = session.query(ESTINSCRIT).filter(ESTINSCRIT.idUtilisateur==id_utilisateur).all()
    for inscription in inscriptions :
        res.append({
            'nomBillet' : session.query(TYPEBILLET).filter(TYPEBILLET.idBillet==inscription.idBillet).first().nomBillet,
            'dateInscription' : inscription.dateInscription,
        })
    session.close()
    return res

def delete_artiste_bd(id_artiste):
    """supprime l'artise de la base de données
    """
    Session = sessionmaker(bind=db.engine)
    session = Session()
    session.execute(t_FAIT_PARTIE.delete().where(t_FAIT_PARTIE.c.idArtiste==id_artiste))
    artiste = session.query(ARTISTE).filter(ARTISTE.idArtiste == id_artiste).first()
    if artiste:
        session.delete(artiste)
    session.commit()
    session.close()