from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)


@app.route('/msk_timezone')
def msk_timezone():
    time = datetime.now(pytz.timezone('Europe/Moscow'))
    return time.strftime("Current time (MSK timezone): %H:%M:%S")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
