import os 
import psycopg2
conn = psycopg2.connect(
    host='localhost', 
    database='flask_db', 
    port=5432, user = os.environ['DB_USER'], 
    password = os.environ['DB_PASS']
    )
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this create a new table

cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
            'title varchar(150) NOT  NULL,'
            'author varchar(50) NOT NULL,'
            'pages_num integer NOT NULL,'
            'review text,'
            'data_added date DEFAULT CURRENT_TIMESTAMP);'
            )

#INSERT data into the table 
cur.execute('INSERT INTO books (title, author, pages_num, review) VALUES (%s, %s, %s, %s)',
            ('The Hobbit', 'J.R.R.Tolkien', 295, 'Amazing book!'))
cur.execute('INSERT INTO books (title, author, pages_num, review) VALUES (%s, %s, %s, %s)',
            ('The Lord of the Rings', 'J.R.R.Tolkien', 1138, 'Amazing book!'))
conn.commit()
cur.close()
conn.close()



