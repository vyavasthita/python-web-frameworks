from flask.blueprints import Blueprint
from flask import render_template


person_blueprint = Blueprint('person', __name__, template_folder='templates')


@person_blueprint.route("/person")
def home():
    persons = ['Samskriti', 'Sabhyata']
    return render_template('home.html', users = persons)