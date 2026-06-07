from flask import Flask

from app.config import Config
from app.extensions import db, migrate, login_manager, csrf


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # inicjalizacja rozszerzeń
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # IMPORT MODELI
    from app.models.user import User

    # USER LOADER
    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    # blueprinty
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.jobs.routes import jobs_bp
    from app.applications.routes import applications_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(applications_bp)

    return app