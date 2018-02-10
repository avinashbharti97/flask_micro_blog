#blog.py - controller


#imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xfas\x1c\xc0\xae\x1d\x95 \x06\xe7\xa7\nn\x1e\xb2\xfc&\xcb\xebZ\xdd\xec)\xbe'

app = Flask(__name__)

#pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__) 

#function used for connecting the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#login required function
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('you need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please Try again'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error = error), status_code

@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title= row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html',posts = posts)

#add post function
@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    posts = request.form['posts']
    if not title or not posts:
        flash('all fields are required')
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('insert into posts (title, posts) values(?, ?)', [request.form['title'], request.form['posts']])
        g.db.commit()
        g.db.close()
        flash('new entry was successfully posted')
        return redirect(url_for('main'))
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you were logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
