from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, DateField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for putting a new pet for adoption."""

    name = StringField("Pet's Name", validators=[InputRequired()])
    species = SelectField("Pet's Species", choices=[("dog", "dog"), ("cat", "cat"), ("porcupine", "porcupine"), ("bunny", "bunny"), ("hamster", "hamster"), ("other", "other")])
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=25)])
    notes = TextAreaField("Additional Information", validators=[Optional(), Length(max=200)])
    available = BooleanField("Available for adoption?")
    
class EditPetForm(FlaskForm):
    """Allows the user to edit an existing pet"""

    photo_url = StringField("Photo", validators=[Optional(), URL()])
    notes = TextAreaField("Additional Information", validators=[Optional(), Length(max=200)])
    available = BooleanField("Available for adoption?")