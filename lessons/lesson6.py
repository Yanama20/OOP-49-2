import sqlite3

connect = sqlite3.connect('Users.db')
cursor = connect.cursor()

def create_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
        )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades(
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson VARCHAR(100) NOT NULL,
    grade integer NOT NULL,
    userid INTEGER NOT NULL,
    FOREIGN KEY (userid) REFERENCES users(user_id)
    )
""")
connect.commit()
create_db()
#CRUD - Create ReadF  Update Delete

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO USERS(fio, age, hobby ) VALUES (?,?,?)', (fio, age, hobby))
    connect.commit()
    print(f'Пользователь {fio} дабвлен')

# add_user('Вася Пупкин', 25, 'Бегать')
# add_user('Илья Муромец', 26, 'Отжиматься')
# add_user('Johan Doe', 28, 'Спать')
# add_user('Дмитрий Бэйл', 23, 'Играть')


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print('Список всех пользователей')
        for user in users:
            print(f'ФИО: {user[0]}, ВОЗРАСТ: {user[1]}, ХОББИ: {user[2]}')
    else:
        print('Список пуст')


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

#lesson 7

def del_user_by_id(id):
    cursor.execute('DELETE FROM users WHERE user_id=?', (id,))
    connect.commit()
    print(f'Удалён пользователь с id = {id}')

# del_user_by_id(2)

def update_users_age_by_id(id, age):
    cursor.execute('UPDATE users SET age=? WHERE user_id=?', (age, id))
    connect.commit()
    print(f'Изменена информация о возрасте пользователя с  id = {id}')

# update_users_age_by_id(1, 20)

def add_grade(user_id, lesson, grade):
    cursor.execute(
        "INSERT INTO grades(userid, lesson, grade) VALUES (?,?,?)",
    )
    connect.commit()

add_grade(1, 'math', 5)
connect.close()