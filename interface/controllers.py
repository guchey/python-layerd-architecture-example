from flask import Blueprint, abort, jsonify

from application.service import UserService

api = Blueprint("api", __name__)


@api.route("/user/<id>")
def get_user(id: str):
    service = UserService(id)
    user = service.get_user()
    if user:
        return jsonify(user.asdict())
    else:
        return jsonify({}), 404