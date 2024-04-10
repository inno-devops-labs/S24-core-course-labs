from prometheus_flask_exporter import PrometheusMetrics
from flask import Blueprint
from app import metrics

metrics_api = Blueprint('metrics_api', __name__)
get_counter = metrics.counter('get_counter', 'Get Counter', labels={'method': lambda: request.method})

@metrics_api.route('/metrics')
@get_counter
