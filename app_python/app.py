from flask import Flask, render_template
from prometheus_client import generate_latest
import datetime

import os

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "5000"))
VISITS_FILE = os.environ.get("VISITS_FILE", "data/visits.txt")


def increment_visits():
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())

    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))


def create_app():
    app = Flask(__name__)

    if not os.path.isfile(VISITS_FILE):
        parent_dir = os.path.join(VISITS_FILE, os.pardir)
        os.makedirs(os.path.abspath(parent_dir), exist_ok=True)

        with open(VISITS_FILE, "w") as file:
            file.write("0")

    @app.route('/', methods=["GET"])
    def template():
        increment_visits()
        msk_time = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=3))
        ).strftime('%d.%m.%y %H:%M:%S')

        print(f"datetime rendered is {msk_time}")

        return render_template(
            'index.html',
            time=msk_time
        )

    @app.route("/visits", methods=["GET"])
    def visits():
        with open(VISITS_FILE, "r") as file:
            return {"visits": int(file.read())}

    @app.route('/metrics', methods=["GET"])
    def metrics():
        return generate_latest()

    return app


wsgi_app = create_app()

if __name__ == '__main__':
    print(os.getcwd())
    wsgi_app.run(host=HOST, port=PORT)
