import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS test(
    name text,
    age integer,
    address text
)
""")

date = 26.04       #обычные значения для проверки
name_column = 26.04
mark = 4
name = "Mike"

def add_column(date): #создать столбец в таблице
    c.execute(f"""ALTER TABLE test
            ADD COLUMN "{date}" integer NOT NULL DEFAULT 'нету'
    """)
    conn.commit()

def add_mark(name, name_column, mark): #добавлять значение в столбец
    c.execute(f"""UPDATE test SET "{name_column}" = "{mark}" WHERE name = '{name}'
    """)
    conn.commit()

conn.commit()
conn.close()