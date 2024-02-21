from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def msc_time():
    msc = pytz.timezone('Europe/Moscow')
    cur_time = datetime.now(msc).strftime('%Y-%m-%d %H:%M:%S')
    return f"{cur_time}"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
