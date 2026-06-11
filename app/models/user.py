from datetime import datetime, UTC

from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer

from app.extensions import db
from app.models.enums import UserRole


class User(UserMixin, db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(
        db.String(150),
        nullable=False
    )

    last_name = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.Enum(UserRole),
        nullable=False,
        default=UserRole.JOB_SEEKER
    )

    created = db.Column(
        db.DateTime,
        default=datetime.now(UTC)
    )

    # Generowanie tokenu resetu hasła
    def get_reset_token(self, expires_sec: int = 1800) -> str:
        # Pobieram sekretny klucz z pliku config.py, który jest potrzebny do wygenerowania tokenu
        secret_key = current_app.config.get("SECRET_KEY")
        if not secret_key:
            raise RuntimeError("SECRET_KEY is not configured")

        serializer = URLSafeTimedSerializer(secret_key)
        return serializer.dumps({"user_id": self.id}, salt="password-reset-salt")

    # Metoda weryfikująca token i zwraca go użytkownikowi lub None, jeśli token jest nieprawidłowy lub wygasł
    @staticmethod
    def verify_reset_token(token: str, expires_sec: int = 1800):
        secret_key = current_app.config.get("SECRET_KEY")
        if not secret_key:
            raise RuntimeError("SECRET_KEY is not configured")

        serializer = URLSafeTimedSerializer(secret_key)
        try:
            data = serializer.loads(
                token,
                salt="password-reset-salt",
                max_age=expires_sec,
            )
        except Exception:
            return None

        return User.query.get(data.get("user_id"))

    # ===== SAVED JOBS =====

    saved_jobs = db.relationship(
    "SavedJobOffer",
    back_populates="user",
    cascade="all, delete-orphan",
    lazy=True
    )

    # ===== APPLICATIONS =====
    
    applications = db.relationship(
    "Application",
    back_populates="user",
    cascade="all, delete-orphan",
    lazy=True
)

