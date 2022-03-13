from datetime import datetime
from email.policy import default
from . import db



class Quote:
    '''
    Class that defines quote 
    '''

    def __init__(self, author, quote_message):
        self.author = author 
        self.quote_message = quote_message 




class Admin(db.Model):
    '''
    Class that defines admin/writer priviledge
    Args: base class for all models from flask-sqlalchemy
    '''
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    blogs = db.relationship('Blog', backref='writter', lazy='dynamic')

    def __repr__(self):
        return f'Admin {self.username}'

class Blog(db.Model):
    '''
    class that instanciates blog posts
    '''
    __tablename__ = 'Blogs'
    id = db.Column(db.Integer, primary_key = True)
    blog_post = db.Column(db.String(140))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    timestamp = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'Blog {self.blog_post}'

class User(db.Model):
    '''
    Class that instanctiates users interactions
    '''
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index=True)
    comments = db.relationship('Comment', backref='writter', lazy=True)
    blogs = db.relationship('Blog', backref='writter', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):
    '''
    Class that instanciates comments made by users
    '''
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text())
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Comment {self.comment}'