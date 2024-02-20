from datetime import datetime

import pytz
from flask import Flask, render_template

app = Flask(__name__)

timezone_country = 'Europe/Moscow'


@app.route('/')
def display_time():
    return render_template('index.html',
                           current_time=get_time('Europe/Moscow'), country=timezone_country)


def get_time(timezone_name):
    timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    return current_time


if __name__ == '__main__':
    app.run()
