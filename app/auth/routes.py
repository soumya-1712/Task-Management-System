from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.auth import auth

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user() 
    return redirect(url_for('main.index'))
