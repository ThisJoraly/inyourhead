import sqlite3


class User:
    def __init__(self, db_name="soundstudio.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password, role):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
        self.conn.commit()

    def auth_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, username, password, role FROM users WHERE username=? AND password=?',
                       (username, password))
        result = cursor.fetchone()
        return result[0] if result else None

    def update_user_data(self, user_id, new_data):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE users SET username=?, password=? WHERE id=?',
                       (new_data['username'], new_data['password'], user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
        self.conn.commit()

    def read_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    def get_role(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT role FROM users WHERE id=?', (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def close_connection(self):
        self.conn.close()