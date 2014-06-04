import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost/swamperdb'

CSRF_ENABLED = True  # this is to prevent CSRF attacks
SECRET_KEY = 'big-secret'
