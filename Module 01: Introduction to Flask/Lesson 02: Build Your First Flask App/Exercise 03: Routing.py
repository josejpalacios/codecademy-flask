# Routing: Requests from different URLs directed to different endpoints

# view function: contains the code for processing the request and generating a response

# route(): bind a URL to the view function such that the function will be triggered when the URL is visited

# Multiple URLs can also be bound to the same view function:
from flask import Flask

app = Flask(__name__)

# Create home() function. Bind to URL path using route()
@app.route('/')
# Bind another URL path to home()
@app.route('/home')
def home():
  return 'Hello, World!'

# Create reporter() function. Bind to URL path using /reporter
@app.route('/reporter')
def reporter():
  return 'Reporter Bio'
