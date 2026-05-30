# Modele klas - odzwierciedlenie tabel w bazie danych
from PythonApp.app.extensions import db
from flask_login import UserMixin
from datetime import datetime, timedelta, UTC
from enums import UserRole, JobOfferType, JobType, Level

# UserMixin pochodzi z bilioteki flask_login
# Flask-LOgin wymaga, żeby obiekt użytkownika miał określone metody: is_authenticated
# is_active, is_anonymous, get_id()
# Zamiast pisać je ręcznie, dziedziczysz po UserMixin, który już je implementuje.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(150), nullable = False)
    role = db.Column(db.Enum(UserRole), nullable = False, default = UserRole.JOB_SEEKER)
    created = db.Column(db.DateTime, default = datetime.now(UTC)) # UTC - uniwersalny światowy czas


# Klasa reprezentująca ogłoszenie
class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    description = db.Column(db.String(), nullable = False)
    responsibilites = db.Column(db.String(), nullable = False)
    location = db.Column(db.String(255), nullable = False)
    salary_min = db.Column(db.Float(), nullable = True)
    salary_max = db.Column(db.Float(), nullable = True)
    type_of_contract = db.Column(db.Enum(JobOfferType), nullable = False, default = JobOfferType.UOP)
    level = db.Column(db.Enum(Level), nullable = False)
    job_type = db.Column(db.Enum(JobType), nullable = False)
    is_active = db.Column(db.Boolean, nullable = False, default = True)
    created = db.Column(db.DateTime, default = datetime.now(UTC)) # UTC - uniwersalny światowy czas
    expired = db.Column(db.DateTime, nullable = False,  default=lambda: datetime.now(UTC) + timedelta(days=30))
