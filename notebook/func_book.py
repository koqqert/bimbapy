import sqlite3

def create_db():
    name_db = 'tg' + message.from_user.first_name + '.db'
    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()
    c.execute(f"""CREATE TABLE IF NOT EXISTS {name_db}(
        date string,
        time string,
        message string
    )
    """)