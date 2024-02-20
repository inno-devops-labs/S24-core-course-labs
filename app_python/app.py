from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    time_now = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time_template.html', time_now=time_now)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
