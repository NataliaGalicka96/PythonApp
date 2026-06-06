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
            name = "fk_saved_job_user"
        ),
        nullable = False
    )

    job_offer_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "job_offer.id",
            name = "fk_saved_job_offer"
        ),
        nullable = False
    )

    created_at = db.Column(
        db.DateTime,
        default = datetime.now(UTC)
    )

    # RELATIONSHIP
    
    # User -> jeden User może mieć wiele polubionych ofert
    user = db.relationship(
        "User",
        back_populates = "saved_jobs"
    )

    # JobOffer -> jedna oferta może być zapisana przez wielu użytkowników
    job_offer = db.relationship(
        "JobOffer",
        back_populates="saved_by_users"
    )

    # Użytkownik może dodać tę samą ofertę raz do ulubionych, czyli unikamy duplikowania wpisów
    __table_args__ = (
    db.UniqueConstraint(
        "user_id",
        "job_offer_id",
        name="uq_saved_job"
    ),
)
