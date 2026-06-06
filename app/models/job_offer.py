from datetime import datetime, timedelta, UTC

from app.extensions import db
from app.models.enums import (
    JobOfferType,
    JobType,
    Level
)

class JobOffer(db.Model):

    __tablename__ = "job_offer"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(500),
        nullable=False
    )

    company = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    responsibilities = db.Column(
        db.Text,
        nullable=False
    )

    location = db.Column(
        db.String(255),
        nullable=False
    )

    salary_min = db.Column(db.Float)
    salary_max = db.Column(db.Float)

    type_of_contract = db.Column(
        db.Enum(JobOfferType),
        nullable=False
    )

    level = db.Column(
        db.Enum(Level),
        nullable=False
    )

    job_type = db.Column(
        db.Enum(JobType),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created = db.Column(
        db.DateTime,
        default=datetime.now(UTC)
    )

    expired = db.Column(
        db.DateTime,
        default=lambda: (
            datetime.now(UTC) + timedelta(days=30)
        )
    )

    # recruiter_id = db.Column(
    #     db.Integer,
    #     db.ForeignKey(
    #         "user.id",
    #         name="fk_job_offer_recruiter"),
    #     nullable=True
    # )


    # ===== RELATIONSHIPS =====


    applications = db.relationship(
        "Application",
        back_populates="job_offer",
        cascade="all, delete-orphan",
        lazy=True
    )

    saved_by_users = db.relationship(
        "SavedJobOffer",
        back_populates="job_offer",
        cascade="all, delete-orphan",
        lazy=True
    )