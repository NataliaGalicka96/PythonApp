from flask import (
    Blueprint,
    jsonify,
    request
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db

from app.models.application import Application
from app.models.enums import ApplicationStatus


applications_bp = Blueprint(
    "applications",
    __name__
)

@applications_bp.route(
    "/applications/<int:application_id>/status",
    methods=["POST"]
)
@login_required
def update_application_status(application_id):

    application = Application.query.get_or_404(
        application_id
    )

    print(application)

    # SECURITY

    if application.user_id != current_user.id:

        return jsonify({
            "error": "Brak dostępu"
        }), 403

    data = request.get_json()

    print(request.get_json())

    new_status = data.get("status")

    application.status = ApplicationStatus[
        new_status
    ]

    db.session.commit()

    return jsonify({
        "success": True
    })