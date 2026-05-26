# Plik pomocniczy - uzupełniający tabelę JobOffer przykłdowymi ogłoszeniami
from datetime import datetime, timedelta, UTC
from app import app, db
from models import JobOffer, JobOfferType, Level, JobType

# Przykładowe dane
job_offers = [
    JobOffer(
        title="Python Developer",
        description="Tworzenie i rozwój aplikacji webowych w Pythonie.",
        responsibilites="Pisanie kodu, tworzenie API, utrzymanie aplikacji.",
        location="Warszawa",
        salary_min=12000,
        salary_max=18000,
        type_of_contract=JobOfferType.UOP,
        level=Level.MID,
        job_type=JobType.STACJONARNA,
        is_active=True,
        created=datetime.now(UTC),
        expired=datetime.now(UTC) + timedelta(days=30)
    ),

    JobOffer(
        title="Frontend Developer React",
        description="Rozwój interfejsów użytkownika w React.",
        responsibilites="Tworzenie komponentów, integracja z backendem.",
        location="Kraków",
        salary_min=10000,
        salary_max=16000,
        type_of_contract=JobOfferType.B2B,
        level=Level.JUNIOR,
        job_type=JobType.HYBRYDOWA,
        is_active=True,
        created=datetime.now(UTC),
        expired=datetime.now(UTC) + timedelta(days=30)
    ),

    JobOffer(
        title="DevOps Engineer",
        description="Automatyzacja procesów CI/CD oraz zarządzanie infrastrukturą.",
        responsibilites="Docker, Kubernetes, monitoring systemów.",
        location="Wrocław",
        salary_min=15000,
        salary_max=22000,
        type_of_contract=JobOfferType.B2B,
        level=Level.SENIOR,
        job_type=JobType.HYBRYDOWA,
        is_active=True,
        created=datetime.now(UTC),
        expired=datetime.now(UTC) + timedelta(days=30)
    ),

    JobOffer(
        title="Data Analyst",
        description="Analiza danych biznesowych oraz przygotowywanie raportów.",
        responsibilites="SQL, Power BI, analiza trendów.",
        location="Gdańsk",
        salary_min=8000,
        salary_max=13000,
        type_of_contract=JobOfferType.ZLECENIE,
        level=Level.MID,
        job_type=JobType.ZDALNA,
        is_active=True,
        created=datetime.now(UTC),
        expired=datetime.now(UTC) + timedelta(days=30)
    ),

    JobOffer(
        title="Backend Developer Flask",
        description="Budowa REST API we Flask.",
        responsibilites="Projektowanie modeli danych i endpointów API.",
        location="Poznań",
        salary_min=11000,
        salary_max=17000,
        type_of_contract=JobOfferType.UOP,
        level=Level.MID,
        job_type=JobType.ZDALNA,
        is_active=True,
        created=datetime.now(UTC),
        expired=datetime.now(UTC) + timedelta(days=30)
    )
]

with app.app_context():
    db.session.add_all(job_offers)
    db.session.commit()

    print("Dodano przykładowe oferty pracy.")