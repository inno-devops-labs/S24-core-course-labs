import logging
from dataclasses import dataclass
from datetime import datetime

import pytz
from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

# Logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass
class DateTimeFormatted:
    date: str
    time: str

    @staticmethod
    def from_datetime(date_time: datetime) -> 'DateTimeFormatted':
        return DateTimeFormatted(
            date_time.strftime('%B %d, %Y'), date_time.strftime('%H:%M:%S')
        )


class Router:
    @app.route('/')
    @app.route('/index')
    def display_date_time() -> str:
        logger.debug('Handling request')
        try:
            utc_now = datetime.utcnow()
            moscow_tz = pytz.timezone('Europe/Moscow')
            now: datetime = utc_now.replace(tzinfo=pytz.utc).astimezone(
                moscow_tz
            )

            date_time: DateTimeFormatted = DateTimeFormatted.from_datetime(now)

            return render_template(
                'index.html',
                current_date=date_time.date,
                current_time=date_time.time,
            )
        except Exception as e:
            logging.error(
                f'Got error while handling request. Error: {e}', exc_info=True
            )
            return render_template(
                'index.html', current_date='N/A', current_time='N/A'
            )


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
