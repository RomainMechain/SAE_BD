from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    mail = StringField(validators=[DataRequired()], render_kw={"placeholder": "Email"})
    mdp = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Mot de passe"})
    submit = SubmitField('Se connecter')

class RegisterForm(FlaskForm):
    id = HiddenField('id')
    nom = StringField(validators=[DataRequired()], render_kw={"placeholder": "Nom"})
    prenom = StringField(validators=[DataRequired()], render_kw={"placeholder": "Prénom"})
    mail = StringField(validators=[DataRequired()], render_kw={"placeholder": "Email"})
    mdp = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Mot de passe"})
    telephone = StringField(validators=[DataRequired()], render_kw={"placeholder": "Téléphone"})
    submit = SubmitField('Ajouter')

class addArtisteForm(FlaskForm) :
    id = HiddenField('id')
    nom = StringField(validators=[DataRequired()], render_kw={"placeholder": "Nom"})
    description = StringField(validators=[DataRequired()], render_kw={"placeholder": "Description"})
    photo = FileField(validators=[DataRequired()])
    submit = SubmitField('Ajouter')