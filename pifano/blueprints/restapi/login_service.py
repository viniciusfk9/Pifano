from flask import Blueprint, jsonify, request
from pifano.external.models import User
from flask_login import login_user, logout_user

bp_login = Blueprint('login', __name__)


@bp_login.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            data = {'message': "Username or password is invalid"}
        else:
            login_user(user)

            data = {'message': "User successfully logged in"}
    else:
        data = {'message': "POST request"}

    return jsonify(data)


@bp_login.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()

    return jsonify({'message': "User successfully logged out"})
