from flask import Flask, render_template
# Task 1: import SQLALchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Task 2: set the SQLALCHEMY_DATABASE_URI key
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///song_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
# Task 3: create an SQLAlchemy object named `db` and bind it to your app
db = SQLAlchemy(app)

#a simple initial greeting
@app.route('/')
@app.route('/index')
def greeting():
    return render_template('greeting.html')

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

# Task 13: in terminal, import db from app;import all the classes from models.py; initialize the database using create_all()

# Task 14: in terminal, run add_data.py

#Task 15: uncomment the code below here when you are done creating database instance db and models
import routes
