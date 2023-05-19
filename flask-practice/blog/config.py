import os


base_dir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_DB_URI') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somesecretkey'