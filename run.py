# coding:utf-8
from flask import Flask

from server import register_api as server_api
from portal import register_api as portal_api


if __name__ == '__main__':
    app = Flask(__name__)
    server_api.register(app)
    portal_api.register(app)
    app.run(debug=True, port=8080, host="0.0.0.0")
