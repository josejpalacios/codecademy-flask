# /<variable_name>/: When binding a URL path to a view function, makes any section of the path between slashs variable.
# These variable parts are then passed to the view function

# <converter:variable_name>: Optionally used to enforce the type of variable being accepted
# string => accepts any text without a slash (default)
# int => accepts positive integers
# float => accepts positive floating point values
# path => like string but also accepts slashes
# uuid => accepts UUID strings

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'

# Update path with variable
@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return '''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''.format(reporter_id=reporter_id)
