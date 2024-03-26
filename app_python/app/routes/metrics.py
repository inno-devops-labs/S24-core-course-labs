from flask import Blueprint, Response
from prometheus_client import generate_latest

metric_blueprint = Blueprint('metrics', __name__)

@metric_blueprint.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')