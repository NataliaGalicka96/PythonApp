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

    # Dodanie konfiguracji serwera pocztowego
    MAIL_SERVER = "smtp.gmail.com" # Adres serwera SMTP Gmaila - Simple Mail Transfer Protocol
    MAIL_PORT = 587 # Port komunikacyjny SMTP 587 - TLS
    MAIL_USE_TLS = True # Włączenie szyfrowania połączenia -> Bez TLS hasło i login byłoby przesyłane jawnie

    MAIL_USERNAME = "natalia.galicka.programista@gmail.com" # Adres skrzynki, z której będą wysyłane maila
    MAIL_PASSWORD = "yjfk qjry gauv qrws" # Włączenie uwierzytelniania 2fa i wygenerowania hasła dla aplikacji

    MAIL_DEFAULT_SENDER = MAIL_USERNAME #domyślny nadawca maili