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

