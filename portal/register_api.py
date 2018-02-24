# coding:utf-8
from flask import render_template, redirect
from flask import url_for
# from flask_bootstrap import Bootstrap
# from flask_nav import Nav
# from flask_nav.elements import *
from .views.common import view as common_view
from .views.exhibition import view as exhibition_view
from .views.users import view as user_view
# nav = Nav()
# nav.register_element(
#     'top',
#     Navbar(
#         u'展会管理中心',
#         View(u'主页', 'common.home'),
#         # View(u'展会管理', 'common.home'),
#         Subgroup(u'展会管理',
#                  View(u'查看', 'exhibition.test'),
#                  Separator(),
#                  View(u'创建', 'exhibition.index'),
#                  ),
#         View(u'人员管理', 'exhibition.test3'),
#         # View(u'物料管理', 'common.about'),
#         # View(u'商品管理', 'common.about'),
#         # View(u'费用管理', 'common.about'),
#         # View(u'关于', 'about'),
#         # View(u'统计图表', 'common.about'),
#     ),
# )


def redirect_to_home():
    return redirect(url_for("common.home"))


def register(app):
    # Bootstrap(app)
    # nav.init_app(app)
    app.register_blueprint(common_view.common)
    app.register_blueprint(exhibition_view.exhitibion)
    app.register_blueprint(user_view.user)

    # Bootstrap(app)
    app.route("/")(redirect_to_home)
    # app.route("/index")(index)
    # app.route("/about")(about)
