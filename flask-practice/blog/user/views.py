from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for
from .dao import user_dao
from blog.user.forms import UserLogin, UserRegistration


user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route("/sign_up", methods = ['GET', 'POST'])
def sign_up():
    form = UserRegistration()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data

        user_dao.register_user(name, username, password)
        return redirect(url_for('user.user_registered'))
    
    return render_template('user_registration.html', form=form)

@user_blueprint.route("/sign_in", methods = ['GET', 'POST'])
def sign_in():
    form = UserLogin()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = user_dao.get_user(username)

        if user is None:
            pass

        if user.verify_password(password):
            return redirect(url_for('user.user_logged_in'))
    
    return render_template('user_login.html', form=form)

@user_blueprint.route("/user_created")
def user_registered():
    return render_template('user_registered.html')

@user_blueprint.route("/user_logged_in")
def user_logged_in():
    return render_template('post_login.html')

@user_blueprint.route("/list_users")
def list_users():
    users = user_dao.get_all_users()
    return render_template('list_users.html', users = users)