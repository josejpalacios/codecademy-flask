# Learned:
# - Import Flask class
# - Create Flask application object
# - Create routes for handling requests from different URLs
# - Create variable rules to handle dynamic URLS

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'


@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

# Create third view function. Add <article_name> to URL path
@app.route('/article/<article_name>')
# Add article_name to article function
def article(article_name):
    return """
    <h2>{article_name.replace('-', ' ').title()}</h2>
    <a href="/">Return back to home page</a>
    """
