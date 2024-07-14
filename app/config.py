import os

class Config:
    SECRET_KEY = os.environ.get('accha69420') or 'accha69420'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://soumya:soumya1712@localhost/task_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


