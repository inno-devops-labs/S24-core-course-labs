from flask import Flask, render_template
from api.routes.home import home
from prometheus_flask_exporter import PrometheusMetrics

from api.services.moscow_time import get_current_moscow_time_str



app = Flask(__name__)
app.register_blueprint(home)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='2.0.0')

@app.route('/')
def current_moscow_time():
    cur_time_str = get_current_moscow_time_str()
    return render_template("current_moscow_time.html", time=cur_time_str)

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port
    
    app.run(host="0.0.0.0", port=port, debug=False)
