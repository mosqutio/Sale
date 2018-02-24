from flask import Blueprint
from flask import render_template

common = Blueprint("common", __name__,
                   template_folder="templates",
                   static_folder="static",
                   url_prefix="/common"
                   )


@common.route("/home")
def home():
    return render_template('home.html', title_name='Sale Manager')
