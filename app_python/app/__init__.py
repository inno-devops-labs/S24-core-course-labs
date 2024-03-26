from flask import Flask
from .routes.time_views import time_blueprint
from .routes.metrics import metric_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    
    app.register_blueprint(time_blueprint)
    app.register_blueprint(metric_blueprint)
    
    return app