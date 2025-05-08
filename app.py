from flask import Flask, request, redirect, render_template
import sqlite3
from session import login_user, logout_user, is_logged
from datetime import timedelta
from db import get_db_connection

app = Flask(__name__)

app.secret_key = '3fs09djsjdfj3409fdf93409dkfj9340'
app.permanent_session_lifetime = timedelta(days=30)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return 'Nome de usuário já existente', 409 #TODO: inserir aviso javascript
        
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if login_user(username, password):
            return redirect('/tasks')
        else:
            return 'Credenciais incorretas', 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/tasks')
def tasks():
    if not is_logged():
        return redirect('/login')
    return render_template('tasks.html')

if __name__ == '__main__':
    app.run(debug=True)