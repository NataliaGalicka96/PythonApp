from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    current_app
)

from flask_mail import Message
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.extensions import mail
from app.models.user import User
from app.auth.forms import (
    RegistrationForm,
    LoginForm
)

# blueprint auth
auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


def send_reset_email(user):
    token = user.get_reset_token() # Tworzenie tokenu resetu hasła dla użytkownika
    msg = Message(
        subject="Reset hasła",
        sender=current_app.config.get("MAIL_DEFAULT_SENDER"),
        recipients=[user.email]
    ) #Budowanie wiadomości dla użytkownika, który chce zresetować hasło
    msg.body = f"""Aby zresetować hasło, kliknij poniższy link:
{url_for('auth.reset_token', token=token, _external=True)}

Jeżeli nie zgłaszałeś żądania resetu hasła, zignoruj tę wiadomość."""
    mail.send(msg)


# REJESTRACJA
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    # jeśli użytkownik już zalogowany
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data
        )

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            flash("Konto zostało utworzone", "success")

            return redirect(url_for("auth.login"))

        except Exception:

            db.session.rollback()

            flash("Błąd podczas rejestracji","danger"
            )

    return render_template("auth/register.html", form=form)

# LOGOWANIE
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(user.password,form.password.data):

            login_user(user, 
                       remember=form.remember.data) # Przekazanie do logowania również pola remember - zapamiętaj

            flash("Zalogowano pomyślnie","success"
            )

            return redirect(url_for("dashboard.dashboard"))
        flash("Niepoprawne dane logowania","danger")

    return render_template("auth/login.html", form=form)


# WYLOGOWANIE
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Wylogowano", "info")

    return redirect(url_for("jobs.home"))