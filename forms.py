from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from models import User

class RegistrationForm(FlaskForm):
    username = StringField("Nazwa użytkownika", validators=[DataRequired(), Length(min=4, max=150)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=250)])
    password = PasswordField("Hasło", validators=[DataRequired(), Length(min = 6)])
    confirm_password = PasswordField("Powtórz hasło", validators=[DataRequired(), EqualTo('password', message = "Hasła muszą być takie same")])
    submit = SubmitField("Zarejestruj się")

    # Walidacja użytkownika -> czy username jest unikalne
    def validate_username(self, username):
        existing_user = User.query.filter_by(username = username.data).first() #username.data = dane wprowadzone w formularzu
        if existing_user:
            raise ValidationError("Ta nazwa użytkownika jest już zajęta")
        
    # Walicja email -> czy email jest unikalny
    def validate_email(self, email):
        existing_email = User.query.filer_by(email = email.data).first() #email.data = dane wprowadzone w formularzu
        if existing_email:
            raise ValidationError("Istnieje konto przypisane do tego adresu e-mail")
