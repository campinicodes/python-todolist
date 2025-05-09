from flask import session, redirect, url_for, flash
from db import get_db_connection

def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user['password'] == password:
        session.permanent = True
        session['user_id'] = user['id']
        session['username'] = user['username']
        return True
    return False

def logout_user():
    session.clear()

def is_logged():
    return 'user_id' in session

def require_login():
    if not is_logged():
        flash('Usuário não logado.')
        return redirect(url_for('login'))

def get_user_id():
    return session.get('user_id')