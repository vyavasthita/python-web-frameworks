from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for
from .dao import user_dao
from blog.user.forms import UserForm


user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route("/user", methods = ['GET', 'POST'])
def home():
    form = UserForm()

    if form.validate_on_submit():
        name = form.name.data
        city = form.city.data

        user_dao.create_user(name, city)
        return redirect(url_for('user.user_created'))
    
    return render_template('user_home.html', form=form)

@user_blueprint.route("/user_created")
def user_created():
    return render_template('user_created.html')