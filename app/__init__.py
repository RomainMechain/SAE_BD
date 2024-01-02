import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_dropzone import Dropzone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.normpath(os.path.join(os.path.dirname(__file__), 'database/app.db'))

if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(__file__), 'database'))):
    os.makedirs(os.path.normpath(os.path.join(os.path.dirname(__file__), 'database')))

db = SQLAlchemy(app)

from app import views
from app import models
from app import database
from app import requests
from app import forms