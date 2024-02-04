from flask import Flask, render_template
from datetime import datetime, timezone
import pytz

app = Flask(__name__)


def get_current_time():
    gmt_time = datetime.now(timezone.utc)

    gmt3_timezone = pytz.timezone('Etc/GMT-3')
    gmt3_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(gmt3_timezone)

    return gmt3_time.strftime('%H:%M:%S')


@app.route('/')
def index():
    current_time = get_current_time()
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
