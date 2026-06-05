from datetime import datetime, UTC
from app.extensions import db

class Application(db.Model):

    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(
        db.String(50),
        default="pending"
    )

    created = db.Column(
        db.DateTime,
        default=datetime.now(UTC)
    )

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

    cv_filename = db.Column(
        db.String(255)
    )

    