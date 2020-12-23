# services/users/project/__init__.py


import os

from flask import Flask  # nuevo
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS  # nuevo
from flask_migrate import Migrate  # new

# instanciando la db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()  # nuevo
migrate = Migrate()  # nuevo


def create_app(script_info=None):

    # instanciando la app
    app = Flask(__name__)

    # estableciendo la configuración
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # preparando la extensión
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    # registrar blueprints
    from project.api.users import users_blueprint

    app.register_blueprint(users_blueprint)

    # contexto shell para flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
