from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, request
from .dao import user_dao
from blog.user.forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.user_logged_in'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        user_dao.register_user(form.name.data, form.username.data, form.password.data)
        return redirect(url_for('user.user_registered'))
    
    return render_template('user_registration.html', form=form)

@user_blueprint.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.user_logged_in'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = user_dao.get_user(form.username.data)

        if not user or not user.verify_password(form.password.data):
            return redirect(url_for('user.login'))
         
        login_user(user=user)
        next_page = request.args.get('next')
        
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('user.login')
        
        return redirect(url_for('user.user_logged_in'))

    return render_template('user_login.html', form=form)

@user_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@user_blueprint.route("/user_created")
@login_required
def user_registered():
    return render_template('user_registered.html')

@user_blueprint.route("/user_logged_in")
@login_required
def user_logged_in():
    return render_template('post_login.html')

@user_blueprint.route("/list_users")
def list_users():
    users = user_dao.get_all_users()
    return render_template('list_users.html', users = users)