from app.__init__ import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app.__init__ import db, login
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    deadline = db.Column(db.DateTime)
    complete = db.Column(db.String(20), default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    
    def __repr__(self):
        return f'<Task {self.title}>'
    # def to_dic(self):
    #     return{
    #         'id': self.id,
    #         'name': self.name,
    #         'description':self.description,
    #         'deadline': self.deadline.isoformat() if self.deadline else None,
    #         'status': self.status
    #     }

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150),nullable=False)
    tasks = db.relationship('Task',backref='author',lazy=True)

    def __repr(self):
        return f'<User {self.username}>'
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    tasks = db.relationship('Task',backref='category',lazy=True)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))