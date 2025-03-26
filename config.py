from os import environ, path
# from dotenv import load_dotenv

# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Flask Config
    SECRET_KEY = 'asdfasdfasdfasdfasdfasdfasdf'#environ.get('SECRET_KEY')
    FLASK_APP = 'wsgi.py'
    FLASK_DEBUG = 1
    JSON_AS_ASCII = False

    # image upload configs
    UPLOAD_FOLDER = 'static/profile_pics'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning