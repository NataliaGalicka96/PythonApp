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

    # Tworzenie formularza i przekazanie danych z URL np. /jobs?query=python&location=warszawa request.args zawiera 
    #    {
    #    "query": "python",
    #   "location": "warszawa"
    # }
    # czyli np. form.query.data = "python"
    form = JobSearchForm(request.args)

    # Wyszukuje w bazie danych aktywnych ogłoszeń
    jobs_query = JobOffer.query.filter_by(
        is_active=True
    )

    # wyszukiwarka
    # Sprawdzenie, czy uzytkownik wpisał coś w wyszukiwarkę
    if form.query.data:

        # Tworzę to co wyszukujemy, czyli np: %python%
        search = f"%{form.query.data}%"

        # znajdź wszystko, co zawiera „python”
        # case insensitive LIKE - czyli PYTHON, python, Python -> wszystko pasuje, nie zwraca uwagi na wielkość liter
        jobs_query = jobs_query.filter(
            db.or_(
                JobOffer.title.ilike(search),
                JobOffer.company.ilike(search)
            )
        )

    # lokalizacja
    # Sprawdzamy, czy użytkownik wpisał lokalizację
    if form.location.data:

        #np. %Warszawa%
        location = f"%{form.location.data}%"


        # Wyszukuję w bazie danych wszystkie oferty, które w lokalizacji mają Warszawa -> bez znaczenia wielkość liter
        jobs_query = jobs_query.filter(
            JobOffer.location.ilike(location)
        )

    # PAGINACJA
    # Czytasz numer strony z URL np. /jobs?page=3 -> wtedy page = 3, jeśli nie ma to domyślnie page = 1
    page = request.args.get("page", 1, type=int)

    # Sortowanie ofert w bazie danych malejącowo wg daty utworzenia
    # Wyświetlanie na stronie po 10 ogłoszeń
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