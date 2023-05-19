from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app=app, db=db)

    from .views import root_blueprint
    from .home.views import home_blueprint
    from .user.views import user_blueprint
    from .person.views import person_blueprint

    app.register_blueprint(root_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(person_blueprint)

    return app

from blog import views