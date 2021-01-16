# Protecting pages is the primary objective of authentication.

# LoginManagers have a method user_loader that needs to be defined in order to load and verify a user from our database.

# @login_manager.user_loader
# def load_user(id):
#      return User.query.get(int(id))
# without this function, can't be able to verify users on protected routes.

# Will also have to import the login_required function from flask_login
# This allows the use of @login_required function as a decorator.
# The @login_required decorator will force the user to login before being able to view the page.

import flask
from flask_sqlalchemy import SQLAlchemy
# import login_required here:
from flask_login import login_required
from flask_login import LoginManager, UserMixin
from flask import request, render_template, flash, redirect,url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = flask.Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password) 

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
    
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
# add login_required decorator here:
@login_required
def home():
	return render_template('logged_in.html')
