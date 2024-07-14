from app import app
from flask import Flask, request, jsonify, render_template, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user


# app = Flask(__name__)
# app.config.from_pyfile('config.py')
db = SQLAlchemy(app)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)


main = Blueprint('main',__name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html',user=current_user)
