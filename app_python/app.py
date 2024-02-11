from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route('/')
def display_time():
    moscow_time = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=3)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('page.html', time=formatted_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
