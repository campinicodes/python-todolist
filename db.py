import sqlite3

conn = sqlite3.connect('todo.db')

cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    )'''
)

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    created_at DATETIME,
    completed BOOLEAN DEFAULT 0,
    reccurrent BOOLEAN DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
    )'''
)

conn.commit()
conn.close()

def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn