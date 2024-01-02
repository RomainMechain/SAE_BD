from app import app, db
from app.models import *
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import csv
import sys

@app.cli.command('init_database')
def init_database():
    """Initialise la base de données avec les données des fichiers CSV
    """    
    
    db.create_all()
    Session = sessionmaker(bind=db.engine)
    session = Session()

    