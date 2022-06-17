import logging
import sys
import time
from datetime import datetime
from typing import Optional, List, Tuple

import schedule

from test_gs.currency_rate import currency
from test_gs.db import db
from test_gs.exceptions import EmptySheet, WrongData
from test_gs.sheets import sheet


def get_last_row() -> List[int]:
    """Получение последней строки в google_sheets."""
    query = sheet.get_last_row()
    if query:
        return query
    else:
        logging.info(EmptySheet)


def check_bd() -> Optional[bool]:
    """Получаем состояние бд по уникальному номеру заказа. Сравниваем
    последнюю запись в google_sheets.
    """
    db.execute_query("SELECT number FROM orders")
    record = db.cur.fetchall()
    query = sheet.get_last_row()
    return True if (int(query[0]),) not in record else False


def validate_insert_items(number: int, price: float, date: datetime) -> Tuple[
        int, float, datetime]:
    """Валидация данных полученных из таблиц."""
    if isinstance(number, int) and isinstance(price, float) and isinstance(
            date, datetime):
        return number, price, date
    else:
        logging.info(WrongData)


def update_bd() -> None:
    """Добавление записи в бд. Каждая новая запись логируется."""
    query = get_last_row()
    date_object: datetime = datetime.strptime(str(query[2]), '%d-%m-%Y')
    if check_bd():
        insert_query = """ INSERT INTO orders (number, price, delivered_at) VALUES (%s, %s, %s)"""
        item_tuple = validate_insert_items(query[0],
                                           int(query[1]) * currency.get_res(),
                                           date_object)
        db.execute_query(insert_query, item_tuple)
        logging.info(f'Добавлена запись {int(query[0]),}')
    else:
        print('ничего нового')


def runer_update_bd(params: int) -> update_bd:
    """Запускает бесконечный цикл по обновлению таблицы и бд."""
    schedule.every(params).seconds.do(update_bd)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler(stream=sys.stdout)],
    )
    # Запуск скрипта по обновления страниц
    runer_update_bd(5)
