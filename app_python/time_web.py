from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def get_time():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Moscow is: {moscow_time}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
