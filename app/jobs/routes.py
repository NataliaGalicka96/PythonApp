from flask import (
    Blueprint,
    render_template,
    request
)

from app.extensions import db
from app.models.job_offer import JobOffer
from app.jobs.forms import JobSearchForm

jobs_bp = Blueprint(
    "jobs",
    __name__
)


# HOME - taka strona główna - na której widoczne jest 10 najnowszych ogłoszeń -> dla niezalogowanych dostępna
@jobs_bp.route("/")
def home():

    latest_offers = (
        JobOffer.query
        .filter_by(is_active=True)
        .order_by(JobOffer.created.desc())
        .limit(10)
        .all()
    )

    return render_template("jobs/home.html", offers=latest_offers)


# LISTA OFERT - wyszukiwanie ofert po np. lokalizacji, tytule, firmie
@jobs_bp.route("/jobs")
def jobs():

    form = JobSearchForm(request.args)

    jobs_query = JobOffer.query.filter_by(
        is_active=True
    )

    # wyszukiwarka
    if form.query.data:

        search = f"%{form.query.data}%"

        jobs_query = jobs_query.filter(
            db.or_(
                JobOffer.title.ilike(search),
                JobOffer.company.ilike(search)
            )
        )

    # lokalizacja
    if form.location.data:

        location = f"%{form.location.data}%"

        jobs_query = jobs_query.filter(
            JobOffer.location.ilike(location)
        )


    page = request.args.get("page", 1, type=int)

    offers = (
    jobs_query
    .order_by(JobOffer.created.desc())
    .paginate(page=page, per_page=10)
    )

    return render_template("jobs/home.html", offers=offers, form=form
    )


# SZCZEGÓŁY OFERTY
@jobs_bp.route("/jobs/<int:job_id>")
def job_details(job_id):

    offer = JobOffer.query.get_or_404(job_id)

    return render_template("jobs/job_details.html", offer=offer)