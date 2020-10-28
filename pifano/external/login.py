from flask_login import LoginManager
from pifano.external.models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def configure(app):
    """ Adds Flask-Login to app """
    login_manager.init_app(app)
