from flask import Flask
from .routes.time_views import time_blueprint
from .routes.metrics import metric_blueprint
from .routes.counts import _create_visit, count_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    _create_visit()
    
    app.register_blueprint(time_blueprint)
    app.register_blueprint(metric_blueprint)
    app.register_blueprint(count_blueprint)
    
    return app