from app import app, db
from app.models import *
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.requests import add_user_type
from flask_bcrypt import generate_password_hash
import csv

@app.cli.command('init_database')
def init_database():
    """Initialise la base de données avec les données des fichiers CSV
    """    
    
    db.create_all()
    Session = sessionmaker(bind=db.engine)
    session = Session()

    # Ajout des types d'utilisateurs
    with open('app/static/CSV/type_utilisateur.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            add_user_type(row[0], row[1])

    # Ajout des utilisateurs
    with open('app/static/CSV/utilisateur.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            password = generate_password_hash(row[3]).decode('utf-8')
            user = UTILISATEUR(idUtilisateur=row[0], nomUtilisateur=row[1], prenomUtilisateur=row[2], emailUtilisateur=row[5], mdpUtilisateur=password, numTelUtilisateur=row[4], idTypeUtilisateur=row[6])
            db.session.add(user)
            print("Utilisateur ajouté : " + row[1] + " " + row[2])
    db.session.commit()

    # Ajout des lieux
    with open('app/static/CSV/lieu.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            lieu = LIEU(idLieu=row[0], nomLieu=row[1], adresse=row[2], capactiteLieu=row[3])
            db.session.add(lieu)
            print("Lieu ajouté : " + row[1])
    db.session.commit()

    # Ajout des types d'événements
    with open('app/static/CSV/type_evenement.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            type_event = TYPEEVENEMENT(idTypeEvenement=row[0], nomTypeEvenement=row[1], caracteristiqueTypeEvenement=row[2], estGratuitTypeEvenement=row[3], preInscription=row[4])
            db.session.add(type_event)
            print("Type d'événement ajouté : " + row[1])
    db.session.commit()

    # Ajout des types de billets
    with open('app/static/CSV/type_billet.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            type_ticket = TYPEBILLET(idBillet=row[0], nomBillet=row[1], caracteristiqueBillet=row[2], prixBillet=row[3], nbJoursBillet=row[4])
            db.session.add(type_ticket)
            print("Type de billet ajouté : " + row[1])
    db.session.commit()

    # Ajout des instruments
    with open('app/static/CSV/instrument.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            instrument = INSTRUMENT(idInstrument=row[0], nomInstrument=row[1], descriptionInstrument=row[2])
            db.session.add(instrument)
            print("Instrument ajouté : " + row[1])
    db.session.commit()

    # Ajout des artistes
    with open('app/static/CSV/artiste.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            artist = ARTISTE(idArtiste=row[0], nomArtiste=row[1], descriptionArtiste=row[2], photoArtiste=bytes(row[3], 'utf-8'))
            db.session.add(artist)
            print("Artiste ajouté : " + row[1])
    db.session.commit()

    # Ajout des types de musique
    with open('app/static/CSV/type_musique.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            type_music = TYPEMUSIQUE(idTypeMusique=row[0], nomTypeMusique=row[1], caracteristiqueTypeMusique=row[2])
            db.session.add(type_music)
            print("Type de musique ajouté : " + row[1])
    db.session.commit()

    # Ajout des hébérgements
    with open('app/static/CSV/hebergement.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            hebergement = HEBERGEMENT(idHebergement=row[0], nomHebergement=row[1], descriptionHebergement=row[2], capacite=row[3])
            db.session.add(hebergement)
            print("Hébergement ajouté : " + row[1])
    db.session.commit()

    # Ajouts des groupes
    with open('app/static/CSV/groupe.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            group = GROUPE(idGroupe=row[0], nomGroupe=row[1], descriptionGroupe=row[2], photoGroupe=bytes(row[3], 'utf-8'), lienReseauxGroupe=row[4], lienVideoGroupe=row[5])
            db.session.add(group)
            print("Groupe ajouté : " + row[1])
    db.session.commit()

    # Ajout des événements
    with open('app/static/CSV/evenement.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:    
            date = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')        
            event = EVENEMENT(idEvenement=row[0], nomEvenement=row[1], heureEvenement=date, dureeEvenement=row[3], dureeMontageEvenement=row[4], dureeDemontageEvenement=row[5], idGroupe=row[6], idTypeEvenement=row[7], idLieu=row[8])
            db.session.add(event)
            print("Événement ajouté : " + row[1])
    db.session.commit()

    # Ajout table est_inscrit
    with open('app/static/CSV/est_inscrit.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:    
            date = datetime.strptime(row[2], '%Y-%m-%d')
            est_inscrit = ESTINSCRIT(idUtilisateur=row[0], idBillet=row[1], dateInscription=date)
            db.session.add(est_inscrit)
            print("Inscription ajoutée : " + row[0] + " - " + row[1])
    db.session.commit()

    # Ajout table a_reserve
    with open('app/static/CSV/a_reserve.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:    
            date = datetime.strptime(row[2], '%Y-%m-%d')
            a_reserve = ARESERVE(idGroupe=row[0], idHebergement=row[1], dateAReserve=date, dureeHebergement=row[3])
            db.session.add(a_reserve)
            print("Réservation ajoutée : " + row[0] + " - " + row[1])
    db.session.commit()

    # Ajout des paires de musique
    with open('app/static/CSV/paire_musique.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            session.execute(t_PAIRE_MUSIQUE.insert().values(musique1=row[0], musique2=row[1]))
            print("Paire de musique ajoutée : " + row[0] + " - " + row[1])
            session.commit()

    # Ajout des favories 
    with open('app/static/CSV/est_favorie.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            session.execute(t_EST_FAVORIE.insert().values(idUtilisateur=row[0], idGroupe=row[1]))
            print("Favori ajouté : " + row[0] + " - " + row[1])
            session.commit()

    # Ajout table Joue
    with open('app/static/CSV/joue.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            session.execute(t_JOUE.insert().values(idGroupe=row[0], idInstrument=row[1]))
            print("Joue ajouté : " + row[0] + " - " + row[1])
            session.commit()

    # Ajout table fait_partie
    with open('app/static/CSV/fait_partie.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            session.execute(t_FAIT_PARTIE.insert().values(idGroupe=row[0], idArtiste=row[1]))
            print("Fait partie ajouté : " + row[0] + " - " + row[1])
            session.commit()

    # Ajout table chante
    with open('app/static/CSV/chante.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            session.execute(t_CHANTE.insert().values(idGroupe=row[0], idTypeMusique=row[1]))
            print("Chante ajouté : " + row[0] + " - " + row[1])
            session.commit()

    # Ajout table pre_inscrit
    with open('app/static/CSV/pre_inscrit.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            session.execute(t_PRE_INSCRIT.insert().values(idUtilisateur=row[0], idEvenement=row[1]))
            print("Pré-inscrit ajouté : " + row[0] + " - " + row[1])
            session.commit()