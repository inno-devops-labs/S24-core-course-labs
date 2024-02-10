from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


def getMoscowTime(timezone='Europe/Moscow'):
    moscow_tz = pytz.timezone(timezone)
    return datetime.now(moscow_tz).strftime('%H:%M:%S')


@app.route('/')
def show_time():
    return render_template('time.html', time_in_moscow=getMoscowTime('Europe/Moscow'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
