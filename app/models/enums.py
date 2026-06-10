from enum import Enum

class UserRole(str, Enum):
    JOB_SEEKER = "job_seeker"
    RECRUITER = "recruiter"
    ADMIN = "admin"

class JobOfferType(str, Enum):
    B2B = "Kontrakt B2B"
    DZIEŁO = "Umowa o dzieło"
    UOP = "Umowa o pracę"
    ZLECENIE = "Umowa zlecenie"
    ZASTEPSTWO = "Umowa na zastępstwo"
    PRAKTYKI = "Umowa o staż/praktyki"

class Level(str, Enum):
    PRAKTYKANT = "Praktykant"
    JUNIOR = "Młodszy specjalista"
    MID = "Specjalista"
    SENIOR = "Starszy specjalista"
    EKSPERT = "Ekspert"
    KIEROWNIK = "Kierownik"
    MANAGER = "Menedżer"
    DYREKTOR = "Dyrektor"
    PREZES = "Prezes"

class JobType(str, Enum):
    ZDALNA = "Zdalna"
    HYBRYDOWA = "Hybrydowa"
    STACJONARNA = "Stacjonarna"

class ApplicationStatus(Enum):
    ZAAPLIKOWANO = "Zaaplikowano"
    SELEKCJA = "Selekcja"
    ROZMOWA = "Rozmowa"
    OFERTA = "Oferta"
    ZATRUDNIONY = "Zatrudniony"
    ODRZUCONY = "odrzucony"


