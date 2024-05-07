import sqlite3

conn = sqlite3.connect('journal.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS journal(
    id integer primary key autoincrement,
    name text,
    "01.09.24" integer NOT NULL DEFAULT '-'
)
""")
#обычные значения для проверки
name_column = "д050524"
rename_column = "03.09.24"
mark = 5
name = "ученик3"
name_id = 4
t ='.'

def add_column(name_column): #создать столбец в таблице
    c.execute(f"ALTER TABLE journal ADD COLUMN '{name_column}' string NOT NULL DEFAULT '-'")
    conn.commit()
# add_column(name_column)

def add_mark(name, name_column, mark, name_id): #добавлять значение в столбец
    c.execute(f"UPDATE journal SET '{name_column}' = '{mark}' WHERE id = '{name_id}'")
    conn.commit()
    print(f"Вы успешно добавили пользователю {name} оценку {mark} на число {name_column}")
# add_mark(name, name_column, mark, name_id)

def get_mark_all(*args): #получить все значения из строки
    c.execute(f"SELECT * FROM journal WHERE id = '{name_id}'")
    marks = c.fetchone()[2:]
    c.execute(f"SELECT name FROM journal WHERE id = '{name_id}'")
    name = c.fetchall().pop()[0]
    conn.commit()
    return print(f"{name}: " + ','.join(map(str, marks))) 
# get_mark_all()

def get_mark_day(name, name_column, name_id,t): #получить значение из столбца в опред. день
    c.execute(f"SELECT {name_column} FROM journal WHERE name = '{name}'")
    mark = c.fetchone()[0]
    conn.commit()
    return print(f"Оценка {name} на {name_column[1:3]+t+name_column[3:5]+t+name_column[5:7]} = {mark}") #не работает с опред. символами. обязательно писать в начале букву
# get_mark_day(name, name_column, name_id,t)

conn.commit()
conn.close()