from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, FileField, SelectField, SelectMultipleField
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

class AddGroupForm(FlaskForm):
    nom = StringField(validators=[DataRequired()], render_kw={"placeholder": "Nom"})
    description = StringField(validators=[DataRequired()], render_kw={"placeholder": "Description"})
    lienReseaux = StringField(validators=[DataRequired()], render_kw={"placeholder": "LienReseaux"})
    lienVideo = StringField(validators=[DataRequired()], render_kw={"placeholder": "LienVideo"})
    photo = FileField(validators=[DataRequired()])
    artistes = SelectMultipleField('Artistes', coerce=int, validators=[DataRequired()])
    instruments = SelectMultipleField('Instruments', coerce=int, validators=[DataRequired()])
    types_musique = SelectMultipleField('TypeMusique', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    def __init__(self, artistes, instruments, types_musique, *args, **kwargs):
        super(AddGroupForm, self).__init__(*args, **kwargs)
        self.artistes.choices = [(artiste.idArtiste, artiste.nomArtiste) for artiste in artistes]
        self.instruments.choices = [(instrument.idInstrument, instrument.nomInstrument) for instrument in instruments]
        self.types_musique.choices = [(type_musique.idTypeMusique, type_musique.nomTypeMusique) for type_musique in types_musique]

class AddHebergement(FlaskForm) :
    hebergement = SelectField('Hebergement', coerce=int, validators=[DataRequired()])
    date = SelectField('Date', coerce=str, validators=[DataRequired()])
    nbJours = StringField(validators=[DataRequired()], render_kw={"placeholder": "Nombre de jours"})
    submit = SubmitField('Ajouter')

    def __init__(self, hebergements, dates, *args, **kwargs):
        super(AddHebergement, self).__init__(*args, **kwargs)
        self.hebergement.choices = [(hebergement.idHebergement, hebergement.nomHebergement) for hebergement in hebergements]
        self.date.choices = [(date, date) for date in dates]