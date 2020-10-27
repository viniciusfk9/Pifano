import pytest
from pifano.app import create_app
from pifano.external.models import User


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_context = app.test_request_context()
    app_context.push()

    return app


@pytest.fixture
def db(app):
    with app.app_context():
        app.db.create_all()

        yield app.db

        app.db.session.remove()
        app.db.drop_all()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        app.db.session.add(
            User(name='test', password='test', email='test@test'))

        yield client
