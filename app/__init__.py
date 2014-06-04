# -*- coding: utf-8 -*-

#from app import app, models
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models 

