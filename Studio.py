import sqlite3

import Admins


class Studio:
    def __init__(self, db_name="soundstudio.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS studio (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT not null,
                        room INTEGER not null,
                        microphone TEXT,
                        headphones TEXT,
                        software TEXT
                    )
                ''')
        self.conn.commit()

    def add(self, id, name, room, microphone, headphones, software):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO studio (id, name, room, microphone, headphones, software ) VALUES (?, ?, ?, ?, ?, ?)',
                       (id, name, room, microphone, headphones, software))
        self.conn.commit()
        print(f"Студия добавлена!\nid:{id},\nимя:{name},\nномер комнаты:{room},\nмикрофон:{microphone},\nнаушники:{headphones},\nПО:{software}")
    def update(self, sid,id, name, room, microphone, headphones, software):

        cursor = self.conn.cursor()
        cursor.execute('UPDATE studio SET id=?, name=?, room=?, microphone=?, headphones=?, software=? WHERE id=?',
                       (id, name, room, microphone, headphones, software, sid))
        self.conn.commit()


    def delete(self, sid):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM studio WHERE id=?', (sid,))
        self.conn.commit()

    def read(self, id=None):
        cursor = self.conn.cursor()
        if id is not None:
            cursor.execute('SELECT * FROM studio WHERE id=?', (id,))
        else:
            cursor.execute('SELECT * FROM studio')
        return cursor.fetchall()
    def close(self):
        self.conn.close()