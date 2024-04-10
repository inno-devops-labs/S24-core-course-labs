"""
This module contains the Flask application that
displays the current time in Moscow
"""
from flask import Flask, Blueprint
from flasgger import Swagger,swag_from
from prometheus_flask_exporter import PrometheusMetrics
from api.model.time import TimeModel
from api.schema.time import TimeSchema

app = Flask(__name__)
swagger = Swagger(app)
metrics = PrometheusMetrics(app)


time_api = Blueprint('time_api', __name__)


@time_api.route('/', methods=['GET'])
@swag_from('swags/time.yml')
@metrics.counter('api_counter', 'API counter', labels={'method': 'display_time'})
def display_time():
    """
    Get the current time in Moscow
    ---
    responses:
      200:
        description: The current time in Moscow
        schema:
          type: string
          format: time
    """
    result = TimeModel()
    return TimeSchema().dump(result), 200


app.register_blueprint(time_api, url_prefix='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
