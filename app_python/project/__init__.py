import os
from flask import Flask


def create_app(templates_path: str = ''):
    template_dir = os.path.abspath(templates_path)

    if templates_path:
        app = Flask(__name__, template_folder=template_dir)
    else:
        app = Flask(__name__)

    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    return app
