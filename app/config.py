import os
from dotenv import load_dotenv
from datetime import timedelta

# pip install python-dotenv
# Ładowanie zmiennych z pliku .env

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' +
        os.path.join(basedir, '..', 'job_app.db')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    # Dodanie konfiguracji dla opcji "Zapamiętaj mnie - przy logowaniu", żeby opcja działała np. 30 dni a nie domyślnie cały czas
    REMEMBER_COOKIE_DURATION = timedelta(days=30)