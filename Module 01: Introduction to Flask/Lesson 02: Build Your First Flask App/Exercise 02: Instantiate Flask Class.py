# flask: Python module that contains all the classes and functions needed for building a Flask app

# When creating a Flask object, we need to pass in the name of the application using the special Python variable __name__.

# The value of __name__ depends on how the Python script is executed.
# If we run a Python script directly, such as with python app.py in the terminal,
# then __name__ is equal to the string '__main__'.
# If the script is being imported as a module into another Python script,
# then __name__ would be equal to its filename.

# Import flask
from flask import Flask

# Create instance of Flask and save to app
app = Flask(__name__)

# Print __name__
print(__name__)
