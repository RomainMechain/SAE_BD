import os
from app import app
from flask import render_template, request, redirect, url_for, make_response, send_file, jsonify, Response
from flask_login import login_required, login_user, logout_user, current_user
from flask_bcrypt import generate_password_hash, check_password_hash
from io import BytesIO
from functools import wraps
from unidecode import unidecode
from werkzeug.utils import secure_filename
from app.requests import *
from app.forms import *
from app import *
import base64
import collections

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
        return render_template('search_event.html', events=events, types=get_all_type_event(), int=int)

@app.route('/event', methods=['GET', 'POST'])
@login_required
def event() :
    dico_event = create_dico_event(request.args.get('id_event'))
    return render_template('event.html', dico_event=dico_event, int=int)

@app.route('/groupe', methods=['GET', 'POST'])
@login_required
def groupe() :
    dico_groupe = create_dico_groupe(request.args.get('id_groupe'))
    return render_template('groupe.html', dico_groupe=dico_groupe, int=int, est_favorie=groupe_is_favori(request.args.get('id_groupe'), current_user.idUtilisateur))

@app.route('/add_favori', methods=['GET', 'POST'])
@login_required
def add_favori() :
    add_favori_db(request.args.get('id_groupe'), current_user.idUtilisateur)
    return redirect(url_for('groupe', id_groupe=request.args.get('id_groupe')))

@app.route('/remove_favori', methods=['GET', 'POST'])
@login_required
def remove_favori() :
    remove_favori_db(request.args.get('id_groupe'), current_user.idUtilisateur)
    return redirect(url_for('groupe', id_groupe=request.args.get('id_groupe')))

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