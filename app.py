from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#import mariadb
#import sys

#DB setting
#def get_db():
##Connect with db
#    try:
#        conn = mariadb.connect(
#            user="FLASK_USER",
#            password="FLASK_PASSWORD",
#            host="localhost",
#            port=3306,
#            database="flask_db"
#        )
#    except mariadb.Error as e:
#        print(f"Error connecting to MariaDB Platform: {e}")
#        sys.exit(1)
##Get cursor
#   db = conn.cursor()
#   return db

#def close_db():
#    conn.close()

app = Flask(__name__)

@app.route("/hello")
def homepage():
    return "Hello World"

@app.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
#            try:
#                db.execute(
#                    "INSERT INTO users (username, password) VALUES (?, ?)",
#                    (username, generate_password_hash(password)),
#                )
#            except mariadb.Error as e:
#                print(f"Error: {e}")
#                error = f"User {username} is already registered."
#            else:
#                print("Successful registration")
#                return redirect(url_for("hello"))
            return redirect("/hello")
        flash(error)


    return render_template('register.html')