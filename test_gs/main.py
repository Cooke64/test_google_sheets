from typing import Dict, Any

from flask import Flask

from test_gs.db import db

app = Flask(__name__)


@app.route('/')
def get_result_page() -> Dict[str, Any]:
    """Главная страница с отображением всех данных в таблице."""
    db.cur.execute("SELECT * FROM orders")
    record = db.cur.fetchall()
    return {"record": record}


if __name__ == '__main__':
    app.run(debug=True)
