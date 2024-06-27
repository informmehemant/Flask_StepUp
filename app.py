from flask import Flask, render_template, request, url_for, redirect
import psycopg2
import os
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            port=5432, 
                            user = os.environ['DB_USER'], 
                            password = os.environ['DB_PASS']
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    return render_template('index.html', books=books)

@app.route('/create/', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = request.form['pages_num']
        review = request.form['review']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review) VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')
