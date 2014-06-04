#creats the datbase on the models defined in models.py 

from config import SQLALCHEMY_DATABASE_URI
from app import db 
db.create_all()