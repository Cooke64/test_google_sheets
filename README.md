# test_google_sheets
Срипт на языке python для работы с GoogleSheets

который будет выполнять следующие функции:
1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.» 
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме.
4. Выводит результат таблицы данных с использованием микрофреймворка Flask.
5. Отражает последний заказ в тг боте.
## Технлологии

- Flask
- GoogleSheets Api
- PostgreSql
- Psycopg2
- BS4
- Telebot
## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```git clone git@github.com:Cooke64/test_google_sheets.git```

Cоздать и активировать виртуальное окружение:

```python -m venv env```

```venv/scripts/activate```

При необходимости обновить pip

```python -m pip install --upgrade pip```

Установить зависимости из файла requirements.txt:

```pip install -r requirements.txt```

Выполнить миграции:

```python manage.py migrate```

Создать файл e.env, в котором необходимо создать переменные:

- API_TOKEN

Запустить срипт:
- для отображения всех записей в бд
```main.py```
-  для запуска скрипта
```crud.py```
- для запуска тг бота
```bot_resulter.py```

## Ссылка на документ [Google](https://docs.google.com/spreadsheets/d/1k3WrkkWd7jUzQ_-Cou3KoHg4T0L45XY_xCUhj8nglDA/edit#gid=0).
