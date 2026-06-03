# id
# user_id
# job_offer_id
# created_at
from datetime import datetime, UTC
from app.extensions import db

class SavedJobOffer(db.Model):
    __tablename__ = "saved_job_offer"

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "user.id",
            name = "fk_job_offer_user_liked"
        ),
        nullable = False
    )

    job_offer_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "job_offer.id",
            name = "fk_job_offer_liked"
        )
    )

    created_at = db.Column(
        db.DateTime,
        default = datetime.now(UTC)
    )

    # RELATIONSHIP
    # Dodajemy relację z tabelą JobOffer -> Każda oferta może być dodana do ulubionych przez kilku użytkowników
    # Możemy wtedy użyć w templates {% for saved in latest_saved_jobs %} -> saved.job_offer.title zamiast JOIN
    job_offer = db.relationship(
        "JobOffer",
        backref="saved_by_users"
    )


