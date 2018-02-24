from server.db import db_api
from server.api.view.exhibition import exhibition_to_dict
from flask import jsonify
from flask import request
from server.api.base import BaseResource


class Exhibition(BaseResource):
    resource_name = "exhibitions"

    def __init__(self):
        super(Exhibition, self).__init__()

    def create(self):
        args = request.args

        return jsonify(args)

    def list(self):
        start_time = request.args.get("start_time")
        end_time = request.args.get("end_time")
        limit = request.args.get("limit", 100)
        offset = request.args.get("offset", 0)
        filters = {
            "start_time": start_time,
            "end_time": end_time,
            "limit": limit,
            "offset": offset,
        }
        exhibitions = db_api.list_exhibitions(**filters)
        return jsonify({"exhibitions": exhibition_to_dict(exhibitions)})

    def get(self, obj_id):
        return "kkk" + obj_id

# exhibition = Exhibition()
# print("user.resource_name", exhibition.resource_name)


def register_api(app):
    exhibition = Exhibition()
    app.add_url_rule("/exhibitions/<obj_id>", endpoint=exhibition.resource_name + "_get", methods=['GET'],
                     view_func=exhibition.get)
    app.add_url_rule("/exhibitions", endpoint=exhibition.resource_name + "_list", methods=['GET'],
                     view_func=exhibition.list)
    app.add_url_rule("/exhibitions", endpoint=exhibition.resource_name + "_create", methods=['POST'],
                     view_func=exhibition.create)
