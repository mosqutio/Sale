from server import api
# from server.api.exhibition import exhibition
# from server.api import exhibition
# from server.api.user import user
# from server.api import user


def register(app):
    api.register_api(app)
    # app.route("/users", endpoint="user_list", method=[])(user.list)
    # app.route("/exhibitions", endpoint="exhibition_list")(exhibition.list)
    # exhibition.register_api(app)
    # user.register_api(app)
