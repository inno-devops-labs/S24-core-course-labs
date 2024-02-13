from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def display_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time)


if __name__ == '__main__':
    print("The server is hosting on http://127.0.0.1:5001")
    app.run(host="0.0.0.0", port=5001)
