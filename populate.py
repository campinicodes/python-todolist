import sqlite3

conn = sqlite3.connect('todo.db')
conn.row_factory = sqlite3.Row
conn.execute(''' 
            INSERT INTO tasks(user_id, title, description, due_date, created_at, completed, reccurrent) VALUES (?, ?, ?, ?, ?, ?, ?)
             ''', (1, 'Tare', 'Dteste', '2025-05-16', '2025-05-12', 0, 1))
conn.commit()
conn.close()