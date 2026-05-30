from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Optional


class JobSearchForm(FlaskForm):

    query = StringField(
        "Stanowisko",
        validators=[Optional()]
    )

    location = StringField(
        "Lokalizacja",
        validators=[Optional()]
    )

    submit = SubmitField("Szukaj")