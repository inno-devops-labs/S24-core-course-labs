from flask import Flask, render_template
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)

def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time

if __name__ == '__main__':
    app.run(debug=True)