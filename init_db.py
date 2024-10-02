# init_db.py
import sqlite3

# open a connection between python script and database.db to create it 
connection = sqlite3.connect('database.db')

# open the schema.sql to read what inside it
with open('schema.sql') as f:
    connection.executescript(f.read())

# make the cursor to execute what inside the schema in database
cur = connection.cursor()

cur.execute("INSERT INTO tickets (title, content) VALUES (?, ?)",
            ('First Ticket', 'Content for the first ticket')
            )

cur.execute("INSERT INTO tickets (title, content) VALUES (?, ?)",
            ('Second Ticket', 'Content for the second ticket')
            )

connection.commit()
connection.close()