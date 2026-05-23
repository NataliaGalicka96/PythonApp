from flask import Flask, render_template, redirect, url_for, flash
from extensions import db, login_manager, csrf, migrate
import os # Obsługa plików
from models import User
from flask_login import login_user, login_required, logout_user, current_user
from forms import RegistrationForm, LoginForm

# Do bezpiecznego haszowania haseł:
# generate_password_hash() – tworzy hash hasła
# check_password_hash() – sprawdza czy hasło pasuje do hasha
from werkzeug.security import generate_password_hash, check_password_hash
import logging




# Tworzę aplikację Flaska
# tajny klucz sesji, zabezpieczenie przed CSRF, na produkcji losowy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABCD3456'

# Konfiguracja bazy danych
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'job_app.db')

db.init_app(app)
login_manager.init_app(app)
csrf.init_app(app)
migrate.init_app(app, db)

# Metoda ładowania użytkownika
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Strona główna - dostępna dla niezalogowanych -> tylko przeglądanie ogłoszeń
@app.route("/")
def index():
    return render_template("index.html")

# Rejestracja
@app.route("/register", methods = ['GET', 'POST'])
def register():
    #Sprawdzenie, czy użytkownik jest już zalogowany - jeśli tak, to przekierowujemy na główną stronę
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    #Użytkownik nie jest zalogowany, to tworzymy formularz rejestracji
    form = RegistrationForm()
    if form.validate_on_submit():
        # Dodanie użytkownika do bazy
        hashed_password = generate_password_hash(form.password.data) # dane wprowadzone w formularzu form.password.data'
        new_user = User(first_name = form.first_name.data, last_name = form.last_name.data, email = form.email.data,  password = hashed_password)

        # Próbujemy dodać użytkownika do bazy danych
        try:
            db.session.add(new_user)
            db.session.commit()

            # Wyświetlenie komunikatu
            flash("Twoje konto zostało utworzone! Możesz się zalogować", "success")

            # Przekierowanie na stronę logowania
            return redirect(url_for("login"))
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Błąd przy rejestracji użytkownika: {e}")
            flash("Wystąpił błąd podczas rejestracji użytkownika. Spróbuj ponownie.", "danger")

    # gdy dane w formularzu niepoprawne - wyświetlamy ponownie formularz
    return render_template("register.html", form=form)

# Logowanie
@app.route("/login", methods = ['POST', 'GET'])
def login():
    # Sprawdzenie, czy użytkownik jest już zalogowwany
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    # Użytkownik nie jest zalogowany, to dodamy formularz logowania
    form = LoginForm()
    if form.validate_on_submit():
        # Pobieram użytkownika o podanym emailu
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            # Jeśli istnieje użytkownik o takim emailu w bazie i hasło się zgadza
            # Logujemy użytkownika
            login_user(user)
            flash("Zostałeś zalogowany", "success")
            return redirect(url_for("index"))
        else:
            flash("Niepoprawne dane logowania", "danger")

    # Jeśli brak danych w formularzu, ponowne wyrenderowanie
    return render_template("login.html", form=form)

# Wylogowanie
@login_required
@app.route("/logout")
def logout():
    logout_user()
    flash("Zostałeś wylogowany", "info")
    return redirect(url_for("login"))


if __name__ == '__main__':
    
    # W wersji produkcyjnej zakomentować - NIE UŻYWAĆ
    app.run(debug=True)