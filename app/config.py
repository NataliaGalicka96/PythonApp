import os
from dotenv import load_dotenv

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