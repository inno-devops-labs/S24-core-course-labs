from flask import Flask, render_template
import pytz
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    # get time in Moscow time zone
    msk_time = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', msk_time=msk_time)


if __name__ == '__main__':
    app.run(debug=True)
