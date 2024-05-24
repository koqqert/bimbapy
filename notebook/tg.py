import telebot

bot = telebot.TeleBot('6590499385:AAEeWl9P3UJ0w5sRF2Qc4d3PFSX3-nQgBmQ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, я твоя записная книжка. Напишите команду, которую хотите запустить.{message.chat.id}')

@bot.message_handler(commands=['write'])
def write(message):
    bot.send_message(message.chat.id, 'Напишите сообщение, которое хотите записать.')
    bot.register_next_step_handler(message, write_message)

bot.polling(none_stop=True)