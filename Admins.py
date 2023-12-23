import sqlite3
class Admin:
    def __init__(self, db_name="soundstudio.db", admin_password="123"):
        self.conn = sqlite3.connect(db_name)
        self.admin_password = admin_password

    def auth_password(self, input_password):
        return input_password == self.admin_password


    def update_user_data(self, u, admin_password, uid, new_data):
        if not self.auth_password(admin_password):
            print("Неверный мастер-пароль.")
            return

        u.update_user_data(uid, new_data)
        print(f"Пользователь с ID:{uid} был успешно обновлен.")

    def update(self, admin_password, oid, date, table_number, price):
        if not self.auth_password(admin_password):
            print("Неверный мастер-пароль.")
            return

        cursor = self.conn.cursor()
        cursor.execute('UPDATE orders SET date=?, table_number=?, price=? WHERE id=?',
                       (date, table_number, price, oid))
        self.conn.commit()

    def delete_user(self, u, admin_password, uid):
        if not self.auth_password(admin_password):
            print("Неверный мастер-пароль.")
            return

        u.delete_user(uid)
        print(f"Пользователь с ID:{uid} был удален.")

    def view_all_users(self, u, admin_password):
        if not self.auth_password(admin_password):
            print("Неверный мастер-пароль.")
            return

        users = u.view_all_users()
        print("Все пользователи:")
        for user in users:
            print(user)

    def close_connection(self):
        self.conn.close()