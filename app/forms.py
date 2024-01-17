from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, FileField, DateTimeField, FloatField, SelectField
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

class addEventForm(FlaskForm) :
    nom = StringField(validators=[DataRequired()], render_kw={"placeholder": "Nom"})
    date = StringField(validators=[DataRequired()], render_kw={"placeholder": "date"})
    duree = StringField(validators=[DataRequired()], render_kw={"placeholder": "duree"})
    dureeMontage = StringField(validators=[DataRequired()], render_kw={"placeholder": "dureeMontage"})
    dureeDemontage = StringField(validators=[DataRequired()], render_kw={"placeholder": "dureeDemontage"})
    groupe = SelectField('Groupe', coerce=int, validators=[DataRequired()])
    lieu = SelectField('Lieu', coerce=int, validators=[DataRequired()])
    type_event = SelectField('Type', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    def __init__(self, groupes, lieux, types_event, *args, **kwargs):
        super(addEventForm, self).__init__(*args, **kwargs)
        self.groupe.choices = [(groupe.idGroupe, groupe.nomGroupe) for groupe in groupes]
        self.lieu.choices = [(lieu.idLieu, lieu.nomLieu) for lieu in lieux]
        self.type_event.choices = [(type_event.idTypeEvenement, type_event.nomTypeEvenement) for type_event in types_event]