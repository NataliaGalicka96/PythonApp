from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)

from flask_login import login_required, current_user

from app.extensions import db
from app.models.job_offer import JobOffer
from app.models.saved_job import SavedJobOffer
from app.jobs.forms import JobSearchForm
from app.__init__ import create_app
import logging



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

    # SAVED OFFERS

    saved_offer_ids = set()

    if current_user.is_authenticated:

        saved_offer_ids = {

            saved.job_offer_id
            for saved in current_user.saved_jobs

        }

    return render_template("jobs/home.html", offers=latest_offers, saved_offer_ids = saved_offer_ids)


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


    # SAVED OFFERS

    saved_offer_ids = set()

    if current_user.is_authenticated:

        saved_offer_ids = {

            saved.job_offer_id
            for saved in current_user.saved_jobs

        }

    return render_template("jobs/home.html", offers=offers, form=form, saved_offer_ids = saved_offer_ids
    )


# SZCZEGÓŁY OFERTY
@jobs_bp.route("/jobs/<int:job_id>")
def job_details(job_id):

    offer = JobOffer.query.get_or_404(job_id)

    return render_template("jobs/job_details.html", offer=offer)


# ZAPISANIE OFERTY DO ULUBIONYCH
@jobs_bp.route("/jobs/<int:id>/save", methods = ["POST"])
@login_required # Tylko zalogowany użytkownik
def save_job(id):
    # Pobranie oferty o tym id
    job = JobOffer.query.get_or_404(id)


    # Zasada - jeśli jest już w ulubionych dla tego użytkownika, to usuniemy z ulubionych, a jeśli nei jest to dodamy
    existing_save = SavedJobOffer.query.filter_by(
        user_id = current_user.id,
        job_offer_id = job.id
    ).first()


    try:
        if existing_save:
            db.session.delete(existing_save) #Usuwam wpis z tabeli
            db.session.commit()
            return jsonify({
                "saved": False,
                "message": "Ta oferta została usunięta z ulubionych"
            }), 201
        
         # Zapisywanie do ulubionych
        saved_job = SavedJobOffer (
            user_id = current_user.id,
            job_offer_id = job.id
        )

        db.session.add(saved_job)
        db.session.commit()

        return jsonify({
            "saved": True,
            "message": "Dodano ofertę do ulubionych"
        }), 201
    except Exception as e:
            db.session.rollback()
            create_app.logger.error(f"Wystąpił błąd podczas")
            return jsonify({
                "error", "Wystąpił błąd podczas dodawania oferty do ulubionych"
            }), 500
    
    

   