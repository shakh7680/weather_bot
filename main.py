import logging
import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from data import config
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Ob-havo botga xush kelibsiz\n"
                        "Ob havoni bilish uchun shahar nomini kiriting")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Bu bot ob-havo bot")


@dp.message_handler()
async def weather(message: types.Message):
    city = message.text
    url = f'https://api.weatherapi.com/v1/forecast.json?key={config.API_KEY}&q={city}'
    res_from_url = requests.get(url).json()

    try:
        today_weather = res_from_url["current"]["temp_c"]
        response = f'Bugun {city.capitalize()}da havo harorati {today_weather}\u2103 daraja.'
    except:
        response = f'Bunday shahar mavjud emas'
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)