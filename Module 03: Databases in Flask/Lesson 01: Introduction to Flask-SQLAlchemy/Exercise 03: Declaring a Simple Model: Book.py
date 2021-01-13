# The database object created contains all the functions and helpers from
# both SQLAlchemy and SQLAlchemy Object Relational Mapper (ORM).

# SQLAlchemy ORM: Associates user created classes with database tables,
# and instances of those classes (objects) with rows in their corresponding tables. 

# Models: Classes that mirror the database tables.

# class Book(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)

# Column Parameters:
# * String(N), where N is the maximum number of characters
# * Integer, representing a whole number
# * unique: when True, the values in the column must be unique
# * index: whenTrue, the column is searchable by its values
# * primary_key: when True, the column serves as the primary key

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warnings
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    title = db.Column(db.String(80), index = True, unique = True) # book title
    #Checkpoint #1: insert your code here
    author_name = db.Column(db.String(50), index=True, unique=False)
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of book suggestion
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)


@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just made your first Flask-SQLAlchemy model declaration!"
