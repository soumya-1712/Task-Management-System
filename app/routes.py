from flask import render_template, request, jsonify, redirect, Blueprint, flash, url_for
from app.__init__ import db
# from app import app
from app.models import User,Task,Category
from datetime import datetime
from flask_login import login_required, current_user, login_user, logout_user, login_required 
# from werkzeug.urls import url_for
from flask import url_for
from app.forms import LoginForm, RegistrationForm, TaskForm
from app.__init__ import create_app
from urllib.parse import urlparse

main = Blueprint('main',__name__)



# app = create_app()
# app = Flask(__name__)

@main.route('/')
@main.route('/index')
@login_required
def index():
    categories = Category.query.filter_by(user_id=current_user.id).all()
    selected_category = request.args.get('category','my-task')
    if selected_category == 'my-task':
        tasks = Task.query.filter_by(user_id=current_user.id, category_id=1).all()
    else:
        category = Category.query.filter_by(name=selected_category,user_id=current_user.id).first()
        tasks = category.tasks if category else[]
    # tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks,categories=categories,selected_category=selected_category)


@main.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc !='':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@main.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@main.route('/add_task', methods=['GET','POST'])
# @login_required
def add_task():
    try:
        form = TaskForm()
        if form.validate_on_submit():
            task = Task(title=form.title.data, description=form.description.data, deadline=form.deadline.data, user_id=current_user.id,category_id=form.category.data)
            db.session.add(task)
            db.session.commit()
            flash('Task added successfully!')
            return redirect(url_for('index'))
        return render_template('add_task.html',form=form)
    
        # name = request.form['name']
        # description = request.form.get('description','')
        # deadline_str = request.form.get('deadline',None)
        # status = request.form['status']
        # new_task = Task(name=name,description=description,deadline=deadline_str,status=status)
        # db.session.add(new_task)
        # db.session.commit()
        # return redirect('/')
    except Exception as e:
        print(f"Error adding task: {e}")
        db.session.rollback()  
        return redirect('/')

@main.route('/complete_task', methods=['POST'])
def complete_task():
    try:
        task_id = request.form.get('task_id')
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return redirect('/')
            # return jsonify()
        return jsonify({'error': 'Task not found'}), 404
    except Exception as e:
        print(f"Error completing task: {e}")
        db.session.rollback()  # Rollback the session in case of error
        # return redirect('/')
        return jsonify({'error': str(e)}), 500

@main.route('/api/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        data = request.json
        new_task = Task(
            title=data['title'],
            description=data['description'],
            deadline=data['deadline']
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task), 201

    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@main.route('/api/tasks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def task_detail(id):
    task = Task.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(task.to_dict())

    if request.method == 'PUT':
        data = request.json
        task.title = data['title']
        task.description = data['description']
        task.deadline = data['deadline']
        task.status = data['status']
        db.session.commit()
        return jsonify(task.to_dict())

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204