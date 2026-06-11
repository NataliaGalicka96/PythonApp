from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo,
    ValidationError,
    Email
)

from app.models.user import User

class RegistrationForm(FlaskForm):

    first_name = StringField(
        "Imię",
        validators=[DataRequired(), Length(max=150)]
    )

    last_name = StringField(
        "Nazwisko",
        validators=[DataRequired(), Length(max=150)]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=250)
        ]
    )

    password = PasswordField(
        "Hasło",
        validators=[DataRequired(), Length(min=6)]
    )

    confirm_password = PasswordField(
        "Powtórz hasło",
        validators=[
            DataRequired(),
            EqualTo(
                'password',
                message="Hasła muszą być takie same"
            )
        ]
    )

    submit = SubmitField("Zarejestruj się")

    def validate_email(self, email):

        existing_email = User.query.filter_by(
            email=email.data
        ).first()

        if existing_email:
            raise ValidationError(
                "Istnieje konto przypisane do tego adresu"
            )


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Hasło",
        validators=[DataRequired()]
    )

    remember = BooleanField("Zapamiętaj mnie")

    submit = SubmitField("Zaloguj się")


class RequestResetForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=250)
        ]
    )

    submit = SubmitField("Wyślij link resetujący")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "Nie znaleziono użytkownika z tym adresem email."
            )


class ResetPasswordForm(FlaskForm):

    password = PasswordField(
        "Nowe hasło",
        validators=[DataRequired(), Length(min=6)]
    )

    confirm_password = PasswordField(
        "Powtórz nowe hasło",
        validators=[
            DataRequired(),
            EqualTo(
                'password',
                message="Hasła muszą być takie same"
            )
        ]
    )

    submit = SubmitField("Zresetuj hasło")