import logging

import prometheus_client
from datetime_formatter import DateTimeFormatted
from flask import Blueprint, Response, render_template
from moscow_date_time import get_moscow_date_time
from prometheus_client import Counter
from visits_counter import get_visits, increment_visit_counter

APP_NAME = 'app_python'
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
REQUEST_COUNT = Counter(
    'request_count',
    'App Request Count',
    ['app_name', 'method', 'endpoint', 'http_status'],
)

router = Blueprint('router', __name__)


@router.route('/')
@router.route('/index')
def display_date_time() -> str:
    logger = logging.getLogger(__name__)
    logger.debug('Handling request')
    REQUEST_COUNT.labels(
        app_name=APP_NAME, method='GET', endpoint='/', http_status='200'
    ).inc()
    increment_visit_counter()
    try:
        now = get_moscow_date_time()
        date_time: DateTimeFormatted = DateTimeFormatted.from_datetime(now)
        return render_template(
            'index.html',
            current_date=date_time.date,
            current_time=date_time.time,
        )
    except Exception as e:
        logger.error(
            f'Got error while handling request. Error: {e}', exc_info=True
        )
        return render_template(
            'index.html', current_date='N/A', current_time='N/A'
        )


@router.route('/metrics')
def metrics() -> str:
    REQUEST_COUNT.labels(
        app_name=APP_NAME, method='GET', endpoint='/metrics', http_status='200'
    ).inc()
    return Response(
        prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST
    )


@router.route('/visits')
def visits() -> str:
    REQUEST_COUNT.labels(
        app_name=APP_NAME, method='GET', endpoint='/visits', http_status='200'
    ).inc()
    return f'{get_visits()}'
