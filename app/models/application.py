from datetime import datetime, UTC
from app.extensions import db
from app.models.enums import ApplicationStatus

class Application(db.Model):

    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(
    db.Enum(
        ApplicationStatus,
        validate_strings=True
    ),
    default=ApplicationStatus.ZAAPLIKOWANO,
    nullable=False
    )

    cv_filename = db.Column(
        db.String(255)
    )

    created = db.Column(
        db.DateTime,
        default=datetime.now(UTC)
    )

    # ===== FOREIGN KEYS =====

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "user.id",
            name="fk_application_user"
            ),
        nullable=False
    )

    job_offer_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "job_offer.id",
            name="fk_application_job_offer"         
            ),
        nullable=False
    )

    # ===== RELATIONSHIPS =====
    # RELATIONSHIP
    # Aplikacja na konkretną ofertę pracy
    job_offer = db.relationship(
        "JobOffer",
        back_populates="applications"
    )

    # Aplikacja przez konkretnego Usera
    user = db.relationship(
        "User",
        back_populates="applications"
    )

    # Użytkownik może raz aplikować na daną ofertę pracy
    __table_args__ = (
    db.UniqueConstraint(
        "user_id",
        "job_offer_id",
        name="uq_application"
    ),
)


