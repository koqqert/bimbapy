from flask import Flask, render_template_string
import sqlite3
import telebot

app = Flask(__name__)

# Путь к файлу базы данных
db_file = 'journal.db'

@app.route('/')
def index():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Получаем список таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    conn.close()
    
    list_of_tables = """
        <h1>List of tables</h1>
        <ul>
            {% for table in tables %}
            <li><a href="/table/{{ table }}">{{ table }}</a></li>
            {% endfor %}
        </ul>
    """
    
    tables_list = [table[0] for table in tables]
    return render_template_string(list_of_tables, tables=tables_list)

@app.route('/table/<table_name>')
def show_table(table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Получаем данные из таблицы
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Получаем названия столбцов
    col_names = [description[0] for description in cursor.description]

    conn.close()

    table = """
        <h1>Table: {{ table_name }}</h1>
        <table border="1">
            <thead>
                <tr>
                    {% for col_name in col_names %}
                    <th>{{ col_name }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in rows %}
                <tr>
                    {% for cell in row %}
                    <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <a href="/">Back to tables list</a>
    """

    return render_template_string(table, table_name=table_name, rows=rows, col_names=col_names)
if __name__ == '__main__':
    app.run(debug=True)

