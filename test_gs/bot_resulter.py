import os
from datetime import datetime
from typing import Tuple

import telebot
from dotenv import load_dotenv

from test_gs.currency_rate import currency
from test_gs.sheets import sheet

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
NUMBER, PRICE, DATE = sheet.get_last_row()


def get_params() -> Tuple[int, int, datetime]:
    number, price, date = sheet.get_last_row()
    return number, price, date


def is_delayed(table_time: str) -> bool:
    current_date = datetime.now()
    date_object = datetime.strptime(table_time, '%d.%m.%Y')
    return True if date_object < current_date else False


@bot.message_handler(commands=['start'])
def start_bot_process(message):
    """Запускаем работу бота. Отображение начального экрана бота."""
    number, price, date = get_params()
    bot.send_message(message.chat.id,
                     text=f'Привет, {message.from_user.first_name}!'
                          f'Последний заказ № {number}, {int(price) * currency.get_res()} до {date}',
                     )


bot.polling(none_stop=True)
