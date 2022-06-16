import psycopg2
import psycopg2 as pg2


class Database:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.cur = None
        self.conn = None
        self.port = port

    def connect(self):
        """Создаем подключение к бд и объект курсор."""
        self.conn = pg2.connect(
            database=self.database, user=self.user,
            password=self.password, host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()

    def execute_query(self, query):
        """Выполнение crud."""
        try:
            self.cur.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.Error) as error:
            print("Произошла ошибка при подключении.", error)

    def close(self):
        """Закрытие бд."""
        self.cur.close()
        self.conn.close()


USER = 'postgres'
PASSWORD = '12345678'
HOST = '127.0.0.1'
PORT = '5432'
DATABASE = 'test_google'

db = Database(
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE
)


table = (
    'CREATE TABLE IF NOT EXISTS orders'
    '(id serial PRIMARY KEY,'
    'number integer NOT NULL,'
    'price float NOT NULL,'
    'purchase_time date DEFAULT CURRENT_DATE);'
)

db.connect()
db.execute_query(table)
