from flask import Blueprint
from flask import render_template

exhitibion = Blueprint("exhibition", __name__,
                       template_folder="templates",
                       static_folder="static",
                       url_prefix="/exhibition")


@exhitibion.route("/list")
def index():
    return render_template('list.html', exhibitions=[], title_name='Sale Manager')


@exhitibion.route("/list_pic")
def show_pic():
    return render_template('list_pic.html')


@exhitibion.route("/create")
def create():
    return render_template("create.html", title_name='Sale Manager')
