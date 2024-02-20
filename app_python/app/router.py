import logging

from .datetime_formatter import DateTimeFormatted
from flask import Blueprint, render_template
from .moscow_date_time import get_moscow_date_time

router = Blueprint('router', __name__)


@router.route('/')
@router.route('/index')
def display_date_time() -> str:
    logger = logging.getLogger(__name__)
    logger.debug('Handling request')
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
