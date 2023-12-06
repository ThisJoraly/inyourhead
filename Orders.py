import sqlite3

class Order:
    def __init__(self, db_name="soundstudio.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        minutes INTEGER NOT NULL,
                        cost REAL NOT NULL,
                        description TEXT NOT NULL,
                        date TEXT NOT NULL,
                        user_id INTEGER,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                    )
                ''')
        self.conn.commit()

    def add(self, user_id, date, description, cost, minutes):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO orders (user_id, date, description, cost, minutes) VALUES (?, ?, ?, ?, ?)',
                       (user_id, date, description, cost, minutes))
        self.conn.commit()
        print(f"\nВаш заказ (Дата {date}, Пожелания: {description}, Цена: {cost}, Время в минутах: {minutes})")


    def delete(self, oid):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM orders WHERE id=?', (oid,))
        self.conn.commit()

    def filter(self, user_id=None, date=None):
        cursor = self.conn.cursor()
        if user_id is not None:
            cursor.execute('SELECT * FROM orders WHERE user_id=?', (user_id,))
        elif date is not None:
            cursor.execute('SELECT * FROM orders WHERE date=?', (date,))
        else:
            cursor.execute('SELECT * FROM orders')
        return cursor.fetchall()

    def close(self):
        self.conn.close()