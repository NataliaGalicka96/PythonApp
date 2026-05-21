from flask import Flask, render_template
from extensions import db, login_manager, csrf, migrate
import os # Obsługa plików
from models import User
from flask_login import login_user, login_required, logout_user, current_user



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


if __name__ == '__main__':
    
    # W wersji produkcyjnej zakomentować - NIE UŻYWAĆ
    app.run(debug=True)