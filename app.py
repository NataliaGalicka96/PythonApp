from flask import Flask
from extensions import db, login_manager, csrf, migrate
import os # Obsługa plików



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

if __name__ == '__main__':
    
    # W wersji produkcujnej zakomentować - NIE UŻYWAĆ
    app.run(debug=True)