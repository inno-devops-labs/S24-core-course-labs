from flask import Flask
from api.routes.home import home
from prometheus_flask_exporter import PrometheusMetrics

from api.routes.visits import visits


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(visits)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='2.0.0')

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port
    
    app.run(host="0.0.0.0", port=port, debug=False)
