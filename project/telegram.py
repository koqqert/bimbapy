import os
import sqlite3
import telebot

bot = telebot.TeleBot('6793400912:AAG_0zDEB36_IUoSCagzeiJAMBzk_vL7C-Y')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_info = telebot.types.WebAppInfo('https://koqqert.pythonanywhere.com/')
    btn = telebot.types.KeyboardButton('Журнал', web_app=web_info)
    markup.add(btn)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, напишите команду, которую хотите запустить.', reply_markup=markup)
    

@bot.message_handler(commands=['add_date'])
def ask_for_day(message):
    bot.send_message(message.chat.id,'Какой дату вы хотите добавить?(пример: д010924)')
    bot.register_next_step_handler(message, process_day)
def process_day(message):
    day = message.text
    bot.send_message(message.chat.id,f'{day}')
    conn = sqlite3.connect('project\journal.db') #подключение к базе
    c = conn.cursor()
    c.execute("PRAGMA table_info(journal)")
    columns = [column[1] for column in c.fetchall()]

    if day in columns:
        bot.send_message(message.chat.id, f"Дата '{day}' уже существует.")
    else:
        try:
            c.execute(f"ALTER TABLE journal ADD COLUMN '{day}' string NOT NULL DEFAULT '-'")
            conn.commit()
            bot.send_message(message.chat.id, f"Вы успешно добавили дату '{day}' в таблицу.")
        except sqlite3.OperationalError as e:
            bot.send_message(message.chat.id, f"Ошибка при добавлении даты: {e}")
    
    conn.close()

@bot.message_handler(commands=['add_mark'])
def ask_for_add_mark(message):
    bot.send_message(message.chat.id,'Кому вы хотите добавить оценку?(пример: Иванов И.И.)')
    bot.register_next_step_handler(message, process_name)
def process_name(message):
    name = message.text
    bot.send_message(message.chat.id,'На какое число вы хотите добавить оценку?(пример: д010924)')
    bot.register_next_step_handler(message, lambda m: process_day(m, name))
def process_day(message,name):
    day = message.text
    bot.send_message(message.chat.id,'Какую оценку вы хотите добавить?(пример: 5)')
    bot.register_next_step_handler(message, lambda m: process_add_mark(m, name, day))
def process_add_mark(message, name, day):
    mark = message.text
    conn = sqlite3.connect('project\journal.db') #подключение к базе
    c = conn.cursor()
    c.execute(f"UPDATE journal SET '{day}' = '{mark}' WHERE name = '{name}'")
    conn.commit()
    bot.send_message(message.chat.id, f"Вы успешно добавили пользователю {name} оценку {mark} на число {day}")

    conn.close()
@bot.message_handler(commands=['rename_date'])
def ask_for_rename(message):
    bot.send_message(message.chat.id,'Какую дату вы хотите переименовать?(пример: д010924)')
    bot.register_next_step_handler(message, process_get_date)
def process_get_date(message,):
    date_for_rename = message.text
    bot.send_message(message.chat.id,'Введите новое название даты?(пример: д020924)')
    bot.register_next_step_handler(message, lambda m: process_rename_date(m, date_for_rename))
def process_rename_date(message, date_for_rename):
    new_date = message.text
    conn = sqlite3.connect('project\journal.db') #подключение к базе
    c = conn.cursor()
    c.execute(f"ALTER TABLE journal RENAME COLUMN '{date_for_rename}' TO '{new_date}'")
    conn.commit()
    bot.send_message(message.chat.id, f"Вы успешно переименовали дату {date_for_rename} на {new_date}")
    conn.close()

@bot.message_handler(commands=['delete_date'])
def ask_for_delete(message):
    bot.send_message(message.chat.id,'Какую дату вы хотите удалить?(пример: д010924)')
    bot.register_next_step_handler(message, process_get_date)
def process_get_date(message,):
    date_for_delete = message.text
    conn = sqlite3.connect('project\journal.db') #подключение к базе
    c = conn.cursor()
    c.execute(f"ALTER TABLE journal DROP COLUMN '{date_for_delete}'")
    conn.commit()
    bot.send_message(message.chat.id, f"Вы успешно удалили дату {date_for_delete}")

    conn.close()

@bot.message_handler(commands=['delete_mark'])
def ask_for_delete_mark(message):
    bot.send_message(message.chat.id,'У кого вы хотите удалить оценку?(пример: Иванов И.И.)')
    bot.register_next_step_handler(message, process_get_name)
def process_get_name(message):
    name = message.text
    bot.send_message(message.chat.id,'В какое число вы хотите удалить оценку?(пример: д010924)')
    bot.register_next_step_handler(message, lambda m: process_get_date(m, name))
def process_get_date(message, name):
    date_for_delete = message.text
    conn = sqlite3.connect('project\journal.db') #подключение к базе
    c = conn.cursor()
    c.execute(f"UPDATE journal SET '{date_for_delete}' = '-' WHERE name = '{name}'")
    conn.commit()
    bot.send_message(message.chat.id, f"Вы успешно удалили оценку пользователя {name} на дату {date_for_delete}")
    conn.close()

@bot.message_handler()
def answer(message):
    bot.reply_to(message.chat.id,f"Я вас не понимаю.")

bot.polling(none_stop=True)