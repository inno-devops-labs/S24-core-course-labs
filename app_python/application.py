from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def current_time():

    # Getting current Moscow time
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    # Display current time on HTML document
    return render_template('current_time.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
