from flask import Flask, abort
from markupsafe import escape

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/index/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h1>This is a Flask Web applications.</h1>'

@app.route('/capitalize/<word>')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))
@app.route('/add/<int:n1>/<int:n2>')
def add(n1, n2):
    return '<h1>{}</h1>'.format(escape(n1 + n2))

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bod','Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)