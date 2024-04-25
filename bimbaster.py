import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для подключения к базе данных
def connect_to_database():
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        id INTEGER PRIMARY KEY,
                        student_name TEXT NOT NULL,
                        subject TEXT NOT NULL,
                        grade INTEGER NOT NULL
                    )''')
    conn.commit()
    return conn, cursor

# Функция для добавления оценки
def add_grade(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 3:
        update.message.reply_text("Используйте команду в формате /add_grade <Имя ученика> <Предмет> <Оценка>")
        return
    student_name, subject, grade = args
    try:
        grade = int(grade)
    except ValueError:
        update.message.reply_text("Оценка должна быть числом")
        return

    conn, cursor = connect_to_database()
    cursor.execute("INSERT INTO grades (student_name, subject, grade) VALUES (?, ?, ?)", (student_name, subject, grade))
    conn.commit()
    update.message.reply_text("Оценка успешно добавлена")

# Функция для отправки оценок ученикам
def send_grades(update: Update, context: CallbackContext):
    student_name = update.message.from_user.username  # Получаем имя пользователя Telegram
    conn, cursor = connect_to_database()
    cursor.execute("SELECT subject, grade FROM grades WHERE student_name=?", (student_name,))
    grades = cursor.fetchall()
    if not grades:
        update.message.reply_text("У вас пока нет оценок")
        return
    message = "Ваши оценки:\n"
    for subject, grade in grades:
        message += f"{subject}: {grade}\n"
    update.message.reply_text(message)

# Функция для редактирования оценки (для учителя)
def edit_grade(update: Update, context: CallbackContext):
    # Реализуйте эту функцию с учетом ваших потребностей
    pass

# Функция для отправки таблицы оценок учителю
def send_grades_to_teacher(update: Update, context: CallbackContext):
    # Реализуйте эту функцию с учетом ваших потребностей
    pass

# Основная функция для запуска бота
def main():
    updater = Updater("YOUR_BOT_TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("add_grade", add_grade))
    dp.add_handler(CommandHandler("send_grades", send_grades))
    dp.add_handler(CommandHandler("edit_grade", edit_grade))
    dp.add_handler(CommandHandler("send_grades_to_teacher", send_grades_to_teacher))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
