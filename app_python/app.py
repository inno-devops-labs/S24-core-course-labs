import datetime
import logging
from flask import Flask, render_template

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def display_time():
    try:
        moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
        logging.info("Displayed Moscow time: %s", formatted_time)
        logging.info("Custom log message")

        return render_template('index.html', time=formatted_time)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
