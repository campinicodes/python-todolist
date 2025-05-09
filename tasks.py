import sqlite3
import session
from db import get_db_connection

get_db_connection()

def get_tasks():
    conn = get_db_connection()
    user_id = session.get_user_id()
    tasks = conn.execute('SELECT * FROM tasks where user_id = ? ORDER BY completed, due_date', (user_id)).fetchall()
    conn.close()
    return tasks

def add_task(title, due_date, reccurrent, description):
    conn = get_db_connection()
    user_id = session.get_user_id()
    conn.execute('INSERT INTO tasks (user_id, title, due_date, reccurrent, description) VALUES (?, ?, ?, ?, ?)' , (user_id, title, due_date, reccurrent, description))
    conn.commit()
    conn.close()

def complete_task(task_id):
    conn = get_db_connection()
    user_id = session.get_user_id()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id))
    conn.commit()
    conn.close()

def edit_task(title, due_date, reccurrent, description, task_id):
    conn = get_db_connection()
    user_id = session.get_user_id()
    conn.execute('UPDATE tasks SET title = ?, due_date = ?, reccurrent = ?, description = ? WHERE id = ?', (title, due_date, reccurrent, description, task_id))

def delete_task(task_id):
    conn = get_db_connection()
    user_id = session.get_user_id()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id))
    conn.commit()
    conn.close()