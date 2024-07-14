from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config
from app import routes
import app.routes


db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'


@login.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login.__init__(app)

    from app.routes import main
    app.register_blueprint(main)


    return app 
