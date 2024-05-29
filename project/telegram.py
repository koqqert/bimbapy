from dotenv import load_dotenv
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


@bot.message_handler(commands=['add_day'])
def ask_for_day(message):
    bot.send_message(message.chat.id,'Какой столбец вы хотите добавить?(пример: д010924)')
    bot.register_next_step_handler(message, process_day)
def process_day(message):
    day = message.text
    bot.send_message(message.chat.id,f'{day}')

    conn = sqlite3.connect('project\journal.db')
    c = conn.cursor()

    c.execute("PRAGMA table_info(journal)")
    columns = [column[1] for column in c.fetchall()]

    if day in columns:
        bot.send_message(message.chat.id, f"Столбец '{day}' уже существует.")
    else:
        try:
            c.execute(f"ALTER TABLE journal ADD COLUMN '{day}' string NOT NULL DEFAULT '-'")
            conn.commit()
            bot.send_message(message.chat.id, f"Вы успешно добавили столбец '{day}' в таблицу.")
        except sqlite3.OperationalError as e:
            bot.send_message(message.chat.id, f"Ошибка при добавлении столбца: {e}")
    
    conn.close()

@bot.message_handler()
def answer(message):
    bot.reply_to(message.chat.id,f"Я вас не понимаю.")

bot.polling(none_stop=True)