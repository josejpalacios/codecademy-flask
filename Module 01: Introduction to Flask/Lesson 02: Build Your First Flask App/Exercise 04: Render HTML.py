# Response from view function can also return HTML to be rendered on a webpage
from flask import Flask

# Can also use triple quotes to contain multi-line code
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    # Add <h1> tag to return value
    return '<h1>Hello, World!</h1>'


@app.route('/reporter')
def reporter():
    # Add <h2> tag to return value. Add <a> tag to return value
    return """
    <h2>Reporter Bio</h2>
    <a href='/'>Return to home page</a>
    """
