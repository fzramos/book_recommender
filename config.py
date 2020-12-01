import os

basedir = os.path.abspath(os.path.dirname(__file__))

# secret key for the encrytion of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mamamia King Bowser..'
    SQALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False