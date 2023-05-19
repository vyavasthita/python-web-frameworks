import os


base_dir = os.path.abspath(os.path.dirname(__name__))


class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_DB_URI') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_DB = os.environ.get('MYSQL_DB')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_DB_URI') or \
        "mysql://" + MYSQL_USER + ":" + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/" + MYSQL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somesecretkey'

