from flask import Blueprint, request, jsonify, current_app as app
from pifano.external.models import User

bp_user = Blueprint('user', __name__)


@bp_user.route('/users', methods=['POST'])
def add_user():
    if request.method == 'POST':
        if request.is_json:
            json_data = request.get_json()

            new_user = User(name=json_data['name'],
                            email=json_data['email'],
                            password=json_data['password'])

            if User.query.filter_by(email=new_user.email).first():
                data = {"message": "Email already registered."}
            else:
                app.db.session.add(new_user)
                app.db.session.commit()

                data = {
                    "message":
                    f"User {new_user.name} has been created successfully."
                }

        else:
            data = {"error": "The request payload is not in JSON format"}
    else:
        data = {"error": "POST request"}

    return jsonify(data)


@bp_user.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    users_data = [{
        "id": user.id,
        "name": user.name,
        "email": user.email
    } for user in users]

    data = {"count": len(users_data), "users": users_data}

    return jsonify(data)
