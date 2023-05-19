from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)


from .home.views import home_blueprint
from .user.views import user_blueprint
from .person.views import person_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(person_blueprint)

from blog import views