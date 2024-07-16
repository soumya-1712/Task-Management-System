import os

class Config:
    SECRET_KEY = os.environ.get('secretkey') or 'secretkeystring'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/task_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
