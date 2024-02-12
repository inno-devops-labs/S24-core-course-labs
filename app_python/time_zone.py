from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)


@app.route('/')
# Function which take MSK timezone
def msk_time():
    time = datetime.now(pytz.timezone('Europe/Moscow'))
    return time.strftime("Current time (MSK timezone): %H:%M:%S")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
