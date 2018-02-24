from flask import jsonify
from .base import BaseResource


class User(BaseResource):
    resource_name = "users"

    def __init__(self):
        super(User, self).__init__()

    def get(self, obj_id):
        return "user_id", obj_id

    def list(self):
        return jsonify([])

    def create(self):
        return jsonify([])


# user = User()
# print("user.resource_name", user.resource_name)

def register_api(app):
    user = User()
    app.add_url_rule("/users/<obj_id>", endpoint=user.resource_name + "_get", methods=['GET'],
                     view_func=user.get)
    app.add_url_rule("/users", endpoint=user.resource_name + "_list", methods=['GET'],
                     view_func=user.list)
    app.add_url_rule("/users", endpoint=user.resource_name + "_create", methods=['POST'],
                     view_func=user.create)
