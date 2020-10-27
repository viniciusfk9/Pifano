from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    """ Adds SQLAlchemy extension to app """
    db.init_app(app)
    app.db = db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"
