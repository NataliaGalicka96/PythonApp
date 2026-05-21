# Plik zawiera m.in. inicjalizację ORM - bazę danych, SQLAlchemy
# Plik zawiera inizjalizację LoginManager oraz instancję CSRF
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

# Tworzę instancję bazy danych ORM
# Migracja posłuży nam do aktualizowania/tworzenia tabel w bazie danych
db = SQLAlchemy()
migrate = Migrate()

# Tworzę instancję LoginManager, do tworzenia stron logowania
# Dzięki temu managerowi, nie będę msuiała sama definiować metod np. autoryzacja, zalogowanie użytkownika, czy jest zalogowany itd..
# Ustawiam widok logowania, kategorię komunikatów, ustawienie komunikatu
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.login_message = "Zaloguj się, aby uzyskać dostęp do tej strony"

# Tworzenie instancji CSRF
csrf = CSRFProtect()
