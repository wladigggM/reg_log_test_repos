import sqlite3 as sql
from users import Users


users_database = {}

# - - - - - - - - Функция для регистрации пользователей - - - - - - - - - - - - - - - - - - - - #
def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    searcher = cur.execute(f"""SELECT * FROM users WHERE username ='{username}' AND password = '{password}';""")
    if searcher.fetchone() is not None:
        return "Такой пользователь уже зарегистрирован!"
    else:
        users_database[username] = password
        print("Вы успешно зарегистрировались!")
        return users_database


# - - - - - - - - - Основная функция авторизации - - - - - - - - - - - - - - - - - - - - - - - - #
def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    searcher = cur.execute(f"""SELECT * FROM users WHERE username ='{username}' AND password = '{password}';""")
    if searcher.fetchone() is not None:
        return "Вы успешно авторизировались!"
    else:
        return "Неверный логин или пароль!"


# - - - - - - - - - Коннектор для работы с базой данных - - - - - - - - - - - - - - - - - - - - - #

with sql.connect('users.db') as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL);""")

    while True:
        choice = input("""
        Выберите действие:
    
    1.Регистрация
    2.Авторизация
    3.Выход
    4.Показать базу данных
    >""")
        if choice == "1":
            users_database.update(register())
            for username, password in users_database.items():
                user = Users(username, password)
                cur.execute(
                    f"INSERT INTO users (username, password) VALUES ('{user.user_name}','{user.user_password}')", )

        elif choice == "2":
            print(login())
        elif choice == "3":
            break
        elif choice == "4":
            sel = cur.execute("""
            SELECT * FROM users;""")
            for row in sel:
                print(row)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
