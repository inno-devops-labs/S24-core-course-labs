# app.py
import pytz as pytz
from flask import Flask, render_template
import datetime


app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=current_time)


if __name__ == '__main__':
    app.run(debug=True)