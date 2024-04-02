import telebot
import os
import webbrowser
from shutil import move
import time

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start', 'hello'])
def func_start(message):
    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name}, напишите команду, которую хотите запустить.')

@bot.message_handler(commands=['help']) #help
def help(message):
    bot.send_message(message.chat.id, f'для того, чтобы всё корректно работало нужно:  \n1.открытый Telegram на компьютере  \n2.корректный ввод  \n3.при работе с файлами указывать их расширение  \nдля предложений и вопросов писать @koqqert') 

@bot.message_handler(commands=['browser_youtube']) #открывает ютуб  1
def browser_youtube(message):
    bot.send_message(message.chat.id, 'открываю сайт YouTube')
    webbrowser.open('https://www.youtube.com/')

@bot.message_handler(commands=['browser_vk'])
def browser_youtube(message):
    bot.send_message(message.chat.id, 'открываю сайт VK') #открывает вк  2
    webbrowser.open('https://vk.com/feed')

@bot.message_handler(commands=['browser_telegram']) #открывает тг  3
def browser_youtube(message):
    bot.send_message(message.chat.id, 'открываю сайт Telegram Web')
    webbrowser.open('https://web.telegram.org/a/')

@bot.message_handler(commands=['search_folder']) #поиск папки  4
def search_folder_message(message):
    bot.send_message(message.chat.id, 'введите название папки')
    bot.register_next_step_handler(message, search_folder)
    return
def search_folder(message):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = message.text
    for root, dirs, files in os.walk(desktop_path):
        if folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            os.startfile(folder_path)
            bot.send_message(message.chat.id, f'папка {folder_name} найдена и открыта')
            break

@bot.message_handler(commands=['search_file']) #поиск файл  5
def search_file_message(message):
    bot.send_message(message.chat.id, 'введите название файла')
    bot.register_next_step_handler(message, search_file)
    return
def search_file(message):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = message.text
    print(file_name)
    for root, dirs, files in os.walk(desktop_path):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            os.startfile(file_path)
            bot.send_message(message.chat.id, f'файл {file_name} найден и открыт')
            break

@bot.message_handler(commands=['create_folder']) #создание папки  6 
def create_folder_message(message):
    global check_create_folder
    bot.send_message(message.chat.id, 'введите название папки')
    bot.register_next_step_handler(message, create_folder)
    return
def create_folder(message):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = message.text
    folder_path = os.path.join(desktop_path, folder_name)
    try:
        os.mkdir(folder_path)
        bot.send_message(message.chat.id, 'папка создана')
    except FileExistsError:
        bot.send_message(message.chat.id,"папка уже существует. Введите новое название или удалите старую.")

@bot.message_handler(commands=['del_file']) #удаление файла  7
def del_file_message(message):
    bot.send_message(message.chat.id, 'введите название файла')
    bot.register_next_step_handler(message, del_file)
    return
def del_file(message):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = message.text
    print(file_name)
    file_path = os.path.join(desktop_path, file_name)
    try:
        os.remove(file_path)
        bot.send_message(message.chat.id, f'файл {file_name} удален')
    except FileNotFoundError:
        bot.send_message(message.chat.id, "файл не существует или неправильно введено его название. Введите правильное название или создайте новый.")

@bot.message_handler(commands=['del_folder']) #удаление папки  8
def del_folder_message(message):
    bot.send_message(message.chat.id, 'введите название папки')
    bot.register_next_step_handler(message, del_folder)
    return
def del_folder(message):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = message.text
    folder_path = os.path.join(desktop_path, folder_name)
    try:
        os.rmdir(folder_path)
        bot.send_message(message.chat.id, f'папка {folder_name} удалена')
    except FileNotFoundError:
        bot.send_message(message.chat.id, "папка не существует или неправильно введено её название. Введите правильное название или создайте новую.")

@bot.message_handler(commands=['combo_command'])
def combo_command_message(message):
    global check_combo_command
    bot.send_message(message.chat.id, f'введите команды как числа через пробел: \n1 - открыть ютуб \n2 - открыть вк \n3 - открыть тг веб \n4 - создать папку \n5 - найти и открыть папку \n6 - удалить папку \n7 - удалить файл \n8 - найти и открыть файл \n9 - переместить файл в папку')
    bot.register_next_step_handler(message, combo_command)
    return
def combo_command(message):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    commands = message.text.split()
    print(commands)
    for command in commands:
        if command == '1':
            webbrowser.open('https://www.youtube.com/')
        elif command == '2':
            webbrowser.open('https://vk.com/')
        elif command == '3':
            webbrowser.open('https://web.telegram.org/#/login')
        elif command == '4': #найти и открыть папку
            bot.send_message(message.chat.id, 'введите название папки')
            time.sleep(5)
            bot.register_next_step_handler(message, search_folder_combo)
            return
        elif command == '5': #найти и открыть файл
            bot.send_message(message.chat.id, 'введите название файла')
            time.sleep(5)
            bot.register_next_step_handler(message, search_file_combo)
            return
        elif command == '6': #создание папки
            bot.send_message(message.chat.id, 'введите название папки')
            time.sleep(5)
            bot.register_next_step_handler(message, create_folder_combo)
            return
        elif command == '7': #удаление файла
            bot.send_message(message.chat.id, 'введите название файла')
            time.sleep(5)
            bot.register_next_step_handler(message, del_file_combo)
            return
        elif command == '8': #удаление папки
            bot.send_message(message.chat.id, 'введите название папки')
            time.sleep(5)
            bot.register_next_step_handler(message, del_folder_combo)
            return
        elif command == '9': #переместить файл в папку
            bot.send_message(message.chat.id, 'введите название файла')
            time.sleep(5)
            bot.register_next_step_handler(message, moving_file_combo)
            return
def search_folder_combo(message): #4
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = message.text
    for root, dirs, files in os.walk(desktop_path):
        if folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            os.startfile(folder_path)
            bot.send_message(message.chat.id, f'папка {folder_name} найдена и открыта')
            break

def search_file_combo(message): #5
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = message.text
    for root, dirs, files in os.walk(desktop_path):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            os.startfile(file_path)
            bot.send_message(message.chat.id, f'файл {file_name} найден и открыт')
            break

def create_folder_combo(message): #6
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = message.text
    folder_path = os.path.join(desktop_path, folder_name)
    try:
        os.mkdir(folder_path)
        bot.send_message(message.chat.id, f'папка {folder_name} создана')
    except FileExistsError:
        bot.send_message(message.chat.id, "папка уже существует. Введите новое название или удалите старую.")

def del_file_combo(message): #7
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = message.text
    file_path = os.path.join(desktop_path, file_name)
    try:
        os.remove(file_path)
        bot.send_message(message.chat.id, f'файл {file_name} удален')
    except FileNotFoundError:
        bot.send_message(message.chat.id, "файл не существует. Введите новое название или удалите старый.")

def del_folder_combo(message): #8
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = message.text
    folder_path = os.path.join(desktop_path, folder_name)
    try:
        shutil.rmtree(folder_path)
        bot.send_message(message.chat.id, f'папка {folder_name} удалена')
    except FileNotFoundError:
        bot.send_message(message.chat.id, "папка не существует. Введите новое название или удалите старую.")

@bot.message_handler(commands=['move_file']) #перемещение файлов
def moving_file_message(message):
    bot.send_message(message.chat.id, 'введите название файла')
    bot.register_next_step_handler(message, moving_file_message_check)
    return
@bot.message_handler(func=lambda message: check_moving_file ) #присвоение переменной file_message
def moving_file_message_check(message):
    global file_name, file_path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = message.text
    bot.send_message(message.chat.id, 'введите название папки')
    bot.register_next_step_handler(message, moving_folder_message_check)
    return

def moving_folder_message_check(message):
    global file_name, file_path
    folder_message = message.text
    print(folder_message)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, file_name)
    folder_path = os.path.join(desktop_path, folder_message)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    try:
        move(file_path, folder_path)
        bot.send_message(message.chat.id, f'файл {file_name} перемещен в папку {folder_message}')
    except FileNotFoundError:
        bot.send_message(message.chat.id,"папка уже существует или неправильно введено её название. Введите новое название или удалите старую папку.")


bot.polling(none_stop=True)