# Modele klas - odzwierciedlenie tabel w bazie danych
from extensions import db
from flask_login import UserMixin
from datetime import datetime, UTC
from enums import UserRole

# UserMixin pochodzi z bilioteki flask_login
# Flask-LOgin wymaga, żeby obiekt użytkownika miał określone metody: is_authenticated
# is_active, is_anonymous, get_id()
# Zamiast pisać je ręcznie, dziedziczysz po UserMixin, który już je implementuje.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = False)
    role = db.Column(db.Enum(UserRole), nullable = False, default = UserRole.JOB_SEEKER)
    created = db.Column(db.DateTime, default = datetime.now(UTC)) # UTC - uniwersalny światowy czas


