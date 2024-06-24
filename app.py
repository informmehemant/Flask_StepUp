from flask import Flask, render_template, redirect, url_for
from forms import CoursesForm
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


# @app.route('/', methods=('GET', 'POST'))
# def index():
#     form = CoursesForm()
#     if form.validate_on_submit():
#         courses_list.append({
#             'title': form.title.data,
#             'description': form.description.data,
#             'price': form.price.data,
#             'available': form.available.data,
#             'level': form.level.data
#         })
#         return redirect(url_for('courses'))
#     return render_template('index.html', form=form)

# @app.route('/courses')
# def courses():
#     return render_template('courses.html', courses_list=courses_list)
