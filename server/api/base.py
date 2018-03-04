# from . import exhibition

all_object = []


class BaseResource(object):

    methods = [
        ('get', "GET"),
        ('create', "POST"),
        ('delete', "DELETE"),
        ('list', "GET"),
        ('update', "PUT")
    ]

    def __init__(self):
        # pass
        # print(self)
        all_object.append(self)
        print(all_object)

    @property
    def resource_name(self):
        raise NotImplemented("not implemented")

    def get(self, obj_id):
        raise NotImplemented("not implemented")

    def create(self):
        raise NotImplemented("not implemented")

    def delete(self, obj_id):
        raise NotImplemented("not implemented")

    def list(self):
        raise NotImplemented("not implemented")

    def update(self, obj_id):
        raise NotImplemented("not implemented")

    @staticmethod
    def _get(obj_id):
        return

    def register_api(self, app):
        for func, method in self.methods:
            url = "/" + self.resource_name + ("/<obj_id>" if func in ("get", "delete", "update") else "")
            endpoint = "".join(
                [
                    self.resource_name,
                    "_",
                    func
                ]
            )
            # print(endpoint, url, method)
            app.add_url_rule(url, endpoint=endpoint, methods=[method.upper()], view_func=getattr(self, func))

        # url = "/" + self.resource_name
        # rest_api_func = [self.get, self.create, self.delete, self.list, self.update]
        # for func in rest_api_func:
        #     endpoint = self.resource_name + "_" + func.__name__
        #     if func.__name__.lower() in ("get", "delete", "update"):
        #         url += '/<int:obj_id>'
        #     print(endpoint)
        #     # app.route(url, endpoint=endpoint, methods=[func.__name__.upper()])(func)
        #     app.add_url_rule(url, endpoint=endpoint, methods=[func.__name__.upper()], view_func=func)


# def register_api(app):
#     for o in all_object:
#         o.register_api(app)
