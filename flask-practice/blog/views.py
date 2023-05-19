from flask import render_template
from flask.blueprints import Blueprint


root_blueprint = Blueprint('root', __name__)
@root_blueprint.route("/")
def root():
    return render_template('index.html')
