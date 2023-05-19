from flask.blueprints import Blueprint
from flask import render_template
from .dao import user_dao


user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route("/user")
def home():
    users = ['Dilip', 'Bhoomi']
    user_dao.create_user("bhoomi", "vijayapur")
    return render_template('home.html', users = users)