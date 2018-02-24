from flask import Blueprint
from flask import render_template

user = Blueprint("user", __name__,
                 template_folder="templates",
                 static_folder="static",
                 url_prefix="/user")


@user.route("/list")
def index():
    return render_template('list.html', exhibitions=[],
                           title_name='Sale Manager')


@user.route("/add")
def create():
    return render_template("create.html", title_name='Sale Manager')
