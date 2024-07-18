from aiogram import Bot,Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo
from os import getenv
import sys
from dotenv import load_dotenv
import logging
load_dotenv()
TOKEN = getenv('BOT_TOKEN')

bot = Bot(TOKEN)
dp =Dispatcher(bot)
my = 'mybots123'

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Bosh sahifa', web_app=WebAppInfo(url='https://nkurs.pythonanywhere.com/'))
    button2 = types.KeyboardButton('Kurslar', web_app=WebAppInfo(url='https://nkurs.pythonanywhere.com/courses/'))
    button3 = types.KeyboardButton('saqlangan kurslar',web_app=WebAppInfo(url='https://nkurs.pythonanywhere.com/saveds/'))
    button4 = types.KeyboardButton('sertifikatlarim',web_app=WebAppInfo(url='https://nkurs.pythonanywhere.com/mening/serftifikatlarim/'))
    keyboard.add(button1, button2,button3,button4)
    await message.answer('Salom Ncouse Botiga xush kelibsiz',reply_markup=keyboard)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler('bot.log'),
                            logging.StreamHandler(sys.stdout)
                        ]
                        )
    executor.start_polling(dp)