from flask import Flask
from api.routes.home import home
from prometheus_flask_exporter import PrometheusMetrics


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    return app


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()
    metrics = PrometheusMetrics(app)
    metrics.info('app_info', 'Application info', version='2.0.0')
    app.run(host="0.0.0.0", port=port, debug=True)
