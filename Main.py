import random
import sys


from Users import User
from Admins import Admin
from Orders import Order
from Studio import Studio
def main():
    u = User()
    # u - user
    # uid - user's id
    o = Order()
    # o - order
    # oid - order's id
    a = Admin()
    # a = admin
    s = Studio()
    # st - studio
    # sid - studio id

    while True:
        print("\nДобро пожаловать в приложение студии звукозаписи\n"
              +"1. Войти\n"+"2. Зарегистрироваться\n"+"3. Выйти")

        choice = input(">> ")

        if choice == "1":
            username = input("Введите логин: ")
            password = input("Введите пароль: ")

            user_id = u.auth_user(username, password)

            if user_id is not None:
                role = u.get_role(user_id)
                print(f"Добро пожаловать, {username}!")

                if role == "клиент":
                    handle_client_actions(user_id, u, o)
                elif role == "админ":
                    handle_admin_actions(u, a, o, s)
                else:
                    print("Неверная роль.")
            else:
                print("Извините, введите правильный логин или пароль.")

        elif choice == "2":
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            role = input("Введите свою роль (клиент, админ): ").lower()

            user_id = u.register_user(username, password, role)
            print(f"Добро пожаловать, {username}!")

            if role == "клиент":
                handle_client_actions(user_id, u, o)
            elif role == "админ":
                handle_admin_actions(u, a, o)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

    u.close_connection()
    o.close()
    a.close_connection()


def handle_client_actions(uid, u, o):
    while True:
        print("\nМеню пользователя:")
        print("1. Арендовать студию")
        print("2. Обновить данные аккаунта")
        print("3. Выйти")

        client_choice = input(">> ")

        if client_choice == "1":
            date = input("Введите дату (ГГГГ-ММ-ДД): ")
            description = str(input("Введите пожелания к записи: "))
            minutes = int(input("Введите на сколько минут у вас будет запись: "))
            cost = minutes * 1000

            o.add(uid, date, description, cost, minutes)
            print("Вы арендовали студию!")
        elif client_choice == "2":
            new_username = input("Введите новый логин: ")
            new_password = input("Введите новый пароль: ")

            new_data = {'username': new_username, 'password': new_password}
            u.update_user_data(uid, new_data)
            print("Данные пользователя были обновлены!")

        elif client_choice == "3":
            break

        else:
            print("Извините, укажите правильное значение")


def handle_admin_actions(u, a, o, s):
    while True:
        print("\nАдмин-панель:")
        print("1. Посмотреть всех пользователей")
        print("2. Обновить пользователя по ID")
        print("3. Удалить пользователя")
        print("4. Обновить аренду студии")
        print("5. Удалить аренду студии")
        print("6. Посмотреть все открытые студии")
        print("7. Добавить/открыть комнату студии")
        print("8. Обновить комнату студии")
        print("9. Удалить/закрыть комнату студии")
        print("10. Выйти")

        admin_choice = input(">> ")
        match admin_choice:
            case "1":
                admin_password = input("Введите мастер-пароль: ")
                print(u.read_users())
                break

            case "2":
                admin_password = input("Введите мастер-пароль: ")
                user_id = int(input("Введите ID пользователя: "))
                new_username = input("Введите новый логин: ")
                new_password = input("Введите новый пароль: ")

                new_data = {'username': new_username, 'password': new_password}
                a.update_user_data(u, admin_password, user_id, new_data)
                break
            case "3":
                admin_password = input("Введите мастер-пароль: ")
                user_id = int(input("Введите ID пользователя для удаления: "))
                a.delete_user(u, admin_password, user_id)
                break
            case "4":
                admin_password = input("Введите мастер-пароль: ")
                oid = int(input("Введите ID: "))
                new_date = input("Введите дату (ГГГГ-ММ-ДД): ")
                new_description = int(input("Введите изменения пожеланий к заказу: "))
                new_cost = float(input("Введите новую цену: "))
                new_minutes = int(input("Введите время(в минутах) на запись: "))

                a.update(o, admin_password, new_date, new_description, new_cost, new_minutes)
                print("Данные о аренде студии успешно изменены")
                break
            case "5":
                admin_password = input("Введите мастер-пароль: ")
                oid = int(input("Введите ID заказа для удаления: "))
                o.delete(oid)
                print("Аренда была успешно удалена")
                break
            case "6":
                print(s.read())
                break
            case "7":
                s_a = int(input("Введите id студии: "))
                s_b = input("Введите название студии: ")
                s_c = int(input("Введите номер комнаты студии: "))
                s_d = input("Введите микрофон в студии: ")
                s_e = input("Введите наушники в студии: ")
                s_f = input("Введите ПО в студии: ")
                s.add(s_a, s_b, s_c, s_d, s_e, s_f)
                break
            case "8":
                s_0 = int(input("Введите старый id студии: "))
                s_id = int(input("Введите новый id студии: "))
                s_name = input("Введите новое название студии: ")
                s_room = int(input("Введите новый номер комнаты студии: "))
                s_microphone = input("Введите обновленный микрофон в студии: ")
                s_headphones = input("Введите обновленные наушники в студии: ")
                s_software = input("Введите обновленное ПО в студии: ")
                s.update(s_0, s_id, s_name, s_room, s_microphone, s_headphones, s_software)
                print("Данные о студии успешно изменены!")
                break
            case "9":
                admin_password = input("Введите мастер-пароль: ")
                studid = input("Введите ID комнаты студии что надо удалить: ")
                s.delete(studid)
                break
            case "10":
                sys.exit(0)

            case _:
                print("Извините, введите корректное значение")


if __name__ == "__main__":
    main()