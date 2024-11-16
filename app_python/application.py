from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Путь к файлу для хранения количества посещений
VISITS_FILE = "data/visits.txt"

# Убедитесь, что файл для подсчета посещений существует
os.makedirs("data", exist_ok=True)
if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as file:
        file.write("0")


@app.route('/')
def current_time():
    # Инкремент счетчика посещений
    with open(VISITS_FILE, "r+") as file:
        count = int(file.read().strip())
        count += 1
        file.seek(0)
        file.write(str(count))
        file.truncate()

    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')

    return render_template('current_time.html', current_time=current_time)


@app.route('/visits')
def visits():
    with open(VISITS_FILE, "r") as file:
        count = int(file.read().strip())
    return jsonify(visits=count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
