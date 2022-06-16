import time

import schedule

from test_gs.currency_rate import currency
from test_gs.db import db
from test_gs.sheets import sheet


def update_bd():
    """Получаем состояние бд по уникальному номеру заказа. Сравниваем последнюю запись в
    google_sheets. Если номера такого нет в бд, то добавляем, если нет, то продолжаем проверку.
    """
    db.cur.execute("SELECT number FROM orders")
    record = db.cur.fetchall()
    q = sheet.get_last_row()
    # date_object = datetime.strptime(str(q[2]), '%d-%m-%Y')
    # item_purchase_time = datetime.date(date_object)
    if (int(q[0]),) in record:
        print('Новых записей нет')
    else:
        table = f"INSERT INTO orders(number, price) VALUES ('{q[0]}', {int(q[1]) * currency.get_res()})"
        db.execute_query(table)
        print(f'Добавлена запись {int(q[0]),}')


def runer_update_bd(params: int) -> update_bd:
    """Запускает бесконечный цикл по обновлению таблицы и бд."""
    schedule.every(params).seconds.do(update_bd)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # Запуск скрипта по обновления страниц
    runer_update_bd(60)
