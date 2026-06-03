from flask import (
    Blueprint,
    render_template
)

from flask_login import (
    login_required,
    current_user
)

from app.models.application import Application
from app.models.saved_job_offer import SavedJobOffer

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


# DASHBOARD - główna strona dla zalogowanych
@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    latest_applications = (
        Application.query
        .filter_by(user_id=current_user.id)
        .order_by(Application.created.desc())
        .limit(5)
        .all()
    )

    latest_saved_jobs = (
        SavedJobOffer.query
        .filter_by(user_id = current_user.id)
        .order_by(SavedJobOffer.created_at.desc())
        .limit(5)
        .all()
    )

    return render_template("dashboard/index.html", latest_applications=latest_applications, latest_saved_jobs = latest_saved_jobs )


# WSZYSTKIE APLIKACJE - lista wszystkich aplikacji zalogowanego użytkownika
@dashboard_bp.route("/dashboard/applications")
@login_required
def applications():

    applications = (
        Application.query
        .filter_by(user_id=current_user.id)
        .order_by(Application.created.desc())
        .all()
    )

    return render_template("dashboard/applications.html", applications=applications)



