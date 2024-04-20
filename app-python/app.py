import datetime
import logging
import os
from flask import Flask, render_template, redirect, url_for

COUNTER_PATH = "data/visit_count.txt"

app = Flask(__name__, template_folder="./app_templates")

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')



def visit():
    with open(COUNTER_PATH, "r") as file:
        visits = int(file.read()) + 1

    with open(COUNTER_PATH, "w") as file:
        file.write(str(visits))

    logging.info(f"New count set to {visits}")
    return visits


def store_count():
    if os.path.isfile(COUNTER_PATH):
        logging.info("File already exists - skipping")
        return

    with open(COUNTER_PATH, "w+") as file:
        file.write(str(0))

    logging.info("File `visit_count.txt` created")


@app.route('/')
def display_time():
    try:
        visit()
        moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
        logging.info("Displayed Moscow time: %s", formatted_time)
        logging.info("Custom log message")

        return render_template('index.html', time=formatted_time)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return redirect(url_for('error'))


@app.route('/error')
def handle_error():
    return render_template('error.html')

@app.route('/visits')
def display_visits():
    with open(COUNTER_PATH, "r") as file:
        visits = int(file.read())
        logging.info("Displayed visit count: %d", visits)
        return f"Number of visits: {visits}"

if __name__ == '__main__':
    store_count()
    app.run(host='0.0.0.0')
