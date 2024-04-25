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
name_column = "02.09.24"
rename_column = "03.09.24"
mark = 4
name = "артем"
name_id = 1

def add_column(name_column): #создать столбец в таблице
    c.execute(f"ALTER TABLE journal ADD COLUMN '{name_column}' integer NOT NULL DEFAULT '-'")
    conn.commit()
# add_column(name_column)

def add_mark(name, name_column, mark): #добавлять значение в столбец
    c.execute(f"UPDATE journal SET '{name_column}' = '{mark}' WHERE id = '{name_id}'")
    conn.commit()
# add_mark(name, name_column, mark)

def get_mark_all(*args): #получить все значения из строки
    c.execute(f"SELECT * FROM journal WHERE id = '{name_id}'")
    marks = c.fetchone()[2:]
    return print(''.join(map(str, marks)))
# get_mark_all()

def get_mark_day(name, name_column): #получить значение из столбца в опред. день
    c.execute(f"SELECT '{name_column}' FROM journal WHERE id = '{name_id}'")
    mark = c.fetchall().pop()[0]
    return print(mark)
# get_mark(name, name_column)

conn.commit()
conn.close()