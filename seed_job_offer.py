from app import create_app
from app.extensions import db

from app.models.job_offer import JobOffer

from app.models.enums import (
    JobOfferType,
    JobType,
    Level
)

app = create_app()

with app.app_context():

    offers = [

        JobOffer(
            title="Backend Developer (Python)",
            company="TechCorp",
            description="Rozwój i utrzymanie API we Flasku.",
            responsibilities="Tworzenie REST API, integracje, praca z bazą danych.",
            location="Warszawa",
            salary_min=12000,
            salary_max=18000,
            type_of_contract=JobOfferType.B2B,
            level=Level.MID,
            job_type=JobType.HYBRYDOWA
        ),

        JobOffer(
            title="Frontend Developer (React)",
            company="FutureSoft",
            description="Budowa nowoczesnych aplikacji frontendowych.",
            responsibilities="Tworzenie komponentów React i integracja z API.",
            location="Remote",
            salary_min=10000,
            salary_max=16000,
            type_of_contract=JobOfferType.UOP,
            level=Level.JUNIOR,
            job_type=JobType.ZDALNA
        ),

        JobOffer(
            title="Full Stack Developer",
            company="CodeWave",
            description="Praca nad aplikacją webową end-to-end.",
            responsibilities="Backend Flask + frontend React.",
            location="Kraków",
            salary_min=14000,
            salary_max=22000,
            type_of_contract=JobOfferType.B2B,
            level=Level.SENIOR,
            job_type=JobType.HYBRYDOWA
        ),

        JobOffer(
            title="Data Analyst",
            company="DataMind",
            description="Analiza danych biznesowych i raportowanie.",
            responsibilities="SQL, dashboardy, analiza KPI.",
            location="Wrocław",
            salary_min=9000,
            salary_max=13000,
            type_of_contract=JobOfferType.UOP,
            level=Level.MID,
            job_type=JobType.STACJONARNA
        ),

        JobOffer(
            title="DevOps Engineer",
            company="CloudNet",
            description="Utrzymanie infrastruktury chmurowej.",
            responsibilities="Docker, CI/CD, monitoring aplikacji.",
            location="Gdańsk",
            salary_min=15000,
            salary_max=23000,
            type_of_contract=JobOfferType.B2B,
            level=Level.SENIOR,
            job_type=JobType.ZDALNA
        ),

        JobOffer(
            title="QA Engineer",
            company="SoftLabs",
            description="Testowanie aplikacji webowych.",
            responsibilities="Testy manualne i automatyczne.",
            location="Poznań",
            salary_min=8000,
            salary_max=12000,
            type_of_contract=JobOfferType.UOP,
            level=Level.JUNIOR,
            job_type=JobType.HYBRYDOWA
        ),

        JobOffer(
            title="Mobile Developer (Flutter)",
            company="AppForge",
            description="Rozwój aplikacji mobilnych Flutter.",
            responsibilities="Tworzenie aplikacji Android/iOS.",
            location="Remote",
            salary_min=11000,
            salary_max=17000,
            type_of_contract=JobOfferType.B2B,
            level=Level.MID,
            job_type=JobType.ZDALNA
        ),

        JobOffer(
            title="UI/UX Designer",
            company="Pixel Studio",
            description="Projektowanie interfejsów użytkownika.",
            responsibilities="Tworzenie makiet i design systemów.",
            location="Łódź",
            salary_min=7000,
            salary_max=12000,
            type_of_contract=JobOfferType.UOP,
            level=Level.MID,
            job_type=JobType.HYBRYDOWA
        ),

        JobOffer(
            title="Machine Learning Engineer",
            company="AI Solutions",
            description="Budowa modeli ML i AI.",
            responsibilities="Python, TensorFlow, analiza danych.",
            location="Warszawa",
            salary_min=18000,
            salary_max=28000,
            type_of_contract=JobOfferType.B2B,
            level=Level.SENIOR,
            job_type=JobType.ZDALNA
        ),

        JobOffer(
            title="Junior Python Developer",
            company="StartIT",
            description="Rozwój backendu dla startupu.",
            responsibilities="Pisanie prostych endpointów i testów.",
            location="Katowice",
            salary_min=6000,
            salary_max=9000,
            type_of_contract=JobOfferType.UOP,
            level=Level.JUNIOR,
            job_type=JobType.STACJONARNA
        )

    ]

    db.session.add_all(offers)

    db.session.commit()

    print("Dodano 10 ofert pracy.")