# Plik zawiera m.in. inicjalizację ORM - bazę danych, SQLAlchemy
# Plik zawiera inizjalizację LoginManager oraz instancję CSRF
from flask_sqlalchemy import SQLAlchemy

# Tworzę instancję bazy danych ORM
db = SQLAlchemy()

