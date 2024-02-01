from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)


@app.route('/')
def msk_time():
    mskTime = datetime.now(pytz.timezone('Europe/Moscow'))
    return mskTime.strftime('Current time in Moscow: %H:%M:%S')


if __name__ == '__main__':
    app.run(debug=True)
