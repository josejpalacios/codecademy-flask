# When a user tries to access protected pages without logging in or encounters an error upon login,
# its best to communicate this to the user.

# Can catch authorization issues by adding a new route or endpoint with the @login_manager.unauthorized_handler decorator

# the @login_manager.unauthorized_handler decorator ensures that any time there is an authorization issue,
# the unauthorized() route is called

import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from flask import request, render_template, flash, redirect,url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = flask.Flask(__name__)
app.secret_key = 'secretkeyhardcoded'
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
@login_required
def home():
	return render_template('logged_in.html')

# add a decorator here to handle unauthorized users:
@login_manager.unauthorized_handler
def unauthorized():
  # do stuff
  return "Sorry you must be logged in to view this page"
