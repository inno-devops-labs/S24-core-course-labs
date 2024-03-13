"""
This module contains the API route for the current time in Moscow.
"""
from flask import Blueprint
from flasgger import swag_from
from api.model.time import TimeModel
from api.schema.time import TimeSchema

time_api = Blueprint('time_api', __name__)


@time_api.route('/', methods=['GET'])
@swag_from('swags/time.yml')
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
