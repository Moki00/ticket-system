# Import modules
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY']='your secret key'

# Connect to Database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get ticket
def get_ticket(ticket_id):
    conn = get_db_connection()
    # SELECT the ticket based on its ID
    ticket = conn.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()
    conn.close()
    # Do we have the ticket or 404?
    if ticket is None:
        abort(404)
    return ticket

# Main page
@app.route('/')
def index():
    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets').fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)

# # See a ticket
# @app.route('/<int:ticket_id>')
# def ticket(ticket_id):
#     #user clicks and saves value in 'ticket' var
#     ticket = get_ticket(ticket_id)
#     # render the ticket page in the html
#     return render_template('ticket.html', ticket=ticket)

# # Create tickets
# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     # if user clicks Submit
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         if not title:
#             flash('Title is required!')
#         elif not content:
#             flash('Content is required')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO tickets (title, content) VALUES (?, ?)', (title, content))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#     return render_template('create.html')

# # Edit tickets
# @app.route('/<int:id>/edit', methods=('GET', 'POST'))
# def edit(id):
#     # get the ticket by id
#     ticket = get_ticket(id)

#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         if not title:
#             flash('Title is required!')
#         elif not content:
#             flash('Content is required')
#         else:
#             conn = get_db_connection()
#             # UPDATE has to be like below
#             conn.execute('UPDATE tickets SET title = ?, content = ?', 'WHERE id = ?' , (title, content, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#     return render_template('edit.html', ticket=ticket)

# @app.route('/<int:id>/delete', methods=('POST',))
# def delete(id):
#     ticket = get_ticket(id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM tickets WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     flash('"{}" was successfully deleted.'.format(ticket['title']))
#     return redirect(url_for('index'))

