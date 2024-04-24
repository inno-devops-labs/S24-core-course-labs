from .counts import _increment_visits
from flask import Blueprint, Response


health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health')
def health():
    _increment_visits()
    return Response(status=200)