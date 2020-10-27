from flask import Flask
from flask_migrate import Migrate

from pifano.blueprints.restapi.user_service import bp_user

from pifano.external.models import configure as configure_db


def create_app(*args, **kwargs):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pifano.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'you-can-try-but-you-will-never-guess'

    # Configure DB
    configure_db(app)

    # Configure Flask Migrate
    Migrate(app, app.db)

    # Blueprints
    app.register_blueprint(bp_user)

    return app
