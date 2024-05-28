import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

bot = Bot('6793400912:AAG_0zDEB36_IUoSCagzeiJAMBzk_vL7C-Y')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Журнал', web_app=types.WebAppInfo(url='https://koqqert.pythonanywhere.com/')))
    await message.answer(f'Привет, {message.from_user.first_name}, напишите команду, которую хотите запустить.', reply_markup=markup)

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply(f"Я вас не понимаю.")

if __name__ == '__main__':
    asyncio.run(dp.start_polling())