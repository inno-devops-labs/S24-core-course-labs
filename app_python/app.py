from project import create_app
from flask import render_template

import datetime
import pytz


app = create_app(templates_path='project/templates')


@app.route('/time')
def get_time() -> str:
    # Retrieving Moscow timezone info
    timezone: datetime.tzinfo = pytz.timezone('Europe/Moscow')
    moscow_time: str = datetime.datetime.now(
        timezone
    ).strftime("%d %B, %H:%M:%S")
    return moscow_time


@app.route('/')
def home() -> str:
    # Home page that renders template file
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
