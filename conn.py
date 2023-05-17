import sqlite3

db = sqlite3.connect("2.db")
sql = db.cursor()
db.commit()


succes = 0

def reg(login, firstname,secondname,email, password):
    global succes

    sql.execute(f"SELECT login, password FROM users WHERE login = '{login}' ")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users (login, password, 'e-mail', firstname, secondname) VALUES ('{login}', '{firstname}', '{secondname}', '{email}', '{password}');")
        db.commit()
        print('Успешно!')
        succes = 1
    else:
        print('Такая запись уже существует')
        succes = 0

def login(username, password):
    global succes
    a = sql.execute(f"SELECT login, password FROM users WHERE login = '{username}' AND password = '{password}'")
    db.commit() 
    if not sql.fetchone():
        print("Нет такой записи")
        for i in sql.execute('SELECT * FROM users'):
            print(i)
        succes = 0
    else:
        print('Welcome')
        succes = 1
    

def curent():
    return succes
    
