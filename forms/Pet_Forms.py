from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, optional, NumberRange


class NewPetForm(FlaskForm):

    name = StringField('Pet Name', validators=[
                       InputRequired(message='Name Cannot Be Blank')])
    species = SelectField('Species', choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[
                            URL(message='Must be a valid URL'), optional()])
    age = FloatField('Age', validators=[optional(), NumberRange(
        min=0, max=30, message='Age must be between 0 and 30')])
    notes = TextAreaField('Notes')


class EditPetForm(FlaskForm):

    photo_url = StringField('Photo URL', validators=[
                            URL(message='Must be a valid URL'), optional()])
    notes = TextAreaField('Notes')

    available = BooleanField('This Pet is Available')
