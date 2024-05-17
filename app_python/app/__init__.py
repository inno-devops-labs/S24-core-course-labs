from flask import Flask
from .routes.time_views import time_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    
    app.register_blueprint(time_blueprint)
    
    return app