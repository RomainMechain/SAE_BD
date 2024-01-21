from app import app
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from flask_bcrypt import generate_password_hash, check_password_hash
from app.requests import *
from app.forms import *
from app import *
import base64

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

@app.route('/')
@login_required
def home():
    return render_template('home.html', type_user=current_user.idTypeUtilisateur)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    form = LoginForm()
    user = get_user_by_email(form.mail.data)
    if form.validate_on_submit():
        if user :
            if check_password_hash(user.mdpUtilisateur, form.mdp.data):
                login_user(user, remember=True)
                print(current_user.idTypeUtilisateur)
                return redirect(url_for('home'))
    return render_template('login.html', form=form, login=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register page"""
    form = RegisterForm()
    if form.validate_on_submit():
        if not email_exists(form.mail.data):
            password = generate_password_hash(form.mdp.data).decode('utf-8')
            add_user(form.nom.data, form.prenom.data, form.mail.data, password, form.telephone.data)
            return redirect(url_for('login'))
        else :
            print("Email déjà utilisé")
            return render_template('register.html', form=form, email_exist=True)
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def intersection(liste1, liste2) :
    if len(liste1) == 0 or len(liste2) == 0 :
        return liste1 + liste2
    else :
        res = []
        for event1 in liste1 :
            for event2 in liste2 :
                if event1.idEvenement == event2.idEvenement :
                    res.append(event1)
                    break
    return res 
            

@app.route('/search_event', methods=['GET', 'POST'])
@login_required
def search_event() :
    if request.method == 'POST' :
        id_type = request.form.get('id_type', None)
        search_term = request.form.get('search_term', None)
        return redirect(url_for('search_event', id_type=id_type, search_term=search_term))
    else :
        id_type = request.args.get('id_type')
        search_term = request.args.get('search_term')
        events_type = []
        events_name = []
        if id_type and id_type != "all" :
            events_type = get_event_by_type(id_type)
            print(events_type)
        if search_term :
            events_name = get_event_by_name(search_term)
            print(events_name)
        
        events = intersection(events_type, events_name)

        if (not id_type or id_type == "all") and not search_term :
            events = get_all_event()
        events = order_events(events)
        return render_template('search_event.html', events=events, types=get_all_type_event(), int=int, admin=is_admin(current_user.idTypeUtilisateur))

@app.route('/event', methods=['GET', 'POST'])
@login_required
def event() :
    dico_event = create_dico_event(request.args.get('id_event'))
    nb_pre_inscrit = get_nb_pre_inscrits(request.args.get('id_event'))
    pre_inscrit = est_pre_inscrit(request.args.get('id_event'), current_user.idUtilisateur)
    return render_template('event.html', dico_event=dico_event, int=int, nb_pre_inscrit=nb_pre_inscrit, pre_inscrit=pre_inscrit, admin=is_admin(current_user.idTypeUtilisateur))

@app.route('/groupe', methods=['GET', 'POST'])
@login_required
def groupe() :
    dico_groupe = create_dico_groupe(request.args.get('id_groupe'))
    return render_template('groupe.html', dico_groupe=dico_groupe, admin=is_admin(current_user.idTypeUtilisateur),int=int, est_favorie=groupe_is_favori(request.args.get('id_groupe'), current_user.idUtilisateur))

@app.route('/add_favori', methods=['GET', 'POST'])
@login_required
def add_favori() :
    add_favori_db(request.args.get('id_groupe'), current_user.idUtilisateur)
    return redirect(url_for('groupe', id_groupe=request.args.get('id_groupe'), admin = is_admin(current_user.idTypeUtilisateur)))

@app.route('/remove_favori', methods=['GET', 'POST'])
@login_required
def remove_favori() :
    remove_favori_db(request.args.get('id_groupe'), current_user.idUtilisateur)
    return redirect(url_for('groupe', id_groupe=request.args.get('id_groupe'), admin = is_admin(current_user.idTypeUtilisateur)))

@app.route('/artiste', methods=['GET', 'POST'])
@login_required
def artiste() :
    artiste = get_artiste_by_id(request.args.get('id_artiste'))
    return render_template('artiste.html', artiste=artiste)

@app.route('/type_musique', methods=['GET', 'POST'])
@login_required
def type_musique() :
    type_musique = get_type_musique_by_id(request.args.get('id_type_musique'))
    types_musique = get_paire_musique(request.args.get('id_type_musique'))
    groupes = get_groupe_by_type_musique(request.args.get('id_type_musique'))
    return render_template('type_musique.html', type_musique=type_musique, types_musique=types_musique, groupes=groupes)

@app.route('/lieu/<id_lieu>', methods=['GET', 'POST'])
@login_required
def lieu(id_lieu):
    lieu = get_lieu_by_id(id_lieu)
    events = get_event_by_lieu(id_lieu)
    return render_template('lieu.html', lieu=lieu, events=events, int=int)

@app.route('/search_ticket', methods=['GET', 'POST'])
@login_required
def search_ticket() :
    types_billet = get_all_type_billet()
    return render_template('search_ticket.html', types_billet=types_billet)

@app.route('/ticket', methods=['GET', 'POST'])
@login_required
def ticket() :
    billet = get_billet_by_id(request.args.get('id_billet'))
    dates = get_unique_event_days()
    return render_template('ticket.html', billet=billet, dates=dates)

@app.route('/add_billet', methods=['GET', 'POST'])
@login_required
def add_billet() :
    json = request.get_json()
    if (buy_ticket(json['id_billet'], current_user.idUtilisateur, json['date'])) :
        return jsonify(success=True, redirect_url=url_for('search_ticket'))
    else :
        return jsonify(success=False, message='Vous avez déjà une réservation à cette date',  redirect_url=url_for('ticket', id_billet=json['id_billet']))
    
@app.route('/pre_inscription', methods=['GET', 'POST'])
@login_required
def pre_inscription() :
    id_evevnement = request.args.get('id_evenement')
    if pre_inscription_possible(id_evevnement, current_user.idUtilisateur) :
        pre_inscription_db(id_evevnement, current_user.idUtilisateur)
        return redirect(url_for('event', id_event=id_evevnement))
    return redirect(url_for('search_ticket'))

@app.route('/remove_pre_inscription', methods=['GET', 'POST'])
@login_required
def remove_pre_inscription() :
    id_evevnement = request.args.get('id_evenement')
    remove_pre_inscription_db(id_evevnement, current_user.idUtilisateur)
    return redirect(url_for('event', id_event=id_evevnement))

@app.route('/search_groupe', methods=['GET', 'POST'])
@login_required
def search_groupe() :
    if request.method == 'POST' :
        search_term = request.form.get('search_term', None)
        favori = request.form.get('favori', None)
        return redirect(url_for('search_groupe', search_term=search_term, favori=favori))
    else :
        search_term = request.args.get('search_term')
        favori = request.args.get('favori')
        groupes = get_all_groupe()
        if search_term :
            groupes = get_groupe_by_nom(search_term)
        if favori == 'true':
            print(favori)
            groupes = get_groupe_favori(groupes, current_user.idUtilisateur)
        return render_template('search_groupe.html', groupes=groupes, admin=is_admin(current_user.idTypeUtilisateur))
    
@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil() :
    user = get_user_by_id(current_user.idUtilisateur)
    return render_template('profil.html', user=user)

@app.route('/add_artiste', methods=['GET', 'POST'])
@login_required
def add_artiste() :
    form = addArtisteForm()
    if form.validate_on_submit():
        encoded_photo = base64.b64encode(form.photo.data.read())
        id_artiste = add_artiste_bd(form.nom.data, form.description.data, encoded_photo)
        return redirect(url_for('artiste', id_artiste=id_artiste))
    return render_template('add_artiste.html', form=form)

@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event() :
    form = addEventForm(get_all_groupe(), get_all_lieu(), get_all_type_event())
    if form.validate_on_submit():
        date_object = datetime.strptime(form.date.data, "%Y-%m-%dT%H:%M")
        if not is_float(form.duree.data) or not is_float(form.dureeMontage.data) or not is_float(form.dureeDemontage.data) :
            return render_template('add_event.html', form=form, datetime=datetime, erreur="il faut mettre un nombre pour les durées")
        if not is_date_ok_for_lieu(date_object, form.duree.data,  form.dureeMontage.data, form.dureeDemontage.data, form.lieu.data) :
            return render_template('add_event.html', form=form, datetime=datetime, erreur="le lieu n'est pas disponible à cette date")
        if not is_date_ok_for_groupe(date_object, form.duree.data,  form.dureeMontage.data, form.dureeDemontage.data, form.groupe.data) :
            return render_template('add_event.html', form=form, datetime=datetime, erreur="le groupe n'est pas disponible à cette date")
        id = add_event_db(form.nom.data, date_object, form.duree.data, form.dureeMontage.data, form.dureeDemontage.data, form.groupe.data, form.lieu.data, form.type_event.data)
        return redirect(url_for('event', id_event=id))
    return render_template('add_event.html', form=form, datetime=datetime)


@app.route('/add_groupe', methods=['GET', 'POST'])
@login_required
def add_groupe() :
    form = AddGroupForm(get_all_artiste(), get_all_instrument(), get_all_type_musique())
    if form.validate_on_submit():
        encoded_photo = base64.b64encode(form.photo.data.read())
        id_groupe = add_groupe_db(form.nom.data, form.description.data, form.lienReseaux.data, form.lienVideo.data, encoded_photo, form.artistes.data, form.instruments.data, form.types_musique.data)
        return redirect(url_for('groupe', id_groupe=id_groupe, admin = is_admin(current_user.idTypeUtilisateur)))
    return render_template('add_groupe.html', form=form)

@app.route('/hebergement', methods=['GET', 'POST'])
@login_required
def hebergement() :
    form = AddHebergement(get_all_hebergement(), get_unique_event_days())
    id_groupe = request.args.get('id_groupe')
    liste = create_liste_hebergement(id_groupe)
    groupe = get_groupe_by_id(id_groupe)
    if form.validate_on_submit():
        date_object = datetime.strptime(form.date.data, "%Y-%m-%d")
        if not is_date_ok_for_hebergement_groupe(date_object, int(form.nbJours.data), id_groupe) :
            return render_template('hebergement.html', form=form, groupe=groupe, liste=liste, erreur="le groupe n'est pas disponible à cette date")
        if not is_ok_capacite_hebergement(date_object, int(form.nbJours.data), form.hebergement.data, id_groupe) :
            return render_template('hebergement.html', form=form, groupe=groupe, liste=liste, erreur="le lieu n'est pas disponible à cette date")
        add_hebergement_db(form.hebergement.data, date_object, int(form.nbJours.data), id_groupe)
        return redirect(url_for('hebergement', id_groupe=id_groupe))
    return render_template('hebergement.html', form=form, groupe=groupe, liste=liste)