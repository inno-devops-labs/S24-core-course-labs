"""
This module contains the Flask application that
displays the current time in Moscow
"""
from flask import Flask
from flasgger import Swagger
from api.route.time import time_api

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(time_api, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
