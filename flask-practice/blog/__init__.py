from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app=app, db=db)

    login.init_app(app=app)
    login.login_view = 'user.login'

    from blog.api import api_blueprint
    from .views import root_blueprint
    from .home.views import home_blueprint
    from .user.views import user_blueprint
    from .person.views import person_blueprint

    app.register_blueprint(api_blueprint)
    app.register_blueprint(root_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(person_blueprint)

    return app

from blog import views