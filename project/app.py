from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Путь к файлу базы данных
db_file = 'journal.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tables')
def tables():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Получаем список таблиц, исключая sqlite_sequence
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()

    conn.close()
    
    tables_list = [table[0] for table in tables]
    return render_template('tables.html', tables=tables_list)

@app.route('/table/<table_name>')
def show_table(table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Получаем названия столбцов, исключая столбец id
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns_info = cursor.fetchall()
    col_names = [col[1] for col in columns_info if col[1] != 'id']

    # Получаем данные из таблицы, исключая столбец id
    cursor.execute(f"SELECT {', '.join(col_names)} FROM {table_name}")
    rows = cursor.fetchall()

    conn.close()

    return render_template('table.html', table_name=table_name, rows=rows, col_names=col_names)

if __name__ == '__main__':
    app.run(debug=True)
