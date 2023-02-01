import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sys


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_member_byid(member_id):
    conn = get_db_connection()
    member = conn.execute('SELECT * FROM members WHERE idnum = ?',
                        (member_id,)).fetchone()
    conn.close()
    if type(member) == 'NoneType':
        print("No data found")
        abort(404)
    if member is None:
        flash('No team member with that ID exists')
    else:
        for i in member:
            app.logger.warning("   member information: %s", i)

    return member

def get_member_byname(name):
    conn = get_db_connection()
    member = conn.execute("SELECT * FROM members WHERE last_name like '%?%'",
                     (last_name,)).fetchone()
    conn.close()
    if member is None:
        abort(404)
    return member

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = dict(request.form)
        svalues = data.values()
        app.logger.warning("Posting to index method, Id number input is %s", data['idnum'])
        user = get_member_byid(data['idnum'])
        app.logger.warning("return from memberid %s", user[3])
    conn = get_db_connection()
    members = conn.execute("SELECT * FROM members WHERE status = 'IN' ").fetchall()
    conn.close()
    return render_template('index.html', members=members)

if __name__ == "__main__":
    app.run()

