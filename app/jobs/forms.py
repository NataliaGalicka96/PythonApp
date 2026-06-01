from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Optional


class JobSearchForm(FlaskForm):

    query = StringField(
        "Stanowisko lub technologia",
        validators=[Optional()],
        render_kw={
            "placeholder":
            "Python, Backend, Flask, Google..."
        }
    )

    location = StringField(
        "Lokalizacja",
        validators=[Optional()],
        render_kw={
            "placeholder":
            "Warszawa, Remote..."
        }
    )

    submit = SubmitField("Szukaj")