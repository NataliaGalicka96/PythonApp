from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

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

from app.extensions import db
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

            login_user(user)

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