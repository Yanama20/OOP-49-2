import sqlite3

connect = sqlite3.connect('Users.db')
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    fio VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
""")

#CRUD - Create ReadF  Update Delete

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO USERS(fio, age, hobby ) VALUES (?,?,?)', (fio, age, hobby))
    connect.commit()
    print(f'Пользователь {fio} дабвлен')

# add_user('Вася Пупкин', 25, 'Бегать')

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print('Список всех пользователей')
        for user in users:
            print(f'ФИО: {user[0]}, ВОЗРАСТ: {user[1]}, ХОББИ: {user[2]}')
    else:
        print('Список пуст')

def del_user(fio):
    cursor.execute('DELETE FROM users WHERE fio=?', (fio,))
    connect.commit()

def get_user_by_name(fio):
    cursor.execute('SELECT * FROM users WHERE fio=?', (fio,))
    users = cursor.fetchall()
    if users:
        print('Список пользователей с заданным ФИО:')
        for user in users:
            print(f'ФИО: {user[0]}, ВОЗРАСТ: {user[1]}, ХОББИ: {user[2]}')
    else:
        print('Нет пользователя с таким ФИО.')

def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age=?', (age,))
    users = cursor.fetchall()
    if users:
        print('Список пользователей с заданным возрастом:')
        for user in users:
            print(f'ФИО: {user[0]}, ВОЗРАСТ: {user[1]}, ХОББИ: {user[2]}')
    else:
        print('Нет пользователя с таким возрастом.')

get_user_by_age(25)

connect.close()