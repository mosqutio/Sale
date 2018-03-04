from . import base
from . import exhibition
from . import user


def register_api(app):
    for o in base.all_object:
        o.register_api(app)
