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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    form = LoginForm()
    user = get_user_by_email(form.mail.data)
    if form.validate_on_submit():
        if user :
            if check_password_hash(user.mdpSpectateur, form.mdp.data):
                login_user(user)
                return redirect(url_for('home'))
    return render_template('login.html', form=form, login=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register page"""
    form = LoginForm()
    return render_template('login.html', form=form)
