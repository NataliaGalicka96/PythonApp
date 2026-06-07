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
from app.models.enums import ApplicationStatus

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

    applications = (
        Application.query
        .filter_by(user_id = current_user.id)
        .all()
    )
    grouped_applications = {
        
        status: []
        for status in ApplicationStatus
    }

    for application in applications:

        grouped_applications[application.status].append(application)

    return render_template("dashboard/index.html", latest_applications=latest_applications, 
                           latest_saved_jobs = latest_saved_jobs, grouped_applications=grouped_applications 
                           )


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
