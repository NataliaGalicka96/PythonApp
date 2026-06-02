from datetime import datetime, UTC

from flask_login import UserMixin

from app.extensions import db
from app.models.enums import UserRole


class User(UserMixin, db.Model):

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

    saved_jobs = db.relationship(
    "SavedJobOffer",
    backref="user",
    lazy=True
    )